# SNMP MIB module (EQLIPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLIPSEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:06 2024
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

(eqlGroupId,) = mibBuilder.importSymbols(
    "EQLGROUP-MIB",
    "eqlGroupId")

(eqlMemberIndex,) = mibBuilder.importSymbols(
    "EQLMEMBER-MIB",
    "eqlMemberIndex")

(Unsigned64,) = mibBuilder.importSymbols(
    "EQLSTORAGEPOOL-MIB",
    "Unsigned64")

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

eqlIpsecModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 22)
)
eqlIpsecModule.setRevisions(
        ("2010-07-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SnmpAdminString(OctetString, TextualConvention):
    status = "current"
    displayHint = "t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class InetPortNumber(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IpsecAuthType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("certificates", 2),
          ("manualkey", 3),
          ("presharedkey", 1))
    )



class IpsecIdType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("asn1dn", 5),
          ("fqdn", 4),
          ("ipaddress", 2),
          ("none", 1),
          ("userfqdn", 3))
    )



class IpsecEncType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes-cbc", 2),
          ("nullenc", 1),
          ("triple-des-cbc", 3))
    )



# MIB Managed Objects in the order of their OIDs

_EqlIpsecObjects_ObjectIdentity = ObjectIdentity
eqlIpsecObjects = _EqlIpsecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1)
)
_EqlIpsecTable_Object = MibTable
eqlIpsecTable = _EqlIpsecTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 1)
)
if mibBuilder.loadTexts:
    eqlIpsecTable.setStatus("current")
_EqlIpsecEntry_Object = MibTableRow
eqlIpsecEntry = _EqlIpsecEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 1, 1)
)
eqlIpsecEntry.setIndexNames(
    (0, "EQLIPSEC-MIB", "eqlIpsecInstanceId"),
)
if mibBuilder.loadTexts:
    eqlIpsecEntry.setStatus("current")
_EqlIpsecInstanceId_Type = Integer32
_EqlIpsecInstanceId_Object = MibTableColumn
eqlIpsecInstanceId = _EqlIpsecInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 1, 1, 1),
    _EqlIpsecInstanceId_Type()
)
eqlIpsecInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlIpsecInstanceId.setStatus("current")


class _EqlIpsecEnable_Type(TruthValue):
    """Custom type eqlIpsecEnable based on TruthValue"""


_EqlIpsecEnable_Object = MibTableColumn
eqlIpsecEnable = _EqlIpsecEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 1, 1, 2),
    _EqlIpsecEnable_Type()
)
eqlIpsecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlIpsecEnable.setStatus("current")
_EqlIpsecRowStatus_Type = RowStatus
_EqlIpsecRowStatus_Object = MibTableColumn
eqlIpsecRowStatus = _EqlIpsecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 1, 1, 3),
    _EqlIpsecRowStatus_Type()
)
eqlIpsecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecRowStatus.setStatus("current")
_EqlIpsecPolicyTable_Object = MibTable
eqlIpsecPolicyTable = _EqlIpsecPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 2)
)
if mibBuilder.loadTexts:
    eqlIpsecPolicyTable.setStatus("current")
_EqlIpsecPolicyEntry_Object = MibTableRow
eqlIpsecPolicyEntry = _EqlIpsecPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1)
)
eqlIpsecPolicyEntry.setIndexNames(
    (0, "EQLIPSEC-MIB", "eqlIpsecPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    eqlIpsecPolicyEntry.setStatus("current")
_EqlIpsecPolicyInstanceId_Type = Integer32
_EqlIpsecPolicyInstanceId_Object = MibTableColumn
eqlIpsecPolicyInstanceId = _EqlIpsecPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 1),
    _EqlIpsecPolicyInstanceId_Type()
)
eqlIpsecPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlIpsecPolicyInstanceId.setStatus("current")


class _EqlIpsecPolicyFilterName_Type(SnmpAdminString):
    """Custom type eqlIpsecPolicyFilterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EqlIpsecPolicyFilterName_Type.__name__ = "SnmpAdminString"
_EqlIpsecPolicyFilterName_Object = MibTableColumn
eqlIpsecPolicyFilterName = _EqlIpsecPolicyFilterName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 2),
    _EqlIpsecPolicyFilterName_Type()
)
eqlIpsecPolicyFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPolicyFilterName.setStatus("current")


class _EqlIpsecPolicyFilterIPVersion_Type(InetAddressType):
    """Custom type eqlIpsecPolicyFilterIPVersion based on InetAddressType"""


_EqlIpsecPolicyFilterIPVersion_Object = MibTableColumn
eqlIpsecPolicyFilterIPVersion = _EqlIpsecPolicyFilterIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 3),
    _EqlIpsecPolicyFilterIPVersion_Type()
)
eqlIpsecPolicyFilterIPVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPolicyFilterIPVersion.setStatus("current")
_EqlIpsecPolicyFilterAddress_Type = InetAddress
_EqlIpsecPolicyFilterAddress_Object = MibTableColumn
eqlIpsecPolicyFilterAddress = _EqlIpsecPolicyFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 4),
    _EqlIpsecPolicyFilterAddress_Type()
)
eqlIpsecPolicyFilterAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPolicyFilterAddress.setStatus("current")


class _EqlIpsecPolicyFilterNetmaskLen_Type(Integer32):
    """Custom type eqlIpsecPolicyFilterNetmaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_EqlIpsecPolicyFilterNetmaskLen_Type.__name__ = "Integer32"
_EqlIpsecPolicyFilterNetmaskLen_Object = MibTableColumn
eqlIpsecPolicyFilterNetmaskLen = _EqlIpsecPolicyFilterNetmaskLen_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 5),
    _EqlIpsecPolicyFilterNetmaskLen_Type()
)
eqlIpsecPolicyFilterNetmaskLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPolicyFilterNetmaskLen.setStatus("current")
_EqlIpsecPolicyFilterLocalAddress_Type = InetAddress
_EqlIpsecPolicyFilterLocalAddress_Object = MibTableColumn
eqlIpsecPolicyFilterLocalAddress = _EqlIpsecPolicyFilterLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 6),
    _EqlIpsecPolicyFilterLocalAddress_Type()
)
eqlIpsecPolicyFilterLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPolicyFilterLocalAddress.setStatus("current")


