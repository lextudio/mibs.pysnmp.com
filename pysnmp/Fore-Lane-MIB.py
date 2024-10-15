# SNMP MIB module (Fore-Lane-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-Lane-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:07 2024
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

(AtmAddress,
 EntryStatus,
 NsapAddr,
 systems) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "AtmAddress",
    "EntryStatus",
    "NsapAddr",
    "systems")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

foreLaneModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 4)
)


# Types definitions



class LecConfigType(Integer32):
    """Custom type LecConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 2),
          ("wellknown", 1))
    )





class LaneDataFrameFormat(Integer32):
    """Custom type LaneDataFrameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aflane8023", 2),
          ("aflane8025", 3),
          ("unspecified", 1))
    )





class LaneDataFrameSize(Integer32):
    """Custom type LaneDataFrameSize based on Integer32"""
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
        *(("max1516", 2),
          ("max1580", 6),
          ("max18190", 5),
          ("max4544", 3),
          ("max9234", 4),
          ("unspecified", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LaneLecGroup_ObjectIdentity = ObjectIdentity
laneLecGroup = _LaneLecGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1)
)
_LecConfGroup_ObjectIdentity = ObjectIdentity
lecConfGroup = _LecConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1)
)
_LecDefaultLecsConfigType_Type = LecConfigType
_LecDefaultLecsConfigType_Object = MibScalar
lecDefaultLecsConfigType = _LecDefaultLecsConfigType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 1),
    _LecDefaultLecsConfigType_Type()
)
lecDefaultLecsConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecDefaultLecsConfigType.setStatus("current")
_LecDefaultLecsAtmAddress_Type = AtmAddress
_LecDefaultLecsAtmAddress_Object = MibScalar
lecDefaultLecsAtmAddress = _LecDefaultLecsAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 2),
    _LecDefaultLecsAtmAddress_Type()
)
lecDefaultLecsAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecDefaultLecsAtmAddress.setStatus("current")
_LecConfTable_Object = MibTable
lecConfTable = _LecConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10)
)
if mibBuilder.loadTexts:
    lecConfTable.setStatus("current")
_LecConfEntry_Object = MibTableRow
lecConfEntry = _LecConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1)
)
lecConfEntry.setIndexNames(
    (0, "Fore-Lane-MIB", "lecConfIndex"),
)
if mibBuilder.loadTexts:
    lecConfEntry.setStatus("current")


class _LecConfIndex_Type(Integer32):
    """Custom type lecConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LecConfIndex_Type.__name__ = "Integer32"
_LecConfIndex_Object = MibTableColumn
lecConfIndex = _LecConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 1),
    _LecConfIndex_Type()
)
lecConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConfIndex.setStatus("current")
_LecConfAtmAddress_Type = AtmAddress
_LecConfAtmAddress_Object = MibTableColumn
lecConfAtmAddress = _LecConfAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 2),
    _LecConfAtmAddress_Type()
)
lecConfAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecConfAtmAddress.setStatus("current")


class _LecConfAdminStatus_Type(Integer32):
    """Custom type lecConfAdminStatus based on Integer32"""
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


_LecConfAdminStatus_Type.__name__ = "Integer32"
_LecConfAdminStatus_Object = MibTableColumn
lecConfAdminStatus = _LecConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 3),
    _LecConfAdminStatus_Type()
)
lecConfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecConfAdminStatus.setStatus("current")


class _LecConfOperStatus_Type(Integer32):
    """Custom type lecConfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("joining", 3),
          ("up", 1))
    )


