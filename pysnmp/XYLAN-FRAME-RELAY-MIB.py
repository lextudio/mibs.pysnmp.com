# SNMP MIB module (XYLAN-FRAME-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-FRAME-RELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:02 2024
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

(xylanFrArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanFrArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrxPortGroup_ObjectIdentity = ObjectIdentity
frxPortGroup = _FrxPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 1)
)
_FrxPortTable_Object = MibTable
frxPortTable = _FrxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    frxPortTable.setStatus("mandatory")
_FrxPortEntry_Object = MibTableRow
frxPortEntry = _FrxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1)
)
frxPortEntry.setIndexNames(
    (0, "XYLAN-FRAME-RELAY-MIB", "frxPortSlotIndex"),
    (0, "XYLAN-FRAME-RELAY-MIB", "frxPortPortIndex"),
)
if mibBuilder.loadTexts:
    frxPortEntry.setStatus("mandatory")


class _FrxPortSlotIndex_Type(Integer32):
    """Custom type frxPortSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_FrxPortSlotIndex_Type.__name__ = "Integer32"
_FrxPortSlotIndex_Object = MibTableColumn
frxPortSlotIndex = _FrxPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 1),
    _FrxPortSlotIndex_Type()
)
frxPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPortSlotIndex.setStatus("mandatory")


class _FrxPortPortIndex_Type(Integer32):
    """Custom type frxPortPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_FrxPortPortIndex_Type.__name__ = "Integer32"
_FrxPortPortIndex_Object = MibTableColumn
frxPortPortIndex = _FrxPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 2),
    _FrxPortPortIndex_Type()
)
frxPortPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPortPortIndex.setStatus("mandatory")


class _FrxPortDescription_Type(DisplayString):
    """Custom type frxPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FrxPortDescription_Type.__name__ = "DisplayString"
_FrxPortDescription_Object = MibTableColumn
frxPortDescription = _FrxPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 3),
    _FrxPortDescription_Type()
)
frxPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxPortDescription.setStatus("mandatory")


class _FrxPortDefaultBridgingVLAN_Type(Integer32):
    """Custom type frxPortDefaultBridgingVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxPortDefaultBridgingVLAN_Type.__name__ = "Integer32"
_FrxPortDefaultBridgingVLAN_Object = MibTableColumn
frxPortDefaultBridgingVLAN = _FrxPortDefaultBridgingVLAN_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 4),
    _FrxPortDefaultBridgingVLAN_Type()
)
frxPortDefaultBridgingVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxPortDefaultBridgingVLAN.setStatus("mandatory")


class _FrxPortDefaultBridgingServiceNumber_Type(Integer32):
    """Custom type frxPortDefaultBridgingServiceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_FrxPortDefaultBridgingServiceNumber_Type.__name__ = "Integer32"
_FrxPortDefaultBridgingServiceNumber_Object = MibTableColumn
frxPortDefaultBridgingServiceNumber = _FrxPortDefaultBridgingServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 5),
    _FrxPortDefaultBridgingServiceNumber_Type()
)
frxPortDefaultBridgingServiceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxPortDefaultBridgingServiceNumber.setStatus("mandatory")


class _FrxPortDefaultRoutingVLAN_Type(Integer32):
    """Custom type frxPortDefaultRoutingVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxPortDefaultRoutingVLAN_Type.__name__ = "Integer32"
_FrxPortDefaultRoutingVLAN_Object = MibTableColumn
frxPortDefaultRoutingVLAN = _FrxPortDefaultRoutingVLAN_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 6),
    _FrxPortDefaultRoutingVLAN_Type()
)
frxPortDefaultRoutingVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxPortDefaultRoutingVLAN.setStatus("mandatory")


class _FrxPortDefaultCompressionAdminStatus_Type(Integer32):
    """Custom type frxPortDefaultCompressionAdminStatus based on Integer32"""
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


_FrxPortDefaultCompressionAdminStatus_Type.__name__ = "Integer32"
_FrxPortDefaultCompressionAdminStatus_Object = MibTableColumn
frxPortDefaultCompressionAdminStatus = _FrxPortDefaultCompressionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 7),
    _FrxPortDefaultCompressionAdminStatus_Type()
)
frxPortDefaultCompressionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxPortDefaultCompressionAdminStatus.setStatus("mandatory")