class _EqlIpsecPolicyFilterPort_Type(Integer32):
    """Custom type eqlIpsecPolicyFilterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EqlIpsecPolicyFilterPort_Type.__name__ = "Integer32"
_EqlIpsecPolicyFilterPort_Object = MibTableColumn
eqlIpsecPolicyFilterPort = _EqlIpsecPolicyFilterPort_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 7),
    _EqlIpsecPolicyFilterPort_Type()
)
eqlIpsecPolicyFilterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPolicyFilterPort.setStatus("current")


class _EqlIpsecPolicyFilterLocalPort_Type(Integer32):
    """Custom type eqlIpsecPolicyFilterLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EqlIpsecPolicyFilterLocalPort_Type.__name__ = "Integer32"
_EqlIpsecPolicyFilterLocalPort_Object = MibTableColumn
eqlIpsecPolicyFilterLocalPort = _EqlIpsecPolicyFilterLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 8),
    _EqlIpsecPolicyFilterLocalPort_Type()
)
eqlIpsecPolicyFilterLocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPolicyFilterLocalPort.setStatus("current")


class _EqlIpsecPolicyFilterProtocol_Type(Integer32):
    """Custom type eqlIpsecPolicyFilterProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EqlIpsecPolicyFilterProtocol_Type.__name__ = "Integer32"
_EqlIpsecPolicyFilterProtocol_Object = MibTableColumn
eqlIpsecPolicyFilterProtocol = _EqlIpsecPolicyFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 9),
    _EqlIpsecPolicyFilterProtocol_Type()
)
eqlIpsecPolicyFilterProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPolicyFilterProtocol.setStatus("current")


class _EqlIpsecPolicyFilterPeerName_Type(SnmpAdminString):
    """Custom type eqlIpsecPolicyFilterPeerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlIpsecPolicyFilterPeerName_Type.__name__ = "SnmpAdminString"
_EqlIpsecPolicyFilterPeerName_Object = MibTableColumn
eqlIpsecPolicyFilterPeerName = _EqlIpsecPolicyFilterPeerName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 10),
    _EqlIpsecPolicyFilterPeerName_Type()
)
eqlIpsecPolicyFilterPeerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPolicyFilterPeerName.setStatus("current")


class _EqlIpsecPolicyFilterAction_Type(Integer32):
    """Custom type eqlIpsecPolicyFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 3),
          ("ipsec", 1),
          ("pass", 2))
    )


_EqlIpsecPolicyFilterAction_Type.__name__ = "Integer32"
_EqlIpsecPolicyFilterAction_Object = MibTableColumn
eqlIpsecPolicyFilterAction = _EqlIpsecPolicyFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 11),
    _EqlIpsecPolicyFilterAction_Type()
)
eqlIpsecPolicyFilterAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPolicyFilterAction.setStatus("current")
_EqlIpsecPolicyFilterRowStatus_Type = RowStatus
_EqlIpsecPolicyFilterRowStatus_Object = MibTableColumn
eqlIpsecPolicyFilterRowStatus = _EqlIpsecPolicyFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 12),
    _EqlIpsecPolicyFilterRowStatus_Type()
)
eqlIpsecPolicyFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPolicyFilterRowStatus.setStatus("current")
_EqlIpsecCertConfigTable_Object = MibTable
eqlIpsecCertConfigTable = _EqlIpsecCertConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 3)
)
if mibBuilder.loadTexts:
    eqlIpsecCertConfigTable.setStatus("current")
_EqlIpsecCertConfigEntry_Object = MibTableRow
eqlIpsecCertConfigEntry = _EqlIpsecCertConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 3, 1)
)
eqlIpsecCertConfigEntry.setIndexNames(
    (0, "EQLIPSEC-MIB", "eqlIpsecCertInstanceId"),
)
if mibBuilder.loadTexts:
    eqlIpsecCertConfigEntry.setStatus("current")
_EqlIpsecCertInstanceId_Type = Integer32
_EqlIpsecCertInstanceId_Object = MibTableColumn
eqlIpsecCertInstanceId = _EqlIpsecCertInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 3, 1, 1),
    _EqlIpsecCertInstanceId_Type()
)
eqlIpsecCertInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlIpsecCertInstanceId.setStatus("current")


class _EqlIpsecCertName_Type(SnmpAdminString):
    """Custom type eqlIpsecCertName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EqlIpsecCertName_Type.__name__ = "SnmpAdminString"
_EqlIpsecCertName_Object = MibTableColumn
eqlIpsecCertName = _EqlIpsecCertName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 3, 1, 2),
    _EqlIpsecCertName_Type()
)
eqlIpsecCertName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecCertName.setStatus("current")


class _EqlIpsecCertFileName_Type(SnmpAdminString):
    """Custom type eqlIpsecCertFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlIpsecCertFileName_Type.__name__ = "SnmpAdminString"
_EqlIpsecCertFileName_Object = MibTableColumn
eqlIpsecCertFileName = _EqlIpsecCertFileName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 3, 1, 3),
    _EqlIpsecCertFileName_Type()
)
eqlIpsecCertFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecCertFileName.setStatus("current")


class _EqlIpsecCertType_Type(Integer32):
    """Custom type eqlIpsecCertType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("intermediate", 3),
          ("local-cert", 1),
          ("root-cert", 2))
    )


_EqlIpsecCertType_Type.__name__ = "Integer32"
_EqlIpsecCertType_Object = MibTableColumn
eqlIpsecCertType = _EqlIpsecCertType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 3, 1, 4),
    _EqlIpsecCertType_Type()
)
eqlIpsecCertType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecCertType.setStatus("current")


class _EqlIpsecPrivKeyFileName_Type(SnmpAdminString):
    """Custom type eqlIpsecPrivKeyFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlIpsecPrivKeyFileName_Type.__name__ = "SnmpAdminString"
_EqlIpsecPrivKeyFileName_Object = MibTableColumn
eqlIpsecPrivKeyFileName = _EqlIpsecPrivKeyFileName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 3, 1, 5),
    _EqlIpsecPrivKeyFileName_Type()
)
eqlIpsecPrivKeyFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPrivKeyFileName.setStatus("current")


class _EqlIpsecCertPassword_Type(SnmpAdminString):
    """Custom type eqlIpsecCertPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlIpsecCertPassword_Type.__name__ = "SnmpAdminString"