_LecConfOperStatus_Type.__name__ = "Integer32"
_LecConfOperStatus_Object = MibTableColumn
lecConfOperStatus = _LecConfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 4),
    _LecConfOperStatus_Type()
)
lecConfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConfOperStatus.setStatus("current")
_LecConfElanName_Type = DisplayString
_LecConfElanName_Object = MibTableColumn
lecConfElanName = _LecConfElanName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 5),
    _LecConfElanName_Type()
)
lecConfElanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecConfElanName.setStatus("current")
_LecConfMacAddress_Type = MacAddress
_LecConfMacAddress_Object = MibTableColumn
lecConfMacAddress = _LecConfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 6),
    _LecConfMacAddress_Type()
)
lecConfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConfMacAddress.setStatus("current")
_LecConfLecsConfigType_Type = LecConfigType
_LecConfLecsConfigType_Object = MibTableColumn
lecConfLecsConfigType = _LecConfLecsConfigType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 7),
    _LecConfLecsConfigType_Type()
)
lecConfLecsConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecConfLecsConfigType.setStatus("current")
_LecConfLecsAtmAddress_Type = AtmAddress
_LecConfLecsAtmAddress_Object = MibTableColumn
lecConfLecsAtmAddress = _LecConfLecsAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 8),
    _LecConfLecsAtmAddress_Type()
)
lecConfLecsAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecConfLecsAtmAddress.setStatus("current")
_LecConfLesAtmAddress_Type = AtmAddress
_LecConfLesAtmAddress_Object = MibTableColumn
lecConfLesAtmAddress = _LecConfLesAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 9),
    _LecConfLesAtmAddress_Type()
)
lecConfLesAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecConfLesAtmAddress.setStatus("current")
_LecConfEntryStatus_Type = EntryStatus
_LecConfEntryStatus_Object = MibTableColumn
lecConfEntryStatus = _LecConfEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 10),
    _LecConfEntryStatus_Type()
)
lecConfEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecConfEntryStatus.setStatus("current")
_LecConfIfName_Type = DisplayString
_LecConfIfName_Object = MibTableColumn
lecConfIfName = _LecConfIfName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 11),
    _LecConfIfName_Type()
)
lecConfIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConfIfName.setStatus("current")
_LecStatGroup_ObjectIdentity = ObjectIdentity
lecStatGroup = _LecStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 2)
)
_LecArpGroup_ObjectIdentity = ObjectIdentity
lecArpGroup = _LecArpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3)
)


class _ElarpFlush_Type(Integer32):
    """Custom type elarpFlush based on Integer32"""
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


_ElarpFlush_Type.__name__ = "Integer32"
_ElarpFlush_Object = MibScalar
elarpFlush = _ElarpFlush_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 1),
    _ElarpFlush_Type()
)
elarpFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elarpFlush.setStatus("current")
_LecArpTable_Object = MibTable
lecArpTable = _LecArpTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10)
)
if mibBuilder.loadTexts:
    lecArpTable.setStatus("current")
_LecArpEntry_Object = MibTableRow
lecArpEntry = _LecArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10, 1)
)
lecArpEntry.setIndexNames(
    (0, "Fore-Lane-MIB", "lecArpMacAddress"),
)
if mibBuilder.loadTexts:
    lecArpEntry.setStatus("current")
_LecArpMacAddress_Type = MacAddress
_LecArpMacAddress_Object = MibTableColumn
lecArpMacAddress = _LecArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10, 1, 1),
    _LecArpMacAddress_Type()
)
lecArpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpMacAddress.setStatus("current")
_LecArpAtmAddress_Type = AtmAddress
_LecArpAtmAddress_Object = MibTableColumn
lecArpAtmAddress = _LecArpAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10, 1, 2),
    _LecArpAtmAddress_Type()
)
lecArpAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpAtmAddress.setStatus("current")


class _LecArpFlags_Type(Integer32):
    """Custom type lecArpFlags based on Integer32"""
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
        *(("incomplete", 1),
          ("loopback", 2),
          ("pending", 3),
          ("valid", 4))
    )


_LecArpFlags_Type.__name__ = "Integer32"
_LecArpFlags_Object = MibTableColumn
lecArpFlags = _LecArpFlags_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10, 1, 3),
    _LecArpFlags_Type()
)
lecArpFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpFlags.setStatus("current")
_LecArpConnVPI_Type = Integer32
_LecArpConnVPI_Object = MibTableColumn
lecArpConnVPI = _LecArpConnVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10, 1, 4),
    _LecArpConnVPI_Type()
)
lecArpConnVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpConnVPI.setStatus("current")
_LecArpConnVCI_Type = Integer32
_LecArpConnVCI_Object = MibTableColumn
lecArpConnVCI = _LecArpConnVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10, 1, 5),
    _LecArpConnVCI_Type()
)
lecArpConnVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpConnVCI.setStatus("current")


