# SNMP MIB module (CISCO-LWAPP-MFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-MFP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:46 2024
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

(cLApEntry,
 cLApIfSmtDot11Bssid,
 cLApIfSmtParamEntry) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApEntry",
    "cLApIfSmtDot11Bssid",
    "cLApIfSmtParamEntry")

(cldcClientMacAddress,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "cldcClientMacAddress")

(CLEventFrames,
 CLMfpEventType,
 CLMfpVersion,
 CLTimeBaseStatus) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLEventFrames",
    "CLMfpEventType",
    "CLMfpVersion",
    "CLTimeBaseStatus")

(cLWlanConfigEntry,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanConfigEntry")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappMfpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 518)
)
ciscoLwappMfpMIB.setRevisions(
        ("2007-01-20 15:45",
         "2006-04-10 15:45")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappMfpMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappMfpMIBNotifs = _CiscoLwappMfpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 0)
)
_CiscoLwappMfpMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMfpMIBNotifObjects = _CiscoLwappMfpMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 1)
)
_CLApMacAddress_Type = MacAddress
_CLApMacAddress_Object = MibScalar
cLApMacAddress = _CLApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 1),
    _CLApMacAddress_Type()
)
cLApMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApMacAddress.setStatus("current")


class _CLApDot11IfSlotIdx_Type(Unsigned32):
    """Custom type cLApDot11IfSlotIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CLApDot11IfSlotIdx_Type.__name__ = "Unsigned32"
_CLApDot11IfSlotIdx_Object = MibScalar
cLApDot11IfSlotIdx = _CLApDot11IfSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 2),
    _CLApDot11IfSlotIdx_Type()
)
cLApDot11IfSlotIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApDot11IfSlotIdx.setStatus("current")
_CLWlanIdx_Type = Unsigned32
_CLWlanIdx_Object = MibScalar
cLWlanIdx = _CLWlanIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 3),
    _CLWlanIdx_Type()
)
cLWlanIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLWlanIdx.setStatus("current")
_CLMfpApIfMfpProtectionActual_Type = TruthValue
_CLMfpApIfMfpProtectionActual_Object = MibScalar
cLMfpApIfMfpProtectionActual = _CLMfpApIfMfpProtectionActual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 4),
    _CLMfpApIfMfpProtectionActual_Type()
)
cLMfpApIfMfpProtectionActual.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLMfpApIfMfpProtectionActual.setStatus("current")
_CLMfpEventType_Type = CLMfpEventType
_CLMfpEventType_Object = MibScalar
cLMfpEventType = _CLMfpEventType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 5),
    _CLMfpEventType_Type()
)
cLMfpEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLMfpEventType.setStatus("current")
_CLMfpEventTotal_Type = Gauge32
_CLMfpEventTotal_Object = MibScalar
cLMfpEventTotal = _CLMfpEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 6),
    _CLMfpEventTotal_Type()
)
cLMfpEventTotal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLMfpEventTotal.setStatus("current")
_CLMfpEventPeriod_Type = TimeInterval
_CLMfpEventPeriod_Object = MibScalar
cLMfpEventPeriod = _CLMfpEventPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 7),
    _CLMfpEventPeriod_Type()
)
cLMfpEventPeriod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLMfpEventPeriod.setStatus("current")
_CLMfpEventFrames_Type = CLEventFrames
_CLMfpEventFrames_Object = MibScalar
cLMfpEventFrames = _CLMfpEventFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 8),
    _CLMfpEventFrames_Type()
)
cLMfpEventFrames.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLMfpEventFrames.setStatus("current")
_CLClientLastSourceMacAddress_Type = MacAddress
_CLClientLastSourceMacAddress_Object = MibScalar
cLClientLastSourceMacAddress = _CLClientLastSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 10),
    _CLClientLastSourceMacAddress_Type()
)
cLClientLastSourceMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLClientLastSourceMacAddress.setStatus("current")
_CiscoLwappMfpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMfpMIBObjects = _CiscoLwappMfpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2)
)
_CiscoLwappMfpConfig_ObjectIdentity = ObjectIdentity
ciscoLwappMfpConfig = _CiscoLwappMfpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 1)
)


class _CLMfpProtectType_Type(Integer32):
    """Custom type cLMfpProtectType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cLMfpProtectApAuth", 2),
          ("cLMfpProtectMfp", 3),
          ("cLMfpProtectNone", 1))
    )