_EqlIpsecCertPassword_Object = MibTableColumn
eqlIpsecCertPassword = _EqlIpsecCertPassword_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 3, 1, 6),
    _EqlIpsecCertPassword_Type()
)
eqlIpsecCertPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecCertPassword.setStatus("current")
_EqlIpsecCertRowStatus_Type = RowStatus
_EqlIpsecCertRowStatus_Object = MibTableColumn
eqlIpsecCertRowStatus = _EqlIpsecCertRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 3, 1, 7),
    _EqlIpsecCertRowStatus_Type()
)
eqlIpsecCertRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecCertRowStatus.setStatus("current")
_EqlIpsecPeerTable_Object = MibTable
eqlIpsecPeerTable = _EqlIpsecPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4)
)
if mibBuilder.loadTexts:
    eqlIpsecPeerTable.setStatus("current")
_EqlIpsecPeerEntry_Object = MibTableRow
eqlIpsecPeerEntry = _EqlIpsecPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1)
)
eqlIpsecPeerEntry.setIndexNames(
    (0, "EQLIPSEC-MIB", "eqlIpsecPeerInstanceId"),
)
if mibBuilder.loadTexts:
    eqlIpsecPeerEntry.setStatus("current")
_EqlIpsecPeerInstanceId_Type = Integer32
_EqlIpsecPeerInstanceId_Object = MibTableColumn
eqlIpsecPeerInstanceId = _EqlIpsecPeerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 1),
    _EqlIpsecPeerInstanceId_Type()
)
eqlIpsecPeerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlIpsecPeerInstanceId.setStatus("current")


class _EqlIpsecPeerName_Type(SnmpAdminString):
    """Custom type eqlIpsecPeerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlIpsecPeerName_Type.__name__ = "SnmpAdminString"
_EqlIpsecPeerName_Object = MibTableColumn
eqlIpsecPeerName = _EqlIpsecPeerName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 2),
    _EqlIpsecPeerName_Type()
)
eqlIpsecPeerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPeerName.setStatus("current")


class _EqlIpsecPeerAuthType_Type(Integer32):
    """Custom type eqlIpsecPeerAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("certificates", 2),
          ("manualkey", 3),
          ("presharedkey", 1))
    )


_EqlIpsecPeerAuthType_Type.__name__ = "Integer32"
_EqlIpsecPeerAuthType_Object = MibTableColumn
eqlIpsecPeerAuthType = _EqlIpsecPeerAuthType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 3),
    _EqlIpsecPeerAuthType_Type()
)
eqlIpsecPeerAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPeerAuthType.setStatus("current")


class _EqlIpsecPeerPreSharedKey_Type(DisplayString):
    """Custom type eqlIpsecPeerPreSharedKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 130),
    )


_EqlIpsecPeerPreSharedKey_Type.__name__ = "DisplayString"
_EqlIpsecPeerPreSharedKey_Object = MibTableColumn
eqlIpsecPeerPreSharedKey = _EqlIpsecPeerPreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 4),
    _EqlIpsecPeerPreSharedKey_Type()
)
eqlIpsecPeerPreSharedKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPeerPreSharedKey.setStatus("current")


class _EqlIpsecPeerCertIdType_Type(Integer32):
    """Custom type eqlIpsecPeerCertIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("asn1dn", 5),
          ("fqdn", 4),
          ("ipaddress", 2),
          ("none", 1),
          ("userfqdn", 3))
    )


_EqlIpsecPeerCertIdType_Type.__name__ = "Integer32"
_EqlIpsecPeerCertIdType_Object = MibTableColumn
eqlIpsecPeerCertIdType = _EqlIpsecPeerCertIdType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 5),
    _EqlIpsecPeerCertIdType_Type()
)
eqlIpsecPeerCertIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlIpsecPeerCertIdType.setStatus("current")


class _EqlIpsecPeerCertIdValue_Type(SnmpAdminString):
    """Custom type eqlIpsecPeerCertIdValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EqlIpsecPeerCertIdValue_Type.__name__ = "SnmpAdminString"
_EqlIpsecPeerCertIdValue_Object = MibTableColumn
eqlIpsecPeerCertIdValue = _EqlIpsecPeerCertIdValue_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 6),
    _EqlIpsecPeerCertIdValue_Type()
)
eqlIpsecPeerCertIdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlIpsecPeerCertIdValue.setStatus("current")
_EqlIpsecPeerNullEnc_Type = TruthValue
_EqlIpsecPeerNullEnc_Object = MibTableColumn
eqlIpsecPeerNullEnc = _EqlIpsecPeerNullEnc_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 7),
    _EqlIpsecPeerNullEnc_Type()
)
eqlIpsecPeerNullEnc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPeerNullEnc.setStatus("current")


class _EqlIpsecPeerTunnelMode_Type(TruthValue):
    """Custom type eqlIpsecPeerTunnelMode based on TruthValue"""


_EqlIpsecPeerTunnelMode_Object = MibTableColumn
eqlIpsecPeerTunnelMode = _EqlIpsecPeerTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 8),
    _EqlIpsecPeerTunnelMode_Type()
)
eqlIpsecPeerTunnelMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPeerTunnelMode.setStatus("current")


class _EqlIpsecPeerTunnelAddressIPVersion_Type(InetAddressType):
    """Custom type eqlIpsecPeerTunnelAddressIPVersion based on InetAddressType"""


_EqlIpsecPeerTunnelAddressIPVersion_Object = MibTableColumn
eqlIpsecPeerTunnelAddressIPVersion = _EqlIpsecPeerTunnelAddressIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 9),
    _EqlIpsecPeerTunnelAddressIPVersion_Type()
)
eqlIpsecPeerTunnelAddressIPVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPeerTunnelAddressIPVersion.setStatus("current")
_EqlIpsecPeerTunnelAddress_Type = InetAddress
_EqlIpsecPeerTunnelAddress_Object = MibTableColumn
eqlIpsecPeerTunnelAddress = _EqlIpsecPeerTunnelAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 10),
    _EqlIpsecPeerTunnelAddress_Type()
)
eqlIpsecPeerTunnelAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPeerTunnelAddress.setStatus("current")


class _EqlIpsecPeerIkeV2_Type(TruthValue):
    """Custom type eqlIpsecPeerIkeV2 based on TruthValue"""


_EqlIpsecPeerIkeV2_Object = MibTableColumn
eqlIpsecPeerIkeV2 = _EqlIpsecPeerIkeV2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 11),
    _EqlIpsecPeerIkeV2_Type()
)
eqlIpsecPeerIkeV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPeerIkeV2.setStatus("current")


class _EqlIpsecPeerManualKeyEncAlg_Type(Integer32):
    """Custom type eqlIpsecPeerManualKeyEncAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              6,
              7,
              11,
              12,
              13,
              250)
        )
    )
    namedValues = NamedValues(
        *(("aes", 12),
          ("aes-ctr", 13),
          ("blowfish-cbc", 7),
          ("cast128-cbc", 6),
          ("des-cbc", 2),
          ("none", 0),
          ("null-enc", 11),
          ("skipjack", 250),
          ("triple-des-cbc", 3))
    )


