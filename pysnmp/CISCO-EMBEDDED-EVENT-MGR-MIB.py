# SNMP MIB module (CISCO-EMBEDDED-EVENT-MGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-EMBEDDED-EVENT-MGR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:19 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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

cEventMgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 134)
)
cEventMgrMIB.setRevisions(
        ("2006-11-07 00:00",
         "2003-04-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NotifySource(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("policy", 2),
          ("server", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CEventMgrMIBNotif_ObjectIdentity = ObjectIdentity
cEventMgrMIBNotif = _CEventMgrMIBNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 0)
)
_CEventMgrMIBObjects_ObjectIdentity = ObjectIdentity
cEventMgrMIBObjects = _CEventMgrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1)
)
_CeemEventMap_ObjectIdentity = ObjectIdentity
ceemEventMap = _CeemEventMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 1)
)
_CeemEventMapTable_Object = MibTable
ceemEventMapTable = _CeemEventMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ceemEventMapTable.setStatus("current")
_CeemEventMapEntry_Object = MibTableRow
ceemEventMapEntry = _CeemEventMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 1, 1, 1)
)
ceemEventMapEntry.setIndexNames(
    (0, "CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemEventIndex"),
)
if mibBuilder.loadTexts:
    ceemEventMapEntry.setStatus("current")
_CeemEventIndex_Type = Unsigned32
_CeemEventIndex_Object = MibTableColumn
ceemEventIndex = _CeemEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 1, 1, 1, 1),
    _CeemEventIndex_Type()
)
ceemEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceemEventIndex.setStatus("current")


class _CeemEventName_Type(SnmpAdminString):
    """Custom type ceemEventName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CeemEventName_Type.__name__ = "SnmpAdminString"
_CeemEventName_Object = MibTableColumn
ceemEventName = _CeemEventName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 1, 1, 1, 2),
    _CeemEventName_Type()
)
ceemEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemEventName.setStatus("current")
_CeemEventDescrText_Type = SnmpAdminString
_CeemEventDescrText_Object = MibTableColumn
ceemEventDescrText = _CeemEventDescrText_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 1, 1, 1, 3),
    _CeemEventDescrText_Type()
)
ceemEventDescrText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemEventDescrText.setStatus("current")
_CeemHistory_ObjectIdentity = ObjectIdentity
ceemHistory = _CeemHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2)
)


class _CeemHistoryMaxEventEntries_Type(Integer32):
    """Custom type ceemHistoryMaxEventEntries based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_CeemHistoryMaxEventEntries_Type.__name__ = "Integer32"
_CeemHistoryMaxEventEntries_Object = MibScalar
ceemHistoryMaxEventEntries = _CeemHistoryMaxEventEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 1),
    _CeemHistoryMaxEventEntries_Type()
)
ceemHistoryMaxEventEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceemHistoryMaxEventEntries.setStatus("current")


class _CeemHistoryLastEventEntry_Type(Unsigned32):
    """Custom type ceemHistoryLastEventEntry based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CeemHistoryLastEventEntry_Type.__name__ = "Unsigned32"
_CeemHistoryLastEventEntry_Object = MibScalar
ceemHistoryLastEventEntry = _CeemHistoryLastEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 2),
    _CeemHistoryLastEventEntry_Type()
)
ceemHistoryLastEventEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemHistoryLastEventEntry.setStatus("current")
_CeemHistoryEventTable_Object = MibTable
ceemHistoryEventTable = _CeemHistoryEventTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ceemHistoryEventTable.setStatus("current")
_CeemHistoryEventEntry_Object = MibTableRow
ceemHistoryEventEntry = _CeemHistoryEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1)
)
ceemHistoryEventEntry.setIndexNames(
    (0, "CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventIndex"),
)
if mibBuilder.loadTexts:
    ceemHistoryEventEntry.setStatus("current")


class _CeemHistoryEventIndex_Type(Unsigned32):
    """Custom type ceemHistoryEventIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CeemHistoryEventIndex_Type.__name__ = "Unsigned32"
