# SNMP MIB module (IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPSEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:13 2024
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
 experimental,
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
    "experimental",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ipsecMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 500)
)
ipsecMIB.setRevisions(
        ("1999-01-25 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpsecMIBObjects_ObjectIdentity = ObjectIdentity
ipsecMIBObjects = _IpsecMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 500, 1)
)
_Ipsec_ObjectIdentity = ObjectIdentity
ipsec = _Ipsec_ObjectIdentity(
    (1, 3, 6, 1, 3, 500, 1, 1)
)
_IpsecProtSuiteTable_Object = MibTable
ipsecProtSuiteTable = _IpsecProtSuiteTable_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipsecProtSuiteTable.setStatus("current")
_IpsecProtSuiteEntry_Object = MibTableRow
ipsecProtSuiteEntry = _IpsecProtSuiteEntry_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1)
)
ipsecProtSuiteEntry.setIndexNames(
    (0, "IPSEC-MIB", "ipsecProtSuiteIndex"),
)
if mibBuilder.loadTexts:
    ipsecProtSuiteEntry.setStatus("current")


class _IpsecProtSuiteIndex_Type(Integer32):
    """Custom type ipsecProtSuiteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpsecProtSuiteIndex_Type.__name__ = "Integer32"
_IpsecProtSuiteIndex_Object = MibTableColumn
ipsecProtSuiteIndex = _IpsecProtSuiteIndex_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 1),
    _IpsecProtSuiteIndex_Type()
)
ipsecProtSuiteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteIndex.setStatus("current")


class _IpsecProtSuiteLocalAddress_Type(OctetString):
    """Custom type ipsecProtSuiteLocalAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IpsecProtSuiteLocalAddress_Type.__name__ = "OctetString"
_IpsecProtSuiteLocalAddress_Object = MibTableColumn
ipsecProtSuiteLocalAddress = _IpsecProtSuiteLocalAddress_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 2),
    _IpsecProtSuiteLocalAddress_Type()
)
ipsecProtSuiteLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteLocalAddress.setStatus("current")


class _IpsecProtSuiteRemoteAddress_Type(OctetString):
    """Custom type ipsecProtSuiteRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IpsecProtSuiteRemoteAddress_Type.__name__ = "OctetString"
_IpsecProtSuiteRemoteAddress_Object = MibTableColumn
ipsecProtSuiteRemoteAddress = _IpsecProtSuiteRemoteAddress_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 3),
    _IpsecProtSuiteRemoteAddress_Type()
)
ipsecProtSuiteRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteRemoteAddress.setStatus("current")


class _IpsecProtSuiteInboundEspSpi_Type(Unsigned32):
    """Custom type ipsecProtSuiteInboundEspSpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpsecProtSuiteInboundEspSpi_Type.__name__ = "Unsigned32"
_IpsecProtSuiteInboundEspSpi_Object = MibTableColumn
ipsecProtSuiteInboundEspSpi = _IpsecProtSuiteInboundEspSpi_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 4),
    _IpsecProtSuiteInboundEspSpi_Type()
)
ipsecProtSuiteInboundEspSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteInboundEspSpi.setStatus("current")


class _IpsecProtSuiteOutboundEspSpi_Type(Unsigned32):
    """Custom type ipsecProtSuiteOutboundEspSpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpsecProtSuiteOutboundEspSpi_Type.__name__ = "Unsigned32"
_IpsecProtSuiteOutboundEspSpi_Object = MibTableColumn
ipsecProtSuiteOutboundEspSpi = _IpsecProtSuiteOutboundEspSpi_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 5),
    _IpsecProtSuiteOutboundEspSpi_Type()
)
ipsecProtSuiteOutboundEspSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteOutboundEspSpi.setStatus("current")


class _IpsecProtSuiteInboundAhSpi_Type(Unsigned32):
    """Custom type ipsecProtSuiteInboundAhSpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpsecProtSuiteInboundAhSpi_Type.__name__ = "Unsigned32"
_IpsecProtSuiteInboundAhSpi_Object = MibTableColumn
ipsecProtSuiteInboundAhSpi = _IpsecProtSuiteInboundAhSpi_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 6),
    _IpsecProtSuiteInboundAhSpi_Type()
)
ipsecProtSuiteInboundAhSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteInboundAhSpi.setStatus("current")


class _IpsecProtSuiteOutboundAhSpi_Type(Unsigned32):
    """Custom type ipsecProtSuiteOutboundAhSpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpsecProtSuiteOutboundAhSpi_Type.__name__ = "Unsigned32"
_IpsecProtSuiteOutboundAhSpi_Object = MibTableColumn
ipsecProtSuiteOutboundAhSpi = _IpsecProtSuiteOutboundAhSpi_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 7),
    _IpsecProtSuiteOutboundAhSpi_Type()
)
ipsecProtSuiteOutboundAhSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteOutboundAhSpi.setStatus("current")


class _IpsecProtSuiteInboundCompCpi_Type(Integer32):
    """Custom type ipsecProtSuiteInboundCompCpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecProtSuiteInboundCompCpi_Type.__name__ = "Integer32"
_IpsecProtSuiteInboundCompCpi_Object = MibTableColumn
ipsecProtSuiteInboundCompCpi = _IpsecProtSuiteInboundCompCpi_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 8),
    _IpsecProtSuiteInboundCompCpi_Type()
)
ipsecProtSuiteInboundCompCpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteInboundCompCpi.setStatus("current")


class _IpsecProtSuiteOutboundCompCpi_Type(Integer32):
    """Custom type ipsecProtSuiteOutboundCompCpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecProtSuiteOutboundCompCpi_Type.__name__ = "Integer32"
_IpsecProtSuiteOutboundCompCpi_Object = MibTableColumn
ipsecProtSuiteOutboundCompCpi = _IpsecProtSuiteOutboundCompCpi_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 9),
    _IpsecProtSuiteOutboundCompCpi_Type()
)
ipsecProtSuiteOutboundCompCpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteOutboundCompCpi.setStatus("current")


class _IpsecProtSuiteLocalId_Type(OctetString):
    """Custom type ipsecProtSuiteLocalId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_IpsecProtSuiteLocalId_Type.__name__ = "OctetString"
_IpsecProtSuiteLocalId_Object = MibTableColumn
ipsecProtSuiteLocalId = _IpsecProtSuiteLocalId_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 10),
    _IpsecProtSuiteLocalId_Type()
)
ipsecProtSuiteLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteLocalId.setStatus("current")
_IpsecProtSuiteLocalIdType_Type = Unsigned32
_IpsecProtSuiteLocalIdType_Object = MibTableColumn
ipsecProtSuiteLocalIdType = _IpsecProtSuiteLocalIdType_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 11),
    _IpsecProtSuiteLocalIdType_Type()
)
ipsecProtSuiteLocalIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteLocalIdType.setStatus("current")


class _IpsecProtSuiteRemoteId_Type(OctetString):
    """Custom type ipsecProtSuiteRemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_IpsecProtSuiteRemoteId_Type.__name__ = "OctetString"
_IpsecProtSuiteRemoteId_Object = MibTableColumn
ipsecProtSuiteRemoteId = _IpsecProtSuiteRemoteId_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 12),
    _IpsecProtSuiteRemoteId_Type()
)
ipsecProtSuiteRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteRemoteId.setStatus("current")
_IpsecProtSuiteRemoteIdType_Type = Unsigned32
_IpsecProtSuiteRemoteIdType_Object = MibTableColumn
ipsecProtSuiteRemoteIdType = _IpsecProtSuiteRemoteIdType_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 13),
    _IpsecProtSuiteRemoteIdType_Type()
)
ipsecProtSuiteRemoteIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteRemoteIdType.setStatus("current")


class _IpsecProtSuiteProtocol_Type(Integer32):
    """Custom type ipsecProtSuiteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpsecProtSuiteProtocol_Type.__name__ = "Integer32"
_IpsecProtSuiteProtocol_Object = MibTableColumn
ipsecProtSuiteProtocol = _IpsecProtSuiteProtocol_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 14),
    _IpsecProtSuiteProtocol_Type()
)
ipsecProtSuiteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteProtocol.setStatus("current")