_EqlIpsecPeerManualKeyEncAlg_Type.__name__ = "Integer32"
_EqlIpsecPeerManualKeyEncAlg_Object = MibTableColumn
eqlIpsecPeerManualKeyEncAlg = _EqlIpsecPeerManualKeyEncAlg_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 12),
    _EqlIpsecPeerManualKeyEncAlg_Type()
)
eqlIpsecPeerManualKeyEncAlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPeerManualKeyEncAlg.setStatus("current")


class _EqlIpsecPeerManualKeyEncKeyOut_Type(SnmpAdminString):
    """Custom type eqlIpsecPeerManualKeyEncKeyOut based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlIpsecPeerManualKeyEncKeyOut_Type.__name__ = "SnmpAdminString"
_EqlIpsecPeerManualKeyEncKeyOut_Object = MibTableColumn
eqlIpsecPeerManualKeyEncKeyOut = _EqlIpsecPeerManualKeyEncKeyOut_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 13),
    _EqlIpsecPeerManualKeyEncKeyOut_Type()
)
eqlIpsecPeerManualKeyEncKeyOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPeerManualKeyEncKeyOut.setStatus("current")


class _EqlIpsecPeerManualKeyEncKeyIn_Type(SnmpAdminString):
    """Custom type eqlIpsecPeerManualKeyEncKeyIn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlIpsecPeerManualKeyEncKeyIn_Type.__name__ = "SnmpAdminString"
_EqlIpsecPeerManualKeyEncKeyIn_Object = MibTableColumn
eqlIpsecPeerManualKeyEncKeyIn = _EqlIpsecPeerManualKeyEncKeyIn_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 14),
    _EqlIpsecPeerManualKeyEncKeyIn_Type()
)
eqlIpsecPeerManualKeyEncKeyIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPeerManualKeyEncKeyIn.setStatus("current")


class _EqlIpsecPeerManualKeyAuthAlg_Type(Integer32):
    """Custom type eqlIpsecPeerManualKeyAuthAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sha1", 1),
          ("sha256", 2))
    )


_EqlIpsecPeerManualKeyAuthAlg_Type.__name__ = "Integer32"
_EqlIpsecPeerManualKeyAuthAlg_Object = MibTableColumn
eqlIpsecPeerManualKeyAuthAlg = _EqlIpsecPeerManualKeyAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 15),
    _EqlIpsecPeerManualKeyAuthAlg_Type()
)
eqlIpsecPeerManualKeyAuthAlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPeerManualKeyAuthAlg.setStatus("current")


class _EqlIpsecPeerManualKeyAuthKeyOut_Type(SnmpAdminString):
    """Custom type eqlIpsecPeerManualKeyAuthKeyOut based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlIpsecPeerManualKeyAuthKeyOut_Type.__name__ = "SnmpAdminString"
_EqlIpsecPeerManualKeyAuthKeyOut_Object = MibTableColumn
eqlIpsecPeerManualKeyAuthKeyOut = _EqlIpsecPeerManualKeyAuthKeyOut_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 16),
    _EqlIpsecPeerManualKeyAuthKeyOut_Type()
)
eqlIpsecPeerManualKeyAuthKeyOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPeerManualKeyAuthKeyOut.setStatus("current")


class _EqlIpsecPeerManualKeyAuthKeyIn_Type(SnmpAdminString):
    """Custom type eqlIpsecPeerManualKeyAuthKeyIn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlIpsecPeerManualKeyAuthKeyIn_Type.__name__ = "SnmpAdminString"
_EqlIpsecPeerManualKeyAuthKeyIn_Object = MibTableColumn
eqlIpsecPeerManualKeyAuthKeyIn = _EqlIpsecPeerManualKeyAuthKeyIn_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 17),
    _EqlIpsecPeerManualKeyAuthKeyIn_Type()
)
eqlIpsecPeerManualKeyAuthKeyIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPeerManualKeyAuthKeyIn.setStatus("current")
_EqlIpsecPeerManualKeySpiOut_Type = Integer32
_EqlIpsecPeerManualKeySpiOut_Object = MibTableColumn
eqlIpsecPeerManualKeySpiOut = _EqlIpsecPeerManualKeySpiOut_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 18),
    _EqlIpsecPeerManualKeySpiOut_Type()
)
eqlIpsecPeerManualKeySpiOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPeerManualKeySpiOut.setStatus("current")
_EqlIpsecPeerManualKeySpiIn_Type = Integer32
_EqlIpsecPeerManualKeySpiIn_Object = MibTableColumn
eqlIpsecPeerManualKeySpiIn = _EqlIpsecPeerManualKeySpiIn_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 19),
    _EqlIpsecPeerManualKeySpiIn_Type()
)
eqlIpsecPeerManualKeySpiIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPeerManualKeySpiIn.setStatus("current")
_EqlIpsecPeerRowStatus_Type = RowStatus
_EqlIpsecPeerRowStatus_Object = MibTableColumn
eqlIpsecPeerRowStatus = _EqlIpsecPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 20),
    _EqlIpsecPeerRowStatus_Type()
)
eqlIpsecPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecPeerRowStatus.setStatus("current")
_EqlIpsecCertDisplayTable_Object = MibTable
eqlIpsecCertDisplayTable = _EqlIpsecCertDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 5)
)
if mibBuilder.loadTexts:
    eqlIpsecCertDisplayTable.setStatus("current")
_EqlIpsecCertDisplayEntry_Object = MibTableRow
eqlIpsecCertDisplayEntry = _EqlIpsecCertDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1)
)
eqlIpsecCertDisplayEntry.setIndexNames(
    (0, "EQLIPSEC-MIB", "eqlIpsecCertInstanceId"),
)
if mibBuilder.loadTexts:
    eqlIpsecCertDisplayEntry.setStatus("current")


class _EqlIpsecCertDisplayName_Type(SnmpAdminString):
    """Custom type eqlIpsecCertDisplayName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EqlIpsecCertDisplayName_Type.__name__ = "SnmpAdminString"