_CeemHistoryEventIndex_Object = MibTableColumn
ceemHistoryEventIndex = _CeemHistoryEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 1),
    _CeemHistoryEventIndex_Type()
)
ceemHistoryEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceemHistoryEventIndex.setStatus("current")
_CeemHistoryEventType1_Type = Unsigned32
_CeemHistoryEventType1_Object = MibTableColumn
ceemHistoryEventType1 = _CeemHistoryEventType1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 2),
    _CeemHistoryEventType1_Type()
)
ceemHistoryEventType1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemHistoryEventType1.setStatus("current")
_CeemHistoryEventType2_Type = Unsigned32
_CeemHistoryEventType2_Object = MibTableColumn
ceemHistoryEventType2 = _CeemHistoryEventType2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 3),
    _CeemHistoryEventType2_Type()
)
ceemHistoryEventType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemHistoryEventType2.setStatus("current")
_CeemHistoryEventType3_Type = Unsigned32
_CeemHistoryEventType3_Object = MibTableColumn
ceemHistoryEventType3 = _CeemHistoryEventType3_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 4),
    _CeemHistoryEventType3_Type()
)
ceemHistoryEventType3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemHistoryEventType3.setStatus("current")
_CeemHistoryEventType4_Type = Unsigned32
_CeemHistoryEventType4_Object = MibTableColumn
ceemHistoryEventType4 = _CeemHistoryEventType4_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 5),
    _CeemHistoryEventType4_Type()
)
ceemHistoryEventType4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemHistoryEventType4.setStatus("current")


class _CeemHistoryPolicyPath_Type(SnmpAdminString):
    """Custom type ceemHistoryPolicyPath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CeemHistoryPolicyPath_Type.__name__ = "SnmpAdminString"
_CeemHistoryPolicyPath_Object = MibTableColumn
ceemHistoryPolicyPath = _CeemHistoryPolicyPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 6),
    _CeemHistoryPolicyPath_Type()
)
ceemHistoryPolicyPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemHistoryPolicyPath.setStatus("current")


class _CeemHistoryPolicyName_Type(SnmpAdminString):
    """Custom type ceemHistoryPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CeemHistoryPolicyName_Type.__name__ = "SnmpAdminString"
_CeemHistoryPolicyName_Object = MibTableColumn
ceemHistoryPolicyName = _CeemHistoryPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 7),
    _CeemHistoryPolicyName_Type()
)
ceemHistoryPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemHistoryPolicyName.setStatus("current")


class _CeemHistoryPolicyExitStatus_Type(Integer32):
    """Custom type ceemHistoryPolicyExitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CeemHistoryPolicyExitStatus_Type.__name__ = "Integer32"
_CeemHistoryPolicyExitStatus_Object = MibTableColumn
ceemHistoryPolicyExitStatus = _CeemHistoryPolicyExitStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 8),
    _CeemHistoryPolicyExitStatus_Type()
)
ceemHistoryPolicyExitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemHistoryPolicyExitStatus.setStatus("current")


class _CeemHistoryPolicyIntData1_Type(Integer32):
    """Custom type ceemHistoryPolicyIntData1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CeemHistoryPolicyIntData1_Type.__name__ = "Integer32"
_CeemHistoryPolicyIntData1_Object = MibTableColumn
ceemHistoryPolicyIntData1 = _CeemHistoryPolicyIntData1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 9),
    _CeemHistoryPolicyIntData1_Type()
)
ceemHistoryPolicyIntData1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemHistoryPolicyIntData1.setStatus("current")


class _CeemHistoryPolicyIntData2_Type(Integer32):
    """Custom type ceemHistoryPolicyIntData2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CeemHistoryPolicyIntData2_Type.__name__ = "Integer32"
_CeemHistoryPolicyIntData2_Object = MibTableColumn
ceemHistoryPolicyIntData2 = _CeemHistoryPolicyIntData2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 10),
    _CeemHistoryPolicyIntData2_Type()
)
ceemHistoryPolicyIntData2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemHistoryPolicyIntData2.setStatus("current")


class _CeemHistoryPolicyStrData_Type(SnmpAdminString):
    """Custom type ceemHistoryPolicyStrData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CeemHistoryPolicyStrData_Type.__name__ = "SnmpAdminString"
