# SNMP MIB module (XYLAN-CSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-CSM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:58 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xylanCsmArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanCsmArch")


# MODULE-IDENTITY


# Types definitions



class AtmxTrafficDescrParamIndex(Integer32):
    """Custom type AtmxTrafficDescrParamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XylanCsmMIB_ObjectIdentity = ObjectIdentity
xylanCsmMIB = _XylanCsmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1)
)
_AtmxVplGroup_ObjectIdentity = ObjectIdentity
atmxVplGroup = _AtmxVplGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 1)
)
_AtmxVplTable_Object = MibTable
atmxVplTable = _AtmxVplTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    atmxVplTable.setStatus("mandatory")
_AtmxVplEntry_Object = MibTableRow
atmxVplEntry = _AtmxVplEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 1, 1, 1)
)
atmxVplEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "atmxVplSlotIndex"),
    (0, "XYLAN-CSM-MIB", "atmxVplPortIndex"),
    (0, "XYLAN-CSM-MIB", "atmxVplVpi"),
)
if mibBuilder.loadTexts:
    atmxVplEntry.setStatus("mandatory")


class _AtmxVplSlotIndex_Type(Integer32):
    """Custom type atmxVplSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxVplSlotIndex_Type.__name__ = "Integer32"
_AtmxVplSlotIndex_Object = MibTableColumn
atmxVplSlotIndex = _AtmxVplSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 1, 1, 1, 1),
    _AtmxVplSlotIndex_Type()
)
atmxVplSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVplSlotIndex.setStatus("mandatory")


class _AtmxVplPortIndex_Type(Integer32):
    """Custom type atmxVplPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AtmxVplPortIndex_Type.__name__ = "Integer32"
_AtmxVplPortIndex_Object = MibTableColumn
atmxVplPortIndex = _AtmxVplPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 1, 1, 1, 2),
    _AtmxVplPortIndex_Type()
)
atmxVplPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVplPortIndex.setStatus("mandatory")


class _AtmxVplVpi_Type(Integer32):
    """Custom type atmxVplVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtmxVplVpi_Type.__name__ = "Integer32"
_AtmxVplVpi_Object = MibTableColumn
atmxVplVpi = _AtmxVplVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 1, 1, 1, 3),
    _AtmxVplVpi_Type()
)
atmxVplVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVplVpi.setStatus("mandatory")


class _AtmxVplAdminStatus_Type(Integer32):
    """Custom type atmxVplAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AtmxVplAdminStatus_Type.__name__ = "Integer32"
_AtmxVplAdminStatus_Object = MibTableColumn
atmxVplAdminStatus = _AtmxVplAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 1, 1, 1, 4),
    _AtmxVplAdminStatus_Type()
)
atmxVplAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVplAdminStatus.setStatus("mandatory")


class _AtmxVplOperStatus_Type(Integer32):
    """Custom type atmxVplOperStatus based on Integer32"""
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
        *(("end2endDown", 3),
          ("end2endup", 2),
          ("localDown", 5),
          ("localUpEndToEndUnknown", 4),
          ("unknown", 1))
    )


_AtmxVplOperStatus_Type.__name__ = "Integer32"
_AtmxVplOperStatus_Object = MibTableColumn
atmxVplOperStatus = _AtmxVplOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 1, 1, 1, 5),
    _AtmxVplOperStatus_Type()
)
atmxVplOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVplOperStatus.setStatus("mandatory")
_AtmxVplLastChange_Type = DisplayString
_AtmxVplLastChange_Object = MibTableColumn
atmxVplLastChange = _AtmxVplLastChange_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 1, 1, 1, 6),
    _AtmxVplLastChange_Type()
)
atmxVplLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVplLastChange.setStatus("mandatory")
_AtmxVplReceiveTrafficDescrIndex_Type = AtmxTrafficDescrParamIndex
_AtmxVplReceiveTrafficDescrIndex_Object = MibTableColumn
atmxVplReceiveTrafficDescrIndex = _AtmxVplReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 1, 1, 1, 7),
    _AtmxVplReceiveTrafficDescrIndex_Type()
)
atmxVplReceiveTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVplReceiveTrafficDescrIndex.setStatus("mandatory")
_AtmxVplTransmitTrafficDescrIndex_Type = AtmxTrafficDescrParamIndex
_AtmxVplTransmitTrafficDescrIndex_Object = MibTableColumn
atmxVplTransmitTrafficDescrIndex = _AtmxVplTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 1, 1, 1, 8),
    _AtmxVplTransmitTrafficDescrIndex_Type()
)
atmxVplTransmitTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVplTransmitTrafficDescrIndex.setStatus("mandatory")


class _AtmxVplCrossConnectIdentifier_Type(Integer32):
    """Custom type atmxVplCrossConnectIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmxVplCrossConnectIdentifier_Type.__name__ = "Integer32"
_AtmxVplCrossConnectIdentifier_Object = MibTableColumn
atmxVplCrossConnectIdentifier = _AtmxVplCrossConnectIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 1, 1, 1, 9),
    _AtmxVplCrossConnectIdentifier_Type()
)
atmxVplCrossConnectIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVplCrossConnectIdentifier.setStatus("mandatory")


class _AtmxVplRowStatus_Type(Integer32):
    """Custom type atmxVplRowStatus based on Integer32"""
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
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("notActive", 5))
    )


_AtmxVplRowStatus_Type.__name__ = "Integer32"
_AtmxVplRowStatus_Object = MibTableColumn
atmxVplRowStatus = _AtmxVplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 1, 1, 1, 10),
    _AtmxVplRowStatus_Type()
)
atmxVplRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVplRowStatus.setStatus("mandatory")


class _AtmxVplBidirect_Type(Integer32):
    """Custom type atmxVplBidirect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AtmxVplBidirect_Type.__name__ = "Integer32"
_AtmxVplBidirect_Object = MibTableColumn
atmxVplBidirect = _AtmxVplBidirect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 1, 1, 1, 11),
    _AtmxVplBidirect_Type()
)
atmxVplBidirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVplBidirect.setStatus("mandatory")
_AtmxInterfaceConfGroup_ObjectIdentity = ObjectIdentity
atmxInterfaceConfGroup = _AtmxInterfaceConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 2)
)
_AtmxInterfaceConfTable_Object = MibTable
atmxInterfaceConfTable = _AtmxInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    atmxInterfaceConfTable.setStatus("mandatory")
_AtmxInterfaceConfEntry_Object = MibTableRow
atmxInterfaceConfEntry = _AtmxInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 2, 1, 1)
)
atmxInterfaceConfEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "atmxInterfaceSlotIndex"),
    (0, "XYLAN-CSM-MIB", "atmxInterfacePortIndex"),
)
if mibBuilder.loadTexts:
    atmxInterfaceConfEntry.setStatus("mandatory")


class _AtmxInterfaceSlotIndex_Type(Integer32):
    """Custom type atmxInterfaceSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxInterfaceSlotIndex_Type.__name__ = "Integer32"
_AtmxInterfaceSlotIndex_Object = MibTableColumn
atmxInterfaceSlotIndex = _AtmxInterfaceSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 2, 1, 1, 1),
    _AtmxInterfaceSlotIndex_Type()
)
atmxInterfaceSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxInterfaceSlotIndex.setStatus("mandatory")


class _AtmxInterfacePortIndex_Type(Integer32):
    """Custom type atmxInterfacePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AtmxInterfacePortIndex_Type.__name__ = "Integer32"
_AtmxInterfacePortIndex_Object = MibTableColumn
atmxInterfacePortIndex = _AtmxInterfacePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 2, 1, 1, 2),
    _AtmxInterfacePortIndex_Type()
)
atmxInterfacePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxInterfacePortIndex.setStatus("mandatory")


class _AtmxInterfaceMaxVpcs_Type(Integer32):
    """Custom type atmxInterfaceMaxVpcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AtmxInterfaceMaxVpcs_Type.__name__ = "Integer32"
_AtmxInterfaceMaxVpcs_Object = MibTableColumn
atmxInterfaceMaxVpcs = _AtmxInterfaceMaxVpcs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 2, 1, 1, 3),
    _AtmxInterfaceMaxVpcs_Type()
)
atmxInterfaceMaxVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxInterfaceMaxVpcs.setStatus("mandatory")


class _AtmxInterfaceMaxVccs_Type(Integer32):
    """Custom type atmxInterfaceMaxVccs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AtmxInterfaceMaxVccs_Type.__name__ = "Integer32"
_AtmxInterfaceMaxVccs_Object = MibTableColumn
atmxInterfaceMaxVccs = _AtmxInterfaceMaxVccs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 2, 1, 1, 4),
    _AtmxInterfaceMaxVccs_Type()
)
atmxInterfaceMaxVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxInterfaceMaxVccs.setStatus("mandatory")


class _AtmxInterfaceConfVpcs_Type(Integer32):
    """Custom type atmxInterfaceConfVpcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AtmxInterfaceConfVpcs_Type.__name__ = "Integer32"
_AtmxInterfaceConfVpcs_Object = MibTableColumn
atmxInterfaceConfVpcs = _AtmxInterfaceConfVpcs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 2, 1, 1, 5),
    _AtmxInterfaceConfVpcs_Type()
)
atmxInterfaceConfVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxInterfaceConfVpcs.setStatus("mandatory")


class _AtmxInterfaceConfVccs_Type(Integer32):
    """Custom type atmxInterfaceConfVccs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AtmxInterfaceConfVccs_Type.__name__ = "Integer32"
_AtmxInterfaceConfVccs_Object = MibTableColumn
atmxInterfaceConfVccs = _AtmxInterfaceConfVccs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 2, 1, 1, 6),
    _AtmxInterfaceConfVccs_Type()
)
atmxInterfaceConfVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxInterfaceConfVccs.setStatus("mandatory")


class _AtmxInterfaceMaxActiveVpiBits_Type(Integer32):
    """Custom type atmxInterfaceMaxActiveVpiBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AtmxInterfaceMaxActiveVpiBits_Type.__name__ = "Integer32"
_AtmxInterfaceMaxActiveVpiBits_Object = MibTableColumn
atmxInterfaceMaxActiveVpiBits = _AtmxInterfaceMaxActiveVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 2, 1, 1, 7),
    _AtmxInterfaceMaxActiveVpiBits_Type()
)
atmxInterfaceMaxActiveVpiBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxInterfaceMaxActiveVpiBits.setStatus("mandatory")


class _AtmxInterfaceMaxActiveVciBits_Type(Integer32):
    """Custom type atmxInterfaceMaxActiveVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AtmxInterfaceMaxActiveVciBits_Type.__name__ = "Integer32"
_AtmxInterfaceMaxActiveVciBits_Object = MibTableColumn
atmxInterfaceMaxActiveVciBits = _AtmxInterfaceMaxActiveVciBits_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 2, 1, 1, 8),
    _AtmxInterfaceMaxActiveVciBits_Type()
)
atmxInterfaceMaxActiveVciBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxInterfaceMaxActiveVciBits.setStatus("mandatory")


class _AtmxInterfaceIlmiVpi_Type(Integer32):
    """Custom type atmxInterfaceIlmiVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmxInterfaceIlmiVpi_Type.__name__ = "Integer32"
_AtmxInterfaceIlmiVpi_Object = MibTableColumn
atmxInterfaceIlmiVpi = _AtmxInterfaceIlmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 2, 1, 1, 9),
    _AtmxInterfaceIlmiVpi_Type()
)
atmxInterfaceIlmiVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxInterfaceIlmiVpi.setStatus("mandatory")


class _AtmxInterfaceIlmiVci_Type(Integer32):
    """Custom type atmxInterfaceIlmiVci based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmxInterfaceIlmiVci_Type.__name__ = "Integer32"
_AtmxInterfaceIlmiVci_Object = MibTableColumn
atmxInterfaceIlmiVci = _AtmxInterfaceIlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 2, 1, 1, 10),
    _AtmxInterfaceIlmiVci_Type()
)
atmxInterfaceIlmiVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxInterfaceIlmiVci.setStatus("mandatory")


class _AtmxInterfaceAddressType_Type(Integer32):
    """Custom type atmxInterfaceAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("nativeE164", 3),
          ("nsapE164", 2),
          ("other", 4),
          ("private", 1))
    )


_AtmxInterfaceAddressType_Type.__name__ = "Integer32"
_AtmxInterfaceAddressType_Object = MibTableColumn
atmxInterfaceAddressType = _AtmxInterfaceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 2, 1, 1, 11),
    _AtmxInterfaceAddressType_Type()
)
atmxInterfaceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxInterfaceAddressType.setStatus("mandatory")
_AtmxVclGroup_ObjectIdentity = ObjectIdentity
atmxVclGroup = _AtmxVclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3)
)
_AtmxVclTable_Object = MibTable
atmxVclTable = _AtmxVclTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    atmxVclTable.setStatus("mandatory")
_AtmxVclEntry_Object = MibTableRow
atmxVclEntry = _AtmxVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1, 1)
)
atmxVclEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "atmxVclSlotIndex"),
    (0, "XYLAN-CSM-MIB", "atmxVclPortIndex"),
    (0, "XYLAN-CSM-MIB", "atmxVclVpi"),
    (0, "XYLAN-CSM-MIB", "atmxVclVci"),
)
if mibBuilder.loadTexts:
    atmxVclEntry.setStatus("mandatory")


class _AtmxVclSlotIndex_Type(Integer32):
    """Custom type atmxVclSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxVclSlotIndex_Type.__name__ = "Integer32"
_AtmxVclSlotIndex_Object = MibTableColumn
atmxVclSlotIndex = _AtmxVclSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1, 1, 1),
    _AtmxVclSlotIndex_Type()
)
atmxVclSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVclSlotIndex.setStatus("mandatory")


class _AtmxVclPortIndex_Type(Integer32):
    """Custom type atmxVclPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AtmxVclPortIndex_Type.__name__ = "Integer32"
_AtmxVclPortIndex_Object = MibTableColumn
atmxVclPortIndex = _AtmxVclPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1, 1, 2),
    _AtmxVclPortIndex_Type()
)
atmxVclPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVclPortIndex.setStatus("mandatory")


class _AtmxVclVpi_Type(Integer32):
    """Custom type atmxVclVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmxVclVpi_Type.__name__ = "Integer32"
_AtmxVclVpi_Object = MibTableColumn
atmxVclVpi = _AtmxVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1, 1, 3),
    _AtmxVclVpi_Type()
)
atmxVclVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVclVpi.setStatus("mandatory")


class _AtmxVclVci_Type(Integer32):
    """Custom type atmxVclVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmxVclVci_Type.__name__ = "Integer32"
_AtmxVclVci_Object = MibTableColumn
atmxVclVci = _AtmxVclVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1, 1, 4),
    _AtmxVclVci_Type()
)
atmxVclVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVclVci.setStatus("mandatory")


class _AtmxVclAdminStatus_Type(Integer32):
    """Custom type atmxVclAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AtmxVclAdminStatus_Type.__name__ = "Integer32"
_AtmxVclAdminStatus_Object = MibTableColumn
atmxVclAdminStatus = _AtmxVclAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1, 1, 5),
    _AtmxVclAdminStatus_Type()
)
atmxVclAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVclAdminStatus.setStatus("mandatory")


class _AtmxVclOperStatus_Type(Integer32):
    """Custom type atmxVclOperStatus based on Integer32"""
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
        *(("end2endDown", 3),
          ("end2endup", 2),
          ("localDown", 5),
          ("localUpEndToEndUnknown", 4),
          ("unknown", 1))
    )


_AtmxVclOperStatus_Type.__name__ = "Integer32"
_AtmxVclOperStatus_Object = MibTableColumn
atmxVclOperStatus = _AtmxVclOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1, 1, 6),
    _AtmxVclOperStatus_Type()
)
atmxVclOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVclOperStatus.setStatus("mandatory")
_AtmxVclLastChange_Type = DisplayString
_AtmxVclLastChange_Object = MibTableColumn
atmxVclLastChange = _AtmxVclLastChange_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1, 1, 7),
    _AtmxVclLastChange_Type()
)
atmxVclLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVclLastChange.setStatus("mandatory")
_AtmxVclReceiveTrafficDescrIndex_Type = AtmxTrafficDescrParamIndex
_AtmxVclReceiveTrafficDescrIndex_Object = MibTableColumn
atmxVclReceiveTrafficDescrIndex = _AtmxVclReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1, 1, 8),
    _AtmxVclReceiveTrafficDescrIndex_Type()
)
atmxVclReceiveTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVclReceiveTrafficDescrIndex.setStatus("mandatory")
_AtmxVclTransmitTrafficDescrIndex_Type = AtmxTrafficDescrParamIndex
_AtmxVclTransmitTrafficDescrIndex_Object = MibTableColumn
atmxVclTransmitTrafficDescrIndex = _AtmxVclTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1, 1, 9),
    _AtmxVclTransmitTrafficDescrIndex_Type()
)
atmxVclTransmitTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVclTransmitTrafficDescrIndex.setStatus("mandatory")


class _AtmxVccAalType_Type(Integer32):
    """Custom type atmxVccAalType based on Integer32"""
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
        *(("aal1", 1),
          ("aal34", 2),
          ("aal5", 3),
          ("other", 4),
          ("unknown", 5))
    )


_AtmxVccAalType_Type.__name__ = "Integer32"
_AtmxVccAalType_Object = MibTableColumn
atmxVccAalType = _AtmxVccAalType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1, 1, 10),
    _AtmxVccAalType_Type()
)
atmxVccAalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccAalType.setStatus("mandatory")


class _AtmxVccAal5CpcsTransmitSduSize_Type(Integer32):
    """Custom type atmxVccAal5CpcsTransmitSduSize based on Integer32"""
    defaultValue = 9188

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmxVccAal5CpcsTransmitSduSize_Type.__name__ = "Integer32"
_AtmxVccAal5CpcsTransmitSduSize_Object = MibTableColumn
atmxVccAal5CpcsTransmitSduSize = _AtmxVccAal5CpcsTransmitSduSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1, 1, 11),
    _AtmxVccAal5CpcsTransmitSduSize_Type()
)
atmxVccAal5CpcsTransmitSduSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccAal5CpcsTransmitSduSize.setStatus("mandatory")


class _AtmxVccAal5CpcsReceiveSduSize_Type(Integer32):
    """Custom type atmxVccAal5CpcsReceiveSduSize based on Integer32"""
    defaultValue = 9188

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmxVccAal5CpcsReceiveSduSize_Type.__name__ = "Integer32"
_AtmxVccAal5CpcsReceiveSduSize_Object = MibTableColumn
atmxVccAal5CpcsReceiveSduSize = _AtmxVccAal5CpcsReceiveSduSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1, 1, 12),
    _AtmxVccAal5CpcsReceiveSduSize_Type()
)
atmxVccAal5CpcsReceiveSduSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccAal5CpcsReceiveSduSize.setStatus("mandatory")


class _AtmxVccAal5EncapsType_Type(Integer32):
    """Custom type atmxVccAal5EncapsType based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("llcEncapsulation", 7),
          ("multiprotocolFrameRelaySscs", 8),
          ("other", 9),
          ("unknown", 10),
          ("vcMultiplexBridgedProtocol8023", 2),
          ("vcMultiplexBridgedProtocol8025", 3),
          ("vcMultiplexBridgedProtocol8026", 4),
          ("vcMultiplexLANemulation8023", 5),
          ("vcMultiplexLANemulation8025", 6),
          ("vcMultiplexRoutedProtocol", 1))
    )


_AtmxVccAal5EncapsType_Type.__name__ = "Integer32"
_AtmxVccAal5EncapsType_Object = MibTableColumn
atmxVccAal5EncapsType = _AtmxVccAal5EncapsType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1, 1, 13),
    _AtmxVccAal5EncapsType_Type()
)
atmxVccAal5EncapsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccAal5EncapsType.setStatus("mandatory")


class _AtmxVclCrossConnectIdentifier_Type(Integer32):
    """Custom type atmxVclCrossConnectIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmxVclCrossConnectIdentifier_Type.__name__ = "Integer32"
_AtmxVclCrossConnectIdentifier_Object = MibTableColumn
atmxVclCrossConnectIdentifier = _AtmxVclCrossConnectIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1, 1, 14),
    _AtmxVclCrossConnectIdentifier_Type()
)
atmxVclCrossConnectIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVclCrossConnectIdentifier.setStatus("mandatory")


class _AtmxVclRowStatus_Type(Integer32):
    """Custom type atmxVclRowStatus based on Integer32"""
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
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("notActive", 5))
    )


_AtmxVclRowStatus_Type.__name__ = "Integer32"
_AtmxVclRowStatus_Object = MibTableColumn
atmxVclRowStatus = _AtmxVclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1, 1, 15),
    _AtmxVclRowStatus_Type()
)
atmxVclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVclRowStatus.setStatus("mandatory")


class _AtmxVclBidirect_Type(Integer32):
    """Custom type atmxVclBidirect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AtmxVclBidirect_Type.__name__ = "Integer32"
_AtmxVclBidirect_Object = MibTableColumn
atmxVclBidirect = _AtmxVclBidirect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 3, 1, 1, 16),
    _AtmxVclBidirect_Type()
)
atmxVclBidirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVclBidirect.setStatus("mandatory")
_XylnatmInterfaceConfGroup_ObjectIdentity = ObjectIdentity
xylnatmInterfaceConfGroup = _XylnatmInterfaceConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4)
)
_XylnatmInterfaceConfTable_Object = MibTable
xylnatmInterfaceConfTable = _XylnatmInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1)
)
if mibBuilder.loadTexts:
    xylnatmInterfaceConfTable.setStatus("mandatory")
_XylnatmInterfaceConfEntry_Object = MibTableRow
xylnatmInterfaceConfEntry = _XylnatmInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1)
)
xylnatmInterfaceConfEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "xylnatmInterfaceSlotIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmInterfacePortIndex"),
)
if mibBuilder.loadTexts:
    xylnatmInterfaceConfEntry.setStatus("mandatory")


class _XylnatmInterfaceSlotIndex_Type(Integer32):
    """Custom type xylnatmInterfaceSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_XylnatmInterfaceSlotIndex_Type.__name__ = "Integer32"
_XylnatmInterfaceSlotIndex_Object = MibTableColumn
xylnatmInterfaceSlotIndex = _XylnatmInterfaceSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 1),
    _XylnatmInterfaceSlotIndex_Type()
)
xylnatmInterfaceSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceSlotIndex.setStatus("mandatory")


class _XylnatmInterfacePortIndex_Type(Integer32):
    """Custom type xylnatmInterfacePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_XylnatmInterfacePortIndex_Type.__name__ = "Integer32"
_XylnatmInterfacePortIndex_Object = MibTableColumn
xylnatmInterfacePortIndex = _XylnatmInterfacePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 2),
    _XylnatmInterfacePortIndex_Type()
)
xylnatmInterfacePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfacePortIndex.setStatus("mandatory")
_XylnatmInterfaceDescription_Type = DisplayString
_XylnatmInterfaceDescription_Object = MibTableColumn
xylnatmInterfaceDescription = _XylnatmInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 3),
    _XylnatmInterfaceDescription_Type()
)
xylnatmInterfaceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmInterfaceDescription.setStatus("mandatory")


class _XylnatmInterfaceTransType_Type(Integer32):
    """Custom type xylnatmInterfaceTransType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              20)
        )
    )
    namedValues = NamedValues(
        *(("ds1", 8),
          ("ds3", 3),
          ("e1", 9),
          ("e3", 6),
          ("eightb10b", 5),
          ("fourb5b", 4),
          ("internal", 20),
          ("sonetSts12", 7),
          ("sonetSts3", 2),
          ("unknown", 1))
    )


_XylnatmInterfaceTransType_Type.__name__ = "Integer32"
_XylnatmInterfaceTransType_Object = MibTableColumn
xylnatmInterfaceTransType = _XylnatmInterfaceTransType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 4),
    _XylnatmInterfaceTransType_Type()
)
xylnatmInterfaceTransType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceTransType.setStatus("mandatory")


class _XylnatmInterfaceType_Type(Integer32):
    """Custom type xylnatmInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nni-iisp-network", 4),
          ("nni-iisp-user", 5),
          ("other", 6),
          ("pnni10", 3),
          ("private", 2),
          ("public", 1))
    )


_XylnatmInterfaceType_Type.__name__ = "Integer32"
_XylnatmInterfaceType_Object = MibTableColumn
xylnatmInterfaceType = _XylnatmInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 5),
    _XylnatmInterfaceType_Type()
)
xylnatmInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmInterfaceType.setStatus("mandatory")


class _XylnatmInterfaceMediaType_Type(Integer32):
    """Custom type xylnatmInterfaceMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("coax", 2),
          ("internal", 7),
          ("multimode", 4),
          ("singlemode", 3),
          ("stp", 5),
          ("unknown", 1),
          ("utp", 6))
    )


_XylnatmInterfaceMediaType_Type.__name__ = "Integer32"
_XylnatmInterfaceMediaType_Object = MibTableColumn
xylnatmInterfaceMediaType = _XylnatmInterfaceMediaType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 6),
    _XylnatmInterfaceMediaType_Type()
)
xylnatmInterfaceMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceMediaType.setStatus("mandatory")
_XylnatmInterfaceAtmAddress_Type = DisplayString
_XylnatmInterfaceAtmAddress_Object = MibTableColumn
xylnatmInterfaceAtmAddress = _XylnatmInterfaceAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 7),
    _XylnatmInterfaceAtmAddress_Type()
)
xylnatmInterfaceAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmInterfaceAtmAddress.setStatus("mandatory")


class _XylnatmInterfacePortMode_Type(Integer32):
    """Custom type xylnatmInterfacePortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 3),
          ("off", 1),
          ("passthru", 2))
    )


_XylnatmInterfacePortMode_Type.__name__ = "Integer32"
_XylnatmInterfacePortMode_Object = MibTableColumn
xylnatmInterfacePortMode = _XylnatmInterfacePortMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 8),
    _XylnatmInterfacePortMode_Type()
)
xylnatmInterfacePortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfacePortMode.setStatus("mandatory")


class _XylnatmInterfaceOperStatus_Type(Integer32):
    """Custom type xylnatmInterfaceOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_XylnatmInterfaceOperStatus_Type.__name__ = "Integer32"
_XylnatmInterfaceOperStatus_Object = MibTableColumn
xylnatmInterfaceOperStatus = _XylnatmInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 9),
    _XylnatmInterfaceOperStatus_Type()
)
xylnatmInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceOperStatus.setStatus("mandatory")


class _XylnatmInterfaceQsaalStatus_Type(Integer32):
    """Custom type xylnatmInterfaceQsaalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_XylnatmInterfaceQsaalStatus_Type.__name__ = "Integer32"
_XylnatmInterfaceQsaalStatus_Object = MibTableColumn
xylnatmInterfaceQsaalStatus = _XylnatmInterfaceQsaalStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 10),
    _XylnatmInterfaceQsaalStatus_Type()
)
xylnatmInterfaceQsaalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceQsaalStatus.setStatus("mandatory")


class _XylnatmInterfaceIlmiStatus_Type(Integer32):
    """Custom type xylnatmInterfaceIlmiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_XylnatmInterfaceIlmiStatus_Type.__name__ = "Integer32"
_XylnatmInterfaceIlmiStatus_Object = MibTableColumn
xylnatmInterfaceIlmiStatus = _XylnatmInterfaceIlmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 11),
    _XylnatmInterfaceIlmiStatus_Type()
)
xylnatmInterfaceIlmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceIlmiStatus.setStatus("mandatory")


class _XylnatmInterfaceTpRedirect_Type(Integer32):
    """Custom type xylnatmInterfaceTpRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_XylnatmInterfaceTpRedirect_Type.__name__ = "Integer32"
