# SNMP MIB module (CISCO-ETHER-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ETHER-CFM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:56 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 MacAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoEtherCfmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 461)
)
ciscoEtherCfmMIB.setRevisions(
        ("2004-12-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CfmMepid(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoEtherCfmMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoEtherCfmMIBNotifs = _CiscoEtherCfmMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 0)
)
_CiscoEtherCfmNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoEtherCfmNotificationPrefix = _CiscoEtherCfmNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0)
)
_CiscoEtherCfmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEtherCfmMIBObjects = _CiscoEtherCfmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1)
)
_CecCfmEvents_ObjectIdentity = ObjectIdentity
cecCfmEvents = _CecCfmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1)
)


class _CEtherCfmMaxEventIndex_Type(Unsigned32):
    """Custom type cEtherCfmMaxEventIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CEtherCfmMaxEventIndex_Type.__name__ = "Unsigned32"
_CEtherCfmMaxEventIndex_Object = MibScalar
cEtherCfmMaxEventIndex = _CEtherCfmMaxEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 1),
    _CEtherCfmMaxEventIndex_Type()
)
cEtherCfmMaxEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEtherCfmMaxEventIndex.setStatus("current")
_CEtherCfmEventTable_Object = MibTable
cEtherCfmEventTable = _CEtherCfmEventTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cEtherCfmEventTable.setStatus("current")
_CEtherCfmEventEntry_Object = MibTableRow
cEtherCfmEventEntry = _CEtherCfmEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1)
)
cEtherCfmEventEntry.setIndexNames(
    (0, "CISCO-ETHER-CFM-MIB", "cEtherCfmEventDomainIndex"),
    (0, "CISCO-ETHER-CFM-MIB", "cEtherCfmEventSvlan"),
    (0, "CISCO-ETHER-CFM-MIB", "cEtherCfmEventIndex"),
)
if mibBuilder.loadTexts:
    cEtherCfmEventEntry.setStatus("current")


class _CEtherCfmEventDomainIndex_Type(Unsigned32):
    """Custom type cEtherCfmEventDomainIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CEtherCfmEventDomainIndex_Type.__name__ = "Unsigned32"
_CEtherCfmEventDomainIndex_Object = MibTableColumn
cEtherCfmEventDomainIndex = _CEtherCfmEventDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 1),
    _CEtherCfmEventDomainIndex_Type()
)
cEtherCfmEventDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cEtherCfmEventDomainIndex.setStatus("current")
_CEtherCfmEventSvlan_Type = VlanId
_CEtherCfmEventSvlan_Object = MibTableColumn
cEtherCfmEventSvlan = _CEtherCfmEventSvlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 2),
    _CEtherCfmEventSvlan_Type()
)
cEtherCfmEventSvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cEtherCfmEventSvlan.setStatus("current")


class _CEtherCfmEventIndex_Type(Unsigned32):
    """Custom type cEtherCfmEventIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CEtherCfmEventIndex_Type.__name__ = "Unsigned32"
_CEtherCfmEventIndex_Object = MibTableColumn
cEtherCfmEventIndex = _CEtherCfmEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 3),
    _CEtherCfmEventIndex_Type()
)
cEtherCfmEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cEtherCfmEventIndex.setStatus("current")
_CEtherCfmEventDomainName_Type = SnmpAdminString
_CEtherCfmEventDomainName_Object = MibTableColumn
cEtherCfmEventDomainName = _CEtherCfmEventDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 4),
    _CEtherCfmEventDomainName_Type()
)
cEtherCfmEventDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEtherCfmEventDomainName.setStatus("current")


class _CEtherCfmEventType_Type(Integer32):
    """Custom type cEtherCfmEventType based on Integer32"""
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
        *(("config", 5),
          ("loop", 4),
          ("mepDown", 2),
          ("mepUp", 1),
          ("xcheckMissing", 6),
          ("xcheckServiceUp", 8),
          ("xcheckUnknown", 7),
          ("xconnect", 3))
    )


_CEtherCfmEventType_Type.__name__ = "Integer32"
_CEtherCfmEventType_Object = MibTableColumn
cEtherCfmEventType = _CEtherCfmEventType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 5),
    _CEtherCfmEventType_Type()
)
cEtherCfmEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEtherCfmEventType.setStatus("current")
_CEtherCfmEventLastChange_Type = TimeStamp
_CEtherCfmEventLastChange_Object = MibTableColumn
cEtherCfmEventLastChange = _CEtherCfmEventLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 6),
    _CEtherCfmEventLastChange_Type()
)
cEtherCfmEventLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEtherCfmEventLastChange.setStatus("current")


class _CEtherCfmEventServiceId_Type(SnmpAdminString):
    """Custom type cEtherCfmEventServiceId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CEtherCfmEventServiceId_Type.__name__ = "SnmpAdminString"
