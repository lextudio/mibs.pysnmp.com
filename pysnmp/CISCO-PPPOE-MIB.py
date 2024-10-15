# SNMP MIB module (CISCO-PPPOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PPPOE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:03 2024
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

(atmVclEntry,
 atmVclVci,
 atmVclVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclEntry",
    "atmVclVci",
    "atmVclVpi")

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(Percent,) = mibBuilder.importSymbols(
    "CISCO-QOS-PIB-MIB",
    "Percent")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(VlanId,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoPppoeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 194)
)
ciscoPppoeMIB.setRevisions(
        ("2011-04-25 00:00",
         "2005-12-21 00:00",
         "2001-02-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoPppoeMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPppoeMIBObjects = _CiscoPppoeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1)
)
_CPppoeSystemSessionInfo_ObjectIdentity = ObjectIdentity
cPppoeSystemSessionInfo = _CPppoeSystemSessionInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 1)
)
_CPppoeSystemCurrSessions_Type = Gauge32
_CPppoeSystemCurrSessions_Object = MibScalar
cPppoeSystemCurrSessions = _CPppoeSystemCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 1, 1),
    _CPppoeSystemCurrSessions_Type()
)
cPppoeSystemCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPppoeSystemCurrSessions.setStatus("current")
if mibBuilder.loadTexts:
    cPppoeSystemCurrSessions.setUnits("sessions")
_CPppoeSystemHighWaterSessions_Type = Gauge32
_CPppoeSystemHighWaterSessions_Object = MibScalar
cPppoeSystemHighWaterSessions = _CPppoeSystemHighWaterSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 1, 2),
    _CPppoeSystemHighWaterSessions_Type()
)
cPppoeSystemHighWaterSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPppoeSystemHighWaterSessions.setStatus("current")
if mibBuilder.loadTexts:
    cPppoeSystemHighWaterSessions.setUnits("sessions")
_CPppoeSystemMaxAllowedSessions_Type = Unsigned32
_CPppoeSystemMaxAllowedSessions_Object = MibScalar
cPppoeSystemMaxAllowedSessions = _CPppoeSystemMaxAllowedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 1, 3),
    _CPppoeSystemMaxAllowedSessions_Type()
)
cPppoeSystemMaxAllowedSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPppoeSystemMaxAllowedSessions.setStatus("current")
if mibBuilder.loadTexts:
    cPppoeSystemMaxAllowedSessions.setUnits("sessions")
_CPppoeSystemThresholdSessions_Type = Unsigned32
_CPppoeSystemThresholdSessions_Object = MibScalar
cPppoeSystemThresholdSessions = _CPppoeSystemThresholdSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 1, 4),
    _CPppoeSystemThresholdSessions_Type()
)
cPppoeSystemThresholdSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPppoeSystemThresholdSessions.setStatus("current")
if mibBuilder.loadTexts:
    cPppoeSystemThresholdSessions.setUnits("sessions")