_XylnatmInterfaceTpRedirect_Object = MibTableColumn
xylnatmInterfaceTpRedirect = _XylnatmInterfaceTpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 12),
    _XylnatmInterfaceTpRedirect_Type()
)
xylnatmInterfaceTpRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceTpRedirect.setStatus("mandatory")


class _XylnatmInterfaceCutOverSlot_Type(Integer32):
    """Custom type xylnatmInterfaceCutOverSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_XylnatmInterfaceCutOverSlot_Type.__name__ = "Integer32"
_XylnatmInterfaceCutOverSlot_Object = MibTableColumn
xylnatmInterfaceCutOverSlot = _XylnatmInterfaceCutOverSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 13),
    _XylnatmInterfaceCutOverSlot_Type()
)
xylnatmInterfaceCutOverSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmInterfaceCutOverSlot.setStatus("mandatory")


class _XylnatmInterfaceCutOverPort_Type(Integer32):
    """Custom type xylnatmInterfaceCutOverPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_XylnatmInterfaceCutOverPort_Type.__name__ = "Integer32"
_XylnatmInterfaceCutOverPort_Object = MibTableColumn
xylnatmInterfaceCutOverPort = _XylnatmInterfaceCutOverPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 14),
    _XylnatmInterfaceCutOverPort_Type()
)
xylnatmInterfaceCutOverPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmInterfaceCutOverPort.setStatus("mandatory")


class _XylnatmInterfaceClearPortStats_Type(Integer32):
    """Custom type xylnatmInterfaceClearPortStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_XylnatmInterfaceClearPortStats_Type.__name__ = "Integer32"
_XylnatmInterfaceClearPortStats_Object = MibTableColumn
xylnatmInterfaceClearPortStats = _XylnatmInterfaceClearPortStats_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 15),
    _XylnatmInterfaceClearPortStats_Type()
)
xylnatmInterfaceClearPortStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmInterfaceClearPortStats.setStatus("mandatory")


class _XylnatmInterfaceClearChanStats_Type(Integer32):
    """Custom type xylnatmInterfaceClearChanStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_XylnatmInterfaceClearChanStats_Type.__name__ = "Integer32"
_XylnatmInterfaceClearChanStats_Object = MibTableColumn
xylnatmInterfaceClearChanStats = _XylnatmInterfaceClearChanStats_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 16),
    _XylnatmInterfaceClearChanStats_Type()
)
xylnatmInterfaceClearChanStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmInterfaceClearChanStats.setStatus("mandatory")


class _XylnatmInterfaceClearSlotStats_Type(Integer32):
    """Custom type xylnatmInterfaceClearSlotStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_XylnatmInterfaceClearSlotStats_Type.__name__ = "Integer32"
_XylnatmInterfaceClearSlotStats_Object = MibTableColumn
xylnatmInterfaceClearSlotStats = _XylnatmInterfaceClearSlotStats_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 17),
    _XylnatmInterfaceClearSlotStats_Type()
)
xylnatmInterfaceClearSlotStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmInterfaceClearSlotStats.setStatus("mandatory")


class _XylnatmInterfaceTransmissionType_Type(Integer32):
    """Custom type xylnatmInterfaceTransmissionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 4),
          ("sdh", 2),
          ("sonet12c", 3),
          ("sonet3c", 1))
    )


_XylnatmInterfaceTransmissionType_Type.__name__ = "Integer32"
_XylnatmInterfaceTransmissionType_Object = MibTableColumn
xylnatmInterfaceTransmissionType = _XylnatmInterfaceTransmissionType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 18),
    _XylnatmInterfaceTransmissionType_Type()
)
xylnatmInterfaceTransmissionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmInterfaceTransmissionType.setStatus("mandatory")


class _XylnatmInterfaceIlmiState_Type(Integer32):
    """Custom type xylnatmInterfaceIlmiState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmInterfaceIlmiState_Type.__name__ = "Integer32"
_XylnatmInterfaceIlmiState_Object = MibTableColumn
xylnatmInterfaceIlmiState = _XylnatmInterfaceIlmiState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 19),
    _XylnatmInterfaceIlmiState_Type()
)
xylnatmInterfaceIlmiState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmInterfaceIlmiState.setStatus("mandatory")


class _XylnatmInterfaceTimingMode_Type(Integer32):
    """Custom type xylnatmInterfaceTimingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("loop", 2))
    )


_XylnatmInterfaceTimingMode_Type.__name__ = "Integer32"
_XylnatmInterfaceTimingMode_Object = MibTableColumn
xylnatmInterfaceTimingMode = _XylnatmInterfaceTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 20),
    _XylnatmInterfaceTimingMode_Type()
)
xylnatmInterfaceTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmInterfaceTimingMode.setStatus("mandatory")


class _XylnatmInterfaceLocalSrc_Type(Integer32):
    """Custom type xylnatmInterfaceLocalSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busLine19M", 3),
          ("busLine8K", 2),
          ("oscillator", 1))
    )


_XylnatmInterfaceLocalSrc_Type.__name__ = "Integer32"
_XylnatmInterfaceLocalSrc_Object = MibTableColumn
xylnatmInterfaceLocalSrc = _XylnatmInterfaceLocalSrc_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 21),
    _XylnatmInterfaceLocalSrc_Type()
)
xylnatmInterfaceLocalSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmInterfaceLocalSrc.setStatus("mandatory")


class _XylnatmInterfaceUniVersion_Type(Integer32):
    """Custom type xylnatmInterfaceUniVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("uni30", 1),
          ("uni31", 2),
          ("uniIisp", 3))
    )


_XylnatmInterfaceUniVersion_Type.__name__ = "Integer32"
_XylnatmInterfaceUniVersion_Object = MibTableColumn
xylnatmInterfaceUniVersion = _XylnatmInterfaceUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 1, 1, 22),
    _XylnatmInterfaceUniVersion_Type()
)
xylnatmInterfaceUniVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmInterfaceUniVersion.setStatus("mandatory")
_XylnatmILMIConfTable_Object = MibTable
xylnatmILMIConfTable = _XylnatmILMIConfTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3)
)
if mibBuilder.loadTexts:
    xylnatmILMIConfTable.setStatus("mandatory")
_XylnatmILMIConfEntry_Object = MibTableRow
xylnatmILMIConfEntry = _XylnatmILMIConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1)
)
xylnatmILMIConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xylnatmILMIConfEntry.setStatus("mandatory")
_XylnatmILMIConfSlot_Type = Integer32
_XylnatmILMIConfSlot_Object = MibTableColumn
xylnatmILMIConfSlot = _XylnatmILMIConfSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 1),
    _XylnatmILMIConfSlot_Type()
)
xylnatmILMIConfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmILMIConfSlot.setStatus("mandatory")
_XylnatmILMIConfPort_Type = Integer32
_XylnatmILMIConfPort_Object = MibTableColumn
xylnatmILMIConfPort = _XylnatmILMIConfPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 2),
    _XylnatmILMIConfPort_Type()
)
xylnatmILMIConfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmILMIConfPort.setStatus("mandatory")
_XylnatmILMIConfInstance_Type = Integer32
_XylnatmILMIConfInstance_Object = MibTableColumn
xylnatmILMIConfInstance = _XylnatmILMIConfInstance_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 3),
    _XylnatmILMIConfInstance_Type()
)
xylnatmILMIConfInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmILMIConfInstance.setStatus("mandatory")


class _XylnatmILMIConfILMIEnable_Type(Integer32):
    """Custom type xylnatmILMIConfILMIEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_XylnatmILMIConfILMIEnable_Type.__name__ = "Integer32"
_XylnatmILMIConfILMIEnable_Object = MibTableColumn
xylnatmILMIConfILMIEnable = _XylnatmILMIConfILMIEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 4),
    _XylnatmILMIConfILMIEnable_Type()
)
xylnatmILMIConfILMIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmILMIConfILMIEnable.setStatus("mandatory")


class _XylnatmILMIConfILMIPollEnable_Type(Integer32):
    """Custom type xylnatmILMIConfILMIPollEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_XylnatmILMIConfILMIPollEnable_Type.__name__ = "Integer32"
_XylnatmILMIConfILMIPollEnable_Object = MibTableColumn
xylnatmILMIConfILMIPollEnable = _XylnatmILMIConfILMIPollEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 5),
    _XylnatmILMIConfILMIPollEnable_Type()
)
xylnatmILMIConfILMIPollEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmILMIConfILMIPollEnable.setStatus("mandatory")


class _XylnatmILMIConfAutoCfgEnable_Type(Integer32):
    """Custom type xylnatmILMIConfAutoCfgEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_XylnatmILMIConfAutoCfgEnable_Type.__name__ = "Integer32"
_XylnatmILMIConfAutoCfgEnable_Object = MibTableColumn
xylnatmILMIConfAutoCfgEnable = _XylnatmILMIConfAutoCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 6),
    _XylnatmILMIConfAutoCfgEnable_Type()
)
xylnatmILMIConfAutoCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmILMIConfAutoCfgEnable.setStatus("mandatory")


class _XylnatmILMIConfAutoCfgStatus_Type(Integer32):
    """Custom type xylnatmILMIConfAutoCfgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cfgDone", 1),
          ("idle", 2),
          ("inProgress", 3))
    )


_XylnatmILMIConfAutoCfgStatus_Type.__name__ = "Integer32"
_XylnatmILMIConfAutoCfgStatus_Object = MibTableColumn
xylnatmILMIConfAutoCfgStatus = _XylnatmILMIConfAutoCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 7),
    _XylnatmILMIConfAutoCfgStatus_Type()
)
xylnatmILMIConfAutoCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmILMIConfAutoCfgStatus.setStatus("mandatory")


class _XylnatmILMIConfAutoCfgTrigg_Type(Integer32):
    """Custom type xylnatmILMIConfAutoCfgTrigg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("logic", 4),
          ("phy", 3),
          ("phyLogic", 2),
          ("unknown", 1))
    )


_XylnatmILMIConfAutoCfgTrigg_Type.__name__ = "Integer32"
_XylnatmILMIConfAutoCfgTrigg_Object = MibTableColumn
xylnatmILMIConfAutoCfgTrigg = _XylnatmILMIConfAutoCfgTrigg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 8),
    _XylnatmILMIConfAutoCfgTrigg_Type()
)
xylnatmILMIConfAutoCfgTrigg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmILMIConfAutoCfgTrigg.setStatus("mandatory")


class _XylnatmILMIConfAutoCfgDfltIf_Type(Integer32):
    """Custom type xylnatmILMIConfAutoCfgDfltIf based on Integer32"""
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
        *(("iispNetwork", 3),
          ("iispUser", 4),
          ("pnni", 2),
          ("privateUNI", 1),
          ("publicUNI", 5))
    )


_XylnatmILMIConfAutoCfgDfltIf_Type.__name__ = "Integer32"
_XylnatmILMIConfAutoCfgDfltIf_Object = MibTableColumn
xylnatmILMIConfAutoCfgDfltIf = _XylnatmILMIConfAutoCfgDfltIf_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 9),
    _XylnatmILMIConfAutoCfgDfltIf_Type()
)
xylnatmILMIConfAutoCfgDfltIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmILMIConfAutoCfgDfltIf.setStatus("mandatory")


class _XylnatmILMIConfAutoCfgDfltSigVer_Type(Integer32):
    """Custom type xylnatmILMIConfAutoCfgDfltSigVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("uni30", 1),
          ("uni31", 2),
          ("uni40", 3))
    )


_XylnatmILMIConfAutoCfgDfltSigVer_Type.__name__ = "Integer32"
_XylnatmILMIConfAutoCfgDfltSigVer_Object = MibTableColumn
xylnatmILMIConfAutoCfgDfltSigVer = _XylnatmILMIConfAutoCfgDfltSigVer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 10),
    _XylnatmILMIConfAutoCfgDfltSigVer_Type()
)
xylnatmILMIConfAutoCfgDfltSigVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmILMIConfAutoCfgDfltSigVer.setStatus("mandatory")


class _XylnatmILMIConfAutoCfgCurIf_Type(Integer32):
    """Custom type xylnatmILMIConfAutoCfgCurIf based on Integer32"""
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
        *(("iispNetwork", 3),
          ("iispUser", 4),
          ("pnni", 2),
          ("privateUNI", 1),
          ("publicUNI", 5))
    )


_XylnatmILMIConfAutoCfgCurIf_Type.__name__ = "Integer32"
_XylnatmILMIConfAutoCfgCurIf_Object = MibTableColumn
xylnatmILMIConfAutoCfgCurIf = _XylnatmILMIConfAutoCfgCurIf_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 11),
    _XylnatmILMIConfAutoCfgCurIf_Type()
)
xylnatmILMIConfAutoCfgCurIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmILMIConfAutoCfgCurIf.setStatus("mandatory")


class _XylnatmILMIConfAutoCfgCurSigVer_Type(Integer32):
    """Custom type xylnatmILMIConfAutoCfgCurSigVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("uni30", 1),
          ("uni31", 2),
          ("uni40", 3))
    )


_XylnatmILMIConfAutoCfgCurSigVer_Type.__name__ = "Integer32"
_XylnatmILMIConfAutoCfgCurSigVer_Object = MibTableColumn
xylnatmILMIConfAutoCfgCurSigVer = _XylnatmILMIConfAutoCfgCurSigVer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 12),
    _XylnatmILMIConfAutoCfgCurSigVer_Type()
)
xylnatmILMIConfAutoCfgCurSigVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmILMIConfAutoCfgCurSigVer.setStatus("mandatory")


class _XylnatmILMIConfAutoCfgCurILMIVer_Type(Integer32):
    """Custom type xylnatmILMIConfAutoCfgCurILMIVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ilmi40", 2),
          ("unsupported", 1))
    )


_XylnatmILMIConfAutoCfgCurILMIVer_Type.__name__ = "Integer32"
_XylnatmILMIConfAutoCfgCurILMIVer_Object = MibTableColumn
xylnatmILMIConfAutoCfgCurILMIVer = _XylnatmILMIConfAutoCfgCurILMIVer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 13),
    _XylnatmILMIConfAutoCfgCurILMIVer_Type()
)
xylnatmILMIConfAutoCfgCurILMIVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmILMIConfAutoCfgCurILMIVer.setStatus("mandatory")


class _XylnatmILMIConfPeerUniType_Type(Integer32):
    """Custom type xylnatmILMIConfPeerUniType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("public", 1))
    )


_XylnatmILMIConfPeerUniType_Type.__name__ = "Integer32"
_XylnatmILMIConfPeerUniType_Object = MibTableColumn
xylnatmILMIConfPeerUniType = _XylnatmILMIConfPeerUniType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 14),
    _XylnatmILMIConfPeerUniType_Type()
)
xylnatmILMIConfPeerUniType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmILMIConfPeerUniType.setStatus("mandatory")


class _XylnatmILMIConfPeerUniVer_Type(Integer32):
    """Custom type xylnatmILMIConfPeerUniVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("uni30", 1),
          ("uni31", 2),
          ("uni40", 3))
    )


_XylnatmILMIConfPeerUniVer_Type.__name__ = "Integer32"
_XylnatmILMIConfPeerUniVer_Object = MibTableColumn
xylnatmILMIConfPeerUniVer = _XylnatmILMIConfPeerUniVer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 15),
    _XylnatmILMIConfPeerUniVer_Type()
)
xylnatmILMIConfPeerUniVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmILMIConfPeerUniVer.setStatus("mandatory")


class _XylnatmILMIConfPeerDevType_Type(Integer32):
    """Custom type xylnatmILMIConfPeerDevType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("node", 2),
          ("user", 1))
    )


_XylnatmILMIConfPeerDevType_Type.__name__ = "Integer32"
_XylnatmILMIConfPeerDevType_Object = MibTableColumn
xylnatmILMIConfPeerDevType = _XylnatmILMIConfPeerDevType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 16),
    _XylnatmILMIConfPeerDevType_Type()
)
xylnatmILMIConfPeerDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmILMIConfPeerDevType.setStatus("mandatory")


class _XylnatmILMIConfPeerNNISigVer_Type(Integer32):
    """Custom type xylnatmILMIConfPeerNNISigVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iisp", 2),
          ("pnni10", 3),
          ("unsupported", 1))
    )


_XylnatmILMIConfPeerNNISigVer_Type.__name__ = "Integer32"
_XylnatmILMIConfPeerNNISigVer_Object = MibTableColumn
xylnatmILMIConfPeerNNISigVer = _XylnatmILMIConfPeerNNISigVer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 17),
    _XylnatmILMIConfPeerNNISigVer_Type()
)
xylnatmILMIConfPeerNNISigVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmILMIConfPeerNNISigVer.setStatus("mandatory")


class _XylnatmILMIConfPeerILMIVer_Type(Integer32):
    """Custom type xylnatmILMIConfPeerILMIVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ilmi40", 2),
          ("unsupported", 1))
    )


_XylnatmILMIConfPeerILMIVer_Type.__name__ = "Integer32"
_XylnatmILMIConfPeerILMIVer_Object = MibTableColumn
xylnatmILMIConfPeerILMIVer = _XylnatmILMIConfPeerILMIVer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 3, 1, 18),
    _XylnatmILMIConfPeerILMIVer_Type()
)
xylnatmILMIConfPeerILMIVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmILMIConfPeerILMIVer.setStatus("mandatory")
_AtmxVpCrossConnectGroup_ObjectIdentity = ObjectIdentity
atmxVpCrossConnectGroup = _AtmxVpCrossConnectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5)
)
_AtmxVpCrossConnectTable_Object = MibTable
atmxVpCrossConnectTable = _AtmxVpCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 1)
)
if mibBuilder.loadTexts:
    atmxVpCrossConnectTable.setStatus("mandatory")
_AtmxVpCrossConnectEntry_Object = MibTableRow
atmxVpCrossConnectEntry = _AtmxVpCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 1, 1)
)
atmxVpCrossConnectEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "atmxVpCrossConnectLowSlotIndex"),
    (0, "XYLAN-CSM-MIB", "atmxVpCrossConnectLowPortIndex"),
    (0, "XYLAN-CSM-MIB", "atmxVpCrossConnectLowVpi"),
    (0, "XYLAN-CSM-MIB", "atmxVpCrossConnectHighSlotIndex"),
    (0, "XYLAN-CSM-MIB", "atmxVpCrossConnectHighPortIndex"),
    (0, "XYLAN-CSM-MIB", "atmxVpCrossConnectHighVpi"),
)
if mibBuilder.loadTexts:
    atmxVpCrossConnectEntry.setStatus("mandatory")


class _AtmxVpCrossConnectIndex_Type(Integer32):
    """Custom type atmxVpCrossConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmxVpCrossConnectIndex_Type.__name__ = "Integer32"
_AtmxVpCrossConnectIndex_Object = MibTableColumn
atmxVpCrossConnectIndex = _AtmxVpCrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 1, 1, 1),
    _AtmxVpCrossConnectIndex_Type()
)
atmxVpCrossConnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVpCrossConnectIndex.setStatus("mandatory")


class _AtmxVpCrossConnectLowSlotIndex_Type(Integer32):
    """Custom type atmxVpCrossConnectLowSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxVpCrossConnectLowSlotIndex_Type.__name__ = "Integer32"
_AtmxVpCrossConnectLowSlotIndex_Object = MibTableColumn
atmxVpCrossConnectLowSlotIndex = _AtmxVpCrossConnectLowSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 1, 1, 2),
    _AtmxVpCrossConnectLowSlotIndex_Type()
)
atmxVpCrossConnectLowSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVpCrossConnectLowSlotIndex.setStatus("mandatory")
_AtmxVpCrossConnectLowPortIndex_Type = Integer32
_AtmxVpCrossConnectLowPortIndex_Object = MibTableColumn
atmxVpCrossConnectLowPortIndex = _AtmxVpCrossConnectLowPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 1, 1, 3),
    _AtmxVpCrossConnectLowPortIndex_Type()
)
atmxVpCrossConnectLowPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVpCrossConnectLowPortIndex.setStatus("mandatory")


class _AtmxVpCrossConnectLowVpi_Type(Integer32):
    """Custom type atmxVpCrossConnectLowVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtmxVpCrossConnectLowVpi_Type.__name__ = "Integer32"
_AtmxVpCrossConnectLowVpi_Object = MibTableColumn
atmxVpCrossConnectLowVpi = _AtmxVpCrossConnectLowVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 1, 1, 4),
    _AtmxVpCrossConnectLowVpi_Type()
)
atmxVpCrossConnectLowVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVpCrossConnectLowVpi.setStatus("mandatory")
_AtmxVpCrossConnectHighSlotIndex_Type = Integer32
_AtmxVpCrossConnectHighSlotIndex_Object = MibTableColumn
atmxVpCrossConnectHighSlotIndex = _AtmxVpCrossConnectHighSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 1, 1, 5),
    _AtmxVpCrossConnectHighSlotIndex_Type()
)
atmxVpCrossConnectHighSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVpCrossConnectHighSlotIndex.setStatus("mandatory")
_AtmxVpCrossConnectHighPortIndex_Type = Integer32
_AtmxVpCrossConnectHighPortIndex_Object = MibTableColumn
atmxVpCrossConnectHighPortIndex = _AtmxVpCrossConnectHighPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 1, 1, 6),
    _AtmxVpCrossConnectHighPortIndex_Type()
)
atmxVpCrossConnectHighPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVpCrossConnectHighPortIndex.setStatus("mandatory")


class _AtmxVpCrossConnectHighVpi_Type(Integer32):
    """Custom type atmxVpCrossConnectHighVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtmxVpCrossConnectHighVpi_Type.__name__ = "Integer32"
_AtmxVpCrossConnectHighVpi_Object = MibTableColumn
atmxVpCrossConnectHighVpi = _AtmxVpCrossConnectHighVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 1, 1, 7),
    _AtmxVpCrossConnectHighVpi_Type()
)
atmxVpCrossConnectHighVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVpCrossConnectHighVpi.setStatus("mandatory")


class _AtmxVpCrossConnectAdminStatus_Type(Integer32):
    """Custom type atmxVpCrossConnectAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AtmxVpCrossConnectAdminStatus_Type.__name__ = "Integer32"
_AtmxVpCrossConnectAdminStatus_Object = MibTableColumn
atmxVpCrossConnectAdminStatus = _AtmxVpCrossConnectAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 1, 1, 8),
    _AtmxVpCrossConnectAdminStatus_Type()
)
atmxVpCrossConnectAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVpCrossConnectAdminStatus.setStatus("mandatory")


class _AtmxVpCrossConnectL2HOperStatus_Type(Integer32):
    """Custom type atmxVpCrossConnectL2HOperStatus based on Integer32"""
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
        *(("end2endDown", 3),
          ("end2endup", 2),
          ("localDown", 5),
          ("localUpEndToEndUnknown", 4),
          ("unknown", 1))
    )


_AtmxVpCrossConnectL2HOperStatus_Type.__name__ = "Integer32"
_AtmxVpCrossConnectL2HOperStatus_Object = MibTableColumn
atmxVpCrossConnectL2HOperStatus = _AtmxVpCrossConnectL2HOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 1, 1, 9),
    _AtmxVpCrossConnectL2HOperStatus_Type()
)
atmxVpCrossConnectL2HOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVpCrossConnectL2HOperStatus.setStatus("mandatory")


class _AtmxVpCrossConnectH2LOperStatus_Type(Integer32):
    """Custom type atmxVpCrossConnectH2LOperStatus based on Integer32"""
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
        *(("end2endDown", 3),
          ("end2endup", 2),
          ("localDown", 5),
          ("localUpEndToEndUnknown", 4),
          ("unknown", 1))
    )


_AtmxVpCrossConnectH2LOperStatus_Type.__name__ = "Integer32"
_AtmxVpCrossConnectH2LOperStatus_Object = MibTableColumn
atmxVpCrossConnectH2LOperStatus = _AtmxVpCrossConnectH2LOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 1, 1, 10),
    _AtmxVpCrossConnectH2LOperStatus_Type()
)
atmxVpCrossConnectH2LOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVpCrossConnectH2LOperStatus.setStatus("mandatory")
_AtmxVpCrossConnectL2HLastChange_Type = DisplayString
_AtmxVpCrossConnectL2HLastChange_Object = MibTableColumn
atmxVpCrossConnectL2HLastChange = _AtmxVpCrossConnectL2HLastChange_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 1, 1, 11),
    _AtmxVpCrossConnectL2HLastChange_Type()
)
atmxVpCrossConnectL2HLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVpCrossConnectL2HLastChange.setStatus("mandatory")
_AtmxVpCrossConnectH2LLastChange_Type = DisplayString
_AtmxVpCrossConnectH2LLastChange_Object = MibTableColumn
atmxVpCrossConnectH2LLastChange = _AtmxVpCrossConnectH2LLastChange_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 1, 1, 12),
    _AtmxVpCrossConnectH2LLastChange_Type()
)
atmxVpCrossConnectH2LLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVpCrossConnectH2LLastChange.setStatus("mandatory")


class _AtmxVpCrossConnectRowStatus_Type(Integer32):
    """Custom type atmxVpCrossConnectRowStatus based on Integer32"""
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
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("notActive", 5))
    )


_AtmxVpCrossConnectRowStatus_Type.__name__ = "Integer32"
_AtmxVpCrossConnectRowStatus_Object = MibTableColumn
atmxVpCrossConnectRowStatus = _AtmxVpCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 1, 1, 13),
    _AtmxVpCrossConnectRowStatus_Type()
)
atmxVpCrossConnectRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVpCrossConnectRowStatus.setStatus("mandatory")
_AtmxSvcVpCrossConnectTable_Object = MibTable
atmxSvcVpCrossConnectTable = _AtmxSvcVpCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 2)
)
if mibBuilder.loadTexts:
    atmxSvcVpCrossConnectTable.setStatus("mandatory")
_AtmxSvcVpCrossConnectEntry_Object = MibTableRow
atmxSvcVpCrossConnectEntry = _AtmxSvcVpCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 2, 1)
)
atmxSvcVpCrossConnectEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "atmxSvcVpCrossConnectLowSlotIndex"),
    (0, "XYLAN-CSM-MIB", "atmxSvcVpCrossConnectLowPortIndex"),
    (0, "XYLAN-CSM-MIB", "atmxSvcVpCrossConnectLowVpi"),
    (0, "XYLAN-CSM-MIB", "atmxSvcVpCrossConnectHighSlotIndex"),
    (0, "XYLAN-CSM-MIB", "atmxSvcVpCrossConnectHighPortIndex"),
    (0, "XYLAN-CSM-MIB", "atmxSvcVpCrossConnectHighVpi"),
)
if mibBuilder.loadTexts:
    atmxSvcVpCrossConnectEntry.setStatus("mandatory")


class _AtmxSvcVpCrossConnectLowSlotIndex_Type(Integer32):
    """Custom type atmxSvcVpCrossConnectLowSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxSvcVpCrossConnectLowSlotIndex_Type.__name__ = "Integer32"
_AtmxSvcVpCrossConnectLowSlotIndex_Object = MibTableColumn
atmxSvcVpCrossConnectLowSlotIndex = _AtmxSvcVpCrossConnectLowSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 2, 1, 1),
    _AtmxSvcVpCrossConnectLowSlotIndex_Type()
)
atmxSvcVpCrossConnectLowSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxSvcVpCrossConnectLowSlotIndex.setStatus("mandatory")


class _AtmxSvcVpCrossConnectLowPortIndex_Type(Integer32):
    """Custom type atmxSvcVpCrossConnectLowPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_AtmxSvcVpCrossConnectLowPortIndex_Type.__name__ = "Integer32"
