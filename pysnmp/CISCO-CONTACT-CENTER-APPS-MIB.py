# SNMP MIB module (CISCO-CONTACT-CENTER-APPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CONTACT-CENTER-APPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:41 2024
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

(CiscoURLString,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLString")

(InetAddressDNS,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressDNS")

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

ciscoCcaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 473)
)
ciscoCcaMIB.setRevisions(
        ("2009-05-06 17:00",
         "2005-04-05 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CcaIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CcaComponentType(Integer32, TextualConvention):
    status = "current"
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
        *(("campaign", 7),
          ("cg", 5),
          ("ctios", 6),
          ("dialer", 8),
          ("distAW", 3),
          ("logger", 2),
          ("pg", 4),
          ("router", 1))
    )



class CcaComponentStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("active", 5),
          ("disabled", 2),
          ("disconnected", 7),
          ("notRoutable", 9),
          ("standby", 6),
          ("started", 4),
          ("stopped", 3),
          ("uninitialized", 8),
          ("unknown", 1))
    )



class CcaComponentSide(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sideA", 1),
          ("sideB", 2))
    )



class CcaPeripheralType(Integer32, TextualConvention):
    status = "current"
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              23)
        )
    )
    namedValues = NamedValues(
        *(("acmiCRS", 19),
          ("acmiIPCC", 18),
          ("acp1000", 9),
          ("alcatel", 13),
          ("aspect", 1),
          ("callManager", 17),
          ("dms100", 3),
          ("ericssonMD110", 12),
          ("g2", 4),
          ("g3", 5),
          ("galaxy", 6),
          ("mediaRouting", 14),
          ("meridian", 2),
          ("neax2400", 8),
          ("nonVoiceAgent", 15),
          ("rolm9005", 10),
          ("siemensHicom", 11),
          ("softACD", 21),
          ("spectrum", 7),
          ("symposium", 16),
          ("systemIPCC", 23),
          ("vru", 20))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCcaMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCcaMIBNotifs = _CiscoCcaMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 0)
)
_CiscoCcaMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCcaMIBObjects = _CiscoCcaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1)
)
_CccaGeneralInfo_ObjectIdentity = ObjectIdentity
cccaGeneralInfo = _CccaGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 1)
)
_CccaName_Type = InetAddressDNS
_CccaName_Object = MibScalar
cccaName = _CccaName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 1, 1),
    _CccaName_Type()
)
cccaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaName.setStatus("current")
_CccaDescription_Type = SnmpAdminString
_CccaDescription_Object = MibScalar
cccaDescription = _CccaDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 1, 2),
    _CccaDescription_Type()
)
cccaDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDescription.setStatus("current")
_CccaVersion_Type = SnmpAdminString
_CccaVersion_Object = MibScalar
cccaVersion = _CccaVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 1, 3),
    _CccaVersion_Type()
)
cccaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaVersion.setStatus("current")
_CccaTimeZoneName_Type = SnmpAdminString
_CccaTimeZoneName_Object = MibScalar
cccaTimeZoneName = _CccaTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 1, 4),
    _CccaTimeZoneName_Type()
)
cccaTimeZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaTimeZoneName.setStatus("current")


class _CccaTimeZoneOffsetHours_Type(Integer32):
    """Custom type cccaTimeZoneOffsetHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_CccaTimeZoneOffsetHours_Type.__name__ = "Integer32"
_CccaTimeZoneOffsetHours_Object = MibScalar
cccaTimeZoneOffsetHours = _CccaTimeZoneOffsetHours_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 1, 5),
    _CccaTimeZoneOffsetHours_Type()
)
cccaTimeZoneOffsetHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaTimeZoneOffsetHours.setStatus("current")


class _CccaTimeZoneOffsetMinutes_Type(Integer32):
    """Custom type cccaTimeZoneOffsetMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-59, 59),
    )


_CccaTimeZoneOffsetMinutes_Type.__name__ = "Integer32"
_CccaTimeZoneOffsetMinutes_Object = MibScalar
cccaTimeZoneOffsetMinutes = _CccaTimeZoneOffsetMinutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 1, 6),
    _CccaTimeZoneOffsetMinutes_Type()
)
cccaTimeZoneOffsetMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaTimeZoneOffsetMinutes.setStatus("current")
_CccaSupportToolsURL_Type = CiscoURLString
_CccaSupportToolsURL_Object = MibScalar
cccaSupportToolsURL = _CccaSupportToolsURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 1, 7),
    _CccaSupportToolsURL_Type()
)
cccaSupportToolsURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaSupportToolsURL.setStatus("current")
_CccaWebSetupURL_Type = CiscoURLString
_CccaWebSetupURL_Object = MibScalar
cccaWebSetupURL = _CccaWebSetupURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 1, 8),
    _CccaWebSetupURL_Type()
)
cccaWebSetupURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaWebSetupURL.setStatus("current")
_CccaNotificationsEnabled_Type = TruthValue
_CccaNotificationsEnabled_Object = MibScalar
cccaNotificationsEnabled = _CccaNotificationsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 1, 9),
    _CccaNotificationsEnabled_Type()
)
cccaNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cccaNotificationsEnabled.setStatus("current")
_CccaComponents_ObjectIdentity = ObjectIdentity
cccaComponents = _CccaComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 2)
)
_CccaInstanceTable_Object = MibTable
cccaInstanceTable = _CccaInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cccaInstanceTable.setStatus("current")
_CccaInstanceEntry_Object = MibTableRow
cccaInstanceEntry = _CccaInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 2, 1, 1)
)
cccaInstanceEntry.setIndexNames(
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaInstanceNumber"),
)
if mibBuilder.loadTexts:
    cccaInstanceEntry.setStatus("current")
_CccaInstanceNumber_Type = Unsigned32
_CccaInstanceNumber_Object = MibTableColumn
cccaInstanceNumber = _CccaInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 2, 1, 1, 1),
    _CccaInstanceNumber_Type()
)
cccaInstanceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cccaInstanceNumber.setStatus("current")
_CccaInstanceName_Type = SnmpAdminString
_CccaInstanceName_Object = MibTableColumn
cccaInstanceName = _CccaInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 2, 1, 1, 2),
    _CccaInstanceName_Type()
)
cccaInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaInstanceName.setStatus("current")
_CccaComponentTable_Object = MibTable
cccaComponentTable = _CccaComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cccaComponentTable.setStatus("current")
_CccaComponentEntry_Object = MibTableRow
cccaComponentEntry = _CccaComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 2, 2, 1)
)
cccaComponentEntry.setIndexNames(
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaInstanceNumber"),
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentIndex"),
)
if mibBuilder.loadTexts:
    cccaComponentEntry.setStatus("current")
_CccaComponentIndex_Type = CcaIndex
_CccaComponentIndex_Object = MibTableColumn
cccaComponentIndex = _CccaComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 2, 2, 1, 1),
    _CccaComponentIndex_Type()
)
cccaComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cccaComponentIndex.setStatus("current")
_CccaComponentType_Type = CcaComponentType
_CccaComponentType_Object = MibTableColumn
cccaComponentType = _CccaComponentType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 2, 2, 1, 2),
    _CccaComponentType_Type()
)
cccaComponentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaComponentType.setStatus("current")
_CccaComponentName_Type = SnmpAdminString
_CccaComponentName_Object = MibTableColumn
cccaComponentName = _CccaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 2, 2, 1, 3),
    _CccaComponentName_Type()
)
cccaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaComponentName.setStatus("current")
_CccaComponentStatus_Type = CcaComponentStatus
_CccaComponentStatus_Object = MibTableColumn
cccaComponentStatus = _CccaComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 2, 2, 1, 4),
    _CccaComponentStatus_Type()
)
cccaComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaComponentStatus.setStatus("current")
_CccaComponentElmtTable_Object = MibTable
cccaComponentElmtTable = _CccaComponentElmtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cccaComponentElmtTable.setStatus("current")
_CccaComponentElmtEntry_Object = MibTableRow
cccaComponentElmtEntry = _CccaComponentElmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 2, 3, 1)
)
cccaComponentElmtEntry.setIndexNames(
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaInstanceNumber"),
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentIndex"),
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentElmtIndex"),
)
if mibBuilder.loadTexts:
    cccaComponentElmtEntry.setStatus("current")


class _CccaComponentElmtIndex_Type(Unsigned32):
    """Custom type cccaComponentElmtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CccaComponentElmtIndex_Type.__name__ = "Unsigned32"
_CccaComponentElmtIndex_Object = MibTableColumn
cccaComponentElmtIndex = _CccaComponentElmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 2, 3, 1, 1),
    _CccaComponentElmtIndex_Type()
)
cccaComponentElmtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cccaComponentElmtIndex.setStatus("current")
_CccaComponentElmtName_Type = SnmpAdminString
_CccaComponentElmtName_Object = MibTableColumn
cccaComponentElmtName = _CccaComponentElmtName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 2, 3, 1, 2),
    _CccaComponentElmtName_Type()
)
cccaComponentElmtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaComponentElmtName.setStatus("current")


class _CccaComponentElmtRunID_Type(Unsigned32):
    """Custom type cccaComponentElmtRunID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CccaComponentElmtRunID_Type.__name__ = "Unsigned32"