class _FrxPortDefaultCompressionPRetryTime_Type(Integer32):
    """Custom type frxPortDefaultCompressionPRetryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrxPortDefaultCompressionPRetryTime_Type.__name__ = "Integer32"
_FrxPortDefaultCompressionPRetryTime_Object = MibTableColumn
frxPortDefaultCompressionPRetryTime = _FrxPortDefaultCompressionPRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 8),
    _FrxPortDefaultCompressionPRetryTime_Type()
)
frxPortDefaultCompressionPRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxPortDefaultCompressionPRetryTime.setStatus("mandatory")


class _FrxPortDefaultCompressionPRetryCount_Type(Integer32):
    """Custom type frxPortDefaultCompressionPRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 255),
    )


_FrxPortDefaultCompressionPRetryCount_Type.__name__ = "Integer32"
_FrxPortDefaultCompressionPRetryCount_Object = MibTableColumn
frxPortDefaultCompressionPRetryCount = _FrxPortDefaultCompressionPRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 9),
    _FrxPortDefaultCompressionPRetryCount_Type()
)
frxPortDefaultCompressionPRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxPortDefaultCompressionPRetryCount.setStatus("mandatory")


class _FrxPortDefaultBridgingMode_Type(Integer32):
    """Custom type frxPortDefaultBridgingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FrxPortDefaultBridgingMode_Type.__name__ = "Integer32"
_FrxPortDefaultBridgingMode_Object = MibTableColumn
frxPortDefaultBridgingMode = _FrxPortDefaultBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 10),
    _FrxPortDefaultBridgingMode_Type()
)
frxPortDefaultBridgingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxPortDefaultBridgingMode.setStatus("mandatory")
_FrxVcControlGroup_ObjectIdentity = ObjectIdentity
frxVcControlGroup = _FrxVcControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 2)
)
_FrxVcControlTable_Object = MibTable
frxVcControlTable = _FrxVcControlTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    frxVcControlTable.setStatus("mandatory")
_FrxVcControlEntry_Object = MibTableRow
frxVcControlEntry = _FrxVcControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1)
)
frxVcControlEntry.setIndexNames(
    (0, "XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"),
    (0, "XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"),
    (0, "XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"),
)
if mibBuilder.loadTexts:
    frxVcControlEntry.setStatus("mandatory")


class _FrxVcControlSlotIndex_Type(Integer32):
    """Custom type frxVcControlSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_FrxVcControlSlotIndex_Type.__name__ = "Integer32"
_FrxVcControlSlotIndex_Object = MibTableColumn
frxVcControlSlotIndex = _FrxVcControlSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1, 1),
    _FrxVcControlSlotIndex_Type()
)
frxVcControlSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcControlSlotIndex.setStatus("mandatory")


class _FrxVcControlPortIndex_Type(Integer32):
    """Custom type frxVcControlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_FrxVcControlPortIndex_Type.__name__ = "Integer32"
_FrxVcControlPortIndex_Object = MibTableColumn
frxVcControlPortIndex = _FrxVcControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1, 2),
    _FrxVcControlPortIndex_Type()
)
frxVcControlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcControlPortIndex.setStatus("mandatory")


class _FrxVcControlDlci_Type(Integer32):
    """Custom type frxVcControlDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FrxVcControlDlci_Type.__name__ = "Integer32"
_FrxVcControlDlci_Object = MibTableColumn
frxVcControlDlci = _FrxVcControlDlci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1, 3),
    _FrxVcControlDlci_Type()
)
frxVcControlDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcControlDlci.setStatus("mandatory")


class _FrxVcControlCompressionAdminStatus_Type(Integer32):
    """Custom type frxVcControlCompressionAdminStatus based on Integer32"""
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


_FrxVcControlCompressionAdminStatus_Type.__name__ = "Integer32"
_FrxVcControlCompressionAdminStatus_Object = MibTableColumn
frxVcControlCompressionAdminStatus = _FrxVcControlCompressionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1, 4),
    _FrxVcControlCompressionAdminStatus_Type()
)
frxVcControlCompressionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxVcControlCompressionAdminStatus.setStatus("mandatory")


class _FrxVcControlCompressionOperPhase_Type(Integer32):
    """Custom type frxVcControlCompressionOperPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("initialization", 2),
          ("operation", 3))
    )


_FrxVcControlCompressionOperPhase_Type.__name__ = "Integer32"
_FrxVcControlCompressionOperPhase_Object = MibTableColumn
frxVcControlCompressionOperPhase = _FrxVcControlCompressionOperPhase_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1, 5),
    _FrxVcControlCompressionOperPhase_Type()
)
frxVcControlCompressionOperPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcControlCompressionOperPhase.setStatus("mandatory")


class _FrxVcControlCompressionPRetryTime_Type(Integer32):
    """Custom type frxVcControlCompressionPRetryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrxVcControlCompressionPRetryTime_Type.__name__ = "Integer32"