_AtmxSvcVpCrossConnectLowPortIndex_Object = MibTableColumn
atmxSvcVpCrossConnectLowPortIndex = _AtmxSvcVpCrossConnectLowPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 2, 1, 2),
    _AtmxSvcVpCrossConnectLowPortIndex_Type()
)
atmxSvcVpCrossConnectLowPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxSvcVpCrossConnectLowPortIndex.setStatus("mandatory")


class _AtmxSvcVpCrossConnectLowVpi_Type(Integer32):
    """Custom type atmxSvcVpCrossConnectLowVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtmxSvcVpCrossConnectLowVpi_Type.__name__ = "Integer32"
_AtmxSvcVpCrossConnectLowVpi_Object = MibTableColumn
atmxSvcVpCrossConnectLowVpi = _AtmxSvcVpCrossConnectLowVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 2, 1, 3),
    _AtmxSvcVpCrossConnectLowVpi_Type()
)
atmxSvcVpCrossConnectLowVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxSvcVpCrossConnectLowVpi.setStatus("mandatory")


class _AtmxSvcVpCrossConnectHighSlotIndex_Type(Integer32):
    """Custom type atmxSvcVpCrossConnectHighSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxSvcVpCrossConnectHighSlotIndex_Type.__name__ = "Integer32"
_AtmxSvcVpCrossConnectHighSlotIndex_Object = MibTableColumn
atmxSvcVpCrossConnectHighSlotIndex = _AtmxSvcVpCrossConnectHighSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 2, 1, 4),
    _AtmxSvcVpCrossConnectHighSlotIndex_Type()
)
atmxSvcVpCrossConnectHighSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxSvcVpCrossConnectHighSlotIndex.setStatus("mandatory")


class _AtmxSvcVpCrossConnectHighPortIndex_Type(Integer32):
    """Custom type atmxSvcVpCrossConnectHighPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_AtmxSvcVpCrossConnectHighPortIndex_Type.__name__ = "Integer32"
_AtmxSvcVpCrossConnectHighPortIndex_Object = MibTableColumn
atmxSvcVpCrossConnectHighPortIndex = _AtmxSvcVpCrossConnectHighPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 2, 1, 5),
    _AtmxSvcVpCrossConnectHighPortIndex_Type()
)
atmxSvcVpCrossConnectHighPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxSvcVpCrossConnectHighPortIndex.setStatus("mandatory")


class _AtmxSvcVpCrossConnectHighVpi_Type(Integer32):
    """Custom type atmxSvcVpCrossConnectHighVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtmxSvcVpCrossConnectHighVpi_Type.__name__ = "Integer32"
_AtmxSvcVpCrossConnectHighVpi_Object = MibTableColumn
atmxSvcVpCrossConnectHighVpi = _AtmxSvcVpCrossConnectHighVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 2, 1, 6),
    _AtmxSvcVpCrossConnectHighVpi_Type()
)
atmxSvcVpCrossConnectHighVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxSvcVpCrossConnectHighVpi.setStatus("mandatory")
_AtmxSvcVpCrossConnectCreationTime_Type = DisplayString
_AtmxSvcVpCrossConnectCreationTime_Object = MibTableColumn
atmxSvcVpCrossConnectCreationTime = _AtmxSvcVpCrossConnectCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 2, 1, 7),
    _AtmxSvcVpCrossConnectCreationTime_Type()
)
atmxSvcVpCrossConnectCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSvcVpCrossConnectCreationTime.setStatus("mandatory")
_AtmxSvcVpCrossConnectLowTDIndex_Type = Integer32
_AtmxSvcVpCrossConnectLowTDIndex_Object = MibTableColumn
atmxSvcVpCrossConnectLowTDIndex = _AtmxSvcVpCrossConnectLowTDIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 2, 1, 8),
    _AtmxSvcVpCrossConnectLowTDIndex_Type()
)
atmxSvcVpCrossConnectLowTDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSvcVpCrossConnectLowTDIndex.setStatus("mandatory")
_AtmxSvcVpCrossConnectHighTDIndex_Type = Integer32
_AtmxSvcVpCrossConnectHighTDIndex_Object = MibTableColumn
atmxSvcVpCrossConnectHighTDIndex = _AtmxSvcVpCrossConnectHighTDIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 2, 1, 9),
    _AtmxSvcVpCrossConnectHighTDIndex_Type()
)
atmxSvcVpCrossConnectHighTDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSvcVpCrossConnectHighTDIndex.setStatus("mandatory")
_AtmxSvcVpCrossConnectRowStatus_Type = Integer32
_AtmxSvcVpCrossConnectRowStatus_Object = MibTableColumn
atmxSvcVpCrossConnectRowStatus = _AtmxSvcVpCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 5, 2, 1, 10),
    _AtmxSvcVpCrossConnectRowStatus_Type()
)
atmxSvcVpCrossConnectRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSvcVpCrossConnectRowStatus.setStatus("mandatory")
_XylnatmInterfaceStatGroup_ObjectIdentity = ObjectIdentity
xylnatmInterfaceStatGroup = _XylnatmInterfaceStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6)
)
_XylnatmInterfaceStatTable_Object = MibTable
xylnatmInterfaceStatTable = _XylnatmInterfaceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1)
)
if mibBuilder.loadTexts:
    xylnatmInterfaceStatTable.setStatus("mandatory")
_XylnatmInterfaceStatEntry_Object = MibTableRow
xylnatmInterfaceStatEntry = _XylnatmInterfaceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1)
)
xylnatmInterfaceStatEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "xylnatmInterfaceStatSlotIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmInterfaceStatPortIndex"),
)
if mibBuilder.loadTexts:
    xylnatmInterfaceStatEntry.setStatus("mandatory")
_XylnatmInterfaceStatSlotIndex_Type = Integer32
_XylnatmInterfaceStatSlotIndex_Object = MibTableColumn
xylnatmInterfaceStatSlotIndex = _XylnatmInterfaceStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 1),
    _XylnatmInterfaceStatSlotIndex_Type()
)
xylnatmInterfaceStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatSlotIndex.setStatus("mandatory")
_XylnatmInterfaceStatPortIndex_Type = Integer32
_XylnatmInterfaceStatPortIndex_Object = MibTableColumn
xylnatmInterfaceStatPortIndex = _XylnatmInterfaceStatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 2),
    _XylnatmInterfaceStatPortIndex_Type()
)
xylnatmInterfaceStatPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatPortIndex.setStatus("mandatory")
_XylnatmInterfaceStatRxCells_Type = Counter32
_XylnatmInterfaceStatRxCells_Object = MibTableColumn
xylnatmInterfaceStatRxCells = _XylnatmInterfaceStatRxCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 3),
    _XylnatmInterfaceStatRxCells_Type()
)
xylnatmInterfaceStatRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatRxCells.setStatus("mandatory")
_XylnatmInterfaceStatRxClp0Cells_Type = Counter32
_XylnatmInterfaceStatRxClp0Cells_Object = MibTableColumn
xylnatmInterfaceStatRxClp0Cells = _XylnatmInterfaceStatRxClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 4),
    _XylnatmInterfaceStatRxClp0Cells_Type()
)
xylnatmInterfaceStatRxClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatRxClp0Cells.setStatus("mandatory")
_XylnatmInterfaceStatRxClp1Cells_Type = Counter32
_XylnatmInterfaceStatRxClp1Cells_Object = MibTableColumn
xylnatmInterfaceStatRxClp1Cells = _XylnatmInterfaceStatRxClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 5),
    _XylnatmInterfaceStatRxClp1Cells_Type()
)
xylnatmInterfaceStatRxClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatRxClp1Cells.setStatus("mandatory")
_XylnatmInterfaceStatTxCells_Type = Counter32
_XylnatmInterfaceStatTxCells_Object = MibTableColumn
xylnatmInterfaceStatTxCells = _XylnatmInterfaceStatTxCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 6),
    _XylnatmInterfaceStatTxCells_Type()
)
xylnatmInterfaceStatTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatTxCells.setStatus("mandatory")
_XylnatmInterfaceStatMarkEfciCells_Type = Counter32
_XylnatmInterfaceStatMarkEfciCells_Object = MibTableColumn
xylnatmInterfaceStatMarkEfciCells = _XylnatmInterfaceStatMarkEfciCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 7),
    _XylnatmInterfaceStatMarkEfciCells_Type()
)
xylnatmInterfaceStatMarkEfciCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatMarkEfciCells.setStatus("mandatory")
_XylnatmInterfaceStatMarkGcraCells_Type = Counter32
_XylnatmInterfaceStatMarkGcraCells_Object = MibTableColumn
xylnatmInterfaceStatMarkGcraCells = _XylnatmInterfaceStatMarkGcraCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 8),
    _XylnatmInterfaceStatMarkGcraCells_Type()
)
xylnatmInterfaceStatMarkGcraCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatMarkGcraCells.setStatus("mandatory")
_XylnatmInterfaceStatTotalDiscardCells_Type = Counter32
_XylnatmInterfaceStatTotalDiscardCells_Object = MibTableColumn
xylnatmInterfaceStatTotalDiscardCells = _XylnatmInterfaceStatTotalDiscardCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 9),
    _XylnatmInterfaceStatTotalDiscardCells_Type()
)
xylnatmInterfaceStatTotalDiscardCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatTotalDiscardCells.setStatus("mandatory")
_XylnatmInterfaceStatDxCongClp0Cells_Type = Counter32
_XylnatmInterfaceStatDxCongClp0Cells_Object = MibTableColumn
xylnatmInterfaceStatDxCongClp0Cells = _XylnatmInterfaceStatDxCongClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 10),
    _XylnatmInterfaceStatDxCongClp0Cells_Type()
)
xylnatmInterfaceStatDxCongClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatDxCongClp0Cells.setStatus("mandatory")
_XylnatmInterfaceStatDxCongClp1Cells_Type = Counter32
_XylnatmInterfaceStatDxCongClp1Cells_Object = MibTableColumn
xylnatmInterfaceStatDxCongClp1Cells = _XylnatmInterfaceStatDxCongClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 11),
    _XylnatmInterfaceStatDxCongClp1Cells_Type()
)
xylnatmInterfaceStatDxCongClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatDxCongClp1Cells.setStatus("mandatory")
_XylnatmInterfaceStatDxGcraClp0Cells_Type = Counter32
_XylnatmInterfaceStatDxGcraClp0Cells_Object = MibTableColumn
xylnatmInterfaceStatDxGcraClp0Cells = _XylnatmInterfaceStatDxGcraClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 12),
    _XylnatmInterfaceStatDxGcraClp0Cells_Type()
)
xylnatmInterfaceStatDxGcraClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatDxGcraClp0Cells.setStatus("mandatory")
_XylnatmInterfaceStatDxGcraClp1Cells_Type = Counter32
_XylnatmInterfaceStatDxGcraClp1Cells_Object = MibTableColumn
xylnatmInterfaceStatDxGcraClp1Cells = _XylnatmInterfaceStatDxGcraClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 13),
    _XylnatmInterfaceStatDxGcraClp1Cells_Type()
)
xylnatmInterfaceStatDxGcraClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatDxGcraClp1Cells.setStatus("mandatory")
_XylnatmInterfaceStatDxGcrabClp0Cells_Type = Counter32
_XylnatmInterfaceStatDxGcrabClp0Cells_Object = MibTableColumn
xylnatmInterfaceStatDxGcrabClp0Cells = _XylnatmInterfaceStatDxGcrabClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 14),
    _XylnatmInterfaceStatDxGcrabClp0Cells_Type()
)
xylnatmInterfaceStatDxGcrabClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatDxGcrabClp0Cells.setStatus("mandatory")
_XylnatmInterfaceStatDxGcrabClp1Cells_Type = Counter32
_XylnatmInterfaceStatDxGcrabClp1Cells_Object = MibTableColumn
xylnatmInterfaceStatDxGcrabClp1Cells = _XylnatmInterfaceStatDxGcrabClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 15),
    _XylnatmInterfaceStatDxGcrabClp1Cells_Type()
)
xylnatmInterfaceStatDxGcrabClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatDxGcrabClp1Cells.setStatus("mandatory")
_XylnatmInterfaceStatUnknownVpVcCells_Type = Counter32
_XylnatmInterfaceStatUnknownVpVcCells_Object = MibTableColumn
xylnatmInterfaceStatUnknownVpVcCells = _XylnatmInterfaceStatUnknownVpVcCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 16),
    _XylnatmInterfaceStatUnknownVpVcCells_Type()
)
xylnatmInterfaceStatUnknownVpVcCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatUnknownVpVcCells.setStatus("mandatory")
_XylnatmInterfaceStatUnknownVpiCells_Type = Counter32
_XylnatmInterfaceStatUnknownVpiCells_Object = MibTableColumn
xylnatmInterfaceStatUnknownVpiCells = _XylnatmInterfaceStatUnknownVpiCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 17),
    _XylnatmInterfaceStatUnknownVpiCells_Type()
)
xylnatmInterfaceStatUnknownVpiCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatUnknownVpiCells.setStatus("mandatory")
_XylnatmInterfaceStatUnknownVciCells_Type = Counter32
_XylnatmInterfaceStatUnknownVciCells_Object = MibTableColumn
xylnatmInterfaceStatUnknownVciCells = _XylnatmInterfaceStatUnknownVciCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 18),
    _XylnatmInterfaceStatUnknownVciCells_Type()
)
xylnatmInterfaceStatUnknownVciCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatUnknownVciCells.setStatus("mandatory")


class _XylnatmInterfaceStatUniType_Type(Integer32):
    """Custom type xylnatmInterfaceStatUniType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("public", 1))
    )


_XylnatmInterfaceStatUniType_Type.__name__ = "Integer32"
_XylnatmInterfaceStatUniType_Object = MibTableColumn
xylnatmInterfaceStatUniType = _XylnatmInterfaceStatUniType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 19),
    _XylnatmInterfaceStatUniType_Type()
)
xylnatmInterfaceStatUniType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatUniType.setStatus("mandatory")


class _XylnatmInterfaceStatUniVersion_Type(Integer32):
    """Custom type xylnatmInterfaceStatUniVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uni30", 1),
          ("uni31", 2))
    )


_XylnatmInterfaceStatUniVersion_Type.__name__ = "Integer32"
_XylnatmInterfaceStatUniVersion_Object = MibTableColumn
xylnatmInterfaceStatUniVersion = _XylnatmInterfaceStatUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 20),
    _XylnatmInterfaceStatUniVersion_Type()
)
xylnatmInterfaceStatUniVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatUniVersion.setStatus("mandatory")
_XylnatmInterfaceStatRemainingRxBandwidth_Type = Counter32
_XylnatmInterfaceStatRemainingRxBandwidth_Object = MibTableColumn
xylnatmInterfaceStatRemainingRxBandwidth = _XylnatmInterfaceStatRemainingRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 21),
    _XylnatmInterfaceStatRemainingRxBandwidth_Type()
)
xylnatmInterfaceStatRemainingRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatRemainingRxBandwidth.setStatus("mandatory")
_XylnatmInterfaceStatRemainingTxBandwidth_Type = Counter32
_XylnatmInterfaceStatRemainingTxBandwidth_Object = MibTableColumn
xylnatmInterfaceStatRemainingTxBandwidth = _XylnatmInterfaceStatRemainingTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 6, 1, 1, 22),
    _XylnatmInterfaceStatRemainingTxBandwidth_Type()
)
xylnatmInterfaceStatRemainingTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmInterfaceStatRemainingTxBandwidth.setStatus("mandatory")
_AtmxVcCrossConnectGroup_ObjectIdentity = ObjectIdentity
atmxVcCrossConnectGroup = _AtmxVcCrossConnectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7)
)
_AtmxVcCrossConnectTable_Object = MibTable
atmxVcCrossConnectTable = _AtmxVcCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 1)
)
if mibBuilder.loadTexts:
    atmxVcCrossConnectTable.setStatus("mandatory")
_AtmxVcCrossConnectEntry_Object = MibTableRow
atmxVcCrossConnectEntry = _AtmxVcCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 1, 1)
)
atmxVcCrossConnectEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "atmxVcCrossConnectLowSlotIndex"),
    (0, "XYLAN-CSM-MIB", "atmxVcCrossConnectLowPortIndex"),
    (0, "XYLAN-CSM-MIB", "atmxVcCrossConnectLowVpi"),
    (0, "XYLAN-CSM-MIB", "atmxVcCrossConnectLowVci"),
    (0, "XYLAN-CSM-MIB", "atmxVcCrossConnectHighSlotIndex"),
    (0, "XYLAN-CSM-MIB", "atmxVcCrossConnectHighPortIndex"),
    (0, "XYLAN-CSM-MIB", "atmxVcCrossConnectHighVpi"),
    (0, "XYLAN-CSM-MIB", "atmxVcCrossConnectHighVci"),
)
if mibBuilder.loadTexts:
    atmxVcCrossConnectEntry.setStatus("mandatory")


class _AtmxVcCrossConnectIndex_Type(Integer32):
    """Custom type atmxVcCrossConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmxVcCrossConnectIndex_Type.__name__ = "Integer32"
_AtmxVcCrossConnectIndex_Object = MibTableColumn
atmxVcCrossConnectIndex = _AtmxVcCrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 1, 1, 1),
    _AtmxVcCrossConnectIndex_Type()
)
atmxVcCrossConnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVcCrossConnectIndex.setStatus("mandatory")


class _AtmxVcCrossConnectLowSlotIndex_Type(Integer32):
    """Custom type atmxVcCrossConnectLowSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxVcCrossConnectLowSlotIndex_Type.__name__ = "Integer32"
_AtmxVcCrossConnectLowSlotIndex_Object = MibTableColumn
atmxVcCrossConnectLowSlotIndex = _AtmxVcCrossConnectLowSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 1, 1, 2),
    _AtmxVcCrossConnectLowSlotIndex_Type()
)
atmxVcCrossConnectLowSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVcCrossConnectLowSlotIndex.setStatus("mandatory")
_AtmxVcCrossConnectLowPortIndex_Type = Integer32
_AtmxVcCrossConnectLowPortIndex_Object = MibTableColumn
atmxVcCrossConnectLowPortIndex = _AtmxVcCrossConnectLowPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 1, 1, 3),
    _AtmxVcCrossConnectLowPortIndex_Type()
)
atmxVcCrossConnectLowPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVcCrossConnectLowPortIndex.setStatus("mandatory")


class _AtmxVcCrossConnectLowVpi_Type(Integer32):
    """Custom type atmxVcCrossConnectLowVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmxVcCrossConnectLowVpi_Type.__name__ = "Integer32"
_AtmxVcCrossConnectLowVpi_Object = MibTableColumn
atmxVcCrossConnectLowVpi = _AtmxVcCrossConnectLowVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 1, 1, 4),
    _AtmxVcCrossConnectLowVpi_Type()
)
atmxVcCrossConnectLowVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVcCrossConnectLowVpi.setStatus("mandatory")


class _AtmxVcCrossConnectLowVci_Type(Integer32):
    """Custom type atmxVcCrossConnectLowVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmxVcCrossConnectLowVci_Type.__name__ = "Integer32"
_AtmxVcCrossConnectLowVci_Object = MibTableColumn
atmxVcCrossConnectLowVci = _AtmxVcCrossConnectLowVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 1, 1, 5),
    _AtmxVcCrossConnectLowVci_Type()
)
atmxVcCrossConnectLowVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVcCrossConnectLowVci.setStatus("mandatory")


class _AtmxVcCrossConnectHighSlotIndex_Type(Integer32):
    """Custom type atmxVcCrossConnectHighSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxVcCrossConnectHighSlotIndex_Type.__name__ = "Integer32"
_AtmxVcCrossConnectHighSlotIndex_Object = MibTableColumn
atmxVcCrossConnectHighSlotIndex = _AtmxVcCrossConnectHighSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 1, 1, 6),
    _AtmxVcCrossConnectHighSlotIndex_Type()
)
atmxVcCrossConnectHighSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVcCrossConnectHighSlotIndex.setStatus("mandatory")
_AtmxVcCrossConnectHighPortIndex_Type = Integer32
_AtmxVcCrossConnectHighPortIndex_Object = MibTableColumn
atmxVcCrossConnectHighPortIndex = _AtmxVcCrossConnectHighPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 1, 1, 7),
    _AtmxVcCrossConnectHighPortIndex_Type()
)
atmxVcCrossConnectHighPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVcCrossConnectHighPortIndex.setStatus("mandatory")


class _AtmxVcCrossConnectHighVpi_Type(Integer32):
    """Custom type atmxVcCrossConnectHighVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmxVcCrossConnectHighVpi_Type.__name__ = "Integer32"
_AtmxVcCrossConnectHighVpi_Object = MibTableColumn
atmxVcCrossConnectHighVpi = _AtmxVcCrossConnectHighVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 1, 1, 8),
    _AtmxVcCrossConnectHighVpi_Type()
)
atmxVcCrossConnectHighVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVcCrossConnectHighVpi.setStatus("mandatory")


class _AtmxVcCrossConnectHighVci_Type(Integer32):
    """Custom type atmxVcCrossConnectHighVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmxVcCrossConnectHighVci_Type.__name__ = "Integer32"
_AtmxVcCrossConnectHighVci_Object = MibTableColumn
atmxVcCrossConnectHighVci = _AtmxVcCrossConnectHighVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 1, 1, 9),
    _AtmxVcCrossConnectHighVci_Type()
)
atmxVcCrossConnectHighVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVcCrossConnectHighVci.setStatus("mandatory")


class _AtmxVcCrossConnectAdminStatus_Type(Integer32):
    """Custom type atmxVcCrossConnectAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AtmxVcCrossConnectAdminStatus_Type.__name__ = "Integer32"
_AtmxVcCrossConnectAdminStatus_Object = MibTableColumn
atmxVcCrossConnectAdminStatus = _AtmxVcCrossConnectAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 1, 1, 10),
    _AtmxVcCrossConnectAdminStatus_Type()
)
atmxVcCrossConnectAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVcCrossConnectAdminStatus.setStatus("mandatory")


class _AtmxVcCrossConnectL2HOperStatus_Type(Integer32):
    """Custom type atmxVcCrossConnectL2HOperStatus based on Integer32"""
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
        *(("end2endDown", 3),
          ("end2endup", 2),
          ("localDown", 5),
          ("localUpEndToEndUnknown", 4),
          ("unknown", 1))
    )


_AtmxVcCrossConnectL2HOperStatus_Type.__name__ = "Integer32"
_AtmxVcCrossConnectL2HOperStatus_Object = MibTableColumn
atmxVcCrossConnectL2HOperStatus = _AtmxVcCrossConnectL2HOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 1, 1, 11),
    _AtmxVcCrossConnectL2HOperStatus_Type()
)
atmxVcCrossConnectL2HOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVcCrossConnectL2HOperStatus.setStatus("mandatory")


class _AtmxVcCrossConnectH2LOperStatus_Type(Integer32):
    """Custom type atmxVcCrossConnectH2LOperStatus based on Integer32"""
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
        *(("end2endDown", 3),
          ("end2endup", 2),
          ("localDown", 5),
          ("localUpEndToEndUnknown", 4),
          ("unknown", 1))
    )


_AtmxVcCrossConnectH2LOperStatus_Type.__name__ = "Integer32"
_AtmxVcCrossConnectH2LOperStatus_Object = MibTableColumn
atmxVcCrossConnectH2LOperStatus = _AtmxVcCrossConnectH2LOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 1, 1, 12),
    _AtmxVcCrossConnectH2LOperStatus_Type()
)
atmxVcCrossConnectH2LOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVcCrossConnectH2LOperStatus.setStatus("mandatory")
_AtmxVcCrossConnectL2HLastChange_Type = DisplayString
_AtmxVcCrossConnectL2HLastChange_Object = MibTableColumn
atmxVcCrossConnectL2HLastChange = _AtmxVcCrossConnectL2HLastChange_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 1, 1, 13),
    _AtmxVcCrossConnectL2HLastChange_Type()
)
atmxVcCrossConnectL2HLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVcCrossConnectL2HLastChange.setStatus("mandatory")
_AtmxVcCrossConnectH2LLastChange_Type = DisplayString
_AtmxVcCrossConnectH2LLastChange_Object = MibTableColumn
atmxVcCrossConnectH2LLastChange = _AtmxVcCrossConnectH2LLastChange_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 1, 1, 14),
    _AtmxVcCrossConnectH2LLastChange_Type()
)
atmxVcCrossConnectH2LLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVcCrossConnectH2LLastChange.setStatus("mandatory")


class _AtmxVcCrossConnectRowStatus_Type(Integer32):
    """Custom type atmxVcCrossConnectRowStatus based on Integer32"""
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
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("notActive", 5))
    )


_AtmxVcCrossConnectRowStatus_Type.__name__ = "Integer32"
_AtmxVcCrossConnectRowStatus_Object = MibTableColumn
atmxVcCrossConnectRowStatus = _AtmxVcCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 1, 1, 15),
    _AtmxVcCrossConnectRowStatus_Type()
)
atmxVcCrossConnectRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVcCrossConnectRowStatus.setStatus("mandatory")
_AtmxSvcVcCrossConnectTable_Object = MibTable
atmxSvcVcCrossConnectTable = _AtmxSvcVcCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 2)
)
if mibBuilder.loadTexts:
    atmxSvcVcCrossConnectTable.setStatus("mandatory")
_AtmxSvcVcCrossConnectEntry_Object = MibTableRow
atmxSvcVcCrossConnectEntry = _AtmxSvcVcCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 2, 1)
)
atmxSvcVcCrossConnectEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "atmxSvcVcCrossConnectLowSlotIndex"),
    (0, "XYLAN-CSM-MIB", "atmxSvcVcCrossConnectLowPortIndex"),
    (0, "XYLAN-CSM-MIB", "atmxSvcVcCrossConnectLowVpi"),
    (0, "XYLAN-CSM-MIB", "atmxSvcVcCrossConnectLowVci"),
    (0, "XYLAN-CSM-MIB", "atmxSvcVcCrossConnectHighSlotIndex"),
    (0, "XYLAN-CSM-MIB", "atmxSvcVcCrossConnectHighPortIndex"),
    (0, "XYLAN-CSM-MIB", "atmxSvcVcCrossConnectHighVpi"),
    (0, "XYLAN-CSM-MIB", "atmxSvcVcCrossConnectHighVci"),
)
if mibBuilder.loadTexts:
    atmxSvcVcCrossConnectEntry.setStatus("mandatory")


class _AtmxSvcVcCrossConnectLowSlotIndex_Type(Integer32):
    """Custom type atmxSvcVcCrossConnectLowSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxSvcVcCrossConnectLowSlotIndex_Type.__name__ = "Integer32"
_AtmxSvcVcCrossConnectLowSlotIndex_Object = MibTableColumn
atmxSvcVcCrossConnectLowSlotIndex = _AtmxSvcVcCrossConnectLowSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 2, 1, 1),
    _AtmxSvcVcCrossConnectLowSlotIndex_Type()
)
atmxSvcVcCrossConnectLowSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxSvcVcCrossConnectLowSlotIndex.setStatus("mandatory")


class _AtmxSvcVcCrossConnectLowPortIndex_Type(Integer32):
    """Custom type atmxSvcVcCrossConnectLowPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_AtmxSvcVcCrossConnectLowPortIndex_Type.__name__ = "Integer32"