_CccaComponentElmtRunID_Object = MibTableColumn
cccaComponentElmtRunID = _CccaComponentElmtRunID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 2, 3, 1, 3),
    _CccaComponentElmtRunID_Type()
)
cccaComponentElmtRunID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaComponentElmtRunID.setStatus("current")
_CccaComponentElmtStatus_Type = CcaComponentStatus
_CccaComponentElmtStatus_Object = MibTableColumn
cccaComponentElmtStatus = _CccaComponentElmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 2, 3, 1, 4),
    _CccaComponentElmtStatus_Type()
)
cccaComponentElmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaComponentElmtStatus.setStatus("current")
_CccaComponentInfo_ObjectIdentity = ObjectIdentity
cccaComponentInfo = _CccaComponentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3)
)
_CccaRouterTable_Object = MibTable
cccaRouterTable = _CccaRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cccaRouterTable.setStatus("current")
_CccaRouterEntry_Object = MibTableRow
cccaRouterEntry = _CccaRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 1, 1)
)
cccaRouterEntry.setIndexNames(
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaInstanceNumber"),
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentIndex"),
)
if mibBuilder.loadTexts:
    cccaRouterEntry.setStatus("current")
_CccaRouterSide_Type = CcaComponentSide
_CccaRouterSide_Object = MibTableColumn
cccaRouterSide = _CccaRouterSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 1, 1, 1),
    _CccaRouterSide_Type()
)
cccaRouterSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaRouterSide.setStatus("current")
_CccaRouterCallsPerSec_Type = Gauge32
_CccaRouterCallsPerSec_Object = MibTableColumn
cccaRouterCallsPerSec = _CccaRouterCallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 1, 1, 2),
    _CccaRouterCallsPerSec_Type()
)
cccaRouterCallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaRouterCallsPerSec.setStatus("current")
if mibBuilder.loadTexts:
    cccaRouterCallsPerSec.setUnits("calls")
_CccaRouterAgentsLoggedOn_Type = Gauge32
_CccaRouterAgentsLoggedOn_Object = MibTableColumn
cccaRouterAgentsLoggedOn = _CccaRouterAgentsLoggedOn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 1, 1, 3),
    _CccaRouterAgentsLoggedOn_Type()
)
cccaRouterAgentsLoggedOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaRouterAgentsLoggedOn.setStatus("current")
if mibBuilder.loadTexts:
    cccaRouterAgentsLoggedOn.setUnits("agents")
_CccaRouterCallsInProgress_Type = Gauge32
_CccaRouterCallsInProgress_Object = MibTableColumn
cccaRouterCallsInProgress = _CccaRouterCallsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 1, 1, 4),
    _CccaRouterCallsInProgress_Type()
)
cccaRouterCallsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaRouterCallsInProgress.setStatus("current")
if mibBuilder.loadTexts:
    cccaRouterCallsInProgress.setUnits("calls")
_CccaRouterDuplexPairName_Type = InetAddressDNS
_CccaRouterDuplexPairName_Object = MibTableColumn
cccaRouterDuplexPairName = _CccaRouterDuplexPairName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 1, 1, 5),
    _CccaRouterDuplexPairName_Type()
)
cccaRouterDuplexPairName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaRouterDuplexPairName.setStatus("current")


class _CccaRouterNicCount_Type(Gauge32):
    """Custom type cccaRouterNicCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CccaRouterNicCount_Type.__name__ = "Gauge32"
_CccaRouterNicCount_Object = MibTableColumn
cccaRouterNicCount = _CccaRouterNicCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 1, 1, 6),
    _CccaRouterNicCount_Type()
)
cccaRouterNicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaRouterNicCount.setStatus("current")
if mibBuilder.loadTexts:
    cccaRouterNicCount.setUnits("entries")


class _CccaRouterPGsEnabledCount_Type(Gauge32):
    """Custom type cccaRouterPGsEnabledCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_CccaRouterPGsEnabledCount_Type.__name__ = "Gauge32"
_CccaRouterPGsEnabledCount_Object = MibTableColumn
cccaRouterPGsEnabledCount = _CccaRouterPGsEnabledCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 1, 1, 7),
    _CccaRouterPGsEnabledCount_Type()
)
cccaRouterPGsEnabledCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaRouterPGsEnabledCount.setStatus("current")
if mibBuilder.loadTexts:
    cccaRouterPGsEnabledCount.setUnits("peripherals")
_CccaRouterCallsInQueue_Type = Gauge32
_CccaRouterCallsInQueue_Object = MibTableColumn
cccaRouterCallsInQueue = _CccaRouterCallsInQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 1, 1, 8),
    _CccaRouterCallsInQueue_Type()
)
cccaRouterCallsInQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaRouterCallsInQueue.setStatus("current")
if mibBuilder.loadTexts:
    cccaRouterCallsInQueue.setUnits("calls")
_CccaRouterAppGwEnabled_Type = TruthValue
_CccaRouterAppGwEnabled_Object = MibTableColumn
cccaRouterAppGwEnabled = _CccaRouterAppGwEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 1, 1, 9),
    _CccaRouterAppGwEnabled_Type()
)
cccaRouterAppGwEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaRouterAppGwEnabled.setStatus("current")
_CccaRouterDBWorkerEnabled_Type = TruthValue
_CccaRouterDBWorkerEnabled_Object = MibTableColumn
cccaRouterDBWorkerEnabled = _CccaRouterDBWorkerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 1, 1, 10),
    _CccaRouterDBWorkerEnabled_Type()
)
cccaRouterDBWorkerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaRouterDBWorkerEnabled.setStatus("current")
_CccaRouterPublicHighAddr_Type = InetAddressDNS
_CccaRouterPublicHighAddr_Object = MibTableColumn
cccaRouterPublicHighAddr = _CccaRouterPublicHighAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 1, 1, 11),
    _CccaRouterPublicHighAddr_Type()
)
cccaRouterPublicHighAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaRouterPublicHighAddr.setStatus("current")
_CccaRouterPublicNonHighAddr_Type = InetAddressDNS
_CccaRouterPublicNonHighAddr_Object = MibTableColumn
cccaRouterPublicNonHighAddr = _CccaRouterPublicNonHighAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 1, 1, 12),
    _CccaRouterPublicNonHighAddr_Type()
)
cccaRouterPublicNonHighAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaRouterPublicNonHighAddr.setStatus("current")
_CccaRouterPrivateHighAddr_Type = InetAddressDNS
_CccaRouterPrivateHighAddr_Object = MibTableColumn
cccaRouterPrivateHighAddr = _CccaRouterPrivateHighAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 1, 1, 13),
    _CccaRouterPrivateHighAddr_Type()
)
cccaRouterPrivateHighAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaRouterPrivateHighAddr.setStatus("current")
_CccaRouterPrivateNonHighAddr_Type = InetAddressDNS
_CccaRouterPrivateNonHighAddr_Object = MibTableColumn
cccaRouterPrivateNonHighAddr = _CccaRouterPrivateNonHighAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 1, 1, 14),
    _CccaRouterPrivateNonHighAddr_Type()
)
cccaRouterPrivateNonHighAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaRouterPrivateNonHighAddr.setStatus("current")
_CccaNicTable_Object = MibTable
cccaNicTable = _CccaNicTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cccaNicTable.setStatus("current")
_CccaNicEntry_Object = MibTableRow
cccaNicEntry = _CccaNicEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 2, 1)
)
cccaNicEntry.setIndexNames(
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaInstanceNumber"),
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentIndex"),
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaNicIndex"),
)
if mibBuilder.loadTexts:
    cccaNicEntry.setStatus("current")
_CccaNicIndex_Type = CcaIndex
_CccaNicIndex_Object = MibTableColumn
cccaNicIndex = _CccaNicIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 2, 1, 1),
    _CccaNicIndex_Type()
)
cccaNicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cccaNicIndex.setStatus("current")


class _CccaNicType_Type(Integer32):
    """Custom type cccaNicType based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("att", 2),
          ("aucsINAP", 3),
          ("cain", 4),
          ("crsp", 5),
          ("cwc", 6),
          ("generic", 1),
          ("gktmp", 7),
          ("incrp", 8),
          ("mci", 9),
          ("nortel", 10),
          ("ntl", 11),
          ("sprint", 12),
          ("ss7in", 13),
          ("stentor", 14),
          ("timINAP", 15))
    )


_CccaNicType_Type.__name__ = "Integer32"
_CccaNicType_Object = MibTableColumn
cccaNicType = _CccaNicType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 2, 1, 2),
    _CccaNicType_Type()
)
cccaNicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaNicType.setStatus("current")
_CccaNicStatus_Type = CcaComponentStatus
_CccaNicStatus_Object = MibTableColumn
cccaNicStatus = _CccaNicStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 2, 1, 3),
    _CccaNicStatus_Type()
)
cccaNicStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaNicStatus.setStatus("current")
_CccaLoggerTable_Object = MibTable
cccaLoggerTable = _CccaLoggerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cccaLoggerTable.setStatus("current")
_CccaLoggerEntry_Object = MibTableRow
cccaLoggerEntry = _CccaLoggerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 3, 1)
)
cccaLoggerEntry.setIndexNames(
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaInstanceNumber"),
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentIndex"),
)
if mibBuilder.loadTexts:
    cccaLoggerEntry.setStatus("current")
_CccaLoggerSide_Type = CcaComponentSide
_CccaLoggerSide_Object = MibTableColumn
cccaLoggerSide = _CccaLoggerSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 3, 1, 1),
    _CccaLoggerSide_Type()
)
cccaLoggerSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaLoggerSide.setStatus("current")


class _CccaLoggerType_Type(Integer32):
    """Custom type cccaLoggerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cicm", 3),
          ("nam", 2),
          ("standard", 1))
    )