_CPppoeSystemExceededSessionErrors_Type = Counter32
_CPppoeSystemExceededSessionErrors_Object = MibScalar
cPppoeSystemExceededSessionErrors = _CPppoeSystemExceededSessionErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 1, 5),
    _CPppoeSystemExceededSessionErrors_Type()
)
cPppoeSystemExceededSessionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPppoeSystemExceededSessionErrors.setStatus("current")
_CPppoeSystemPerMacSessionlimit_Type = Unsigned32
_CPppoeSystemPerMacSessionlimit_Object = MibScalar
cPppoeSystemPerMacSessionlimit = _CPppoeSystemPerMacSessionlimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 1, 6),
    _CPppoeSystemPerMacSessionlimit_Type()
)
cPppoeSystemPerMacSessionlimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPppoeSystemPerMacSessionlimit.setStatus("current")
_CPppoeSystemPerMacIWFSessionlimit_Type = Unsigned32
_CPppoeSystemPerMacIWFSessionlimit_Object = MibScalar
cPppoeSystemPerMacIWFSessionlimit = _CPppoeSystemPerMacIWFSessionlimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 1, 7),
    _CPppoeSystemPerMacIWFSessionlimit_Type()
)
cPppoeSystemPerMacIWFSessionlimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPppoeSystemPerMacIWFSessionlimit.setStatus("current")
_CPppoeSystemPerMacThrottleRatelimit_Type = Unsigned32
_CPppoeSystemPerMacThrottleRatelimit_Object = MibScalar
cPppoeSystemPerMacThrottleRatelimit = _CPppoeSystemPerMacThrottleRatelimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 1, 8),
    _CPppoeSystemPerMacThrottleRatelimit_Type()
)
cPppoeSystemPerMacThrottleRatelimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPppoeSystemPerMacThrottleRatelimit.setStatus("current")
_CPppoeSystemPerVLANlimit_Type = Unsigned32
_CPppoeSystemPerVLANlimit_Object = MibScalar
cPppoeSystemPerVLANlimit = _CPppoeSystemPerVLANlimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 1, 9),
    _CPppoeSystemPerVLANlimit_Type()
)
cPppoeSystemPerVLANlimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPppoeSystemPerVLANlimit.setStatus("current")
_CPppoeSystemPerVLANthrottleRatelimit_Type = Unsigned32
_CPppoeSystemPerVLANthrottleRatelimit_Object = MibScalar
cPppoeSystemPerVLANthrottleRatelimit = _CPppoeSystemPerVLANthrottleRatelimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 1, 10),
    _CPppoeSystemPerVLANthrottleRatelimit_Type()
)
cPppoeSystemPerVLANthrottleRatelimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPppoeSystemPerVLANthrottleRatelimit.setStatus("current")
_CPppoeSystemPerVClimit_Type = Unsigned32
_CPppoeSystemPerVClimit_Object = MibScalar
cPppoeSystemPerVClimit = _CPppoeSystemPerVClimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 1, 11),
    _CPppoeSystemPerVClimit_Type()
)
cPppoeSystemPerVClimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPppoeSystemPerVClimit.setStatus("current")
_CPppoeSystemPerVCThrottleRatelimit_Type = Unsigned32
_CPppoeSystemPerVCThrottleRatelimit_Object = MibScalar
cPppoeSystemPerVCThrottleRatelimit = _CPppoeSystemPerVCThrottleRatelimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 1, 12),
    _CPppoeSystemPerVCThrottleRatelimit_Type()
)
cPppoeSystemPerVCThrottleRatelimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPppoeSystemPerVCThrottleRatelimit.setStatus("current")
_CPppoeSystemSessionLossThreshold_Type = Unsigned32
_CPppoeSystemSessionLossThreshold_Object = MibScalar
cPppoeSystemSessionLossThreshold = _CPppoeSystemSessionLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 1, 13),
    _CPppoeSystemSessionLossThreshold_Type()
)
cPppoeSystemSessionLossThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPppoeSystemSessionLossThreshold.setStatus("current")
_CPppoeSystemSessionLossPercent_Type = Percent
_CPppoeSystemSessionLossPercent_Object = MibScalar
cPppoeSystemSessionLossPercent = _CPppoeSystemSessionLossPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 1, 14),
    _CPppoeSystemSessionLossPercent_Type()
)
cPppoeSystemSessionLossPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPppoeSystemSessionLossPercent.setStatus("current")
_CPppoeVcCfgInfo_ObjectIdentity = ObjectIdentity
cPppoeVcCfgInfo = _CPppoeVcCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 2)
)
_CPppoeVcCfgTable_Object = MibTable
cPppoeVcCfgTable = _CPppoeVcCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cPppoeVcCfgTable.setStatus("current")
_CPppoeVcCfgEntry_Object = MibTableRow
cPppoeVcCfgEntry = _CPppoeVcCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cPppoeVcCfgEntry.setStatus("current")


class _CPppoeVcEnable_Type(TruthValue):
    """Custom type cPppoeVcEnable based on TruthValue"""


_CPppoeVcEnable_Object = MibTableColumn
cPppoeVcEnable = _CPppoeVcEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 2, 1, 1, 1),
    _CPppoeVcEnable_Type()
)
cPppoeVcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPppoeVcEnable.setStatus("current")
_CPppoeVcSessionsInfo_ObjectIdentity = ObjectIdentity
cPppoeVcSessionsInfo = _CPppoeVcSessionsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 3)
)
_CPppoeVcSessionsTable_Object = MibTable
cPppoeVcSessionsTable = _CPppoeVcSessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cPppoeVcSessionsTable.setStatus("current")
_CPppoeVcSessionsEntry_Object = MibTableRow
cPppoeVcSessionsEntry = _CPppoeVcSessionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 3, 1, 1)
)
cPppoeVcSessionsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    cPppoeVcSessionsEntry.setStatus("current")
_CPppoeVcCurrSessions_Type = Gauge32
_CPppoeVcCurrSessions_Object = MibTableColumn
cPppoeVcCurrSessions = _CPppoeVcCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 3, 1, 1, 1),
    _CPppoeVcCurrSessions_Type()
)
cPppoeVcCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPppoeVcCurrSessions.setStatus("current")
if mibBuilder.loadTexts:
    cPppoeVcCurrSessions.setUnits("sessions")
