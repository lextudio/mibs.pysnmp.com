# SNMP MIB module (IPSEC-IPSECACTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPSEC-IPSECACTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:10 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(IfDirection,) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IfDirection")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SpdAdminStatus,
 SpdIPPacketLogging,
 spdActions) = mibBuilder.importSymbols(
    "IPSEC-SPD-MIB",
    "SpdAdminStatus",
    "SpdIPPacketLogging",
    "spdActions")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ipsaMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 1)
)
ipsaMIB.setRevisions(
        ("2006-10-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IpsecDoiEncapsulationMode(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IpsecDoiIpcompTransform(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class IpsecDoiAuthAlgorithm(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IpsecDoiEspTransform(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class IpsecDoiIdentType(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class IpsaCredentialType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("kerberos", 4),
          ("reserved", 0),
          ("sharedSecret", 2),
          ("unknown", 1),
          ("x509", 3))
    )



class IpsaIdentityFilter(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )



# MIB Managed Objects in the order of their OIDs

_IpsaConfigObjects_ObjectIdentity = ObjectIdentity
ipsaConfigObjects = _IpsaConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1)
)
_IpsaSaPreconfiguredActionTable_Object = MibTable
ipsaSaPreconfiguredActionTable = _IpsaSaPreconfiguredActionTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipsaSaPreconfiguredActionTable.setStatus("current")
_IpsaSaPreconfiguredActionEntry_Object = MibTableRow
ipsaSaPreconfiguredActionEntry = _IpsaSaPreconfiguredActionEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1)
)
ipsaSaPreconfiguredActionEntry.setIndexNames(
    (0, "IPSEC-IPSECACTION-MIB", "ipsaSaPreActActionName"),
    (0, "IPSEC-IPSECACTION-MIB", "ipsaSaPreActSADirection"),
)
if mibBuilder.loadTexts:
    ipsaSaPreconfiguredActionEntry.setStatus("current")


class _IpsaSaPreActActionName_Type(SnmpAdminString):
    """Custom type ipsaSaPreActActionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpsaSaPreActActionName_Type.__name__ = "SnmpAdminString"
_IpsaSaPreActActionName_Object = MibTableColumn
ipsaSaPreActActionName = _IpsaSaPreActActionName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 1),
    _IpsaSaPreActActionName_Type()
)
ipsaSaPreActActionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsaSaPreActActionName.setStatus("current")
_IpsaSaPreActSADirection_Type = IfDirection
_IpsaSaPreActSADirection_Object = MibTableColumn
ipsaSaPreActSADirection = _IpsaSaPreActSADirection_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 2),
    _IpsaSaPreActSADirection_Type()
)
ipsaSaPreActSADirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsaSaPreActSADirection.setStatus("current")
_IpsaSaPreActActionDescription_Type = SnmpAdminString
_IpsaSaPreActActionDescription_Object = MibTableColumn
ipsaSaPreActActionDescription = _IpsaSaPreActActionDescription_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 3),
    _IpsaSaPreActActionDescription_Type()
)
ipsaSaPreActActionDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActActionDescription.setStatus("current")


class _IpsaSaPreActActionLifetimeSec_Type(Unsigned32):
    """Custom type ipsaSaPreActActionLifetimeSec based on Unsigned32"""
    defaultValue = 28800


_IpsaSaPreActActionLifetimeSec_Object = MibTableColumn
ipsaSaPreActActionLifetimeSec = _IpsaSaPreActActionLifetimeSec_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 4),
    _IpsaSaPreActActionLifetimeSec_Type()
)
ipsaSaPreActActionLifetimeSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActActionLifetimeSec.setStatus("current")
if mibBuilder.loadTexts:
    ipsaSaPreActActionLifetimeSec.setUnits("seconds")


class _IpsaSaPreActActionLifetimeKB_Type(Unsigned32):
    """Custom type ipsaSaPreActActionLifetimeKB based on Unsigned32"""
    defaultValue = 0


_IpsaSaPreActActionLifetimeKB_Object = MibTableColumn
ipsaSaPreActActionLifetimeKB = _IpsaSaPreActActionLifetimeKB_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 5),
    _IpsaSaPreActActionLifetimeKB_Type()
)
ipsaSaPreActActionLifetimeKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActActionLifetimeKB.setStatus("current")


class _IpsaSaPreActDoActionLogging_Type(TruthValue):
    """Custom type ipsaSaPreActDoActionLogging based on TruthValue"""


_IpsaSaPreActDoActionLogging_Object = MibTableColumn
ipsaSaPreActDoActionLogging = _IpsaSaPreActDoActionLogging_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 6),
    _IpsaSaPreActDoActionLogging_Type()
)
ipsaSaPreActDoActionLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActDoActionLogging.setStatus("current")


class _IpsaSaPreActDoPacketLogging_Type(SpdIPPacketLogging):
    """Custom type ipsaSaPreActDoPacketLogging based on SpdIPPacketLogging"""
    defaultValue = -1


_IpsaSaPreActDoPacketLogging_Object = MibTableColumn
ipsaSaPreActDoPacketLogging = _IpsaSaPreActDoPacketLogging_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 7),
    _IpsaSaPreActDoPacketLogging_Type()
)
ipsaSaPreActDoPacketLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActDoPacketLogging.setStatus("current")


class _IpsaSaPreActDFHandling_Type(Integer32):
    """Custom type ipsaSaPreActDFHandling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("copy", 1),
          ("set", 2))
    )


_IpsaSaPreActDFHandling_Type.__name__ = "Integer32"
_IpsaSaPreActDFHandling_Object = MibTableColumn
ipsaSaPreActDFHandling = _IpsaSaPreActDFHandling_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 8),
    _IpsaSaPreActDFHandling_Type()
)
ipsaSaPreActDFHandling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActDFHandling.setStatus("current")


class _IpsaSaPreActActionType_Type(IpsecDoiEncapsulationMode):
    """Custom type ipsaSaPreActActionType based on IpsecDoiEncapsulationMode"""
    defaultValue = 1


_IpsaSaPreActActionType_Object = MibTableColumn
ipsaSaPreActActionType = _IpsaSaPreActActionType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 9),
    _IpsaSaPreActActionType_Type()
)
ipsaSaPreActActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActActionType.setStatus("current")
_IpsaSaPreActAHSPI_Type = Integer32
_IpsaSaPreActAHSPI_Object = MibTableColumn
ipsaSaPreActAHSPI = _IpsaSaPreActAHSPI_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 10),
    _IpsaSaPreActAHSPI_Type()
)
ipsaSaPreActAHSPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActAHSPI.setStatus("current")