_CeemHistoryPolicyStrData_Object = MibTableColumn
ceemHistoryPolicyStrData = _CeemHistoryPolicyStrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 11),
    _CeemHistoryPolicyStrData_Type()
)
ceemHistoryPolicyStrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemHistoryPolicyStrData.setStatus("current")
_CeemHistoryNotifyType_Type = NotifySource
_CeemHistoryNotifyType_Object = MibTableColumn
ceemHistoryNotifyType = _CeemHistoryNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 12),
    _CeemHistoryNotifyType_Type()
)
ceemHistoryNotifyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemHistoryNotifyType.setStatus("current")
_CeemHistoryEventType5_Type = Unsigned32
_CeemHistoryEventType5_Object = MibTableColumn
ceemHistoryEventType5 = _CeemHistoryEventType5_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 13),
    _CeemHistoryEventType5_Type()
)
ceemHistoryEventType5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemHistoryEventType5.setStatus("current")
_CeemHistoryEventType6_Type = Unsigned32
_CeemHistoryEventType6_Object = MibTableColumn
ceemHistoryEventType6 = _CeemHistoryEventType6_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 14),
    _CeemHistoryEventType6_Type()
)
ceemHistoryEventType6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemHistoryEventType6.setStatus("current")
_CeemHistoryEventType7_Type = Unsigned32
_CeemHistoryEventType7_Object = MibTableColumn
ceemHistoryEventType7 = _CeemHistoryEventType7_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 15),
    _CeemHistoryEventType7_Type()
)
ceemHistoryEventType7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemHistoryEventType7.setStatus("current")
_CeemHistoryEventType8_Type = Unsigned32
_CeemHistoryEventType8_Object = MibTableColumn
ceemHistoryEventType8 = _CeemHistoryEventType8_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 16),
    _CeemHistoryEventType8_Type()
)
ceemHistoryEventType8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemHistoryEventType8.setStatus("current")
_CeemRegisteredPolicy_ObjectIdentity = ObjectIdentity
ceemRegisteredPolicy = _CeemRegisteredPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3)
)
_CeemRegisteredPolicyTable_Object = MibTable
ceemRegisteredPolicyTable = _CeemRegisteredPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ceemRegisteredPolicyTable.setStatus("current")
_CeemRegisteredPolicyEntry_Object = MibTableRow
ceemRegisteredPolicyEntry = _CeemRegisteredPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1)
)
ceemRegisteredPolicyEntry.setIndexNames(
    (0, "CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyIndex"),
)
if mibBuilder.loadTexts:
    ceemRegisteredPolicyEntry.setStatus("current")
_CeemRegisteredPolicyIndex_Type = Unsigned32
_CeemRegisteredPolicyIndex_Object = MibTableColumn
ceemRegisteredPolicyIndex = _CeemRegisteredPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 1),
    _CeemRegisteredPolicyIndex_Type()
)
ceemRegisteredPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceemRegisteredPolicyIndex.setStatus("current")


class _CeemRegisteredPolicyName_Type(SnmpAdminString):
    """Custom type ceemRegisteredPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CeemRegisteredPolicyName_Type.__name__ = "SnmpAdminString"
_CeemRegisteredPolicyName_Object = MibTableColumn
ceemRegisteredPolicyName = _CeemRegisteredPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 2),
    _CeemRegisteredPolicyName_Type()
)
ceemRegisteredPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemRegisteredPolicyName.setStatus("current")
_CeemRegisteredPolicyEventType1_Type = Unsigned32
_CeemRegisteredPolicyEventType1_Object = MibTableColumn
ceemRegisteredPolicyEventType1 = _CeemRegisteredPolicyEventType1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 3),
    _CeemRegisteredPolicyEventType1_Type()
)
ceemRegisteredPolicyEventType1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemRegisteredPolicyEventType1.setStatus("current")
_CeemRegisteredPolicyEventType2_Type = Unsigned32
_CeemRegisteredPolicyEventType2_Object = MibTableColumn
ceemRegisteredPolicyEventType2 = _CeemRegisteredPolicyEventType2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 4),
    _CeemRegisteredPolicyEventType2_Type()
)
ceemRegisteredPolicyEventType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemRegisteredPolicyEventType2.setStatus("current")
_CeemRegisteredPolicyEventType3_Type = Unsigned32
_CeemRegisteredPolicyEventType3_Object = MibTableColumn
ceemRegisteredPolicyEventType3 = _CeemRegisteredPolicyEventType3_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 5),
    _CeemRegisteredPolicyEventType3_Type()
)
ceemRegisteredPolicyEventType3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemRegisteredPolicyEventType3.setStatus("current")
_CeemRegisteredPolicyEventType4_Type = Unsigned32
_CeemRegisteredPolicyEventType4_Object = MibTableColumn
ceemRegisteredPolicyEventType4 = _CeemRegisteredPolicyEventType4_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 6),
    _CeemRegisteredPolicyEventType4_Type()
)
ceemRegisteredPolicyEventType4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemRegisteredPolicyEventType4.setStatus("current")


class _CeemRegisteredPolicyStatus_Type(Integer32):
    """Custom type ceemRegisteredPolicyStatus based on Integer32"""
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


_CeemRegisteredPolicyStatus_Type.__name__ = "Integer32"
_CeemRegisteredPolicyStatus_Object = MibTableColumn
ceemRegisteredPolicyStatus = _CeemRegisteredPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 7),
    _CeemRegisteredPolicyStatus_Type()
)
ceemRegisteredPolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemRegisteredPolicyStatus.setStatus("current")


class _CeemRegisteredPolicyType_Type(Integer32):
    """Custom type ceemRegisteredPolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 2),
          ("user", 1))
    )