_AtmxSvcVcCrossConnectLowPortIndex_Object = MibTableColumn
atmxSvcVcCrossConnectLowPortIndex = _AtmxSvcVcCrossConnectLowPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 2, 1, 2),
    _AtmxSvcVcCrossConnectLowPortIndex_Type()
)
atmxSvcVcCrossConnectLowPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxSvcVcCrossConnectLowPortIndex.setStatus("mandatory")


class _AtmxSvcVcCrossConnectLowVpi_Type(Integer32):
    """Custom type atmxSvcVcCrossConnectLowVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmxSvcVcCrossConnectLowVpi_Type.__name__ = "Integer32"
_AtmxSvcVcCrossConnectLowVpi_Object = MibTableColumn
atmxSvcVcCrossConnectLowVpi = _AtmxSvcVcCrossConnectLowVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 2, 1, 3),
    _AtmxSvcVcCrossConnectLowVpi_Type()
)
atmxSvcVcCrossConnectLowVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxSvcVcCrossConnectLowVpi.setStatus("mandatory")


class _AtmxSvcVcCrossConnectLowVci_Type(Integer32):
    """Custom type atmxSvcVcCrossConnectLowVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmxSvcVcCrossConnectLowVci_Type.__name__ = "Integer32"
_AtmxSvcVcCrossConnectLowVci_Object = MibTableColumn
atmxSvcVcCrossConnectLowVci = _AtmxSvcVcCrossConnectLowVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 2, 1, 4),
    _AtmxSvcVcCrossConnectLowVci_Type()
)
atmxSvcVcCrossConnectLowVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxSvcVcCrossConnectLowVci.setStatus("mandatory")


class _AtmxSvcVcCrossConnectHighSlotIndex_Type(Integer32):
    """Custom type atmxSvcVcCrossConnectHighSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxSvcVcCrossConnectHighSlotIndex_Type.__name__ = "Integer32"
_AtmxSvcVcCrossConnectHighSlotIndex_Object = MibTableColumn
atmxSvcVcCrossConnectHighSlotIndex = _AtmxSvcVcCrossConnectHighSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 2, 1, 5),
    _AtmxSvcVcCrossConnectHighSlotIndex_Type()
)
atmxSvcVcCrossConnectHighSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxSvcVcCrossConnectHighSlotIndex.setStatus("mandatory")
_AtmxSvcVcCrossConnectHighPortIndex_Type = Integer32
_AtmxSvcVcCrossConnectHighPortIndex_Object = MibTableColumn
atmxSvcVcCrossConnectHighPortIndex = _AtmxSvcVcCrossConnectHighPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 2, 1, 6),
    _AtmxSvcVcCrossConnectHighPortIndex_Type()
)
atmxSvcVcCrossConnectHighPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxSvcVcCrossConnectHighPortIndex.setStatus("mandatory")


class _AtmxSvcVcCrossConnectHighVpi_Type(Integer32):
    """Custom type atmxSvcVcCrossConnectHighVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmxSvcVcCrossConnectHighVpi_Type.__name__ = "Integer32"
_AtmxSvcVcCrossConnectHighVpi_Object = MibTableColumn
atmxSvcVcCrossConnectHighVpi = _AtmxSvcVcCrossConnectHighVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 2, 1, 7),
    _AtmxSvcVcCrossConnectHighVpi_Type()
)
atmxSvcVcCrossConnectHighVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxSvcVcCrossConnectHighVpi.setStatus("mandatory")


class _AtmxSvcVcCrossConnectHighVci_Type(Integer32):
    """Custom type atmxSvcVcCrossConnectHighVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmxSvcVcCrossConnectHighVci_Type.__name__ = "Integer32"
_AtmxSvcVcCrossConnectHighVci_Object = MibTableColumn
atmxSvcVcCrossConnectHighVci = _AtmxSvcVcCrossConnectHighVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 2, 1, 8),
    _AtmxSvcVcCrossConnectHighVci_Type()
)
atmxSvcVcCrossConnectHighVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxSvcVcCrossConnectHighVci.setStatus("mandatory")
_AtmxSvcVcCrossConnectCreationTime_Type = DisplayString
_AtmxSvcVcCrossConnectCreationTime_Object = MibTableColumn
atmxSvcVcCrossConnectCreationTime = _AtmxSvcVcCrossConnectCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 2, 1, 9),
    _AtmxSvcVcCrossConnectCreationTime_Type()
)
atmxSvcVcCrossConnectCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSvcVcCrossConnectCreationTime.setStatus("mandatory")
_AtmxSvcVcCrossConnectLowTDIndex_Type = Integer32
_AtmxSvcVcCrossConnectLowTDIndex_Object = MibTableColumn
atmxSvcVcCrossConnectLowTDIndex = _AtmxSvcVcCrossConnectLowTDIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 2, 1, 10),
    _AtmxSvcVcCrossConnectLowTDIndex_Type()
)
atmxSvcVcCrossConnectLowTDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSvcVcCrossConnectLowTDIndex.setStatus("mandatory")
_AtmxSvcVcCrossConnectHighTDIndex_Type = Integer32
_AtmxSvcVcCrossConnectHighTDIndex_Object = MibTableColumn
atmxSvcVcCrossConnectHighTDIndex = _AtmxSvcVcCrossConnectHighTDIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 2, 1, 11),
    _AtmxSvcVcCrossConnectHighTDIndex_Type()
)
atmxSvcVcCrossConnectHighTDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSvcVcCrossConnectHighTDIndex.setStatus("mandatory")
_AtmxSvcVcCrossConnectRowStatus_Type = Integer32
_AtmxSvcVcCrossConnectRowStatus_Object = MibTableColumn
atmxSvcVcCrossConnectRowStatus = _AtmxSvcVcCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 7, 2, 1, 12),
    _AtmxSvcVcCrossConnectRowStatus_Type()
)
atmxSvcVcCrossConnectRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSvcVcCrossConnectRowStatus.setStatus("mandatory")
_AtmxTrafficDescrGroup_ObjectIdentity = ObjectIdentity
atmxTrafficDescrGroup = _AtmxTrafficDescrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 8)
)
_AtmxTrafficDescrParamTable_Object = MibTable
atmxTrafficDescrParamTable = _AtmxTrafficDescrParamTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 8, 1)
)
if mibBuilder.loadTexts:
    atmxTrafficDescrParamTable.setStatus("mandatory")
_AtmxTrafficDescrParamEntry_Object = MibTableRow
atmxTrafficDescrParamEntry = _AtmxTrafficDescrParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 8, 1, 1)
)
atmxTrafficDescrParamEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "atmxTrafficDescrParamIndex"),
)
if mibBuilder.loadTexts:
    atmxTrafficDescrParamEntry.setStatus("mandatory")
_AtmxTrafficDescrParamIndex_Type = AtmxTrafficDescrParamIndex
_AtmxTrafficDescrParamIndex_Object = MibTableColumn
atmxTrafficDescrParamIndex = _AtmxTrafficDescrParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 8, 1, 1, 1),
    _AtmxTrafficDescrParamIndex_Type()
)
atmxTrafficDescrParamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxTrafficDescrParamIndex.setStatus("mandatory")


class _AtmxTrafficDescrType_Type(Integer32):
    """Custom type atmxTrafficDescrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("atmxClpNoTaggingNoScr", 3),
          ("atmxClpNoTaggingScr", 6),
          ("atmxClpTaggingNoScr", 4),
          ("atmxClpTaggingScr", 7),
          ("atmxNoClpNoScr", 2),
          ("atmxNoClpScr", 5),
          ("atmxNoTrafficDescriptor", 1))
    )


_AtmxTrafficDescrType_Type.__name__ = "Integer32"
_AtmxTrafficDescrType_Object = MibTableColumn
atmxTrafficDescrType = _AtmxTrafficDescrType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 8, 1, 1, 2),
    _AtmxTrafficDescrType_Type()
)
atmxTrafficDescrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxTrafficDescrType.setStatus("mandatory")


class _AtmxTrafficDescrParam1_Type(Integer32):
    """Custom type atmxTrafficDescrParam1 based on Integer32"""
    defaultValue = 0


_AtmxTrafficDescrParam1_Object = MibTableColumn
atmxTrafficDescrParam1 = _AtmxTrafficDescrParam1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 8, 1, 1, 3),
    _AtmxTrafficDescrParam1_Type()
)
atmxTrafficDescrParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxTrafficDescrParam1.setStatus("mandatory")


class _AtmxTrafficDescrParam2_Type(Integer32):
    """Custom type atmxTrafficDescrParam2 based on Integer32"""
    defaultValue = 0


_AtmxTrafficDescrParam2_Object = MibTableColumn
atmxTrafficDescrParam2 = _AtmxTrafficDescrParam2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 8, 1, 1, 4),
    _AtmxTrafficDescrParam2_Type()
)
atmxTrafficDescrParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxTrafficDescrParam2.setStatus("mandatory")


class _AtmxTrafficDescrParam3_Type(Integer32):
    """Custom type atmxTrafficDescrParam3 based on Integer32"""
    defaultValue = 0


_AtmxTrafficDescrParam3_Object = MibTableColumn
atmxTrafficDescrParam3 = _AtmxTrafficDescrParam3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 8, 1, 1, 5),
    _AtmxTrafficDescrParam3_Type()
)
atmxTrafficDescrParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxTrafficDescrParam3.setStatus("mandatory")


class _AtmxTrafficDescrParam4_Type(Integer32):
    """Custom type atmxTrafficDescrParam4 based on Integer32"""
    defaultValue = 0


_AtmxTrafficDescrParam4_Object = MibTableColumn
atmxTrafficDescrParam4 = _AtmxTrafficDescrParam4_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 8, 1, 1, 6),
    _AtmxTrafficDescrParam4_Type()
)
atmxTrafficDescrParam4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxTrafficDescrParam4.setStatus("mandatory")


class _AtmxTrafficDescrParam5_Type(Integer32):
    """Custom type atmxTrafficDescrParam5 based on Integer32"""
    defaultValue = 0


_AtmxTrafficDescrParam5_Object = MibTableColumn
atmxTrafficDescrParam5 = _AtmxTrafficDescrParam5_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 8, 1, 1, 7),
    _AtmxTrafficDescrParam5_Type()
)
atmxTrafficDescrParam5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxTrafficDescrParam5.setStatus("mandatory")


class _AtmxTrafficQoSClass_Type(Integer32):
    """Custom type atmxTrafficQoSClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmxTrafficQoSClass_Type.__name__ = "Integer32"
_AtmxTrafficQoSClass_Object = MibTableColumn
atmxTrafficQoSClass = _AtmxTrafficQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 8, 1, 1, 8),
    _AtmxTrafficQoSClass_Type()
)
atmxTrafficQoSClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxTrafficQoSClass.setStatus("mandatory")


class _AtmxTrafficDescrRowStatus_Type(Integer32):
    """Custom type atmxTrafficDescrRowStatus based on Integer32"""
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
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("notActive", 5))
    )


_AtmxTrafficDescrRowStatus_Type.__name__ = "Integer32"
_AtmxTrafficDescrRowStatus_Object = MibTableColumn
atmxTrafficDescrRowStatus = _AtmxTrafficDescrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 8, 1, 1, 9),
    _AtmxTrafficDescrRowStatus_Type()
)
atmxTrafficDescrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxTrafficDescrRowStatus.setStatus("mandatory")
_XylnatmVplGroup_ObjectIdentity = ObjectIdentity
xylnatmVplGroup = _XylnatmVplGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9)
)
_XylnatmVplTable_Object = MibTable
xylnatmVplTable = _XylnatmVplTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1)
)
if mibBuilder.loadTexts:
    xylnatmVplTable.setStatus("mandatory")
_XylnatmVplEntry_Object = MibTableRow
xylnatmVplEntry = _XylnatmVplEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1)
)
xylnatmVplEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "xylnatmVplSlotIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVplPortIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVplVpi"),
)
if mibBuilder.loadTexts:
    xylnatmVplEntry.setStatus("mandatory")
_XylnatmVplSlotIndex_Type = Integer32
_XylnatmVplSlotIndex_Object = MibTableColumn
xylnatmVplSlotIndex = _XylnatmVplSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 1),
    _XylnatmVplSlotIndex_Type()
)
xylnatmVplSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplSlotIndex.setStatus("mandatory")
_XylnatmVplPortIndex_Type = Integer32
_XylnatmVplPortIndex_Object = MibTableColumn
xylnatmVplPortIndex = _XylnatmVplPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 2),
    _XylnatmVplPortIndex_Type()
)
xylnatmVplPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplPortIndex.setStatus("mandatory")
_XylnatmVplVpi_Type = Integer32
_XylnatmVplVpi_Object = MibTableColumn
xylnatmVplVpi = _XylnatmVplVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 3),
    _XylnatmVplVpi_Type()
)
xylnatmVplVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplVpi.setStatus("mandatory")
_XylnatmVplConnectionDescr_Type = DisplayString
_XylnatmVplConnectionDescr_Object = MibTableColumn
xylnatmVplConnectionDescr = _XylnatmVplConnectionDescr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 4),
    _XylnatmVplConnectionDescr_Type()
)
xylnatmVplConnectionDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplConnectionDescr.setStatus("mandatory")


class _XylnatmVplChanType_Type(Integer32):
    """Custom type xylnatmVplChanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("vpNNI", 5),
          ("vpUni", 6))
    )


_XylnatmVplChanType_Type.__name__ = "Integer32"
_XylnatmVplChanType_Object = MibTableColumn
xylnatmVplChanType = _XylnatmVplChanType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 5),
    _XylnatmVplChanType_Type()
)
xylnatmVplChanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplChanType.setStatus("mandatory")


class _XylnatmVplTransportPriority_Type(Integer32):
    """Custom type xylnatmVplTransportPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("qosAbr", 7),
          ("qosCbr", 3),
          ("qosCbrPrs", 2),
          ("qosUbr", 8),
          ("qosVbrNrt", 6),
          ("qosVbrRt", 5))
    )


_XylnatmVplTransportPriority_Type.__name__ = "Integer32"
_XylnatmVplTransportPriority_Object = MibTableColumn
xylnatmVplTransportPriority = _XylnatmVplTransportPriority_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 6),
    _XylnatmVplTransportPriority_Type()
)
xylnatmVplTransportPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplTransportPriority.setStatus("mandatory")
_XylnatmVplUserPriority_Type = Integer32
_XylnatmVplUserPriority_Object = MibTableColumn
xylnatmVplUserPriority = _XylnatmVplUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 7),
    _XylnatmVplUserPriority_Type()
)
xylnatmVplUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplUserPriority.setStatus("mandatory")


class _XylnatmVplStatsMode_Type(Integer32):
    """Custom type xylnatmVplStatsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cntGcraDxCell", 1),
          ("cntGcraPsCell", 3),
          ("mrkGcraDxCell", 2),
          ("mrkGcraPsCell", 4))
    )


_XylnatmVplStatsMode_Type.__name__ = "Integer32"
_XylnatmVplStatsMode_Object = MibTableColumn
xylnatmVplStatsMode = _XylnatmVplStatsMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 8),
    _XylnatmVplStatsMode_Type()
)
xylnatmVplStatsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplStatsMode.setStatus("mandatory")
_XylnatmVplPrTrackPortBase_Type = Integer32
_XylnatmVplPrTrackPortBase_Object = MibTableColumn
xylnatmVplPrTrackPortBase = _XylnatmVplPrTrackPortBase_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 9),
    _XylnatmVplPrTrackPortBase_Type()
)
xylnatmVplPrTrackPortBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplPrTrackPortBase.setStatus("mandatory")
_XylnatmVplPrTrackPort1_Type = Integer32
_XylnatmVplPrTrackPort1_Object = MibTableColumn
xylnatmVplPrTrackPort1 = _XylnatmVplPrTrackPort1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 10),
    _XylnatmVplPrTrackPort1_Type()
)
xylnatmVplPrTrackPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplPrTrackPort1.setStatus("mandatory")
_XylnatmVplPrTrackPort2_Type = Integer32
_XylnatmVplPrTrackPort2_Object = MibTableColumn
xylnatmVplPrTrackPort2 = _XylnatmVplPrTrackPort2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 11),
    _XylnatmVplPrTrackPort2_Type()
)
xylnatmVplPrTrackPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplPrTrackPort2.setStatus("mandatory")
_XylnatmVplPrTrackPort3_Type = Integer32
_XylnatmVplPrTrackPort3_Object = MibTableColumn
xylnatmVplPrTrackPort3 = _XylnatmVplPrTrackPort3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 12),
    _XylnatmVplPrTrackPort3_Type()
)
xylnatmVplPrTrackPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplPrTrackPort3.setStatus("mandatory")
_XylnatmVplAltTrackPortBase_Type = Integer32
_XylnatmVplAltTrackPortBase_Object = MibTableColumn
xylnatmVplAltTrackPortBase = _XylnatmVplAltTrackPortBase_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 13),
    _XylnatmVplAltTrackPortBase_Type()
)
xylnatmVplAltTrackPortBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplAltTrackPortBase.setStatus("mandatory")
_XylnatmVplAltTrackPort1_Type = Integer32
_XylnatmVplAltTrackPort1_Object = MibTableColumn
xylnatmVplAltTrackPort1 = _XylnatmVplAltTrackPort1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 14),
    _XylnatmVplAltTrackPort1_Type()
)
xylnatmVplAltTrackPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplAltTrackPort1.setStatus("mandatory")
_XylnatmVplAltTrackPort2_Type = Integer32
_XylnatmVplAltTrackPort2_Object = MibTableColumn
xylnatmVplAltTrackPort2 = _XylnatmVplAltTrackPort2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 15),
    _XylnatmVplAltTrackPort2_Type()
)
xylnatmVplAltTrackPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplAltTrackPort2.setStatus("mandatory")
_XylnatmVplAltTrackPort3_Type = Integer32
_XylnatmVplAltTrackPort3_Object = MibTableColumn
xylnatmVplAltTrackPort3 = _XylnatmVplAltTrackPort3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 16),
    _XylnatmVplAltTrackPort3_Type()
)
xylnatmVplAltTrackPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplAltTrackPort3.setStatus("mandatory")


class _XylnatmVplLgclChanRedirect_Type(Integer32):
    """Custom type xylnatmVplLgclChanRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 2),
          ("notAllowed", 1))
    )


_XylnatmVplLgclChanRedirect_Type.__name__ = "Integer32"
_XylnatmVplLgclChanRedirect_Object = MibTableColumn
xylnatmVplLgclChanRedirect = _XylnatmVplLgclChanRedirect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 17),
    _XylnatmVplLgclChanRedirect_Type()
)
xylnatmVplLgclChanRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplLgclChanRedirect.setStatus("mandatory")


class _XylnatmVplAAL5Discard_Type(Integer32):
    """Custom type xylnatmVplAAL5Discard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("earlyPktDiscard", 1),
          ("partialPktDiscard", 3))
    )


_XylnatmVplAAL5Discard_Type.__name__ = "Integer32"
_XylnatmVplAAL5Discard_Object = MibTableColumn
xylnatmVplAAL5Discard = _XylnatmVplAAL5Discard_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 18),
    _XylnatmVplAAL5Discard_Type()
)
xylnatmVplAAL5Discard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplAAL5Discard.setStatus("mandatory")


class _XylnatmVplF4F5SegEndpt_Type(Integer32):
    """Custom type xylnatmVplF4F5SegEndpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVplF4F5SegEndpt_Type.__name__ = "Integer32"
_XylnatmVplF4F5SegEndpt_Object = MibTableColumn
xylnatmVplF4F5SegEndpt = _XylnatmVplF4F5SegEndpt_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 19),
    _XylnatmVplF4F5SegEndpt_Type()
)
xylnatmVplF4F5SegEndpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplF4F5SegEndpt.setStatus("mandatory")


class _XylnatmVplF4F5CopySeg_Type(Integer32):
    """Custom type xylnatmVplF4F5CopySeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVplF4F5CopySeg_Type.__name__ = "Integer32"
_XylnatmVplF4F5CopySeg_Object = MibTableColumn
xylnatmVplF4F5CopySeg = _XylnatmVplF4F5CopySeg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 20),
    _XylnatmVplF4F5CopySeg_Type()
)
xylnatmVplF4F5CopySeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplF4F5CopySeg.setStatus("mandatory")


class _XylnatmVplF4F5End2EndEndpt_Type(Integer32):
    """Custom type xylnatmVplF4F5End2EndEndpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVplF4F5End2EndEndpt_Type.__name__ = "Integer32"
_XylnatmVplF4F5End2EndEndpt_Object = MibTableColumn
xylnatmVplF4F5End2EndEndpt = _XylnatmVplF4F5End2EndEndpt_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 21),
    _XylnatmVplF4F5End2EndEndpt_Type()
)
xylnatmVplF4F5End2EndEndpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplF4F5End2EndEndpt.setStatus("mandatory")


class _XylnatmVplF4F5CopyEnd2End_Type(Integer32):
    """Custom type xylnatmVplF4F5CopyEnd2End based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVplF4F5CopyEnd2End_Type.__name__ = "Integer32"
_XylnatmVplF4F5CopyEnd2End_Object = MibTableColumn
xylnatmVplF4F5CopyEnd2End = _XylnatmVplF4F5CopyEnd2End_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 22),
    _XylnatmVplF4F5CopyEnd2End_Type()
)
xylnatmVplF4F5CopyEnd2End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplF4F5CopyEnd2End.setStatus("mandatory")


class _XylnatmVplOamEndpt_Type(Integer32):
    """Custom type xylnatmVplOamEndpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVplOamEndpt_Type.__name__ = "Integer32"
_XylnatmVplOamEndpt_Object = MibTableColumn
xylnatmVplOamEndpt = _XylnatmVplOamEndpt_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 23),
    _XylnatmVplOamEndpt_Type()
)
xylnatmVplOamEndpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplOamEndpt.setStatus("mandatory")


class _XylnatmVplOamCopy_Type(Integer32):
    """Custom type xylnatmVplOamCopy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVplOamCopy_Type.__name__ = "Integer32"
_XylnatmVplOamCopy_Object = MibTableColumn
xylnatmVplOamCopy = _XylnatmVplOamCopy_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 24),
    _XylnatmVplOamCopy_Type()
)
xylnatmVplOamCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplOamCopy.setStatus("mandatory")


class _XylnatmVplRmFwdEndpt_Type(Integer32):
    """Custom type xylnatmVplRmFwdEndpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVplRmFwdEndpt_Type.__name__ = "Integer32"
_XylnatmVplRmFwdEndpt_Object = MibTableColumn
xylnatmVplRmFwdEndpt = _XylnatmVplRmFwdEndpt_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 25),
    _XylnatmVplRmFwdEndpt_Type()
)
xylnatmVplRmFwdEndpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplRmFwdEndpt.setStatus("mandatory")


class _XylnatmVplRmFwdCopy_Type(Integer32):
    """Custom type xylnatmVplRmFwdCopy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVplRmFwdCopy_Type.__name__ = "Integer32"
_XylnatmVplRmFwdCopy_Object = MibTableColumn
xylnatmVplRmFwdCopy = _XylnatmVplRmFwdCopy_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 26),
    _XylnatmVplRmFwdCopy_Type()
)
xylnatmVplRmFwdCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplRmFwdCopy.setStatus("mandatory")


class _XylnatmVplRmFwdGcraAdv_Type(Integer32):
    """Custom type xylnatmVplRmFwdGcraAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVplRmFwdGcraAdv_Type.__name__ = "Integer32"
_XylnatmVplRmFwdGcraAdv_Object = MibTableColumn
xylnatmVplRmFwdGcraAdv = _XylnatmVplRmFwdGcraAdv_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 27),
    _XylnatmVplRmFwdGcraAdv_Type()
)
xylnatmVplRmFwdGcraAdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplRmFwdGcraAdv.setStatus("mandatory")


class _XylnatmVplRmBkwdEndpt_Type(Integer32):
    """Custom type xylnatmVplRmBkwdEndpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVplRmBkwdEndpt_Type.__name__ = "Integer32"
_XylnatmVplRmBkwdEndpt_Object = MibTableColumn
xylnatmVplRmBkwdEndpt = _XylnatmVplRmBkwdEndpt_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 28),
    _XylnatmVplRmBkwdEndpt_Type()
)
xylnatmVplRmBkwdEndpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplRmBkwdEndpt.setStatus("mandatory")


class _XylnatmVplRmBkwdCopy_Type(Integer32):
    """Custom type xylnatmVplRmBkwdCopy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVplRmBkwdCopy_Type.__name__ = "Integer32"
_XylnatmVplRmBkwdCopy_Object = MibTableColumn
xylnatmVplRmBkwdCopy = _XylnatmVplRmBkwdCopy_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 29),
    _XylnatmVplRmBkwdCopy_Type()
)
xylnatmVplRmBkwdCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplRmBkwdCopy.setStatus("mandatory")


class _XylnatmVplRmBkwdGcraAdv_Type(Integer32):
    """Custom type xylnatmVplRmBkwdGcraAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVplRmBkwdGcraAdv_Type.__name__ = "Integer32"
_XylnatmVplRmBkwdGcraAdv_Object = MibTableColumn
xylnatmVplRmBkwdGcraAdv = _XylnatmVplRmBkwdGcraAdv_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 30),
    _XylnatmVplRmBkwdGcraAdv_Type()
)
xylnatmVplRmBkwdGcraAdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplRmBkwdGcraAdv.setStatus("mandatory")


class _XylnatmVplRmDiscard_Type(Integer32):
    """Custom type xylnatmVplRmDiscard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVplRmDiscard_Type.__name__ = "Integer32"
_XylnatmVplRmDiscard_Object = MibTableColumn
xylnatmVplRmDiscard = _XylnatmVplRmDiscard_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 31),
    _XylnatmVplRmDiscard_Type()
)
xylnatmVplRmDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplRmDiscard.setStatus("mandatory")


class _XylnatmVplGcraAPoliceMode_Type(Integer32):
    """Custom type xylnatmVplGcraAPoliceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("gcraEmDxAll", 1),
          ("gcraEmMarkAllDxAll", 3),
          ("gcraEmMarkClp0DxAll", 4),
          ("gcraEmMarkClp0DxClp1", 2))
    )


_XylnatmVplGcraAPoliceMode_Type.__name__ = "Integer32"
_XylnatmVplGcraAPoliceMode_Object = MibTableColumn
xylnatmVplGcraAPoliceMode = _XylnatmVplGcraAPoliceMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 32),
    _XylnatmVplGcraAPoliceMode_Type()
)
xylnatmVplGcraAPoliceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplGcraAPoliceMode.setStatus("mandatory")