_CLMfpProtectType_Type.__name__ = "Integer32"
_CLMfpProtectType_Object = MibScalar
cLMfpProtectType = _CLMfpProtectType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 1, 1),
    _CLMfpProtectType_Type()
)
cLMfpProtectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMfpProtectType.setStatus("current")
_CLMfpWlanConfigTable_Object = MibTable
cLMfpWlanConfigTable = _CLMfpWlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cLMfpWlanConfigTable.setStatus("current")
_CLMfpWlanConfigEntry_Object = MibTableRow
cLMfpWlanConfigEntry = _CLMfpWlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cLMfpWlanConfigEntry.setStatus("current")


class _CLMfpVersionRequired_Type(CLMfpVersion):
    """Custom type cLMfpVersionRequired based on CLMfpVersion"""


_CLMfpVersionRequired_Object = MibTableColumn
cLMfpVersionRequired = _CLMfpVersionRequired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 1, 2, 1, 2),
    _CLMfpVersionRequired_Type()
)
cLMfpVersionRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMfpVersionRequired.setStatus("current")


class _CLMfpProtectionEnable_Type(TruthValue):
    """Custom type cLMfpProtectionEnable based on TruthValue"""


_CLMfpProtectionEnable_Object = MibTableColumn
cLMfpProtectionEnable = _CLMfpProtectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 1, 2, 1, 3),
    _CLMfpProtectionEnable_Type()
)
cLMfpProtectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMfpProtectionEnable.setStatus("current")


class _CLMfpClientProtection_Type(Integer32):
    """Custom type cLMfpClientProtection based on Integer32"""
    defaultValue = 2

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
          ("enabled", 2),
          ("required", 3))
    )


_CLMfpClientProtection_Type.__name__ = "Integer32"
_CLMfpClientProtection_Object = MibTableColumn
cLMfpClientProtection = _CLMfpClientProtection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 1, 2, 1, 4),
    _CLMfpClientProtection_Type()
)
cLMfpClientProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMfpClientProtection.setStatus("current")
_CiscoLwappMfpStatus_ObjectIdentity = ObjectIdentity
ciscoLwappMfpStatus = _CiscoLwappMfpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2)
)
_CLMfpCtrlTimeBaseStatus_Type = CLTimeBaseStatus
_CLMfpCtrlTimeBaseStatus_Object = MibScalar
cLMfpCtrlTimeBaseStatus = _CLMfpCtrlTimeBaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 1),
    _CLMfpCtrlTimeBaseStatus_Type()
)
cLMfpCtrlTimeBaseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMfpCtrlTimeBaseStatus.setStatus("current")
_CLMfpApParamTable_Object = MibTable
cLMfpApParamTable = _CLMfpApParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cLMfpApParamTable.setStatus("current")
_CLMfpApParamEntry_Object = MibTableRow
cLMfpApParamEntry = _CLMfpApParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cLMfpApParamEntry.setStatus("current")


class _CLMfpApMfpValidationEnable_Type(TruthValue):
    """Custom type cLMfpApMfpValidationEnable based on TruthValue"""


_CLMfpApMfpValidationEnable_Object = MibTableColumn
cLMfpApMfpValidationEnable = _CLMfpApMfpValidationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 2, 1, 1),
    _CLMfpApMfpValidationEnable_Type()
)
cLMfpApMfpValidationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMfpApMfpValidationEnable.setStatus("current")
_CLMfpApMfpValidationActual_Type = TruthValue
_CLMfpApMfpValidationActual_Object = MibTableColumn
cLMfpApMfpValidationActual = _CLMfpApMfpValidationActual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 2, 1, 2),
    _CLMfpApMfpValidationActual_Type()
)
cLMfpApMfpValidationActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMfpApMfpValidationActual.setStatus("current")
_CLMfpApIfSmtCapTable_Object = MibTable
cLMfpApIfSmtCapTable = _CLMfpApIfSmtCapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cLMfpApIfSmtCapTable.setStatus("current")
_CLMfpApIfSmtCapEntry_Object = MibTableRow
cLMfpApIfSmtCapEntry = _CLMfpApIfSmtCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cLMfpApIfSmtCapEntry.setStatus("current")
_CLMfpApIfMfpVersionSupported_Type = CLMfpVersion
_CLMfpApIfMfpVersionSupported_Object = MibTableColumn
cLMfpApIfMfpVersionSupported = _CLMfpApIfMfpVersionSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 3, 1, 1),
    _CLMfpApIfMfpVersionSupported_Type()
)
cLMfpApIfMfpVersionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMfpApIfMfpVersionSupported.setStatus("current")


