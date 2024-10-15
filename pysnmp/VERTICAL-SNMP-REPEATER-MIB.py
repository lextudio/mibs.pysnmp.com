# SNMP MIB module (VERTICAL-SNMP-REPEATER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERTICAL-SNMP-REPEATER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:24 2024
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

(OwnerString,) = mibBuilder.importSymbols(
    "RFC1271-MIB",
    "OwnerString")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(vertical,) = mibBuilder.importSymbols(
    "VERTICALT1-E1-MIB",
    "vertical")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VsnmpDot3RptrMgt_ObjectIdentity = ObjectIdentity
vsnmpDot3RptrMgt = _VsnmpDot3RptrMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 4)
)
_VrptrBasicPackage_ObjectIdentity = ObjectIdentity
vrptrBasicPackage = _VrptrBasicPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1)
)
_VrptrGroupInfo_ObjectIdentity = ObjectIdentity
vrptrGroupInfo = _VrptrGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 2)
)
_VrptrGroupTable_Object = MibTable
vrptrGroupTable = _VrptrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vrptrGroupTable.setStatus("mandatory")
_VrptrGroupEntry_Object = MibTableRow
vrptrGroupEntry = _VrptrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 2, 1, 1)
)
vrptrGroupEntry.setIndexNames(
    (0, "VERTICAL-SNMP-REPEATER-MIB", "vrptrGroupIndex"),
)
if mibBuilder.loadTexts:
    vrptrGroupEntry.setStatus("mandatory")


class _VrptrGroupIndex_Type(Integer32):
    """Custom type vrptrGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VrptrGroupIndex_Type.__name__ = "Integer32"
_VrptrGroupIndex_Object = MibTableColumn
vrptrGroupIndex = _VrptrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 2, 1, 1, 1),
    _VrptrGroupIndex_Type()
)
vrptrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrGroupIndex.setStatus("mandatory")
_VrptrGroupObjectID_Type = ObjectIdentifier
_VrptrGroupObjectID_Object = MibTableColumn
vrptrGroupObjectID = _VrptrGroupObjectID_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 2, 1, 1, 3),
    _VrptrGroupObjectID_Type()
)
vrptrGroupObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrGroupObjectID.setStatus("mandatory")


class _VrptrGroupOperStatus_Type(Integer32):
    """Custom type vrptrGroupOperStatus based on Integer32"""
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
        *(("malfunctioning", 3),
          ("notPresent", 4),
          ("operational", 2),
          ("other", 1),
          ("resetInProgress", 6),
          ("underTest", 5))
    )


_VrptrGroupOperStatus_Type.__name__ = "Integer32"
_VrptrGroupOperStatus_Object = MibTableColumn
vrptrGroupOperStatus = _VrptrGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 2, 1, 1, 4),
    _VrptrGroupOperStatus_Type()
)
vrptrGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrGroupOperStatus.setStatus("mandatory")


class _VrptrGroupPortCapacity_Type(Integer32):
    """Custom type vrptrGroupPortCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VrptrGroupPortCapacity_Type.__name__ = "Integer32"
_VrptrGroupPortCapacity_Object = MibTableColumn
vrptrGroupPortCapacity = _VrptrGroupPortCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 2, 1, 1, 6),
    _VrptrGroupPortCapacity_Type()
)
vrptrGroupPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrGroupPortCapacity.setStatus("mandatory")


class _VrptrGroupSlotNumber_Type(Integer32):
    """Custom type vrptrGroupSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_VrptrGroupSlotNumber_Type.__name__ = "Integer32"
_VrptrGroupSlotNumber_Object = MibTableColumn
vrptrGroupSlotNumber = _VrptrGroupSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 2, 1, 1, 7),
    _VrptrGroupSlotNumber_Type()
)
vrptrGroupSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrGroupSlotNumber.setStatus("mandatory")


class _VrptrGroupBroadcastDomainNumber_Type(Integer32):
    """Custom type vrptrGroupBroadcastDomainNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_VrptrGroupBroadcastDomainNumber_Type.__name__ = "Integer32"
_VrptrGroupBroadcastDomainNumber_Object = MibTableColumn
vrptrGroupBroadcastDomainNumber = _VrptrGroupBroadcastDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 2, 1, 1, 8),
    _VrptrGroupBroadcastDomainNumber_Type()
)
vrptrGroupBroadcastDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrGroupBroadcastDomainNumber.setStatus("mandatory")