class _XylnatmVplGcraBPoliceMode_Type(Integer32):
    """Custom type xylnatmVplGcraBPoliceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("gcraEmDxAll", 1),
          ("gcraEmMarkAllDxAll", 3),
          ("gcraEmMarkClp0DxAll", 4),
          ("gcraEmMarkClp0DxClp1", 2))
    )


_XylnatmVplGcraBPoliceMode_Type.__name__ = "Integer32"
_XylnatmVplGcraBPoliceMode_Object = MibTableColumn
xylnatmVplGcraBPoliceMode = _XylnatmVplGcraBPoliceMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 33),
    _XylnatmVplGcraBPoliceMode_Type()
)
xylnatmVplGcraBPoliceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplGcraBPoliceMode.setStatus("mandatory")
_XylnatmVplMcGroupId_Type = Integer32
_XylnatmVplMcGroupId_Object = MibTableColumn
xylnatmVplMcGroupId = _XylnatmVplMcGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 34),
    _XylnatmVplMcGroupId_Type()
)
xylnatmVplMcGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplMcGroupId.setStatus("mandatory")


class _XylnatmVplMcIngressEgress_Type(Integer32):
    """Custom type xylnatmVplMcIngressEgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_XylnatmVplMcIngressEgress_Type.__name__ = "Integer32"
_XylnatmVplMcIngressEgress_Object = MibTableColumn
xylnatmVplMcIngressEgress = _XylnatmVplMcIngressEgress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 9, 1, 1, 35),
    _XylnatmVplMcIngressEgress_Type()
)
xylnatmVplMcIngressEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplMcIngressEgress.setStatus("mandatory")
_XylnatmVclGroup_ObjectIdentity = ObjectIdentity
xylnatmVclGroup = _XylnatmVclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10)
)
_XylnatmVclTable_Object = MibTable
xylnatmVclTable = _XylnatmVclTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1)
)
if mibBuilder.loadTexts:
    xylnatmVclTable.setStatus("mandatory")
_XylnatmVclEntry_Object = MibTableRow
xylnatmVclEntry = _XylnatmVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1)
)
xylnatmVclEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "xylnatmVclSlotIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVclPortIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVclVpi"),
    (0, "XYLAN-CSM-MIB", "xylnatmVclVci"),
)
if mibBuilder.loadTexts:
    xylnatmVclEntry.setStatus("mandatory")
_XylnatmVclSlotIndex_Type = Integer32
_XylnatmVclSlotIndex_Object = MibTableColumn
xylnatmVclSlotIndex = _XylnatmVclSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 1),
    _XylnatmVclSlotIndex_Type()
)
xylnatmVclSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclSlotIndex.setStatus("mandatory")
_XylnatmVclPortIndex_Type = Integer32
_XylnatmVclPortIndex_Object = MibTableColumn
xylnatmVclPortIndex = _XylnatmVclPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 2),
    _XylnatmVclPortIndex_Type()
)
xylnatmVclPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclPortIndex.setStatus("mandatory")
_XylnatmVclVpi_Type = Integer32
_XylnatmVclVpi_Object = MibTableColumn
xylnatmVclVpi = _XylnatmVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 3),
    _XylnatmVclVpi_Type()
)
xylnatmVclVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclVpi.setStatus("mandatory")
_XylnatmVclVci_Type = Integer32
_XylnatmVclVci_Object = MibTableColumn
xylnatmVclVci = _XylnatmVclVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 4),
    _XylnatmVclVci_Type()
)
xylnatmVclVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclVci.setStatus("mandatory")
_XylnatmVclConnectionDescr_Type = DisplayString
_XylnatmVclConnectionDescr_Object = MibTableColumn
xylnatmVclConnectionDescr = _XylnatmVclConnectionDescr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 5),
    _XylnatmVclConnectionDescr_Type()
)
xylnatmVclConnectionDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclConnectionDescr.setStatus("mandatory")


class _XylnatmVclChanType_Type(Integer32):
    """Custom type xylnatmVclChanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("vcNni", 3),
          ("vcUni", 4))
    )


_XylnatmVclChanType_Type.__name__ = "Integer32"
_XylnatmVclChanType_Object = MibTableColumn
xylnatmVclChanType = _XylnatmVclChanType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 6),
    _XylnatmVclChanType_Type()
)
xylnatmVclChanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclChanType.setStatus("mandatory")


class _XylnatmVclTransportPriority_Type(Integer32):
    """Custom type xylnatmVclTransportPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("qosAbr", 7),
          ("qosCbr", 3),
          ("qosCbrPrs", 2),
          ("qosUbr", 8),
          ("qosVbrNrt", 6),
          ("qosVbrRt", 5))
    )


_XylnatmVclTransportPriority_Type.__name__ = "Integer32"
_XylnatmVclTransportPriority_Object = MibTableColumn
xylnatmVclTransportPriority = _XylnatmVclTransportPriority_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 7),
    _XylnatmVclTransportPriority_Type()
)
xylnatmVclTransportPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclTransportPriority.setStatus("mandatory")
_XylnatmVclUserPriority_Type = Integer32
_XylnatmVclUserPriority_Object = MibTableColumn
xylnatmVclUserPriority = _XylnatmVclUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 8),
    _XylnatmVclUserPriority_Type()
)
xylnatmVclUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclUserPriority.setStatus("mandatory")


class _XylnatmVclStatsMode_Type(Integer32):
    """Custom type xylnatmVclStatsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cntGcraDxCell", 1),
          ("cntGcraPsCell", 3),
          ("mrkGcraDxCell", 2),
          ("mrkGcraPsCell", 4))
    )


_XylnatmVclStatsMode_Type.__name__ = "Integer32"
_XylnatmVclStatsMode_Object = MibTableColumn
xylnatmVclStatsMode = _XylnatmVclStatsMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 9),
    _XylnatmVclStatsMode_Type()
)
xylnatmVclStatsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclStatsMode.setStatus("mandatory")
_XylnatmVclPrTrackPortBase_Type = Integer32
_XylnatmVclPrTrackPortBase_Object = MibTableColumn
xylnatmVclPrTrackPortBase = _XylnatmVclPrTrackPortBase_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 10),
    _XylnatmVclPrTrackPortBase_Type()
)
xylnatmVclPrTrackPortBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclPrTrackPortBase.setStatus("mandatory")
_XylnatmVclPrTrackPort1_Type = Integer32
_XylnatmVclPrTrackPort1_Object = MibTableColumn
xylnatmVclPrTrackPort1 = _XylnatmVclPrTrackPort1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 11),
    _XylnatmVclPrTrackPort1_Type()
)
xylnatmVclPrTrackPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclPrTrackPort1.setStatus("mandatory")
_XylnatmVclPrTrackPort2_Type = Integer32
_XylnatmVclPrTrackPort2_Object = MibTableColumn
xylnatmVclPrTrackPort2 = _XylnatmVclPrTrackPort2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 12),
    _XylnatmVclPrTrackPort2_Type()
)
xylnatmVclPrTrackPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclPrTrackPort2.setStatus("mandatory")
_XylnatmVclPrTrackPort3_Type = Integer32
_XylnatmVclPrTrackPort3_Object = MibTableColumn
xylnatmVclPrTrackPort3 = _XylnatmVclPrTrackPort3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 13),
    _XylnatmVclPrTrackPort3_Type()
)
xylnatmVclPrTrackPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclPrTrackPort3.setStatus("mandatory")
_XylnatmVclAltTrackPortBase_Type = Integer32
_XylnatmVclAltTrackPortBase_Object = MibTableColumn
xylnatmVclAltTrackPortBase = _XylnatmVclAltTrackPortBase_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 14),
    _XylnatmVclAltTrackPortBase_Type()
)
xylnatmVclAltTrackPortBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclAltTrackPortBase.setStatus("mandatory")
_XylnatmVclAltTrackPort1_Type = Integer32
_XylnatmVclAltTrackPort1_Object = MibTableColumn
xylnatmVclAltTrackPort1 = _XylnatmVclAltTrackPort1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 15),
    _XylnatmVclAltTrackPort1_Type()
)
xylnatmVclAltTrackPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclAltTrackPort1.setStatus("mandatory")
_XylnatmVclAltTrackPort2_Type = Integer32
_XylnatmVclAltTrackPort2_Object = MibTableColumn
xylnatmVclAltTrackPort2 = _XylnatmVclAltTrackPort2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 16),
    _XylnatmVclAltTrackPort2_Type()
)
xylnatmVclAltTrackPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclAltTrackPort2.setStatus("mandatory")
_XylnatmVclAltTrackPort3_Type = Integer32
_XylnatmVclAltTrackPort3_Object = MibTableColumn
xylnatmVclAltTrackPort3 = _XylnatmVclAltTrackPort3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 17),
    _XylnatmVclAltTrackPort3_Type()
)
xylnatmVclAltTrackPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclAltTrackPort3.setStatus("mandatory")


class _XylnatmVclLgclChanRedirect_Type(Integer32):
    """Custom type xylnatmVclLgclChanRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 2),
          ("notAllowed", 1))
    )


_XylnatmVclLgclChanRedirect_Type.__name__ = "Integer32"
_XylnatmVclLgclChanRedirect_Object = MibTableColumn
xylnatmVclLgclChanRedirect = _XylnatmVclLgclChanRedirect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 18),
    _XylnatmVclLgclChanRedirect_Type()
)
xylnatmVclLgclChanRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclLgclChanRedirect.setStatus("mandatory")


class _XylnatmVclAAL5Discard_Type(Integer32):
    """Custom type xylnatmVclAAL5Discard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("earlyPktDiscard", 1),
          ("partialPktDiscard", 3))
    )


_XylnatmVclAAL5Discard_Type.__name__ = "Integer32"
_XylnatmVclAAL5Discard_Object = MibTableColumn
xylnatmVclAAL5Discard = _XylnatmVclAAL5Discard_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 19),
    _XylnatmVclAAL5Discard_Type()
)
xylnatmVclAAL5Discard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclAAL5Discard.setStatus("mandatory")


class _XylnatmVclF4F5SegEndpt_Type(Integer32):
    """Custom type xylnatmVclF4F5SegEndpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVclF4F5SegEndpt_Type.__name__ = "Integer32"
_XylnatmVclF4F5SegEndpt_Object = MibTableColumn
xylnatmVclF4F5SegEndpt = _XylnatmVclF4F5SegEndpt_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 20),
    _XylnatmVclF4F5SegEndpt_Type()
)
xylnatmVclF4F5SegEndpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclF4F5SegEndpt.setStatus("mandatory")


class _XylnatmVclF4F5CopySeg_Type(Integer32):
    """Custom type xylnatmVclF4F5CopySeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVclF4F5CopySeg_Type.__name__ = "Integer32"
_XylnatmVclF4F5CopySeg_Object = MibTableColumn
xylnatmVclF4F5CopySeg = _XylnatmVclF4F5CopySeg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 21),
    _XylnatmVclF4F5CopySeg_Type()
)
xylnatmVclF4F5CopySeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclF4F5CopySeg.setStatus("mandatory")


class _XylnatmVclF4F5End2EndEndpt_Type(Integer32):
    """Custom type xylnatmVclF4F5End2EndEndpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVclF4F5End2EndEndpt_Type.__name__ = "Integer32"
_XylnatmVclF4F5End2EndEndpt_Object = MibTableColumn
xylnatmVclF4F5End2EndEndpt = _XylnatmVclF4F5End2EndEndpt_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 22),
    _XylnatmVclF4F5End2EndEndpt_Type()
)
xylnatmVclF4F5End2EndEndpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclF4F5End2EndEndpt.setStatus("mandatory")


class _XylnatmVclF4F5CopyEnd2End_Type(Integer32):
    """Custom type xylnatmVclF4F5CopyEnd2End based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVclF4F5CopyEnd2End_Type.__name__ = "Integer32"
_XylnatmVclF4F5CopyEnd2End_Object = MibTableColumn
xylnatmVclF4F5CopyEnd2End = _XylnatmVclF4F5CopyEnd2End_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 23),
    _XylnatmVclF4F5CopyEnd2End_Type()
)
xylnatmVclF4F5CopyEnd2End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclF4F5CopyEnd2End.setStatus("mandatory")


class _XylnatmVclOamEndpt_Type(Integer32):
    """Custom type xylnatmVclOamEndpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVclOamEndpt_Type.__name__ = "Integer32"
_XylnatmVclOamEndpt_Object = MibTableColumn
xylnatmVclOamEndpt = _XylnatmVclOamEndpt_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 24),
    _XylnatmVclOamEndpt_Type()
)
xylnatmVclOamEndpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclOamEndpt.setStatus("mandatory")


class _XylnatmVclOamCopy_Type(Integer32):
    """Custom type xylnatmVclOamCopy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVclOamCopy_Type.__name__ = "Integer32"
_XylnatmVclOamCopy_Object = MibTableColumn
xylnatmVclOamCopy = _XylnatmVclOamCopy_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 25),
    _XylnatmVclOamCopy_Type()
)
xylnatmVclOamCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclOamCopy.setStatus("mandatory")


class _XylnatmVclRmFwdEndpt_Type(Integer32):
    """Custom type xylnatmVclRmFwdEndpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVclRmFwdEndpt_Type.__name__ = "Integer32"
_XylnatmVclRmFwdEndpt_Object = MibTableColumn
xylnatmVclRmFwdEndpt = _XylnatmVclRmFwdEndpt_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 26),
    _XylnatmVclRmFwdEndpt_Type()
)
xylnatmVclRmFwdEndpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclRmFwdEndpt.setStatus("mandatory")


class _XylnatmVclRmFwdCopy_Type(Integer32):
    """Custom type xylnatmVclRmFwdCopy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVclRmFwdCopy_Type.__name__ = "Integer32"
_XylnatmVclRmFwdCopy_Object = MibTableColumn
xylnatmVclRmFwdCopy = _XylnatmVclRmFwdCopy_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 27),
    _XylnatmVclRmFwdCopy_Type()
)
xylnatmVclRmFwdCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclRmFwdCopy.setStatus("mandatory")


class _XylnatmVclRmFwdGcraAdv_Type(Integer32):
    """Custom type xylnatmVclRmFwdGcraAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVclRmFwdGcraAdv_Type.__name__ = "Integer32"
_XylnatmVclRmFwdGcraAdv_Object = MibTableColumn
xylnatmVclRmFwdGcraAdv = _XylnatmVclRmFwdGcraAdv_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 28),
    _XylnatmVclRmFwdGcraAdv_Type()
)
xylnatmVclRmFwdGcraAdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclRmFwdGcraAdv.setStatus("mandatory")


class _XylnatmVclRmBkwdEndpt_Type(Integer32):
    """Custom type xylnatmVclRmBkwdEndpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVclRmBkwdEndpt_Type.__name__ = "Integer32"
_XylnatmVclRmBkwdEndpt_Object = MibTableColumn
xylnatmVclRmBkwdEndpt = _XylnatmVclRmBkwdEndpt_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 29),
    _XylnatmVclRmBkwdEndpt_Type()
)
xylnatmVclRmBkwdEndpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclRmBkwdEndpt.setStatus("mandatory")


class _XylnatmVclRmBkwdCopy_Type(Integer32):
    """Custom type xylnatmVclRmBkwdCopy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVclRmBkwdCopy_Type.__name__ = "Integer32"
_XylnatmVclRmBkwdCopy_Object = MibTableColumn
xylnatmVclRmBkwdCopy = _XylnatmVclRmBkwdCopy_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 30),
    _XylnatmVclRmBkwdCopy_Type()
)
xylnatmVclRmBkwdCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclRmBkwdCopy.setStatus("mandatory")


class _XylnatmVclRmBkwdGcraAdv_Type(Integer32):
    """Custom type xylnatmVclRmBkwdGcraAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVclRmBkwdGcraAdv_Type.__name__ = "Integer32"
_XylnatmVclRmBkwdGcraAdv_Object = MibTableColumn
xylnatmVclRmBkwdGcraAdv = _XylnatmVclRmBkwdGcraAdv_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 31),
    _XylnatmVclRmBkwdGcraAdv_Type()
)
xylnatmVclRmBkwdGcraAdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclRmBkwdGcraAdv.setStatus("mandatory")


class _XylnatmVclRmDiscard_Type(Integer32):
    """Custom type xylnatmVclRmDiscard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVclRmDiscard_Type.__name__ = "Integer32"
_XylnatmVclRmDiscard_Object = MibTableColumn
xylnatmVclRmDiscard = _XylnatmVclRmDiscard_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 32),
    _XylnatmVclRmDiscard_Type()
)
xylnatmVclRmDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclRmDiscard.setStatus("mandatory")


class _XylnatmVclGcraAPoliceMode_Type(Integer32):
    """Custom type xylnatmVclGcraAPoliceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("gcraEmDxAll", 1),
          ("gcraEmMarkAllDxAll", 3),
          ("gcraEmMarkClp0DxAll", 4),
          ("gcraEmMarkClp0DxClp1", 2))
    )


_XylnatmVclGcraAPoliceMode_Type.__name__ = "Integer32"
_XylnatmVclGcraAPoliceMode_Object = MibTableColumn
xylnatmVclGcraAPoliceMode = _XylnatmVclGcraAPoliceMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 33),
    _XylnatmVclGcraAPoliceMode_Type()
)
xylnatmVclGcraAPoliceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclGcraAPoliceMode.setStatus("mandatory")


class _XylnatmVclGcraBPoliceMode_Type(Integer32):
    """Custom type xylnatmVclGcraBPoliceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("gcraEmDxAll", 1),
          ("gcraEmMarkAllDxAll", 3),
          ("gcraEmMarkClp0DxAll", 4),
          ("gcraEmMarkClp0DxClp1", 2))
    )


_XylnatmVclGcraBPoliceMode_Type.__name__ = "Integer32"
_XylnatmVclGcraBPoliceMode_Object = MibTableColumn
xylnatmVclGcraBPoliceMode = _XylnatmVclGcraBPoliceMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 34),
    _XylnatmVclGcraBPoliceMode_Type()
)
xylnatmVclGcraBPoliceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclGcraBPoliceMode.setStatus("mandatory")
_XylnatmVclMcGroupId_Type = Integer32
_XylnatmVclMcGroupId_Object = MibTableColumn
xylnatmVclMcGroupId = _XylnatmVclMcGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 35),
    _XylnatmVclMcGroupId_Type()
)
xylnatmVclMcGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclMcGroupId.setStatus("mandatory")


class _XylnatmVclMcIngressEgress_Type(Integer32):
    """Custom type xylnatmVclMcIngressEgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_XylnatmVclMcIngressEgress_Type.__name__ = "Integer32"
_XylnatmVclMcIngressEgress_Object = MibTableColumn
xylnatmVclMcIngressEgress = _XylnatmVclMcIngressEgress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 10, 1, 1, 36),
    _XylnatmVclMcIngressEgress_Type()
)
xylnatmVclMcIngressEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclMcIngressEgress.setStatus("mandatory")
_XylnatmVplStatGroup_ObjectIdentity = ObjectIdentity
xylnatmVplStatGroup = _XylnatmVplStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 11)
)
_XylnatmVplStatTable_Object = MibTable
xylnatmVplStatTable = _XylnatmVplStatTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 11, 1)
)
if mibBuilder.loadTexts:
    xylnatmVplStatTable.setStatus("mandatory")
_XylnatmVplStatEntry_Object = MibTableRow
xylnatmVplStatEntry = _XylnatmVplStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 11, 1, 1)
)
xylnatmVplStatEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "xylnatmVplStatSlotIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVplStatPortIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVplStatVpi"),
)
if mibBuilder.loadTexts:
    xylnatmVplStatEntry.setStatus("mandatory")
_XylnatmVplStatSlotIndex_Type = Integer32
_XylnatmVplStatSlotIndex_Object = MibTableColumn
xylnatmVplStatSlotIndex = _XylnatmVplStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 11, 1, 1, 1),
    _XylnatmVplStatSlotIndex_Type()
)
xylnatmVplStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplStatSlotIndex.setStatus("mandatory")


class _XylnatmVplStatPortIndex_Type(Integer32):
    """Custom type xylnatmVplStatPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_XylnatmVplStatPortIndex_Type.__name__ = "Integer32"
_XylnatmVplStatPortIndex_Object = MibTableColumn
xylnatmVplStatPortIndex = _XylnatmVplStatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 11, 1, 1, 2),
    _XylnatmVplStatPortIndex_Type()
)
xylnatmVplStatPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplStatPortIndex.setStatus("mandatory")
_XylnatmVplStatVpi_Type = Integer32
_XylnatmVplStatVpi_Object = MibTableColumn
xylnatmVplStatVpi = _XylnatmVplStatVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 11, 1, 1, 3),
    _XylnatmVplStatVpi_Type()
)
xylnatmVplStatVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplStatVpi.setStatus("mandatory")
_XylnatmVplStatRxCells_Type = Counter32
_XylnatmVplStatRxCells_Object = MibTableColumn
xylnatmVplStatRxCells = _XylnatmVplStatRxCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 11, 1, 1, 4),
    _XylnatmVplStatRxCells_Type()
)
xylnatmVplStatRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplStatRxCells.setStatus("mandatory")
_XylnatmVplStatTxCells_Type = Counter32
_XylnatmVplStatTxCells_Object = MibTableColumn
xylnatmVplStatTxCells = _XylnatmVplStatTxCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 11, 1, 1, 5),
    _XylnatmVplStatTxCells_Type()
)
xylnatmVplStatTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplStatTxCells.setStatus("mandatory")
_XylnatmVplStatRxClp0Cells_Type = Counter32
_XylnatmVplStatRxClp0Cells_Object = MibTableColumn
xylnatmVplStatRxClp0Cells = _XylnatmVplStatRxClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 11, 1, 1, 6),
    _XylnatmVplStatRxClp0Cells_Type()
)
xylnatmVplStatRxClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplStatRxClp0Cells.setStatus("mandatory")
_XylnatmVplStatRxClp1Cells_Type = Counter32
_XylnatmVplStatRxClp1Cells_Object = MibTableColumn
xylnatmVplStatRxClp1Cells = _XylnatmVplStatRxClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 11, 1, 1, 7),
    _XylnatmVplStatRxClp1Cells_Type()
)
xylnatmVplStatRxClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplStatRxClp1Cells.setStatus("mandatory")
_XylnatmVplStatDxCongClp0Cells_Type = Counter32
_XylnatmVplStatDxCongClp0Cells_Object = MibTableColumn
xylnatmVplStatDxCongClp0Cells = _XylnatmVplStatDxCongClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 11, 1, 1, 8),
    _XylnatmVplStatDxCongClp0Cells_Type()
)
xylnatmVplStatDxCongClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplStatDxCongClp0Cells.setStatus("mandatory")
_XylnatmVplStatDxCongClp1Cells_Type = Counter32
_XylnatmVplStatDxCongClp1Cells_Object = MibTableColumn
xylnatmVplStatDxCongClp1Cells = _XylnatmVplStatDxCongClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 11, 1, 1, 9),
    _XylnatmVplStatDxCongClp1Cells_Type()
)
xylnatmVplStatDxCongClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplStatDxCongClp1Cells.setStatus("mandatory")
_XylnatmVplStatDxGcraClp0Cells_Type = Counter32
_XylnatmVplStatDxGcraClp0Cells_Object = MibTableColumn
xylnatmVplStatDxGcraClp0Cells = _XylnatmVplStatDxGcraClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 11, 1, 1, 10),
    _XylnatmVplStatDxGcraClp0Cells_Type()
)
xylnatmVplStatDxGcraClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplStatDxGcraClp0Cells.setStatus("mandatory")
_XylnatmVplStatDxGcraClp1Cells_Type = Counter32
_XylnatmVplStatDxGcraClp1Cells_Object = MibTableColumn
xylnatmVplStatDxGcraClp1Cells = _XylnatmVplStatDxGcraClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 11, 1, 1, 11),
    _XylnatmVplStatDxGcraClp1Cells_Type()
)
xylnatmVplStatDxGcraClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplStatDxGcraClp1Cells.setStatus("mandatory")
_XylnatmVplStatDxGcraBClp0Cells_Type = Counter32
_XylnatmVplStatDxGcraBClp0Cells_Object = MibTableColumn
xylnatmVplStatDxGcraBClp0Cells = _XylnatmVplStatDxGcraBClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 11, 1, 1, 12),
    _XylnatmVplStatDxGcraBClp0Cells_Type()
)
xylnatmVplStatDxGcraBClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplStatDxGcraBClp0Cells.setStatus("mandatory")
_XylnatmVplStatDxGcraBClp1Cells_Type = Counter32
_XylnatmVplStatDxGcraBClp1Cells_Object = MibTableColumn
xylnatmVplStatDxGcraBClp1Cells = _XylnatmVplStatDxGcraBClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 11, 1, 1, 13),
    _XylnatmVplStatDxGcraBClp1Cells_Type()
)
xylnatmVplStatDxGcraBClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplStatDxGcraBClp1Cells.setStatus("mandatory")
_XylnatmVclStatGroup_ObjectIdentity = ObjectIdentity
xylnatmVclStatGroup = _XylnatmVclStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 12)
)
_XylnatmVclStatTable_Object = MibTable
xylnatmVclStatTable = _XylnatmVclStatTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 12, 1)
)
if mibBuilder.loadTexts:
    xylnatmVclStatTable.setStatus("mandatory")
_XylnatmVclStatEntry_Object = MibTableRow
xylnatmVclStatEntry = _XylnatmVclStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 12, 1, 1)
)
xylnatmVclStatEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "xylnatmVclStatSlotIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVclStatPortIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVclStatVpi"),
    (0, "XYLAN-CSM-MIB", "xylnatmVclStatVci"),
)
if mibBuilder.loadTexts:
    xylnatmVclStatEntry.setStatus("mandatory")
_XylnatmVclStatSlotIndex_Type = Integer32
_XylnatmVclStatSlotIndex_Object = MibTableColumn
xylnatmVclStatSlotIndex = _XylnatmVclStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 12, 1, 1, 1),
    _XylnatmVclStatSlotIndex_Type()
)
xylnatmVclStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclStatSlotIndex.setStatus("mandatory")