class _LecArpFlush_Type(Integer32):
    """Custom type lecArpFlush based on Integer32"""
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


_LecArpFlush_Type.__name__ = "Integer32"
_LecArpFlush_Object = MibTableColumn
lecArpFlush = _LecArpFlush_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10, 1, 6),
    _LecArpFlush_Type()
)
lecArpFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecArpFlush.setStatus("current")
_LecArpElanName_Type = DisplayString
_LecArpElanName_Object = MibTableColumn
lecArpElanName = _LecArpElanName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10, 1, 7),
    _LecArpElanName_Type()
)
lecArpElanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpElanName.setStatus("current")
_LaneLesGroup_ObjectIdentity = ObjectIdentity
laneLesGroup = _LaneLesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2)
)
_LesConfGroup_ObjectIdentity = ObjectIdentity
lesConfGroup = _LesConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1)
)
_LesConfTable_Object = MibTable
lesConfTable = _LesConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lesConfTable.setStatus("current")
_LesConfEntry_Object = MibTableRow
lesConfEntry = _LesConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1)
)
lesConfEntry.setIndexNames(
    (0, "Fore-Lane-MIB", "lesConfIndex"),
)
if mibBuilder.loadTexts:
    lesConfEntry.setStatus("current")


class _LesConfIndex_Type(Integer32):
    """Custom type lesConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LesConfIndex_Type.__name__ = "Integer32"
_LesConfIndex_Object = MibTableColumn
lesConfIndex = _LesConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 1),
    _LesConfIndex_Type()
)
lesConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesConfIndex.setStatus("current")
_LesConfAtmAddress_Type = AtmAddress
_LesConfAtmAddress_Object = MibTableColumn
lesConfAtmAddress = _LesConfAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 2),
    _LesConfAtmAddress_Type()
)
lesConfAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesConfAtmAddress.setStatus("current")


class _LesConfAdminStatus_Type(Integer32):
    """Custom type lesConfAdminStatus based on Integer32"""
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


_LesConfAdminStatus_Type.__name__ = "Integer32"
_LesConfAdminStatus_Object = MibTableColumn
lesConfAdminStatus = _LesConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 3),
    _LesConfAdminStatus_Type()
)
lesConfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesConfAdminStatus.setStatus("current")


class _LesConfOperStatus_Type(Integer32):
    """Custom type lesConfOperStatus based on Integer32"""
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


_LesConfOperStatus_Type.__name__ = "Integer32"
_LesConfOperStatus_Object = MibTableColumn
lesConfOperStatus = _LesConfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 4),
    _LesConfOperStatus_Type()
)
lesConfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesConfOperStatus.setStatus("current")
_LesConfElanName_Type = DisplayString
_LesConfElanName_Object = MibTableColumn
lesConfElanName = _LesConfElanName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 5),
    _LesConfElanName_Type()
)
lesConfElanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesConfElanName.setStatus("current")
_LesConfBusAtmAddress_Type = AtmAddress
_LesConfBusAtmAddress_Object = MibTableColumn
lesConfBusAtmAddress = _LesConfBusAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 6),
    _LesConfBusAtmAddress_Type()
)
lesConfBusAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesConfBusAtmAddress.setStatus("current")


class _LesConfBusMaster_Type(Integer32):
    """Custom type lesConfBusMaster based on Integer32"""
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


_LesConfBusMaster_Type.__name__ = "Integer32"
_LesConfBusMaster_Object = MibTableColumn
lesConfBusMaster = _LesConfBusMaster_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 7),
    _LesConfBusMaster_Type()
)
lesConfBusMaster.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesConfBusMaster.setStatus("deprecated")
_LesConfEntryStatus_Type = EntryStatus
_LesConfEntryStatus_Object = MibTableColumn
lesConfEntryStatus = _LesConfEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 8),
    _LesConfEntryStatus_Type()
)
lesConfEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesConfEntryStatus.setStatus("current")
_LesConfLanType_Type = LaneDataFrameFormat
_LesConfLanType_Object = MibTableColumn
lesConfLanType = _LesConfLanType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 9),
    _LesConfLanType_Type()
)
lesConfLanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesConfLanType.setStatus("current")
_LesConfMaxFrameSize_Type = LaneDataFrameSize
_LesConfMaxFrameSize_Object = MibTableColumn
lesConfMaxFrameSize = _LesConfMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 10),
    _LesConfMaxFrameSize_Type()
)
lesConfMaxFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesConfMaxFrameSize.setStatus("current")


class _LesConfSecureServer_Type(Integer32):
    """Custom type lesConfSecureServer based on Integer32"""
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


_LesConfSecureServer_Type.__name__ = "Integer32"
_LesConfSecureServer_Object = MibTableColumn
lesConfSecureServer = _LesConfSecureServer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 11),
    _LesConfSecureServer_Type()
)
lesConfSecureServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesConfSecureServer.setStatus("current")
_LesConfLECSAtmAddress_Type = AtmAddress
_LesConfLECSAtmAddress_Object = MibTableColumn
lesConfLECSAtmAddress = _LesConfLECSAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 12),
    _LesConfLECSAtmAddress_Type()
)
lesConfLECSAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesConfLECSAtmAddress.setStatus("current")
_LesConfAnycastAtmAddress_Type = AtmAddress
_LesConfAnycastAtmAddress_Object = MibTableColumn
lesConfAnycastAtmAddress = _LesConfAnycastAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 13),
    _LesConfAnycastAtmAddress_Type()
)
lesConfAnycastAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesConfAnycastAtmAddress.setStatus("current")


class _LesConfRegisterTLVs_Type(Integer32):
    """Custom type lesConfRegisterTLVs based on Integer32"""
    defaultValue = 1

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


_LesConfRegisterTLVs_Type.__name__ = "Integer32"
_LesConfRegisterTLVs_Object = MibTableColumn
lesConfRegisterTLVs = _LesConfRegisterTLVs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 14),
    _LesConfRegisterTLVs_Type()
)
lesConfRegisterTLVs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesConfRegisterTLVs.setStatus("current")
_LesConfElanId_Type = Integer32
_LesConfElanId_Object = MibTableColumn
lesConfElanId = _LesConfElanId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 15),
    _LesConfElanId_Type()
)
lesConfElanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesConfElanId.setStatus("current")


class _LesConfTokenRingNumber_Type(Integer32):
    """Custom type lesConfTokenRingNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LesConfTokenRingNumber_Type.__name__ = "Integer32"