class _VrptrGroupNetworkAdapterNumber_Type(Integer32):
    """Custom type vrptrGroupNetworkAdapterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrptrGroupNetworkAdapterNumber_Type.__name__ = "Integer32"
_VrptrGroupNetworkAdapterNumber_Object = MibTableColumn
vrptrGroupNetworkAdapterNumber = _VrptrGroupNetworkAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 2, 1, 1, 9),
    _VrptrGroupNetworkAdapterNumber_Type()
)
vrptrGroupNetworkAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrGroupNetworkAdapterNumber.setStatus("mandatory")


class _VrptrGroupLedStatus_Type(Integer32):
    """Custom type vrptrGroupLedStatus based on Integer32"""
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
        *(("green", 3),
          ("greenRed", 5),
          ("none", 2),
          ("red", 4),
          ("unknown", 1))
    )


_VrptrGroupLedStatus_Type.__name__ = "Integer32"
_VrptrGroupLedStatus_Object = MibTableColumn
vrptrGroupLedStatus = _VrptrGroupLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 2, 1, 1, 10),
    _VrptrGroupLedStatus_Type()
)
vrptrGroupLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrGroupLedStatus.setStatus("mandatory")


class _VrptrGroupExternalPortCapacity_Type(Integer32):
    """Custom type vrptrGroupExternalPortCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VrptrGroupExternalPortCapacity_Type.__name__ = "Integer32"
_VrptrGroupExternalPortCapacity_Object = MibScalar
vrptrGroupExternalPortCapacity = _VrptrGroupExternalPortCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 2, 1, 1, 11),
    _VrptrGroupExternalPortCapacity_Type()
)
vrptrGroupExternalPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrGroupExternalPortCapacity.setStatus("mandatory")
_VrptrPortInfo_ObjectIdentity = ObjectIdentity
vrptrPortInfo = _VrptrPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 3)
)
_VrptrPortTable_Object = MibTable
vrptrPortTable = _VrptrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    vrptrPortTable.setStatus("mandatory")
_VrptrPortEntry_Object = MibTableRow
vrptrPortEntry = _VrptrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 3, 1, 1)
)
vrptrPortEntry.setIndexNames(
    (0, "VERTICAL-SNMP-REPEATER-MIB", "vrptrPortGroupIndex"),
    (0, "VERTICAL-SNMP-REPEATER-MIB", "vrptrPortIndex"),
)
if mibBuilder.loadTexts:
    vrptrPortEntry.setStatus("mandatory")


class _VrptrPortGroupIndex_Type(Integer32):
    """Custom type vrptrPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VrptrPortGroupIndex_Type.__name__ = "Integer32"
_VrptrPortGroupIndex_Object = MibTableColumn
vrptrPortGroupIndex = _VrptrPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 3, 1, 1, 1),
    _VrptrPortGroupIndex_Type()
)
vrptrPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrPortGroupIndex.setStatus("mandatory")


class _VrptrPortIndex_Type(Integer32):
    """Custom type vrptrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VrptrPortIndex_Type.__name__ = "Integer32"
_VrptrPortIndex_Object = MibTableColumn
vrptrPortIndex = _VrptrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 3, 1, 1, 2),
    _VrptrPortIndex_Type()
)
vrptrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrPortIndex.setStatus("mandatory")


class _VrptrPortAdminStatus_Type(Integer32):
    """Custom type vrptrPortAdminStatus based on Integer32"""
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


_VrptrPortAdminStatus_Type.__name__ = "Integer32"
_VrptrPortAdminStatus_Object = MibTableColumn
vrptrPortAdminStatus = _VrptrPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 3, 1, 1, 3),
    _VrptrPortAdminStatus_Type()
)
vrptrPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrptrPortAdminStatus.setStatus("mandatory")


class _VrptrPortAutoPartitionState_Type(Integer32):
    """Custom type vrptrPortAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoPartitioned", 2),
          ("notAutoPartitioned", 1))
    )


_VrptrPortAutoPartitionState_Type.__name__ = "Integer32"
_VrptrPortAutoPartitionState_Object = MibTableColumn
vrptrPortAutoPartitionState = _VrptrPortAutoPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 3, 1, 1, 4),
    _VrptrPortAutoPartitionState_Type()
)
vrptrPortAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrPortAutoPartitionState.setStatus("mandatory")


class _VrptrPortOperStatus_Type(Integer32):
    """Custom type vrptrPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 2),
          ("notPresent", 3),
          ("operational", 1))
    )


_VrptrPortOperStatus_Type.__name__ = "Integer32"
_VrptrPortOperStatus_Object = MibTableColumn
vrptrPortOperStatus = _VrptrPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 3, 1, 1, 5),
    _VrptrPortOperStatus_Type()
)
vrptrPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrPortOperStatus.setStatus("mandatory")


class _VrptrPortRptrId_Type(Integer32):
    """Custom type vrptrPortRptrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VrptrPortRptrId_Type.__name__ = "Integer32"
_VrptrPortRptrId_Object = MibTableColumn
vrptrPortRptrId = _VrptrPortRptrId_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 3, 1, 1, 6),
    _VrptrPortRptrId_Type()
)
vrptrPortRptrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrPortRptrId.setStatus("mandatory")


class _VrptrPortLinkState_Type(Integer32):
    """Custom type vrptrPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("noLink", 2))
    )