_CEtherCfmEventServiceId_Object = MibTableColumn
cEtherCfmEventServiceId = _CEtherCfmEventServiceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 7),
    _CEtherCfmEventServiceId_Type()
)
cEtherCfmEventServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEtherCfmEventServiceId.setStatus("current")
_CEtherCfmEventLclMepid_Type = CfmMepid
_CEtherCfmEventLclMepid_Object = MibTableColumn
cEtherCfmEventLclMepid = _CEtherCfmEventLclMepid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 8),
    _CEtherCfmEventLclMepid_Type()
)
cEtherCfmEventLclMepid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEtherCfmEventLclMepid.setStatus("current")
_CEtherCfmEventLclMacAddress_Type = MacAddress
_CEtherCfmEventLclMacAddress_Object = MibTableColumn
cEtherCfmEventLclMacAddress = _CEtherCfmEventLclMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 9),
    _CEtherCfmEventLclMacAddress_Type()
)
cEtherCfmEventLclMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEtherCfmEventLclMacAddress.setStatus("current")
_CEtherCfmEventLclMepCount_Type = Gauge32
_CEtherCfmEventLclMepCount_Object = MibTableColumn
cEtherCfmEventLclMepCount = _CEtherCfmEventLclMepCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 10),
    _CEtherCfmEventLclMepCount_Type()
)
cEtherCfmEventLclMepCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEtherCfmEventLclMepCount.setStatus("current")
_CEtherCfmEventLclIfCount_Type = Gauge32
_CEtherCfmEventLclIfCount_Object = MibTableColumn
cEtherCfmEventLclIfCount = _CEtherCfmEventLclIfCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 11),
    _CEtherCfmEventLclIfCount_Type()
)
cEtherCfmEventLclIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEtherCfmEventLclIfCount.setStatus("current")
_CEtherCfmEventRmtMepid_Type = CfmMepid
_CEtherCfmEventRmtMepid_Object = MibTableColumn
cEtherCfmEventRmtMepid = _CEtherCfmEventRmtMepid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 12),
    _CEtherCfmEventRmtMepid_Type()
)
cEtherCfmEventRmtMepid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEtherCfmEventRmtMepid.setStatus("current")
_CEtherCfmEventRmtMacAddress_Type = MacAddress
_CEtherCfmEventRmtMacAddress_Object = MibTableColumn
cEtherCfmEventRmtMacAddress = _CEtherCfmEventRmtMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 13),
    _CEtherCfmEventRmtMacAddress_Type()
)
cEtherCfmEventRmtMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEtherCfmEventRmtMacAddress.setStatus("current")


class _CEtherCfmEventRmtPortState_Type(Integer32):
    """Custom type cEtherCfmEventRmtPortState based on Integer32"""
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
        *(("adminDown", 3),
          ("down", 2),
          ("localExcessiveErrors", 6),
          ("localNoData", 7),
          ("remoteExcessiveErrors", 5),
          ("test", 4),
          ("up", 1))
    )


_CEtherCfmEventRmtPortState_Type.__name__ = "Integer32"
_CEtherCfmEventRmtPortState_Object = MibTableColumn
cEtherCfmEventRmtPortState = _CEtherCfmEventRmtPortState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 14),
    _CEtherCfmEventRmtPortState_Type()
)
cEtherCfmEventRmtPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEtherCfmEventRmtPortState.setStatus("current")