_CeemRegisteredPolicyType_Type.__name__ = "Integer32"
_CeemRegisteredPolicyType_Object = MibTableColumn
ceemRegisteredPolicyType = _CeemRegisteredPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 8),
    _CeemRegisteredPolicyType_Type()
)
ceemRegisteredPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemRegisteredPolicyType.setStatus("current")
_CeemRegisteredPolicyNotifFlag_Type = TruthValue
_CeemRegisteredPolicyNotifFlag_Object = MibTableColumn
ceemRegisteredPolicyNotifFlag = _CeemRegisteredPolicyNotifFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 9),
    _CeemRegisteredPolicyNotifFlag_Type()
)
ceemRegisteredPolicyNotifFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemRegisteredPolicyNotifFlag.setStatus("current")
_CeemRegisteredPolicyRegTime_Type = DateAndTime
_CeemRegisteredPolicyRegTime_Object = MibTableColumn
ceemRegisteredPolicyRegTime = _CeemRegisteredPolicyRegTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 10),
    _CeemRegisteredPolicyRegTime_Type()
)
ceemRegisteredPolicyRegTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemRegisteredPolicyRegTime.setStatus("current")
_CeemRegisteredPolicyEnabledTime_Type = DateAndTime
_CeemRegisteredPolicyEnabledTime_Object = MibTableColumn
ceemRegisteredPolicyEnabledTime = _CeemRegisteredPolicyEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 11),
    _CeemRegisteredPolicyEnabledTime_Type()
)
ceemRegisteredPolicyEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemRegisteredPolicyEnabledTime.setStatus("current")
_CeemRegisteredPolicyRunTime_Type = DateAndTime
_CeemRegisteredPolicyRunTime_Object = MibTableColumn
ceemRegisteredPolicyRunTime = _CeemRegisteredPolicyRunTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 12),
    _CeemRegisteredPolicyRunTime_Type()
)
ceemRegisteredPolicyRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemRegisteredPolicyRunTime.setStatus("current")
_CeemRegisteredPolicyRunCount_Type = Counter32
_CeemRegisteredPolicyRunCount_Object = MibTableColumn
ceemRegisteredPolicyRunCount = _CeemRegisteredPolicyRunCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 13),
    _CeemRegisteredPolicyRunCount_Type()
)
ceemRegisteredPolicyRunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemRegisteredPolicyRunCount.setStatus("current")
_CeemRegisteredPolicyEventType5_Type = Unsigned32
_CeemRegisteredPolicyEventType5_Object = MibTableColumn
ceemRegisteredPolicyEventType5 = _CeemRegisteredPolicyEventType5_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 14),
    _CeemRegisteredPolicyEventType5_Type()
)
ceemRegisteredPolicyEventType5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemRegisteredPolicyEventType5.setStatus("current")
_CeemRegisteredPolicyEventType6_Type = Unsigned32
_CeemRegisteredPolicyEventType6_Object = MibTableColumn
ceemRegisteredPolicyEventType6 = _CeemRegisteredPolicyEventType6_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 15),
    _CeemRegisteredPolicyEventType6_Type()
)
ceemRegisteredPolicyEventType6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemRegisteredPolicyEventType6.setStatus("current")
_CeemRegisteredPolicyEventType7_Type = Unsigned32
_CeemRegisteredPolicyEventType7_Object = MibTableColumn
ceemRegisteredPolicyEventType7 = _CeemRegisteredPolicyEventType7_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 16),
    _CeemRegisteredPolicyEventType7_Type()
)
ceemRegisteredPolicyEventType7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemRegisteredPolicyEventType7.setStatus("current")
_CeemRegisteredPolicyEventType8_Type = Unsigned32
_CeemRegisteredPolicyEventType8_Object = MibTableColumn
ceemRegisteredPolicyEventType8 = _CeemRegisteredPolicyEventType8_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 17),
    _CeemRegisteredPolicyEventType8_Type()
)
ceemRegisteredPolicyEventType8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceemRegisteredPolicyEventType8.setStatus("current")
_CEventMgrConformance_ObjectIdentity = ObjectIdentity
cEventMgrConformance = _CEventMgrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 3)
)
_CEventMgrCompliances_ObjectIdentity = ObjectIdentity
cEventMgrCompliances = _CEventMgrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 1)
)
_CEventMgrGroups_ObjectIdentity = ObjectIdentity
cEventMgrGroups = _CEventMgrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 2)
)