class _IpsaSaPreActAHTransformName_Type(SnmpAdminString):
    """Custom type ipsaSaPreActAHTransformName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpsaSaPreActAHTransformName_Type.__name__ = "SnmpAdminString"
_IpsaSaPreActAHTransformName_Object = MibTableColumn
ipsaSaPreActAHTransformName = _IpsaSaPreActAHTransformName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 11),
    _IpsaSaPreActAHTransformName_Type()
)
ipsaSaPreActAHTransformName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActAHTransformName.setStatus("current")


class _IpsaSaPreActAHSharedSecretName_Type(SnmpAdminString):
    """Custom type ipsaSaPreActAHSharedSecretName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpsaSaPreActAHSharedSecretName_Type.__name__ = "SnmpAdminString"
_IpsaSaPreActAHSharedSecretName_Object = MibTableColumn
ipsaSaPreActAHSharedSecretName = _IpsaSaPreActAHSharedSecretName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 12),
    _IpsaSaPreActAHSharedSecretName_Type()
)
ipsaSaPreActAHSharedSecretName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActAHSharedSecretName.setStatus("current")
_IpsaSaPreActESPSPI_Type = Integer32
_IpsaSaPreActESPSPI_Object = MibTableColumn
ipsaSaPreActESPSPI = _IpsaSaPreActESPSPI_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 13),
    _IpsaSaPreActESPSPI_Type()
)
ipsaSaPreActESPSPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActESPSPI.setStatus("current")


class _IpsaSaPreActESPTransformName_Type(SnmpAdminString):
    """Custom type ipsaSaPreActESPTransformName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpsaSaPreActESPTransformName_Type.__name__ = "SnmpAdminString"
_IpsaSaPreActESPTransformName_Object = MibTableColumn
ipsaSaPreActESPTransformName = _IpsaSaPreActESPTransformName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 14),
    _IpsaSaPreActESPTransformName_Type()
)
ipsaSaPreActESPTransformName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActESPTransformName.setStatus("current")


class _IpsaSaPreActESPEncSecretName_Type(SnmpAdminString):
    """Custom type ipsaSaPreActESPEncSecretName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpsaSaPreActESPEncSecretName_Type.__name__ = "SnmpAdminString"
_IpsaSaPreActESPEncSecretName_Object = MibTableColumn
ipsaSaPreActESPEncSecretName = _IpsaSaPreActESPEncSecretName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 15),
    _IpsaSaPreActESPEncSecretName_Type()
)
ipsaSaPreActESPEncSecretName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActESPEncSecretName.setStatus("current")


class _IpsaSaPreActESPAuthSecretName_Type(SnmpAdminString):
    """Custom type ipsaSaPreActESPAuthSecretName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpsaSaPreActESPAuthSecretName_Type.__name__ = "SnmpAdminString"
_IpsaSaPreActESPAuthSecretName_Object = MibTableColumn
ipsaSaPreActESPAuthSecretName = _IpsaSaPreActESPAuthSecretName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 16),
    _IpsaSaPreActESPAuthSecretName_Type()
)
ipsaSaPreActESPAuthSecretName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActESPAuthSecretName.setStatus("current")
_IpsaSaPreActIPCompSPI_Type = Integer32
_IpsaSaPreActIPCompSPI_Object = MibTableColumn
ipsaSaPreActIPCompSPI = _IpsaSaPreActIPCompSPI_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 17),
    _IpsaSaPreActIPCompSPI_Type()
)
ipsaSaPreActIPCompSPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActIPCompSPI.setStatus("current")


class _IpsaSaPreActIPCompTransformName_Type(SnmpAdminString):
    """Custom type ipsaSaPreActIPCompTransformName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpsaSaPreActIPCompTransformName_Type.__name__ = "SnmpAdminString"
_IpsaSaPreActIPCompTransformName_Object = MibTableColumn
ipsaSaPreActIPCompTransformName = _IpsaSaPreActIPCompTransformName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 18),
    _IpsaSaPreActIPCompTransformName_Type()
)
ipsaSaPreActIPCompTransformName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActIPCompTransformName.setStatus("current")


class _IpsaSaPreActPeerGatewayIdName_Type(SnmpAdminString):
    """Custom type ipsaSaPreActPeerGatewayIdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpsaSaPreActPeerGatewayIdName_Type.__name__ = "SnmpAdminString"
_IpsaSaPreActPeerGatewayIdName_Object = MibTableColumn
ipsaSaPreActPeerGatewayIdName = _IpsaSaPreActPeerGatewayIdName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 19),
    _IpsaSaPreActPeerGatewayIdName_Type()
)
ipsaSaPreActPeerGatewayIdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActPeerGatewayIdName.setStatus("current")
_IpsaSaPreActLastChanged_Type = TimeStamp
_IpsaSaPreActLastChanged_Object = MibTableColumn
ipsaSaPreActLastChanged = _IpsaSaPreActLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 20),
    _IpsaSaPreActLastChanged_Type()
)
ipsaSaPreActLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsaSaPreActLastChanged.setStatus("current")


class _IpsaSaPreActStorageType_Type(StorageType):
    """Custom type ipsaSaPreActStorageType based on StorageType"""


_IpsaSaPreActStorageType_Object = MibTableColumn
ipsaSaPreActStorageType = _IpsaSaPreActStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 21),
    _IpsaSaPreActStorageType_Type()
)
ipsaSaPreActStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActStorageType.setStatus("current")
_IpsaSaPreActRowStatus_Type = RowStatus
_IpsaSaPreActRowStatus_Object = MibTableColumn
ipsaSaPreActRowStatus = _IpsaSaPreActRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 1, 1, 22),
    _IpsaSaPreActRowStatus_Type()
)
ipsaSaPreActRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaSaPreActRowStatus.setStatus("current")
_IpsaAhTransformTable_Object = MibTable
ipsaAhTransformTable = _IpsaAhTransformTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipsaAhTransformTable.setStatus("current")
_IpsaAhTransformEntry_Object = MibTableRow
ipsaAhTransformEntry = _IpsaAhTransformEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1)
)
ipsaAhTransformEntry.setIndexNames(
    (0, "IPSEC-IPSECACTION-MIB", "ipsaAhTranName"),
)
if mibBuilder.loadTexts:
    ipsaAhTransformEntry.setStatus("current")


class _IpsaAhTranName_Type(SnmpAdminString):
    """Custom type ipsaAhTranName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpsaAhTranName_Type.__name__ = "SnmpAdminString"
