# SNMP MIB module (PBC-GENERIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PBC-GENERIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:59 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(pbcCaps,
 pbcManagement,
 pbcModuleRegs) = mibBuilder.importSymbols(
    "PBC-ENT-MIB",
    "pbcCaps",
    "pbcManagement",
    "pbcModuleRegs")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

pbcGenericSystemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cableDS", 1),
          ("cableUS", 2),
          ("cableUsLogical", 7),
          ("fastEthernet", 3),
          ("gigabitEthernet", 4),
          ("notApplicable", 0),
          ("rs232", 6),
          ("tenGigabitEthernet", 5))
    )



class ChgHistoryDataPath(Integer32, TextualConvention):
    status = "current"
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
        *(("cmdSource", 2),
          ("erase", 1),
          ("local", 6),
          ("operational", 4),
          ("startup", 3),
          ("tftp", 5))
    )



# MIB Managed Objects in the order of their OIDs

_PbcGeneric_ObjectIdentity = ObjectIdentity
pbcGeneric = _PbcGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1)
)
_PbcChassis_ObjectIdentity = ObjectIdentity
pbcChassis = _PbcChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1)
)
_PbcChassisEntityIndex_Type = Unsigned32
_PbcChassisEntityIndex_Object = MibScalar
pbcChassisEntityIndex = _PbcChassisEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 1),
    _PbcChassisEntityIndex_Type()
)
pbcChassisEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcChassisEntityIndex.setStatus("current")


class _PbcChassisOperStatus_Type(Integer32):
    """Custom type pbcChassisOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("failure", 6),
          ("initializing", 7),
          ("operational", 1),
          ("standby", 4),
          ("testing", 5),
          ("unconfigured", 8))
    )


_PbcChassisOperStatus_Type.__name__ = "Integer32"
_PbcChassisOperStatus_Object = MibScalar
pbcChassisOperStatus = _PbcChassisOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 2),
    _PbcChassisOperStatus_Type()
)
pbcChassisOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcChassisOperStatus.setStatus("current")
_PbcChassisSlots_Type = Unsigned32
_PbcChassisSlots_Object = MibScalar
pbcChassisSlots = _PbcChassisSlots_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 3),
    _PbcChassisSlots_Type()
)
pbcChassisSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcChassisSlots.setStatus("current")
_PbcContactInfo_Type = DisplayString
_PbcContactInfo_Object = MibScalar
pbcContactInfo = _PbcContactInfo_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 4),
    _PbcContactInfo_Type()
)
pbcContactInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcContactInfo.setStatus("current")
_PbcHostName_Type = DisplayString
_PbcHostName_Object = MibScalar
pbcHostName = _PbcHostName_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 5),
    _PbcHostName_Type()
)
pbcHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcHostName.setStatus("current")
_PbcDomainName_Type = DisplayString
_PbcDomainName_Object = MibScalar
pbcDomainName = _PbcDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 6),
    _PbcDomainName_Type()
)
pbcDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcDomainName.setStatus("current")


class _PbcDateTimeOfLastChange_Type(DateAndTime):
    """Custom type pbcDateTimeOfLastChange based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_PbcDateTimeOfLastChange_Object = MibScalar
pbcDateTimeOfLastChange = _PbcDateTimeOfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 7),
    _PbcDateTimeOfLastChange_Type()
)
pbcDateTimeOfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcDateTimeOfLastChange.setStatus("current")
_PbcCardIfIndexTableNumEntries_Type = Unsigned32
_PbcCardIfIndexTableNumEntries_Object = MibScalar
pbcCardIfIndexTableNumEntries = _PbcCardIfIndexTableNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 8),
    _PbcCardIfIndexTableNumEntries_Type()
)
pbcCardIfIndexTableNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCardIfIndexTableNumEntries.setStatus("current")
_PbcCardIfIndexTable_Object = MibTable
pbcCardIfIndexTable = _PbcCardIfIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 9)
)
if mibBuilder.loadTexts:
    pbcCardIfIndexTable.setStatus("current")