_LesConfTokenRingNumber_Object = MibTableColumn
lesConfTokenRingNumber = _LesConfTokenRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 16),
    _LesConfTokenRingNumber_Type()
)
lesConfTokenRingNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesConfTokenRingNumber.setStatus("current")


class _LesConfForwardArp_Type(Integer32):
    """Custom type lesConfForwardArp based on Integer32"""
    defaultValue = 2

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


_LesConfForwardArp_Type.__name__ = "Integer32"
_LesConfForwardArp_Object = MibTableColumn
lesConfForwardArp = _LesConfForwardArp_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 17),
    _LesConfForwardArp_Type()
)
lesConfForwardArp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesConfForwardArp.setStatus("current")
_LesLnniConfTable_Object = MibTable
lesLnniConfTable = _LesLnniConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lesLnniConfTable.setStatus("current")
_LesLnniConfEntry_Object = MibTableRow
lesLnniConfEntry = _LesLnniConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 2, 1)
)
lesLnniConfEntry.setIndexNames(
    (0, "Fore-Lane-MIB", "lesConfIndex"),
    (0, "Fore-Lane-MIB", "lesLnniConfAtmAddress"),
)
if mibBuilder.loadTexts:
    lesLnniConfEntry.setStatus("current")
_LesLnniConfAtmAddress_Type = NsapAddr
_LesLnniConfAtmAddress_Object = MibTableColumn
lesLnniConfAtmAddress = _LesLnniConfAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 2, 1, 1),
    _LesLnniConfAtmAddress_Type()
)
lesLnniConfAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLnniConfAtmAddress.setStatus("current")
_LesLnniConfEntryStatus_Type = EntryStatus
_LesLnniConfEntryStatus_Object = MibTableColumn
lesLnniConfEntryStatus = _LesLnniConfEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 2, 1, 2),
    _LesLnniConfEntryStatus_Type()
)
lesLnniConfEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLnniConfEntryStatus.setStatus("current")
_LesLeqGroup_ObjectIdentity = ObjectIdentity
lesLeqGroup = _LesLeqGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3)
)
_LesLeqConfLesId_Type = Integer32
_LesLeqConfLesId_Object = MibScalar
lesLeqConfLesId = _LesLeqConfLesId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 1),
    _LesLeqConfLesId_Type()
)
lesLeqConfLesId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLeqConfLesId.setStatus("current")