_CPppoeVcHighWaterSessions_Type = Gauge32
_CPppoeVcHighWaterSessions_Object = MibTableColumn
cPppoeVcHighWaterSessions = _CPppoeVcHighWaterSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 3, 1, 1, 2),
    _CPppoeVcHighWaterSessions_Type()
)
cPppoeVcHighWaterSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPppoeVcHighWaterSessions.setStatus("current")
if mibBuilder.loadTexts:
    cPppoeVcHighWaterSessions.setUnits("sessions")
_CPppoeVcMaxAllowedSessions_Type = Unsigned32
_CPppoeVcMaxAllowedSessions_Object = MibTableColumn
cPppoeVcMaxAllowedSessions = _CPppoeVcMaxAllowedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 3, 1, 1, 3),
    _CPppoeVcMaxAllowedSessions_Type()
)
cPppoeVcMaxAllowedSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPppoeVcMaxAllowedSessions.setStatus("current")
if mibBuilder.loadTexts:
    cPppoeVcMaxAllowedSessions.setUnits("sessions")
_CPppoeVcThresholdSessions_Type = Unsigned32
_CPppoeVcThresholdSessions_Object = MibTableColumn
cPppoeVcThresholdSessions = _CPppoeVcThresholdSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 3, 1, 1, 4),
    _CPppoeVcThresholdSessions_Type()
)
cPppoeVcThresholdSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPppoeVcThresholdSessions.setStatus("current")
if mibBuilder.loadTexts:
    cPppoeVcThresholdSessions.setUnits("sessions")
_CPppoeVcExceededSessionErrors_Type = Counter32
_CPppoeVcExceededSessionErrors_Object = MibTableColumn
cPppoeVcExceededSessionErrors = _CPppoeVcExceededSessionErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 3, 1, 1, 5),
    _CPppoeVcExceededSessionErrors_Type()
)
cPppoeVcExceededSessionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPppoeVcExceededSessionErrors.setStatus("current")
if mibBuilder.loadTexts:
    cPppoeVcExceededSessionErrors.setUnits("attempts")
_CPppoeSessionsPerInterfaceInfo_ObjectIdentity = ObjectIdentity
cPppoeSessionsPerInterfaceInfo = _CPppoeSessionsPerInterfaceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 4)
)
_CPppoeSessionsPerInterfaceTable_Object = MibTable
cPppoeSessionsPerInterfaceTable = _CPppoeSessionsPerInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cPppoeSessionsPerInterfaceTable.setStatus("current")
_CPppoeSessionsPerInterfaceEntry_Object = MibTableRow
cPppoeSessionsPerInterfaceEntry = _CPppoeSessionsPerInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 4, 1, 1)
)
cPppoeSessionsPerInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cPppoeSessionsPerInterfaceEntry.setStatus("current")
_CPppoeTotalSessions_Type = Gauge32
_CPppoeTotalSessions_Object = MibTableColumn
cPppoeTotalSessions = _CPppoeTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 4, 1, 1, 1),
    _CPppoeTotalSessions_Type()
)
cPppoeTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPppoeTotalSessions.setStatus("current")
if mibBuilder.loadTexts:
    cPppoeTotalSessions.setUnits("sessions")
_CPppoePtaSessions_Type = Gauge32
_CPppoePtaSessions_Object = MibTableColumn
cPppoePtaSessions = _CPppoePtaSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 4, 1, 1, 2),
    _CPppoePtaSessions_Type()
)
cPppoePtaSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPppoePtaSessions.setStatus("current")
if mibBuilder.loadTexts:
    cPppoePtaSessions.setUnits("sessions")