_CccaLoggerType_Type.__name__ = "Integer32"
_CccaLoggerType_Object = MibTableColumn
cccaLoggerType = _CccaLoggerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 3, 1, 2),
    _CccaLoggerType_Type()
)
cccaLoggerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaLoggerType.setStatus("current")
_CccaLoggerRouterSideAName_Type = InetAddressDNS
_CccaLoggerRouterSideAName_Object = MibTableColumn
cccaLoggerRouterSideAName = _CccaLoggerRouterSideAName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 3, 1, 3),
    _CccaLoggerRouterSideAName_Type()
)
cccaLoggerRouterSideAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaLoggerRouterSideAName.setStatus("current")
_CccaLoggerRouterSideBName_Type = InetAddressDNS
_CccaLoggerRouterSideBName_Object = MibTableColumn
cccaLoggerRouterSideBName = _CccaLoggerRouterSideBName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 3, 1, 4),
    _CccaLoggerRouterSideBName_Type()
)
cccaLoggerRouterSideBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaLoggerRouterSideBName.setStatus("current")
_CccaLoggerDuplexPairName_Type = InetAddressDNS
_CccaLoggerDuplexPairName_Object = MibTableColumn
cccaLoggerDuplexPairName = _CccaLoggerDuplexPairName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 3, 1, 5),
    _CccaLoggerDuplexPairName_Type()
)
cccaLoggerDuplexPairName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaLoggerDuplexPairName.setStatus("current")
_CccaLoggerHDSReplication_Type = TruthValue
_CccaLoggerHDSReplication_Object = MibTableColumn
cccaLoggerHDSReplication = _CccaLoggerHDSReplication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 3, 1, 6),
    _CccaLoggerHDSReplication_Type()
)
cccaLoggerHDSReplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaLoggerHDSReplication.setStatus("current")
_CccaLoggerAvgDBWriteTime_Type = Unsigned32
_CccaLoggerAvgDBWriteTime_Object = MibTableColumn
cccaLoggerAvgDBWriteTime = _CccaLoggerAvgDBWriteTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 3, 1, 7),
    _CccaLoggerAvgDBWriteTime_Type()
)
cccaLoggerAvgDBWriteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaLoggerAvgDBWriteTime.setStatus("current")
if mibBuilder.loadTexts:
    cccaLoggerAvgDBWriteTime.setUnits("hundred nanoseconds")
_CccaDistAwTable_Object = MibTable
cccaDistAwTable = _CccaDistAwTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cccaDistAwTable.setStatus("current")
_CccaDistAwEntry_Object = MibTableRow
cccaDistAwEntry = _CccaDistAwEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 4, 1)
)
cccaDistAwEntry.setIndexNames(
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaInstanceNumber"),
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentIndex"),
)
if mibBuilder.loadTexts:
    cccaDistAwEntry.setStatus("current")
_CccaDistAwSide_Type = CcaComponentSide
_CccaDistAwSide_Object = MibTableColumn
cccaDistAwSide = _CccaDistAwSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 4, 1, 1),
    _CccaDistAwSide_Type()
)
cccaDistAwSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDistAwSide.setStatus("deprecated")


class _CccaDistAwType_Type(Integer32):
    """Custom type cccaDistAwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cicm", 2),
          ("nam", 1),
          ("standard", 0))
    )


_CccaDistAwType_Type.__name__ = "Integer32"
_CccaDistAwType_Object = MibTableColumn
cccaDistAwType = _CccaDistAwType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 4, 1, 2),
    _CccaDistAwType_Type()
)
cccaDistAwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDistAwType.setStatus("current")
_CccaDistAwAdminSiteName_Type = SnmpAdminString
_CccaDistAwAdminSiteName_Object = MibTableColumn
cccaDistAwAdminSiteName = _CccaDistAwAdminSiteName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 4, 1, 3),
    _CccaDistAwAdminSiteName_Type()
)
cccaDistAwAdminSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDistAwAdminSiteName.setStatus("current")
_CccaDistAwRouterSideAName_Type = InetAddressDNS
_CccaDistAwRouterSideAName_Object = MibTableColumn
cccaDistAwRouterSideAName = _CccaDistAwRouterSideAName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 4, 1, 4),
    _CccaDistAwRouterSideAName_Type()
)
cccaDistAwRouterSideAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDistAwRouterSideAName.setStatus("current")
_CccaDistAwRouterSideBName_Type = InetAddressDNS
_CccaDistAwRouterSideBName_Object = MibTableColumn
cccaDistAwRouterSideBName = _CccaDistAwRouterSideBName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 4, 1, 5),
    _CccaDistAwRouterSideBName_Type()
)
cccaDistAwRouterSideBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDistAwRouterSideBName.setStatus("current")
_CccaDistAwLoggerSideAName_Type = InetAddressDNS
_CccaDistAwLoggerSideAName_Object = MibTableColumn
cccaDistAwLoggerSideAName = _CccaDistAwLoggerSideAName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 4, 1, 6),
    _CccaDistAwLoggerSideAName_Type()
)
cccaDistAwLoggerSideAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDistAwLoggerSideAName.setStatus("current")
_CccaDistAwLoggerSideBName_Type = InetAddressDNS
_CccaDistAwLoggerSideBName_Object = MibTableColumn
cccaDistAwLoggerSideBName = _CccaDistAwLoggerSideBName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 4, 1, 7),
    _CccaDistAwLoggerSideBName_Type()
)
cccaDistAwLoggerSideBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDistAwLoggerSideBName.setStatus("current")
_CccaDistAwDuplexPairName_Type = InetAddressDNS
_CccaDistAwDuplexPairName_Object = MibTableColumn
cccaDistAwDuplexPairName = _CccaDistAwDuplexPairName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 4, 1, 8),
    _CccaDistAwDuplexPairName_Type()
)
cccaDistAwDuplexPairName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDistAwDuplexPairName.setStatus("deprecated")
_CccaDistAwHDSEnabled_Type = TruthValue
_CccaDistAwHDSEnabled_Object = MibTableColumn
cccaDistAwHDSEnabled = _CccaDistAwHDSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 4, 1, 9),
    _CccaDistAwHDSEnabled_Type()
)
cccaDistAwHDSEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDistAwHDSEnabled.setStatus("current")
_CccaDistAwWebViewEnabled_Type = TruthValue
_CccaDistAwWebViewEnabled_Object = MibTableColumn
cccaDistAwWebViewEnabled = _CccaDistAwWebViewEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 4, 1, 10),
    _CccaDistAwWebViewEnabled_Type()
)
cccaDistAwWebViewEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDistAwWebViewEnabled.setStatus("current")
_CccaDistAwWebViewServerName_Type = SnmpAdminString
_CccaDistAwWebViewServerName_Object = MibTableColumn
cccaDistAwWebViewServerName = _CccaDistAwWebViewServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 4, 1, 11),
    _CccaDistAwWebViewServerName_Type()
)
cccaDistAwWebViewServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDistAwWebViewServerName.setStatus("current")
_CccaDistAwWebReskillingURL_Type = SnmpAdminString
_CccaDistAwWebReskillingURL_Object = MibTableColumn
cccaDistAwWebReskillingURL = _CccaDistAwWebReskillingURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 4, 1, 12),
    _CccaDistAwWebReskillingURL_Type()
)
cccaDistAwWebReskillingURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDistAwWebReskillingURL.setStatus("current")
_CccaPgTable_Object = MibTable
cccaPgTable = _CccaPgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cccaPgTable.setStatus("current")
_CccaPgEntry_Object = MibTableRow
cccaPgEntry = _CccaPgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 5, 1)
)
cccaPgEntry.setIndexNames(
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaInstanceNumber"),
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentIndex"),
)
if mibBuilder.loadTexts:
    cccaPgEntry.setStatus("current")


class _CccaPgNumber_Type(Unsigned32):
    """Custom type cccaPgNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_CccaPgNumber_Type.__name__ = "Unsigned32"
_CccaPgNumber_Object = MibTableColumn
cccaPgNumber = _CccaPgNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 5, 1, 1),
    _CccaPgNumber_Type()
)
cccaPgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaPgNumber.setStatus("deprecated")
_CccaPgSide_Type = CcaComponentSide
_CccaPgSide_Object = MibTableColumn
cccaPgSide = _CccaPgSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 5, 1, 2),
    _CccaPgSide_Type()
)
cccaPgSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaPgSide.setStatus("current")
_CccaPgRouterSideAName_Type = InetAddressDNS
_CccaPgRouterSideAName_Object = MibTableColumn
cccaPgRouterSideAName = _CccaPgRouterSideAName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 5, 1, 3),
    _CccaPgRouterSideAName_Type()
)
cccaPgRouterSideAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaPgRouterSideAName.setStatus("current")
_CccaPgRouterSideBName_Type = InetAddressDNS
_CccaPgRouterSideBName_Object = MibTableColumn
cccaPgRouterSideBName = _CccaPgRouterSideBName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 5, 1, 4),
    _CccaPgRouterSideBName_Type()
)
cccaPgRouterSideBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaPgRouterSideBName.setStatus("current")
_CccaPgDuplexPairName_Type = InetAddressDNS
_CccaPgDuplexPairName_Object = MibTableColumn
cccaPgDuplexPairName = _CccaPgDuplexPairName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 5, 1, 5),
    _CccaPgDuplexPairName_Type()
)
cccaPgDuplexPairName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaPgDuplexPairName.setStatus("current")