_IpsaAhTranName_Object = MibTableColumn
ipsaAhTranName = _IpsaAhTranName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 1),
    _IpsaAhTranName_Type()
)
ipsaAhTranName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsaAhTranName.setStatus("current")
_IpsaAhTranMaxLifetimeSec_Type = Unsigned32
_IpsaAhTranMaxLifetimeSec_Object = MibTableColumn
ipsaAhTranMaxLifetimeSec = _IpsaAhTranMaxLifetimeSec_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 2),
    _IpsaAhTranMaxLifetimeSec_Type()
)
ipsaAhTranMaxLifetimeSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaAhTranMaxLifetimeSec.setStatus("current")
if mibBuilder.loadTexts:
    ipsaAhTranMaxLifetimeSec.setUnits("seconds")
_IpsaAhTranMaxLifetimeKB_Type = Unsigned32
_IpsaAhTranMaxLifetimeKB_Object = MibTableColumn
ipsaAhTranMaxLifetimeKB = _IpsaAhTranMaxLifetimeKB_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 3),
    _IpsaAhTranMaxLifetimeKB_Type()
)
ipsaAhTranMaxLifetimeKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaAhTranMaxLifetimeKB.setStatus("current")
_IpsaAhTranAlgorithm_Type = IpsecDoiAuthAlgorithm
_IpsaAhTranAlgorithm_Object = MibTableColumn
ipsaAhTranAlgorithm = _IpsaAhTranAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 4),
    _IpsaAhTranAlgorithm_Type()
)
ipsaAhTranAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaAhTranAlgorithm.setStatus("current")
_IpsaAhTranReplayProtection_Type = TruthValue
_IpsaAhTranReplayProtection_Object = MibTableColumn
ipsaAhTranReplayProtection = _IpsaAhTranReplayProtection_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 5),
    _IpsaAhTranReplayProtection_Type()
)
ipsaAhTranReplayProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaAhTranReplayProtection.setStatus("current")
_IpsaAhTranReplayWindowSize_Type = Unsigned32
_IpsaAhTranReplayWindowSize_Object = MibTableColumn
ipsaAhTranReplayWindowSize = _IpsaAhTranReplayWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 6),
    _IpsaAhTranReplayWindowSize_Type()
)
ipsaAhTranReplayWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaAhTranReplayWindowSize.setStatus("current")
_IpsaAhTranLastChanged_Type = TimeStamp
_IpsaAhTranLastChanged_Object = MibTableColumn
ipsaAhTranLastChanged = _IpsaAhTranLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 7),
    _IpsaAhTranLastChanged_Type()
)
ipsaAhTranLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsaAhTranLastChanged.setStatus("current")


class _IpsaAhTranStorageType_Type(StorageType):
    """Custom type ipsaAhTranStorageType based on StorageType"""


_IpsaAhTranStorageType_Object = MibTableColumn
ipsaAhTranStorageType = _IpsaAhTranStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 8),
    _IpsaAhTranStorageType_Type()
)
ipsaAhTranStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaAhTranStorageType.setStatus("current")
_IpsaAhTranRowStatus_Type = RowStatus
_IpsaAhTranRowStatus_Object = MibTableColumn
ipsaAhTranRowStatus = _IpsaAhTranRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 2, 1, 9),
    _IpsaAhTranRowStatus_Type()
)
ipsaAhTranRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaAhTranRowStatus.setStatus("current")
_IpsaEspTransformTable_Object = MibTable
ipsaEspTransformTable = _IpsaEspTransformTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ipsaEspTransformTable.setStatus("current")
_IpsaEspTransformEntry_Object = MibTableRow
ipsaEspTransformEntry = _IpsaEspTransformEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1)
)
ipsaEspTransformEntry.setIndexNames(
    (0, "IPSEC-IPSECACTION-MIB", "ipsaEspTranName"),
)
if mibBuilder.loadTexts:
    ipsaEspTransformEntry.setStatus("current")