_VrptrPortLinkState_Type.__name__ = "Integer32"
_VrptrPortLinkState_Object = MibTableColumn
vrptrPortLinkState = _VrptrPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 3, 1, 1, 7),
    _VrptrPortLinkState_Type()
)
vrptrPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrPortLinkState.setStatus("mandatory")


class _VrptrPortSpeed_Type(Integer32):
    """Custom type vrptrPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mbps-10", 2),
          ("mbps-100", 3),
          ("unknown", 1))
    )


_VrptrPortSpeed_Type.__name__ = "Integer32"
_VrptrPortSpeed_Object = MibTableColumn
vrptrPortSpeed = _VrptrPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 3, 1, 1, 8),
    _VrptrPortSpeed_Type()
)
vrptrPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrPortSpeed.setStatus("mandatory")


class _VrptrPortSpeedSelect_Type(Integer32):
    """Custom type vrptrPortSpeedSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed-select-10", 2),
          ("speed-select-100", 3),
          ("speed-select-auto", 1))
    )


_VrptrPortSpeedSelect_Type.__name__ = "Integer32"
_VrptrPortSpeedSelect_Object = MibTableColumn
vrptrPortSpeedSelect = _VrptrPortSpeedSelect_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 3, 1, 1, 9),
    _VrptrPortSpeedSelect_Type()
)
vrptrPortSpeedSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrPortSpeedSelect.setStatus("mandatory")


class _VrptrPortDuplex_Type(Integer32):
    """Custom type vrptrPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("half", 2),
          ("unknown", 1))
    )


_VrptrPortDuplex_Type.__name__ = "Integer32"
_VrptrPortDuplex_Object = MibTableColumn
vrptrPortDuplex = _VrptrPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 3, 1, 1, 10),
    _VrptrPortDuplex_Type()
)
vrptrPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrPortDuplex.setStatus("mandatory")


class _VrptrPortDuplexSelect_Type(Integer32):
    """Custom type vrptrPortDuplexSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("duplex-select-auto", 1),
          ("duplex-select-full", 3),
          ("duplex-select-half", 2))
    )


_VrptrPortDuplexSelect_Type.__name__ = "Integer32"
_VrptrPortDuplexSelect_Object = MibTableColumn
vrptrPortDuplexSelect = _VrptrPortDuplexSelect_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 3, 1, 1, 11),
    _VrptrPortDuplexSelect_Type()
)
vrptrPortDuplexSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrPortDuplexSelect.setStatus("mandatory")


class _VrptrPortPolarity_Type(Integer32):
    """Custom type vrptrPortPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossed", 3),
          ("straight", 2),
          ("unknown", 1))
    )


_VrptrPortPolarity_Type.__name__ = "Integer32"
_VrptrPortPolarity_Object = MibTableColumn
vrptrPortPolarity = _VrptrPortPolarity_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 3, 1, 1, 12),
    _VrptrPortPolarity_Type()
)
vrptrPortPolarity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrPortPolarity.setStatus("mandatory")
_VrptrAllRptrInfo_ObjectIdentity = ObjectIdentity
vrptrAllRptrInfo = _VrptrAllRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 4)
)
_VrptrInfoTable_Object = MibTable
vrptrInfoTable = _VrptrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    vrptrInfoTable.setStatus("mandatory")
_VrptrInfoEntry_Object = MibTableRow
vrptrInfoEntry = _VrptrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 4, 1, 1)
)
vrptrInfoEntry.setIndexNames(
    (0, "VERTICAL-SNMP-REPEATER-MIB", "vrptrInfoId"),
)
if mibBuilder.loadTexts:
    vrptrInfoEntry.setStatus("mandatory")


class _VrptrInfoId_Type(Integer32):
    """Custom type vrptrInfoId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VrptrInfoId_Type.__name__ = "Integer32"
_VrptrInfoId_Object = MibTableColumn
vrptrInfoId = _VrptrInfoId_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 4, 1, 1, 1),
    _VrptrInfoId_Type()
)
vrptrInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrInfoId.setStatus("mandatory")


class _VrptrInfoRptrType_Type(Integer32):
    """Custom type vrptrInfoRptrType based on Integer32"""
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
        *(("onehundredMbClassI", 3),
          ("onehundredMbClassII", 4),
          ("other", 1),
          ("tenMb", 2),
          ("tenMbOrOnehundredMb", 5))
    )