class _CccaPgPimCount_Type(Gauge32):
    """Custom type cccaPgPimCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CccaPgPimCount_Type.__name__ = "Gauge32"
_CccaPgPimCount_Object = MibTableColumn
cccaPgPimCount = _CccaPgPimCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 5, 1, 6),
    _CccaPgPimCount_Type()
)
cccaPgPimCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaPgPimCount.setStatus("current")
_CccaPgCallsInProgress_Type = Gauge32
_CccaPgCallsInProgress_Object = MibTableColumn
cccaPgCallsInProgress = _CccaPgCallsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 5, 1, 7),
    _CccaPgCallsInProgress_Type()
)
cccaPgCallsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaPgCallsInProgress.setStatus("current")
if mibBuilder.loadTexts:
    cccaPgCallsInProgress.setUnits("calls")
_CccaPgAgentsLoggedOn_Type = Gauge32
_CccaPgAgentsLoggedOn_Object = MibTableColumn
cccaPgAgentsLoggedOn = _CccaPgAgentsLoggedOn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 5, 1, 8),
    _CccaPgAgentsLoggedOn_Type()
)
cccaPgAgentsLoggedOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaPgAgentsLoggedOn.setStatus("current")
if mibBuilder.loadTexts:
    cccaPgAgentsLoggedOn.setUnits("agents")
_CccaPgAgentsReady_Type = Gauge32
_CccaPgAgentsReady_Object = MibTableColumn
cccaPgAgentsReady = _CccaPgAgentsReady_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 5, 1, 9),
    _CccaPgAgentsReady_Type()
)
cccaPgAgentsReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaPgAgentsReady.setStatus("current")
if mibBuilder.loadTexts:
    cccaPgAgentsReady.setUnits("agents")
_CccaPgAgentsTalking_Type = Gauge32
_CccaPgAgentsTalking_Object = MibTableColumn
cccaPgAgentsTalking = _CccaPgAgentsTalking_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 5, 1, 10),
    _CccaPgAgentsTalking_Type()
)
cccaPgAgentsTalking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaPgAgentsTalking.setStatus("current")
if mibBuilder.loadTexts:
    cccaPgAgentsTalking.setUnits("agents")
_CccaPgID_Type = Unsigned32
_CccaPgID_Object = MibTableColumn
cccaPgID = _CccaPgID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 5, 1, 11),
    _CccaPgID_Type()
)
cccaPgID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaPgID.setStatus("current")
_CccaPimTable_Object = MibTable
cccaPimTable = _CccaPimTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 6)
)
if mibBuilder.loadTexts:
    cccaPimTable.setStatus("current")
_CccaPimEntry_Object = MibTableRow
cccaPimEntry = _CccaPimEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 6, 1)
)
cccaPimEntry.setIndexNames(
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaInstanceNumber"),
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentIndex"),
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaPimNumber"),
)
if mibBuilder.loadTexts:
    cccaPimEntry.setStatus("current")


class _CccaPimNumber_Type(Unsigned32):
    """Custom type cccaPimNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CccaPimNumber_Type.__name__ = "Unsigned32"
_CccaPimNumber_Object = MibTableColumn
cccaPimNumber = _CccaPimNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 6, 1, 1),
    _CccaPimNumber_Type()
)
cccaPimNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cccaPimNumber.setStatus("current")
_CccaPimPeripheralName_Type = SnmpAdminString
_CccaPimPeripheralName_Object = MibTableColumn
cccaPimPeripheralName = _CccaPimPeripheralName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 6, 1, 2),
    _CccaPimPeripheralName_Type()
)
cccaPimPeripheralName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaPimPeripheralName.setStatus("current")
_CccaPimPeripheralType_Type = CcaPeripheralType
_CccaPimPeripheralType_Object = MibTableColumn
cccaPimPeripheralType = _CccaPimPeripheralType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 6, 1, 3),
    _CccaPimPeripheralType_Type()
)
cccaPimPeripheralType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaPimPeripheralType.setStatus("current")
_CccaPimStatus_Type = CcaComponentStatus
_CccaPimStatus_Object = MibTableColumn
cccaPimStatus = _CccaPimStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 6, 1, 4),
    _CccaPimStatus_Type()
)
cccaPimStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaPimStatus.setStatus("current")
_CccaPimPeripheralHostName_Type = InetAddressDNS
_CccaPimPeripheralHostName_Object = MibTableColumn
cccaPimPeripheralHostName = _CccaPimPeripheralHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 6, 1, 5),
    _CccaPimPeripheralHostName_Type()
)
cccaPimPeripheralHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaPimPeripheralHostName.setStatus("current")
_CccaCgTable_Object = MibTable
cccaCgTable = _CccaCgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 7)
)
if mibBuilder.loadTexts:
    cccaCgTable.setStatus("current")
_CccaCgEntry_Object = MibTableRow
cccaCgEntry = _CccaCgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 7, 1)
)
cccaCgEntry.setIndexNames(
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaInstanceNumber"),
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentIndex"),
)
if mibBuilder.loadTexts:
    cccaCgEntry.setStatus("current")