class _XylnatmVclStatPortIndex_Type(Integer32):
    """Custom type xylnatmVclStatPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_XylnatmVclStatPortIndex_Type.__name__ = "Integer32"
_XylnatmVclStatPortIndex_Object = MibTableColumn
xylnatmVclStatPortIndex = _XylnatmVclStatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 12, 1, 1, 2),
    _XylnatmVclStatPortIndex_Type()
)
xylnatmVclStatPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclStatPortIndex.setStatus("mandatory")
_XylnatmVclStatVpi_Type = Integer32
_XylnatmVclStatVpi_Object = MibTableColumn
xylnatmVclStatVpi = _XylnatmVclStatVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 12, 1, 1, 3),
    _XylnatmVclStatVpi_Type()
)
xylnatmVclStatVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclStatVpi.setStatus("mandatory")
_XylnatmVclStatVci_Type = Integer32
_XylnatmVclStatVci_Object = MibTableColumn
xylnatmVclStatVci = _XylnatmVclStatVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 12, 1, 1, 4),
    _XylnatmVclStatVci_Type()
)
xylnatmVclStatVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclStatVci.setStatus("mandatory")
_XylnatmVclStatRxCells_Type = Counter32
_XylnatmVclStatRxCells_Object = MibTableColumn
xylnatmVclStatRxCells = _XylnatmVclStatRxCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 12, 1, 1, 5),
    _XylnatmVclStatRxCells_Type()
)
xylnatmVclStatRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclStatRxCells.setStatus("mandatory")
_XylnatmVclStatTxCells_Type = Counter32
_XylnatmVclStatTxCells_Object = MibTableColumn
xylnatmVclStatTxCells = _XylnatmVclStatTxCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 12, 1, 1, 6),
    _XylnatmVclStatTxCells_Type()
)
xylnatmVclStatTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclStatTxCells.setStatus("mandatory")
_XylnatmVclStatRxClp0Cells_Type = Counter32
_XylnatmVclStatRxClp0Cells_Object = MibTableColumn
xylnatmVclStatRxClp0Cells = _XylnatmVclStatRxClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 12, 1, 1, 7),
    _XylnatmVclStatRxClp0Cells_Type()
)
xylnatmVclStatRxClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclStatRxClp0Cells.setStatus("mandatory")
_XylnatmVclStatRxClp1Cells_Type = Counter32
_XylnatmVclStatRxClp1Cells_Object = MibTableColumn
xylnatmVclStatRxClp1Cells = _XylnatmVclStatRxClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 12, 1, 1, 8),
    _XylnatmVclStatRxClp1Cells_Type()
)
xylnatmVclStatRxClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclStatRxClp1Cells.setStatus("mandatory")
_XylnatmVclStatDxCongClp0Cells_Type = Counter32
_XylnatmVclStatDxCongClp0Cells_Object = MibTableColumn
xylnatmVclStatDxCongClp0Cells = _XylnatmVclStatDxCongClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 12, 1, 1, 9),
    _XylnatmVclStatDxCongClp0Cells_Type()
)
xylnatmVclStatDxCongClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclStatDxCongClp0Cells.setStatus("mandatory")
_XylnatmVclStatDxCongClp1Cells_Type = Counter32
_XylnatmVclStatDxCongClp1Cells_Object = MibTableColumn
xylnatmVclStatDxCongClp1Cells = _XylnatmVclStatDxCongClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 12, 1, 1, 10),
    _XylnatmVclStatDxCongClp1Cells_Type()
)
xylnatmVclStatDxCongClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclStatDxCongClp1Cells.setStatus("mandatory")
_XylnatmVclStatDxGcraClp0Cells_Type = Counter32
_XylnatmVclStatDxGcraClp0Cells_Object = MibTableColumn
xylnatmVclStatDxGcraClp0Cells = _XylnatmVclStatDxGcraClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 12, 1, 1, 11),
    _XylnatmVclStatDxGcraClp0Cells_Type()
)
xylnatmVclStatDxGcraClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclStatDxGcraClp0Cells.setStatus("mandatory")
_XylnatmVclStatDxGcraClp1Cells_Type = Counter32
_XylnatmVclStatDxGcraClp1Cells_Object = MibTableColumn
xylnatmVclStatDxGcraClp1Cells = _XylnatmVclStatDxGcraClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 12, 1, 1, 12),
    _XylnatmVclStatDxGcraClp1Cells_Type()
)
xylnatmVclStatDxGcraClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclStatDxGcraClp1Cells.setStatus("mandatory")
_XylnatmVclStatDxGcraBClp0Cells_Type = Counter32
_XylnatmVclStatDxGcraBClp0Cells_Object = MibTableColumn
xylnatmVclStatDxGcraBClp0Cells = _XylnatmVclStatDxGcraBClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 12, 1, 1, 13),
    _XylnatmVclStatDxGcraBClp0Cells_Type()
)
xylnatmVclStatDxGcraBClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclStatDxGcraBClp0Cells.setStatus("mandatory")
_XylnatmVclStatDxGcraBClp1Cells_Type = Counter32
_XylnatmVclStatDxGcraBClp1Cells_Object = MibTableColumn
xylnatmVclStatDxGcraBClp1Cells = _XylnatmVclStatDxGcraBClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 12, 1, 1, 14),
    _XylnatmVclStatDxGcraBClp1Cells_Type()
)
xylnatmVclStatDxGcraBClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclStatDxGcraBClp1Cells.setStatus("mandatory")
_XylnatmVcCrossConnectGroup_ObjectIdentity = ObjectIdentity
xylnatmVcCrossConnectGroup = _XylnatmVcCrossConnectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13)
)
_XylnatmVcCrossConnectTable_Object = MibTable
xylnatmVcCrossConnectTable = _XylnatmVcCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1)
)
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectTable.setStatus("mandatory")
_XylnatmVcCrossConnectEntry_Object = MibTableRow
xylnatmVcCrossConnectEntry = _XylnatmVcCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1)
)
xylnatmVcCrossConnectEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "xylnatmVcCrossConnectLowSlotIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVcCrossConnectLowPortIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVcCrossConnectLowVpi"),
    (0, "XYLAN-CSM-MIB", "xylnatmVcCrossConnectLowVci"),
    (0, "XYLAN-CSM-MIB", "xylnatmVcCrossConnectHighSlotIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVcCrossConnectHighPortIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVcCrossConnectHighVpi"),
    (0, "XYLAN-CSM-MIB", "xylnatmVcCrossConnectHighVci"),
)
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectEntry.setStatus("mandatory")
_XylnatmVcCrossConnectLowSlotIndex_Type = Integer32
_XylnatmVcCrossConnectLowSlotIndex_Object = MibTableColumn
xylnatmVcCrossConnectLowSlotIndex = _XylnatmVcCrossConnectLowSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 1),
    _XylnatmVcCrossConnectLowSlotIndex_Type()
)
xylnatmVcCrossConnectLowSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectLowSlotIndex.setStatus("mandatory")
_XylnatmVcCrossConnectLowPortIndex_Type = Integer32
_XylnatmVcCrossConnectLowPortIndex_Object = MibTableColumn
xylnatmVcCrossConnectLowPortIndex = _XylnatmVcCrossConnectLowPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 2),
    _XylnatmVcCrossConnectLowPortIndex_Type()
)
xylnatmVcCrossConnectLowPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectLowPortIndex.setStatus("mandatory")


class _XylnatmVcCrossConnectLowVpi_Type(Integer32):
    """Custom type xylnatmVcCrossConnectLowVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_XylnatmVcCrossConnectLowVpi_Type.__name__ = "Integer32"
_XylnatmVcCrossConnectLowVpi_Object = MibTableColumn
xylnatmVcCrossConnectLowVpi = _XylnatmVcCrossConnectLowVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 3),
    _XylnatmVcCrossConnectLowVpi_Type()
)
xylnatmVcCrossConnectLowVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectLowVpi.setStatus("mandatory")


class _XylnatmVcCrossConnectLowVci_Type(Integer32):
    """Custom type xylnatmVcCrossConnectLowVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XylnatmVcCrossConnectLowVci_Type.__name__ = "Integer32"
_XylnatmVcCrossConnectLowVci_Object = MibTableColumn
xylnatmVcCrossConnectLowVci = _XylnatmVcCrossConnectLowVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 4),
    _XylnatmVcCrossConnectLowVci_Type()
)
xylnatmVcCrossConnectLowVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectLowVci.setStatus("mandatory")


class _XylnatmVcCrossConnectHighSlotIndex_Type(Integer32):
    """Custom type xylnatmVcCrossConnectHighSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_XylnatmVcCrossConnectHighSlotIndex_Type.__name__ = "Integer32"
_XylnatmVcCrossConnectHighSlotIndex_Object = MibTableColumn
xylnatmVcCrossConnectHighSlotIndex = _XylnatmVcCrossConnectHighSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 5),
    _XylnatmVcCrossConnectHighSlotIndex_Type()
)
xylnatmVcCrossConnectHighSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectHighSlotIndex.setStatus("mandatory")
_XylnatmVcCrossConnectHighPortIndex_Type = Integer32
_XylnatmVcCrossConnectHighPortIndex_Object = MibTableColumn
xylnatmVcCrossConnectHighPortIndex = _XylnatmVcCrossConnectHighPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 6),
    _XylnatmVcCrossConnectHighPortIndex_Type()
)
xylnatmVcCrossConnectHighPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectHighPortIndex.setStatus("mandatory")


class _XylnatmVcCrossConnectHighVpi_Type(Integer32):
    """Custom type xylnatmVcCrossConnectHighVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_XylnatmVcCrossConnectHighVpi_Type.__name__ = "Integer32"
_XylnatmVcCrossConnectHighVpi_Object = MibTableColumn
xylnatmVcCrossConnectHighVpi = _XylnatmVcCrossConnectHighVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 7),
    _XylnatmVcCrossConnectHighVpi_Type()
)
xylnatmVcCrossConnectHighVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectHighVpi.setStatus("mandatory")


class _XylnatmVcCrossConnectHighVci_Type(Integer32):
    """Custom type xylnatmVcCrossConnectHighVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XylnatmVcCrossConnectHighVci_Type.__name__ = "Integer32"
_XylnatmVcCrossConnectHighVci_Object = MibTableColumn
xylnatmVcCrossConnectHighVci = _XylnatmVcCrossConnectHighVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 8),
    _XylnatmVcCrossConnectHighVci_Type()
)
xylnatmVcCrossConnectHighVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectHighVci.setStatus("mandatory")


class _XylnatmVcCrossConnectConnectionId_Type(Integer32):
    """Custom type xylnatmVcCrossConnectConnectionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("multicastChild", 2),
          ("multicastParent", 1),
          ("nonMulticastParent", 3),
          ("unknown", 4))
    )


_XylnatmVcCrossConnectConnectionId_Type.__name__ = "Integer32"
_XylnatmVcCrossConnectConnectionId_Object = MibTableColumn
xylnatmVcCrossConnectConnectionId = _XylnatmVcCrossConnectConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 9),
    _XylnatmVcCrossConnectConnectionId_Type()
)
xylnatmVcCrossConnectConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectConnectionId.setStatus("mandatory")
_XylnatmVcCrossConnectLowRxTrafficDescrIndex_Type = Integer32
_XylnatmVcCrossConnectLowRxTrafficDescrIndex_Object = MibTableColumn
xylnatmVcCrossConnectLowRxTrafficDescrIndex = _XylnatmVcCrossConnectLowRxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 10),
    _XylnatmVcCrossConnectLowRxTrafficDescrIndex_Type()
)
xylnatmVcCrossConnectLowRxTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectLowRxTrafficDescrIndex.setStatus("mandatory")
_XylnatmVcCrossConnectLowTxTrafficDescrIndex_Type = Integer32
_XylnatmVcCrossConnectLowTxTrafficDescrIndex_Object = MibTableColumn
xylnatmVcCrossConnectLowTxTrafficDescrIndex = _XylnatmVcCrossConnectLowTxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 11),
    _XylnatmVcCrossConnectLowTxTrafficDescrIndex_Type()
)
xylnatmVcCrossConnectLowTxTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectLowTxTrafficDescrIndex.setStatus("mandatory")


class _XylnatmVcCrossConnectMCastEnable_Type(Integer32):
    """Custom type xylnatmVcCrossConnectMCastEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_XylnatmVcCrossConnectMCastEnable_Type.__name__ = "Integer32"
_XylnatmVcCrossConnectMCastEnable_Object = MibTableColumn
xylnatmVcCrossConnectMCastEnable = _XylnatmVcCrossConnectMCastEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 12),
    _XylnatmVcCrossConnectMCastEnable_Type()
)
xylnatmVcCrossConnectMCastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectMCastEnable.setStatus("mandatory")
_XylnatmVcCrossConnectL2HLastChange_Type = DisplayString
_XylnatmVcCrossConnectL2HLastChange_Object = MibTableColumn
xylnatmVcCrossConnectL2HLastChange = _XylnatmVcCrossConnectL2HLastChange_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 13),
    _XylnatmVcCrossConnectL2HLastChange_Type()
)
xylnatmVcCrossConnectL2HLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectL2HLastChange.setStatus("mandatory")
_XylnatmVcCrossConnectH2LLastChange_Type = DisplayString
_XylnatmVcCrossConnectH2LLastChange_Object = MibTableColumn
xylnatmVcCrossConnectH2LLastChange = _XylnatmVcCrossConnectH2LLastChange_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 14),
    _XylnatmVcCrossConnectH2LLastChange_Type()
)
xylnatmVcCrossConnectH2LLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectH2LLastChange.setStatus("mandatory")


class _XylnatmVcCrossConnectL2HOperStatus_Type(Integer32):
    """Custom type xylnatmVcCrossConnectL2HOperStatus based on Integer32"""
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
        *(("end2endDown", 3),
          ("end2endup", 2),
          ("localDown", 5),
          ("localUpEndToEndUnknown", 4),
          ("unknown", 1))
    )


_XylnatmVcCrossConnectL2HOperStatus_Type.__name__ = "Integer32"
_XylnatmVcCrossConnectL2HOperStatus_Object = MibTableColumn
xylnatmVcCrossConnectL2HOperStatus = _XylnatmVcCrossConnectL2HOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 15),
    _XylnatmVcCrossConnectL2HOperStatus_Type()
)
xylnatmVcCrossConnectL2HOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectL2HOperStatus.setStatus("mandatory")


class _XylnatmVcCrossConnectH2LOperStatus_Type(Integer32):
    """Custom type xylnatmVcCrossConnectH2LOperStatus based on Integer32"""
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
        *(("end2endDown", 3),
          ("end2endup", 2),
          ("localDown", 5),
          ("localUpEndToEndUnknown", 4),
          ("unknown", 1))
    )


_XylnatmVcCrossConnectH2LOperStatus_Type.__name__ = "Integer32"
_XylnatmVcCrossConnectH2LOperStatus_Object = MibTableColumn
xylnatmVcCrossConnectH2LOperStatus = _XylnatmVcCrossConnectH2LOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 16),
    _XylnatmVcCrossConnectH2LOperStatus_Type()
)
xylnatmVcCrossConnectH2LOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectH2LOperStatus.setStatus("mandatory")


class _XylnatmVcCrossConnectVcType_Type(Integer32):
    """Custom type xylnatmVcCrossConnectVcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("control", 4),
          ("pvc", 1),
          ("softPvc", 3),
          ("svc", 2))
    )


_XylnatmVcCrossConnectVcType_Type.__name__ = "Integer32"
_XylnatmVcCrossConnectVcType_Object = MibTableColumn
xylnatmVcCrossConnectVcType = _XylnatmVcCrossConnectVcType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 17),
    _XylnatmVcCrossConnectVcType_Type()
)
xylnatmVcCrossConnectVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectVcType.setStatus("mandatory")
_XylnatmVcCrossConnectPvcIdentifier_Type = Integer32
_XylnatmVcCrossConnectPvcIdentifier_Object = MibTableColumn
xylnatmVcCrossConnectPvcIdentifier = _XylnatmVcCrossConnectPvcIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 18),
    _XylnatmVcCrossConnectPvcIdentifier_Type()
)
xylnatmVcCrossConnectPvcIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectPvcIdentifier.setStatus("mandatory")


class _XylnatmVcCrossConnectRowStatus_Type(Integer32):
    """Custom type xylnatmVcCrossConnectRowStatus based on Integer32"""
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
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("notActive", 5))
    )


_XylnatmVcCrossConnectRowStatus_Type.__name__ = "Integer32"
_XylnatmVcCrossConnectRowStatus_Object = MibTableColumn
xylnatmVcCrossConnectRowStatus = _XylnatmVcCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 13, 1, 1, 19),
    _XylnatmVcCrossConnectRowStatus_Type()
)
xylnatmVcCrossConnectRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVcCrossConnectRowStatus.setStatus("mandatory")
_XylnatmVpCrossConnectGroup_ObjectIdentity = ObjectIdentity
xylnatmVpCrossConnectGroup = _XylnatmVpCrossConnectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14)
)
_XylnatmVpCrossConnectTable_Object = MibTable
xylnatmVpCrossConnectTable = _XylnatmVpCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1)
)
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectTable.setStatus("mandatory")
_XylnatmVpCrossConnectEntry_Object = MibTableRow
xylnatmVpCrossConnectEntry = _XylnatmVpCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1)
)
xylnatmVpCrossConnectEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "xylnatmVpCrossConnectLowSlotIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVpCrossConnectLowPortIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVpCrossConnectLowVpi"),
    (0, "XYLAN-CSM-MIB", "xylnatmVpCrossConnectHighSlotIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVpCrossConnectHighPortIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVpCrossConnectHighVpi"),
)
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectEntry.setStatus("mandatory")


class _XylnatmVpCrossConnectLowSlotIndex_Type(Integer32):
    """Custom type xylnatmVpCrossConnectLowSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_XylnatmVpCrossConnectLowSlotIndex_Type.__name__ = "Integer32"
_XylnatmVpCrossConnectLowSlotIndex_Object = MibTableColumn
xylnatmVpCrossConnectLowSlotIndex = _XylnatmVpCrossConnectLowSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1, 1),
    _XylnatmVpCrossConnectLowSlotIndex_Type()
)
xylnatmVpCrossConnectLowSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectLowSlotIndex.setStatus("mandatory")
_XylnatmVpCrossConnectLowPortIndex_Type = Integer32
_XylnatmVpCrossConnectLowPortIndex_Object = MibTableColumn
xylnatmVpCrossConnectLowPortIndex = _XylnatmVpCrossConnectLowPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1, 2),
    _XylnatmVpCrossConnectLowPortIndex_Type()
)
xylnatmVpCrossConnectLowPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectLowPortIndex.setStatus("mandatory")


class _XylnatmVpCrossConnectLowVpi_Type(Integer32):
    """Custom type xylnatmVpCrossConnectLowVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_XylnatmVpCrossConnectLowVpi_Type.__name__ = "Integer32"
_XylnatmVpCrossConnectLowVpi_Object = MibTableColumn
xylnatmVpCrossConnectLowVpi = _XylnatmVpCrossConnectLowVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1, 3),
    _XylnatmVpCrossConnectLowVpi_Type()
)
xylnatmVpCrossConnectLowVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectLowVpi.setStatus("mandatory")


class _XylnatmVpCrossConnectHighSlotIndex_Type(Integer32):
    """Custom type xylnatmVpCrossConnectHighSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_XylnatmVpCrossConnectHighSlotIndex_Type.__name__ = "Integer32"
_XylnatmVpCrossConnectHighSlotIndex_Object = MibTableColumn
xylnatmVpCrossConnectHighSlotIndex = _XylnatmVpCrossConnectHighSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1, 4),
    _XylnatmVpCrossConnectHighSlotIndex_Type()
)
xylnatmVpCrossConnectHighSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectHighSlotIndex.setStatus("mandatory")
_XylnatmVpCrossConnectHighPortIndex_Type = Integer32
_XylnatmVpCrossConnectHighPortIndex_Object = MibTableColumn
xylnatmVpCrossConnectHighPortIndex = _XylnatmVpCrossConnectHighPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1, 5),
    _XylnatmVpCrossConnectHighPortIndex_Type()
)
xylnatmVpCrossConnectHighPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectHighPortIndex.setStatus("mandatory")


class _XylnatmVpCrossConnectHighVpi_Type(Integer32):
    """Custom type xylnatmVpCrossConnectHighVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_XylnatmVpCrossConnectHighVpi_Type.__name__ = "Integer32"
_XylnatmVpCrossConnectHighVpi_Object = MibTableColumn
xylnatmVpCrossConnectHighVpi = _XylnatmVpCrossConnectHighVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1, 6),
    _XylnatmVpCrossConnectHighVpi_Type()
)
xylnatmVpCrossConnectHighVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectHighVpi.setStatus("mandatory")


class _XylnatmVpCrossConnectConnectionId_Type(Integer32):
    """Custom type xylnatmVpCrossConnectConnectionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("multicastChild", 2),
          ("multicastParent", 1),
          ("nonMulticastParent", 3),
          ("unknown", 4))
    )


_XylnatmVpCrossConnectConnectionId_Type.__name__ = "Integer32"
_XylnatmVpCrossConnectConnectionId_Object = MibTableColumn
xylnatmVpCrossConnectConnectionId = _XylnatmVpCrossConnectConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1, 7),
    _XylnatmVpCrossConnectConnectionId_Type()
)
xylnatmVpCrossConnectConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectConnectionId.setStatus("mandatory")
_XylnatmVpCrossConnectLowRxTrafficDescrIndex_Type = Integer32
_XylnatmVpCrossConnectLowRxTrafficDescrIndex_Object = MibTableColumn
xylnatmVpCrossConnectLowRxTrafficDescrIndex = _XylnatmVpCrossConnectLowRxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1, 8),
    _XylnatmVpCrossConnectLowRxTrafficDescrIndex_Type()
)
xylnatmVpCrossConnectLowRxTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectLowRxTrafficDescrIndex.setStatus("mandatory")
_XylnatmVpCrossConnectLowTxTrafficDescrIndex_Type = Integer32
_XylnatmVpCrossConnectLowTxTrafficDescrIndex_Object = MibTableColumn
xylnatmVpCrossConnectLowTxTrafficDescrIndex = _XylnatmVpCrossConnectLowTxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1, 9),
    _XylnatmVpCrossConnectLowTxTrafficDescrIndex_Type()
)
xylnatmVpCrossConnectLowTxTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectLowTxTrafficDescrIndex.setStatus("mandatory")


class _XylnatmVpCrossConnectMCastEnable_Type(Integer32):
    """Custom type xylnatmVpCrossConnectMCastEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylnatmVpCrossConnectMCastEnable_Type.__name__ = "Integer32"
_XylnatmVpCrossConnectMCastEnable_Object = MibTableColumn
xylnatmVpCrossConnectMCastEnable = _XylnatmVpCrossConnectMCastEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1, 10),
    _XylnatmVpCrossConnectMCastEnable_Type()
)
xylnatmVpCrossConnectMCastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectMCastEnable.setStatus("mandatory")
_XylnatmVpCrossConnectL2HLastChange_Type = DisplayString
_XylnatmVpCrossConnectL2HLastChange_Object = MibTableColumn
xylnatmVpCrossConnectL2HLastChange = _XylnatmVpCrossConnectL2HLastChange_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1, 11),
    _XylnatmVpCrossConnectL2HLastChange_Type()
)
xylnatmVpCrossConnectL2HLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectL2HLastChange.setStatus("mandatory")
_XylnatmVpCrossConnectH2LLastChange_Type = DisplayString
_XylnatmVpCrossConnectH2LLastChange_Object = MibTableColumn
xylnatmVpCrossConnectH2LLastChange = _XylnatmVpCrossConnectH2LLastChange_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1, 12),
    _XylnatmVpCrossConnectH2LLastChange_Type()
)
xylnatmVpCrossConnectH2LLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectH2LLastChange.setStatus("mandatory")


class _XylnatmVpCrossConnectL2HOperStatus_Type(Integer32):
    """Custom type xylnatmVpCrossConnectL2HOperStatus based on Integer32"""
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
        *(("end2endDown", 3),
          ("end2endup", 2),
          ("localDown", 5),
          ("localUpEndToEndUnknown", 4),
          ("unknown", 1))
    )


_XylnatmVpCrossConnectL2HOperStatus_Type.__name__ = "Integer32"
_XylnatmVpCrossConnectL2HOperStatus_Object = MibTableColumn
xylnatmVpCrossConnectL2HOperStatus = _XylnatmVpCrossConnectL2HOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1, 13),
    _XylnatmVpCrossConnectL2HOperStatus_Type()
)
xylnatmVpCrossConnectL2HOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectL2HOperStatus.setStatus("mandatory")


class _XylnatmVpCrossConnectH2LOperStatus_Type(Integer32):
    """Custom type xylnatmVpCrossConnectH2LOperStatus based on Integer32"""
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
        *(("end2endDown", 3),
          ("end2endup", 2),
          ("localDown", 5),
          ("localUpEndToEndUnknown", 4),
          ("unknown", 1))
    )


_XylnatmVpCrossConnectH2LOperStatus_Type.__name__ = "Integer32"
_XylnatmVpCrossConnectH2LOperStatus_Object = MibTableColumn
xylnatmVpCrossConnectH2LOperStatus = _XylnatmVpCrossConnectH2LOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1, 14),
    _XylnatmVpCrossConnectH2LOperStatus_Type()
)
xylnatmVpCrossConnectH2LOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectH2LOperStatus.setStatus("mandatory")


class _XylnatmVpCrossConnectVcType_Type(Integer32):
    """Custom type xylnatmVpCrossConnectVcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("control", 4),
          ("pvc", 1),
          ("softPvc", 3),
          ("svc", 2))
    )


_XylnatmVpCrossConnectVcType_Type.__name__ = "Integer32"
_XylnatmVpCrossConnectVcType_Object = MibTableColumn
xylnatmVpCrossConnectVcType = _XylnatmVpCrossConnectVcType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1, 15),
    _XylnatmVpCrossConnectVcType_Type()
)
xylnatmVpCrossConnectVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectVcType.setStatus("mandatory")
_XylnatmVpCrossConnectPvcIdentifier_Type = Integer32
_XylnatmVpCrossConnectPvcIdentifier_Object = MibTableColumn
xylnatmVpCrossConnectPvcIdentifier = _XylnatmVpCrossConnectPvcIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1, 16),
    _XylnatmVpCrossConnectPvcIdentifier_Type()
)
xylnatmVpCrossConnectPvcIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectPvcIdentifier.setStatus("mandatory")


class _XylnatmVpCrossConnectRowStatus_Type(Integer32):
    """Custom type xylnatmVpCrossConnectRowStatus based on Integer32"""
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
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("notActive", 5))
    )


_XylnatmVpCrossConnectRowStatus_Type.__name__ = "Integer32"
_XylnatmVpCrossConnectRowStatus_Object = MibTableColumn
xylnatmVpCrossConnectRowStatus = _XylnatmVpCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 14, 1, 1, 17),
    _XylnatmVpCrossConnectRowStatus_Type()
)
xylnatmVpCrossConnectRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVpCrossConnectRowStatus.setStatus("mandatory")
_XylnatmVclModGroup_ObjectIdentity = ObjectIdentity
xylnatmVclModGroup = _XylnatmVclModGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 15)
)
_XylnatmVclModTable_Object = MibTable
xylnatmVclModTable = _XylnatmVclModTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 15, 1)
)
if mibBuilder.loadTexts:
    xylnatmVclModTable.setStatus("mandatory")
_XylnatmVclModEntry_Object = MibTableRow
xylnatmVclModEntry = _XylnatmVclModEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 15, 1, 1)
)
xylnatmVclModEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "xylnatmVclModSlotIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVclModPortIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVclModVclVpi"),
    (0, "XYLAN-CSM-MIB", "xylnatmVclModVclVci"),
)
if mibBuilder.loadTexts:
    xylnatmVclModEntry.setStatus("mandatory")