_PbcCardIfIndexEntry_Object = MibTableRow
pbcCardIfIndexEntry = _PbcCardIfIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 9, 1)
)
pbcCardIfIndexEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pbcCardIfIndexEntry.setStatus("current")
_PbcCardIfCardIndex_Type = Unsigned32
_PbcCardIfCardIndex_Object = MibTableColumn
pbcCardIfCardIndex = _PbcCardIfCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 9, 1, 1),
    _PbcCardIfCardIndex_Type()
)
pbcCardIfCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCardIfCardIndex.setStatus("current")
_PbcCardIfPortNumber_Type = Unsigned32
_PbcCardIfPortNumber_Object = MibTableColumn
pbcCardIfPortNumber = _PbcCardIfPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 9, 1, 2),
    _PbcCardIfPortNumber_Type()
)
pbcCardIfPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCardIfPortNumber.setStatus("current")
_PbcCardIfPortType_Type = PortType
_PbcCardIfPortType_Object = MibTableColumn
pbcCardIfPortType = _PbcCardIfPortType_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 9, 1, 3),
    _PbcCardIfPortType_Type()
)
pbcCardIfPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCardIfPortType.setStatus("current")
_PbcCardIfSlotNumber_Type = Unsigned32
_PbcCardIfSlotNumber_Object = MibTableColumn
pbcCardIfSlotNumber = _PbcCardIfSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 9, 1, 4),
    _PbcCardIfSlotNumber_Type()
)
pbcCardIfSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCardIfSlotNumber.setStatus("current")
_PbcCardIfPortIndex_Type = Unsigned32
_PbcCardIfPortIndex_Object = MibTableColumn
pbcCardIfPortIndex = _PbcCardIfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 9, 1, 5),
    _PbcCardIfPortIndex_Type()
)
pbcCardIfPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCardIfPortIndex.setStatus("current")
_PbcCardTableNumEntries_Type = Unsigned32
_PbcCardTableNumEntries_Object = MibScalar
pbcCardTableNumEntries = _PbcCardTableNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 10),
    _PbcCardTableNumEntries_Type()
)
pbcCardTableNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCardTableNumEntries.setStatus("current")
_PbcCardTable_Object = MibTable
pbcCardTable = _PbcCardTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11)
)
if mibBuilder.loadTexts:
    pbcCardTable.setStatus("current")
_PbcCardEntry_Object = MibTableRow
pbcCardEntry = _PbcCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1)
)
pbcCardEntry.setIndexNames(
    (0, "PBC-GENERIC-MIB", "pbcCardIfCardIndex"),
)
if mibBuilder.loadTexts:
    pbcCardEntry.setStatus("current")
_PbcCardSlotNumber_Type = Unsigned32
_PbcCardSlotNumber_Object = MibTableColumn
pbcCardSlotNumber = _PbcCardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 1),
    _PbcCardSlotNumber_Type()
)
pbcCardSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCardSlotNumber.setStatus("current")
_PbcCardEntityIndex_Type = Unsigned32
_PbcCardEntityIndex_Object = MibTableColumn
pbcCardEntityIndex = _PbcCardEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 2),
    _PbcCardEntityIndex_Type()
)
pbcCardEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCardEntityIndex.setStatus("current")


class _PbcCardAdminStatus_Type(Integer32):
    """Custom type pbcCardAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("reset", 4),
          ("testing", 3),
          ("up", 1))
    )


_PbcCardAdminStatus_Type.__name__ = "Integer32"
_PbcCardAdminStatus_Object = MibTableColumn
pbcCardAdminStatus = _PbcCardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 3),
    _PbcCardAdminStatus_Type()
)
pbcCardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCardAdminStatus.setStatus("current")


class _PbcCardOperStatus_Type(Integer32):
    """Custom type pbcCardOperStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("failure", 6),
          ("initializing", 7),
          ("notPresent", 8),
          ("operational", 2),
          ("standby", 4),
          ("testing", 5),
          ("unspecified", 1))
    )


_PbcCardOperStatus_Type.__name__ = "Integer32"
_PbcCardOperStatus_Object = MibTableColumn
pbcCardOperStatus = _PbcCardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 4),
    _PbcCardOperStatus_Type()
)
pbcCardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCardOperStatus.setStatus("current")
_PbcCardUpTime_Type = TimeTicks
_PbcCardUpTime_Object = MibTableColumn
pbcCardUpTime = _PbcCardUpTime_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 5),
    _PbcCardUpTime_Type()
)
pbcCardUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCardUpTime.setStatus("current")
_PbcCardnvRAMSize_Type = Unsigned32
_PbcCardnvRAMSize_Object = MibTableColumn
pbcCardnvRAMSize = _PbcCardnvRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 6),
    _PbcCardnvRAMSize_Type()
)
pbcCardnvRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCardnvRAMSize.setStatus("current")
_PbcCardNumPorts_Type = Unsigned32
_PbcCardNumPorts_Object = MibTableColumn
pbcCardNumPorts = _PbcCardNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 7),
    _PbcCardNumPorts_Type()
)
pbcCardNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCardNumPorts.setStatus("current")