class _LesLeqTableReload_Type(Integer32):
    """Custom type lesLeqTableReload based on Integer32"""
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
        *(("failed", 5),
          ("go", 2),
          ("idle", 1),
          ("inProgress", 3),
          ("succeeded", 4))
    )


_LesLeqTableReload_Type.__name__ = "Integer32"
_LesLeqTableReload_Object = MibScalar
lesLeqTableReload = _LesLeqTableReload_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 2),
    _LesLeqTableReload_Type()
)
lesLeqTableReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLeqTableReload.setStatus("current")
_LesLeqStatLesId_Type = Integer32
_LesLeqStatLesId_Object = MibScalar
lesLeqStatLesId = _LesLeqStatLesId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 3),
    _LesLeqStatLesId_Type()
)
lesLeqStatLesId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLeqStatLesId.setStatus("current")
_LesLeqLastTime_Type = TimeTicks
_LesLeqLastTime_Object = MibScalar
lesLeqLastTime = _LesLeqLastTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 4),
    _LesLeqLastTime_Type()
)
lesLeqLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLeqLastTime.setStatus("current")
_LesLeqTable_Object = MibTable
lesLeqTable = _LesLeqTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 5)
)
if mibBuilder.loadTexts:
    lesLeqTable.setStatus("current")
_LesLeqEntry_Object = MibTableRow
lesLeqEntry = _LesLeqEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 5, 1)
)
lesLeqEntry.setIndexNames(
    (0, "Fore-Lane-MIB", "lesLeqIndex"),
)
if mibBuilder.loadTexts:
    lesLeqEntry.setStatus("current")
_LesLeqIndex_Type = Integer32
_LesLeqIndex_Object = MibTableColumn
lesLeqIndex = _LesLeqIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 5, 1, 1),
    _LesLeqIndex_Type()
)
lesLeqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLeqIndex.setStatus("current")
_LesLeqNsap_Type = NsapAddr
_LesLeqNsap_Object = MibTableColumn
lesLeqNsap = _LesLeqNsap_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 5, 1, 2),
    _LesLeqNsap_Type()
)
lesLeqNsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLeqNsap.setStatus("current")
_LesLeqName_Type = DisplayString
_LesLeqName_Object = MibTableColumn
lesLeqName = _LesLeqName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 5, 1, 3),
    _LesLeqName_Type()
)
lesLeqName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLeqName.setStatus("current")
_LesStatGroup_ObjectIdentity = ObjectIdentity
lesStatGroup = _LesStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 2)
)
_LaneBusGroup_ObjectIdentity = ObjectIdentity
laneBusGroup = _LaneBusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 3)
)
_BusConfGroup_ObjectIdentity = ObjectIdentity
busConfGroup = _BusConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1)
)
_BusConfTable_Object = MibTable
busConfTable = _BusConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    busConfTable.setStatus("deprecated")
_BusConfEntry_Object = MibTableRow
busConfEntry = _BusConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1)
)
busConfEntry.setIndexNames(
    (0, "Fore-Lane-MIB", "busConfIndex"),
)
if mibBuilder.loadTexts:
    busConfEntry.setStatus("deprecated")