_XylnatmVclModSlotIndex_Type = Integer32
_XylnatmVclModSlotIndex_Object = MibTableColumn
xylnatmVclModSlotIndex = _XylnatmVclModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 15, 1, 1, 1),
    _XylnatmVclModSlotIndex_Type()
)
xylnatmVclModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclModSlotIndex.setStatus("mandatory")
_XylnatmVclModPortIndex_Type = Integer32
_XylnatmVclModPortIndex_Object = MibTableColumn
xylnatmVclModPortIndex = _XylnatmVclModPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 15, 1, 1, 2),
    _XylnatmVclModPortIndex_Type()
)
xylnatmVclModPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclModPortIndex.setStatus("mandatory")
_XylnatmVclModVclVpi_Type = Integer32
_XylnatmVclModVclVpi_Object = MibTableColumn
xylnatmVclModVclVpi = _XylnatmVclModVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 15, 1, 1, 3),
    _XylnatmVclModVclVpi_Type()
)
xylnatmVclModVclVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclModVclVpi.setStatus("mandatory")
_XylnatmVclModVclVci_Type = Integer32
_XylnatmVclModVclVci_Object = MibTableColumn
xylnatmVclModVclVci = _XylnatmVclModVclVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 15, 1, 1, 4),
    _XylnatmVclModVclVci_Type()
)
xylnatmVclModVclVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVclModVclVci.setStatus("mandatory")
_XylnatmVclModDestSlotIndex_Type = Integer32
_XylnatmVclModDestSlotIndex_Object = MibTableColumn
xylnatmVclModDestSlotIndex = _XylnatmVclModDestSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 15, 1, 1, 5),
    _XylnatmVclModDestSlotIndex_Type()
)
xylnatmVclModDestSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclModDestSlotIndex.setStatus("mandatory")
_XylnatmVclModDestPortIndex_Type = Integer32
_XylnatmVclModDestPortIndex_Object = MibTableColumn
xylnatmVclModDestPortIndex = _XylnatmVclModDestPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 15, 1, 1, 6),
    _XylnatmVclModDestPortIndex_Type()
)
xylnatmVclModDestPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclModDestPortIndex.setStatus("mandatory")
_XylnatmVclModDestVclVpi_Type = Integer32
_XylnatmVclModDestVclVpi_Object = MibTableColumn
xylnatmVclModDestVclVpi = _XylnatmVclModDestVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 15, 1, 1, 7),
    _XylnatmVclModDestVclVpi_Type()
)
xylnatmVclModDestVclVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclModDestVclVpi.setStatus("mandatory")
_XylnatmVclModDestVclVci_Type = Integer32
_XylnatmVclModDestVclVci_Object = MibTableColumn
xylnatmVclModDestVclVci = _XylnatmVclModDestVclVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 15, 1, 1, 8),
    _XylnatmVclModDestVclVci_Type()
)
xylnatmVclModDestVclVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclModDestVclVci.setStatus("mandatory")


class _XylnatmVclModDestStatus_Type(Integer32):
    """Custom type xylnatmVclModDestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2))
    )


_XylnatmVclModDestStatus_Type.__name__ = "Integer32"
_XylnatmVclModDestStatus_Object = MibTableColumn
xylnatmVclModDestStatus = _XylnatmVclModDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 15, 1, 1, 9),
    _XylnatmVclModDestStatus_Type()
)
xylnatmVclModDestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVclModDestStatus.setStatus("mandatory")
_XylnatmVplModGroup_ObjectIdentity = ObjectIdentity
xylnatmVplModGroup = _XylnatmVplModGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 16)
)
_XylnatmVplModTable_Object = MibTable
xylnatmVplModTable = _XylnatmVplModTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 16, 1)
)
if mibBuilder.loadTexts:
    xylnatmVplModTable.setStatus("mandatory")
_XylnatmVplModEntry_Object = MibTableRow
xylnatmVplModEntry = _XylnatmVplModEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 16, 1, 1)
)
xylnatmVplModEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "xylnatmVplModSlotIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVplModPortIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmVplModVplVpi"),
)
if mibBuilder.loadTexts:
    xylnatmVplModEntry.setStatus("mandatory")
_XylnatmVplModSlotIndex_Type = Integer32
_XylnatmVplModSlotIndex_Object = MibTableColumn
xylnatmVplModSlotIndex = _XylnatmVplModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 16, 1, 1, 1),
    _XylnatmVplModSlotIndex_Type()
)
xylnatmVplModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplModSlotIndex.setStatus("mandatory")
_XylnatmVplModPortIndex_Type = Integer32
_XylnatmVplModPortIndex_Object = MibTableColumn
xylnatmVplModPortIndex = _XylnatmVplModPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 16, 1, 1, 2),
    _XylnatmVplModPortIndex_Type()
)
xylnatmVplModPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplModPortIndex.setStatus("mandatory")
_XylnatmVplModVplVpi_Type = Integer32
_XylnatmVplModVplVpi_Object = MibTableColumn
xylnatmVplModVplVpi = _XylnatmVplModVplVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 16, 1, 1, 3),
    _XylnatmVplModVplVpi_Type()
)
xylnatmVplModVplVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVplModVplVpi.setStatus("mandatory")
_XylnatmVplModDestSlotIndex_Type = Integer32
_XylnatmVplModDestSlotIndex_Object = MibTableColumn
xylnatmVplModDestSlotIndex = _XylnatmVplModDestSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 16, 1, 1, 4),
    _XylnatmVplModDestSlotIndex_Type()
)
xylnatmVplModDestSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplModDestSlotIndex.setStatus("mandatory")
_XylnatmVplModDestPortIndex_Type = Integer32
_XylnatmVplModDestPortIndex_Object = MibTableColumn
xylnatmVplModDestPortIndex = _XylnatmVplModDestPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 16, 1, 1, 5),
    _XylnatmVplModDestPortIndex_Type()
)
xylnatmVplModDestPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplModDestPortIndex.setStatus("mandatory")
_XylnatmVplModDestVplVpi_Type = Integer32
_XylnatmVplModDestVplVpi_Object = MibTableColumn
xylnatmVplModDestVplVpi = _XylnatmVplModDestVplVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 16, 1, 1, 6),
    _XylnatmVplModDestVplVpi_Type()
)
xylnatmVplModDestVplVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplModDestVplVpi.setStatus("mandatory")


class _XylnatmVplModDestStatus_Type(Integer32):
    """Custom type xylnatmVplModDestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2))
    )


_XylnatmVplModDestStatus_Type.__name__ = "Integer32"
_XylnatmVplModDestStatus_Object = MibTableColumn
xylnatmVplModDestStatus = _XylnatmVplModDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 16, 1, 1, 7),
    _XylnatmVplModDestStatus_Type()
)
xylnatmVplModDestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVplModDestStatus.setStatus("mandatory")
_XylnatmClockingxCtrlGroup_ObjectIdentity = ObjectIdentity
xylnatmClockingxCtrlGroup = _XylnatmClockingxCtrlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 17)
)
_XylnatmClockingxCtrlTable_Object = MibTable
xylnatmClockingxCtrlTable = _XylnatmClockingxCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 17, 1)
)
if mibBuilder.loadTexts:
    xylnatmClockingxCtrlTable.setStatus("mandatory")
_XylnatmClockingxCtrlEntry_Object = MibTableRow
xylnatmClockingxCtrlEntry = _XylnatmClockingxCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 17, 1, 1)
)
xylnatmClockingxCtrlEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "xylnatmClockingxCtrlBusLine"),
    (0, "XYLAN-CSM-MIB", "xylnatmClockingxCtrlSrcLevel"),
)
if mibBuilder.loadTexts:
    xylnatmClockingxCtrlEntry.setStatus("mandatory")


class _XylnatmClockingxCtrlBusLine_Type(Integer32):
    """Custom type xylnatmClockingxCtrlBusLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eightKhz", 1),
          ("nineteenMhz", 2))
    )


_XylnatmClockingxCtrlBusLine_Type.__name__ = "Integer32"
_XylnatmClockingxCtrlBusLine_Object = MibTableColumn
xylnatmClockingxCtrlBusLine = _XylnatmClockingxCtrlBusLine_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 17, 1, 1, 1),
    _XylnatmClockingxCtrlBusLine_Type()
)
xylnatmClockingxCtrlBusLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmClockingxCtrlBusLine.setStatus("mandatory")


class _XylnatmClockingxCtrlSrcLevel_Type(Integer32):
    """Custom type xylnatmClockingxCtrlSrcLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )


_XylnatmClockingxCtrlSrcLevel_Type.__name__ = "Integer32"
_XylnatmClockingxCtrlSrcLevel_Object = MibTableColumn
xylnatmClockingxCtrlSrcLevel = _XylnatmClockingxCtrlSrcLevel_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 17, 1, 1, 2),
    _XylnatmClockingxCtrlSrcLevel_Type()
)
xylnatmClockingxCtrlSrcLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmClockingxCtrlSrcLevel.setStatus("mandatory")


class _XylnatmClockingxSrcOperState_Type(Integer32):
    """Custom type xylnatmClockingxSrcOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1),
          ("standby", 3))
    )


_XylnatmClockingxSrcOperState_Type.__name__ = "Integer32"
_XylnatmClockingxSrcOperState_Object = MibTableColumn
xylnatmClockingxSrcOperState = _XylnatmClockingxSrcOperState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 17, 1, 1, 3),
    _XylnatmClockingxSrcOperState_Type()
)
xylnatmClockingxSrcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmClockingxSrcOperState.setStatus("mandatory")


class _XylnatmClockingxSrcType_Type(Integer32):
    """Custom type xylnatmClockingxSrcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", 1),
          ("onboardOscillator", 3),
          ("receiveDataDerived", 2))
    )


_XylnatmClockingxSrcType_Type.__name__ = "Integer32"
_XylnatmClockingxSrcType_Object = MibTableColumn
xylnatmClockingxSrcType = _XylnatmClockingxSrcType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 17, 1, 1, 4),
    _XylnatmClockingxSrcType_Type()
)
xylnatmClockingxSrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmClockingxSrcType.setStatus("mandatory")


class _XylnatmClockingxCtrlSlot_Type(Integer32):
    """Custom type xylnatmClockingxCtrlSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_XylnatmClockingxCtrlSlot_Type.__name__ = "Integer32"
_XylnatmClockingxCtrlSlot_Object = MibTableColumn
xylnatmClockingxCtrlSlot = _XylnatmClockingxCtrlSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 17, 1, 1, 5),
    _XylnatmClockingxCtrlSlot_Type()
)
xylnatmClockingxCtrlSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmClockingxCtrlSlot.setStatus("mandatory")


class _XylnatmClockingxCtrlPort_Type(Integer32):
    """Custom type xylnatmClockingxCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_XylnatmClockingxCtrlPort_Type.__name__ = "Integer32"
_XylnatmClockingxCtrlPort_Object = MibTableColumn
xylnatmClockingxCtrlPort = _XylnatmClockingxCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 17, 1, 1, 6),
    _XylnatmClockingxCtrlPort_Type()
)
xylnatmClockingxCtrlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmClockingxCtrlPort.setStatus("mandatory")


class _XylnatmClockingxGlobalCST_Type(Integer32):
    """Custom type xylnatmClockingxGlobalCST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_XylnatmClockingxGlobalCST_Type.__name__ = "Integer32"
_XylnatmClockingxGlobalCST_Object = MibScalar
xylnatmClockingxGlobalCST = _XylnatmClockingxGlobalCST_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 17, 2),
    _XylnatmClockingxGlobalCST_Type()
)
xylnatmClockingxGlobalCST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmClockingxGlobalCST.setStatus("mandatory")
_XylnatmTrafficShaperConfGroup_ObjectIdentity = ObjectIdentity
xylnatmTrafficShaperConfGroup = _XylnatmTrafficShaperConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 18)
)
_XylnatmTrafficShaperConfTable_Object = MibTable
xylnatmTrafficShaperConfTable = _XylnatmTrafficShaperConfTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 18, 1)
)
if mibBuilder.loadTexts:
    xylnatmTrafficShaperConfTable.setStatus("mandatory")
_XylnatmTrafficShaperConfEntry_Object = MibTableRow
xylnatmTrafficShaperConfEntry = _XylnatmTrafficShaperConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 18, 1, 1)
)
xylnatmTrafficShaperConfEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "xylnatmTrafficShaperConfSlotIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmTrafficShaperConfPortIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmTrafficShaperConfTsNumIndex"),
)
if mibBuilder.loadTexts:
    xylnatmTrafficShaperConfEntry.setStatus("mandatory")


class _XylnatmTrafficShaperConfSlotIndex_Type(Integer32):
    """Custom type xylnatmTrafficShaperConfSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_XylnatmTrafficShaperConfSlotIndex_Type.__name__ = "Integer32"
_XylnatmTrafficShaperConfSlotIndex_Object = MibTableColumn
xylnatmTrafficShaperConfSlotIndex = _XylnatmTrafficShaperConfSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 18, 1, 1, 1),
    _XylnatmTrafficShaperConfSlotIndex_Type()
)
xylnatmTrafficShaperConfSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmTrafficShaperConfSlotIndex.setStatus("mandatory")


class _XylnatmTrafficShaperConfPortIndex_Type(Integer32):
    """Custom type xylnatmTrafficShaperConfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_XylnatmTrafficShaperConfPortIndex_Type.__name__ = "Integer32"
_XylnatmTrafficShaperConfPortIndex_Object = MibTableColumn
xylnatmTrafficShaperConfPortIndex = _XylnatmTrafficShaperConfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 18, 1, 1, 2),
    _XylnatmTrafficShaperConfPortIndex_Type()
)
xylnatmTrafficShaperConfPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmTrafficShaperConfPortIndex.setStatus("mandatory")


class _XylnatmTrafficShaperConfTsNumIndex_Type(Integer32):
    """Custom type xylnatmTrafficShaperConfTsNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_XylnatmTrafficShaperConfTsNumIndex_Type.__name__ = "Integer32"
_XylnatmTrafficShaperConfTsNumIndex_Object = MibTableColumn
xylnatmTrafficShaperConfTsNumIndex = _XylnatmTrafficShaperConfTsNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 18, 1, 1, 3),
    _XylnatmTrafficShaperConfTsNumIndex_Type()
)
xylnatmTrafficShaperConfTsNumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmTrafficShaperConfTsNumIndex.setStatus("mandatory")


class _XylnatmTrafficShaperConfCDV_Type(Integer32):
    """Custom type xylnatmTrafficShaperConfCDV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 1000),
    )


_XylnatmTrafficShaperConfCDV_Type.__name__ = "Integer32"
_XylnatmTrafficShaperConfCDV_Object = MibTableColumn
xylnatmTrafficShaperConfCDV = _XylnatmTrafficShaperConfCDV_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 18, 1, 1, 4),
    _XylnatmTrafficShaperConfCDV_Type()
)
xylnatmTrafficShaperConfCDV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmTrafficShaperConfCDV.setStatus("mandatory")
_XylnatmTrafficShaperConfPCR_Type = Integer32
_XylnatmTrafficShaperConfPCR_Object = MibTableColumn
xylnatmTrafficShaperConfPCR = _XylnatmTrafficShaperConfPCR_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 18, 1, 1, 5),
    _XylnatmTrafficShaperConfPCR_Type()
)
xylnatmTrafficShaperConfPCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmTrafficShaperConfPCR.setStatus("mandatory")
_XylnatmTrafficShaperConfSCR_Type = Integer32
_XylnatmTrafficShaperConfSCR_Object = MibTableColumn
xylnatmTrafficShaperConfSCR = _XylnatmTrafficShaperConfSCR_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 18, 1, 1, 6),
    _XylnatmTrafficShaperConfSCR_Type()
)
xylnatmTrafficShaperConfSCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmTrafficShaperConfSCR.setStatus("mandatory")
_XylnatmTrafficShaperConfMBS_Type = Integer32
_XylnatmTrafficShaperConfMBS_Object = MibTableColumn
xylnatmTrafficShaperConfMBS = _XylnatmTrafficShaperConfMBS_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 18, 1, 1, 7),
    _XylnatmTrafficShaperConfMBS_Type()
)
xylnatmTrafficShaperConfMBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmTrafficShaperConfMBS.setStatus("mandatory")
_XylnatmTrafficShaperMemGroup_ObjectIdentity = ObjectIdentity
xylnatmTrafficShaperMemGroup = _XylnatmTrafficShaperMemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 19)
)
_XylnatmTrafficShaperMemTable_Object = MibTable
xylnatmTrafficShaperMemTable = _XylnatmTrafficShaperMemTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 19, 1)
)
if mibBuilder.loadTexts:
    xylnatmTrafficShaperMemTable.setStatus("mandatory")
_XylnatmTrafficShaperMemEntry_Object = MibTableRow
xylnatmTrafficShaperMemEntry = _XylnatmTrafficShaperMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 19, 1, 1)
)
xylnatmTrafficShaperMemEntry.setIndexNames(
    (0, "XYLAN-CSM-MIB", "xylnatmTrafficShaperMemSlotIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmTrafficShaperMemPortIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmTrafficShaperMemTsNumIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmTrafficShaperMemVpiNumIndex"),
    (0, "XYLAN-CSM-MIB", "xylnatmTrafficShaperMemVciNumIndex"),
)
if mibBuilder.loadTexts:
    xylnatmTrafficShaperMemEntry.setStatus("mandatory")


class _XylnatmTrafficShaperMemSlotIndex_Type(Integer32):
    """Custom type xylnatmTrafficShaperMemSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_XylnatmTrafficShaperMemSlotIndex_Type.__name__ = "Integer32"
_XylnatmTrafficShaperMemSlotIndex_Object = MibTableColumn
xylnatmTrafficShaperMemSlotIndex = _XylnatmTrafficShaperMemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 19, 1, 1, 1),
    _XylnatmTrafficShaperMemSlotIndex_Type()
)
xylnatmTrafficShaperMemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmTrafficShaperMemSlotIndex.setStatus("mandatory")


class _XylnatmTrafficShaperMemPortIndex_Type(Integer32):
    """Custom type xylnatmTrafficShaperMemPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_XylnatmTrafficShaperMemPortIndex_Type.__name__ = "Integer32"
_XylnatmTrafficShaperMemPortIndex_Object = MibTableColumn
xylnatmTrafficShaperMemPortIndex = _XylnatmTrafficShaperMemPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 19, 1, 1, 2),
    _XylnatmTrafficShaperMemPortIndex_Type()
)
xylnatmTrafficShaperMemPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmTrafficShaperMemPortIndex.setStatus("mandatory")


class _XylnatmTrafficShaperMemTsNumIndex_Type(Integer32):
    """Custom type xylnatmTrafficShaperMemTsNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_XylnatmTrafficShaperMemTsNumIndex_Type.__name__ = "Integer32"
_XylnatmTrafficShaperMemTsNumIndex_Object = MibTableColumn
xylnatmTrafficShaperMemTsNumIndex = _XylnatmTrafficShaperMemTsNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 19, 1, 1, 3),
    _XylnatmTrafficShaperMemTsNumIndex_Type()
)
xylnatmTrafficShaperMemTsNumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmTrafficShaperMemTsNumIndex.setStatus("mandatory")
_XylnatmTrafficShaperMemVpiNumIndex_Type = Integer32
_XylnatmTrafficShaperMemVpiNumIndex_Object = MibTableColumn
xylnatmTrafficShaperMemVpiNumIndex = _XylnatmTrafficShaperMemVpiNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 19, 1, 1, 4),
    _XylnatmTrafficShaperMemVpiNumIndex_Type()
)
xylnatmTrafficShaperMemVpiNumIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmTrafficShaperMemVpiNumIndex.setStatus("mandatory")
_XylnatmTrafficShaperMemVciNumIndex_Type = Integer32
_XylnatmTrafficShaperMemVciNumIndex_Object = MibTableColumn
xylnatmTrafficShaperMemVciNumIndex = _XylnatmTrafficShaperMemVciNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 19, 1, 1, 5),
    _XylnatmTrafficShaperMemVciNumIndex_Type()
)
xylnatmTrafficShaperMemVciNumIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmTrafficShaperMemVciNumIndex.setStatus("mandatory")