_EqlIpsecCertDisplayName_Object = MibTableColumn
eqlIpsecCertDisplayName = _EqlIpsecCertDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 1),
    _EqlIpsecCertDisplayName_Type()
)
eqlIpsecCertDisplayName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecCertDisplayName.setStatus("current")


class _EqlIpsecCertDisplayIssuedToDName_Type(SnmpAdminString):
    """Custom type eqlIpsecCertDisplayIssuedToDName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EqlIpsecCertDisplayIssuedToDName_Type.__name__ = "SnmpAdminString"
_EqlIpsecCertDisplayIssuedToDName_Object = MibTableColumn
eqlIpsecCertDisplayIssuedToDName = _EqlIpsecCertDisplayIssuedToDName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 2),
    _EqlIpsecCertDisplayIssuedToDName_Type()
)
eqlIpsecCertDisplayIssuedToDName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecCertDisplayIssuedToDName.setStatus("current")


class _EqlIpsecCertDisplaySerialNumber_Type(SnmpAdminString):
    """Custom type eqlIpsecCertDisplaySerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlIpsecCertDisplaySerialNumber_Type.__name__ = "SnmpAdminString"
_EqlIpsecCertDisplaySerialNumber_Object = MibTableColumn
eqlIpsecCertDisplaySerialNumber = _EqlIpsecCertDisplaySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 3),
    _EqlIpsecCertDisplaySerialNumber_Type()
)
eqlIpsecCertDisplaySerialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecCertDisplaySerialNumber.setStatus("current")


class _EqlIpsecCertDisplayIssuedByDName_Type(SnmpAdminString):
    """Custom type eqlIpsecCertDisplayIssuedByDName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EqlIpsecCertDisplayIssuedByDName_Type.__name__ = "SnmpAdminString"
_EqlIpsecCertDisplayIssuedByDName_Object = MibTableColumn
eqlIpsecCertDisplayIssuedByDName = _EqlIpsecCertDisplayIssuedByDName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 4),
    _EqlIpsecCertDisplayIssuedByDName_Type()
)
eqlIpsecCertDisplayIssuedByDName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecCertDisplayIssuedByDName.setStatus("current")


class _EqlIpsecCertDisplayIssuedOn_Type(SnmpAdminString):
    """Custom type eqlIpsecCertDisplayIssuedOn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlIpsecCertDisplayIssuedOn_Type.__name__ = "SnmpAdminString"
_EqlIpsecCertDisplayIssuedOn_Object = MibTableColumn
eqlIpsecCertDisplayIssuedOn = _EqlIpsecCertDisplayIssuedOn_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 5),
    _EqlIpsecCertDisplayIssuedOn_Type()
)
eqlIpsecCertDisplayIssuedOn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecCertDisplayIssuedOn.setStatus("current")


class _EqlIpsecCertDisplayExpiresOn_Type(SnmpAdminString):
    """Custom type eqlIpsecCertDisplayExpiresOn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlIpsecCertDisplayExpiresOn_Type.__name__ = "SnmpAdminString"
_EqlIpsecCertDisplayExpiresOn_Object = MibTableColumn
eqlIpsecCertDisplayExpiresOn = _EqlIpsecCertDisplayExpiresOn_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 6),
    _EqlIpsecCertDisplayExpiresOn_Type()
)
eqlIpsecCertDisplayExpiresOn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecCertDisplayExpiresOn.setStatus("current")


class _EqlIpsecCertDisplaySha1Fingerprint_Type(SnmpAdminString):
    """Custom type eqlIpsecCertDisplaySha1Fingerprint based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlIpsecCertDisplaySha1Fingerprint_Type.__name__ = "SnmpAdminString"
_EqlIpsecCertDisplaySha1Fingerprint_Object = MibTableColumn
eqlIpsecCertDisplaySha1Fingerprint = _EqlIpsecCertDisplaySha1Fingerprint_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 7),
    _EqlIpsecCertDisplaySha1Fingerprint_Type()
)
eqlIpsecCertDisplaySha1Fingerprint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecCertDisplaySha1Fingerprint.setStatus("current")


class _EqlIpsecCertDisplayMd5Fingerprint_Type(SnmpAdminString):
    """Custom type eqlIpsecCertDisplayMd5Fingerprint based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlIpsecCertDisplayMd5Fingerprint_Type.__name__ = "SnmpAdminString"
_EqlIpsecCertDisplayMd5Fingerprint_Object = MibTableColumn
eqlIpsecCertDisplayMd5Fingerprint = _EqlIpsecCertDisplayMd5Fingerprint_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 8),
    _EqlIpsecCertDisplayMd5Fingerprint_Type()
)
eqlIpsecCertDisplayMd5Fingerprint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecCertDisplayMd5Fingerprint.setStatus("current")


class _EqlIpsecCertDisplayLocal_Type(Integer32):
    """Custom type eqlIpsecCertDisplayLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("intermediate", 3),
          ("local-cert", 1),
          ("root-cert", 2))
    )


_EqlIpsecCertDisplayLocal_Type.__name__ = "Integer32"
_EqlIpsecCertDisplayLocal_Object = MibTableColumn
eqlIpsecCertDisplayLocal = _EqlIpsecCertDisplayLocal_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 9),
    _EqlIpsecCertDisplayLocal_Type()
)
eqlIpsecCertDisplayLocal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecCertDisplayLocal.setStatus("current")


class _EqlIpsecCertDisplayFormat_Type(Integer32):
    """Custom type eqlIpsecCertDisplayFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pkcs12", 2),
          ("x509", 1))
    )


_EqlIpsecCertDisplayFormat_Type.__name__ = "Integer32"
_EqlIpsecCertDisplayFormat_Object = MibTableColumn
eqlIpsecCertDisplayFormat = _EqlIpsecCertDisplayFormat_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 10),
    _EqlIpsecCertDisplayFormat_Type()
)
eqlIpsecCertDisplayFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecCertDisplayFormat.setStatus("current")


class _EqlIpsecCertDisplaySubAltName_Type(SnmpAdminString):
    """Custom type eqlIpsecCertDisplaySubAltName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EqlIpsecCertDisplaySubAltName_Type.__name__ = "SnmpAdminString"
_EqlIpsecCertDisplaySubAltName_Object = MibTableColumn
eqlIpsecCertDisplaySubAltName = _EqlIpsecCertDisplaySubAltName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 11),
    _EqlIpsecCertDisplaySubAltName_Type()
)
eqlIpsecCertDisplaySubAltName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecCertDisplaySubAltName.setStatus("current")
_EqlIpsecSecAssocTable_Object = MibTable
eqlIpsecSecAssocTable = _EqlIpsecSecAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 6)
)
if mibBuilder.loadTexts:
    eqlIpsecSecAssocTable.setStatus("current")