_VrptrInfoRptrType_Type.__name__ = "Integer32"
_VrptrInfoRptrType_Object = MibTableColumn
vrptrInfoRptrType = _VrptrInfoRptrType_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 4, 1, 1, 2),
    _VrptrInfoRptrType_Type()
)
vrptrInfoRptrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrInfoRptrType.setStatus("mandatory")


class _VrptrInfoOperStatus_Type(Integer32):
    """Custom type vrptrInfoOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("ok", 2),
          ("other", 1))
    )


_VrptrInfoOperStatus_Type.__name__ = "Integer32"
_VrptrInfoOperStatus_Object = MibTableColumn
vrptrInfoOperStatus = _VrptrInfoOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 4, 1, 1, 3),
    _VrptrInfoOperStatus_Type()
)
vrptrInfoOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrInfoOperStatus.setStatus("mandatory")


class _VrptrInfoReset_Type(Integer32):
    """Custom type vrptrInfoReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_VrptrInfoReset_Type.__name__ = "Integer32"
_VrptrInfoReset_Object = MibTableColumn
vrptrInfoReset = _VrptrInfoReset_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 4, 1, 1, 4),
    _VrptrInfoReset_Type()
)
vrptrInfoReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrptrInfoReset.setStatus("mandatory")
_VrptrInfoPartitionedPorts_Type = Gauge32
_VrptrInfoPartitionedPorts_Object = MibTableColumn
vrptrInfoPartitionedPorts = _VrptrInfoPartitionedPorts_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 4, 1, 1, 5),
    _VrptrInfoPartitionedPorts_Type()
)
vrptrInfoPartitionedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrInfoPartitionedPorts.setStatus("mandatory")
_VrptrInfoLastChange_Type = TimeTicks
_VrptrInfoLastChange_Object = MibTableColumn
vrptrInfoLastChange = _VrptrInfoLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 1, 4, 1, 1, 6),
    _VrptrInfoLastChange_Type()
)
vrptrInfoLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrInfoLastChange.setStatus("mandatory")
_VrptrMonitorPackage_ObjectIdentity = ObjectIdentity
vrptrMonitorPackage = _VrptrMonitorPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2)
)
_VrptrMonitorPortInfo_ObjectIdentity = ObjectIdentity
vrptrMonitorPortInfo = _VrptrMonitorPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3)
)
_VrptrMonitorPortTable_Object = MibTable
vrptrMonitorPortTable = _VrptrMonitorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    vrptrMonitorPortTable.setStatus("mandatory")
_VrptrMonitorPortEntry_Object = MibTableRow
vrptrMonitorPortEntry = _VrptrMonitorPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1)
)
vrptrMonitorPortEntry.setIndexNames(
    (0, "VERTICAL-SNMP-REPEATER-MIB", "vrptrMonitorPortGroupIndex"),
    (0, "VERTICAL-SNMP-REPEATER-MIB", "vrptrMonitorPortIndex"),
)
if mibBuilder.loadTexts:
    vrptrMonitorPortEntry.setStatus("mandatory")


class _VrptrMonitorPortGroupIndex_Type(Integer32):
    """Custom type vrptrMonitorPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VrptrMonitorPortGroupIndex_Type.__name__ = "Integer32"
_VrptrMonitorPortGroupIndex_Object = MibTableColumn
vrptrMonitorPortGroupIndex = _VrptrMonitorPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 1),
    _VrptrMonitorPortGroupIndex_Type()
)
vrptrMonitorPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortGroupIndex.setStatus("mandatory")


class _VrptrMonitorPortIndex_Type(Integer32):
    """Custom type vrptrMonitorPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VrptrMonitorPortIndex_Type.__name__ = "Integer32"
_VrptrMonitorPortIndex_Object = MibTableColumn
vrptrMonitorPortIndex = _VrptrMonitorPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 2),
    _VrptrMonitorPortIndex_Type()
)
vrptrMonitorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortIndex.setStatus("mandatory")
_VrptrMonitorPortReadableFrames_Type = Counter32
_VrptrMonitorPortReadableFrames_Object = MibTableColumn
vrptrMonitorPortReadableFrames = _VrptrMonitorPortReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 3),
    _VrptrMonitorPortReadableFrames_Type()
)
vrptrMonitorPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortReadableFrames.setStatus("mandatory")


class _VrptrMonitorPortReadableOctets_Type(Integer32):
    """Custom type vrptrMonitorPortReadableOctets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", -1),
          ("supported", 0))
    )


_VrptrMonitorPortReadableOctets_Type.__name__ = "Integer32"
_VrptrMonitorPortReadableOctets_Object = MibTableColumn
vrptrMonitorPortReadableOctets = _VrptrMonitorPortReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 4),
    _VrptrMonitorPortReadableOctets_Type()
)
vrptrMonitorPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortReadableOctets.setStatus("mandatory")


class _VrptrMonitorPortFCSErrors_Type(Integer32):
    """Custom type vrptrMonitorPortFCSErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", -1),
          ("supported", 0))
    )