class _IpsecProtSuiteLocalPort_Type(Integer32):
    """Custom type ipsecProtSuiteLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecProtSuiteLocalPort_Type.__name__ = "Integer32"
_IpsecProtSuiteLocalPort_Object = MibTableColumn
ipsecProtSuiteLocalPort = _IpsecProtSuiteLocalPort_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 15),
    _IpsecProtSuiteLocalPort_Type()
)
ipsecProtSuiteLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteLocalPort.setStatus("current")


class _IpsecProtSuiteRemotePort_Type(Integer32):
    """Custom type ipsecProtSuiteRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecProtSuiteRemotePort_Type.__name__ = "Integer32"
_IpsecProtSuiteRemotePort_Object = MibTableColumn
ipsecProtSuiteRemotePort = _IpsecProtSuiteRemotePort_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 16),
    _IpsecProtSuiteRemotePort_Type()
)
ipsecProtSuiteRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteRemotePort.setStatus("current")
_IpsecProtSuiteDifHelGroupDesc_Type = Integer32
_IpsecProtSuiteDifHelGroupDesc_Object = MibTableColumn
ipsecProtSuiteDifHelGroupDesc = _IpsecProtSuiteDifHelGroupDesc_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 17),
    _IpsecProtSuiteDifHelGroupDesc_Type()
)
ipsecProtSuiteDifHelGroupDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteDifHelGroupDesc.setStatus("current")
_IpsecProtSuiteDifHelGroupType_Type = Integer32
_IpsecProtSuiteDifHelGroupType_Object = MibTableColumn
ipsecProtSuiteDifHelGroupType = _IpsecProtSuiteDifHelGroupType_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 18),
    _IpsecProtSuiteDifHelGroupType_Type()
)
ipsecProtSuiteDifHelGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteDifHelGroupType.setStatus("current")
_IpsecProtSuitePFS_Type = TruthValue
_IpsecProtSuitePFS_Object = MibTableColumn
ipsecProtSuitePFS = _IpsecProtSuitePFS_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 19),
    _IpsecProtSuitePFS_Type()
)
ipsecProtSuitePFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuitePFS.setStatus("current")


class _IpsecProtSuiteEncapsulation_Type(Integer32):
    """Custom type ipsecProtSuiteEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 1),
          ("tunnel", 2))
    )


_IpsecProtSuiteEncapsulation_Type.__name__ = "Integer32"
_IpsecProtSuiteEncapsulation_Object = MibTableColumn
ipsecProtSuiteEncapsulation = _IpsecProtSuiteEncapsulation_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 20),
    _IpsecProtSuiteEncapsulation_Type()
)
ipsecProtSuiteEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteEncapsulation.setStatus("current")


class _IpsecProtSuiteEspEncAlg_Type(Integer32):
    """Custom type ipsecProtSuiteEspEncAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpsecProtSuiteEspEncAlg_Type.__name__ = "Integer32"
_IpsecProtSuiteEspEncAlg_Object = MibTableColumn
ipsecProtSuiteEspEncAlg = _IpsecProtSuiteEspEncAlg_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 21),
    _IpsecProtSuiteEspEncAlg_Type()
)
ipsecProtSuiteEspEncAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteEspEncAlg.setStatus("current")
_IpsecProtSuiteEspEncKeyLength_Type = Unsigned32
_IpsecProtSuiteEspEncKeyLength_Object = MibTableColumn
ipsecProtSuiteEspEncKeyLength = _IpsecProtSuiteEspEncKeyLength_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 22),
    _IpsecProtSuiteEspEncKeyLength_Type()
)
ipsecProtSuiteEspEncKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteEspEncKeyLength.setStatus("current")


class _IpsecProtSuiteEspAuthAlg_Type(Integer32):
    """Custom type ipsecProtSuiteEspAuthAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpsecProtSuiteEspAuthAlg_Type.__name__ = "Integer32"
_IpsecProtSuiteEspAuthAlg_Object = MibTableColumn
ipsecProtSuiteEspAuthAlg = _IpsecProtSuiteEspAuthAlg_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 23),
    _IpsecProtSuiteEspAuthAlg_Type()
)
ipsecProtSuiteEspAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteEspAuthAlg.setStatus("current")


class _IpsecProtSuiteAhAuthAlg_Type(Integer32):
    """Custom type ipsecProtSuiteAhAuthAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpsecProtSuiteAhAuthAlg_Type.__name__ = "Integer32"
_IpsecProtSuiteAhAuthAlg_Object = MibTableColumn
ipsecProtSuiteAhAuthAlg = _IpsecProtSuiteAhAuthAlg_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 24),
    _IpsecProtSuiteAhAuthAlg_Type()
)
ipsecProtSuiteAhAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteAhAuthAlg.setStatus("current")


class _IpsecProtSuiteCompAlg_Type(Integer32):
    """Custom type ipsecProtSuiteCompAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpsecProtSuiteCompAlg_Type.__name__ = "Integer32"
_IpsecProtSuiteCompAlg_Object = MibTableColumn
ipsecProtSuiteCompAlg = _IpsecProtSuiteCompAlg_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 25),
    _IpsecProtSuiteCompAlg_Type()
)
ipsecProtSuiteCompAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteCompAlg.setStatus("current")
_IpsecProtSuiteCreationTime_Type = DateAndTime
_IpsecProtSuiteCreationTime_Object = MibTableColumn
ipsecProtSuiteCreationTime = _IpsecProtSuiteCreationTime_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 26),
    _IpsecProtSuiteCreationTime_Type()
)
ipsecProtSuiteCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteCreationTime.setStatus("current")


class _IpsecProtSuiteTimeLimit_Type(OctetString):
    """Custom type ipsecProtSuiteTimeLimit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_IpsecProtSuiteTimeLimit_Type.__name__ = "OctetString"
_IpsecProtSuiteTimeLimit_Object = MibTableColumn
ipsecProtSuiteTimeLimit = _IpsecProtSuiteTimeLimit_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 27),
    _IpsecProtSuiteTimeLimit_Type()
)
ipsecProtSuiteTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteTimeLimit.setStatus("current")


class _IpsecProtSuiteTrafficLimit_Type(OctetString):
    """Custom type ipsecProtSuiteTrafficLimit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_IpsecProtSuiteTrafficLimit_Type.__name__ = "OctetString"
_IpsecProtSuiteTrafficLimit_Object = MibTableColumn
ipsecProtSuiteTrafficLimit = _IpsecProtSuiteTrafficLimit_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 28),
    _IpsecProtSuiteTrafficLimit_Type()
)
ipsecProtSuiteTrafficLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteTrafficLimit.setStatus("current")
if mibBuilder.loadTexts:
    ipsecProtSuiteTrafficLimit.setUnits("1024-byte blocks")


class _IpsecProtSuiteInTrafficCount_Type(OctetString):
    """Custom type ipsecProtSuiteInTrafficCount based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_IpsecProtSuiteInTrafficCount_Type.__name__ = "OctetString"
_IpsecProtSuiteInTrafficCount_Object = MibTableColumn
ipsecProtSuiteInTrafficCount = _IpsecProtSuiteInTrafficCount_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 29),
    _IpsecProtSuiteInTrafficCount_Type()
)
ipsecProtSuiteInTrafficCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteInTrafficCount.setStatus("current")
if mibBuilder.loadTexts:
    ipsecProtSuiteInTrafficCount.setUnits("1024-byte blocks")