_EqlIpsecSecAssocEntry_Object = MibTableRow
eqlIpsecSecAssocEntry = _EqlIpsecSecAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1)
)
eqlIpsecSecAssocEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLIPSEC-MIB", "eqlIpsecSecAssocInstanceIdHigh"),
    (0, "EQLIPSEC-MIB", "eqlIpsecSecAssocInstanceIdLow"),
)
if mibBuilder.loadTexts:
    eqlIpsecSecAssocEntry.setStatus("current")
_EqlIpsecSecAssocInstanceIdHigh_Type = Unsigned32
_EqlIpsecSecAssocInstanceIdHigh_Object = MibTableColumn
eqlIpsecSecAssocInstanceIdHigh = _EqlIpsecSecAssocInstanceIdHigh_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 1),
    _EqlIpsecSecAssocInstanceIdHigh_Type()
)
eqlIpsecSecAssocInstanceIdHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlIpsecSecAssocInstanceIdHigh.setStatus("current")
_EqlIpsecSecAssocInstanceIdLow_Type = Unsigned32
_EqlIpsecSecAssocInstanceIdLow_Object = MibTableColumn
eqlIpsecSecAssocInstanceIdLow = _EqlIpsecSecAssocInstanceIdLow_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 2),
    _EqlIpsecSecAssocInstanceIdLow_Type()
)
eqlIpsecSecAssocInstanceIdLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlIpsecSecAssocInstanceIdLow.setStatus("current")
_EqlIpsecSecAssocSrcAddressIPVersion_Type = InetAddressType
_EqlIpsecSecAssocSrcAddressIPVersion_Object = MibTableColumn
eqlIpsecSecAssocSrcAddressIPVersion = _EqlIpsecSecAssocSrcAddressIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 3),
    _EqlIpsecSecAssocSrcAddressIPVersion_Type()
)
eqlIpsecSecAssocSrcAddressIPVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecSecAssocSrcAddressIPVersion.setStatus("current")
_EqlIpsecSecAssocSrcAddress_Type = InetAddress
_EqlIpsecSecAssocSrcAddress_Object = MibTableColumn
eqlIpsecSecAssocSrcAddress = _EqlIpsecSecAssocSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 4),
    _EqlIpsecSecAssocSrcAddress_Type()
)
eqlIpsecSecAssocSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecSecAssocSrcAddress.setStatus("current")
_EqlIpsecSecAssocDstAddressIPVersion_Type = InetAddressType
_EqlIpsecSecAssocDstAddressIPVersion_Object = MibTableColumn
eqlIpsecSecAssocDstAddressIPVersion = _EqlIpsecSecAssocDstAddressIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 5),
    _EqlIpsecSecAssocDstAddressIPVersion_Type()
)
eqlIpsecSecAssocDstAddressIPVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecSecAssocDstAddressIPVersion.setStatus("current")
_EqlIpsecSecAssocDstAddress_Type = InetAddress
_EqlIpsecSecAssocDstAddress_Object = MibTableColumn
eqlIpsecSecAssocDstAddress = _EqlIpsecSecAssocDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 6),
    _EqlIpsecSecAssocDstAddress_Type()
)
eqlIpsecSecAssocDstAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecSecAssocDstAddress.setStatus("current")


class _EqlIpsecSecAssocEncAlg_Type(Integer32):
    """Custom type eqlIpsecSecAssocEncAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              6,
              7,
              11,
              12,
              13,
              250)
        )
    )
    namedValues = NamedValues(
        *(("aes", 12),
          ("aes-ctr", 13),
          ("blowfish-cbc", 7),
          ("cast128-cbc", 6),
          ("des-cbc", 2),
          ("none", 0),
          ("null-enc", 11),
          ("skipjack", 250),
          ("triple-des-cbc", 3))
    )


_EqlIpsecSecAssocEncAlg_Type.__name__ = "Integer32"
_EqlIpsecSecAssocEncAlg_Object = MibTableColumn
eqlIpsecSecAssocEncAlg = _EqlIpsecSecAssocEncAlg_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 7),
    _EqlIpsecSecAssocEncAlg_Type()
)
eqlIpsecSecAssocEncAlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecSecAssocEncAlg.setStatus("current")


class _EqlIpsecSecAssocAuthAlg_Type(Integer32):
    """Custom type eqlIpsecSecAssocAuthAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              5,
              6,
              7,
              8,
              9,
              249,
              250,
              251,
              252)
        )
    )
    namedValues = NamedValues(
        *(("aes-xcbc-mac", 9),
          ("md5", 249),
          ("md5-hmac", 2),
          ("none", 0),
          ("null", 251),
          ("ripemd160-hmac", 8),
          ("sha", 250),
          ("sha1-hmac", 3),
          ("sha2-256", 5),
          ("sha2-384", 6),
          ("sha2-512", 7),
          ("tcp-md5", 252))
    )


_EqlIpsecSecAssocAuthAlg_Type.__name__ = "Integer32"
_EqlIpsecSecAssocAuthAlg_Object = MibTableColumn
eqlIpsecSecAssocAuthAlg = _EqlIpsecSecAssocAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 8),
    _EqlIpsecSecAssocAuthAlg_Type()
)
eqlIpsecSecAssocAuthAlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecSecAssocAuthAlg.setStatus("current")
_EqlIpsecSecAssocSpi_Type = Integer32
_EqlIpsecSecAssocSpi_Object = MibTableColumn
eqlIpsecSecAssocSpi = _EqlIpsecSecAssocSpi_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 9),
    _EqlIpsecSecAssocSpi_Type()
)
eqlIpsecSecAssocSpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecSecAssocSpi.setStatus("current")


class _EqlIpsecSecAssocEncKey_Type(SnmpAdminString):
    """Custom type eqlIpsecSecAssocEncKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlIpsecSecAssocEncKey_Type.__name__ = "SnmpAdminString"
_EqlIpsecSecAssocEncKey_Object = MibTableColumn
eqlIpsecSecAssocEncKey = _EqlIpsecSecAssocEncKey_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 10),
    _EqlIpsecSecAssocEncKey_Type()
)
eqlIpsecSecAssocEncKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecSecAssocEncKey.setStatus("current")


class _EqlIpsecSecAssocAuthKey_Type(SnmpAdminString):
    """Custom type eqlIpsecSecAssocAuthKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlIpsecSecAssocAuthKey_Type.__name__ = "SnmpAdminString"