class _IpsaEspTranName_Type(SnmpAdminString):
    """Custom type ipsaEspTranName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpsaEspTranName_Type.__name__ = "SnmpAdminString"
_IpsaEspTranName_Object = MibTableColumn
ipsaEspTranName = _IpsaEspTranName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 1),
    _IpsaEspTranName_Type()
)
ipsaEspTranName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsaEspTranName.setStatus("current")
_IpsaEspTranMaxLifetimeSec_Type = Unsigned32
_IpsaEspTranMaxLifetimeSec_Object = MibTableColumn
ipsaEspTranMaxLifetimeSec = _IpsaEspTranMaxLifetimeSec_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 2),
    _IpsaEspTranMaxLifetimeSec_Type()
)
ipsaEspTranMaxLifetimeSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaEspTranMaxLifetimeSec.setStatus("current")
if mibBuilder.loadTexts:
    ipsaEspTranMaxLifetimeSec.setUnits("seconds")
_IpsaEspTranMaxLifetimeKB_Type = Unsigned32
_IpsaEspTranMaxLifetimeKB_Object = MibTableColumn
ipsaEspTranMaxLifetimeKB = _IpsaEspTranMaxLifetimeKB_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 3),
    _IpsaEspTranMaxLifetimeKB_Type()
)
ipsaEspTranMaxLifetimeKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaEspTranMaxLifetimeKB.setStatus("current")
_IpsaEspTranCipherTransformId_Type = IpsecDoiEspTransform
_IpsaEspTranCipherTransformId_Object = MibTableColumn
ipsaEspTranCipherTransformId = _IpsaEspTranCipherTransformId_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 4),
    _IpsaEspTranCipherTransformId_Type()
)
ipsaEspTranCipherTransformId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaEspTranCipherTransformId.setStatus("current")
_IpsaEspTranCipherKeyLength_Type = Unsigned32
_IpsaEspTranCipherKeyLength_Object = MibTableColumn
ipsaEspTranCipherKeyLength = _IpsaEspTranCipherKeyLength_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 5),
    _IpsaEspTranCipherKeyLength_Type()
)
ipsaEspTranCipherKeyLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaEspTranCipherKeyLength.setStatus("current")
_IpsaEspTranCipherKeyRounds_Type = Unsigned32
_IpsaEspTranCipherKeyRounds_Object = MibTableColumn
ipsaEspTranCipherKeyRounds = _IpsaEspTranCipherKeyRounds_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 6),
    _IpsaEspTranCipherKeyRounds_Type()
)
ipsaEspTranCipherKeyRounds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaEspTranCipherKeyRounds.setStatus("current")
_IpsaEspTranIntegrityAlgorithmId_Type = IpsecDoiAuthAlgorithm
_IpsaEspTranIntegrityAlgorithmId_Object = MibTableColumn
ipsaEspTranIntegrityAlgorithmId = _IpsaEspTranIntegrityAlgorithmId_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 7),
    _IpsaEspTranIntegrityAlgorithmId_Type()
)
ipsaEspTranIntegrityAlgorithmId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaEspTranIntegrityAlgorithmId.setStatus("current")
_IpsaEspTranReplayPrevention_Type = TruthValue
_IpsaEspTranReplayPrevention_Object = MibTableColumn
ipsaEspTranReplayPrevention = _IpsaEspTranReplayPrevention_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 8),
    _IpsaEspTranReplayPrevention_Type()
)
ipsaEspTranReplayPrevention.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaEspTranReplayPrevention.setStatus("current")
_IpsaEspTranReplayWindowSize_Type = Unsigned32
_IpsaEspTranReplayWindowSize_Object = MibTableColumn
ipsaEspTranReplayWindowSize = _IpsaEspTranReplayWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 9),
    _IpsaEspTranReplayWindowSize_Type()
)
ipsaEspTranReplayWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaEspTranReplayWindowSize.setStatus("current")
_IpsaEspTranLastChanged_Type = TimeStamp
_IpsaEspTranLastChanged_Object = MibTableColumn
ipsaEspTranLastChanged = _IpsaEspTranLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 10),
    _IpsaEspTranLastChanged_Type()
)
ipsaEspTranLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsaEspTranLastChanged.setStatus("current")


class _IpsaEspTranStorageType_Type(StorageType):
    """Custom type ipsaEspTranStorageType based on StorageType"""


_IpsaEspTranStorageType_Object = MibTableColumn
ipsaEspTranStorageType = _IpsaEspTranStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 11),
    _IpsaEspTranStorageType_Type()
)
ipsaEspTranStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaEspTranStorageType.setStatus("current")
_IpsaEspTranRowStatus_Type = RowStatus
_IpsaEspTranRowStatus_Object = MibTableColumn
ipsaEspTranRowStatus = _IpsaEspTranRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 3, 1, 12),
    _IpsaEspTranRowStatus_Type()
)
ipsaEspTranRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaEspTranRowStatus.setStatus("current")
_IpsaIpcompTransformTable_Object = MibTable
ipsaIpcompTransformTable = _IpsaIpcompTransformTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ipsaIpcompTransformTable.setStatus("current")
_IpsaIpcompTransformEntry_Object = MibTableRow
ipsaIpcompTransformEntry = _IpsaIpcompTransformEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1)
)
ipsaIpcompTransformEntry.setIndexNames(
    (0, "IPSEC-IPSECACTION-MIB", "ipsaIpcompTranName"),
)
if mibBuilder.loadTexts:
    ipsaIpcompTransformEntry.setStatus("current")


class _IpsaIpcompTranName_Type(SnmpAdminString):
    """Custom type ipsaIpcompTranName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpsaIpcompTranName_Type.__name__ = "SnmpAdminString"
_IpsaIpcompTranName_Object = MibTableColumn
ipsaIpcompTranName = _IpsaIpcompTranName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 1),
    _IpsaIpcompTranName_Type()
)
ipsaIpcompTranName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsaIpcompTranName.setStatus("current")
_IpsaIpcompTranMaxLifetimeSec_Type = Unsigned32
_IpsaIpcompTranMaxLifetimeSec_Object = MibTableColumn
ipsaIpcompTranMaxLifetimeSec = _IpsaIpcompTranMaxLifetimeSec_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 2),
    _IpsaIpcompTranMaxLifetimeSec_Type()
)
ipsaIpcompTranMaxLifetimeSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaIpcompTranMaxLifetimeSec.setStatus("current")
if mibBuilder.loadTexts:
    ipsaIpcompTranMaxLifetimeSec.setUnits("seconds")
_IpsaIpcompTranMaxLifetimeKB_Type = Unsigned32
_IpsaIpcompTranMaxLifetimeKB_Object = MibTableColumn
ipsaIpcompTranMaxLifetimeKB = _IpsaIpcompTranMaxLifetimeKB_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 3),
    _IpsaIpcompTranMaxLifetimeKB_Type()
)
ipsaIpcompTranMaxLifetimeKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaIpcompTranMaxLifetimeKB.setStatus("current")
_IpsaIpcompTranAlgorithm_Type = IpsecDoiIpcompTransform
_IpsaIpcompTranAlgorithm_Object = MibTableColumn
ipsaIpcompTranAlgorithm = _IpsaIpcompTranAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 4),
    _IpsaIpcompTranAlgorithm_Type()
)
ipsaIpcompTranAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaIpcompTranAlgorithm.setStatus("current")
_IpsaIpcompTranDictionarySize_Type = Unsigned32
_IpsaIpcompTranDictionarySize_Object = MibTableColumn
ipsaIpcompTranDictionarySize = _IpsaIpcompTranDictionarySize_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 5),
    _IpsaIpcompTranDictionarySize_Type()
)
ipsaIpcompTranDictionarySize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaIpcompTranDictionarySize.setStatus("current")
_IpsaIpcompTranPrivateAlgorithm_Type = Unsigned32
_IpsaIpcompTranPrivateAlgorithm_Object = MibTableColumn
ipsaIpcompTranPrivateAlgorithm = _IpsaIpcompTranPrivateAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 6),
    _IpsaIpcompTranPrivateAlgorithm_Type()
)
ipsaIpcompTranPrivateAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaIpcompTranPrivateAlgorithm.setStatus("current")
_IpsaIpcompTranLastChanged_Type = TimeStamp
_IpsaIpcompTranLastChanged_Object = MibTableColumn
ipsaIpcompTranLastChanged = _IpsaIpcompTranLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 7),
    _IpsaIpcompTranLastChanged_Type()
)
ipsaIpcompTranLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsaIpcompTranLastChanged.setStatus("current")


class _IpsaIpcompTranStorageType_Type(StorageType):
    """Custom type ipsaIpcompTranStorageType based on StorageType"""