class _IpsecProtSuiteOutTrafficCount_Type(OctetString):
    """Custom type ipsecProtSuiteOutTrafficCount based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_IpsecProtSuiteOutTrafficCount_Type.__name__ = "OctetString"
_IpsecProtSuiteOutTrafficCount_Object = MibTableColumn
ipsecProtSuiteOutTrafficCount = _IpsecProtSuiteOutTrafficCount_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 30),
    _IpsecProtSuiteOutTrafficCount_Type()
)
ipsecProtSuiteOutTrafficCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteOutTrafficCount.setStatus("current")
if mibBuilder.loadTexts:
    ipsecProtSuiteOutTrafficCount.setUnits("1024-byte blocks")
_IpsecProtSuiteInboundTraffic_Type = Counter64
_IpsecProtSuiteInboundTraffic_Object = MibTableColumn
ipsecProtSuiteInboundTraffic = _IpsecProtSuiteInboundTraffic_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 31),
    _IpsecProtSuiteInboundTraffic_Type()
)
ipsecProtSuiteInboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteInboundTraffic.setStatus("current")
if mibBuilder.loadTexts:
    ipsecProtSuiteInboundTraffic.setUnits("bytes")
_IpsecProtSuiteOutboundTraffic_Type = Counter64
_IpsecProtSuiteOutboundTraffic_Object = MibTableColumn
ipsecProtSuiteOutboundTraffic = _IpsecProtSuiteOutboundTraffic_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 32),
    _IpsecProtSuiteOutboundTraffic_Type()
)
ipsecProtSuiteOutboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteOutboundTraffic.setStatus("current")
if mibBuilder.loadTexts:
    ipsecProtSuiteOutboundTraffic.setUnits("bytes")
_IpsecProtSuiteInboundPackets_Type = Counter64
_IpsecProtSuiteInboundPackets_Object = MibTableColumn
ipsecProtSuiteInboundPackets = _IpsecProtSuiteInboundPackets_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 33),
    _IpsecProtSuiteInboundPackets_Type()
)
ipsecProtSuiteInboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteInboundPackets.setStatus("current")
_IpsecProtSuiteOutboundPackets_Type = Counter64
_IpsecProtSuiteOutboundPackets_Object = MibTableColumn
ipsecProtSuiteOutboundPackets = _IpsecProtSuiteOutboundPackets_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 34),
    _IpsecProtSuiteOutboundPackets_Type()
)
ipsecProtSuiteOutboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteOutboundPackets.setStatus("current")
_IpsecProtSuiteDecryptErrors_Type = Counter32
_IpsecProtSuiteDecryptErrors_Object = MibTableColumn
ipsecProtSuiteDecryptErrors = _IpsecProtSuiteDecryptErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 35),
    _IpsecProtSuiteDecryptErrors_Type()
)
ipsecProtSuiteDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteDecryptErrors.setStatus("current")
_IpsecProtSuiteAuthErrors_Type = Counter32
_IpsecProtSuiteAuthErrors_Object = MibTableColumn
ipsecProtSuiteAuthErrors = _IpsecProtSuiteAuthErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 36),
    _IpsecProtSuiteAuthErrors_Type()
)
ipsecProtSuiteAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteAuthErrors.setStatus("current")
_IpsecProtSuiteReplayErrors_Type = Counter32
_IpsecProtSuiteReplayErrors_Object = MibTableColumn
ipsecProtSuiteReplayErrors = _IpsecProtSuiteReplayErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 37),
    _IpsecProtSuiteReplayErrors_Type()
)
ipsecProtSuiteReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteReplayErrors.setStatus("current")
_IpsecProtSuitePolicyErrors_Type = Counter32
_IpsecProtSuitePolicyErrors_Object = MibTableColumn
ipsecProtSuitePolicyErrors = _IpsecProtSuitePolicyErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 38),
    _IpsecProtSuitePolicyErrors_Type()
)
ipsecProtSuitePolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuitePolicyErrors.setStatus("current")
_IpsecProtSuiteOtherReceiveErrors_Type = Counter32
_IpsecProtSuiteOtherReceiveErrors_Object = MibTableColumn
ipsecProtSuiteOtherReceiveErrors = _IpsecProtSuiteOtherReceiveErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 39),
    _IpsecProtSuiteOtherReceiveErrors_Type()
)
ipsecProtSuiteOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteOtherReceiveErrors.setStatus("current")
_IpsecProtSuiteSendErrors_Type = Counter32
_IpsecProtSuiteSendErrors_Object = MibTableColumn
ipsecProtSuiteSendErrors = _IpsecProtSuiteSendErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 1, 1, 40),
    _IpsecProtSuiteSendErrors_Type()
)
ipsecProtSuiteSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecProtSuiteSendErrors.setStatus("current")
_IpsecIkeSaTable_Object = MibTable
ipsecIkeSaTable = _IpsecIkeSaTable_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipsecIkeSaTable.setStatus("current")
_IpsecIkeSaEntry_Object = MibTableRow
ipsecIkeSaEntry = _IpsecIkeSaEntry_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1)
)
ipsecIkeSaEntry.setIndexNames(
    (0, "IPSEC-MIB", "ipsecIkeSaIndex"),
)
if mibBuilder.loadTexts:
    ipsecIkeSaEntry.setStatus("current")


class _IpsecIkeSaIndex_Type(Integer32):
    """Custom type ipsecIkeSaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_IpsecIkeSaIndex_Type.__name__ = "Integer32"
_IpsecIkeSaIndex_Object = MibTableColumn
ipsecIkeSaIndex = _IpsecIkeSaIndex_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 1),
    _IpsecIkeSaIndex_Type()
)
ipsecIkeSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaIndex.setStatus("current")


class _IpsecIkeSaInitiatorCookie_Type(OctetString):
    """Custom type ipsecIkeSaInitiatorCookie based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_IpsecIkeSaInitiatorCookie_Type.__name__ = "OctetString"
_IpsecIkeSaInitiatorCookie_Object = MibTableColumn
ipsecIkeSaInitiatorCookie = _IpsecIkeSaInitiatorCookie_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 2),
    _IpsecIkeSaInitiatorCookie_Type()
)
ipsecIkeSaInitiatorCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaInitiatorCookie.setStatus("current")


class _IpsecIkeSaResponderCookie_Type(OctetString):
    """Custom type ipsecIkeSaResponderCookie based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_IpsecIkeSaResponderCookie_Type.__name__ = "OctetString"
_IpsecIkeSaResponderCookie_Object = MibTableColumn
ipsecIkeSaResponderCookie = _IpsecIkeSaResponderCookie_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 3),
    _IpsecIkeSaResponderCookie_Type()
)
ipsecIkeSaResponderCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaResponderCookie.setStatus("current")


class _IpsecIkeSaLocalIpAddress_Type(OctetString):
    """Custom type ipsecIkeSaLocalIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IpsecIkeSaLocalIpAddress_Type.__name__ = "OctetString"
_IpsecIkeSaLocalIpAddress_Object = MibTableColumn
ipsecIkeSaLocalIpAddress = _IpsecIkeSaLocalIpAddress_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 4),
    _IpsecIkeSaLocalIpAddress_Type()
)
ipsecIkeSaLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaLocalIpAddress.setStatus("current")


class _IpsecIkeSaLocalPortNumber_Type(Integer32):
    """Custom type ipsecIkeSaLocalPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecIkeSaLocalPortNumber_Type.__name__ = "Integer32"
_IpsecIkeSaLocalPortNumber_Object = MibTableColumn
ipsecIkeSaLocalPortNumber = _IpsecIkeSaLocalPortNumber_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 5),
    _IpsecIkeSaLocalPortNumber_Type()
)
ipsecIkeSaLocalPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaLocalPortNumber.setStatus("current")


class _IpsecIkeSaLocalIdType_Type(Integer32):
    """Custom type ipsecIkeSaLocalIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpsecIkeSaLocalIdType_Type.__name__ = "Integer32"
_IpsecIkeSaLocalIdType_Object = MibTableColumn
ipsecIkeSaLocalIdType = _IpsecIkeSaLocalIdType_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 8),
    _IpsecIkeSaLocalIdType_Type()
)
ipsecIkeSaLocalIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaLocalIdType.setStatus("current")


class _IpsecIkeSaLocalId_Type(OctetString):
    """Custom type ipsecIkeSaLocalId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_IpsecIkeSaLocalId_Type.__name__ = "OctetString"
_IpsecIkeSaLocalId_Object = MibTableColumn
ipsecIkeSaLocalId = _IpsecIkeSaLocalId_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 9),
    _IpsecIkeSaLocalId_Type()
)
ipsecIkeSaLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaLocalId.setStatus("current")