_EqlIpsecSecAssocAuthKey_Object = MibTableColumn
eqlIpsecSecAssocAuthKey = _EqlIpsecSecAssocAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 11),
    _EqlIpsecSecAssocAuthKey_Type()
)
eqlIpsecSecAssocAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecSecAssocAuthKey.setStatus("current")
_EqlIpsecSecAssocManual_Type = TruthValue
_EqlIpsecSecAssocManual_Object = MibTableColumn
eqlIpsecSecAssocManual = _EqlIpsecSecAssocManual_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 12),
    _EqlIpsecSecAssocManual_Type()
)
eqlIpsecSecAssocManual.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecSecAssocManual.setStatus("current")
_EqlIpsecStaleSecAssocDeleteTable_Object = MibTable
eqlIpsecStaleSecAssocDeleteTable = _EqlIpsecStaleSecAssocDeleteTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 7)
)
if mibBuilder.loadTexts:
    eqlIpsecStaleSecAssocDeleteTable.setStatus("current")
_EqlIpsecStaleSecAssocDeleteEntry_Object = MibTableRow
eqlIpsecStaleSecAssocDeleteEntry = _EqlIpsecStaleSecAssocDeleteEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 7, 1)
)
eqlIpsecStaleSecAssocDeleteEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLIPSEC-MIB", "eqlIpsecStaleSecAssocDeleteInstanceId"),
)
if mibBuilder.loadTexts:
    eqlIpsecStaleSecAssocDeleteEntry.setStatus("current")