_VrptrMonitorPortFCSErrors_Type.__name__ = "Integer32"
_VrptrMonitorPortFCSErrors_Object = MibTableColumn
vrptrMonitorPortFCSErrors = _VrptrMonitorPortFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 5),
    _VrptrMonitorPortFCSErrors_Type()
)
vrptrMonitorPortFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortFCSErrors.setStatus("mandatory")


class _VrptrMonitorPortAlignmentErrors_Type(Integer32):
    """Custom type vrptrMonitorPortAlignmentErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", -1),
          ("supported", 0))
    )


_VrptrMonitorPortAlignmentErrors_Type.__name__ = "Integer32"
_VrptrMonitorPortAlignmentErrors_Object = MibTableColumn
vrptrMonitorPortAlignmentErrors = _VrptrMonitorPortAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 6),
    _VrptrMonitorPortAlignmentErrors_Type()
)
vrptrMonitorPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortAlignmentErrors.setStatus("mandatory")


class _VrptrMonitorPortFrameTooLongs_Type(Integer32):
    """Custom type vrptrMonitorPortFrameTooLongs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", -1),
          ("supported", 0))
    )


_VrptrMonitorPortFrameTooLongs_Type.__name__ = "Integer32"
_VrptrMonitorPortFrameTooLongs_Object = MibTableColumn
vrptrMonitorPortFrameTooLongs = _VrptrMonitorPortFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 7),
    _VrptrMonitorPortFrameTooLongs_Type()
)
vrptrMonitorPortFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortFrameTooLongs.setStatus("mandatory")
_VrptrMonitorPortShortEvents_Type = Counter32
_VrptrMonitorPortShortEvents_Object = MibTableColumn
vrptrMonitorPortShortEvents = _VrptrMonitorPortShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 8),
    _VrptrMonitorPortShortEvents_Type()
)
vrptrMonitorPortShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortShortEvents.setStatus("mandatory")


class _VrptrMonitorPortRunts_Type(Integer32):
    """Custom type vrptrMonitorPortRunts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", -1),
          ("supported", 0))
    )


_VrptrMonitorPortRunts_Type.__name__ = "Integer32"
_VrptrMonitorPortRunts_Object = MibTableColumn
vrptrMonitorPortRunts = _VrptrMonitorPortRunts_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 9),
    _VrptrMonitorPortRunts_Type()
)
vrptrMonitorPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortRunts.setStatus("mandatory")


class _VrptrMonitorPortCollisions_Type(Integer32):
    """Custom type vrptrMonitorPortCollisions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", -1),
          ("supported", 0))
    )


_VrptrMonitorPortCollisions_Type.__name__ = "Integer32"
_VrptrMonitorPortCollisions_Object = MibTableColumn
vrptrMonitorPortCollisions = _VrptrMonitorPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 10),
    _VrptrMonitorPortCollisions_Type()
)
vrptrMonitorPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortCollisions.setStatus("mandatory")
_VrptrMonitorPortLateEvents_Type = Counter32
_VrptrMonitorPortLateEvents_Object = MibTableColumn
vrptrMonitorPortLateEvents = _VrptrMonitorPortLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 11),
    _VrptrMonitorPortLateEvents_Type()
)
vrptrMonitorPortLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortLateEvents.setStatus("mandatory")
_VrptrMonitorPortVeryLongEvents_Type = Counter32
_VrptrMonitorPortVeryLongEvents_Object = MibTableColumn
vrptrMonitorPortVeryLongEvents = _VrptrMonitorPortVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 12),
    _VrptrMonitorPortVeryLongEvents_Type()
)
vrptrMonitorPortVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortVeryLongEvents.setStatus("mandatory")