class _CccaCgNumber_Type(Unsigned32):
    """Custom type cccaCgNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_CccaCgNumber_Type.__name__ = "Unsigned32"
_CccaCgNumber_Object = MibTableColumn
cccaCgNumber = _CccaCgNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 7, 1, 1),
    _CccaCgNumber_Type()
)
cccaCgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCgNumber.setStatus("deprecated")
_CccaCgSide_Type = CcaComponentSide
_CccaCgSide_Object = MibTableColumn
cccaCgSide = _CccaCgSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 7, 1, 2),
    _CccaCgSide_Type()
)
cccaCgSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCgSide.setStatus("current")
_CccaCgPgSideAName_Type = InetAddressDNS
_CccaCgPgSideAName_Object = MibTableColumn
cccaCgPgSideAName = _CccaCgPgSideAName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 7, 1, 3),
    _CccaCgPgSideAName_Type()
)
cccaCgPgSideAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCgPgSideAName.setStatus("current")
_CccaCgPgSideBName_Type = InetAddressDNS
_CccaCgPgSideBName_Object = MibTableColumn
cccaCgPgSideBName = _CccaCgPgSideBName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 7, 1, 4),
    _CccaCgPgSideBName_Type()
)
cccaCgPgSideBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCgPgSideBName.setStatus("current")
_CccaCgDuplexPairName_Type = InetAddressDNS
_CccaCgDuplexPairName_Object = MibTableColumn
cccaCgDuplexPairName = _CccaCgDuplexPairName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 7, 1, 5),
    _CccaCgDuplexPairName_Type()
)
cccaCgDuplexPairName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCgDuplexPairName.setStatus("current")
_CccaCgOpenSessions_Type = Gauge32
_CccaCgOpenSessions_Object = MibTableColumn
cccaCgOpenSessions = _CccaCgOpenSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 7, 1, 6),
    _CccaCgOpenSessions_Type()
)
cccaCgOpenSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCgOpenSessions.setStatus("current")
_CccaCgOtherSessions_Type = Gauge32
_CccaCgOtherSessions_Object = MibTableColumn
cccaCgOtherSessions = _CccaCgOtherSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 7, 1, 7),
    _CccaCgOtherSessions_Type()
)
cccaCgOtherSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCgOtherSessions.setStatus("current")
_CccaCgID_Type = Unsigned32
_CccaCgID_Object = MibTableColumn
cccaCgID = _CccaCgID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 7, 1, 8),
    _CccaCgID_Type()
)
cccaCgID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCgID.setStatus("current")
_CccaCtiOsTable_Object = MibTable
cccaCtiOsTable = _CccaCtiOsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 8)
)
if mibBuilder.loadTexts:
    cccaCtiOsTable.setStatus("current")
_CccaCtiOsEntry_Object = MibTableRow
cccaCtiOsEntry = _CccaCtiOsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 8, 1)
)
cccaCtiOsEntry.setIndexNames(
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaInstanceNumber"),
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentIndex"),
)
if mibBuilder.loadTexts:
    cccaCtiOsEntry.setStatus("current")
_CccaCtiOsServerName_Type = SnmpAdminString
_CccaCtiOsServerName_Object = MibTableColumn
cccaCtiOsServerName = _CccaCtiOsServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 8, 1, 1),
    _CccaCtiOsServerName_Type()
)
cccaCtiOsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCtiOsServerName.setStatus("current")
_CccaCtiOsPeripheralName_Type = SnmpAdminString
_CccaCtiOsPeripheralName_Object = MibTableColumn
cccaCtiOsPeripheralName = _CccaCtiOsPeripheralName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 8, 1, 2),
    _CccaCtiOsPeripheralName_Type()
)
cccaCtiOsPeripheralName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCtiOsPeripheralName.setStatus("current")
_CccaCtiOsPeripheralType_Type = CcaPeripheralType
_CccaCtiOsPeripheralType_Object = MibTableColumn
cccaCtiOsPeripheralType = _CccaCtiOsPeripheralType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 8, 1, 3),
    _CccaCtiOsPeripheralType_Type()
)
cccaCtiOsPeripheralType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCtiOsPeripheralType.setStatus("current")
_CccaCtiOsCgSideAName_Type = InetAddressDNS
_CccaCtiOsCgSideAName_Object = MibTableColumn
cccaCtiOsCgSideAName = _CccaCtiOsCgSideAName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 8, 1, 4),
    _CccaCtiOsCgSideAName_Type()
)
cccaCtiOsCgSideAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCtiOsCgSideAName.setStatus("current")
_CccaCtiOsCgSideBName_Type = InetAddressDNS
_CccaCtiOsCgSideBName_Object = MibTableColumn
cccaCtiOsCgSideBName = _CccaCtiOsCgSideBName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 8, 1, 5),
    _CccaCtiOsCgSideBName_Type()
)
cccaCtiOsCgSideBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCtiOsCgSideBName.setStatus("current")
_CccaCtiOsPeerName_Type = InetAddressDNS
_CccaCtiOsPeerName_Object = MibTableColumn
cccaCtiOsPeerName = _CccaCtiOsPeerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 8, 1, 6),
    _CccaCtiOsPeerName_Type()
)
cccaCtiOsPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCtiOsPeerName.setStatus("current")
_CccaCtiOsActiveClients_Type = Gauge32
_CccaCtiOsActiveClients_Object = MibTableColumn
cccaCtiOsActiveClients = _CccaCtiOsActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 8, 1, 7),
    _CccaCtiOsActiveClients_Type()
)
cccaCtiOsActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCtiOsActiveClients.setStatus("current")
_CccaCtiOsActiveMonitors_Type = Gauge32
_CccaCtiOsActiveMonitors_Object = MibTableColumn
cccaCtiOsActiveMonitors = _CccaCtiOsActiveMonitors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 8, 1, 8),
    _CccaCtiOsActiveMonitors_Type()
)
cccaCtiOsActiveMonitors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCtiOsActiveMonitors.setStatus("current")
_CccaCtiOsCallsInProgress_Type = Gauge32
_CccaCtiOsCallsInProgress_Object = MibTableColumn
cccaCtiOsCallsInProgress = _CccaCtiOsCallsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 8, 1, 9),
    _CccaCtiOsCallsInProgress_Type()
)
cccaCtiOsCallsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCtiOsCallsInProgress.setStatus("current")
_CccaCtiOsCallsFailed_Type = Unsigned32
_CccaCtiOsCallsFailed_Object = MibTableColumn
cccaCtiOsCallsFailed = _CccaCtiOsCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 8, 1, 10),
    _CccaCtiOsCallsFailed_Type()
)
cccaCtiOsCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCtiOsCallsFailed.setStatus("current")
_CccaCampaignMgrTable_Object = MibTable
cccaCampaignMgrTable = _CccaCampaignMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 9)
)
if mibBuilder.loadTexts:
    cccaCampaignMgrTable.setStatus("current")
_CccaCampaignMgrEntry_Object = MibTableRow
cccaCampaignMgrEntry = _CccaCampaignMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 9, 1)
)
cccaCampaignMgrEntry.setIndexNames(
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaInstanceNumber"),
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentIndex"),
)
if mibBuilder.loadTexts:
    cccaCampaignMgrEntry.setStatus("current")
_CccaCampaignMgrDbUtilization_Type = Gauge32
_CccaCampaignMgrDbUtilization_Object = MibTableColumn
cccaCampaignMgrDbUtilization = _CccaCampaignMgrDbUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 9, 1, 1),
    _CccaCampaignMgrDbUtilization_Type()
)
cccaCampaignMgrDbUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCampaignMgrDbUtilization.setStatus("current")
if mibBuilder.loadTexts:
    cccaCampaignMgrDbUtilization.setUnits("percent")
_CccaCampaignMgrQueueDepth_Type = Gauge32
_CccaCampaignMgrQueueDepth_Object = MibTableColumn
cccaCampaignMgrQueueDepth = _CccaCampaignMgrQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 9, 1, 2),
    _CccaCampaignMgrQueueDepth_Type()
)
cccaCampaignMgrQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCampaignMgrQueueDepth.setStatus("current")
if mibBuilder.loadTexts:
    cccaCampaignMgrQueueDepth.setUnits("entries")
_CccaCampaignMgrAvgQueueTime_Type = Gauge32
_CccaCampaignMgrAvgQueueTime_Object = MibTableColumn
cccaCampaignMgrAvgQueueTime = _CccaCampaignMgrAvgQueueTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 9, 1, 3),
    _CccaCampaignMgrAvgQueueTime_Type()
)
cccaCampaignMgrAvgQueueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCampaignMgrAvgQueueTime.setStatus("current")
if mibBuilder.loadTexts:
    cccaCampaignMgrAvgQueueTime.setUnits("milliseconds")
_CccaCampaignMgrActiveDialers_Type = Gauge32
_CccaCampaignMgrActiveDialers_Object = MibTableColumn
cccaCampaignMgrActiveDialers = _CccaCampaignMgrActiveDialers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 9, 1, 4),
    _CccaCampaignMgrActiveDialers_Type()
)
cccaCampaignMgrActiveDialers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaCampaignMgrActiveDialers.setStatus("current")
if mibBuilder.loadTexts:
    cccaCampaignMgrActiveDialers.setUnits("dialers")
_CccaDialerTable_Object = MibTable
cccaDialerTable = _CccaDialerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 10)
)
if mibBuilder.loadTexts:
    cccaDialerTable.setStatus("current")
_CccaDialerEntry_Object = MibTableRow
cccaDialerEntry = _CccaDialerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 10, 1)
)
cccaDialerEntry.setIndexNames(
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaInstanceNumber"),
    (0, "CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentIndex"),
)
if mibBuilder.loadTexts:
    cccaDialerEntry.setStatus("current")
_CccaDialerCampaignMgrName_Type = InetAddressDNS
_CccaDialerCampaignMgrName_Object = MibTableColumn
cccaDialerCampaignMgrName = _CccaDialerCampaignMgrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 10, 1, 1),
    _CccaDialerCampaignMgrName_Type()
)
cccaDialerCampaignMgrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDialerCampaignMgrName.setStatus("current")
_CccaDialerCampaignMgrStatus_Type = CcaComponentStatus
_CccaDialerCampaignMgrStatus_Object = MibTableColumn
cccaDialerCampaignMgrStatus = _CccaDialerCampaignMgrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 10, 1, 2),
    _CccaDialerCampaignMgrStatus_Type()
)
cccaDialerCampaignMgrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDialerCampaignMgrStatus.setStatus("current")
_CccaDialerCtiServerAName_Type = InetAddressDNS
_CccaDialerCtiServerAName_Object = MibTableColumn
cccaDialerCtiServerAName = _CccaDialerCtiServerAName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 10, 1, 3),
    _CccaDialerCtiServerAName_Type()
)
cccaDialerCtiServerAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDialerCtiServerAName.setStatus("current")
_CccaDialerCtiServerBName_Type = InetAddressDNS
_CccaDialerCtiServerBName_Object = MibTableColumn
cccaDialerCtiServerBName = _CccaDialerCtiServerBName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 10, 1, 4),
    _CccaDialerCtiServerBName_Type()
)
cccaDialerCtiServerBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDialerCtiServerBName.setStatus("current")
_CccaDialerCtiServerStatus_Type = CcaComponentStatus
_CccaDialerCtiServerStatus_Object = MibTableColumn
cccaDialerCtiServerStatus = _CccaDialerCtiServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 10, 1, 5),
    _CccaDialerCtiServerStatus_Type()
)
cccaDialerCtiServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDialerCtiServerStatus.setStatus("current")
_CccaDialerMediaRouterStatus_Type = CcaComponentStatus
_CccaDialerMediaRouterStatus_Object = MibTableColumn
cccaDialerMediaRouterStatus = _CccaDialerMediaRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 10, 1, 6),
    _CccaDialerMediaRouterStatus_Type()
)
cccaDialerMediaRouterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDialerMediaRouterStatus.setStatus("current")
_CccaDialerQueueDepth_Type = Gauge32
_CccaDialerQueueDepth_Object = MibTableColumn
cccaDialerQueueDepth = _CccaDialerQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 10, 1, 7),
    _CccaDialerQueueDepth_Type()
)
cccaDialerQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDialerQueueDepth.setStatus("current")
if mibBuilder.loadTexts:
    cccaDialerQueueDepth.setUnits("messages")
_CccaDialerAvgQueueTime_Type = Gauge32
_CccaDialerAvgQueueTime_Object = MibTableColumn
cccaDialerAvgQueueTime = _CccaDialerAvgQueueTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 10, 1, 8),
    _CccaDialerAvgQueueTime_Type()
)
cccaDialerAvgQueueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDialerAvgQueueTime.setStatus("current")
if mibBuilder.loadTexts:
    cccaDialerAvgQueueTime.setUnits("milliseconds")
_CccaDialerTalkingAgents_Type = Gauge32
_CccaDialerTalkingAgents_Object = MibTableColumn
cccaDialerTalkingAgents = _CccaDialerTalkingAgents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 10, 1, 9),
    _CccaDialerTalkingAgents_Type()
)
cccaDialerTalkingAgents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDialerTalkingAgents.setStatus("current")
if mibBuilder.loadTexts:
    cccaDialerTalkingAgents.setUnits("agents")
_CccaDialerCallAttemptsPerSec_Type = Gauge32
_CccaDialerCallAttemptsPerSec_Object = MibTableColumn
cccaDialerCallAttemptsPerSec = _CccaDialerCallAttemptsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 10, 1, 10),
    _CccaDialerCallAttemptsPerSec_Type()
)
cccaDialerCallAttemptsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDialerCallAttemptsPerSec.setStatus("current")
if mibBuilder.loadTexts:
    cccaDialerCallAttemptsPerSec.setUnits("calls")
_CccaDialerConfiguredPorts_Type = Gauge32
_CccaDialerConfiguredPorts_Object = MibTableColumn
cccaDialerConfiguredPorts = _CccaDialerConfiguredPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 10, 1, 11),
    _CccaDialerConfiguredPorts_Type()
)
cccaDialerConfiguredPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDialerConfiguredPorts.setStatus("current")
if mibBuilder.loadTexts:
    cccaDialerConfiguredPorts.setUnits("ports")
_CccaDialerBusyCustomerPorts_Type = Gauge32
_CccaDialerBusyCustomerPorts_Object = MibTableColumn
cccaDialerBusyCustomerPorts = _CccaDialerBusyCustomerPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 10, 1, 12),
    _CccaDialerBusyCustomerPorts_Type()
)
cccaDialerBusyCustomerPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDialerBusyCustomerPorts.setStatus("current")
if mibBuilder.loadTexts:
    cccaDialerBusyCustomerPorts.setUnits("ports")
_CccaDialerBusyReservationPorts_Type = Gauge32
_CccaDialerBusyReservationPorts_Object = MibTableColumn
cccaDialerBusyReservationPorts = _CccaDialerBusyReservationPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 10, 1, 13),
    _CccaDialerBusyReservationPorts_Type()
)
cccaDialerBusyReservationPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDialerBusyReservationPorts.setStatus("current")
if mibBuilder.loadTexts:
    cccaDialerBusyReservationPorts.setUnits("ports")
_CccaDialerIdlePorts_Type = Gauge32
_CccaDialerIdlePorts_Object = MibTableColumn
cccaDialerIdlePorts = _CccaDialerIdlePorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 10, 1, 14),
    _CccaDialerIdlePorts_Type()
)
cccaDialerIdlePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDialerIdlePorts.setStatus("current")
if mibBuilder.loadTexts:
    cccaDialerIdlePorts.setUnits("ports")
_CccaDialerBlockedPorts_Type = Gauge32
_CccaDialerBlockedPorts_Object = MibTableColumn
cccaDialerBlockedPorts = _CccaDialerBlockedPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 3, 10, 1, 15),
    _CccaDialerBlockedPorts_Type()
)
cccaDialerBlockedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cccaDialerBlockedPorts.setStatus("current")
if mibBuilder.loadTexts:
    cccaDialerBlockedPorts.setUnits("ports")
_CccaNotificationInfo_ObjectIdentity = ObjectIdentity
cccaNotificationInfo = _CccaNotificationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 4)
)
_CccaEventComponentId_Type = SnmpAdminString
_CccaEventComponentId_Object = MibScalar
cccaEventComponentId = _CccaEventComponentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 4, 1),
    _CccaEventComponentId_Type()
)
cccaEventComponentId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cccaEventComponentId.setStatus("current")


class _CccaEventState_Type(Integer32):
    """Custom type cccaEventState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              9)
        )
    )
    namedValues = NamedValues(
        *(("applicationError", 2),
          ("clear", 0),
          ("raise", 4),
          ("singleStateRaise", 9))
    )