class _CEtherCfmEventRmtServiceId_Type(SnmpAdminString):
    """Custom type cEtherCfmEventRmtServiceId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CEtherCfmEventRmtServiceId_Type.__name__ = "SnmpAdminString"
_CEtherCfmEventRmtServiceId_Object = MibTableColumn
cEtherCfmEventRmtServiceId = _CEtherCfmEventRmtServiceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 15),
    _CEtherCfmEventRmtServiceId_Type()
)
cEtherCfmEventRmtServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEtherCfmEventRmtServiceId.setStatus("current")


class _CEtherCfmEventCode_Type(Integer32):
    """Custom type cEtherCfmEventCode based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("configClear", 6),
          ("lastGasp", 4),
          ("loopClear", 7),
          ("new", 1),
          ("portState", 3),
          ("returning", 2),
          ("timeout", 5),
          ("unknownClear", 9),
          ("xconnectClear", 8))
    )


_CEtherCfmEventCode_Type.__name__ = "Integer32"
_CEtherCfmEventCode_Object = MibTableColumn
cEtherCfmEventCode = _CEtherCfmEventCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 16),
    _CEtherCfmEventCode_Type()
)
cEtherCfmEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEtherCfmEventCode.setStatus("current")


class _CEtherCfmEventDeleteRow_Type(Integer32):
    """Custom type cEtherCfmEventDeleteRow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("noop", 1))
    )


_CEtherCfmEventDeleteRow_Type.__name__ = "Integer32"
_CEtherCfmEventDeleteRow_Object = MibTableColumn
cEtherCfmEventDeleteRow = _CEtherCfmEventDeleteRow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 17),
    _CEtherCfmEventDeleteRow_Type()
)
cEtherCfmEventDeleteRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cEtherCfmEventDeleteRow.setStatus("current")
_CiscoEtherCfmMIBConform_ObjectIdentity = ObjectIdentity
ciscoEtherCfmMIBConform = _CiscoEtherCfmMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 2)
)
_CiscoEtherCfmMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEtherCfmMIBCompliances = _CiscoEtherCfmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 1)
)
_CiscoEtherCfmMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEtherCfmMIBGroups = _CiscoEtherCfmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 2)
)

# Managed Objects groups

ciscoEtherCfmMIBEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 2, 1)
)
ciscoEtherCfmMIBEventGroup.setObjects(
      *(("CISCO-ETHER-CFM-MIB", "cEtherCfmMaxEventIndex"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventDomainName"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventType"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLastChange"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepid"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepCount"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclIfCount"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtPortState"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtServiceId"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventCode"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventDeleteRow"))
)
if mibBuilder.loadTexts:
    ciscoEtherCfmMIBEventGroup.setStatus("current")


# Notification objects

cEtherCfmCcMepUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 1)
)
cEtherCfmCcMepUp.setObjects(
      *(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepCount"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclIfCount"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventCode"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtPortState"))
)
if mibBuilder.loadTexts:
    cEtherCfmCcMepUp.setStatus(
        "current"
    )

cEtherCfmCcMepDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 2)
)
cEtherCfmCcMepDown.setObjects(
      *(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepCount"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclIfCount"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventCode"))
)
if mibBuilder.loadTexts:
    cEtherCfmCcMepDown.setStatus(
        "current"
    )

cEtherCfmCcCrossconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 3)
)
cEtherCfmCcCrossconnect.setObjects(
      *(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtServiceId"))
)
if mibBuilder.loadTexts:
    cEtherCfmCcCrossconnect.setStatus(
        "current"
    )

cEtherCfmCcLoop = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 4)
)
cEtherCfmCcLoop.setObjects(
      *(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepid"))
)
if mibBuilder.loadTexts:
    cEtherCfmCcLoop.setStatus(
        "current"
    )

cEtherCfmCcConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 5)
)
cEtherCfmCcConfigError.setObjects(
      *(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepid"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"))
)
if mibBuilder.loadTexts:
    cEtherCfmCcConfigError.setStatus(
        "current"
    )

cEtherCfmXCheckMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 6)
)
cEtherCfmXCheckMissing.setObjects(
      *(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"))
)
if mibBuilder.loadTexts:
    cEtherCfmXCheckMissing.setStatus(
        "current"
    )

cEtherCfmXCheckUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 7)
)
cEtherCfmXCheckUnknown.setObjects(
      *(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"))
)
if mibBuilder.loadTexts:
    cEtherCfmXCheckUnknown.setStatus(
        "current"
    )

cEtherCfmXCheckServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 8)
)
cEtherCfmXCheckServiceUp.setObjects(
      *(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"))
)
if mibBuilder.loadTexts:
    cEtherCfmXCheckServiceUp.setStatus(
        "current"
    )


# Notifications groups

ciscoEtherCfmMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 2, 2)
)
ciscoEtherCfmMIBNotifGroup.setObjects(
      *(("CISCO-ETHER-CFM-MIB", "cEtherCfmCcMepUp"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmCcMepDown"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmCcCrossconnect"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmCcLoop"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmCcConfigError"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmXCheckMissing"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmXCheckUnknown"),
        ("CISCO-ETHER-CFM-MIB", "cEtherCfmXCheckServiceUp"))
)
if mibBuilder.loadTexts:
    ciscoEtherCfmMIBNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoEtherCfmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoEtherCfmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ETHER-CFM-MIB",
    **{"CfmMepid": CfmMepid,
       "ciscoEtherCfmMIB": ciscoEtherCfmMIB,
       "ciscoEtherCfmMIBNotifs": ciscoEtherCfmMIBNotifs,
       "ciscoEtherCfmNotificationPrefix": ciscoEtherCfmNotificationPrefix,
       "cEtherCfmCcMepUp": cEtherCfmCcMepUp,
       "cEtherCfmCcMepDown": cEtherCfmCcMepDown,
       "cEtherCfmCcCrossconnect": cEtherCfmCcCrossconnect,
       "cEtherCfmCcLoop": cEtherCfmCcLoop,
       "cEtherCfmCcConfigError": cEtherCfmCcConfigError,
       "cEtherCfmXCheckMissing": cEtherCfmXCheckMissing,
       "cEtherCfmXCheckUnknown": cEtherCfmXCheckUnknown,
       "cEtherCfmXCheckServiceUp": cEtherCfmXCheckServiceUp,
       "ciscoEtherCfmMIBObjects": ciscoEtherCfmMIBObjects,
       "cecCfmEvents": cecCfmEvents,
       "cEtherCfmMaxEventIndex": cEtherCfmMaxEventIndex,
       "cEtherCfmEventTable": cEtherCfmEventTable,
       "cEtherCfmEventEntry": cEtherCfmEventEntry,
       "cEtherCfmEventDomainIndex": cEtherCfmEventDomainIndex,
       "cEtherCfmEventSvlan": cEtherCfmEventSvlan,
       "cEtherCfmEventIndex": cEtherCfmEventIndex,
       "cEtherCfmEventDomainName": cEtherCfmEventDomainName,
       "cEtherCfmEventType": cEtherCfmEventType,
       "cEtherCfmEventLastChange": cEtherCfmEventLastChange,
       "cEtherCfmEventServiceId": cEtherCfmEventServiceId,
       "cEtherCfmEventLclMepid": cEtherCfmEventLclMepid,
       "cEtherCfmEventLclMacAddress": cEtherCfmEventLclMacAddress,
       "cEtherCfmEventLclMepCount": cEtherCfmEventLclMepCount,
       "cEtherCfmEventLclIfCount": cEtherCfmEventLclIfCount,
       "cEtherCfmEventRmtMepid": cEtherCfmEventRmtMepid,
       "cEtherCfmEventRmtMacAddress": cEtherCfmEventRmtMacAddress,
       "cEtherCfmEventRmtPortState": cEtherCfmEventRmtPortState,
       "cEtherCfmEventRmtServiceId": cEtherCfmEventRmtServiceId,
       "cEtherCfmEventCode": cEtherCfmEventCode,
       "cEtherCfmEventDeleteRow": cEtherCfmEventDeleteRow,
       "ciscoEtherCfmMIBConform": ciscoEtherCfmMIBConform,
       "ciscoEtherCfmMIBCompliances": ciscoEtherCfmMIBCompliances,
       "ciscoEtherCfmMIBCompliance": ciscoEtherCfmMIBCompliance,
       "ciscoEtherCfmMIBGroups": ciscoEtherCfmMIBGroups,
       "ciscoEtherCfmMIBEventGroup": ciscoEtherCfmMIBEventGroup,
       "ciscoEtherCfmMIBNotifGroup": ciscoEtherCfmMIBNotifGroup}
)