class _VrptrMonitorPortDataRateMismatches_Type(Integer32):
    """Custom type vrptrMonitorPortDataRateMismatches based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", -1),
          ("supported", 0))
    )


_VrptrMonitorPortDataRateMismatches_Type.__name__ = "Integer32"
_VrptrMonitorPortDataRateMismatches_Object = MibTableColumn
vrptrMonitorPortDataRateMismatches = _VrptrMonitorPortDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 13),
    _VrptrMonitorPortDataRateMismatches_Type()
)
vrptrMonitorPortDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortDataRateMismatches.setStatus("mandatory")
_VrptrMonitorPortAutoPartitions_Type = Counter32
_VrptrMonitorPortAutoPartitions_Object = MibTableColumn
vrptrMonitorPortAutoPartitions = _VrptrMonitorPortAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 14),
    _VrptrMonitorPortAutoPartitions_Type()
)
vrptrMonitorPortAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortAutoPartitions.setStatus("mandatory")
_VrptrMonitorPortTotalErrors_Type = Counter32
_VrptrMonitorPortTotalErrors_Object = MibTableColumn
vrptrMonitorPortTotalErrors = _VrptrMonitorPortTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 15),
    _VrptrMonitorPortTotalErrors_Type()
)
vrptrMonitorPortTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortTotalErrors.setStatus("mandatory")
_VrptrMonitorPortLastChange_Type = TimeTicks
_VrptrMonitorPortLastChange_Object = MibTableColumn
vrptrMonitorPortLastChange = _VrptrMonitorPortLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 16),
    _VrptrMonitorPortLastChange_Type()
)
vrptrMonitorPortLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortLastChange.setStatus("mandatory")
_VrptrMonitorPortSentFrames_Type = Counter32
_VrptrMonitorPortSentFrames_Object = MibTableColumn
vrptrMonitorPortSentFrames = _VrptrMonitorPortSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 17),
    _VrptrMonitorPortSentFrames_Type()
)
vrptrMonitorPortSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortSentFrames.setStatus("mandatory")
_VrptrMonitorPortSentOctets_Type = Counter32
_VrptrMonitorPortSentOctets_Object = MibTableColumn
vrptrMonitorPortSentOctets = _VrptrMonitorPortSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 18),
    _VrptrMonitorPortSentOctets_Type()
)
vrptrMonitorPortSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortSentOctets.setStatus("mandatory")
_VrptrMonitorPortDroppedFrames_Type = Counter32
_VrptrMonitorPortDroppedFrames_Object = MibTableColumn
vrptrMonitorPortDroppedFrames = _VrptrMonitorPortDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 19),
    _VrptrMonitorPortDroppedFrames_Type()
)
vrptrMonitorPortDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortDroppedFrames.setStatus("mandatory")
_VrptrMonitorPortOtherErrors_Type = Counter32
_VrptrMonitorPortOtherErrors_Object = MibTableColumn
vrptrMonitorPortOtherErrors = _VrptrMonitorPortOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 1, 1, 20),
    _VrptrMonitorPortOtherErrors_Type()
)
vrptrMonitorPortOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortOtherErrors.setStatus("mandatory")
_VrptrMonitor100PortTable_Object = MibTable
vrptrMonitor100PortTable = _VrptrMonitor100PortTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 2)
)
if mibBuilder.loadTexts:
    vrptrMonitor100PortTable.setStatus("mandatory")
_VrptrMonitor100PortEntry_Object = MibTableRow
vrptrMonitor100PortEntry = _VrptrMonitor100PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 2, 1)
)
vrptrMonitor100PortEntry.setIndexNames(
    (0, "VERTICAL-SNMP-REPEATER-MIB", "vrptrMonitorPortGroupIndex"),
    (0, "VERTICAL-SNMP-REPEATER-MIB", "vrptrMonitorPortIndex"),
)
if mibBuilder.loadTexts:
    vrptrMonitor100PortEntry.setStatus("mandatory")
_VrptrMonitorPortIsolates_Type = Counter32
_VrptrMonitorPortIsolates_Object = MibTableColumn
vrptrMonitorPortIsolates = _VrptrMonitorPortIsolates_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 2, 1, 1),
    _VrptrMonitorPortIsolates_Type()
)
vrptrMonitorPortIsolates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortIsolates.setStatus("mandatory")
_VrptrMonitorPortSymbolErrors_Type = Counter32
_VrptrMonitorPortSymbolErrors_Object = MibTableColumn
vrptrMonitorPortSymbolErrors = _VrptrMonitorPortSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 2, 1, 2),
    _VrptrMonitorPortSymbolErrors_Type()
)
vrptrMonitorPortSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortSymbolErrors.setStatus("mandatory")
_VrptrMonitorPortUpper32Octets_Type = Counter32
_VrptrMonitorPortUpper32Octets_Object = MibTableColumn
vrptrMonitorPortUpper32Octets = _VrptrMonitorPortUpper32Octets_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 2, 1, 3),
    _VrptrMonitorPortUpper32Octets_Type()
)
vrptrMonitorPortUpper32Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortUpper32Octets.setStatus("mandatory")
_VrptrMonitorPortUpper32SentOctets_Type = Counter32
_VrptrMonitorPortUpper32SentOctets_Object = MibTableColumn
vrptrMonitorPortUpper32SentOctets = _VrptrMonitorPortUpper32SentOctets_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 3, 2, 1, 4),
    _VrptrMonitorPortUpper32SentOctets_Type()
)
vrptrMonitorPortUpper32SentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonitorPortUpper32SentOctets.setStatus("mandatory")
_VrptrMonitorAllRptrInfo_ObjectIdentity = ObjectIdentity
vrptrMonitorAllRptrInfo = _VrptrMonitorAllRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 4)
)
_VrptrMonTable_Object = MibTable
vrptrMonTable = _VrptrMonTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 4, 1)
)
if mibBuilder.loadTexts:
    vrptrMonTable.setStatus("mandatory")
_VrptrMonEntry_Object = MibTableRow
vrptrMonEntry = _VrptrMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 4, 1, 1)
)
vrptrMonEntry.setIndexNames(
    (0, "VERTICAL-SNMP-REPEATER-MIB", "vrptrInfoId"),
)
if mibBuilder.loadTexts:
    vrptrMonEntry.setStatus("mandatory")


class _VrptrMonTxCollisions_Type(Integer32):
    """Custom type vrptrMonTxCollisions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", -1),
          ("supported", 0))
    )