class _BusConfIndex_Type(Integer32):
    """Custom type busConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BusConfIndex_Type.__name__ = "Integer32"
_BusConfIndex_Object = MibTableColumn
busConfIndex = _BusConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1, 1),
    _BusConfIndex_Type()
)
busConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busConfIndex.setStatus("deprecated")
_BusConfAtmAddress_Type = AtmAddress
_BusConfAtmAddress_Object = MibTableColumn
busConfAtmAddress = _BusConfAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1, 2),
    _BusConfAtmAddress_Type()
)
busConfAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    busConfAtmAddress.setStatus("deprecated")


class _BusConfAdminStatus_Type(Integer32):
    """Custom type busConfAdminStatus based on Integer32"""
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


_BusConfAdminStatus_Type.__name__ = "Integer32"
_BusConfAdminStatus_Object = MibTableColumn
busConfAdminStatus = _BusConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1, 3),
    _BusConfAdminStatus_Type()
)
busConfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    busConfAdminStatus.setStatus("deprecated")


class _BusConfOperStatus_Type(Integer32):
    """Custom type busConfOperStatus based on Integer32"""
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


_BusConfOperStatus_Type.__name__ = "Integer32"
_BusConfOperStatus_Object = MibTableColumn
busConfOperStatus = _BusConfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1, 4),
    _BusConfOperStatus_Type()
)
busConfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busConfOperStatus.setStatus("deprecated")
_BusConfName_Type = DisplayString
_BusConfName_Object = MibTableColumn
busConfName = _BusConfName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1, 5),
    _BusConfName_Type()
)
busConfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    busConfName.setStatus("deprecated")
_BusConfEntryStatus_Type = EntryStatus
_BusConfEntryStatus_Object = MibTableColumn
busConfEntryStatus = _BusConfEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1, 6),
    _BusConfEntryStatus_Type()
)
busConfEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    busConfEntryStatus.setStatus("deprecated")
_BusConfLanType_Type = LaneDataFrameFormat
_BusConfLanType_Object = MibTableColumn
busConfLanType = _BusConfLanType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1, 7),
    _BusConfLanType_Type()
)
busConfLanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    busConfLanType.setStatus("deprecated")
_BusConfMaxFrameSize_Type = LaneDataFrameSize
_BusConfMaxFrameSize_Object = MibTableColumn
busConfMaxFrameSize = _BusConfMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1, 8),
    _BusConfMaxFrameSize_Type()
)
busConfMaxFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    busConfMaxFrameSize.setStatus("deprecated")
_BusStatGroup_ObjectIdentity = ObjectIdentity
busStatGroup = _BusStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 2)
)
_LaneLecsGroup_ObjectIdentity = ObjectIdentity
laneLecsGroup = _LaneLecsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 4)
)
_LecsConfGroup_ObjectIdentity = ObjectIdentity
lecsConfGroup = _LecsConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1)
)
_LecsConfTable_Object = MibTable
lecsConfTable = _LecsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    lecsConfTable.setStatus("current")
_LecsConfEntry_Object = MibTableRow
lecsConfEntry = _LecsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1)
)
lecsConfEntry.setIndexNames(
    (0, "Fore-Lane-MIB", "lecsConfIndex"),
)
if mibBuilder.loadTexts:
    lecsConfEntry.setStatus("current")


class _LecsConfIndex_Type(Integer32):
    """Custom type lecsConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LecsConfIndex_Type.__name__ = "Integer32"
_LecsConfIndex_Object = MibTableColumn
lecsConfIndex = _LecsConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 1),
    _LecsConfIndex_Type()
)
lecsConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsConfIndex.setStatus("current")
_LecsConfAtmAddress_Type = AtmAddress
_LecsConfAtmAddress_Object = MibTableColumn
lecsConfAtmAddress = _LecsConfAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 2),
    _LecsConfAtmAddress_Type()
)
lecsConfAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsConfAtmAddress.setStatus("current")


class _LecsConfAdminStatus_Type(Integer32):
    """Custom type lecsConfAdminStatus based on Integer32"""
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


_LecsConfAdminStatus_Type.__name__ = "Integer32"
_LecsConfAdminStatus_Object = MibTableColumn
lecsConfAdminStatus = _LecsConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 3),
    _LecsConfAdminStatus_Type()
)
lecsConfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsConfAdminStatus.setStatus("current")


class _LecsConfOperStatus_Type(Integer32):
    """Custom type lecsConfOperStatus based on Integer32"""
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