_CccaEventState_Type.__name__ = "Integer32"
_CccaEventState_Object = MibScalar
cccaEventState = _CccaEventState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 4, 2),
    _CccaEventState_Type()
)
cccaEventState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cccaEventState.setStatus("current")
_CccaEventMessageId_Type = Unsigned32
_CccaEventMessageId_Object = MibScalar
cccaEventMessageId = _CccaEventMessageId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 4, 3),
    _CccaEventMessageId_Type()
)
cccaEventMessageId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cccaEventMessageId.setStatus("current")
_CccaEventOriginatingNode_Type = SnmpAdminString
_CccaEventOriginatingNode_Object = MibScalar
cccaEventOriginatingNode = _CccaEventOriginatingNode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 4, 4),
    _CccaEventOriginatingNode_Type()
)
cccaEventOriginatingNode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cccaEventOriginatingNode.setStatus("current")


class _CccaEventOriginatingNodeType_Type(Integer32):
    """Custom type cccaEventOriginatingNodeType based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("aw", 4),
          ("ba", 8),
          ("cg", 7),
          ("listener", 6),
          ("logger", 5),
          ("nic", 3),
          ("pg", 2),
          ("router", 1),
          ("unknown", 0))
    )


_CccaEventOriginatingNodeType_Type.__name__ = "Integer32"
_CccaEventOriginatingNodeType_Object = MibScalar
cccaEventOriginatingNodeType = _CccaEventOriginatingNodeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 4, 5),
    _CccaEventOriginatingNodeType_Type()
)
cccaEventOriginatingNodeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cccaEventOriginatingNodeType.setStatus("current")
_CccaEventOriginatingProcessName_Type = SnmpAdminString
_CccaEventOriginatingProcessName_Object = MibScalar
cccaEventOriginatingProcessName = _CccaEventOriginatingProcessName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 4, 6),
    _CccaEventOriginatingProcessName_Type()
)
cccaEventOriginatingProcessName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cccaEventOriginatingProcessName.setStatus("current")
_CccaEventOriginatingSide_Type = CcaComponentSide
_CccaEventOriginatingSide_Object = MibScalar
cccaEventOriginatingSide = _CccaEventOriginatingSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 4, 7),
    _CccaEventOriginatingSide_Type()
)
cccaEventOriginatingSide.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cccaEventOriginatingSide.setStatus("current")
_CccaEventDmpId_Type = Integer32
_CccaEventDmpId_Object = MibScalar
cccaEventDmpId = _CccaEventDmpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 4, 8),
    _CccaEventDmpId_Type()
)
cccaEventDmpId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cccaEventDmpId.setStatus("current")


class _CccaEventSeverity_Type(Integer32):
    """Custom type cccaEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("informational", 1),
          ("warning", 2))
    )


_CccaEventSeverity_Type.__name__ = "Integer32"
_CccaEventSeverity_Object = MibScalar
cccaEventSeverity = _CccaEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 4, 9),
    _CccaEventSeverity_Type()
)
cccaEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cccaEventSeverity.setStatus("current")
_CccaEventTimestamp_Type = DateAndTime
_CccaEventTimestamp_Object = MibScalar
cccaEventTimestamp = _CccaEventTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 4, 10),
    _CccaEventTimestamp_Type()
)
cccaEventTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cccaEventTimestamp.setStatus("current")
_CccaEventText_Type = SnmpAdminString
_CccaEventText_Object = MibScalar
cccaEventText = _CccaEventText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 1, 4, 11),
    _CccaEventText_Type()
)
cccaEventText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cccaEventText.setStatus("current")
_CiscoCcaMIBConform_ObjectIdentity = ObjectIdentity
ciscoCcaMIBConform = _CiscoCcaMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2)
)
_CiscoCcaMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCcaMIBCompliances = _CiscoCcaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 1)
)
_CiscoCcaMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCcaMIBGroups = _CiscoCcaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2)
)

# Managed Objects groups

cccaGeneralInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 1)
)
cccaGeneralInfoGroup.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDescription"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaVersion"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaTimeZoneName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaTimeZoneOffsetHours"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaTimeZoneOffsetMinutes"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaSupportToolsURL"))
)
if mibBuilder.loadTexts:
    cccaGeneralInfoGroup.setStatus("current")

cccaInstanceTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 2)
)
cccaInstanceTableGroup.setObjects(
    ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaInstanceName")
)
if mibBuilder.loadTexts:
    cccaInstanceTableGroup.setStatus("current")

cccaComponentTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 3)
)
cccaComponentTableGroup.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentType"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentStatus"))
)
if mibBuilder.loadTexts:
    cccaComponentTableGroup.setStatus("current")

cccaComponentElmtTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 4)
)
cccaComponentElmtTableGroup.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentElmtName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentElmtRunID"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaComponentElmtStatus"))
)
if mibBuilder.loadTexts:
    cccaComponentElmtTableGroup.setStatus("current")

cccaRouterTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 5)
)
cccaRouterTableGroup.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaRouterSide"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaRouterCallsPerSec"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaRouterAgentsLoggedOn"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaRouterCallsInProgress"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaRouterDuplexPairName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaRouterNicCount"))
)
if mibBuilder.loadTexts:
    cccaRouterTableGroup.setStatus("current")

cccaNicTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 6)
)
cccaNicTableGroup.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaNicType"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaNicStatus"))
)
if mibBuilder.loadTexts:
    cccaNicTableGroup.setStatus("current")

cccaLoggerTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 7)
)
cccaLoggerTableGroup.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaLoggerSide"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaLoggerType"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaLoggerRouterSideAName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaLoggerRouterSideBName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaLoggerDuplexPairName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaLoggerHDSReplication"))
)
if mibBuilder.loadTexts:
    cccaLoggerTableGroup.setStatus("current")

cccaDistAwTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 8)
)
cccaDistAwTableGroup.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDistAwSide"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDistAwType"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDistAwAdminSiteName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDistAwRouterSideAName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDistAwRouterSideBName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDistAwLoggerSideAName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDistAwLoggerSideBName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDistAwDuplexPairName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDistAwHDSEnabled"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDistAwWebViewEnabled"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDistAwWebViewServerName"))
)
if mibBuilder.loadTexts:
    cccaDistAwTableGroup.setStatus("current")

cccaPgTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 9)
)
cccaPgTableGroup.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaPgNumber"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaPgSide"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaPgRouterSideAName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaPgRouterSideBName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaPgDuplexPairName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaPgPimCount"))
)
if mibBuilder.loadTexts:
    cccaPgTableGroup.setStatus("current")

cccaPimTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 10)
)
cccaPimTableGroup.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaPimPeripheralName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaPimPeripheralType"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaPimStatus"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaPimPeripheralHostName"))
)
if mibBuilder.loadTexts:
    cccaPimTableGroup.setStatus("current")

cccaCgTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 11)
)
cccaCgTableGroup.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCgNumber"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCgSide"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCgPgSideAName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCgPgSideBName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCgDuplexPairName"))
)
if mibBuilder.loadTexts:
    cccaCgTableGroup.setStatus("current")

cccaCtiOsTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 12)
)
cccaCtiOsTableGroup.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCtiOsServerName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCtiOsPeripheralName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCtiOsPeripheralType"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCtiOsCgSideAName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCtiOsCgSideBName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCtiOsPeerName"))
)
if mibBuilder.loadTexts:
    cccaCtiOsTableGroup.setStatus("current")

cccaIcmNotificationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 13)
)
cccaIcmNotificationInfoGroup.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventComponentId"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventState"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventMessageId"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventOriginatingNode"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventOriginatingNodeType"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventOriginatingProcessName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventOriginatingSide"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventDmpId"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventSeverity"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventTimestamp"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventText"))
)
if mibBuilder.loadTexts:
    cccaIcmNotificationInfoGroup.setStatus("current")

cccaCampaignMgrTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 15)
)
cccaCampaignMgrTableGroup.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCampaignMgrDbUtilization"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCampaignMgrQueueDepth"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCampaignMgrAvgQueueTime"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCampaignMgrActiveDialers"))
)
if mibBuilder.loadTexts:
    cccaCampaignMgrTableGroup.setStatus("current")

cccaDialerTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 16)
)
cccaDialerTableGroup.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDialerCampaignMgrName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDialerCampaignMgrStatus"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDialerCtiServerAName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDialerCtiServerBName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDialerCtiServerStatus"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDialerMediaRouterStatus"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDialerQueueDepth"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDialerAvgQueueTime"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDialerTalkingAgents"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDialerCallAttemptsPerSec"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDialerConfiguredPorts"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDialerBusyCustomerPorts"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDialerBusyReservationPorts"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDialerIdlePorts"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDialerBlockedPorts"))
)
if mibBuilder.loadTexts:
    cccaDialerTableGroup.setStatus("current")

cccaGeneralInfoGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 17)
)
cccaGeneralInfoGroupSup1.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaWebSetupURL"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaNotificationsEnabled"))
)
if mibBuilder.loadTexts:
    cccaGeneralInfoGroupSup1.setStatus("current")

cccaRouterTableGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 18)
)
cccaRouterTableGroupSup1.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaRouterPGsEnabledCount"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaRouterCallsInQueue"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaRouterAppGwEnabled"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaRouterDBWorkerEnabled"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaRouterPublicHighAddr"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaRouterPublicNonHighAddr"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaRouterPrivateHighAddr"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaRouterPrivateNonHighAddr"))
)
if mibBuilder.loadTexts:
    cccaRouterTableGroupSup1.setStatus("current")

cccaLoggerTableGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 19)
)
cccaLoggerTableGroupSup1.setObjects(
    ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaLoggerAvgDBWriteTime")
)
if mibBuilder.loadTexts:
    cccaLoggerTableGroupSup1.setStatus("current")

cccaDistAwTableGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 20)
)
cccaDistAwTableGroupSup1.setObjects(
    ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaDistAwWebReskillingURL")
)
if mibBuilder.loadTexts:
    cccaDistAwTableGroupSup1.setStatus("current")

cccaPgTableGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 21)
)
cccaPgTableGroupSup1.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaPgCallsInProgress"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaPgAgentsLoggedOn"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaPgAgentsReady"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaPgAgentsTalking"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaPgID"))
)
if mibBuilder.loadTexts:
    cccaPgTableGroupSup1.setStatus("current")

cccaCgTableGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 22)
)
cccaCgTableGroupSup1.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCgOpenSessions"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCgOtherSessions"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCgID"))
)
if mibBuilder.loadTexts:
    cccaCgTableGroupSup1.setStatus("current")

cccaCtiOsTableGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 23)
)
cccaCtiOsTableGroupSup1.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCtiOsActiveClients"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCtiOsActiveMonitors"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCtiOsCallsInProgress"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaCtiOsCallsFailed"))
)
if mibBuilder.loadTexts:
    cccaCtiOsTableGroupSup1.setStatus("current")


# Notification objects

cccaIcmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 0, 1)
)
cccaIcmEvent.setObjects(
      *(("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventComponentId"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventState"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventMessageId"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventOriginatingNode"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventOriginatingNodeType"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventOriginatingProcessName"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventOriginatingSide"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventDmpId"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventSeverity"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventTimestamp"),
        ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaEventText"))
)
if mibBuilder.loadTexts:
    cccaIcmEvent.setStatus(
        "current"
    )


# Notifications groups

cccaIcmEventsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 2, 14)
)
cccaIcmEventsGroup.setObjects(
    ("CISCO-CONTACT-CENTER-APPS-MIB", "cccaIcmEvent")
)
if mibBuilder.loadTexts:
    cccaIcmEventsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCccaMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCccaMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoCccaMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 473, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCccaMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CONTACT-CENTER-APPS-MIB",
    **{"CcaIndex": CcaIndex,
       "CcaComponentType": CcaComponentType,
       "CcaComponentStatus": CcaComponentStatus,
       "CcaComponentSide": CcaComponentSide,
       "CcaPeripheralType": CcaPeripheralType,
       "ciscoCcaMIB": ciscoCcaMIB,
       "ciscoCcaMIBNotifs": ciscoCcaMIBNotifs,
       "cccaIcmEvent": cccaIcmEvent,
       "ciscoCcaMIBObjects": ciscoCcaMIBObjects,
       "cccaGeneralInfo": cccaGeneralInfo,
       "cccaName": cccaName,
       "cccaDescription": cccaDescription,
       "cccaVersion": cccaVersion,
       "cccaTimeZoneName": cccaTimeZoneName,
       "cccaTimeZoneOffsetHours": cccaTimeZoneOffsetHours,
       "cccaTimeZoneOffsetMinutes": cccaTimeZoneOffsetMinutes,
       "cccaSupportToolsURL": cccaSupportToolsURL,
       "cccaWebSetupURL": cccaWebSetupURL,
       "cccaNotificationsEnabled": cccaNotificationsEnabled,
       "cccaComponents": cccaComponents,
       "cccaInstanceTable": cccaInstanceTable,
       "cccaInstanceEntry": cccaInstanceEntry,
       "cccaInstanceNumber": cccaInstanceNumber,
       "cccaInstanceName": cccaInstanceName,
       "cccaComponentTable": cccaComponentTable,
       "cccaComponentEntry": cccaComponentEntry,
       "cccaComponentIndex": cccaComponentIndex,
       "cccaComponentType": cccaComponentType,
       "cccaComponentName": cccaComponentName,
       "cccaComponentStatus": cccaComponentStatus,
       "cccaComponentElmtTable": cccaComponentElmtTable,
       "cccaComponentElmtEntry": cccaComponentElmtEntry,
       "cccaComponentElmtIndex": cccaComponentElmtIndex,
       "cccaComponentElmtName": cccaComponentElmtName,
       "cccaComponentElmtRunID": cccaComponentElmtRunID,
       "cccaComponentElmtStatus": cccaComponentElmtStatus,
       "cccaComponentInfo": cccaComponentInfo,
       "cccaRouterTable": cccaRouterTable,
       "cccaRouterEntry": cccaRouterEntry,
       "cccaRouterSide": cccaRouterSide,
       "cccaRouterCallsPerSec": cccaRouterCallsPerSec,
       "cccaRouterAgentsLoggedOn": cccaRouterAgentsLoggedOn,
       "cccaRouterCallsInProgress": cccaRouterCallsInProgress,
       "cccaRouterDuplexPairName": cccaRouterDuplexPairName,
       "cccaRouterNicCount": cccaRouterNicCount,
       "cccaRouterPGsEnabledCount": cccaRouterPGsEnabledCount,
       "cccaRouterCallsInQueue": cccaRouterCallsInQueue,
       "cccaRouterAppGwEnabled": cccaRouterAppGwEnabled,
       "cccaRouterDBWorkerEnabled": cccaRouterDBWorkerEnabled,
       "cccaRouterPublicHighAddr": cccaRouterPublicHighAddr,
       "cccaRouterPublicNonHighAddr": cccaRouterPublicNonHighAddr,
       "cccaRouterPrivateHighAddr": cccaRouterPrivateHighAddr,
       "cccaRouterPrivateNonHighAddr": cccaRouterPrivateNonHighAddr,
       "cccaNicTable": cccaNicTable,
       "cccaNicEntry": cccaNicEntry,
       "cccaNicIndex": cccaNicIndex,
       "cccaNicType": cccaNicType,
       "cccaNicStatus": cccaNicStatus,
       "cccaLoggerTable": cccaLoggerTable,
       "cccaLoggerEntry": cccaLoggerEntry,
       "cccaLoggerSide": cccaLoggerSide,
       "cccaLoggerType": cccaLoggerType,
       "cccaLoggerRouterSideAName": cccaLoggerRouterSideAName,
       "cccaLoggerRouterSideBName": cccaLoggerRouterSideBName,
       "cccaLoggerDuplexPairName": cccaLoggerDuplexPairName,
       "cccaLoggerHDSReplication": cccaLoggerHDSReplication,
       "cccaLoggerAvgDBWriteTime": cccaLoggerAvgDBWriteTime,
       "cccaDistAwTable": cccaDistAwTable,
       "cccaDistAwEntry": cccaDistAwEntry,
       "cccaDistAwSide": cccaDistAwSide,
       "cccaDistAwType": cccaDistAwType,
       "cccaDistAwAdminSiteName": cccaDistAwAdminSiteName,
       "cccaDistAwRouterSideAName": cccaDistAwRouterSideAName,
       "cccaDistAwRouterSideBName": cccaDistAwRouterSideBName,
       "cccaDistAwLoggerSideAName": cccaDistAwLoggerSideAName,
       "cccaDistAwLoggerSideBName": cccaDistAwLoggerSideBName,
       "cccaDistAwDuplexPairName": cccaDistAwDuplexPairName,
       "cccaDistAwHDSEnabled": cccaDistAwHDSEnabled,
       "cccaDistAwWebViewEnabled": cccaDistAwWebViewEnabled,
       "cccaDistAwWebViewServerName": cccaDistAwWebViewServerName,
       "cccaDistAwWebReskillingURL": cccaDistAwWebReskillingURL,
       "cccaPgTable": cccaPgTable,
       "cccaPgEntry": cccaPgEntry,
       "cccaPgNumber": cccaPgNumber,
       "cccaPgSide": cccaPgSide,
       "cccaPgRouterSideAName": cccaPgRouterSideAName,
       "cccaPgRouterSideBName": cccaPgRouterSideBName,
       "cccaPgDuplexPairName": cccaPgDuplexPairName,
       "cccaPgPimCount": cccaPgPimCount,
       "cccaPgCallsInProgress": cccaPgCallsInProgress,
       "cccaPgAgentsLoggedOn": cccaPgAgentsLoggedOn,
       "cccaPgAgentsReady": cccaPgAgentsReady,
       "cccaPgAgentsTalking": cccaPgAgentsTalking,
       "cccaPgID": cccaPgID,
       "cccaPimTable": cccaPimTable,
       "cccaPimEntry": cccaPimEntry,
       "cccaPimNumber": cccaPimNumber,
       "cccaPimPeripheralName": cccaPimPeripheralName,
       "cccaPimPeripheralType": cccaPimPeripheralType,
       "cccaPimStatus": cccaPimStatus,
       "cccaPimPeripheralHostName": cccaPimPeripheralHostName,
       "cccaCgTable": cccaCgTable,
       "cccaCgEntry": cccaCgEntry,
       "cccaCgNumber": cccaCgNumber,
       "cccaCgSide": cccaCgSide,
       "cccaCgPgSideAName": cccaCgPgSideAName,
       "cccaCgPgSideBName": cccaCgPgSideBName,
       "cccaCgDuplexPairName": cccaCgDuplexPairName,
       "cccaCgOpenSessions": cccaCgOpenSessions,
       "cccaCgOtherSessions": cccaCgOtherSessions,
       "cccaCgID": cccaCgID,
       "cccaCtiOsTable": cccaCtiOsTable,
       "cccaCtiOsEntry": cccaCtiOsEntry,
       "cccaCtiOsServerName": cccaCtiOsServerName,
       "cccaCtiOsPeripheralName": cccaCtiOsPeripheralName,
       "cccaCtiOsPeripheralType": cccaCtiOsPeripheralType,
       "cccaCtiOsCgSideAName": cccaCtiOsCgSideAName,
       "cccaCtiOsCgSideBName": cccaCtiOsCgSideBName,
       "cccaCtiOsPeerName": cccaCtiOsPeerName,
       "cccaCtiOsActiveClients": cccaCtiOsActiveClients,
       "cccaCtiOsActiveMonitors": cccaCtiOsActiveMonitors,
       "cccaCtiOsCallsInProgress": cccaCtiOsCallsInProgress,
       "cccaCtiOsCallsFailed": cccaCtiOsCallsFailed,
       "cccaCampaignMgrTable": cccaCampaignMgrTable,
       "cccaCampaignMgrEntry": cccaCampaignMgrEntry,
       "cccaCampaignMgrDbUtilization": cccaCampaignMgrDbUtilization,
       "cccaCampaignMgrQueueDepth": cccaCampaignMgrQueueDepth,
       "cccaCampaignMgrAvgQueueTime": cccaCampaignMgrAvgQueueTime,
       "cccaCampaignMgrActiveDialers": cccaCampaignMgrActiveDialers,
       "cccaDialerTable": cccaDialerTable,
       "cccaDialerEntry": cccaDialerEntry,
       "cccaDialerCampaignMgrName": cccaDialerCampaignMgrName,
       "cccaDialerCampaignMgrStatus": cccaDialerCampaignMgrStatus,
       "cccaDialerCtiServerAName": cccaDialerCtiServerAName,
       "cccaDialerCtiServerBName": cccaDialerCtiServerBName,
       "cccaDialerCtiServerStatus": cccaDialerCtiServerStatus,
       "cccaDialerMediaRouterStatus": cccaDialerMediaRouterStatus,
       "cccaDialerQueueDepth": cccaDialerQueueDepth,
       "cccaDialerAvgQueueTime": cccaDialerAvgQueueTime,
       "cccaDialerTalkingAgents": cccaDialerTalkingAgents,
       "cccaDialerCallAttemptsPerSec": cccaDialerCallAttemptsPerSec,
       "cccaDialerConfiguredPorts": cccaDialerConfiguredPorts,
       "cccaDialerBusyCustomerPorts": cccaDialerBusyCustomerPorts,
       "cccaDialerBusyReservationPorts": cccaDialerBusyReservationPorts,
       "cccaDialerIdlePorts": cccaDialerIdlePorts,
       "cccaDialerBlockedPorts": cccaDialerBlockedPorts,
       "cccaNotificationInfo": cccaNotificationInfo,
       "cccaEventComponentId": cccaEventComponentId,
       "cccaEventState": cccaEventState,
       "cccaEventMessageId": cccaEventMessageId,
       "cccaEventOriginatingNode": cccaEventOriginatingNode,
       "cccaEventOriginatingNodeType": cccaEventOriginatingNodeType,
       "cccaEventOriginatingProcessName": cccaEventOriginatingProcessName,
       "cccaEventOriginatingSide": cccaEventOriginatingSide,
       "cccaEventDmpId": cccaEventDmpId,
       "cccaEventSeverity": cccaEventSeverity,
       "cccaEventTimestamp": cccaEventTimestamp,
       "cccaEventText": cccaEventText,
       "ciscoCcaMIBConform": ciscoCcaMIBConform,
       "ciscoCcaMIBCompliances": ciscoCcaMIBCompliances,
       "ciscoCccaMIBComplianceRev1": ciscoCccaMIBComplianceRev1,
       "ciscoCccaMIBComplianceRev2": ciscoCccaMIBComplianceRev2,
       "ciscoCcaMIBGroups": ciscoCcaMIBGroups,
       "cccaGeneralInfoGroup": cccaGeneralInfoGroup,
       "cccaInstanceTableGroup": cccaInstanceTableGroup,
       "cccaComponentTableGroup": cccaComponentTableGroup,
       "cccaComponentElmtTableGroup": cccaComponentElmtTableGroup,
       "cccaRouterTableGroup": cccaRouterTableGroup,
       "cccaNicTableGroup": cccaNicTableGroup,
       "cccaLoggerTableGroup": cccaLoggerTableGroup,
       "cccaDistAwTableGroup": cccaDistAwTableGroup,
       "cccaPgTableGroup": cccaPgTableGroup,
       "cccaPimTableGroup": cccaPimTableGroup,
       "cccaCgTableGroup": cccaCgTableGroup,
       "cccaCtiOsTableGroup": cccaCtiOsTableGroup,
       "cccaIcmNotificationInfoGroup": cccaIcmNotificationInfoGroup,
       "cccaIcmEventsGroup": cccaIcmEventsGroup,
       "cccaCampaignMgrTableGroup": cccaCampaignMgrTableGroup,
       "cccaDialerTableGroup": cccaDialerTableGroup,
       "cccaGeneralInfoGroupSup1": cccaGeneralInfoGroupSup1,
       "cccaRouterTableGroupSup1": cccaRouterTableGroupSup1,
       "cccaLoggerTableGroupSup1": cccaLoggerTableGroupSup1,
       "cccaDistAwTableGroupSup1": cccaDistAwTableGroupSup1,
       "cccaPgTableGroupSup1": cccaPgTableGroupSup1,
       "cccaCgTableGroupSup1": cccaCgTableGroupSup1,
       "cccaCtiOsTableGroupSup1": cccaCtiOsTableGroupSup1}
)