_IpsaIpcompTranStorageType_Object = MibTableColumn
ipsaIpcompTranStorageType = _IpsaIpcompTranStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 8),
    _IpsaIpcompTranStorageType_Type()
)
ipsaIpcompTranStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaIpcompTranStorageType.setStatus("current")
_IpsaIpcompTranRowStatus_Type = RowStatus
_IpsaIpcompTranRowStatus_Object = MibTableColumn
ipsaIpcompTranRowStatus = _IpsaIpcompTranRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 4, 1, 9),
    _IpsaIpcompTranRowStatus_Type()
)
ipsaIpcompTranRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaIpcompTranRowStatus.setStatus("current")
_IpsaCredentialTable_Object = MibTable
ipsaCredentialTable = _IpsaCredentialTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ipsaCredentialTable.setStatus("current")
_IpsaCredentialEntry_Object = MibTableRow
ipsaCredentialEntry = _IpsaCredentialEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1)
)
ipsaCredentialEntry.setIndexNames(
    (0, "IPSEC-IPSECACTION-MIB", "ipsaCredName"),
)
if mibBuilder.loadTexts:
    ipsaCredentialEntry.setStatus("current")


class _IpsaCredName_Type(SnmpAdminString):
    """Custom type ipsaCredName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpsaCredName_Type.__name__ = "SnmpAdminString"
_IpsaCredName_Object = MibTableColumn
ipsaCredName = _IpsaCredName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 1),
    _IpsaCredName_Type()
)
ipsaCredName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsaCredName.setStatus("current")
_IpsaCredType_Type = IpsaCredentialType
_IpsaCredType_Object = MibTableColumn
ipsaCredType = _IpsaCredType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 2),
    _IpsaCredType_Type()
)
ipsaCredType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaCredType.setStatus("current")


class _IpsaCredCredential_Type(OctetString):
    """Custom type ipsaCredCredential based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_IpsaCredCredential_Type.__name__ = "OctetString"
_IpsaCredCredential_Object = MibTableColumn
ipsaCredCredential = _IpsaCredCredential_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 3),
    _IpsaCredCredential_Type()
)
ipsaCredCredential.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaCredCredential.setStatus("current")
_IpsaCredSize_Type = Integer32
_IpsaCredSize_Object = MibTableColumn
ipsaCredSize = _IpsaCredSize_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 4),
    _IpsaCredSize_Type()
)
ipsaCredSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsaCredSize.setStatus("current")


class _IpsaCredMngName_Type(SnmpAdminString):
    """Custom type ipsaCredMngName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpsaCredMngName_Type.__name__ = "SnmpAdminString"
_IpsaCredMngName_Object = MibTableColumn
ipsaCredMngName = _IpsaCredMngName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 5),
    _IpsaCredMngName_Type()
)
ipsaCredMngName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaCredMngName.setStatus("current")


class _IpsaCredRemoteID_Type(OctetString):
    """Custom type ipsaCredRemoteID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_IpsaCredRemoteID_Type.__name__ = "OctetString"
_IpsaCredRemoteID_Object = MibTableColumn
ipsaCredRemoteID = _IpsaCredRemoteID_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 6),
    _IpsaCredRemoteID_Type()
)
ipsaCredRemoteID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaCredRemoteID.setStatus("current")


class _IpsaCredAdminStatus_Type(SpdAdminStatus):
    """Custom type ipsaCredAdminStatus based on SpdAdminStatus"""


_IpsaCredAdminStatus_Object = MibTableColumn
ipsaCredAdminStatus = _IpsaCredAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 7),
    _IpsaCredAdminStatus_Type()
)
ipsaCredAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaCredAdminStatus.setStatus("current")
_IpsaCredLastChanged_Type = TimeStamp
_IpsaCredLastChanged_Object = MibTableColumn
ipsaCredLastChanged = _IpsaCredLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 8),
    _IpsaCredLastChanged_Type()
)
ipsaCredLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsaCredLastChanged.setStatus("current")


class _IpsaCredStorageType_Type(StorageType):
    """Custom type ipsaCredStorageType based on StorageType"""


_IpsaCredStorageType_Object = MibTableColumn
ipsaCredStorageType = _IpsaCredStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 9),
    _IpsaCredStorageType_Type()
)
ipsaCredStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaCredStorageType.setStatus("current")
_IpsaCredRowStatus_Type = RowStatus
_IpsaCredRowStatus_Object = MibTableColumn
ipsaCredRowStatus = _IpsaCredRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 5, 1, 10),
    _IpsaCredRowStatus_Type()
)
ipsaCredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaCredRowStatus.setStatus("current")
_IpsaCredentialSegmentTable_Object = MibTable
ipsaCredentialSegmentTable = _IpsaCredentialSegmentTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ipsaCredentialSegmentTable.setStatus("current")
_IpsaCredentialSegmentEntry_Object = MibTableRow
ipsaCredentialSegmentEntry = _IpsaCredentialSegmentEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 6, 1)
)
ipsaCredentialSegmentEntry.setIndexNames(
    (0, "IPSEC-IPSECACTION-MIB", "ipsaCredName"),
    (0, "IPSEC-IPSECACTION-MIB", "ipsaCredSegIndex"),
)
if mibBuilder.loadTexts:
    ipsaCredentialSegmentEntry.setStatus("current")


class _IpsaCredSegIndex_Type(Integer32):
    """Custom type ipsaCredSegIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpsaCredSegIndex_Type.__name__ = "Integer32"
_IpsaCredSegIndex_Object = MibTableColumn
ipsaCredSegIndex = _IpsaCredSegIndex_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 6, 1, 1),
    _IpsaCredSegIndex_Type()
)
ipsaCredSegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsaCredSegIndex.setStatus("current")
_IpsaCredSegValue_Type = OctetString
_IpsaCredSegValue_Object = MibTableColumn
ipsaCredSegValue = _IpsaCredSegValue_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 6, 1, 2),
    _IpsaCredSegValue_Type()
)
ipsaCredSegValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaCredSegValue.setStatus("current")
_IpsaCredSegLastChanged_Type = TimeStamp
_IpsaCredSegLastChanged_Object = MibTableColumn
ipsaCredSegLastChanged = _IpsaCredSegLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 6, 1, 3),
    _IpsaCredSegLastChanged_Type()
)
ipsaCredSegLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsaCredSegLastChanged.setStatus("current")


class _IpsaCredSegStorageType_Type(StorageType):
    """Custom type ipsaCredSegStorageType based on StorageType"""


_IpsaCredSegStorageType_Object = MibTableColumn
ipsaCredSegStorageType = _IpsaCredSegStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 6, 1, 4),
    _IpsaCredSegStorageType_Type()
)
ipsaCredSegStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsaCredSegStorageType.setStatus("current")
_IpsaCredSegRowStatus_Type = RowStatus
_IpsaCredSegRowStatus_Object = MibTableColumn
ipsaCredSegRowStatus = _IpsaCredSegRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 6, 1, 5),
    _IpsaCredSegRowStatus_Type()
)
ipsaCredSegRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaCredSegRowStatus.setStatus("current")
_IpsaPeerIdentityTable_Object = MibTable
ipsaPeerIdentityTable = _IpsaPeerIdentityTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ipsaPeerIdentityTable.setStatus("current")
_IpsaPeerIdentityEntry_Object = MibTableRow
ipsaPeerIdentityEntry = _IpsaPeerIdentityEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1)
)
ipsaPeerIdentityEntry.setIndexNames(
    (0, "IPSEC-IPSECACTION-MIB", "ipsaPeerIdName"),
    (0, "IPSEC-IPSECACTION-MIB", "ipsaPeerIdPriority"),
)
if mibBuilder.loadTexts:
    ipsaPeerIdentityEntry.setStatus("current")


class _IpsaPeerIdName_Type(SnmpAdminString):
    """Custom type ipsaPeerIdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpsaPeerIdName_Type.__name__ = "SnmpAdminString"