class _CLMfpApIfMfpProtectionCapability_Type(Integer32):
    """Custom type cLMfpApIfMfpProtectionCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("protectCapAllFrames", 3),
          ("protectCapNoBeacon", 2),
          ("protectCapNone", 1))
    )


_CLMfpApIfMfpProtectionCapability_Type.__name__ = "Integer32"
_CLMfpApIfMfpProtectionCapability_Object = MibTableColumn
cLMfpApIfMfpProtectionCapability = _CLMfpApIfMfpProtectionCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 3, 1, 2),
    _CLMfpApIfMfpProtectionCapability_Type()
)
cLMfpApIfMfpProtectionCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMfpApIfMfpProtectionCapability.setStatus("current")


class _CLMfpApIfMfpValidationCapability_Type(Integer32):
    """Custom type cLMfpApIfMfpValidationCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("validateCapAllFrames", 2),
          ("validateCapNone", 1))
    )


_CLMfpApIfMfpValidationCapability_Type.__name__ = "Integer32"
_CLMfpApIfMfpValidationCapability_Object = MibTableColumn
cLMfpApIfMfpValidationCapability = _CLMfpApIfMfpValidationCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 3, 1, 3),
    _CLMfpApIfMfpValidationCapability_Type()
)
cLMfpApIfMfpValidationCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMfpApIfMfpValidationCapability.setStatus("current")


class _CLMfpCtrlNotifEnable_Type(TruthValue):
    """Custom type cLMfpCtrlNotifEnable based on TruthValue"""


_CLMfpCtrlNotifEnable_Object = MibScalar
cLMfpCtrlNotifEnable = _CLMfpCtrlNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 4),
    _CLMfpCtrlNotifEnable_Type()
)
cLMfpCtrlNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMfpCtrlNotifEnable.setStatus("current")
_CLMfpClientTable_Object = MibTable
cLMfpClientTable = _CLMfpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 5)
)
if mibBuilder.loadTexts:
    cLMfpClientTable.setStatus("current")
_CLMfpClientEntry_Object = MibTableRow
cLMfpClientEntry = _CLMfpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 5, 1)
)
cLMfpClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cLMfpClientEntry.setStatus("current")
_CLMfpClientMfpEnabled_Type = TruthValue
_CLMfpClientMfpEnabled_Object = MibTableColumn
cLMfpClientMfpEnabled = _CLMfpClientMfpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 5, 1, 1),
    _CLMfpClientMfpEnabled_Type()
)
cLMfpClientMfpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMfpClientMfpEnabled.setStatus("current")
_CiscoLwappMfpMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappMfpMIBConform = _CiscoLwappMfpMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 3)
)
_CiscoLwappMfpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappMfpMIBCompliances = _CiscoLwappMfpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 1)
)
_CiscoLwappMfpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappMfpMIBGroups = _CiscoLwappMfpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2)
)
cLWlanConfigEntry.registerAugmentions(
    ("CISCO-LWAPP-MFP-MIB",
     "cLMfpWlanConfigEntry")
)
cLMfpWlanConfigEntry.setIndexNames(*cLWlanConfigEntry.getIndexNames())
cLApEntry.registerAugmentions(
    ("CISCO-LWAPP-MFP-MIB",
     "cLMfpApParamEntry")
)
cLMfpApParamEntry.setIndexNames(*cLApEntry.getIndexNames())
cLApIfSmtParamEntry.registerAugmentions(
    ("CISCO-LWAPP-MFP-MIB",
     "cLMfpApIfSmtCapEntry")
)
cLMfpApIfSmtCapEntry.setIndexNames(*cLApIfSmtParamEntry.getIndexNames())

# Managed Objects groups

ciscoLwappMfpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2, 1)
)
ciscoLwappMfpConfigGroup.setObjects(
      *(("CISCO-LWAPP-MFP-MIB", "cLMfpProtectType"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpVersionRequired"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpProtectionEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappMfpConfigGroup.setStatus("current")

ciscoLwappMfpStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2, 2)
)
ciscoLwappMfpStatusGroup.setObjects(
      *(("CISCO-LWAPP-MFP-MIB", "cLMfpCtrlTimeBaseStatus"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpCtrlNotifEnable"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpApIfMfpVersionSupported"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpApIfMfpProtectionCapability"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpApIfMfpValidationCapability"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpApMfpValidationEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappMfpStatusGroup.setStatus("current")

ciscoLwappMfpNotifObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2, 3)
)
ciscoLwappMfpNotifObjsGroup.setObjects(
      *(("CISCO-LWAPP-MFP-MIB", "cLApMacAddress"),
        ("CISCO-LWAPP-MFP-MIB", "cLApDot11IfSlotIdx"),
        ("CISCO-LWAPP-MFP-MIB", "cLWlanIdx"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpApIfMfpProtectionActual"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpApMfpValidationActual"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpEventType"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpEventTotal"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpEventPeriod"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpEventFrames"))
)
if mibBuilder.loadTexts:
    ciscoLwappMfpNotifObjsGroup.setStatus("current")

ciscoLwappMfpConfigSup1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2, 5)
)
ciscoLwappMfpConfigSup1Group.setObjects(
    ("CISCO-LWAPP-MFP-MIB", "cLMfpClientProtection")
)
if mibBuilder.loadTexts:
    ciscoLwappMfpConfigSup1Group.setStatus("current")