_CPppoeFwdedSessions_Type = Gauge32
_CPppoeFwdedSessions_Object = MibTableColumn
cPppoeFwdedSessions = _CPppoeFwdedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 4, 1, 1, 3),
    _CPppoeFwdedSessions_Type()
)
cPppoeFwdedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPppoeFwdedSessions.setStatus("current")
if mibBuilder.loadTexts:
    cPppoeFwdedSessions.setUnits("sessions")
_CPppoeTransSessions_Type = Gauge32
_CPppoeTransSessions_Object = MibTableColumn
cPppoeTransSessions = _CPppoeTransSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 4, 1, 1, 4),
    _CPppoeTransSessions_Type()
)
cPppoeTransSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPppoeTransSessions.setStatus("current")
if mibBuilder.loadTexts:
    cPppoeTransSessions.setUnits("sessions")
_CPppoePerInterfaceSessionLossThreshold_Type = Unsigned32
_CPppoePerInterfaceSessionLossThreshold_Object = MibTableColumn
cPppoePerInterfaceSessionLossThreshold = _CPppoePerInterfaceSessionLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 4, 1, 1, 5),
    _CPppoePerInterfaceSessionLossThreshold_Type()
)
cPppoePerInterfaceSessionLossThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPppoePerInterfaceSessionLossThreshold.setStatus("current")
_CPppoePerInterfaceSessionLossPercent_Type = Unsigned32
_CPppoePerInterfaceSessionLossPercent_Object = MibTableColumn
cPppoePerInterfaceSessionLossPercent = _CPppoePerInterfaceSessionLossPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 4, 1, 1, 6),
    _CPppoePerInterfaceSessionLossPercent_Type()
)
cPppoePerInterfaceSessionLossPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPppoePerInterfaceSessionLossPercent.setStatus("current")
_CPppoeSystemSessionNotifyObjects_ObjectIdentity = ObjectIdentity
cPppoeSystemSessionNotifyObjects = _CPppoeSystemSessionNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 5)
)
_CPppoeSystemSessionClientMacAddress_Type = MacAddress
_CPppoeSystemSessionClientMacAddress_Object = MibScalar
cPppoeSystemSessionClientMacAddress = _CPppoeSystemSessionClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 5, 1),
    _CPppoeSystemSessionClientMacAddress_Type()
)
cPppoeSystemSessionClientMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cPppoeSystemSessionClientMacAddress.setStatus("current")
_CPppoeSystemSessionVlanID_Type = VlanId
_CPppoeSystemSessionVlanID_Object = MibScalar
cPppoeSystemSessionVlanID = _CPppoeSystemSessionVlanID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 5, 2),
    _CPppoeSystemSessionVlanID_Type()
)
cPppoeSystemSessionVlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cPppoeSystemSessionVlanID.setStatus("current")
_CPppoeSystemSessionInnerVlanID_Type = VlanIndex
_CPppoeSystemSessionInnerVlanID_Object = MibScalar
cPppoeSystemSessionInnerVlanID = _CPppoeSystemSessionInnerVlanID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 5, 3),
    _CPppoeSystemSessionInnerVlanID_Type()
)
cPppoeSystemSessionInnerVlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cPppoeSystemSessionInnerVlanID.setStatus("current")
_CPppoeSystemSessionVci_Type = AtmVcIdentifier
_CPppoeSystemSessionVci_Object = MibScalar
cPppoeSystemSessionVci = _CPppoeSystemSessionVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 5, 4),
    _CPppoeSystemSessionVci_Type()
)
cPppoeSystemSessionVci.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cPppoeSystemSessionVci.setStatus("current")
_CPppoeSystemSessionVpi_Type = AtmVpIdentifier
_CPppoeSystemSessionVpi_Object = MibScalar
cPppoeSystemSessionVpi = _CPppoeSystemSessionVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 1, 5, 5),
    _CPppoeSystemSessionVpi_Type()
)
cPppoeSystemSessionVpi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cPppoeSystemSessionVpi.setStatus("current")
_CiscoPppoeMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoPppoeMIBNotificationPrefix = _CiscoPppoeMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 2)
)
_CiscoPppoeMIBNotification_ObjectIdentity = ObjectIdentity
ciscoPppoeMIBNotification = _CiscoPppoeMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 2, 0)
)
_CiscoPppoeMIBConformance_ObjectIdentity = ObjectIdentity
ciscoPppoeMIBConformance = _CiscoPppoeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 3)
)
_CiscoPppoeMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPppoeMIBCompliances = _CiscoPppoeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 3, 1)
)
_CiscoPppoeMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPppoeMIBGroups = _CiscoPppoeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 3, 2)
)
atmVclEntry.registerAugmentions(
    ("CISCO-PPPOE-MIB",
     "cPppoeVcCfgEntry")
)
cPppoeVcCfgEntry.setIndexNames(*atmVclEntry.getIndexNames())