_LecsConfOperStatus_Type.__name__ = "Integer32"
_LecsConfOperStatus_Object = MibTableColumn
lecsConfOperStatus = _LecsConfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 4),
    _LecsConfOperStatus_Type()
)
lecsConfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsConfOperStatus.setStatus("current")
_LecsConfDatabase_Type = DisplayString
_LecsConfDatabase_Object = MibTableColumn
lecsConfDatabase = _LecsConfDatabase_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 5),
    _LecsConfDatabase_Type()
)
lecsConfDatabase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsConfDatabase.setStatus("current")
_LecsConfEntryStatus_Type = EntryStatus
_LecsConfEntryStatus_Object = MibTableColumn
lecsConfEntryStatus = _LecsConfEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 6),
    _LecsConfEntryStatus_Type()
)
lecsConfEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsConfEntryStatus.setStatus("current")


class _LecsConfDefaultLesFlag_Type(Integer32):
    """Custom type lecsConfDefaultLesFlag based on Integer32"""
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


_LecsConfDefaultLesFlag_Type.__name__ = "Integer32"
_LecsConfDefaultLesFlag_Object = MibTableColumn
lecsConfDefaultLesFlag = _LecsConfDefaultLesFlag_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 7),
    _LecsConfDefaultLesFlag_Type()
)
lecsConfDefaultLesFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsConfDefaultLesFlag.setStatus("current")
_LecsConfDefaultLesAtmAddress_Type = AtmAddress
_LecsConfDefaultLesAtmAddress_Object = MibTableColumn
lecsConfDefaultLesAtmAddress = _LecsConfDefaultLesAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 8),
    _LecsConfDefaultLesAtmAddress_Type()
)
lecsConfDefaultLesAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsConfDefaultLesAtmAddress.setStatus("current")


