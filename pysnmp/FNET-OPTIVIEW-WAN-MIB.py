# SNMP MIB module (FNET-OPTIVIEW-WAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FNET-OPTIVIEW-WAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:18 2024
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

(fnetOptiViewGeneric,) = mibBuilder.importSymbols(
    "FNET-GLOBAL-REG",
    "fnetOptiViewGeneric")

(ovTrapAgentSysName,
 ovTrapDescription,
 ovTrapOffenderName,
 ovTrapOffenderNetAddr,
 ovTrapOffenderSubId,
 ovTrapSeverity,
 ovTrapStatus) = mibBuilder.importSymbols(
    "FNET-OPTIVIEW-GENERIC-MIB",
    "ovTrapAgentSysName",
    "ovTrapDescription",
    "ovTrapOffenderName",
    "ovTrapOffenderNetAddr",
    "ovTrapOffenderSubId",
    "ovTrapSeverity",
    "ovTrapStatus")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

probSonetLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12000)
)
probSonetLinkDown.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probSonetLinkDown.setStatus(
        ""
    )

probSonetErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12001)
)
probSonetErrors.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probSonetErrors.setStatus(
        ""
    )

probSonetAlarms = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12002)
)
probSonetAlarms.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probSonetAlarms.setStatus(
        ""
    )

probAtmLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12003)
)
probAtmLinkDown.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probAtmLinkDown.setStatus(
        ""
    )

probAtmErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12004)
)
probAtmErrors.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probAtmErrors.setStatus(
        ""
    )

probPDUCRCErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12005)
)
probPDUCRCErrors.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probPDUCRCErrors.setStatus(
        ""
    )

probPosLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12006)
)
probPosLinkDown.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probPosLinkDown.setStatus(
        ""
    )

probPosErrorsDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12007)
)
probPosErrorsDetected.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probPosErrorsDetected.setStatus(
        ""
    )

probLinkUtilization = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12008)
)
probLinkUtilization.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probLinkUtilization.setStatus(
        ""
    )

probDNSServerNoResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12009)
)
probDNSServerNoResp.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probDNSServerNoResp.setStatus(
        ""
    )

probDNSServerNowUsing = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12010)
)
probDNSServerNowUsing.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probDNSServerNowUsing.setStatus(
        ""
    )

probLostDHCPLease = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12011)
)
probLostDHCPLease.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probLostDHCPLease.setStatus(
        ""
    )

probDefaultRouterNoResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12012)
)
probDefaultRouterNoResp.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probDefaultRouterNoResp.setStatus(
        ""
    )

probDiscoveryFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12013)
)
probDiscoveryFull.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probDiscoveryFull.setStatus(
        ""
    )

probClearCounts = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12014)
)
probClearCounts.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probClearCounts.setStatus(
        ""
    )

probDS1LinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12015)
)
probDS1LinkDown.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probDS1LinkDown.setStatus(
        ""
    )

probDS1Errors = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12016)
)
probDS1Errors.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probDS1Errors.setStatus(
        ""
    )

probDS1Alarms = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12017)
)
probDS1Alarms.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probDS1Alarms.setStatus(
        ""
    )

probDS3LinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12018)
)
probDS3LinkDown.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probDS3LinkDown.setStatus(
        ""
    )

probDS3Errors = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12019)
)
probDS3Errors.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probDS3Errors.setStatus(
        ""
    )

probDS3Alarms = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12020)
)
probDS3Alarms.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probDS3Alarms.setStatus(
        ""
    )

probFrLmiLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12021)
)
probFrLmiLinkDown.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probFrLmiLinkDown.setStatus(
        ""
    )

probFrLmiErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12022)
)
probFrLmiErrors.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probFrLmiErrors.setStatus(
        ""
    )

probFrErrorsDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12023)
)
probFrErrorsDetected.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probFrErrorsDetected.setStatus(
        ""
    )

probVcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12024)
)
probVcDown.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probVcDown.setStatus(
        ""
    )

probInvalidDlci = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12025)
)
probInvalidDlci.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probInvalidDlci.setStatus(
        ""
    )

probFrDEUnderCIRUtilization = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12026)
)
probFrDEUnderCIRUtilization.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probFrDEUnderCIRUtilization.setStatus(
        ""
    )

probHdlcLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12027)
)
probHdlcLinkDown.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probHdlcLinkDown.setStatus(
        ""
    )

probHdlcErrorsDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12028)
)
probHdlcErrorsDetected.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probHdlcErrorsDetected.setStatus(
        ""
    )

probFrDteDceReversed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12029)
)
probFrDteDceReversed.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probFrDteDceReversed.setStatus(
        ""
    )

probKeyDevPingLatency = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 12030)
)
probKeyDevPingLatency.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
)
if mibBuilder.loadTexts:
    probKeyDevPingLatency.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FNET-OPTIVIEW-WAN-MIB",
    **{"probSonetLinkDown": probSonetLinkDown,
       "probSonetErrors": probSonetErrors,
       "probSonetAlarms": probSonetAlarms,
       "probAtmLinkDown": probAtmLinkDown,
       "probAtmErrors": probAtmErrors,
       "probPDUCRCErrors": probPDUCRCErrors,
       "probPosLinkDown": probPosLinkDown,
       "probPosErrorsDetected": probPosErrorsDetected,
       "probLinkUtilization": probLinkUtilization,
       "probDNSServerNoResp": probDNSServerNoResp,
       "probDNSServerNowUsing": probDNSServerNowUsing,
       "probLostDHCPLease": probLostDHCPLease,
       "probDefaultRouterNoResp": probDefaultRouterNoResp,
       "probDiscoveryFull": probDiscoveryFull,
       "probClearCounts": probClearCounts,
       "probDS1LinkDown": probDS1LinkDown,
       "probDS1Errors": probDS1Errors,
       "probDS1Alarms": probDS1Alarms,
       "probDS3LinkDown": probDS3LinkDown,
       "probDS3Errors": probDS3Errors,
       "probDS3Alarms": probDS3Alarms,
       "probFrLmiLinkDown": probFrLmiLinkDown,
       "probFrLmiErrors": probFrLmiErrors,
       "probFrErrorsDetected": probFrErrorsDetected,
       "probVcDown": probVcDown,
       "probInvalidDlci": probInvalidDlci,
       "probFrDEUnderCIRUtilization": probFrDEUnderCIRUtilization,
       "probHdlcLinkDown": probHdlcLinkDown,
       "probHdlcErrorsDetected": probHdlcErrorsDetected,
       "probFrDteDceReversed": probFrDteDceReversed,
       "probKeyDevPingLatency": probKeyDevPingLatency}
)