# Managed Objects groups

cPppoeSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 3, 2, 1)
)
cPppoeSystemGroup.setObjects(
      *(("CISCO-PPPOE-MIB", "cPppoeSystemCurrSessions"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemHighWaterSessions"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemMaxAllowedSessions"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemThresholdSessions"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemExceededSessionErrors"))
)
if mibBuilder.loadTexts:
    cPppoeSystemGroup.setStatus("current")

cPppoeVcCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 3, 2, 2)
)
cPppoeVcCfgGroup.setObjects(
    ("CISCO-PPPOE-MIB", "cPppoeVcEnable")
)
if mibBuilder.loadTexts:
    cPppoeVcCfgGroup.setStatus("current")

cPppoeVcSessionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 3, 2, 3)
)
cPppoeVcSessionsGroup.setObjects(
      *(("CISCO-PPPOE-MIB", "cPppoeVcCurrSessions"),
        ("CISCO-PPPOE-MIB", "cPppoeVcHighWaterSessions"),
        ("CISCO-PPPOE-MIB", "cPppoeVcMaxAllowedSessions"),
        ("CISCO-PPPOE-MIB", "cPppoeVcThresholdSessions"),
        ("CISCO-PPPOE-MIB", "cPppoeVcExceededSessionErrors"))
)
if mibBuilder.loadTexts:
    cPppoeVcSessionsGroup.setStatus("current")

cPppoePerInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 3, 2, 5)
)
cPppoePerInterfaceGroup.setObjects(
      *(("CISCO-PPPOE-MIB", "cPppoeTotalSessions"),
        ("CISCO-PPPOE-MIB", "cPppoePtaSessions"),
        ("CISCO-PPPOE-MIB", "cPppoeFwdedSessions"),
        ("CISCO-PPPOE-MIB", "cPppoeTransSessions"),
        ("CISCO-PPPOE-MIB", "cPppoePerInterfaceSessionLossThreshold"),
        ("CISCO-PPPOE-MIB", "cPppoePerInterfaceSessionLossPercent"))
)
if mibBuilder.loadTexts:
    cPppoePerInterfaceGroup.setStatus("current")

cPppoeSystemLimitsThresholdsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 3, 2, 6)
)
cPppoeSystemLimitsThresholdsGroup.setObjects(
      *(("CISCO-PPPOE-MIB", "cPppoeSystemPerMacSessionlimit"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemPerMacIWFSessionlimit"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemPerMacThrottleRatelimit"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemPerVLANlimit"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemPerVLANthrottleRatelimit"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemPerVClimit"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemPerVCThrottleRatelimit"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionLossThreshold"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionLossPercent"))
)
if mibBuilder.loadTexts:
    cPppoeSystemLimitsThresholdsGroup.setStatus("current")

cPppoeSystemLimitsThresholdsNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 3, 2, 7)
)
cPppoeSystemLimitsThresholdsNotifObjectsGroup.setObjects(
      *(("CISCO-PPPOE-MIB", "cPppoeSystemSessionClientMacAddress"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionVlanID"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionInnerVlanID"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionVci"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionVpi"))
)
if mibBuilder.loadTexts:
    cPppoeSystemLimitsThresholdsNotifObjectsGroup.setStatus("current")


# Notification objects

cPppoeSystemSessionThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 2, 0, 1)
)
cPppoeSystemSessionThresholdTrap.setObjects(
      *(("CISCO-PPPOE-MIB", "cPppoeSystemCurrSessions"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemMaxAllowedSessions"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemThresholdSessions"))
)
if mibBuilder.loadTexts:
    cPppoeSystemSessionThresholdTrap.setStatus(
        "current"
    )

cPppoeVcSessionThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 2, 0, 2)
)
cPppoeVcSessionThresholdTrap.setObjects(
      *(("CISCO-PPPOE-MIB", "cPppoeVcCurrSessions"),
        ("CISCO-PPPOE-MIB", "cPppoeVcMaxAllowedSessions"),
        ("CISCO-PPPOE-MIB", "cPppoeVcThresholdSessions"))
)
if mibBuilder.loadTexts:
    cPppoeVcSessionThresholdTrap.setStatus(
        "current"
    )

cPppoeSystemSessionPerMACLimitNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 2, 0, 3)
)
cPppoeSystemSessionPerMACLimitNotif.setObjects(
      *(("CISCO-PPPOE-MIB", "cPppoeSystemPerMacSessionlimit"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionClientMacAddress"))
)
if mibBuilder.loadTexts:
    cPppoeSystemSessionPerMACLimitNotif.setStatus(
        "current"
    )

cPppoeSystemSessionPerMACThrottleNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 2, 0, 4)
)
cPppoeSystemSessionPerMACThrottleNotif.setObjects(
      *(("CISCO-PPPOE-MIB", "cPppoeSystemPerMacThrottleRatelimit"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionClientMacAddress"))
)
if mibBuilder.loadTexts:
    cPppoeSystemSessionPerMACThrottleNotif.setStatus(
        "current"
    )

cPppoeSystemSessionPerVLANLimitNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 2, 0, 5)
)
cPppoeSystemSessionPerVLANLimitNotif.setObjects(
      *(("CISCO-PPPOE-MIB", "cPppoeSystemPerVLANlimit"),
        ("IF-MIB", "ifDescr"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionVlanID"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionInnerVlanID"))
)
if mibBuilder.loadTexts:
    cPppoeSystemSessionPerVLANLimitNotif.setStatus(
        "current"
    )

cPppoeSystemSessionPerVLANThrottleNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 2, 0, 6)
)
cPppoeSystemSessionPerVLANThrottleNotif.setObjects(
      *(("CISCO-PPPOE-MIB", "cPppoeSystemPerVLANthrottleRatelimit"),
        ("IF-MIB", "ifDescr"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionVlanID"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionInnerVlanID"))
)
if mibBuilder.loadTexts:
    cPppoeSystemSessionPerVLANThrottleNotif.setStatus(
        "current"
    )

cPppoeSystemSessionPerVCLimitNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 2, 0, 7)
)
cPppoeSystemSessionPerVCLimitNotif.setObjects(
      *(("CISCO-PPPOE-MIB", "cPppoeSystemPerVClimit"),
        ("IF-MIB", "ifDescr"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionVci"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionVpi"))
)
if mibBuilder.loadTexts:
    cPppoeSystemSessionPerVCLimitNotif.setStatus(
        "current"
    )

cPppoeSystemSessionPerVCThrottleNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 2, 0, 8)
)
cPppoeSystemSessionPerVCThrottleNotif.setObjects(
      *(("CISCO-PPPOE-MIB", "cPppoeSystemPerVCThrottleRatelimit"),
        ("IF-MIB", "ifDescr"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionVci"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionVpi"))
)
if mibBuilder.loadTexts:
    cPppoeSystemSessionPerVCThrottleNotif.setStatus(
        "current"
    )

cPppoeSystemSessionLossThresholdNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 2, 0, 9)
)
cPppoeSystemSessionLossThresholdNotif.setObjects(
    ("CISCO-PPPOE-MIB", "cPppoeSystemSessionLossThreshold")
)
if mibBuilder.loadTexts:
    cPppoeSystemSessionLossThresholdNotif.setStatus(
        "current"
    )

cPppoePerInterfaceSessionLossThresholdNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 2, 0, 10)
)
cPppoePerInterfaceSessionLossThresholdNotif.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("CISCO-PPPOE-MIB", "cPppoePerInterfaceSessionLossThreshold"))
)
if mibBuilder.loadTexts:
    cPppoePerInterfaceSessionLossThresholdNotif.setStatus(
        "current"
    )

cPppoeSystemSessionLossPercentNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 2, 0, 11)
)
cPppoeSystemSessionLossPercentNotif.setObjects(
    ("CISCO-PPPOE-MIB", "cPppoeSystemSessionLossPercent")
)
if mibBuilder.loadTexts:
    cPppoeSystemSessionLossPercentNotif.setStatus(
        "current"
    )

cPppoePerInterfaceSessionLossPercentNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 2, 0, 12)
)
cPppoePerInterfaceSessionLossPercentNotif.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("CISCO-PPPOE-MIB", "cPppoePerInterfaceSessionLossPercent"))
)
if mibBuilder.loadTexts:
    cPppoePerInterfaceSessionLossPercentNotif.setStatus(
        "current"
    )


# Notifications groups

cPppoeNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 3, 2, 4)
)
cPppoeNotificationsGroup.setObjects(
      *(("CISCO-PPPOE-MIB", "cPppoeSystemSessionThresholdTrap"),
        ("CISCO-PPPOE-MIB", "cPppoeVcSessionThresholdTrap"))
)
if mibBuilder.loadTexts:
    cPppoeNotificationsGroup.setStatus(
        "current"
    )

cPppoeSystemLimitsThresholdsNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 3, 2, 8)
)
cPppoeSystemLimitsThresholdsNotifGroup.setObjects(
      *(("CISCO-PPPOE-MIB", "cPppoeSystemSessionPerMACLimitNotif"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionPerMACThrottleNotif"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionPerVLANLimitNotif"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionPerVLANThrottleNotif"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionPerVCLimitNotif"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionPerVCThrottleNotif"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionLossThresholdNotif"),
        ("CISCO-PPPOE-MIB", "cPppoePerInterfaceSessionLossThresholdNotif"),
        ("CISCO-PPPOE-MIB", "cPppoeSystemSessionLossPercentNotif"),
        ("CISCO-PPPOE-MIB", "cPppoePerInterfaceSessionLossPercentNotif"))
)
if mibBuilder.loadTexts:
    cPppoeSystemLimitsThresholdsNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoPppoeMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPppoeMIBBasicCompliance.setStatus(
        "deprecated"
    )

ciscoPppoeMIBBasicComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 194, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoPppoeMIBBasicComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PPPOE-MIB",
    **{"ciscoPppoeMIB": ciscoPppoeMIB,
       "ciscoPppoeMIBObjects": ciscoPppoeMIBObjects,
       "cPppoeSystemSessionInfo": cPppoeSystemSessionInfo,
       "cPppoeSystemCurrSessions": cPppoeSystemCurrSessions,
       "cPppoeSystemHighWaterSessions": cPppoeSystemHighWaterSessions,
       "cPppoeSystemMaxAllowedSessions": cPppoeSystemMaxAllowedSessions,
       "cPppoeSystemThresholdSessions": cPppoeSystemThresholdSessions,
       "cPppoeSystemExceededSessionErrors": cPppoeSystemExceededSessionErrors,
       "cPppoeSystemPerMacSessionlimit": cPppoeSystemPerMacSessionlimit,
       "cPppoeSystemPerMacIWFSessionlimit": cPppoeSystemPerMacIWFSessionlimit,
       "cPppoeSystemPerMacThrottleRatelimit": cPppoeSystemPerMacThrottleRatelimit,
       "cPppoeSystemPerVLANlimit": cPppoeSystemPerVLANlimit,
       "cPppoeSystemPerVLANthrottleRatelimit": cPppoeSystemPerVLANthrottleRatelimit,
       "cPppoeSystemPerVClimit": cPppoeSystemPerVClimit,
       "cPppoeSystemPerVCThrottleRatelimit": cPppoeSystemPerVCThrottleRatelimit,
       "cPppoeSystemSessionLossThreshold": cPppoeSystemSessionLossThreshold,
       "cPppoeSystemSessionLossPercent": cPppoeSystemSessionLossPercent,
       "cPppoeVcCfgInfo": cPppoeVcCfgInfo,
       "cPppoeVcCfgTable": cPppoeVcCfgTable,
       "cPppoeVcCfgEntry": cPppoeVcCfgEntry,
       "cPppoeVcEnable": cPppoeVcEnable,
       "cPppoeVcSessionsInfo": cPppoeVcSessionsInfo,
       "cPppoeVcSessionsTable": cPppoeVcSessionsTable,
       "cPppoeVcSessionsEntry": cPppoeVcSessionsEntry,
       "cPppoeVcCurrSessions": cPppoeVcCurrSessions,
       "cPppoeVcHighWaterSessions": cPppoeVcHighWaterSessions,
       "cPppoeVcMaxAllowedSessions": cPppoeVcMaxAllowedSessions,
       "cPppoeVcThresholdSessions": cPppoeVcThresholdSessions,
       "cPppoeVcExceededSessionErrors": cPppoeVcExceededSessionErrors,
       "cPppoeSessionsPerInterfaceInfo": cPppoeSessionsPerInterfaceInfo,
       "cPppoeSessionsPerInterfaceTable": cPppoeSessionsPerInterfaceTable,
       "cPppoeSessionsPerInterfaceEntry": cPppoeSessionsPerInterfaceEntry,
       "cPppoeTotalSessions": cPppoeTotalSessions,
       "cPppoePtaSessions": cPppoePtaSessions,
       "cPppoeFwdedSessions": cPppoeFwdedSessions,
       "cPppoeTransSessions": cPppoeTransSessions,
       "cPppoePerInterfaceSessionLossThreshold": cPppoePerInterfaceSessionLossThreshold,
       "cPppoePerInterfaceSessionLossPercent": cPppoePerInterfaceSessionLossPercent,
       "cPppoeSystemSessionNotifyObjects": cPppoeSystemSessionNotifyObjects,
       "cPppoeSystemSessionClientMacAddress": cPppoeSystemSessionClientMacAddress,
       "cPppoeSystemSessionVlanID": cPppoeSystemSessionVlanID,
       "cPppoeSystemSessionInnerVlanID": cPppoeSystemSessionInnerVlanID,
       "cPppoeSystemSessionVci": cPppoeSystemSessionVci,
       "cPppoeSystemSessionVpi": cPppoeSystemSessionVpi,
       "ciscoPppoeMIBNotificationPrefix": ciscoPppoeMIBNotificationPrefix,
       "ciscoPppoeMIBNotification": ciscoPppoeMIBNotification,
       "cPppoeSystemSessionThresholdTrap": cPppoeSystemSessionThresholdTrap,
       "cPppoeVcSessionThresholdTrap": cPppoeVcSessionThresholdTrap,
       "cPppoeSystemSessionPerMACLimitNotif": cPppoeSystemSessionPerMACLimitNotif,
       "cPppoeSystemSessionPerMACThrottleNotif": cPppoeSystemSessionPerMACThrottleNotif,
       "cPppoeSystemSessionPerVLANLimitNotif": cPppoeSystemSessionPerVLANLimitNotif,
       "cPppoeSystemSessionPerVLANThrottleNotif": cPppoeSystemSessionPerVLANThrottleNotif,
       "cPppoeSystemSessionPerVCLimitNotif": cPppoeSystemSessionPerVCLimitNotif,
       "cPppoeSystemSessionPerVCThrottleNotif": cPppoeSystemSessionPerVCThrottleNotif,
       "cPppoeSystemSessionLossThresholdNotif": cPppoeSystemSessionLossThresholdNotif,
       "cPppoePerInterfaceSessionLossThresholdNotif": cPppoePerInterfaceSessionLossThresholdNotif,
       "cPppoeSystemSessionLossPercentNotif": cPppoeSystemSessionLossPercentNotif,
       "cPppoePerInterfaceSessionLossPercentNotif": cPppoePerInterfaceSessionLossPercentNotif,
       "ciscoPppoeMIBConformance": ciscoPppoeMIBConformance,
       "ciscoPppoeMIBCompliances": ciscoPppoeMIBCompliances,
       "ciscoPppoeMIBBasicCompliance": ciscoPppoeMIBBasicCompliance,
       "ciscoPppoeMIBBasicComplianceRev1": ciscoPppoeMIBBasicComplianceRev1,
       "ciscoPppoeMIBGroups": ciscoPppoeMIBGroups,
       "cPppoeSystemGroup": cPppoeSystemGroup,
       "cPppoeVcCfgGroup": cPppoeVcCfgGroup,
       "cPppoeVcSessionsGroup": cPppoeVcSessionsGroup,
       "cPppoeNotificationsGroup": cPppoeNotificationsGroup,
       "cPppoePerInterfaceGroup": cPppoePerInterfaceGroup,
       "cPppoeSystemLimitsThresholdsGroup": cPppoeSystemLimitsThresholdsGroup,
       "cPppoeSystemLimitsThresholdsNotifObjectsGroup": cPppoeSystemLimitsThresholdsNotifObjectsGroup,
       "cPppoeSystemLimitsThresholdsNotifGroup": cPppoeSystemLimitsThresholdsNotifGroup}
)