class _LecsConfWellKnownAddressFlag_Type(Integer32):
    """Custom type lecsConfWellKnownAddressFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atm-forum", 2),
          ("none", 1),
          ("other", 3))
    )


_LecsConfWellKnownAddressFlag_Type.__name__ = "Integer32"
_LecsConfWellKnownAddressFlag_Object = MibTableColumn
lecsConfWellKnownAddressFlag = _LecsConfWellKnownAddressFlag_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 9),
    _LecsConfWellKnownAddressFlag_Type()
)
lecsConfWellKnownAddressFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsConfWellKnownAddressFlag.setStatus("current")
_LecsConfWellKnownAddress_Type = AtmAddress
_LecsConfWellKnownAddress_Object = MibTableColumn
lecsConfWellKnownAddress = _LecsConfWellKnownAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 10),
    _LecsConfWellKnownAddress_Type()
)
lecsConfWellKnownAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsConfWellKnownAddress.setStatus("current")
_LecsStatGroup_ObjectIdentity = ObjectIdentity
lecsStatGroup = _LecsStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 2)
)
_LaneMibExtGroup_ObjectIdentity = ObjectIdentity
laneMibExtGroup = _LaneMibExtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 4, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-Lane-MIB",
    **{"LecConfigType": LecConfigType,
       "LaneDataFrameFormat": LaneDataFrameFormat,
       "LaneDataFrameSize": LaneDataFrameSize,
       "foreLaneModule": foreLaneModule,
       "laneLecGroup": laneLecGroup,
       "lecConfGroup": lecConfGroup,
       "lecDefaultLecsConfigType": lecDefaultLecsConfigType,
       "lecDefaultLecsAtmAddress": lecDefaultLecsAtmAddress,
       "lecConfTable": lecConfTable,
       "lecConfEntry": lecConfEntry,
       "lecConfIndex": lecConfIndex,
       "lecConfAtmAddress": lecConfAtmAddress,
       "lecConfAdminStatus": lecConfAdminStatus,
       "lecConfOperStatus": lecConfOperStatus,
       "lecConfElanName": lecConfElanName,
       "lecConfMacAddress": lecConfMacAddress,
       "lecConfLecsConfigType": lecConfLecsConfigType,
       "lecConfLecsAtmAddress": lecConfLecsAtmAddress,
       "lecConfLesAtmAddress": lecConfLesAtmAddress,
       "lecConfEntryStatus": lecConfEntryStatus,
       "lecConfIfName": lecConfIfName,
       "lecStatGroup": lecStatGroup,
       "lecArpGroup": lecArpGroup,
       "elarpFlush": elarpFlush,
       "lecArpTable": lecArpTable,
       "lecArpEntry": lecArpEntry,
       "lecArpMacAddress": lecArpMacAddress,
       "lecArpAtmAddress": lecArpAtmAddress,
       "lecArpFlags": lecArpFlags,
       "lecArpConnVPI": lecArpConnVPI,
       "lecArpConnVCI": lecArpConnVCI,
       "lecArpFlush": lecArpFlush,
       "lecArpElanName": lecArpElanName,
       "laneLesGroup": laneLesGroup,
       "lesConfGroup": lesConfGroup,
       "lesConfTable": lesConfTable,
       "lesConfEntry": lesConfEntry,
       "lesConfIndex": lesConfIndex,
       "lesConfAtmAddress": lesConfAtmAddress,
       "lesConfAdminStatus": lesConfAdminStatus,
       "lesConfOperStatus": lesConfOperStatus,
       "lesConfElanName": lesConfElanName,
       "lesConfBusAtmAddress": lesConfBusAtmAddress,
       "lesConfBusMaster": lesConfBusMaster,
       "lesConfEntryStatus": lesConfEntryStatus,
       "lesConfLanType": lesConfLanType,
       "lesConfMaxFrameSize": lesConfMaxFrameSize,
       "lesConfSecureServer": lesConfSecureServer,
       "lesConfLECSAtmAddress": lesConfLECSAtmAddress,
       "lesConfAnycastAtmAddress": lesConfAnycastAtmAddress,
       "lesConfRegisterTLVs": lesConfRegisterTLVs,
       "lesConfElanId": lesConfElanId,
       "lesConfTokenRingNumber": lesConfTokenRingNumber,
       "lesConfForwardArp": lesConfForwardArp,
       "lesLnniConfTable": lesLnniConfTable,
       "lesLnniConfEntry": lesLnniConfEntry,
       "lesLnniConfAtmAddress": lesLnniConfAtmAddress,
       "lesLnniConfEntryStatus": lesLnniConfEntryStatus,
       "lesLeqGroup": lesLeqGroup,
       "lesLeqConfLesId": lesLeqConfLesId,
       "lesLeqTableReload": lesLeqTableReload,
       "lesLeqStatLesId": lesLeqStatLesId,
       "lesLeqLastTime": lesLeqLastTime,
       "lesLeqTable": lesLeqTable,
       "lesLeqEntry": lesLeqEntry,
       "lesLeqIndex": lesLeqIndex,
       "lesLeqNsap": lesLeqNsap,
       "lesLeqName": lesLeqName,
       "lesStatGroup": lesStatGroup,
       "laneBusGroup": laneBusGroup,
       "busConfGroup": busConfGroup,
       "busConfTable": busConfTable,
       "busConfEntry": busConfEntry,
       "busConfIndex": busConfIndex,
       "busConfAtmAddress": busConfAtmAddress,
       "busConfAdminStatus": busConfAdminStatus,
       "busConfOperStatus": busConfOperStatus,
       "busConfName": busConfName,
       "busConfEntryStatus": busConfEntryStatus,
       "busConfLanType": busConfLanType,
       "busConfMaxFrameSize": busConfMaxFrameSize,
       "busStatGroup": busStatGroup,
       "laneLecsGroup": laneLecsGroup,
       "lecsConfGroup": lecsConfGroup,
       "lecsConfTable": lecsConfTable,
       "lecsConfEntry": lecsConfEntry,
       "lecsConfIndex": lecsConfIndex,
       "lecsConfAtmAddress": lecsConfAtmAddress,
       "lecsConfAdminStatus": lecsConfAdminStatus,
       "lecsConfOperStatus": lecsConfOperStatus,
       "lecsConfDatabase": lecsConfDatabase,
       "lecsConfEntryStatus": lecsConfEntryStatus,
       "lecsConfDefaultLesFlag": lecsConfDefaultLesFlag,
       "lecsConfDefaultLesAtmAddress": lecsConfDefaultLesAtmAddress,
       "lecsConfWellKnownAddressFlag": lecsConfWellKnownAddressFlag,
       "lecsConfWellKnownAddress": lecsConfWellKnownAddress,
       "lecsStatGroup": lecsStatGroup,
       "laneMibExtGroup": laneMibExtGroup}
)