class _IpsecIkeSaPeerIpAddress_Type(OctetString):
    """Custom type ipsecIkeSaPeerIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IpsecIkeSaPeerIpAddress_Type.__name__ = "OctetString"
_IpsecIkeSaPeerIpAddress_Object = MibTableColumn
ipsecIkeSaPeerIpAddress = _IpsecIkeSaPeerIpAddress_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 10),
    _IpsecIkeSaPeerIpAddress_Type()
)
ipsecIkeSaPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaPeerIpAddress.setStatus("current")


class _IpsecIkeSaPeerPortNumber_Type(Integer32):
    """Custom type ipsecIkeSaPeerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecIkeSaPeerPortNumber_Type.__name__ = "Integer32"
_IpsecIkeSaPeerPortNumber_Object = MibTableColumn
ipsecIkeSaPeerPortNumber = _IpsecIkeSaPeerPortNumber_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 11),
    _IpsecIkeSaPeerPortNumber_Type()
)
ipsecIkeSaPeerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaPeerPortNumber.setStatus("current")


class _IpsecIkeSaAuthMethod_Type(Integer32):
    """Custom type ipsecIkeSaAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecIkeSaAuthMethod_Type.__name__ = "Integer32"
_IpsecIkeSaAuthMethod_Object = MibTableColumn
ipsecIkeSaAuthMethod = _IpsecIkeSaAuthMethod_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 12),
    _IpsecIkeSaAuthMethod_Type()
)
ipsecIkeSaAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaAuthMethod.setStatus("current")


class _IpsecIkeSaPeerIdType_Type(Integer32):
    """Custom type ipsecIkeSaPeerIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpsecIkeSaPeerIdType_Type.__name__ = "Integer32"
_IpsecIkeSaPeerIdType_Object = MibTableColumn
ipsecIkeSaPeerIdType = _IpsecIkeSaPeerIdType_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 13),
    _IpsecIkeSaPeerIdType_Type()
)
ipsecIkeSaPeerIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaPeerIdType.setStatus("current")


class _IpsecIkeSaPeerId_Type(OctetString):
    """Custom type ipsecIkeSaPeerId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_IpsecIkeSaPeerId_Type.__name__ = "OctetString"
_IpsecIkeSaPeerId_Object = MibTableColumn
ipsecIkeSaPeerId = _IpsecIkeSaPeerId_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 14),
    _IpsecIkeSaPeerId_Type()
)
ipsecIkeSaPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaPeerId.setStatus("current")


class _IpsecIkeSaPeerCertSerialNum_Type(OctetString):
    """Custom type ipsecIkeSaPeerCertSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IpsecIkeSaPeerCertSerialNum_Type.__name__ = "OctetString"
_IpsecIkeSaPeerCertSerialNum_Object = MibTableColumn
ipsecIkeSaPeerCertSerialNum = _IpsecIkeSaPeerCertSerialNum_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 15),
    _IpsecIkeSaPeerCertSerialNum_Type()
)
ipsecIkeSaPeerCertSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaPeerCertSerialNum.setStatus("current")


class _IpsecIkeSaPeerCertIssuer_Type(OctetString):
    """Custom type ipsecIkeSaPeerCertIssuer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_IpsecIkeSaPeerCertIssuer_Type.__name__ = "OctetString"
_IpsecIkeSaPeerCertIssuer_Object = MibTableColumn
ipsecIkeSaPeerCertIssuer = _IpsecIkeSaPeerCertIssuer_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 16),
    _IpsecIkeSaPeerCertIssuer_Type()
)
ipsecIkeSaPeerCertIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaPeerCertIssuer.setStatus("current")


class _IpsecIkeSaEncAlg_Type(Integer32):
    """Custom type ipsecIkeSaEncAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecIkeSaEncAlg_Type.__name__ = "Integer32"
_IpsecIkeSaEncAlg_Object = MibTableColumn
ipsecIkeSaEncAlg = _IpsecIkeSaEncAlg_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 17),
    _IpsecIkeSaEncAlg_Type()
)
ipsecIkeSaEncAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaEncAlg.setStatus("current")
_IpsecIkeSaEncKeyLength_Type = Integer32
_IpsecIkeSaEncKeyLength_Object = MibTableColumn
ipsecIkeSaEncKeyLength = _IpsecIkeSaEncKeyLength_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 18),
    _IpsecIkeSaEncKeyLength_Type()
)
ipsecIkeSaEncKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaEncKeyLength.setStatus("current")


class _IpsecIkeSaHashAlg_Type(Integer32):
    """Custom type ipsecIkeSaHashAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecIkeSaHashAlg_Type.__name__ = "Integer32"
_IpsecIkeSaHashAlg_Object = MibTableColumn
ipsecIkeSaHashAlg = _IpsecIkeSaHashAlg_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 19),
    _IpsecIkeSaHashAlg_Type()
)
ipsecIkeSaHashAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaHashAlg.setStatus("current")


class _IpsecIkeSaDifHelGroupDesc_Type(Integer32):
    """Custom type ipsecIkeSaDifHelGroupDesc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecIkeSaDifHelGroupDesc_Type.__name__ = "Integer32"
_IpsecIkeSaDifHelGroupDesc_Object = MibTableColumn
ipsecIkeSaDifHelGroupDesc = _IpsecIkeSaDifHelGroupDesc_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 20),
    _IpsecIkeSaDifHelGroupDesc_Type()
)
ipsecIkeSaDifHelGroupDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaDifHelGroupDesc.setStatus("current")


class _IpsecIkeSaDifHelGroupType_Type(Integer32):
    """Custom type ipsecIkeSaDifHelGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecIkeSaDifHelGroupType_Type.__name__ = "Integer32"
_IpsecIkeSaDifHelGroupType_Object = MibTableColumn
ipsecIkeSaDifHelGroupType = _IpsecIkeSaDifHelGroupType_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 21),
    _IpsecIkeSaDifHelGroupType_Type()
)
ipsecIkeSaDifHelGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaDifHelGroupType.setStatus("current")
_IpsecIkeSaDifHelFieldSize_Type = Integer32
_IpsecIkeSaDifHelFieldSize_Object = MibTableColumn
ipsecIkeSaDifHelFieldSize = _IpsecIkeSaDifHelFieldSize_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 22),
    _IpsecIkeSaDifHelFieldSize_Type()
)
ipsecIkeSaDifHelFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaDifHelFieldSize.setStatus("current")


class _IpsecIkeSaPRF_Type(Integer32):
    """Custom type ipsecIkeSaPRF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecIkeSaPRF_Type.__name__ = "Integer32"
_IpsecIkeSaPRF_Object = MibTableColumn
ipsecIkeSaPRF = _IpsecIkeSaPRF_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 23),
    _IpsecIkeSaPRF_Type()
)
ipsecIkeSaPRF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaPRF.setStatus("current")
_IpsecIkeSaPFS_Type = TruthValue
_IpsecIkeSaPFS_Object = MibTableColumn
ipsecIkeSaPFS = _IpsecIkeSaPFS_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 24),
    _IpsecIkeSaPFS_Type()
)
ipsecIkeSaPFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaPFS.setStatus("current")
_IpsecIkeSaTimeStart_Type = DateAndTime
_IpsecIkeSaTimeStart_Object = MibTableColumn
ipsecIkeSaTimeStart = _IpsecIkeSaTimeStart_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 25),
    _IpsecIkeSaTimeStart_Type()
)
ipsecIkeSaTimeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaTimeStart.setStatus("current")
_IpsecIkeSaTimeLimit_Type = OctetString
_IpsecIkeSaTimeLimit_Object = MibTableColumn
ipsecIkeSaTimeLimit = _IpsecIkeSaTimeLimit_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 26),
    _IpsecIkeSaTimeLimit_Type()
)
ipsecIkeSaTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaTimeLimit.setStatus("current")
if mibBuilder.loadTexts:
    ipsecIkeSaTimeLimit.setUnits("seconds")