class _XylnatmTrafficShaperMemVpiOper_Type(Integer32):
    """Custom type xylnatmTrafficShaperMemVpiOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("none", 1),
          ("rem", 3))
    )


_XylnatmTrafficShaperMemVpiOper_Type.__name__ = "Integer32"
_XylnatmTrafficShaperMemVpiOper_Object = MibTableColumn
xylnatmTrafficShaperMemVpiOper = _XylnatmTrafficShaperMemVpiOper_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 19, 1, 1, 6),
    _XylnatmTrafficShaperMemVpiOper_Type()
)
xylnatmTrafficShaperMemVpiOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmTrafficShaperMemVpiOper.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-CSM-MIB",
    **{"AtmxTrafficDescrParamIndex": AtmxTrafficDescrParamIndex,
       "xylanCsmMIB": xylanCsmMIB,
       "atmxVplGroup": atmxVplGroup,
       "atmxVplTable": atmxVplTable,
       "atmxVplEntry": atmxVplEntry,
       "atmxVplSlotIndex": atmxVplSlotIndex,
       "atmxVplPortIndex": atmxVplPortIndex,
       "atmxVplVpi": atmxVplVpi,
       "atmxVplAdminStatus": atmxVplAdminStatus,
       "atmxVplOperStatus": atmxVplOperStatus,
       "atmxVplLastChange": atmxVplLastChange,
       "atmxVplReceiveTrafficDescrIndex": atmxVplReceiveTrafficDescrIndex,
       "atmxVplTransmitTrafficDescrIndex": atmxVplTransmitTrafficDescrIndex,
       "atmxVplCrossConnectIdentifier": atmxVplCrossConnectIdentifier,
       "atmxVplRowStatus": atmxVplRowStatus,
       "atmxVplBidirect": atmxVplBidirect,
       "atmxInterfaceConfGroup": atmxInterfaceConfGroup,
       "atmxInterfaceConfTable": atmxInterfaceConfTable,
       "atmxInterfaceConfEntry": atmxInterfaceConfEntry,
       "atmxInterfaceSlotIndex": atmxInterfaceSlotIndex,
       "atmxInterfacePortIndex": atmxInterfacePortIndex,
       "atmxInterfaceMaxVpcs": atmxInterfaceMaxVpcs,
       "atmxInterfaceMaxVccs": atmxInterfaceMaxVccs,
       "atmxInterfaceConfVpcs": atmxInterfaceConfVpcs,
       "atmxInterfaceConfVccs": atmxInterfaceConfVccs,
       "atmxInterfaceMaxActiveVpiBits": atmxInterfaceMaxActiveVpiBits,
       "atmxInterfaceMaxActiveVciBits": atmxInterfaceMaxActiveVciBits,
       "atmxInterfaceIlmiVpi": atmxInterfaceIlmiVpi,
       "atmxInterfaceIlmiVci": atmxInterfaceIlmiVci,
       "atmxInterfaceAddressType": atmxInterfaceAddressType,
       "atmxVclGroup": atmxVclGroup,
       "atmxVclTable": atmxVclTable,
       "atmxVclEntry": atmxVclEntry,
       "atmxVclSlotIndex": atmxVclSlotIndex,
       "atmxVclPortIndex": atmxVclPortIndex,
       "atmxVclVpi": atmxVclVpi,
       "atmxVclVci": atmxVclVci,
       "atmxVclAdminStatus": atmxVclAdminStatus,
       "atmxVclOperStatus": atmxVclOperStatus,
       "atmxVclLastChange": atmxVclLastChange,
       "atmxVclReceiveTrafficDescrIndex": atmxVclReceiveTrafficDescrIndex,
       "atmxVclTransmitTrafficDescrIndex": atmxVclTransmitTrafficDescrIndex,
       "atmxVccAalType": atmxVccAalType,
       "atmxVccAal5CpcsTransmitSduSize": atmxVccAal5CpcsTransmitSduSize,
       "atmxVccAal5CpcsReceiveSduSize": atmxVccAal5CpcsReceiveSduSize,
       "atmxVccAal5EncapsType": atmxVccAal5EncapsType,
       "atmxVclCrossConnectIdentifier": atmxVclCrossConnectIdentifier,
       "atmxVclRowStatus": atmxVclRowStatus,
       "atmxVclBidirect": atmxVclBidirect,
       "xylnatmInterfaceConfGroup": xylnatmInterfaceConfGroup,
       "xylnatmInterfaceConfTable": xylnatmInterfaceConfTable,
       "xylnatmInterfaceConfEntry": xylnatmInterfaceConfEntry,
       "xylnatmInterfaceSlotIndex": xylnatmInterfaceSlotIndex,
       "xylnatmInterfacePortIndex": xylnatmInterfacePortIndex,
       "xylnatmInterfaceDescription": xylnatmInterfaceDescription,
       "xylnatmInterfaceTransType": xylnatmInterfaceTransType,
       "xylnatmInterfaceType": xylnatmInterfaceType,
       "xylnatmInterfaceMediaType": xylnatmInterfaceMediaType,
       "xylnatmInterfaceAtmAddress": xylnatmInterfaceAtmAddress,
       "xylnatmInterfacePortMode": xylnatmInterfacePortMode,
       "xylnatmInterfaceOperStatus": xylnatmInterfaceOperStatus,
       "xylnatmInterfaceQsaalStatus": xylnatmInterfaceQsaalStatus,
       "xylnatmInterfaceIlmiStatus": xylnatmInterfaceIlmiStatus,
       "xylnatmInterfaceTpRedirect": xylnatmInterfaceTpRedirect,
       "xylnatmInterfaceCutOverSlot": xylnatmInterfaceCutOverSlot,
       "xylnatmInterfaceCutOverPort": xylnatmInterfaceCutOverPort,
       "xylnatmInterfaceClearPortStats": xylnatmInterfaceClearPortStats,
       "xylnatmInterfaceClearChanStats": xylnatmInterfaceClearChanStats,
       "xylnatmInterfaceClearSlotStats": xylnatmInterfaceClearSlotStats,
       "xylnatmInterfaceTransmissionType": xylnatmInterfaceTransmissionType,
       "xylnatmInterfaceIlmiState": xylnatmInterfaceIlmiState,
       "xylnatmInterfaceTimingMode": xylnatmInterfaceTimingMode,
       "xylnatmInterfaceLocalSrc": xylnatmInterfaceLocalSrc,
       "xylnatmInterfaceUniVersion": xylnatmInterfaceUniVersion,
       "xylnatmILMIConfTable": xylnatmILMIConfTable,
       "xylnatmILMIConfEntry": xylnatmILMIConfEntry,
       "xylnatmILMIConfSlot": xylnatmILMIConfSlot,
       "xylnatmILMIConfPort": xylnatmILMIConfPort,
       "xylnatmILMIConfInstance": xylnatmILMIConfInstance,
       "xylnatmILMIConfILMIEnable": xylnatmILMIConfILMIEnable,
       "xylnatmILMIConfILMIPollEnable": xylnatmILMIConfILMIPollEnable,
       "xylnatmILMIConfAutoCfgEnable": xylnatmILMIConfAutoCfgEnable,
       "xylnatmILMIConfAutoCfgStatus": xylnatmILMIConfAutoCfgStatus,
       "xylnatmILMIConfAutoCfgTrigg": xylnatmILMIConfAutoCfgTrigg,
       "xylnatmILMIConfAutoCfgDfltIf": xylnatmILMIConfAutoCfgDfltIf,
       "xylnatmILMIConfAutoCfgDfltSigVer": xylnatmILMIConfAutoCfgDfltSigVer,
       "xylnatmILMIConfAutoCfgCurIf": xylnatmILMIConfAutoCfgCurIf,
       "xylnatmILMIConfAutoCfgCurSigVer": xylnatmILMIConfAutoCfgCurSigVer,
       "xylnatmILMIConfAutoCfgCurILMIVer": xylnatmILMIConfAutoCfgCurILMIVer,
       "xylnatmILMIConfPeerUniType": xylnatmILMIConfPeerUniType,
       "xylnatmILMIConfPeerUniVer": xylnatmILMIConfPeerUniVer,
       "xylnatmILMIConfPeerDevType": xylnatmILMIConfPeerDevType,
       "xylnatmILMIConfPeerNNISigVer": xylnatmILMIConfPeerNNISigVer,
       "xylnatmILMIConfPeerILMIVer": xylnatmILMIConfPeerILMIVer,
       "atmxVpCrossConnectGroup": atmxVpCrossConnectGroup,
       "atmxVpCrossConnectTable": atmxVpCrossConnectTable,
       "atmxVpCrossConnectEntry": atmxVpCrossConnectEntry,
       "atmxVpCrossConnectIndex": atmxVpCrossConnectIndex,
       "atmxVpCrossConnectLowSlotIndex": atmxVpCrossConnectLowSlotIndex,
       "atmxVpCrossConnectLowPortIndex": atmxVpCrossConnectLowPortIndex,
       "atmxVpCrossConnectLowVpi": atmxVpCrossConnectLowVpi,
       "atmxVpCrossConnectHighSlotIndex": atmxVpCrossConnectHighSlotIndex,
       "atmxVpCrossConnectHighPortIndex": atmxVpCrossConnectHighPortIndex,
       "atmxVpCrossConnectHighVpi": atmxVpCrossConnectHighVpi,
       "atmxVpCrossConnectAdminStatus": atmxVpCrossConnectAdminStatus,
       "atmxVpCrossConnectL2HOperStatus": atmxVpCrossConnectL2HOperStatus,
       "atmxVpCrossConnectH2LOperStatus": atmxVpCrossConnectH2LOperStatus,
       "atmxVpCrossConnectL2HLastChange": atmxVpCrossConnectL2HLastChange,
       "atmxVpCrossConnectH2LLastChange": atmxVpCrossConnectH2LLastChange,
       "atmxVpCrossConnectRowStatus": atmxVpCrossConnectRowStatus,
       "atmxSvcVpCrossConnectTable": atmxSvcVpCrossConnectTable,
       "atmxSvcVpCrossConnectEntry": atmxSvcVpCrossConnectEntry,
       "atmxSvcVpCrossConnectLowSlotIndex": atmxSvcVpCrossConnectLowSlotIndex,
       "atmxSvcVpCrossConnectLowPortIndex": atmxSvcVpCrossConnectLowPortIndex,
       "atmxSvcVpCrossConnectLowVpi": atmxSvcVpCrossConnectLowVpi,
       "atmxSvcVpCrossConnectHighSlotIndex": atmxSvcVpCrossConnectHighSlotIndex,
       "atmxSvcVpCrossConnectHighPortIndex": atmxSvcVpCrossConnectHighPortIndex,
       "atmxSvcVpCrossConnectHighVpi": atmxSvcVpCrossConnectHighVpi,
       "atmxSvcVpCrossConnectCreationTime": atmxSvcVpCrossConnectCreationTime,
       "atmxSvcVpCrossConnectLowTDIndex": atmxSvcVpCrossConnectLowTDIndex,
       "atmxSvcVpCrossConnectHighTDIndex": atmxSvcVpCrossConnectHighTDIndex,
       "atmxSvcVpCrossConnectRowStatus": atmxSvcVpCrossConnectRowStatus,
       "xylnatmInterfaceStatGroup": xylnatmInterfaceStatGroup,
       "xylnatmInterfaceStatTable": xylnatmInterfaceStatTable,
       "xylnatmInterfaceStatEntry": xylnatmInterfaceStatEntry,
       "xylnatmInterfaceStatSlotIndex": xylnatmInterfaceStatSlotIndex,
       "xylnatmInterfaceStatPortIndex": xylnatmInterfaceStatPortIndex,
       "xylnatmInterfaceStatRxCells": xylnatmInterfaceStatRxCells,
       "xylnatmInterfaceStatRxClp0Cells": xylnatmInterfaceStatRxClp0Cells,
       "xylnatmInterfaceStatRxClp1Cells": xylnatmInterfaceStatRxClp1Cells,
       "xylnatmInterfaceStatTxCells": xylnatmInterfaceStatTxCells,
       "xylnatmInterfaceStatMarkEfciCells": xylnatmInterfaceStatMarkEfciCells,
       "xylnatmInterfaceStatMarkGcraCells": xylnatmInterfaceStatMarkGcraCells,
       "xylnatmInterfaceStatTotalDiscardCells": xylnatmInterfaceStatTotalDiscardCells,
       "xylnatmInterfaceStatDxCongClp0Cells": xylnatmInterfaceStatDxCongClp0Cells,
       "xylnatmInterfaceStatDxCongClp1Cells": xylnatmInterfaceStatDxCongClp1Cells,
       "xylnatmInterfaceStatDxGcraClp0Cells": xylnatmInterfaceStatDxGcraClp0Cells,
       "xylnatmInterfaceStatDxGcraClp1Cells": xylnatmInterfaceStatDxGcraClp1Cells,
       "xylnatmInterfaceStatDxGcrabClp0Cells": xylnatmInterfaceStatDxGcrabClp0Cells,
       "xylnatmInterfaceStatDxGcrabClp1Cells": xylnatmInterfaceStatDxGcrabClp1Cells,
       "xylnatmInterfaceStatUnknownVpVcCells": xylnatmInterfaceStatUnknownVpVcCells,
       "xylnatmInterfaceStatUnknownVpiCells": xylnatmInterfaceStatUnknownVpiCells,
       "xylnatmInterfaceStatUnknownVciCells": xylnatmInterfaceStatUnknownVciCells,
       "xylnatmInterfaceStatUniType": xylnatmInterfaceStatUniType,
       "xylnatmInterfaceStatUniVersion": xylnatmInterfaceStatUniVersion,
       "xylnatmInterfaceStatRemainingRxBandwidth": xylnatmInterfaceStatRemainingRxBandwidth,
       "xylnatmInterfaceStatRemainingTxBandwidth": xylnatmInterfaceStatRemainingTxBandwidth,
       "atmxVcCrossConnectGroup": atmxVcCrossConnectGroup,
       "atmxVcCrossConnectTable": atmxVcCrossConnectTable,
       "atmxVcCrossConnectEntry": atmxVcCrossConnectEntry,
       "atmxVcCrossConnectIndex": atmxVcCrossConnectIndex,
       "atmxVcCrossConnectLowSlotIndex": atmxVcCrossConnectLowSlotIndex,
       "atmxVcCrossConnectLowPortIndex": atmxVcCrossConnectLowPortIndex,
       "atmxVcCrossConnectLowVpi": atmxVcCrossConnectLowVpi,
       "atmxVcCrossConnectLowVci": atmxVcCrossConnectLowVci,
       "atmxVcCrossConnectHighSlotIndex": atmxVcCrossConnectHighSlotIndex,
       "atmxVcCrossConnectHighPortIndex": atmxVcCrossConnectHighPortIndex,
       "atmxVcCrossConnectHighVpi": atmxVcCrossConnectHighVpi,
       "atmxVcCrossConnectHighVci": atmxVcCrossConnectHighVci,
       "atmxVcCrossConnectAdminStatus": atmxVcCrossConnectAdminStatus,
       "atmxVcCrossConnectL2HOperStatus": atmxVcCrossConnectL2HOperStatus,
       "atmxVcCrossConnectH2LOperStatus": atmxVcCrossConnectH2LOperStatus,
       "atmxVcCrossConnectL2HLastChange": atmxVcCrossConnectL2HLastChange,
       "atmxVcCrossConnectH2LLastChange": atmxVcCrossConnectH2LLastChange,
       "atmxVcCrossConnectRowStatus": atmxVcCrossConnectRowStatus,
       "atmxSvcVcCrossConnectTable": atmxSvcVcCrossConnectTable,
       "atmxSvcVcCrossConnectEntry": atmxSvcVcCrossConnectEntry,
       "atmxSvcVcCrossConnectLowSlotIndex": atmxSvcVcCrossConnectLowSlotIndex,
       "atmxSvcVcCrossConnectLowPortIndex": atmxSvcVcCrossConnectLowPortIndex,
       "atmxSvcVcCrossConnectLowVpi": atmxSvcVcCrossConnectLowVpi,
       "atmxSvcVcCrossConnectLowVci": atmxSvcVcCrossConnectLowVci,
       "atmxSvcVcCrossConnectHighSlotIndex": atmxSvcVcCrossConnectHighSlotIndex,
       "atmxSvcVcCrossConnectHighPortIndex": atmxSvcVcCrossConnectHighPortIndex,
       "atmxSvcVcCrossConnectHighVpi": atmxSvcVcCrossConnectHighVpi,
       "atmxSvcVcCrossConnectHighVci": atmxSvcVcCrossConnectHighVci,
       "atmxSvcVcCrossConnectCreationTime": atmxSvcVcCrossConnectCreationTime,
       "atmxSvcVcCrossConnectLowTDIndex": atmxSvcVcCrossConnectLowTDIndex,
       "atmxSvcVcCrossConnectHighTDIndex": atmxSvcVcCrossConnectHighTDIndex,
       "atmxSvcVcCrossConnectRowStatus": atmxSvcVcCrossConnectRowStatus,
       "atmxTrafficDescrGroup": atmxTrafficDescrGroup,
       "atmxTrafficDescrParamTable": atmxTrafficDescrParamTable,
       "atmxTrafficDescrParamEntry": atmxTrafficDescrParamEntry,
       "atmxTrafficDescrParamIndex": atmxTrafficDescrParamIndex,
       "atmxTrafficDescrType": atmxTrafficDescrType,
       "atmxTrafficDescrParam1": atmxTrafficDescrParam1,
       "atmxTrafficDescrParam2": atmxTrafficDescrParam2,
       "atmxTrafficDescrParam3": atmxTrafficDescrParam3,
       "atmxTrafficDescrParam4": atmxTrafficDescrParam4,
       "atmxTrafficDescrParam5": atmxTrafficDescrParam5,
       "atmxTrafficQoSClass": atmxTrafficQoSClass,
       "atmxTrafficDescrRowStatus": atmxTrafficDescrRowStatus,
       "xylnatmVplGroup": xylnatmVplGroup,
       "xylnatmVplTable": xylnatmVplTable,
       "xylnatmVplEntry": xylnatmVplEntry,
       "xylnatmVplSlotIndex": xylnatmVplSlotIndex,
       "xylnatmVplPortIndex": xylnatmVplPortIndex,
       "xylnatmVplVpi": xylnatmVplVpi,
       "xylnatmVplConnectionDescr": xylnatmVplConnectionDescr,
       "xylnatmVplChanType": xylnatmVplChanType,
       "xylnatmVplTransportPriority": xylnatmVplTransportPriority,
       "xylnatmVplUserPriority": xylnatmVplUserPriority,
       "xylnatmVplStatsMode": xylnatmVplStatsMode,
       "xylnatmVplPrTrackPortBase": xylnatmVplPrTrackPortBase,
       "xylnatmVplPrTrackPort1": xylnatmVplPrTrackPort1,
       "xylnatmVplPrTrackPort2": xylnatmVplPrTrackPort2,
       "xylnatmVplPrTrackPort3": xylnatmVplPrTrackPort3,
       "xylnatmVplAltTrackPortBase": xylnatmVplAltTrackPortBase,
       "xylnatmVplAltTrackPort1": xylnatmVplAltTrackPort1,
       "xylnatmVplAltTrackPort2": xylnatmVplAltTrackPort2,
       "xylnatmVplAltTrackPort3": xylnatmVplAltTrackPort3,
       "xylnatmVplLgclChanRedirect": xylnatmVplLgclChanRedirect,
       "xylnatmVplAAL5Discard": xylnatmVplAAL5Discard,
       "xylnatmVplF4F5SegEndpt": xylnatmVplF4F5SegEndpt,
       "xylnatmVplF4F5CopySeg": xylnatmVplF4F5CopySeg,
       "xylnatmVplF4F5End2EndEndpt": xylnatmVplF4F5End2EndEndpt,
       "xylnatmVplF4F5CopyEnd2End": xylnatmVplF4F5CopyEnd2End,
       "xylnatmVplOamEndpt": xylnatmVplOamEndpt,
       "xylnatmVplOamCopy": xylnatmVplOamCopy,
       "xylnatmVplRmFwdEndpt": xylnatmVplRmFwdEndpt,
       "xylnatmVplRmFwdCopy": xylnatmVplRmFwdCopy,
       "xylnatmVplRmFwdGcraAdv": xylnatmVplRmFwdGcraAdv,
       "xylnatmVplRmBkwdEndpt": xylnatmVplRmBkwdEndpt,
       "xylnatmVplRmBkwdCopy": xylnatmVplRmBkwdCopy,
       "xylnatmVplRmBkwdGcraAdv": xylnatmVplRmBkwdGcraAdv,
       "xylnatmVplRmDiscard": xylnatmVplRmDiscard,
       "xylnatmVplGcraAPoliceMode": xylnatmVplGcraAPoliceMode,
       "xylnatmVplGcraBPoliceMode": xylnatmVplGcraBPoliceMode,
       "xylnatmVplMcGroupId": xylnatmVplMcGroupId,
       "xylnatmVplMcIngressEgress": xylnatmVplMcIngressEgress,
       "xylnatmVclGroup": xylnatmVclGroup,
       "xylnatmVclTable": xylnatmVclTable,
       "xylnatmVclEntry": xylnatmVclEntry,
       "xylnatmVclSlotIndex": xylnatmVclSlotIndex,
       "xylnatmVclPortIndex": xylnatmVclPortIndex,
       "xylnatmVclVpi": xylnatmVclVpi,
       "xylnatmVclVci": xylnatmVclVci,
       "xylnatmVclConnectionDescr": xylnatmVclConnectionDescr,
       "xylnatmVclChanType": xylnatmVclChanType,
       "xylnatmVclTransportPriority": xylnatmVclTransportPriority,
       "xylnatmVclUserPriority": xylnatmVclUserPriority,
       "xylnatmVclStatsMode": xylnatmVclStatsMode,
       "xylnatmVclPrTrackPortBase": xylnatmVclPrTrackPortBase,
       "xylnatmVclPrTrackPort1": xylnatmVclPrTrackPort1,
       "xylnatmVclPrTrackPort2": xylnatmVclPrTrackPort2,
       "xylnatmVclPrTrackPort3": xylnatmVclPrTrackPort3,
       "xylnatmVclAltTrackPortBase": xylnatmVclAltTrackPortBase,
       "xylnatmVclAltTrackPort1": xylnatmVclAltTrackPort1,
       "xylnatmVclAltTrackPort2": xylnatmVclAltTrackPort2,
       "xylnatmVclAltTrackPort3": xylnatmVclAltTrackPort3,
       "xylnatmVclLgclChanRedirect": xylnatmVclLgclChanRedirect,
       "xylnatmVclAAL5Discard": xylnatmVclAAL5Discard,
       "xylnatmVclF4F5SegEndpt": xylnatmVclF4F5SegEndpt,
       "xylnatmVclF4F5CopySeg": xylnatmVclF4F5CopySeg,
       "xylnatmVclF4F5End2EndEndpt": xylnatmVclF4F5End2EndEndpt,
       "xylnatmVclF4F5CopyEnd2End": xylnatmVclF4F5CopyEnd2End,
       "xylnatmVclOamEndpt": xylnatmVclOamEndpt,
       "xylnatmVclOamCopy": xylnatmVclOamCopy,
       "xylnatmVclRmFwdEndpt": xylnatmVclRmFwdEndpt,
       "xylnatmVclRmFwdCopy": xylnatmVclRmFwdCopy,
       "xylnatmVclRmFwdGcraAdv": xylnatmVclRmFwdGcraAdv,
       "xylnatmVclRmBkwdEndpt": xylnatmVclRmBkwdEndpt,
       "xylnatmVclRmBkwdCopy": xylnatmVclRmBkwdCopy,
       "xylnatmVclRmBkwdGcraAdv": xylnatmVclRmBkwdGcraAdv,
       "xylnatmVclRmDiscard": xylnatmVclRmDiscard,
       "xylnatmVclGcraAPoliceMode": xylnatmVclGcraAPoliceMode,
       "xylnatmVclGcraBPoliceMode": xylnatmVclGcraBPoliceMode,
       "xylnatmVclMcGroupId": xylnatmVclMcGroupId,
       "xylnatmVclMcIngressEgress": xylnatmVclMcIngressEgress,
       "xylnatmVplStatGroup": xylnatmVplStatGroup,
       "xylnatmVplStatTable": xylnatmVplStatTable,
       "xylnatmVplStatEntry": xylnatmVplStatEntry,
       "xylnatmVplStatSlotIndex": xylnatmVplStatSlotIndex,
       "xylnatmVplStatPortIndex": xylnatmVplStatPortIndex,
       "xylnatmVplStatVpi": xylnatmVplStatVpi,
       "xylnatmVplStatRxCells": xylnatmVplStatRxCells,
       "xylnatmVplStatTxCells": xylnatmVplStatTxCells,
       "xylnatmVplStatRxClp0Cells": xylnatmVplStatRxClp0Cells,
       "xylnatmVplStatRxClp1Cells": xylnatmVplStatRxClp1Cells,
       "xylnatmVplStatDxCongClp0Cells": xylnatmVplStatDxCongClp0Cells,
       "xylnatmVplStatDxCongClp1Cells": xylnatmVplStatDxCongClp1Cells,
       "xylnatmVplStatDxGcraClp0Cells": xylnatmVplStatDxGcraClp0Cells,
       "xylnatmVplStatDxGcraClp1Cells": xylnatmVplStatDxGcraClp1Cells,
       "xylnatmVplStatDxGcraBClp0Cells": xylnatmVplStatDxGcraBClp0Cells,
       "xylnatmVplStatDxGcraBClp1Cells": xylnatmVplStatDxGcraBClp1Cells,
       "xylnatmVclStatGroup": xylnatmVclStatGroup,
       "xylnatmVclStatTable": xylnatmVclStatTable,
       "xylnatmVclStatEntry": xylnatmVclStatEntry,
       "xylnatmVclStatSlotIndex": xylnatmVclStatSlotIndex,
       "xylnatmVclStatPortIndex": xylnatmVclStatPortIndex,
       "xylnatmVclStatVpi": xylnatmVclStatVpi,
       "xylnatmVclStatVci": xylnatmVclStatVci,
       "xylnatmVclStatRxCells": xylnatmVclStatRxCells,
       "xylnatmVclStatTxCells": xylnatmVclStatTxCells,
       "xylnatmVclStatRxClp0Cells": xylnatmVclStatRxClp0Cells,
       "xylnatmVclStatRxClp1Cells": xylnatmVclStatRxClp1Cells,
       "xylnatmVclStatDxCongClp0Cells": xylnatmVclStatDxCongClp0Cells,
       "xylnatmVclStatDxCongClp1Cells": xylnatmVclStatDxCongClp1Cells,
       "xylnatmVclStatDxGcraClp0Cells": xylnatmVclStatDxGcraClp0Cells,
       "xylnatmVclStatDxGcraClp1Cells": xylnatmVclStatDxGcraClp1Cells,
       "xylnatmVclStatDxGcraBClp0Cells": xylnatmVclStatDxGcraBClp0Cells,
       "xylnatmVclStatDxGcraBClp1Cells": xylnatmVclStatDxGcraBClp1Cells,
       "xylnatmVcCrossConnectGroup": xylnatmVcCrossConnectGroup,
       "xylnatmVcCrossConnectTable": xylnatmVcCrossConnectTable,
       "xylnatmVcCrossConnectEntry": xylnatmVcCrossConnectEntry,
       "xylnatmVcCrossConnectLowSlotIndex": xylnatmVcCrossConnectLowSlotIndex,
       "xylnatmVcCrossConnectLowPortIndex": xylnatmVcCrossConnectLowPortIndex,
       "xylnatmVcCrossConnectLowVpi": xylnatmVcCrossConnectLowVpi,
       "xylnatmVcCrossConnectLowVci": xylnatmVcCrossConnectLowVci,
       "xylnatmVcCrossConnectHighSlotIndex": xylnatmVcCrossConnectHighSlotIndex,
       "xylnatmVcCrossConnectHighPortIndex": xylnatmVcCrossConnectHighPortIndex,
       "xylnatmVcCrossConnectHighVpi": xylnatmVcCrossConnectHighVpi,
       "xylnatmVcCrossConnectHighVci": xylnatmVcCrossConnectHighVci,
       "xylnatmVcCrossConnectConnectionId": xylnatmVcCrossConnectConnectionId,
       "xylnatmVcCrossConnectLowRxTrafficDescrIndex": xylnatmVcCrossConnectLowRxTrafficDescrIndex,
       "xylnatmVcCrossConnectLowTxTrafficDescrIndex": xylnatmVcCrossConnectLowTxTrafficDescrIndex,
       "xylnatmVcCrossConnectMCastEnable": xylnatmVcCrossConnectMCastEnable,
       "xylnatmVcCrossConnectL2HLastChange": xylnatmVcCrossConnectL2HLastChange,
       "xylnatmVcCrossConnectH2LLastChange": xylnatmVcCrossConnectH2LLastChange,
       "xylnatmVcCrossConnectL2HOperStatus": xylnatmVcCrossConnectL2HOperStatus,
       "xylnatmVcCrossConnectH2LOperStatus": xylnatmVcCrossConnectH2LOperStatus,
       "xylnatmVcCrossConnectVcType": xylnatmVcCrossConnectVcType,
       "xylnatmVcCrossConnectPvcIdentifier": xylnatmVcCrossConnectPvcIdentifier,
       "xylnatmVcCrossConnectRowStatus": xylnatmVcCrossConnectRowStatus,
       "xylnatmVpCrossConnectGroup": xylnatmVpCrossConnectGroup,
       "xylnatmVpCrossConnectTable": xylnatmVpCrossConnectTable,
       "xylnatmVpCrossConnectEntry": xylnatmVpCrossConnectEntry,
       "xylnatmVpCrossConnectLowSlotIndex": xylnatmVpCrossConnectLowSlotIndex,
       "xylnatmVpCrossConnectLowPortIndex": xylnatmVpCrossConnectLowPortIndex,
       "xylnatmVpCrossConnectLowVpi": xylnatmVpCrossConnectLowVpi,
       "xylnatmVpCrossConnectHighSlotIndex": xylnatmVpCrossConnectHighSlotIndex,
       "xylnatmVpCrossConnectHighPortIndex": xylnatmVpCrossConnectHighPortIndex,
       "xylnatmVpCrossConnectHighVpi": xylnatmVpCrossConnectHighVpi,
       "xylnatmVpCrossConnectConnectionId": xylnatmVpCrossConnectConnectionId,
       "xylnatmVpCrossConnectLowRxTrafficDescrIndex": xylnatmVpCrossConnectLowRxTrafficDescrIndex,
       "xylnatmVpCrossConnectLowTxTrafficDescrIndex": xylnatmVpCrossConnectLowTxTrafficDescrIndex,
       "xylnatmVpCrossConnectMCastEnable": xylnatmVpCrossConnectMCastEnable,
       "xylnatmVpCrossConnectL2HLastChange": xylnatmVpCrossConnectL2HLastChange,
       "xylnatmVpCrossConnectH2LLastChange": xylnatmVpCrossConnectH2LLastChange,
       "xylnatmVpCrossConnectL2HOperStatus": xylnatmVpCrossConnectL2HOperStatus,
       "xylnatmVpCrossConnectH2LOperStatus": xylnatmVpCrossConnectH2LOperStatus,
       "xylnatmVpCrossConnectVcType": xylnatmVpCrossConnectVcType,
       "xylnatmVpCrossConnectPvcIdentifier": xylnatmVpCrossConnectPvcIdentifier,
       "xylnatmVpCrossConnectRowStatus": xylnatmVpCrossConnectRowStatus,
       "xylnatmVclModGroup": xylnatmVclModGroup,
       "xylnatmVclModTable": xylnatmVclModTable,
       "xylnatmVclModEntry": xylnatmVclModEntry,
       "xylnatmVclModSlotIndex": xylnatmVclModSlotIndex,
       "xylnatmVclModPortIndex": xylnatmVclModPortIndex,
       "xylnatmVclModVclVpi": xylnatmVclModVclVpi,
       "xylnatmVclModVclVci": xylnatmVclModVclVci,
       "xylnatmVclModDestSlotIndex": xylnatmVclModDestSlotIndex,
       "xylnatmVclModDestPortIndex": xylnatmVclModDestPortIndex,
       "xylnatmVclModDestVclVpi": xylnatmVclModDestVclVpi,
       "xylnatmVclModDestVclVci": xylnatmVclModDestVclVci,
       "xylnatmVclModDestStatus": xylnatmVclModDestStatus,
       "xylnatmVplModGroup": xylnatmVplModGroup,
       "xylnatmVplModTable": xylnatmVplModTable,
       "xylnatmVplModEntry": xylnatmVplModEntry,
       "xylnatmVplModSlotIndex": xylnatmVplModSlotIndex,
       "xylnatmVplModPortIndex": xylnatmVplModPortIndex,
       "xylnatmVplModVplVpi": xylnatmVplModVplVpi,
       "xylnatmVplModDestSlotIndex": xylnatmVplModDestSlotIndex,
       "xylnatmVplModDestPortIndex": xylnatmVplModDestPortIndex,
       "xylnatmVplModDestVplVpi": xylnatmVplModDestVplVpi,
       "xylnatmVplModDestStatus": xylnatmVplModDestStatus,
       "xylnatmClockingxCtrlGroup": xylnatmClockingxCtrlGroup,
       "xylnatmClockingxCtrlTable": xylnatmClockingxCtrlTable,
       "xylnatmClockingxCtrlEntry": xylnatmClockingxCtrlEntry,
       "xylnatmClockingxCtrlBusLine": xylnatmClockingxCtrlBusLine,
       "xylnatmClockingxCtrlSrcLevel": xylnatmClockingxCtrlSrcLevel,
       "xylnatmClockingxSrcOperState": xylnatmClockingxSrcOperState,
       "xylnatmClockingxSrcType": xylnatmClockingxSrcType,
       "xylnatmClockingxCtrlSlot": xylnatmClockingxCtrlSlot,
       "xylnatmClockingxCtrlPort": xylnatmClockingxCtrlPort,
       "xylnatmClockingxGlobalCST": xylnatmClockingxGlobalCST,
       "xylnatmTrafficShaperConfGroup": xylnatmTrafficShaperConfGroup,
       "xylnatmTrafficShaperConfTable": xylnatmTrafficShaperConfTable,
       "xylnatmTrafficShaperConfEntry": xylnatmTrafficShaperConfEntry,
       "xylnatmTrafficShaperConfSlotIndex": xylnatmTrafficShaperConfSlotIndex,
       "xylnatmTrafficShaperConfPortIndex": xylnatmTrafficShaperConfPortIndex,
       "xylnatmTrafficShaperConfTsNumIndex": xylnatmTrafficShaperConfTsNumIndex,
       "xylnatmTrafficShaperConfCDV": xylnatmTrafficShaperConfCDV,
       "xylnatmTrafficShaperConfPCR": xylnatmTrafficShaperConfPCR,
       "xylnatmTrafficShaperConfSCR": xylnatmTrafficShaperConfSCR,
       "xylnatmTrafficShaperConfMBS": xylnatmTrafficShaperConfMBS,
       "xylnatmTrafficShaperMemGroup": xylnatmTrafficShaperMemGroup,
       "xylnatmTrafficShaperMemTable": xylnatmTrafficShaperMemTable,
       "xylnatmTrafficShaperMemEntry": xylnatmTrafficShaperMemEntry,
       "xylnatmTrafficShaperMemSlotIndex": xylnatmTrafficShaperMemSlotIndex,
       "xylnatmTrafficShaperMemPortIndex": xylnatmTrafficShaperMemPortIndex,
       "xylnatmTrafficShaperMemTsNumIndex": xylnatmTrafficShaperMemTsNumIndex,
       "xylnatmTrafficShaperMemVpiNumIndex": xylnatmTrafficShaperMemVpiNumIndex,
       "xylnatmTrafficShaperMemVciNumIndex": xylnatmTrafficShaperMemVciNumIndex,
       "xylnatmTrafficShaperMemVpiOper": xylnatmTrafficShaperMemVpiOper}
)