_EqlIpsecStaleSecAssocDeleteInstanceId_Type = Integer32
_EqlIpsecStaleSecAssocDeleteInstanceId_Object = MibTableColumn
eqlIpsecStaleSecAssocDeleteInstanceId = _EqlIpsecStaleSecAssocDeleteInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 7, 1, 1),
    _EqlIpsecStaleSecAssocDeleteInstanceId_Type()
)
eqlIpsecStaleSecAssocDeleteInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlIpsecStaleSecAssocDeleteInstanceId.setStatus("current")
_EqlIpsecStaleSecAssocDeleteDestAddressIPVersion_Type = InetAddressType
_EqlIpsecStaleSecAssocDeleteDestAddressIPVersion_Object = MibTableColumn
eqlIpsecStaleSecAssocDeleteDestAddressIPVersion = _EqlIpsecStaleSecAssocDeleteDestAddressIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 7, 1, 2),
    _EqlIpsecStaleSecAssocDeleteDestAddressIPVersion_Type()
)
eqlIpsecStaleSecAssocDeleteDestAddressIPVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecStaleSecAssocDeleteDestAddressIPVersion.setStatus("current")
_EqlIpsecStaleSecAssocDeleteDestAddress_Type = InetAddress
_EqlIpsecStaleSecAssocDeleteDestAddress_Object = MibTableColumn
eqlIpsecStaleSecAssocDeleteDestAddress = _EqlIpsecStaleSecAssocDeleteDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 7, 1, 3),
    _EqlIpsecStaleSecAssocDeleteDestAddress_Type()
)
eqlIpsecStaleSecAssocDeleteDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecStaleSecAssocDeleteDestAddress.setStatus("current")
_EqlIpsecStaleSecAssocDeleteRowStatus_Type = RowStatus
_EqlIpsecStaleSecAssocDeleteRowStatus_Object = MibTableColumn
eqlIpsecStaleSecAssocDeleteRowStatus = _EqlIpsecStaleSecAssocDeleteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 22, 1, 7, 1, 4),
    _EqlIpsecStaleSecAssocDeleteRowStatus_Type()
)
eqlIpsecStaleSecAssocDeleteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpsecStaleSecAssocDeleteRowStatus.setStatus("current")
_EqlIpsecNotifications_ObjectIdentity = ObjectIdentity
eqlIpsecNotifications = _EqlIpsecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 22, 2)
)
_EqlIpsecConformance_ObjectIdentity = ObjectIdentity
eqlIpsecConformance = _EqlIpsecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 22, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLIPSEC-MIB",
    **{"SnmpAdminString": SnmpAdminString,
       "InetPortNumber": InetPortNumber,
       "IpsecAuthType": IpsecAuthType,
       "IpsecIdType": IpsecIdType,
       "IpsecEncType": IpsecEncType,
       "eqlIpsecModule": eqlIpsecModule,
       "eqlIpsecObjects": eqlIpsecObjects,
       "eqlIpsecTable": eqlIpsecTable,
       "eqlIpsecEntry": eqlIpsecEntry,
       "eqlIpsecInstanceId": eqlIpsecInstanceId,
       "eqlIpsecEnable": eqlIpsecEnable,
       "eqlIpsecRowStatus": eqlIpsecRowStatus,
       "eqlIpsecPolicyTable": eqlIpsecPolicyTable,
       "eqlIpsecPolicyEntry": eqlIpsecPolicyEntry,
       "eqlIpsecPolicyInstanceId": eqlIpsecPolicyInstanceId,
       "eqlIpsecPolicyFilterName": eqlIpsecPolicyFilterName,
       "eqlIpsecPolicyFilterIPVersion": eqlIpsecPolicyFilterIPVersion,
       "eqlIpsecPolicyFilterAddress": eqlIpsecPolicyFilterAddress,
       "eqlIpsecPolicyFilterNetmaskLen": eqlIpsecPolicyFilterNetmaskLen,
       "eqlIpsecPolicyFilterLocalAddress": eqlIpsecPolicyFilterLocalAddress,
       "eqlIpsecPolicyFilterPort": eqlIpsecPolicyFilterPort,
       "eqlIpsecPolicyFilterLocalPort": eqlIpsecPolicyFilterLocalPort,
       "eqlIpsecPolicyFilterProtocol": eqlIpsecPolicyFilterProtocol,
       "eqlIpsecPolicyFilterPeerName": eqlIpsecPolicyFilterPeerName,
       "eqlIpsecPolicyFilterAction": eqlIpsecPolicyFilterAction,
       "eqlIpsecPolicyFilterRowStatus": eqlIpsecPolicyFilterRowStatus,
       "eqlIpsecCertConfigTable": eqlIpsecCertConfigTable,
       "eqlIpsecCertConfigEntry": eqlIpsecCertConfigEntry,
       "eqlIpsecCertInstanceId": eqlIpsecCertInstanceId,
       "eqlIpsecCertName": eqlIpsecCertName,
       "eqlIpsecCertFileName": eqlIpsecCertFileName,
       "eqlIpsecCertType": eqlIpsecCertType,
       "eqlIpsecPrivKeyFileName": eqlIpsecPrivKeyFileName,
       "eqlIpsecCertPassword": eqlIpsecCertPassword,
       "eqlIpsecCertRowStatus": eqlIpsecCertRowStatus,
       "eqlIpsecPeerTable": eqlIpsecPeerTable,
       "eqlIpsecPeerEntry": eqlIpsecPeerEntry,
       "eqlIpsecPeerInstanceId": eqlIpsecPeerInstanceId,
       "eqlIpsecPeerName": eqlIpsecPeerName,
       "eqlIpsecPeerAuthType": eqlIpsecPeerAuthType,
       "eqlIpsecPeerPreSharedKey": eqlIpsecPeerPreSharedKey,
       "eqlIpsecPeerCertIdType": eqlIpsecPeerCertIdType,
       "eqlIpsecPeerCertIdValue": eqlIpsecPeerCertIdValue,
       "eqlIpsecPeerNullEnc": eqlIpsecPeerNullEnc,
       "eqlIpsecPeerTunnelMode": eqlIpsecPeerTunnelMode,
       "eqlIpsecPeerTunnelAddressIPVersion": eqlIpsecPeerTunnelAddressIPVersion,
       "eqlIpsecPeerTunnelAddress": eqlIpsecPeerTunnelAddress,
       "eqlIpsecPeerIkeV2": eqlIpsecPeerIkeV2,
       "eqlIpsecPeerManualKeyEncAlg": eqlIpsecPeerManualKeyEncAlg,
       "eqlIpsecPeerManualKeyEncKeyOut": eqlIpsecPeerManualKeyEncKeyOut,
       "eqlIpsecPeerManualKeyEncKeyIn": eqlIpsecPeerManualKeyEncKeyIn,
       "eqlIpsecPeerManualKeyAuthAlg": eqlIpsecPeerManualKeyAuthAlg,
       "eqlIpsecPeerManualKeyAuthKeyOut": eqlIpsecPeerManualKeyAuthKeyOut,
       "eqlIpsecPeerManualKeyAuthKeyIn": eqlIpsecPeerManualKeyAuthKeyIn,
       "eqlIpsecPeerManualKeySpiOut": eqlIpsecPeerManualKeySpiOut,
       "eqlIpsecPeerManualKeySpiIn": eqlIpsecPeerManualKeySpiIn,
       "eqlIpsecPeerRowStatus": eqlIpsecPeerRowStatus,
       "eqlIpsecCertDisplayTable": eqlIpsecCertDisplayTable,
       "eqlIpsecCertDisplayEntry": eqlIpsecCertDisplayEntry,
       "eqlIpsecCertDisplayName": eqlIpsecCertDisplayName,
       "eqlIpsecCertDisplayIssuedToDName": eqlIpsecCertDisplayIssuedToDName,
       "eqlIpsecCertDisplaySerialNumber": eqlIpsecCertDisplaySerialNumber,
       "eqlIpsecCertDisplayIssuedByDName": eqlIpsecCertDisplayIssuedByDName,
       "eqlIpsecCertDisplayIssuedOn": eqlIpsecCertDisplayIssuedOn,
       "eqlIpsecCertDisplayExpiresOn": eqlIpsecCertDisplayExpiresOn,
       "eqlIpsecCertDisplaySha1Fingerprint": eqlIpsecCertDisplaySha1Fingerprint,
       "eqlIpsecCertDisplayMd5Fingerprint": eqlIpsecCertDisplayMd5Fingerprint,
       "eqlIpsecCertDisplayLocal": eqlIpsecCertDisplayLocal,
       "eqlIpsecCertDisplayFormat": eqlIpsecCertDisplayFormat,
       "eqlIpsecCertDisplaySubAltName": eqlIpsecCertDisplaySubAltName,
       "eqlIpsecSecAssocTable": eqlIpsecSecAssocTable,
       "eqlIpsecSecAssocEntry": eqlIpsecSecAssocEntry,
       "eqlIpsecSecAssocInstanceIdHigh": eqlIpsecSecAssocInstanceIdHigh,
       "eqlIpsecSecAssocInstanceIdLow": eqlIpsecSecAssocInstanceIdLow,
       "eqlIpsecSecAssocSrcAddressIPVersion": eqlIpsecSecAssocSrcAddressIPVersion,
       "eqlIpsecSecAssocSrcAddress": eqlIpsecSecAssocSrcAddress,
       "eqlIpsecSecAssocDstAddressIPVersion": eqlIpsecSecAssocDstAddressIPVersion,
       "eqlIpsecSecAssocDstAddress": eqlIpsecSecAssocDstAddress,
       "eqlIpsecSecAssocEncAlg": eqlIpsecSecAssocEncAlg,
       "eqlIpsecSecAssocAuthAlg": eqlIpsecSecAssocAuthAlg,
       "eqlIpsecSecAssocSpi": eqlIpsecSecAssocSpi,
       "eqlIpsecSecAssocEncKey": eqlIpsecSecAssocEncKey,
       "eqlIpsecSecAssocAuthKey": eqlIpsecSecAssocAuthKey,
       "eqlIpsecSecAssocManual": eqlIpsecSecAssocManual,
       "eqlIpsecStaleSecAssocDeleteTable": eqlIpsecStaleSecAssocDeleteTable,
       "eqlIpsecStaleSecAssocDeleteEntry": eqlIpsecStaleSecAssocDeleteEntry,
       "eqlIpsecStaleSecAssocDeleteInstanceId": eqlIpsecStaleSecAssocDeleteInstanceId,
       "eqlIpsecStaleSecAssocDeleteDestAddressIPVersion": eqlIpsecStaleSecAssocDeleteDestAddressIPVersion,
       "eqlIpsecStaleSecAssocDeleteDestAddress": eqlIpsecStaleSecAssocDeleteDestAddress,
       "eqlIpsecStaleSecAssocDeleteRowStatus": eqlIpsecStaleSecAssocDeleteRowStatus,
       "eqlIpsecNotifications": eqlIpsecNotifications,
       "eqlIpsecConformance": eqlIpsecConformance}
)