_IpsecIkeSaTrafficLimit_Type = OctetString
_IpsecIkeSaTrafficLimit_Object = MibTableColumn
ipsecIkeSaTrafficLimit = _IpsecIkeSaTrafficLimit_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 27),
    _IpsecIkeSaTrafficLimit_Type()
)
ipsecIkeSaTrafficLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaTrafficLimit.setStatus("current")
if mibBuilder.loadTexts:
    ipsecIkeSaTrafficLimit.setUnits("Kbytes")
_IpsecIkeSaInboundTraffic_Type = Counter64
_IpsecIkeSaInboundTraffic_Object = MibTableColumn
ipsecIkeSaInboundTraffic = _IpsecIkeSaInboundTraffic_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 28),
    _IpsecIkeSaInboundTraffic_Type()
)
ipsecIkeSaInboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaInboundTraffic.setStatus("current")
if mibBuilder.loadTexts:
    ipsecIkeSaInboundTraffic.setUnits("bytes")
_IpsecIkeSaOutboundTraffic_Type = Counter64
_IpsecIkeSaOutboundTraffic_Object = MibTableColumn
ipsecIkeSaOutboundTraffic = _IpsecIkeSaOutboundTraffic_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 29),
    _IpsecIkeSaOutboundTraffic_Type()
)
ipsecIkeSaOutboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaOutboundTraffic.setStatus("current")
if mibBuilder.loadTexts:
    ipsecIkeSaOutboundTraffic.setUnits("bytes")
_IpsecIkeSaInboundPackets_Type = Counter32
_IpsecIkeSaInboundPackets_Object = MibTableColumn
ipsecIkeSaInboundPackets = _IpsecIkeSaInboundPackets_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 30),
    _IpsecIkeSaInboundPackets_Type()
)
ipsecIkeSaInboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaInboundPackets.setStatus("current")
_IpsecIkeSaOutboundPackets_Type = Counter32
_IpsecIkeSaOutboundPackets_Object = MibTableColumn
ipsecIkeSaOutboundPackets = _IpsecIkeSaOutboundPackets_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 31),
    _IpsecIkeSaOutboundPackets_Type()
)
ipsecIkeSaOutboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaOutboundPackets.setStatus("current")
_IpsecIkeProtSuitesCreated_Type = Counter32
_IpsecIkeProtSuitesCreated_Object = MibTableColumn
ipsecIkeProtSuitesCreated = _IpsecIkeProtSuitesCreated_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 32),
    _IpsecIkeProtSuitesCreated_Type()
)
ipsecIkeProtSuitesCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeProtSuitesCreated.setStatus("current")
_IpsecIkeProtSuitesDeleted_Type = Counter32
_IpsecIkeProtSuitesDeleted_Object = MibTableColumn
ipsecIkeProtSuitesDeleted = _IpsecIkeProtSuitesDeleted_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 33),
    _IpsecIkeProtSuitesDeleted_Type()
)
ipsecIkeProtSuitesDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeProtSuitesDeleted.setStatus("current")
_IpsecIkeSaDecryptErrors_Type = Counter32
_IpsecIkeSaDecryptErrors_Object = MibTableColumn
ipsecIkeSaDecryptErrors = _IpsecIkeSaDecryptErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 34),
    _IpsecIkeSaDecryptErrors_Type()
)
ipsecIkeSaDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaDecryptErrors.setStatus("current")
_IpsecIkeSaAuthErrors_Type = Counter32
_IpsecIkeSaAuthErrors_Object = MibTableColumn
ipsecIkeSaAuthErrors = _IpsecIkeSaAuthErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 35),
    _IpsecIkeSaAuthErrors_Type()
)
ipsecIkeSaAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaAuthErrors.setStatus("current")
_IpsecIkeSaOtherReceiveErrors_Type = Counter32
_IpsecIkeSaOtherReceiveErrors_Object = MibTableColumn
ipsecIkeSaOtherReceiveErrors = _IpsecIkeSaOtherReceiveErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 36),
    _IpsecIkeSaOtherReceiveErrors_Type()
)
ipsecIkeSaOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaOtherReceiveErrors.setStatus("current")
_IpsecIkeSaSendErrors_Type = Counter32
_IpsecIkeSaSendErrors_Object = MibTableColumn
ipsecIkeSaSendErrors = _IpsecIkeSaSendErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 2, 1, 37),
    _IpsecIkeSaSendErrors_Type()
)
ipsecIkeSaSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaSendErrors.setStatus("current")
_IpsecTrapsA_ObjectIdentity = ObjectIdentity
ipsecTrapsA = _IpsecTrapsA_ObjectIdentity(
    (1, 3, 6, 1, 3, 500, 1, 1, 3)
)
_IpsecTraps_ObjectIdentity = ObjectIdentity
ipsecTraps = _IpsecTraps_ObjectIdentity(
    (1, 3, 6, 1, 3, 500, 1, 1, 3, 0)
)
_IpsecIpsecStats_ObjectIdentity = ObjectIdentity
ipsecIpsecStats = _IpsecIpsecStats_ObjectIdentity(
    (1, 3, 6, 1, 3, 500, 1, 1, 4)
)
_IpsecIpsecTotalProtSuites_Type = Counter64
_IpsecIpsecTotalProtSuites_Object = MibScalar
ipsecIpsecTotalProtSuites = _IpsecIpsecTotalProtSuites_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 4, 1),
    _IpsecIpsecTotalProtSuites_Type()
)
ipsecIpsecTotalProtSuites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpsecTotalProtSuites.setStatus("current")
_IpsecIpsecNegFailures_Type = Counter64
_IpsecIpsecNegFailures_Object = MibScalar
ipsecIpsecNegFailures = _IpsecIpsecNegFailures_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 4, 2),
    _IpsecIpsecNegFailures_Type()
)
ipsecIpsecNegFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpsecNegFailures.setStatus("current")
_IpsecIpsecTotalInboundPackets_Type = Counter64
_IpsecIpsecTotalInboundPackets_Object = MibScalar
ipsecIpsecTotalInboundPackets = _IpsecIpsecTotalInboundPackets_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 4, 3),
    _IpsecIpsecTotalInboundPackets_Type()
)
ipsecIpsecTotalInboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpsecTotalInboundPackets.setStatus("current")
_IpsecIpsecTotalTransOutboundPackets_Type = Counter64
_IpsecIpsecTotalTransOutboundPackets_Object = MibScalar
ipsecIpsecTotalTransOutboundPackets = _IpsecIpsecTotalTransOutboundPackets_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 4, 4),
    _IpsecIpsecTotalTransOutboundPackets_Type()
)
ipsecIpsecTotalTransOutboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpsecTotalTransOutboundPackets.setStatus("current")
_IpsecIpsecTotalTransInboundTraffic_Type = Counter64
_IpsecIpsecTotalTransInboundTraffic_Object = MibScalar
ipsecIpsecTotalTransInboundTraffic = _IpsecIpsecTotalTransInboundTraffic_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 4, 5),
    _IpsecIpsecTotalTransInboundTraffic_Type()
)
ipsecIpsecTotalTransInboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpsecTotalTransInboundTraffic.setStatus("current")
if mibBuilder.loadTexts:
    ipsecIpsecTotalTransInboundTraffic.setUnits("Kbytes")
_IpsecIpsecTotalTransOutboundTraffic_Type = Counter64
_IpsecIpsecTotalTransOutboundTraffic_Object = MibScalar
ipsecIpsecTotalTransOutboundTraffic = _IpsecIpsecTotalTransOutboundTraffic_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 4, 6),
    _IpsecIpsecTotalTransOutboundTraffic_Type()
)
ipsecIpsecTotalTransOutboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpsecTotalTransOutboundTraffic.setStatus("current")
if mibBuilder.loadTexts:
    ipsecIpsecTotalTransOutboundTraffic.setUnits("Kbytes")