class _PbcCardType_Type(Integer32):
    """Custom type pbcCardType based on Integer32"""
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
        *(("ccm", 1),
          ("dm", 2),
          ("nic", 3),
          ("rim", 4),
          ("sim", 5))
    )


_PbcCardType_Type.__name__ = "Integer32"
_PbcCardType_Object = MibTableColumn
pbcCardType = _PbcCardType_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 8),
    _PbcCardType_Type()
)
pbcCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCardType.setStatus("current")


class _PbcCardPosition_Type(Integer32):
    """Custom type pbcCardPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("front", 1),
          ("rear", 2))
    )


_PbcCardPosition_Type.__name__ = "Integer32"
_PbcCardPosition_Object = MibTableColumn
pbcCardPosition = _PbcCardPosition_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 9),
    _PbcCardPosition_Type()
)
pbcCardPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCardPosition.setStatus("current")
_PbcCardPortTable_Object = MibTable
pbcCardPortTable = _PbcCardPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 12)
)
if mibBuilder.loadTexts:
    pbcCardPortTable.setStatus("current")
_PbcCardPortEntry_Object = MibTableRow
pbcCardPortEntry = _PbcCardPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 12, 1)
)
pbcCardPortEntry.setIndexNames(
    (0, "PBC-GENERIC-MIB", "pbcCardIfCardIndex"),
    (0, "PBC-GENERIC-MIB", "pbcCardIfPortIndex"),
)
if mibBuilder.loadTexts:
    pbcCardPortEntry.setStatus("current")


class _PbcCardPortStatus_Type(Integer32):
    """Custom type pbcCardPortStatus based on Integer32"""
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
        *(("active", 2),
          ("disabled", 4),
          ("notPresent", 5),
          ("standby", 3),
          ("unknown", 1))
    )


_PbcCardPortStatus_Type.__name__ = "Integer32"
_PbcCardPortStatus_Object = MibTableColumn
pbcCardPortStatus = _PbcCardPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 12, 1, 1),
    _PbcCardPortStatus_Type()
)
pbcCardPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCardPortStatus.setStatus("current")
_PbcCardPortEntityIndex_Type = Unsigned32
_PbcCardPortEntityIndex_Object = MibTableColumn
pbcCardPortEntityIndex = _PbcCardPortEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 12, 1, 2),
    _PbcCardPortEntityIndex_Type()
)
pbcCardPortEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCardPortEntityIndex.setStatus("current")
_PbcCardPortAlias_Type = DisplayString
_PbcCardPortAlias_Object = MibTableColumn
pbcCardPortAlias = _PbcCardPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 12, 1, 3),
    _PbcCardPortAlias_Type()
)
pbcCardPortAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCardPortAlias.setStatus("current")
_PbcPortIfTable_Object = MibTable
pbcPortIfTable = _PbcPortIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 13)
)
if mibBuilder.loadTexts:
    pbcPortIfTable.setStatus("current")
_PbcPortIfEntry_Object = MibTableRow
pbcPortIfEntry = _PbcPortIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 13, 1)
)
pbcPortIfEntry.setIndexNames(
    (0, "PBC-GENERIC-MIB", "pbcCardIfPortIndex"),
    (0, "PBC-GENERIC-MIB", "pbcPortIfIndex"),
)
if mibBuilder.loadTexts:
    pbcPortIfEntry.setStatus("current")
_PbcPortIfIndex_Type = InterfaceIndex
_PbcPortIfIndex_Object = MibTableColumn
pbcPortIfIndex = _PbcPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 13, 1, 1),
    _PbcPortIfIndex_Type()
)
pbcPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcPortIfIndex.setStatus("current")
_PbcGenericConformance_ObjectIdentity = ObjectIdentity
pbcGenericConformance = _PbcGenericConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 2)
)
_PbcGenericGroups_ObjectIdentity = ObjectIdentity
pbcGenericGroups = _PbcGenericGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 2, 1)
)
_PbcGenericCompliance_ObjectIdentity = ObjectIdentity
pbcGenericCompliance = _PbcGenericCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 2, 2)
)

# Managed Objects groups

pbcChassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 2, 1, 1)
)
pbcChassisGroup.setObjects(
      *(("PBC-GENERIC-MIB", "pbcChassisEntityIndex"),
        ("PBC-GENERIC-MIB", "pbcChassisOperStatus"),
        ("PBC-GENERIC-MIB", "pbcChassisSlots"),
        ("PBC-GENERIC-MIB", "pbcContactInfo"),
        ("PBC-GENERIC-MIB", "pbcHostName"),
        ("PBC-GENERIC-MIB", "pbcDomainName"),
        ("PBC-GENERIC-MIB", "pbcDateTimeOfLastChange"),
        ("PBC-GENERIC-MIB", "pbcCardIfIndexTableNumEntries"),
        ("PBC-GENERIC-MIB", "pbcCardIfCardIndex"),
        ("PBC-GENERIC-MIB", "pbcCardIfPortNumber"),
        ("PBC-GENERIC-MIB", "pbcCardIfPortType"),
        ("PBC-GENERIC-MIB", "pbcCardIfSlotNumber"),
        ("PBC-GENERIC-MIB", "pbcCardAdminStatus"),
        ("PBC-GENERIC-MIB", "pbcCardTableNumEntries"),
        ("PBC-GENERIC-MIB", "pbcCardSlotNumber"),
        ("PBC-GENERIC-MIB", "pbcCardEntityIndex"),
        ("PBC-GENERIC-MIB", "pbcCardOperStatus"),
        ("PBC-GENERIC-MIB", "pbcCardUpTime"),
        ("PBC-GENERIC-MIB", "pbcCardnvRAMSize"),
        ("PBC-GENERIC-MIB", "pbcCardNumPorts"),
        ("PBC-GENERIC-MIB", "pbcCardPortStatus"),
        ("PBC-GENERIC-MIB", "pbcCardPortEntityIndex"),
        ("PBC-GENERIC-MIB", "pbcCardType"),
        ("PBC-GENERIC-MIB", "pbcCardPosition"),
        ("PBC-GENERIC-MIB", "pbcCardPortAlias"),
        ("PBC-GENERIC-MIB", "pbcPortIfIndex"),
        ("PBC-GENERIC-MIB", "pbcCardIfPortIndex"))
)
if mibBuilder.loadTexts:
    pbcChassisGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pbcGenericBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5987, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pbcGenericBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PBC-GENERIC-MIB",
    **{"PortType": PortType,
       "ChgHistoryDataPath": ChgHistoryDataPath,
       "pbcGenericSystemMib": pbcGenericSystemMib,
       "pbcGeneric": pbcGeneric,
       "pbcChassis": pbcChassis,
       "pbcChassisEntityIndex": pbcChassisEntityIndex,
       "pbcChassisOperStatus": pbcChassisOperStatus,
       "pbcChassisSlots": pbcChassisSlots,
       "pbcContactInfo": pbcContactInfo,
       "pbcHostName": pbcHostName,
       "pbcDomainName": pbcDomainName,
       "pbcDateTimeOfLastChange": pbcDateTimeOfLastChange,
       "pbcCardIfIndexTableNumEntries": pbcCardIfIndexTableNumEntries,
       "pbcCardIfIndexTable": pbcCardIfIndexTable,
       "pbcCardIfIndexEntry": pbcCardIfIndexEntry,
       "pbcCardIfCardIndex": pbcCardIfCardIndex,
       "pbcCardIfPortNumber": pbcCardIfPortNumber,
       "pbcCardIfPortType": pbcCardIfPortType,
       "pbcCardIfSlotNumber": pbcCardIfSlotNumber,
       "pbcCardIfPortIndex": pbcCardIfPortIndex,
       "pbcCardTableNumEntries": pbcCardTableNumEntries,
       "pbcCardTable": pbcCardTable,
       "pbcCardEntry": pbcCardEntry,
       "pbcCardSlotNumber": pbcCardSlotNumber,
       "pbcCardEntityIndex": pbcCardEntityIndex,
       "pbcCardAdminStatus": pbcCardAdminStatus,
       "pbcCardOperStatus": pbcCardOperStatus,
       "pbcCardUpTime": pbcCardUpTime,
       "pbcCardnvRAMSize": pbcCardnvRAMSize,
       "pbcCardNumPorts": pbcCardNumPorts,
       "pbcCardType": pbcCardType,
       "pbcCardPosition": pbcCardPosition,
       "pbcCardPortTable": pbcCardPortTable,
       "pbcCardPortEntry": pbcCardPortEntry,
       "pbcCardPortStatus": pbcCardPortStatus,
       "pbcCardPortEntityIndex": pbcCardPortEntityIndex,
       "pbcCardPortAlias": pbcCardPortAlias,
       "pbcPortIfTable": pbcPortIfTable,
       "pbcPortIfEntry": pbcPortIfEntry,
       "pbcPortIfIndex": pbcPortIfIndex,
       "pbcGenericConformance": pbcGenericConformance,
       "pbcGenericGroups": pbcGenericGroups,
       "pbcChassisGroup": pbcChassisGroup,
       "pbcGenericCompliance": pbcGenericCompliance,
       "pbcGenericBasicCompliance": pbcGenericBasicCompliance}
)