ciscoLwappMfpStatusSup1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2, 6)
)
ciscoLwappMfpStatusSup1Group.setObjects(
    ("CISCO-LWAPP-MFP-MIB", "cLMfpClientMfpEnabled")
)
if mibBuilder.loadTexts:
    ciscoLwappMfpStatusSup1Group.setStatus("current")

ciscoLwappMfpNotifObjsSup1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2, 7)
)
ciscoLwappMfpNotifObjsSup1Group.setObjects(
    ("CISCO-LWAPP-MFP-MIB", "cLClientLastSourceMacAddress")
)
if mibBuilder.loadTexts:
    ciscoLwappMfpNotifObjsSup1Group.setStatus("current")


# Notification objects

ciscoLwappMfpProtectConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 0, 1)
)
ciscoLwappMfpProtectConfigMismatch.setObjects(
      *(("CISCO-LWAPP-MFP-MIB", "cLApMacAddress"),
        ("CISCO-LWAPP-MFP-MIB", "cLApDot11IfSlotIdx"),
        ("CISCO-LWAPP-MFP-MIB", "cLWlanIdx"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpProtectionEnable"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpApIfMfpProtectionActual"))
)
if mibBuilder.loadTexts:
    ciscoLwappMfpProtectConfigMismatch.setStatus(
        "current"
    )

ciscoLwappMfpValidationConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 0, 2)
)
ciscoLwappMfpValidationConfigMismatch.setObjects(
      *(("CISCO-LWAPP-MFP-MIB", "cLApMacAddress"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpApMfpValidationEnable"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpApMfpValidationActual"))
)
if mibBuilder.loadTexts:
    ciscoLwappMfpValidationConfigMismatch.setStatus(
        "current"
    )

ciscoLwappMfpTimebaseStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 0, 3)
)
ciscoLwappMfpTimebaseStatus.setObjects(
    ("CISCO-LWAPP-MFP-MIB", "cLMfpCtrlTimeBaseStatus")
)
if mibBuilder.loadTexts:
    ciscoLwappMfpTimebaseStatus.setStatus(
        "current"
    )

ciscoLwappMfpAnomalyDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 0, 4)
)
ciscoLwappMfpAnomalyDetected.setObjects(
      *(("CISCO-LWAPP-MFP-MIB", "cLApMacAddress"),
        ("CISCO-LWAPP-MFP-MIB", "cLApDot11IfSlotIdx"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfSmtDot11Bssid"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpEventType"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpEventTotal"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpEventPeriod"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpEventFrames"))
)
if mibBuilder.loadTexts:
    ciscoLwappMfpAnomalyDetected.setStatus(
        "deprecated"
    )

ciscoLwappMfpAnomalyDetected1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 0, 5)
)
ciscoLwappMfpAnomalyDetected1.setObjects(
      *(("CISCO-LWAPP-MFP-MIB", "cLApMacAddress"),
        ("CISCO-LWAPP-MFP-MIB", "cLApDot11IfSlotIdx"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfSmtDot11Bssid"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpEventType"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpEventTotal"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpEventPeriod"),
        ("CISCO-LWAPP-MFP-MIB", "cLMfpEventFrames"),
        ("CISCO-LWAPP-MFP-MIB", "cLClientLastSourceMacAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappMfpAnomalyDetected1.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappMfpNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2, 4)
)
ciscoLwappMfpNotifsGroup.setObjects(
      *(("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpProtectConfigMismatch"),
        ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpValidationConfigMismatch"),
        ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpTimebaseStatus"),
        ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpAnomalyDetected"))
)
if mibBuilder.loadTexts:
    ciscoLwappMfpNotifsGroup.setStatus(
        "deprecated"
    )

ciscoLwappMfpNotifsNewGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2, 8)
)
ciscoLwappMfpNotifsNewGroup.setObjects(
      *(("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpProtectConfigMismatch"),
        ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpValidationConfigMismatch"),
        ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpTimebaseStatus"),
        ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpAnomalyDetected1"))
)
if mibBuilder.loadTexts:
    ciscoLwappMfpNotifsNewGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappMfpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappMfpMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappMfpMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappMfpMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-MFP-MIB",
    **{"ciscoLwappMfpMIB": ciscoLwappMfpMIB,
       "ciscoLwappMfpMIBNotifs": ciscoLwappMfpMIBNotifs,
       "ciscoLwappMfpProtectConfigMismatch": ciscoLwappMfpProtectConfigMismatch,
       "ciscoLwappMfpValidationConfigMismatch": ciscoLwappMfpValidationConfigMismatch,
       "ciscoLwappMfpTimebaseStatus": ciscoLwappMfpTimebaseStatus,
       "ciscoLwappMfpAnomalyDetected": ciscoLwappMfpAnomalyDetected,
       "ciscoLwappMfpAnomalyDetected1": ciscoLwappMfpAnomalyDetected1,
       "ciscoLwappMfpMIBNotifObjects": ciscoLwappMfpMIBNotifObjects,
       "cLApMacAddress": cLApMacAddress,
       "cLApDot11IfSlotIdx": cLApDot11IfSlotIdx,
       "cLWlanIdx": cLWlanIdx,
       "cLMfpApIfMfpProtectionActual": cLMfpApIfMfpProtectionActual,
       "cLMfpEventType": cLMfpEventType,
       "cLMfpEventTotal": cLMfpEventTotal,
       "cLMfpEventPeriod": cLMfpEventPeriod,
       "cLMfpEventFrames": cLMfpEventFrames,
       "cLClientLastSourceMacAddress": cLClientLastSourceMacAddress,
       "ciscoLwappMfpMIBObjects": ciscoLwappMfpMIBObjects,
       "ciscoLwappMfpConfig": ciscoLwappMfpConfig,
       "cLMfpProtectType": cLMfpProtectType,
       "cLMfpWlanConfigTable": cLMfpWlanConfigTable,
       "cLMfpWlanConfigEntry": cLMfpWlanConfigEntry,
       "cLMfpVersionRequired": cLMfpVersionRequired,
       "cLMfpProtectionEnable": cLMfpProtectionEnable,
       "cLMfpClientProtection": cLMfpClientProtection,
       "ciscoLwappMfpStatus": ciscoLwappMfpStatus,
       "cLMfpCtrlTimeBaseStatus": cLMfpCtrlTimeBaseStatus,
       "cLMfpApParamTable": cLMfpApParamTable,
       "cLMfpApParamEntry": cLMfpApParamEntry,
       "cLMfpApMfpValidationEnable": cLMfpApMfpValidationEnable,
       "cLMfpApMfpValidationActual": cLMfpApMfpValidationActual,
       "cLMfpApIfSmtCapTable": cLMfpApIfSmtCapTable,
       "cLMfpApIfSmtCapEntry": cLMfpApIfSmtCapEntry,
       "cLMfpApIfMfpVersionSupported": cLMfpApIfMfpVersionSupported,
       "cLMfpApIfMfpProtectionCapability": cLMfpApIfMfpProtectionCapability,
       "cLMfpApIfMfpValidationCapability": cLMfpApIfMfpValidationCapability,
       "cLMfpCtrlNotifEnable": cLMfpCtrlNotifEnable,
       "cLMfpClientTable": cLMfpClientTable,
       "cLMfpClientEntry": cLMfpClientEntry,
       "cLMfpClientMfpEnabled": cLMfpClientMfpEnabled,
       "ciscoLwappMfpMIBConform": ciscoLwappMfpMIBConform,
       "ciscoLwappMfpMIBCompliances": ciscoLwappMfpMIBCompliances,
       "ciscoLwappMfpMIBCompliance": ciscoLwappMfpMIBCompliance,
       "ciscoLwappMfpMIBComplianceRev1": ciscoLwappMfpMIBComplianceRev1,
       "ciscoLwappMfpMIBGroups": ciscoLwappMfpMIBGroups,
       "ciscoLwappMfpConfigGroup": ciscoLwappMfpConfigGroup,
       "ciscoLwappMfpStatusGroup": ciscoLwappMfpStatusGroup,
       "ciscoLwappMfpNotifObjsGroup": ciscoLwappMfpNotifObjsGroup,
       "ciscoLwappMfpNotifsGroup": ciscoLwappMfpNotifsGroup,
       "ciscoLwappMfpConfigSup1Group": ciscoLwappMfpConfigSup1Group,
       "ciscoLwappMfpStatusSup1Group": ciscoLwappMfpStatusSup1Group,
       "ciscoLwappMfpNotifObjsSup1Group": ciscoLwappMfpNotifObjsSup1Group,
       "ciscoLwappMfpNotifsNewGroup": ciscoLwappMfpNotifsNewGroup}
)