_IpsecIpsecErrorStats_ObjectIdentity = ObjectIdentity
ipsecIpsecErrorStats = _IpsecIpsecErrorStats_ObjectIdentity(
    (1, 3, 6, 1, 3, 500, 1, 1, 5)
)
_IpsecIpsecDecryptionErrors_Type = Counter32
_IpsecIpsecDecryptionErrors_Object = MibScalar
ipsecIpsecDecryptionErrors = _IpsecIpsecDecryptionErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 5, 1),
    _IpsecIpsecDecryptionErrors_Type()
)
ipsecIpsecDecryptionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpsecDecryptionErrors.setStatus("current")
_IpsecIpsecAuthenticationErrors_Type = Counter32
_IpsecIpsecAuthenticationErrors_Object = MibScalar
ipsecIpsecAuthenticationErrors = _IpsecIpsecAuthenticationErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 5, 2),
    _IpsecIpsecAuthenticationErrors_Type()
)
ipsecIpsecAuthenticationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpsecAuthenticationErrors.setStatus("current")
_IpsecIpsecReplayErrors_Type = Counter32
_IpsecIpsecReplayErrors_Object = MibScalar
ipsecIpsecReplayErrors = _IpsecIpsecReplayErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 5, 3),
    _IpsecIpsecReplayErrors_Type()
)
ipsecIpsecReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpsecReplayErrors.setStatus("current")
_IpsecIpsecPolicyErrors_Type = Counter32
_IpsecIpsecPolicyErrors_Object = MibScalar
ipsecIpsecPolicyErrors = _IpsecIpsecPolicyErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 5, 4),
    _IpsecIpsecPolicyErrors_Type()
)
ipsecIpsecPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpsecPolicyErrors.setStatus("current")
_IpsecIpsecOtherReceiveErrors_Type = Counter32
_IpsecIpsecOtherReceiveErrors_Object = MibScalar
ipsecIpsecOtherReceiveErrors = _IpsecIpsecOtherReceiveErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 5, 5),
    _IpsecIpsecOtherReceiveErrors_Type()
)
ipsecIpsecOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpsecOtherReceiveErrors.setStatus("current")
_IpsecIpsecSendErrors_Type = Counter32
_IpsecIpsecSendErrors_Object = MibScalar
ipsecIpsecSendErrors = _IpsecIpsecSendErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 5, 6),
    _IpsecIpsecSendErrors_Type()
)
ipsecIpsecSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpsecSendErrors.setStatus("current")
_IpsecUnknownSpiErrors_Type = Counter32
_IpsecUnknownSpiErrors_Object = MibScalar
ipsecUnknownSpiErrors = _IpsecUnknownSpiErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 5, 7),
    _IpsecUnknownSpiErrors_Type()
)
ipsecUnknownSpiErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecUnknownSpiErrors.setStatus("current")
_IpsecIkeStats_ObjectIdentity = ObjectIdentity
ipsecIkeStats = _IpsecIkeStats_ObjectIdentity(
    (1, 3, 6, 1, 3, 500, 1, 1, 6)
)
_IpsecIkeTotalSAs_Type = Counter64
_IpsecIkeTotalSAs_Object = MibScalar
ipsecIkeTotalSAs = _IpsecIkeTotalSAs_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 6, 1),
    _IpsecIkeTotalSAs_Type()
)
ipsecIkeTotalSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeTotalSAs.setStatus("current")
_IpsecIkeNegFailures_Type = Counter64
_IpsecIkeNegFailures_Object = MibScalar
ipsecIkeNegFailures = _IpsecIkeNegFailures_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 6, 2),
    _IpsecIkeNegFailures_Type()
)
ipsecIkeNegFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeNegFailures.setStatus("current")
_IpsecIkeTotalInboundPackets_Type = Counter64
_IpsecIkeTotalInboundPackets_Object = MibScalar
ipsecIkeTotalInboundPackets = _IpsecIkeTotalInboundPackets_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 6, 3),
    _IpsecIkeTotalInboundPackets_Type()
)
ipsecIkeTotalInboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeTotalInboundPackets.setStatus("current")
_IpsecIkeTotalTransOutboundPackets_Type = Counter64
_IpsecIkeTotalTransOutboundPackets_Object = MibScalar
ipsecIkeTotalTransOutboundPackets = _IpsecIkeTotalTransOutboundPackets_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 6, 4),
    _IpsecIkeTotalTransOutboundPackets_Type()
)
ipsecIkeTotalTransOutboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeTotalTransOutboundPackets.setStatus("current")
_IpsecIkeTotalTransInboundTraffic_Type = Counter64
_IpsecIkeTotalTransInboundTraffic_Object = MibScalar
ipsecIkeTotalTransInboundTraffic = _IpsecIkeTotalTransInboundTraffic_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 6, 5),
    _IpsecIkeTotalTransInboundTraffic_Type()
)
ipsecIkeTotalTransInboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeTotalTransInboundTraffic.setStatus("current")
if mibBuilder.loadTexts:
    ipsecIkeTotalTransInboundTraffic.setUnits("Kbytes")
_IpsecIkeTotalTransOutboundTraffic_Type = Counter64
_IpsecIkeTotalTransOutboundTraffic_Object = MibScalar
ipsecIkeTotalTransOutboundTraffic = _IpsecIkeTotalTransOutboundTraffic_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 6, 6),
    _IpsecIkeTotalTransOutboundTraffic_Type()
)
ipsecIkeTotalTransOutboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeTotalTransOutboundTraffic.setStatus("current")
if mibBuilder.loadTexts:
    ipsecIkeTotalTransOutboundTraffic.setUnits("Kbytes")
_IpsecIkeErrorStats_ObjectIdentity = ObjectIdentity
ipsecIkeErrorStats = _IpsecIkeErrorStats_ObjectIdentity(
    (1, 3, 6, 1, 3, 500, 1, 1, 7)
)
_IpsecIkeProtocolErrors_Type = Counter32
_IpsecIkeProtocolErrors_Object = MibScalar
ipsecIkeProtocolErrors = _IpsecIkeProtocolErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 7, 1),
    _IpsecIkeProtocolErrors_Type()
)
ipsecIkeProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeProtocolErrors.setStatus("current")
_IpsecIkeDecryptionErrors_Type = Counter32
_IpsecIkeDecryptionErrors_Object = MibScalar
ipsecIkeDecryptionErrors = _IpsecIkeDecryptionErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 7, 2),
    _IpsecIkeDecryptionErrors_Type()
)
ipsecIkeDecryptionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeDecryptionErrors.setStatus("current")
_IpsecIkeAuthenticationErrors_Type = Counter32
_IpsecIkeAuthenticationErrors_Object = MibScalar
ipsecIkeAuthenticationErrors = _IpsecIkeAuthenticationErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 7, 3),
    _IpsecIkeAuthenticationErrors_Type()
)
ipsecIkeAuthenticationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeAuthenticationErrors.setStatus("current")
_IpsecIkeOtherReceiveErrors_Type = Counter32
_IpsecIkeOtherReceiveErrors_Object = MibScalar
ipsecIkeOtherReceiveErrors = _IpsecIkeOtherReceiveErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 7, 4),
    _IpsecIkeOtherReceiveErrors_Type()
)
ipsecIkeOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeOtherReceiveErrors.setStatus("current")
_IpsecIkeSendErrors_Type = Counter32
_IpsecIkeSendErrors_Object = MibScalar
ipsecIkeSendErrors = _IpsecIkeSendErrors_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 7, 5),
    _IpsecIkeSendErrors_Type()
)
ipsecIkeSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSendErrors.setStatus("current")
_IpsecNotifications_ObjectIdentity = ObjectIdentity
ipsecNotifications = _IpsecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 500, 1, 1, 8)
)
_IpsecNotifyMessageTotalCount_Type = Counter64
_IpsecNotifyMessageTotalCount_Object = MibScalar
ipsecNotifyMessageTotalCount = _IpsecNotifyMessageTotalCount_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 8, 1),
    _IpsecNotifyMessageTotalCount_Type()
)
ipsecNotifyMessageTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecNotifyMessageTotalCount.setStatus("current")
_IpsecNotifyCountTable_Object = MibTable
ipsecNotifyCountTable = _IpsecNotifyCountTable_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ipsecNotifyCountTable.setStatus("current")
_IpsecNotifyCountEntry_Object = MibTableRow
ipsecNotifyCountEntry = _IpsecNotifyCountEntry_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 8, 2, 1)
)
ipsecNotifyCountEntry.setIndexNames(
    (0, "IPSEC-MIB", "ipsecNotifyMessage"),
)
if mibBuilder.loadTexts:
    ipsecNotifyCountEntry.setStatus("current")