# Managed Objects groups

cEventMgrDescrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 2, 1)
)
cEventMgrDescrGroup.setObjects(
      *(("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemEventName"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemEventDescrText"))
)
if mibBuilder.loadTexts:
    cEventMgrDescrGroup.setStatus("current")

cEventMgrHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 2, 2)
)
cEventMgrHistoryGroup.setObjects(
      *(("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryMaxEventEntries"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryLastEventEntry"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType1"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType2"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType3"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType4"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyPath"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyName"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyExitStatus"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyIntData1"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyIntData2"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyStrData"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryNotifyType"))
)
if mibBuilder.loadTexts:
    cEventMgrHistoryGroup.setStatus("current")

cEventMgrRegisteredPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 2, 4)
)
cEventMgrRegisteredPolicyGroup.setObjects(
      *(("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyName"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEventType1"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEventType2"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEventType3"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEventType4"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyStatus"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyType"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyNotifFlag"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyRegTime"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEnabledTime"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyRunTime"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyRunCount"))
)
if mibBuilder.loadTexts:
    cEventMgrRegisteredPolicyGroup.setStatus("current")

cEventMgrHistoryGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 2, 5)
)
cEventMgrHistoryGroupSup1.setObjects(
      *(("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType5"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType6"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType7"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType8"))
)
if mibBuilder.loadTexts:
    cEventMgrHistoryGroupSup1.setStatus("current")

cEventMgrRegisteredPolicyGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 2, 6)
)
cEventMgrRegisteredPolicyGroupSup1.setObjects(
      *(("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEventType5"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEventType6"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEventType7"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEventType8"))
)
if mibBuilder.loadTexts:
    cEventMgrRegisteredPolicyGroupSup1.setStatus("current")


# Notification objects

cEventMgrServerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 0, 1)
)
cEventMgrServerEvent.setObjects(
      *(("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType1"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType2"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType3"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType4"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyPath"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyName"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyExitStatus"))
)
if mibBuilder.loadTexts:
    cEventMgrServerEvent.setStatus(
        "current"
    )

cEventMgrPolicyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 0, 2)
)
cEventMgrPolicyEvent.setObjects(
      *(("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType1"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType2"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType3"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType4"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyPath"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyName"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyIntData1"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyIntData2"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyStrData"))
)
if mibBuilder.loadTexts:
    cEventMgrPolicyEvent.setStatus(
        "current"
    )


# Notifications groups

cEventMgrNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 2, 3)
)
cEventMgrNotificationsGroup.setObjects(
      *(("CISCO-EMBEDDED-EVENT-MGR-MIB", "cEventMgrServerEvent"),
        ("CISCO-EMBEDDED-EVENT-MGR-MIB", "cEventMgrPolicyEvent"))
)
if mibBuilder.loadTexts:
    cEventMgrNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cEventMgrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cEventMgrCompliance.setStatus(
        "deprecated"
    )

cEventMgrComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cEventMgrComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-EMBEDDED-EVENT-MGR-MIB",
    **{"NotifySource": NotifySource,
       "cEventMgrMIB": cEventMgrMIB,
       "cEventMgrMIBNotif": cEventMgrMIBNotif,
       "cEventMgrServerEvent": cEventMgrServerEvent,
       "cEventMgrPolicyEvent": cEventMgrPolicyEvent,
       "cEventMgrMIBObjects": cEventMgrMIBObjects,
       "ceemEventMap": ceemEventMap,
       "ceemEventMapTable": ceemEventMapTable,
       "ceemEventMapEntry": ceemEventMapEntry,
       "ceemEventIndex": ceemEventIndex,
       "ceemEventName": ceemEventName,
       "ceemEventDescrText": ceemEventDescrText,
       "ceemHistory": ceemHistory,
       "ceemHistoryMaxEventEntries": ceemHistoryMaxEventEntries,
       "ceemHistoryLastEventEntry": ceemHistoryLastEventEntry,
       "ceemHistoryEventTable": ceemHistoryEventTable,
       "ceemHistoryEventEntry": ceemHistoryEventEntry,
       "ceemHistoryEventIndex": ceemHistoryEventIndex,
       "ceemHistoryEventType1": ceemHistoryEventType1,
       "ceemHistoryEventType2": ceemHistoryEventType2,
       "ceemHistoryEventType3": ceemHistoryEventType3,
       "ceemHistoryEventType4": ceemHistoryEventType4,
       "ceemHistoryPolicyPath": ceemHistoryPolicyPath,
       "ceemHistoryPolicyName": ceemHistoryPolicyName,
       "ceemHistoryPolicyExitStatus": ceemHistoryPolicyExitStatus,
       "ceemHistoryPolicyIntData1": ceemHistoryPolicyIntData1,
       "ceemHistoryPolicyIntData2": ceemHistoryPolicyIntData2,
       "ceemHistoryPolicyStrData": ceemHistoryPolicyStrData,
       "ceemHistoryNotifyType": ceemHistoryNotifyType,
       "ceemHistoryEventType5": ceemHistoryEventType5,
       "ceemHistoryEventType6": ceemHistoryEventType6,
       "ceemHistoryEventType7": ceemHistoryEventType7,
       "ceemHistoryEventType8": ceemHistoryEventType8,
       "ceemRegisteredPolicy": ceemRegisteredPolicy,
       "ceemRegisteredPolicyTable": ceemRegisteredPolicyTable,
       "ceemRegisteredPolicyEntry": ceemRegisteredPolicyEntry,
       "ceemRegisteredPolicyIndex": ceemRegisteredPolicyIndex,
       "ceemRegisteredPolicyName": ceemRegisteredPolicyName,
       "ceemRegisteredPolicyEventType1": ceemRegisteredPolicyEventType1,
       "ceemRegisteredPolicyEventType2": ceemRegisteredPolicyEventType2,
       "ceemRegisteredPolicyEventType3": ceemRegisteredPolicyEventType3,
       "ceemRegisteredPolicyEventType4": ceemRegisteredPolicyEventType4,
       "ceemRegisteredPolicyStatus": ceemRegisteredPolicyStatus,
       "ceemRegisteredPolicyType": ceemRegisteredPolicyType,
       "ceemRegisteredPolicyNotifFlag": ceemRegisteredPolicyNotifFlag,
       "ceemRegisteredPolicyRegTime": ceemRegisteredPolicyRegTime,
       "ceemRegisteredPolicyEnabledTime": ceemRegisteredPolicyEnabledTime,
       "ceemRegisteredPolicyRunTime": ceemRegisteredPolicyRunTime,
       "ceemRegisteredPolicyRunCount": ceemRegisteredPolicyRunCount,
       "ceemRegisteredPolicyEventType5": ceemRegisteredPolicyEventType5,
       "ceemRegisteredPolicyEventType6": ceemRegisteredPolicyEventType6,
       "ceemRegisteredPolicyEventType7": ceemRegisteredPolicyEventType7,
       "ceemRegisteredPolicyEventType8": ceemRegisteredPolicyEventType8,
       "cEventMgrConformance": cEventMgrConformance,
       "cEventMgrCompliances": cEventMgrCompliances,
       "cEventMgrCompliance": cEventMgrCompliance,
       "cEventMgrComplianceRev1": cEventMgrComplianceRev1,
       "cEventMgrGroups": cEventMgrGroups,
       "cEventMgrDescrGroup": cEventMgrDescrGroup,
       "cEventMgrHistoryGroup": cEventMgrHistoryGroup,
       "cEventMgrNotificationsGroup": cEventMgrNotificationsGroup,
       "cEventMgrRegisteredPolicyGroup": cEventMgrRegisteredPolicyGroup,
       "cEventMgrHistoryGroupSup1": cEventMgrHistoryGroupSup1,
       "cEventMgrRegisteredPolicyGroupSup1": cEventMgrRegisteredPolicyGroupSup1}
)