_FrxVcControlCompressionPRetryTime_Object = MibTableColumn
frxVcControlCompressionPRetryTime = _FrxVcControlCompressionPRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1, 6),
    _FrxVcControlCompressionPRetryTime_Type()
)
frxVcControlCompressionPRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxVcControlCompressionPRetryTime.setStatus("mandatory")


class _FrxVcControlCompressionPRetryCount_Type(Integer32):
    """Custom type frxVcControlCompressionPRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 255),
    )


_FrxVcControlCompressionPRetryCount_Type.__name__ = "Integer32"
_FrxVcControlCompressionPRetryCount_Object = MibTableColumn
frxVcControlCompressionPRetryCount = _FrxVcControlCompressionPRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1, 7),
    _FrxVcControlCompressionPRetryCount_Type()
)
frxVcControlCompressionPRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxVcControlCompressionPRetryCount.setStatus("mandatory")
_FrxVcControlBridgingInUse_Type = Integer32
_FrxVcControlBridgingInUse_Object = MibTableColumn
frxVcControlBridgingInUse = _FrxVcControlBridgingInUse_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1, 8),
    _FrxVcControlBridgingInUse_Type()
)
frxVcControlBridgingInUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxVcControlBridgingInUse.setStatus("mandatory")
_FrxServiceGroup_ObjectIdentity = ObjectIdentity
frxServiceGroup = _FrxServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 3)
)
_FrxServiceTable_Object = MibTable
frxServiceTable = _FrxServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1)
)
if mibBuilder.loadTexts:
    frxServiceTable.setStatus("mandatory")
_FrxServiceEntry_Object = MibTableRow
frxServiceEntry = _FrxServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1)
)
frxServiceEntry.setIndexNames(
    (0, "XYLAN-FRAME-RELAY-MIB", "frxServiceSlotIndex"),
    (0, "XYLAN-FRAME-RELAY-MIB", "frxServicePortIndex"),
    (0, "XYLAN-FRAME-RELAY-MIB", "frxServiceNumber"),
    (0, "XYLAN-FRAME-RELAY-MIB", "frxServiceType"),
)
if mibBuilder.loadTexts:
    frxServiceEntry.setStatus("mandatory")


class _FrxServiceSlotIndex_Type(Integer32):
    """Custom type frxServiceSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_FrxServiceSlotIndex_Type.__name__ = "Integer32"
_FrxServiceSlotIndex_Object = MibTableColumn
frxServiceSlotIndex = _FrxServiceSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 1),
    _FrxServiceSlotIndex_Type()
)
frxServiceSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxServiceSlotIndex.setStatus("mandatory")


class _FrxServicePortIndex_Type(Integer32):
    """Custom type frxServicePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_FrxServicePortIndex_Type.__name__ = "Integer32"
_FrxServicePortIndex_Object = MibTableColumn
frxServicePortIndex = _FrxServicePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 2),
    _FrxServicePortIndex_Type()
)
frxServicePortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxServicePortIndex.setStatus("mandatory")


class _FrxServiceNumber_Type(Integer32):
    """Custom type frxServiceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_FrxServiceNumber_Type.__name__ = "Integer32"
_FrxServiceNumber_Object = MibTableColumn
frxServiceNumber = _FrxServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 3),
    _FrxServiceNumber_Type()
)
frxServiceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxServiceNumber.setStatus("mandatory")


class _FrxServiceTableEntryType_Type(Integer32):
    """Custom type frxServiceTableEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_FrxServiceTableEntryType_Type.__name__ = "Integer32"
_FrxServiceTableEntryType_Object = MibTableColumn
frxServiceTableEntryType = _FrxServiceTableEntryType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 4),
    _FrxServiceTableEntryType_Type()
)
frxServiceTableEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxServiceTableEntryType.setStatus("mandatory")


class _FrxServiceDescription_Type(DisplayString):
    """Custom type frxServiceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FrxServiceDescription_Type.__name__ = "DisplayString"
_FrxServiceDescription_Object = MibTableColumn
frxServiceDescription = _FrxServiceDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 5),
    _FrxServiceDescription_Type()
)
frxServiceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxServiceDescription.setStatus("mandatory")