class _IpsecNotifyMessage_Type(Integer32):
    """Custom type ipsecNotifyMessage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecNotifyMessage_Type.__name__ = "Integer32"
_IpsecNotifyMessage_Object = MibTableColumn
ipsecNotifyMessage = _IpsecNotifyMessage_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 8, 2, 1, 1),
    _IpsecNotifyMessage_Type()
)
ipsecNotifyMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecNotifyMessage.setStatus("current")
_IpsecNotifyMessageCount_Type = Counter32
_IpsecNotifyMessageCount_Object = MibTableColumn
ipsecNotifyMessageCount = _IpsecNotifyMessageCount_Object(
    (1, 3, 6, 1, 3, 500, 1, 1, 8, 2, 1, 2),
    _IpsecNotifyMessageCount_Type()
)
ipsecNotifyMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecNotifyMessageCount.setStatus("current")

# Managed Objects groups


# Notification objects

ipsecTrapIkeNegFailure = NotificationType(
    (1, 3, 6, 1, 3, 500, 1, 1, 3, 0, 1)
)
ipsecTrapIkeNegFailure.setObjects(
      *(("IPSEC-MIB", "ipsecIkeSaLocalIdType"),
        ("IPSEC-MIB", "ipsecIkeSaLocalId"),
        ("IPSEC-MIB", "ipsecIkeSaPeerIdType"),
        ("IPSEC-MIB", "ipsecIkeSaPeerId"),
        ("IPSEC-MIB", "ipsecIkeSaLocalIpAddress"),
        ("IPSEC-MIB", "ipsecIkeSaLocalPortNumber"),
        ("IPSEC-MIB", "ipsecIkeSaPeerIpAddress"),
        ("IPSEC-MIB", "ipsecIkeSaPeerPortNumber"),
        ("IPSEC-MIB", "ipsecIkeSaAuthMethod"),
        ("IPSEC-MIB", "ipsecIkeSaPeerCertSerialNum"),
        ("IPSEC-MIB", "ipsecIkeSaPeerCertIssuer"),
        ("IPSEC-MIB", "ipsecNotifyMessage"))
)
if mibBuilder.loadTexts:
    ipsecTrapIkeNegFailure.setStatus(
        "current"
    )

ipsecTrapInvalidCookie = NotificationType(
    (1, 3, 6, 1, 3, 500, 1, 1, 3, 0, 2)
)
ipsecTrapInvalidCookie.setObjects(
      *(("IPSEC-MIB", "ipsecIkeSaPeerIpAddress"),
        ("IPSEC-MIB", "ipsecIkeSaPeerPortNumber"))
)
if mibBuilder.loadTexts:
    ipsecTrapInvalidCookie.setStatus(
        "current"
    )

ipsecTrapIpsecNegFailure = NotificationType(
    (1, 3, 6, 1, 3, 500, 1, 1, 3, 0, 3)
)
ipsecTrapIpsecNegFailure.setObjects(
      *(("IPSEC-MIB", "ipsecIkeSaIndex"),
        ("IPSEC-MIB", "ipsecNotifyMessage"))
)
if mibBuilder.loadTexts:
    ipsecTrapIpsecNegFailure.setStatus(
        "current"
    )

ipsecTrapIpsecAuthFailure = NotificationType(
    (1, 3, 6, 1, 3, 500, 1, 1, 3, 0, 4)
)
ipsecTrapIpsecAuthFailure.setObjects(
    ("IPSEC-MIB", "ipsecProtSuiteIndex")
)
if mibBuilder.loadTexts:
    ipsecTrapIpsecAuthFailure.setStatus(
        "current"
    )

ipsecTrapIpsecReplayFailure = NotificationType(
    (1, 3, 6, 1, 3, 500, 1, 1, 3, 0, 5)
)
ipsecTrapIpsecReplayFailure.setObjects(
    ("IPSEC-MIB", "ipsecProtSuiteIndex")
)
if mibBuilder.loadTexts:
    ipsecTrapIpsecReplayFailure.setStatus(
        "current"
    )

ipsecTrapIpsecPolicyFailure = NotificationType(
    (1, 3, 6, 1, 3, 500, 1, 1, 3, 0, 6)
)
ipsecTrapIpsecPolicyFailure.setObjects(
    ("IPSEC-MIB", "ipsecProtSuiteIndex")
)
if mibBuilder.loadTexts:
    ipsecTrapIpsecPolicyFailure.setStatus(
        "current"
    )

ipsecTrapInvalidSpi = NotificationType(
    (1, 3, 6, 1, 3, 500, 1, 1, 3, 0, 7)
)
ipsecTrapInvalidSpi.setObjects(
    ("IPSEC-MIB", "ipsecIkeSaPeerIpAddress")
)
if mibBuilder.loadTexts:
    ipsecTrapInvalidSpi.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPSEC-MIB",
    **{"ipsecMIB": ipsecMIB,
       "ipsecMIBObjects": ipsecMIBObjects,
       "ipsec": ipsec,
       "ipsecProtSuiteTable": ipsecProtSuiteTable,
       "ipsecProtSuiteEntry": ipsecProtSuiteEntry,
       "ipsecProtSuiteIndex": ipsecProtSuiteIndex,
       "ipsecProtSuiteLocalAddress": ipsecProtSuiteLocalAddress,
       "ipsecProtSuiteRemoteAddress": ipsecProtSuiteRemoteAddress,
       "ipsecProtSuiteInboundEspSpi": ipsecProtSuiteInboundEspSpi,
       "ipsecProtSuiteOutboundEspSpi": ipsecProtSuiteOutboundEspSpi,
       "ipsecProtSuiteInboundAhSpi": ipsecProtSuiteInboundAhSpi,
       "ipsecProtSuiteOutboundAhSpi": ipsecProtSuiteOutboundAhSpi,
       "ipsecProtSuiteInboundCompCpi": ipsecProtSuiteInboundCompCpi,
       "ipsecProtSuiteOutboundCompCpi": ipsecProtSuiteOutboundCompCpi,
       "ipsecProtSuiteLocalId": ipsecProtSuiteLocalId,
       "ipsecProtSuiteLocalIdType": ipsecProtSuiteLocalIdType,
       "ipsecProtSuiteRemoteId": ipsecProtSuiteRemoteId,
       "ipsecProtSuiteRemoteIdType": ipsecProtSuiteRemoteIdType,
       "ipsecProtSuiteProtocol": ipsecProtSuiteProtocol,
       "ipsecProtSuiteLocalPort": ipsecProtSuiteLocalPort,
       "ipsecProtSuiteRemotePort": ipsecProtSuiteRemotePort,
       "ipsecProtSuiteDifHelGroupDesc": ipsecProtSuiteDifHelGroupDesc,
       "ipsecProtSuiteDifHelGroupType": ipsecProtSuiteDifHelGroupType,
       "ipsecProtSuitePFS": ipsecProtSuitePFS,
       "ipsecProtSuiteEncapsulation": ipsecProtSuiteEncapsulation,
       "ipsecProtSuiteEspEncAlg": ipsecProtSuiteEspEncAlg,
       "ipsecProtSuiteEspEncKeyLength": ipsecProtSuiteEspEncKeyLength,
       "ipsecProtSuiteEspAuthAlg": ipsecProtSuiteEspAuthAlg,
       "ipsecProtSuiteAhAuthAlg": ipsecProtSuiteAhAuthAlg,
       "ipsecProtSuiteCompAlg": ipsecProtSuiteCompAlg,
       "ipsecProtSuiteCreationTime": ipsecProtSuiteCreationTime,
       "ipsecProtSuiteTimeLimit": ipsecProtSuiteTimeLimit,
       "ipsecProtSuiteTrafficLimit": ipsecProtSuiteTrafficLimit,
       "ipsecProtSuiteInTrafficCount": ipsecProtSuiteInTrafficCount,
       "ipsecProtSuiteOutTrafficCount": ipsecProtSuiteOutTrafficCount,
       "ipsecProtSuiteInboundTraffic": ipsecProtSuiteInboundTraffic,
       "ipsecProtSuiteOutboundTraffic": ipsecProtSuiteOutboundTraffic,
       "ipsecProtSuiteInboundPackets": ipsecProtSuiteInboundPackets,
       "ipsecProtSuiteOutboundPackets": ipsecProtSuiteOutboundPackets,
       "ipsecProtSuiteDecryptErrors": ipsecProtSuiteDecryptErrors,
       "ipsecProtSuiteAuthErrors": ipsecProtSuiteAuthErrors,
       "ipsecProtSuiteReplayErrors": ipsecProtSuiteReplayErrors,
       "ipsecProtSuitePolicyErrors": ipsecProtSuitePolicyErrors,
       "ipsecProtSuiteOtherReceiveErrors": ipsecProtSuiteOtherReceiveErrors,
       "ipsecProtSuiteSendErrors": ipsecProtSuiteSendErrors,
       "ipsecIkeSaTable": ipsecIkeSaTable,
       "ipsecIkeSaEntry": ipsecIkeSaEntry,
       "ipsecIkeSaIndex": ipsecIkeSaIndex,
       "ipsecIkeSaInitiatorCookie": ipsecIkeSaInitiatorCookie,
       "ipsecIkeSaResponderCookie": ipsecIkeSaResponderCookie,
       "ipsecIkeSaLocalIpAddress": ipsecIkeSaLocalIpAddress,
       "ipsecIkeSaLocalPortNumber": ipsecIkeSaLocalPortNumber,
       "ipsecIkeSaLocalIdType": ipsecIkeSaLocalIdType,
       "ipsecIkeSaLocalId": ipsecIkeSaLocalId,
       "ipsecIkeSaPeerIpAddress": ipsecIkeSaPeerIpAddress,
       "ipsecIkeSaPeerPortNumber": ipsecIkeSaPeerPortNumber,
       "ipsecIkeSaAuthMethod": ipsecIkeSaAuthMethod,
       "ipsecIkeSaPeerIdType": ipsecIkeSaPeerIdType,
       "ipsecIkeSaPeerId": ipsecIkeSaPeerId,
       "ipsecIkeSaPeerCertSerialNum": ipsecIkeSaPeerCertSerialNum,
       "ipsecIkeSaPeerCertIssuer": ipsecIkeSaPeerCertIssuer,
       "ipsecIkeSaEncAlg": ipsecIkeSaEncAlg,
       "ipsecIkeSaEncKeyLength": ipsecIkeSaEncKeyLength,
       "ipsecIkeSaHashAlg": ipsecIkeSaHashAlg,
       "ipsecIkeSaDifHelGroupDesc": ipsecIkeSaDifHelGroupDesc,
       "ipsecIkeSaDifHelGroupType": ipsecIkeSaDifHelGroupType,
       "ipsecIkeSaDifHelFieldSize": ipsecIkeSaDifHelFieldSize,
       "ipsecIkeSaPRF": ipsecIkeSaPRF,
       "ipsecIkeSaPFS": ipsecIkeSaPFS,
       "ipsecIkeSaTimeStart": ipsecIkeSaTimeStart,
       "ipsecIkeSaTimeLimit": ipsecIkeSaTimeLimit,
       "ipsecIkeSaTrafficLimit": ipsecIkeSaTrafficLimit,
       "ipsecIkeSaInboundTraffic": ipsecIkeSaInboundTraffic,
       "ipsecIkeSaOutboundTraffic": ipsecIkeSaOutboundTraffic,
       "ipsecIkeSaInboundPackets": ipsecIkeSaInboundPackets,
       "ipsecIkeSaOutboundPackets": ipsecIkeSaOutboundPackets,
       "ipsecIkeProtSuitesCreated": ipsecIkeProtSuitesCreated,
       "ipsecIkeProtSuitesDeleted": ipsecIkeProtSuitesDeleted,
       "ipsecIkeSaDecryptErrors": ipsecIkeSaDecryptErrors,
       "ipsecIkeSaAuthErrors": ipsecIkeSaAuthErrors,
       "ipsecIkeSaOtherReceiveErrors": ipsecIkeSaOtherReceiveErrors,
       "ipsecIkeSaSendErrors": ipsecIkeSaSendErrors,
       "ipsecTrapsA": ipsecTrapsA,
       "ipsecTraps": ipsecTraps,
       "ipsecTrapIkeNegFailure": ipsecTrapIkeNegFailure,
       "ipsecTrapInvalidCookie": ipsecTrapInvalidCookie,
       "ipsecTrapIpsecNegFailure": ipsecTrapIpsecNegFailure,
       "ipsecTrapIpsecAuthFailure": ipsecTrapIpsecAuthFailure,
       "ipsecTrapIpsecReplayFailure": ipsecTrapIpsecReplayFailure,
       "ipsecTrapIpsecPolicyFailure": ipsecTrapIpsecPolicyFailure,
       "ipsecTrapInvalidSpi": ipsecTrapInvalidSpi,
       "ipsecIpsecStats": ipsecIpsecStats,
       "ipsecIpsecTotalProtSuites": ipsecIpsecTotalProtSuites,
       "ipsecIpsecNegFailures": ipsecIpsecNegFailures,
       "ipsecIpsecTotalInboundPackets": ipsecIpsecTotalInboundPackets,
       "ipsecIpsecTotalTransOutboundPackets": ipsecIpsecTotalTransOutboundPackets,
       "ipsecIpsecTotalTransInboundTraffic": ipsecIpsecTotalTransInboundTraffic,
       "ipsecIpsecTotalTransOutboundTraffic": ipsecIpsecTotalTransOutboundTraffic,
       "ipsecIpsecErrorStats": ipsecIpsecErrorStats,
       "ipsecIpsecDecryptionErrors": ipsecIpsecDecryptionErrors,
       "ipsecIpsecAuthenticationErrors": ipsecIpsecAuthenticationErrors,
       "ipsecIpsecReplayErrors": ipsecIpsecReplayErrors,
       "ipsecIpsecPolicyErrors": ipsecIpsecPolicyErrors,
       "ipsecIpsecOtherReceiveErrors": ipsecIpsecOtherReceiveErrors,
       "ipsecIpsecSendErrors": ipsecIpsecSendErrors,
       "ipsecUnknownSpiErrors": ipsecUnknownSpiErrors,
       "ipsecIkeStats": ipsecIkeStats,
       "ipsecIkeTotalSAs": ipsecIkeTotalSAs,
       "ipsecIkeNegFailures": ipsecIkeNegFailures,
       "ipsecIkeTotalInboundPackets": ipsecIkeTotalInboundPackets,
       "ipsecIkeTotalTransOutboundPackets": ipsecIkeTotalTransOutboundPackets,
       "ipsecIkeTotalTransInboundTraffic": ipsecIkeTotalTransInboundTraffic,
       "ipsecIkeTotalTransOutboundTraffic": ipsecIkeTotalTransOutboundTraffic,
       "ipsecIkeErrorStats": ipsecIkeErrorStats,
       "ipsecIkeProtocolErrors": ipsecIkeProtocolErrors,
       "ipsecIkeDecryptionErrors": ipsecIkeDecryptionErrors,
       "ipsecIkeAuthenticationErrors": ipsecIkeAuthenticationErrors,
       "ipsecIkeOtherReceiveErrors": ipsecIkeOtherReceiveErrors,
       "ipsecIkeSendErrors": ipsecIkeSendErrors,
       "ipsecNotifications": ipsecNotifications,
       "ipsecNotifyMessageTotalCount": ipsecNotifyMessageTotalCount,
       "ipsecNotifyCountTable": ipsecNotifyCountTable,
       "ipsecNotifyCountEntry": ipsecNotifyCountEntry,
       "ipsecNotifyMessage": ipsecNotifyMessage,
       "ipsecNotifyMessageCount": ipsecNotifyMessageCount}
)