_VrptrMonTxCollisions_Type.__name__ = "Integer32"
_VrptrMonTxCollisions_Object = MibTableColumn
vrptrMonTxCollisions = _VrptrMonTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 4, 1, 1, 1),
    _VrptrMonTxCollisions_Type()
)
vrptrMonTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonTxCollisions.setStatus("mandatory")
_VrptrMonTotalFrames_Type = Counter32
_VrptrMonTotalFrames_Object = MibTableColumn
vrptrMonTotalFrames = _VrptrMonTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 4, 1, 1, 3),
    _VrptrMonTotalFrames_Type()
)
vrptrMonTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonTotalFrames.setStatus("mandatory")
_VrptrMonTotalErrors_Type = Counter32
_VrptrMonTotalErrors_Object = MibTableColumn
vrptrMonTotalErrors = _VrptrMonTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 4, 1, 1, 4),
    _VrptrMonTotalErrors_Type()
)
vrptrMonTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonTotalErrors.setStatus("mandatory")


class _VrptrMonTotalOctets_Type(Integer32):
    """Custom type vrptrMonTotalOctets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", -1),
          ("supported", 0))
    )


_VrptrMonTotalOctets_Type.__name__ = "Integer32"
_VrptrMonTotalOctets_Object = MibTableColumn
vrptrMonTotalOctets = _VrptrMonTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 4, 1, 1, 5),
    _VrptrMonTotalOctets_Type()
)
vrptrMonTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonTotalOctets.setStatus("mandatory")
_VrptrMon100Table_Object = MibTable
vrptrMon100Table = _VrptrMon100Table_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 4, 2)
)
if mibBuilder.loadTexts:
    vrptrMon100Table.setStatus("mandatory")
_VrptrMon100Entry_Object = MibTableRow
vrptrMon100Entry = _VrptrMon100Entry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 4, 2, 1)
)
vrptrMon100Entry.setIndexNames(
    (0, "VERTICAL-SNMP-REPEATER-MIB", "vrptrInfoId"),
)
if mibBuilder.loadTexts:
    vrptrMon100Entry.setStatus("mandatory")
_VrptrMonUpper32TotalOctets_Type = Counter32
_VrptrMonUpper32TotalOctets_Object = MibTableColumn
vrptrMonUpper32TotalOctets = _VrptrMonUpper32TotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 2338, 4, 2, 4, 2, 1, 1),
    _VrptrMonUpper32TotalOctets_Type()
)
vrptrMonUpper32TotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrptrMonUpper32TotalOctets.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERTICAL-SNMP-REPEATER-MIB",
    **{"MacAddress": MacAddress,
       "vsnmpDot3RptrMgt": vsnmpDot3RptrMgt,
       "vrptrBasicPackage": vrptrBasicPackage,
       "vrptrGroupInfo": vrptrGroupInfo,
       "vrptrGroupTable": vrptrGroupTable,
       "vrptrGroupEntry": vrptrGroupEntry,
       "vrptrGroupIndex": vrptrGroupIndex,
       "vrptrGroupObjectID": vrptrGroupObjectID,
       "vrptrGroupOperStatus": vrptrGroupOperStatus,
       "vrptrGroupPortCapacity": vrptrGroupPortCapacity,
       "vrptrGroupSlotNumber": vrptrGroupSlotNumber,
       "vrptrGroupBroadcastDomainNumber": vrptrGroupBroadcastDomainNumber,
       "vrptrGroupNetworkAdapterNumber": vrptrGroupNetworkAdapterNumber,
       "vrptrGroupLedStatus": vrptrGroupLedStatus,
       "vrptrGroupExternalPortCapacity": vrptrGroupExternalPortCapacity,
       "vrptrPortInfo": vrptrPortInfo,
       "vrptrPortTable": vrptrPortTable,
       "vrptrPortEntry": vrptrPortEntry,
       "vrptrPortGroupIndex": vrptrPortGroupIndex,
       "vrptrPortIndex": vrptrPortIndex,
       "vrptrPortAdminStatus": vrptrPortAdminStatus,
       "vrptrPortAutoPartitionState": vrptrPortAutoPartitionState,
       "vrptrPortOperStatus": vrptrPortOperStatus,
       "vrptrPortRptrId": vrptrPortRptrId,
       "vrptrPortLinkState": vrptrPortLinkState,
       "vrptrPortSpeed": vrptrPortSpeed,
       "vrptrPortSpeedSelect": vrptrPortSpeedSelect,
       "vrptrPortDuplex": vrptrPortDuplex,
       "vrptrPortDuplexSelect": vrptrPortDuplexSelect,
       "vrptrPortPolarity": vrptrPortPolarity,
       "vrptrAllRptrInfo": vrptrAllRptrInfo,
       "vrptrInfoTable": vrptrInfoTable,
       "vrptrInfoEntry": vrptrInfoEntry,
       "vrptrInfoId": vrptrInfoId,
       "vrptrInfoRptrType": vrptrInfoRptrType,
       "vrptrInfoOperStatus": vrptrInfoOperStatus,
       "vrptrInfoReset": vrptrInfoReset,
       "vrptrInfoPartitionedPorts": vrptrInfoPartitionedPorts,
       "vrptrInfoLastChange": vrptrInfoLastChange,
       "vrptrMonitorPackage": vrptrMonitorPackage,
       "vrptrMonitorPortInfo": vrptrMonitorPortInfo,
       "vrptrMonitorPortTable": vrptrMonitorPortTable,
       "vrptrMonitorPortEntry": vrptrMonitorPortEntry,
       "vrptrMonitorPortGroupIndex": vrptrMonitorPortGroupIndex,
       "vrptrMonitorPortIndex": vrptrMonitorPortIndex,
       "vrptrMonitorPortReadableFrames": vrptrMonitorPortReadableFrames,
       "vrptrMonitorPortReadableOctets": vrptrMonitorPortReadableOctets,
       "vrptrMonitorPortFCSErrors": vrptrMonitorPortFCSErrors,
       "vrptrMonitorPortAlignmentErrors": vrptrMonitorPortAlignmentErrors,
       "vrptrMonitorPortFrameTooLongs": vrptrMonitorPortFrameTooLongs,
       "vrptrMonitorPortShortEvents": vrptrMonitorPortShortEvents,
       "vrptrMonitorPortRunts": vrptrMonitorPortRunts,
       "vrptrMonitorPortCollisions": vrptrMonitorPortCollisions,
       "vrptrMonitorPortLateEvents": vrptrMonitorPortLateEvents,
       "vrptrMonitorPortVeryLongEvents": vrptrMonitorPortVeryLongEvents,
       "vrptrMonitorPortDataRateMismatches": vrptrMonitorPortDataRateMismatches,
       "vrptrMonitorPortAutoPartitions": vrptrMonitorPortAutoPartitions,
       "vrptrMonitorPortTotalErrors": vrptrMonitorPortTotalErrors,
       "vrptrMonitorPortLastChange": vrptrMonitorPortLastChange,
       "vrptrMonitorPortSentFrames": vrptrMonitorPortSentFrames,
       "vrptrMonitorPortSentOctets": vrptrMonitorPortSentOctets,
       "vrptrMonitorPortDroppedFrames": vrptrMonitorPortDroppedFrames,
       "vrptrMonitorPortOtherErrors": vrptrMonitorPortOtherErrors,
       "vrptrMonitor100PortTable": vrptrMonitor100PortTable,
       "vrptrMonitor100PortEntry": vrptrMonitor100PortEntry,
       "vrptrMonitorPortIsolates": vrptrMonitorPortIsolates,
       "vrptrMonitorPortSymbolErrors": vrptrMonitorPortSymbolErrors,
       "vrptrMonitorPortUpper32Octets": vrptrMonitorPortUpper32Octets,
       "vrptrMonitorPortUpper32SentOctets": vrptrMonitorPortUpper32SentOctets,
       "vrptrMonitorAllRptrInfo": vrptrMonitorAllRptrInfo,
       "vrptrMonTable": vrptrMonTable,
       "vrptrMonEntry": vrptrMonEntry,
       "vrptrMonTxCollisions": vrptrMonTxCollisions,
       "vrptrMonTotalFrames": vrptrMonTotalFrames,
       "vrptrMonTotalErrors": vrptrMonTotalErrors,
       "vrptrMonTotalOctets": vrptrMonTotalOctets,
       "vrptrMon100Table": vrptrMon100Table,
       "vrptrMon100Entry": vrptrMon100Entry,
       "vrptrMonUpper32TotalOctets": vrptrMonUpper32TotalOctets}
)