_IpsaPeerIdName_Object = MibTableColumn
ipsaPeerIdName = _IpsaPeerIdName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 1),
    _IpsaPeerIdName_Type()
)
ipsaPeerIdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsaPeerIdName.setStatus("current")


class _IpsaPeerIdPriority_Type(Integer32):
    """Custom type ipsaPeerIdPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpsaPeerIdPriority_Type.__name__ = "Integer32"
_IpsaPeerIdPriority_Object = MibTableColumn
ipsaPeerIdPriority = _IpsaPeerIdPriority_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 2),
    _IpsaPeerIdPriority_Type()
)
ipsaPeerIdPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsaPeerIdPriority.setStatus("current")
_IpsaPeerIdType_Type = IpsecDoiIdentType
_IpsaPeerIdType_Object = MibTableColumn
ipsaPeerIdType = _IpsaPeerIdType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 3),
    _IpsaPeerIdType_Type()
)
ipsaPeerIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaPeerIdType.setStatus("current")
_IpsaPeerIdValue_Type = IpsaIdentityFilter
_IpsaPeerIdValue_Object = MibTableColumn
ipsaPeerIdValue = _IpsaPeerIdValue_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 4),
    _IpsaPeerIdValue_Type()
)
ipsaPeerIdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaPeerIdValue.setStatus("current")
_IpsaPeerIdAddressType_Type = InetAddressType
_IpsaPeerIdAddressType_Object = MibTableColumn
ipsaPeerIdAddressType = _IpsaPeerIdAddressType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 5),
    _IpsaPeerIdAddressType_Type()
)
ipsaPeerIdAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaPeerIdAddressType.setStatus("current")
_IpsaPeerIdAddress_Type = InetAddress
_IpsaPeerIdAddress_Object = MibTableColumn
ipsaPeerIdAddress = _IpsaPeerIdAddress_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 6),
    _IpsaPeerIdAddress_Type()
)
ipsaPeerIdAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaPeerIdAddress.setStatus("current")


class _IpsaPeerIdCredentialName_Type(SnmpAdminString):
    """Custom type ipsaPeerIdCredentialName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpsaPeerIdCredentialName_Type.__name__ = "SnmpAdminString"
_IpsaPeerIdCredentialName_Object = MibTableColumn
ipsaPeerIdCredentialName = _IpsaPeerIdCredentialName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 7),
    _IpsaPeerIdCredentialName_Type()
)
ipsaPeerIdCredentialName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaPeerIdCredentialName.setStatus("current")
_IpsaPeerIdLastChanged_Type = TimeStamp
_IpsaPeerIdLastChanged_Object = MibTableColumn
ipsaPeerIdLastChanged = _IpsaPeerIdLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 8),
    _IpsaPeerIdLastChanged_Type()
)
ipsaPeerIdLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsaPeerIdLastChanged.setStatus("current")


class _IpsaPeerIdStorageType_Type(StorageType):
    """Custom type ipsaPeerIdStorageType based on StorageType"""


_IpsaPeerIdStorageType_Object = MibTableColumn
ipsaPeerIdStorageType = _IpsaPeerIdStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 9),
    _IpsaPeerIdStorageType_Type()
)
ipsaPeerIdStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaPeerIdStorageType.setStatus("current")
_IpsaPeerIdRowStatus_Type = RowStatus
_IpsaPeerIdRowStatus_Object = MibTableColumn
ipsaPeerIdRowStatus = _IpsaPeerIdRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 1, 7, 1, 10),
    _IpsaPeerIdRowStatus_Type()
)
ipsaPeerIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsaPeerIdRowStatus.setStatus("current")
_IpsaNotificationObjects_ObjectIdentity = ObjectIdentity
ipsaNotificationObjects = _IpsaNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 2)
)
_IpsaNotifications_ObjectIdentity = ObjectIdentity
ipsaNotifications = _IpsaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 2, 0)
)
_IpsaNotificationVariables_ObjectIdentity = ObjectIdentity
ipsaNotificationVariables = _IpsaNotificationVariables_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 2, 1)
)
_IpsaConformanceObjects_ObjectIdentity = ObjectIdentity
ipsaConformanceObjects = _IpsaConformanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 3)
)
_IpsaCompliances_ObjectIdentity = ObjectIdentity
ipsaCompliances = _IpsaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 3, 1)
)
_IpsaGroups_ObjectIdentity = ObjectIdentity
ipsaGroups = _IpsaGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 3, 2)
)

# Managed Objects groups

ipsaPreconfiguredGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 3, 2, 1)
)
ipsaPreconfiguredGroup.setObjects(
      *(("IPSEC-IPSECACTION-MIB", "ipsaSaPreActActionDescription"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActActionLifetimeSec"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActActionLifetimeKB"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActDoActionLogging"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActDoPacketLogging"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActDFHandling"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActActionType"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActAHSPI"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActAHTransformName"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActAHSharedSecretName"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActESPSPI"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActESPTransformName"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActESPEncSecretName"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActESPAuthSecretName"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActIPCompSPI"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActIPCompTransformName"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActPeerGatewayIdName"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActLastChanged"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActStorageType"),
        ("IPSEC-IPSECACTION-MIB", "ipsaSaPreActRowStatus"))
)
if mibBuilder.loadTexts:
    ipsaPreconfiguredGroup.setStatus("current")

ipsaSharedGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 3, 2, 2)
)
ipsaSharedGroup.setObjects(
      *(("IPSEC-IPSECACTION-MIB", "ipsaAhTranMaxLifetimeSec"),
        ("IPSEC-IPSECACTION-MIB", "ipsaAhTranMaxLifetimeKB"),
        ("IPSEC-IPSECACTION-MIB", "ipsaAhTranAlgorithm"),
        ("IPSEC-IPSECACTION-MIB", "ipsaAhTranReplayProtection"),
        ("IPSEC-IPSECACTION-MIB", "ipsaAhTranReplayWindowSize"),
        ("IPSEC-IPSECACTION-MIB", "ipsaAhTranLastChanged"),
        ("IPSEC-IPSECACTION-MIB", "ipsaAhTranStorageType"),
        ("IPSEC-IPSECACTION-MIB", "ipsaAhTranRowStatus"),
        ("IPSEC-IPSECACTION-MIB", "ipsaEspTranMaxLifetimeSec"),
        ("IPSEC-IPSECACTION-MIB", "ipsaEspTranMaxLifetimeKB"),
        ("IPSEC-IPSECACTION-MIB", "ipsaEspTranCipherTransformId"),
        ("IPSEC-IPSECACTION-MIB", "ipsaEspTranCipherKeyLength"),
        ("IPSEC-IPSECACTION-MIB", "ipsaEspTranCipherKeyRounds"),
        ("IPSEC-IPSECACTION-MIB", "ipsaEspTranIntegrityAlgorithmId"),
        ("IPSEC-IPSECACTION-MIB", "ipsaEspTranReplayPrevention"),
        ("IPSEC-IPSECACTION-MIB", "ipsaEspTranReplayWindowSize"),
        ("IPSEC-IPSECACTION-MIB", "ipsaEspTranLastChanged"),
        ("IPSEC-IPSECACTION-MIB", "ipsaEspTranStorageType"),
        ("IPSEC-IPSECACTION-MIB", "ipsaEspTranRowStatus"),
        ("IPSEC-IPSECACTION-MIB", "ipsaIpcompTranDictionarySize"),
        ("IPSEC-IPSECACTION-MIB", "ipsaIpcompTranAlgorithm"),
        ("IPSEC-IPSECACTION-MIB", "ipsaIpcompTranMaxLifetimeSec"),
        ("IPSEC-IPSECACTION-MIB", "ipsaIpcompTranMaxLifetimeKB"),
        ("IPSEC-IPSECACTION-MIB", "ipsaIpcompTranPrivateAlgorithm"),
        ("IPSEC-IPSECACTION-MIB", "ipsaIpcompTranLastChanged"),
        ("IPSEC-IPSECACTION-MIB", "ipsaIpcompTranStorageType"),
        ("IPSEC-IPSECACTION-MIB", "ipsaIpcompTranRowStatus"),
        ("IPSEC-IPSECACTION-MIB", "ipsaCredType"),
        ("IPSEC-IPSECACTION-MIB", "ipsaCredCredential"),
        ("IPSEC-IPSECACTION-MIB", "ipsaCredMngName"),
        ("IPSEC-IPSECACTION-MIB", "ipsaCredSize"),
        ("IPSEC-IPSECACTION-MIB", "ipsaCredRemoteID"),
        ("IPSEC-IPSECACTION-MIB", "ipsaCredAdminStatus"),
        ("IPSEC-IPSECACTION-MIB", "ipsaCredLastChanged"),
        ("IPSEC-IPSECACTION-MIB", "ipsaCredStorageType"),
        ("IPSEC-IPSECACTION-MIB", "ipsaCredRowStatus"),
        ("IPSEC-IPSECACTION-MIB", "ipsaCredSegValue"),
        ("IPSEC-IPSECACTION-MIB", "ipsaCredSegLastChanged"),
        ("IPSEC-IPSECACTION-MIB", "ipsaCredSegStorageType"),
        ("IPSEC-IPSECACTION-MIB", "ipsaCredSegRowStatus"),
        ("IPSEC-IPSECACTION-MIB", "ipsaPeerIdValue"),
        ("IPSEC-IPSECACTION-MIB", "ipsaPeerIdType"),
        ("IPSEC-IPSECACTION-MIB", "ipsaPeerIdAddress"),
        ("IPSEC-IPSECACTION-MIB", "ipsaPeerIdAddressType"),
        ("IPSEC-IPSECACTION-MIB", "ipsaPeerIdCredentialName"),
        ("IPSEC-IPSECACTION-MIB", "ipsaPeerIdLastChanged"),
        ("IPSEC-IPSECACTION-MIB", "ipsaPeerIdStorageType"),
        ("IPSEC-IPSECACTION-MIB", "ipsaPeerIdRowStatus"))
)
if mibBuilder.loadTexts:
    ipsaSharedGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipsaIPsecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 153, 4, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ipsaIPsecCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPSEC-IPSECACTION-MIB",
    **{"IpsecDoiEncapsulationMode": IpsecDoiEncapsulationMode,
       "IpsecDoiIpcompTransform": IpsecDoiIpcompTransform,
       "IpsecDoiAuthAlgorithm": IpsecDoiAuthAlgorithm,
       "IpsecDoiEspTransform": IpsecDoiEspTransform,
       "IpsecDoiIdentType": IpsecDoiIdentType,
       "IpsaCredentialType": IpsaCredentialType,
       "IpsaIdentityFilter": IpsaIdentityFilter,
       "ipsaMIB": ipsaMIB,
       "ipsaConfigObjects": ipsaConfigObjects,
       "ipsaSaPreconfiguredActionTable": ipsaSaPreconfiguredActionTable,
       "ipsaSaPreconfiguredActionEntry": ipsaSaPreconfiguredActionEntry,
       "ipsaSaPreActActionName": ipsaSaPreActActionName,
       "ipsaSaPreActSADirection": ipsaSaPreActSADirection,
       "ipsaSaPreActActionDescription": ipsaSaPreActActionDescription,
       "ipsaSaPreActActionLifetimeSec": ipsaSaPreActActionLifetimeSec,
       "ipsaSaPreActActionLifetimeKB": ipsaSaPreActActionLifetimeKB,
       "ipsaSaPreActDoActionLogging": ipsaSaPreActDoActionLogging,
       "ipsaSaPreActDoPacketLogging": ipsaSaPreActDoPacketLogging,
       "ipsaSaPreActDFHandling": ipsaSaPreActDFHandling,
       "ipsaSaPreActActionType": ipsaSaPreActActionType,
       "ipsaSaPreActAHSPI": ipsaSaPreActAHSPI,
       "ipsaSaPreActAHTransformName": ipsaSaPreActAHTransformName,
       "ipsaSaPreActAHSharedSecretName": ipsaSaPreActAHSharedSecretName,
       "ipsaSaPreActESPSPI": ipsaSaPreActESPSPI,
       "ipsaSaPreActESPTransformName": ipsaSaPreActESPTransformName,
       "ipsaSaPreActESPEncSecretName": ipsaSaPreActESPEncSecretName,
       "ipsaSaPreActESPAuthSecretName": ipsaSaPreActESPAuthSecretName,
       "ipsaSaPreActIPCompSPI": ipsaSaPreActIPCompSPI,
       "ipsaSaPreActIPCompTransformName": ipsaSaPreActIPCompTransformName,
       "ipsaSaPreActPeerGatewayIdName": ipsaSaPreActPeerGatewayIdName,
       "ipsaSaPreActLastChanged": ipsaSaPreActLastChanged,
       "ipsaSaPreActStorageType": ipsaSaPreActStorageType,
       "ipsaSaPreActRowStatus": ipsaSaPreActRowStatus,
       "ipsaAhTransformTable": ipsaAhTransformTable,
       "ipsaAhTransformEntry": ipsaAhTransformEntry,
       "ipsaAhTranName": ipsaAhTranName,
       "ipsaAhTranMaxLifetimeSec": ipsaAhTranMaxLifetimeSec,
       "ipsaAhTranMaxLifetimeKB": ipsaAhTranMaxLifetimeKB,
       "ipsaAhTranAlgorithm": ipsaAhTranAlgorithm,
       "ipsaAhTranReplayProtection": ipsaAhTranReplayProtection,
       "ipsaAhTranReplayWindowSize": ipsaAhTranReplayWindowSize,
       "ipsaAhTranLastChanged": ipsaAhTranLastChanged,
       "ipsaAhTranStorageType": ipsaAhTranStorageType,
       "ipsaAhTranRowStatus": ipsaAhTranRowStatus,
       "ipsaEspTransformTable": ipsaEspTransformTable,
       "ipsaEspTransformEntry": ipsaEspTransformEntry,
       "ipsaEspTranName": ipsaEspTranName,
       "ipsaEspTranMaxLifetimeSec": ipsaEspTranMaxLifetimeSec,
       "ipsaEspTranMaxLifetimeKB": ipsaEspTranMaxLifetimeKB,
       "ipsaEspTranCipherTransformId": ipsaEspTranCipherTransformId,
       "ipsaEspTranCipherKeyLength": ipsaEspTranCipherKeyLength,
       "ipsaEspTranCipherKeyRounds": ipsaEspTranCipherKeyRounds,
       "ipsaEspTranIntegrityAlgorithmId": ipsaEspTranIntegrityAlgorithmId,
       "ipsaEspTranReplayPrevention": ipsaEspTranReplayPrevention,
       "ipsaEspTranReplayWindowSize": ipsaEspTranReplayWindowSize,
       "ipsaEspTranLastChanged": ipsaEspTranLastChanged,
       "ipsaEspTranStorageType": ipsaEspTranStorageType,
       "ipsaEspTranRowStatus": ipsaEspTranRowStatus,
       "ipsaIpcompTransformTable": ipsaIpcompTransformTable,
       "ipsaIpcompTransformEntry": ipsaIpcompTransformEntry,
       "ipsaIpcompTranName": ipsaIpcompTranName,
       "ipsaIpcompTranMaxLifetimeSec": ipsaIpcompTranMaxLifetimeSec,
       "ipsaIpcompTranMaxLifetimeKB": ipsaIpcompTranMaxLifetimeKB,
       "ipsaIpcompTranAlgorithm": ipsaIpcompTranAlgorithm,
       "ipsaIpcompTranDictionarySize": ipsaIpcompTranDictionarySize,
       "ipsaIpcompTranPrivateAlgorithm": ipsaIpcompTranPrivateAlgorithm,
       "ipsaIpcompTranLastChanged": ipsaIpcompTranLastChanged,
       "ipsaIpcompTranStorageType": ipsaIpcompTranStorageType,
       "ipsaIpcompTranRowStatus": ipsaIpcompTranRowStatus,
       "ipsaCredentialTable": ipsaCredentialTable,
       "ipsaCredentialEntry": ipsaCredentialEntry,
       "ipsaCredName": ipsaCredName,
       "ipsaCredType": ipsaCredType,
       "ipsaCredCredential": ipsaCredCredential,
       "ipsaCredSize": ipsaCredSize,
       "ipsaCredMngName": ipsaCredMngName,
       "ipsaCredRemoteID": ipsaCredRemoteID,
       "ipsaCredAdminStatus": ipsaCredAdminStatus,
       "ipsaCredLastChanged": ipsaCredLastChanged,
       "ipsaCredStorageType": ipsaCredStorageType,
       "ipsaCredRowStatus": ipsaCredRowStatus,
       "ipsaCredentialSegmentTable": ipsaCredentialSegmentTable,
       "ipsaCredentialSegmentEntry": ipsaCredentialSegmentEntry,
       "ipsaCredSegIndex": ipsaCredSegIndex,
       "ipsaCredSegValue": ipsaCredSegValue,
       "ipsaCredSegLastChanged": ipsaCredSegLastChanged,
       "ipsaCredSegStorageType": ipsaCredSegStorageType,
       "ipsaCredSegRowStatus": ipsaCredSegRowStatus,
       "ipsaPeerIdentityTable": ipsaPeerIdentityTable,
       "ipsaPeerIdentityEntry": ipsaPeerIdentityEntry,
       "ipsaPeerIdName": ipsaPeerIdName,
       "ipsaPeerIdPriority": ipsaPeerIdPriority,
       "ipsaPeerIdType": ipsaPeerIdType,
       "ipsaPeerIdValue": ipsaPeerIdValue,
       "ipsaPeerIdAddressType": ipsaPeerIdAddressType,
       "ipsaPeerIdAddress": ipsaPeerIdAddress,
       "ipsaPeerIdCredentialName": ipsaPeerIdCredentialName,
       "ipsaPeerIdLastChanged": ipsaPeerIdLastChanged,
       "ipsaPeerIdStorageType": ipsaPeerIdStorageType,
       "ipsaPeerIdRowStatus": ipsaPeerIdRowStatus,
       "ipsaNotificationObjects": ipsaNotificationObjects,
       "ipsaNotifications": ipsaNotifications,
       "ipsaNotificationVariables": ipsaNotificationVariables,
       "ipsaConformanceObjects": ipsaConformanceObjects,
       "ipsaCompliances": ipsaCompliances,
       "ipsaIPsecCompliance": ipsaIPsecCompliance,
       "ipsaGroups": ipsaGroups,
       "ipsaPreconfiguredGroup": ipsaPreconfiguredGroup,
       "ipsaSharedGroup": ipsaSharedGroup}
)