class _FrxServiceType_Type(Integer32):
    """Custom type frxServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bridging", 6),
          ("routing", 5),
          ("trunking", 4))
    )


_FrxServiceType_Type.__name__ = "Integer32"
_FrxServiceType_Object = MibTableColumn
frxServiceType = _FrxServiceType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 6),
    _FrxServiceType_Type()
)
frxServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxServiceType.setStatus("mandatory")


class _FrxServiceOperStatus_Type(Integer32):
    """Custom type frxServiceOperStatus based on Integer32"""
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


_FrxServiceOperStatus_Type.__name__ = "Integer32"
_FrxServiceOperStatus_Object = MibTableColumn
frxServiceOperStatus = _FrxServiceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 7),
    _FrxServiceOperStatus_Type()
)
frxServiceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxServiceOperStatus.setStatus("mandatory")


class _FrxServiceAdminStatus_Type(Integer32):
    """Custom type frxServiceAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_FrxServiceAdminStatus_Type.__name__ = "Integer32"
_FrxServiceAdminStatus_Object = MibTableColumn
frxServiceAdminStatus = _FrxServiceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 8),
    _FrxServiceAdminStatus_Type()
)
frxServiceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxServiceAdminStatus.setStatus("mandatory")


class _FrxServiceVirtualCircuits_Type(OctetString):
    """Custom type frxServiceVirtualCircuits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_FrxServiceVirtualCircuits_Type.__name__ = "OctetString"
_FrxServiceVirtualCircuits_Object = MibTableColumn
frxServiceVirtualCircuits = _FrxServiceVirtualCircuits_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 9),
    _FrxServiceVirtualCircuits_Type()
)
frxServiceVirtualCircuits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxServiceVirtualCircuits.setStatus("mandatory")


class _FrxServiceVlans_Type(OctetString):
    """Custom type frxServiceVlans based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FrxServiceVlans_Type.__name__ = "OctetString"
_FrxServiceVlans_Object = MibTableColumn
frxServiceVlans = _FrxServiceVlans_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 10),
    _FrxServiceVlans_Type()
)
frxServiceVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxServiceVlans.setStatus("mandatory")


class _FrxServiceBridgingMode_Type(Integer32):
    """Custom type frxServiceBridgingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FrxServiceBridgingMode_Type.__name__ = "Integer32"
_FrxServiceBridgingMode_Object = MibTableColumn
frxServiceBridgingMode = _FrxServiceBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 11),
    _FrxServiceBridgingMode_Type()
)
frxServiceBridgingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxServiceBridgingMode.setStatus("mandatory")
_FrxVcStatsGroup_ObjectIdentity = ObjectIdentity
frxVcStatsGroup = _FrxVcStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4)
)
_FrxVcStatsTable_Object = MibTable
frxVcStatsTable = _FrxVcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1)
)
if mibBuilder.loadTexts:
    frxVcStatsTable.setStatus("mandatory")
_FrxVcStatsEntry_Object = MibTableRow
frxVcStatsEntry = _FrxVcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1)
)
frxVcStatsEntry.setIndexNames(
    (0, "XYLAN-FRAME-RELAY-MIB", "frxVcStatsSlotIndex"),
    (0, "XYLAN-FRAME-RELAY-MIB", "frxVcStatsPortIndex"),
    (0, "XYLAN-FRAME-RELAY-MIB", "frxVcStatsDlci"),
)
if mibBuilder.loadTexts:
    frxVcStatsEntry.setStatus("mandatory")


class _FrxVcStatsSlotIndex_Type(Integer32):
    """Custom type frxVcStatsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_FrxVcStatsSlotIndex_Type.__name__ = "Integer32"
_FrxVcStatsSlotIndex_Object = MibTableColumn
frxVcStatsSlotIndex = _FrxVcStatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 1),
    _FrxVcStatsSlotIndex_Type()
)
frxVcStatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsSlotIndex.setStatus("mandatory")


class _FrxVcStatsPortIndex_Type(Integer32):
    """Custom type frxVcStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_FrxVcStatsPortIndex_Type.__name__ = "Integer32"
_FrxVcStatsPortIndex_Object = MibTableColumn
frxVcStatsPortIndex = _FrxVcStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 2),
    _FrxVcStatsPortIndex_Type()
)
frxVcStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsPortIndex.setStatus("mandatory")


class _FrxVcStatsDlci_Type(Integer32):
    """Custom type frxVcStatsDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_FrxVcStatsDlci_Type.__name__ = "Integer32"
_FrxVcStatsDlci_Object = MibTableColumn
frxVcStatsDlci = _FrxVcStatsDlci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 3),
    _FrxVcStatsDlci_Type()
)
frxVcStatsDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsDlci.setStatus("mandatory")
_FrxVcStatsTxIPOctets_Type = Counter32
_FrxVcStatsTxIPOctets_Object = MibTableColumn
frxVcStatsTxIPOctets = _FrxVcStatsTxIPOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 4),
    _FrxVcStatsTxIPOctets_Type()
)
frxVcStatsTxIPOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsTxIPOctets.setStatus("mandatory")
_FrxVcStatsTxIPFrames_Type = Counter32
_FrxVcStatsTxIPFrames_Object = MibTableColumn
frxVcStatsTxIPFrames = _FrxVcStatsTxIPFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 5),
    _FrxVcStatsTxIPFrames_Type()
)
frxVcStatsTxIPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsTxIPFrames.setStatus("mandatory")
_FrxVcStatsRxIPOctets_Type = Counter32
_FrxVcStatsRxIPOctets_Object = MibTableColumn
frxVcStatsRxIPOctets = _FrxVcStatsRxIPOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 6),
    _FrxVcStatsRxIPOctets_Type()
)
frxVcStatsRxIPOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsRxIPOctets.setStatus("mandatory")
_FrxVcStatsRxIPFrames_Type = Counter32
_FrxVcStatsRxIPFrames_Object = MibTableColumn
frxVcStatsRxIPFrames = _FrxVcStatsRxIPFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 7),
    _FrxVcStatsRxIPFrames_Type()
)
frxVcStatsRxIPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsRxIPFrames.setStatus("mandatory")
_FrxVcStatsTxIPXOctets_Type = Counter32
_FrxVcStatsTxIPXOctets_Object = MibTableColumn
frxVcStatsTxIPXOctets = _FrxVcStatsTxIPXOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 8),
    _FrxVcStatsTxIPXOctets_Type()
)
frxVcStatsTxIPXOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsTxIPXOctets.setStatus("mandatory")
_FrxVcStatsTxIPXFrames_Type = Counter32
_FrxVcStatsTxIPXFrames_Object = MibTableColumn
frxVcStatsTxIPXFrames = _FrxVcStatsTxIPXFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 9),
    _FrxVcStatsTxIPXFrames_Type()
)
frxVcStatsTxIPXFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsTxIPXFrames.setStatus("mandatory")
_FrxVcStatsRxIPXOctets_Type = Counter32
_FrxVcStatsRxIPXOctets_Object = MibTableColumn
frxVcStatsRxIPXOctets = _FrxVcStatsRxIPXOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 10),
    _FrxVcStatsRxIPXOctets_Type()
)
frxVcStatsRxIPXOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsRxIPXOctets.setStatus("mandatory")
_FrxVcStatsRxIPXFrames_Type = Counter32
_FrxVcStatsRxIPXFrames_Object = MibTableColumn
frxVcStatsRxIPXFrames = _FrxVcStatsRxIPXFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 11),
    _FrxVcStatsRxIPXFrames_Type()
)
frxVcStatsRxIPXFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsRxIPXFrames.setStatus("mandatory")
_FrxVcStatsTxBPDUOctets_Type = Counter32
_FrxVcStatsTxBPDUOctets_Object = MibTableColumn
frxVcStatsTxBPDUOctets = _FrxVcStatsTxBPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 12),
    _FrxVcStatsTxBPDUOctets_Type()
)
frxVcStatsTxBPDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsTxBPDUOctets.setStatus("mandatory")
_FrxVcStatsTxBPDUFrames_Type = Counter32
_FrxVcStatsTxBPDUFrames_Object = MibTableColumn
frxVcStatsTxBPDUFrames = _FrxVcStatsTxBPDUFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 13),
    _FrxVcStatsTxBPDUFrames_Type()
)
frxVcStatsTxBPDUFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsTxBPDUFrames.setStatus("mandatory")
_FrxVcStatsRxBPDUOctets_Type = Counter32
_FrxVcStatsRxBPDUOctets_Object = MibTableColumn
frxVcStatsRxBPDUOctets = _FrxVcStatsRxBPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 14),
    _FrxVcStatsRxBPDUOctets_Type()
)
frxVcStatsRxBPDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsRxBPDUOctets.setStatus("mandatory")
_FrxVcStatsRxBPDUFrames_Type = Counter32
_FrxVcStatsRxBPDUFrames_Object = MibTableColumn
frxVcStatsRxBPDUFrames = _FrxVcStatsRxBPDUFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 15),
    _FrxVcStatsRxBPDUFrames_Type()
)
frxVcStatsRxBPDUFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsRxBPDUFrames.setStatus("mandatory")
_FrxVcStatsTxEthernetOctets_Type = Counter32
_FrxVcStatsTxEthernetOctets_Object = MibTableColumn
frxVcStatsTxEthernetOctets = _FrxVcStatsTxEthernetOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 16),
    _FrxVcStatsTxEthernetOctets_Type()
)
frxVcStatsTxEthernetOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsTxEthernetOctets.setStatus("mandatory")
_FrxVcStatsTxEthernetFrames_Type = Counter32
_FrxVcStatsTxEthernetFrames_Object = MibTableColumn
frxVcStatsTxEthernetFrames = _FrxVcStatsTxEthernetFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 17),
    _FrxVcStatsTxEthernetFrames_Type()
)
frxVcStatsTxEthernetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsTxEthernetFrames.setStatus("mandatory")
_FrxVcStatsRxEthernetOctets_Type = Counter32
_FrxVcStatsRxEthernetOctets_Object = MibTableColumn
frxVcStatsRxEthernetOctets = _FrxVcStatsRxEthernetOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 18),
    _FrxVcStatsRxEthernetOctets_Type()
)
frxVcStatsRxEthernetOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsRxEthernetOctets.setStatus("mandatory")
_FrxVcStatsRxEthernetFrames_Type = Counter32
_FrxVcStatsRxEthernetFrames_Object = MibTableColumn
frxVcStatsRxEthernetFrames = _FrxVcStatsRxEthernetFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 19),
    _FrxVcStatsRxEthernetFrames_Type()
)
frxVcStatsRxEthernetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsRxEthernetFrames.setStatus("mandatory")
_FrxVcStatsTx8025Octets_Type = Counter32
_FrxVcStatsTx8025Octets_Object = MibTableColumn
frxVcStatsTx8025Octets = _FrxVcStatsTx8025Octets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 20),
    _FrxVcStatsTx8025Octets_Type()
)
frxVcStatsTx8025Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsTx8025Octets.setStatus("mandatory")
_FrxVcStatsTx8025Frames_Type = Counter32
_FrxVcStatsTx8025Frames_Object = MibTableColumn
frxVcStatsTx8025Frames = _FrxVcStatsTx8025Frames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 21),
    _FrxVcStatsTx8025Frames_Type()
)
frxVcStatsTx8025Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsTx8025Frames.setStatus("mandatory")
_FrxVcStatsRx8025Octets_Type = Counter32
_FrxVcStatsRx8025Octets_Object = MibTableColumn
frxVcStatsRx8025Octets = _FrxVcStatsRx8025Octets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 22),
    _FrxVcStatsRx8025Octets_Type()
)
frxVcStatsRx8025Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsRx8025Octets.setStatus("mandatory")
_FrxVcStatsRx8025Frames_Type = Counter32
_FrxVcStatsRx8025Frames_Object = MibTableColumn
frxVcStatsRx8025Frames = _FrxVcStatsRx8025Frames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 23),
    _FrxVcStatsRx8025Frames_Type()
)
frxVcStatsRx8025Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsRx8025Frames.setStatus("mandatory")
_FrxVcStatsTxFDDIOctets_Type = Counter32
_FrxVcStatsTxFDDIOctets_Object = MibTableColumn
frxVcStatsTxFDDIOctets = _FrxVcStatsTxFDDIOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 24),
    _FrxVcStatsTxFDDIOctets_Type()
)
frxVcStatsTxFDDIOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsTxFDDIOctets.setStatus("mandatory")
_FrxVcStatsTxFDDIFrames_Type = Counter32
_FrxVcStatsTxFDDIFrames_Object = MibTableColumn
frxVcStatsTxFDDIFrames = _FrxVcStatsTxFDDIFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 25),
    _FrxVcStatsTxFDDIFrames_Type()
)
frxVcStatsTxFDDIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsTxFDDIFrames.setStatus("mandatory")
_FrxVcStatsRxFDDIOctets_Type = Counter32
_FrxVcStatsRxFDDIOctets_Object = MibTableColumn
frxVcStatsRxFDDIOctets = _FrxVcStatsRxFDDIOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 26),
    _FrxVcStatsRxFDDIOctets_Type()
)
frxVcStatsRxFDDIOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsRxFDDIOctets.setStatus("mandatory")
_FrxVcStatsRxFDDIFrames_Type = Counter32
_FrxVcStatsRxFDDIFrames_Object = MibTableColumn
frxVcStatsRxFDDIFrames = _FrxVcStatsRxFDDIFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 27),
    _FrxVcStatsRxFDDIFrames_Type()
)
frxVcStatsRxFDDIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsRxFDDIFrames.setStatus("mandatory")
_FrxVcStatsTxCompressedOctets_Type = Counter32
_FrxVcStatsTxCompressedOctets_Object = MibTableColumn
frxVcStatsTxCompressedOctets = _FrxVcStatsTxCompressedOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 28),
    _FrxVcStatsTxCompressedOctets_Type()
)
frxVcStatsTxCompressedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsTxCompressedOctets.setStatus("mandatory")
_FrxVcStatsTxCompressedFrames_Type = Counter32
_FrxVcStatsTxCompressedFrames_Object = MibTableColumn
frxVcStatsTxCompressedFrames = _FrxVcStatsTxCompressedFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 29),
    _FrxVcStatsTxCompressedFrames_Type()
)
frxVcStatsTxCompressedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsTxCompressedFrames.setStatus("mandatory")
_FrxVcStatsRxCompressedOctets_Type = Counter32
_FrxVcStatsRxCompressedOctets_Object = MibTableColumn
frxVcStatsRxCompressedOctets = _FrxVcStatsRxCompressedOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 30),
    _FrxVcStatsRxCompressedOctets_Type()
)
frxVcStatsRxCompressedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsRxCompressedOctets.setStatus("mandatory")
_FrxVcStatsRxCompressedFrames_Type = Counter32
_FrxVcStatsRxCompressedFrames_Object = MibTableColumn
frxVcStatsRxCompressedFrames = _FrxVcStatsRxCompressedFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 31),
    _FrxVcStatsRxCompressedFrames_Type()
)
frxVcStatsRxCompressedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsRxCompressedFrames.setStatus("mandatory")
_FrxVcStatsTxPrecompressedOctets_Type = Counter32
_FrxVcStatsTxPrecompressedOctets_Object = MibTableColumn
frxVcStatsTxPrecompressedOctets = _FrxVcStatsTxPrecompressedOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 32),
    _FrxVcStatsTxPrecompressedOctets_Type()
)
frxVcStatsTxPrecompressedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsTxPrecompressedOctets.setStatus("mandatory")
_FrxVcStatsRxDecompressedOctets_Type = Counter32
_FrxVcStatsRxDecompressedOctets_Object = MibTableColumn
frxVcStatsRxDecompressedOctets = _FrxVcStatsRxDecompressedOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 33),
    _FrxVcStatsRxDecompressedOctets_Type()
)
frxVcStatsRxDecompressedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsRxDecompressedOctets.setStatus("mandatory")
_FrxVcStatsRxCompressedDiscards_Type = Counter32
_FrxVcStatsRxCompressedDiscards_Object = MibTableColumn
frxVcStatsRxCompressedDiscards = _FrxVcStatsRxCompressedDiscards_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 34),
    _FrxVcStatsRxCompressedDiscards_Type()
)
frxVcStatsRxCompressedDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxVcStatsRxCompressedDiscards.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-FRAME-RELAY-MIB",
    **{"frxPortGroup": frxPortGroup,
       "frxPortTable": frxPortTable,
       "frxPortEntry": frxPortEntry,
       "frxPortSlotIndex": frxPortSlotIndex,
       "frxPortPortIndex": frxPortPortIndex,
       "frxPortDescription": frxPortDescription,
       "frxPortDefaultBridgingVLAN": frxPortDefaultBridgingVLAN,
       "frxPortDefaultBridgingServiceNumber": frxPortDefaultBridgingServiceNumber,
       "frxPortDefaultRoutingVLAN": frxPortDefaultRoutingVLAN,
       "frxPortDefaultCompressionAdminStatus": frxPortDefaultCompressionAdminStatus,
       "frxPortDefaultCompressionPRetryTime": frxPortDefaultCompressionPRetryTime,
       "frxPortDefaultCompressionPRetryCount": frxPortDefaultCompressionPRetryCount,
       "frxPortDefaultBridgingMode": frxPortDefaultBridgingMode,
       "frxVcControlGroup": frxVcControlGroup,
       "frxVcControlTable": frxVcControlTable,
       "frxVcControlEntry": frxVcControlEntry,
       "frxVcControlSlotIndex": frxVcControlSlotIndex,
       "frxVcControlPortIndex": frxVcControlPortIndex,
       "frxVcControlDlci": frxVcControlDlci,
       "frxVcControlCompressionAdminStatus": frxVcControlCompressionAdminStatus,
       "frxVcControlCompressionOperPhase": frxVcControlCompressionOperPhase,
       "frxVcControlCompressionPRetryTime": frxVcControlCompressionPRetryTime,
       "frxVcControlCompressionPRetryCount": frxVcControlCompressionPRetryCount,
       "frxVcControlBridgingInUse": frxVcControlBridgingInUse,
       "frxServiceGroup": frxServiceGroup,
       "frxServiceTable": frxServiceTable,
       "frxServiceEntry": frxServiceEntry,
       "frxServiceSlotIndex": frxServiceSlotIndex,
       "frxServicePortIndex": frxServicePortIndex,
       "frxServiceNumber": frxServiceNumber,
       "frxServiceTableEntryType": frxServiceTableEntryType,
       "frxServiceDescription": frxServiceDescription,
       "frxServiceType": frxServiceType,
       "frxServiceOperStatus": frxServiceOperStatus,
       "frxServiceAdminStatus": frxServiceAdminStatus,
       "frxServiceVirtualCircuits": frxServiceVirtualCircuits,
       "frxServiceVlans": frxServiceVlans,
       "frxServiceBridgingMode": frxServiceBridgingMode,
       "frxVcStatsGroup": frxVcStatsGroup,
       "frxVcStatsTable": frxVcStatsTable,
       "frxVcStatsEntry": frxVcStatsEntry,
       "frxVcStatsSlotIndex": frxVcStatsSlotIndex,
       "frxVcStatsPortIndex": frxVcStatsPortIndex,
       "frxVcStatsDlci": frxVcStatsDlci,
       "frxVcStatsTxIPOctets": frxVcStatsTxIPOctets,
       "frxVcStatsTxIPFrames": frxVcStatsTxIPFrames,
       "frxVcStatsRxIPOctets": frxVcStatsRxIPOctets,
       "frxVcStatsRxIPFrames": frxVcStatsRxIPFrames,
       "frxVcStatsTxIPXOctets": frxVcStatsTxIPXOctets,
       "frxVcStatsTxIPXFrames": frxVcStatsTxIPXFrames,
       "frxVcStatsRxIPXOctets": frxVcStatsRxIPXOctets,
       "frxVcStatsRxIPXFrames": frxVcStatsRxIPXFrames,
       "frxVcStatsTxBPDUOctets": frxVcStatsTxBPDUOctets,
       "frxVcStatsTxBPDUFrames": frxVcStatsTxBPDUFrames,
       "frxVcStatsRxBPDUOctets": frxVcStatsRxBPDUOctets,
       "frxVcStatsRxBPDUFrames": frxVcStatsRxBPDUFrames,
       "frxVcStatsTxEthernetOctets": frxVcStatsTxEthernetOctets,
       "frxVcStatsTxEthernetFrames": frxVcStatsTxEthernetFrames,
       "frxVcStatsRxEthernetOctets": frxVcStatsRxEthernetOctets,
       "frxVcStatsRxEthernetFrames": frxVcStatsRxEthernetFrames,
       "frxVcStatsTx8025Octets": frxVcStatsTx8025Octets,
       "frxVcStatsTx8025Frames": frxVcStatsTx8025Frames,
       "frxVcStatsRx8025Octets": frxVcStatsRx8025Octets,
       "frxVcStatsRx8025Frames": frxVcStatsRx8025Frames,
       "frxVcStatsTxFDDIOctets": frxVcStatsTxFDDIOctets,
       "frxVcStatsTxFDDIFrames": frxVcStatsTxFDDIFrames,
       "frxVcStatsRxFDDIOctets": frxVcStatsRxFDDIOctets,
       "frxVcStatsRxFDDIFrames": frxVcStatsRxFDDIFrames,
       "frxVcStatsTxCompressedOctets": frxVcStatsTxCompressedOctets,
       "frxVcStatsTxCompressedFrames": frxVcStatsTxCompressedFrames,
       "frxVcStatsRxCompressedOctets": frxVcStatsRxCompressedOctets,
       "frxVcStatsRxCompressedFrames": frxVcStatsRxCompressedFrames,
       "frxVcStatsTxPrecompressedOctets": frxVcStatsTxPrecompressedOctets,
       "frxVcStatsRxDecompressedOctets": frxVcStatsRxDecompressedOctets,
       "frxVcStatsRxCompressedDiscards": frxVcStatsRxCompressedDiscards}
)
