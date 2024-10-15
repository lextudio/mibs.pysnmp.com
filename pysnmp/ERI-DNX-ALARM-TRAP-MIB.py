# SNMP MIB module (ERI-DNX-ALARM-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ERI-DNX-ALARM-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:21 2024
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

(dnxTrapEnterprise,
 trapResourceAddress,
 trapResourceKey,
 trapResourceType,
 trapSequence,
 trapSeverity,
 trapState,
 trapTime,
 trapType) = mibBuilder.importSymbols(
    "ERI-DNX-SMC-MIB",
    "dnxTrapEnterprise",
    "trapResourceAddress",
    "trapResourceKey",
    "trapResourceType",
    "trapSequence",
    "trapSeverity",
    "trapState",
    "trapTime",
    "trapType")

(eriMibs,) = mibBuilder.importSymbols(
    "ERI-ROOT-SMI",
    "eriMibs")

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


# MODULE-IDENTITY

eriDNXAlarmTrapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 644, 3, 12)
)
eriDNXAlarmTrapMIB.setRevisions(
        ("2003-05-06 00:00",
         "2003-01-10 00:00",
         "2002-08-20 00:00",
         "2002-07-03 00:00",
         "2002-06-05 00:00",
         "2002-04-08 00:00",
         "2002-03-11 00:00",
         "2001-12-05 00:00",
         "2001-09-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

evntDevColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1)
)
evntDevColdStart.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntDevColdStart.setStatus(
        "current"
    )

evntDevWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2)
)
evntDevWarmStart.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntDevWarmStart.setStatus(
        "current"
    )

setSlotMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 101)
)
setSlotMismatch.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSlotMismatch.setStatus(
        "current"
    )

setSlotMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 102)
)
setSlotMissing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSlotMissing.setStatus(
        "current"
    )

clearSlotMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 141)
)
clearSlotMismatch.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSlotMismatch.setStatus(
        "current"
    )

clearSlotMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 142)
)
clearSlotMissing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSlotMissing.setStatus(
        "current"
    )

evntDevOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 201)
)
evntDevOnline.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntDevOnline.setStatus(
        "current"
    )

evntDevStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 202)
)
evntDevStandby.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntDevStandby.setStatus(
        "current"
    )

setDevFrameSyncNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 203)
)
setDevFrameSyncNotPresent.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setDevFrameSyncNotPresent.setStatus(
        "current"
    )

setDevSystemClockNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 204)
)
setDevSystemClockNotPresent.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setDevSystemClockNotPresent.setStatus(
        "current"
    )

setDevDataBaseNotInsync = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 206)
)
setDevDataBaseNotInsync.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setDevDataBaseNotInsync.setStatus(
        "current"
    )

setDevFreeRunError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 207)
)
setDevFreeRunError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setDevFreeRunError.setStatus(
        "current"
    )

setDevOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 208)
)
setDevOffline.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setDevOffline.setStatus(
        "current"
    )

setDevDefective = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 209)
)
setDevDefective.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setDevDefective.setStatus(
        "current"
    )

setDevBusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 210)
)
setDevBusError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setDevBusError.setStatus(
        "current"
    )

setDevStratum3ClkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 216)
)
setDevStratum3ClkFailure.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setDevStratum3ClkFailure.setStatus(
        "current"
    )

setDevCircuitCardMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 219)
)
setDevCircuitCardMissing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setDevCircuitCardMissing.setStatus(
        "current"
    )

setDevConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 225)
)
setDevConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setDevConfigError.setStatus(
        "current"
    )

setDevNoRearCard = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 228)
)
setDevNoRearCard.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setDevNoRearCard.setStatus(
        "current"
    )

evntDevOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 231)
)
evntDevOutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntDevOutOfService.setStatus(
        "current"
    )

evntDevNotOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 241)
)
evntDevNotOnline.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntDevNotOnline.setStatus(
        "current"
    )

evntDevNotStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 242)
)
evntDevNotStandby.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntDevNotStandby.setStatus(
        "current"
    )

clearDevFrameSyncNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 243)
)
clearDevFrameSyncNotPresent.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearDevFrameSyncNotPresent.setStatus(
        "current"
    )

clearDevSystemClockNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 244)
)
clearDevSystemClockNotPresent.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearDevSystemClockNotPresent.setStatus(
        "current"
    )

clearDevDataBaseNotInsync = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 246)
)
clearDevDataBaseNotInsync.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearDevDataBaseNotInsync.setStatus(
        "current"
    )

clearDevFreeRunError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 247)
)
clearDevFreeRunError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearDevFreeRunError.setStatus(
        "current"
    )

clearDevOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 248)
)
clearDevOffline.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearDevOffline.setStatus(
        "current"
    )

clearDevDefective = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 249)
)
clearDevDefective.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearDevDefective.setStatus(
        "current"
    )

clearDevBusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 250)
)
clearDevBusError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearDevBusError.setStatus(
        "current"
    )

clearDevStratum3ClkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 256)
)
clearDevStratum3ClkFailure.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearDevStratum3ClkFailure.setStatus(
        "current"
    )

clearDevCircuitCardMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 259)
)
clearDevCircuitCardMissing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearDevCircuitCardMissing.setStatus(
        "current"
    )

clearDevConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 265)
)
clearDevConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearDevConfigError.setStatus(
        "current"
    )

clearDevNoRearCard = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 268)
)
clearDevNoRearCard.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearDevNoRearCard.setStatus(
        "current"
    )

evntDevInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 271)
)
evntDevInService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntDevInService.setStatus(
        "current"
    )

setT1E1RcvFarEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 301)
)
setT1E1RcvFarEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT1E1RcvFarEndLOF.setStatus(
        "current"
    )

setT1E1NearEndSendLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 302)
)
setT1E1NearEndSendLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT1E1NearEndSendLOF.setStatus(
        "current"
    )

evntT1E1RcvingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 303)
)
evntT1E1RcvingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT1E1RcvingAIS.setStatus(
        "current"
    )

setT1E1NearEndSendingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 304)
)
setT1E1NearEndSendingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT1E1NearEndSendingAIS.setStatus(
        "current"
    )

setT1E1NearEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 305)
)
setT1E1NearEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT1E1NearEndLOF.setStatus(
        "current"
    )

setT1E1NearEndLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 306)
)
setT1E1NearEndLossOfSignal.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT1E1NearEndLossOfSignal.setStatus(
        "current"
    )

evntT1E1NearEndLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 307)
)
evntT1E1NearEndLooped.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT1E1NearEndLooped.setStatus(
        "current"
    )

setT1E1Ts16AIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 308)
)
setT1E1Ts16AIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT1E1Ts16AIS.setStatus(
        "current"
    )

setT1E1FarEndSendingTs16LOMF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 309)
)
setT1E1FarEndSendingTs16LOMF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT1E1FarEndSendingTs16LOMF.setStatus(
        "current"
    )

setT1E1NearEndSendingTs16LOMF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 310)
)
setT1E1NearEndSendingTs16LOMF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT1E1NearEndSendingTs16LOMF.setStatus(
        "current"
    )

setT1E1OtherLineStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 312)
)
setT1E1OtherLineStatus.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT1E1OtherLineStatus.setStatus(
        "current"
    )

setT1E1NearEndUnavailableSig = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 313)
)
setT1E1NearEndUnavailableSig.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT1E1NearEndUnavailableSig.setStatus(
        "current"
    )

evntT1E1CarrierEquipOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 314)
)
evntT1E1CarrierEquipOutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT1E1CarrierEquipOutOfService.setStatus(
        "current"
    )

evntE1NationalSa4TxRxSame = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 316)
)
evntE1NationalSa4TxRxSame.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntE1NationalSa4TxRxSame.setStatus(
        "current"
    )

setT1E1NearEndTxSlip = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 321)
)
setT1E1NearEndTxSlip.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT1E1NearEndTxSlip.setStatus(
        "current"
    )

setT1E1NearEndRxSlip = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 322)
)
setT1E1NearEndRxSlip.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT1E1NearEndRxSlip.setStatus(
        "current"
    )

setT1E1NearEndSeverErroredFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 323)
)
setT1E1NearEndSeverErroredFrame.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT1E1NearEndSeverErroredFrame.setStatus(
        "current"
    )

setT1E1ChangeFrameAlignment = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 324)
)
setT1E1ChangeFrameAlignment.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT1E1ChangeFrameAlignment.setStatus(
        "current"
    )

setT1E1ConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 325)
)
setT1E1ConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT1E1ConfigError.setStatus(
        "current"
    )

evntT1E1InTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 330)
)
evntT1E1InTest.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT1E1InTest.setStatus(
        "current"
    )

evntT1E1OutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 331)
)
evntT1E1OutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT1E1OutOfService.setStatus(
        "current"
    )

clearT1E1RcvFarEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 341)
)
clearT1E1RcvFarEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT1E1RcvFarEndLOF.setStatus(
        "current"
    )

clearT1E1NearEndSendLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 342)
)
clearT1E1NearEndSendLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT1E1NearEndSendLOF.setStatus(
        "current"
    )

evntT1E1StoppedRcvingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 343)
)
evntT1E1StoppedRcvingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT1E1StoppedRcvingAIS.setStatus(
        "current"
    )

clearT1E1NearEndSendingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 344)
)
clearT1E1NearEndSendingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT1E1NearEndSendingAIS.setStatus(
        "current"
    )

clearT1E1NearEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 345)
)
clearT1E1NearEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT1E1NearEndLOF.setStatus(
        "current"
    )

clearT1E1NearEndLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 346)
)
clearT1E1NearEndLossOfSignal.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT1E1NearEndLossOfSignal.setStatus(
        "current"
    )

evntT1E1NearEndLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 347)
)
evntT1E1NearEndLoopOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT1E1NearEndLoopOff.setStatus(
        "current"
    )

clearT1E1Ts16AIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 348)
)
clearT1E1Ts16AIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT1E1Ts16AIS.setStatus(
        "current"
    )

clearT1E1FarEndSendingTs16LOMF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 349)
)
clearT1E1FarEndSendingTs16LOMF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT1E1FarEndSendingTs16LOMF.setStatus(
        "current"
    )

clearT1E1NearEndSendingTs16LOMF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 350)
)
clearT1E1NearEndSendingTs16LOMF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT1E1NearEndSendingTs16LOMF.setStatus(
        "current"
    )

clearT1E1OtherLineStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 352)
)
clearT1E1OtherLineStatus.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT1E1OtherLineStatus.setStatus(
        "current"
    )

clearT1E1NearEndUnavailableSig = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 353)
)
clearT1E1NearEndUnavailableSig.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT1E1NearEndUnavailableSig.setStatus(
        "current"
    )

evntT1E1CarrierEquipInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 354)
)
evntT1E1CarrierEquipInService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT1E1CarrierEquipInService.setStatus(
        "current"
    )

evntE1NationalSa4TxRxDiff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 356)
)
evntE1NationalSa4TxRxDiff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntE1NationalSa4TxRxDiff.setStatus(
        "current"
    )

clearT1E1NearEndTxSlip = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 361)
)
clearT1E1NearEndTxSlip.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT1E1NearEndTxSlip.setStatus(
        "current"
    )

clearT1E1NearEndRxSlip = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 362)
)
clearT1E1NearEndRxSlip.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT1E1NearEndRxSlip.setStatus(
        "current"
    )

clearT1E1NearEndSeverErroredFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 363)
)
clearT1E1NearEndSeverErroredFrame.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT1E1NearEndSeverErroredFrame.setStatus(
        "current"
    )

clearT1E1ChangeFrameAlignment = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 364)
)
clearT1E1ChangeFrameAlignment.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT1E1ChangeFrameAlignment.setStatus(
        "current"
    )

clearT1E1ConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 365)
)
clearT1E1ConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT1E1ConfigError.setStatus(
        "current"
    )

evntT1E1TestOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 370)
)
evntT1E1TestOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT1E1TestOff.setStatus(
        "current"
    )

evntT1E1InService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 371)
)
evntT1E1InService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT1E1InService.setStatus(
        "current"
    )

setHsRcvFIFOError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 401)
)
setHsRcvFIFOError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHsRcvFIFOError.setStatus(
        "current"
    )

setHsXmtFIFOError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 402)
)
setHsXmtFIFOError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHsXmtFIFOError.setStatus(
        "current"
    )

setHsClockEdgeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 403)
)
setHsClockEdgeError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHsClockEdgeError.setStatus(
        "current"
    )

setHsCarrierFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 404)
)
setHsCarrierFailure.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHsCarrierFailure.setStatus(
        "current"
    )

evntHsNearEndLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 407)
)
evntHsNearEndLooped.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHsNearEndLooped.setStatus(
        "current"
    )

evntHsNoBtsAssigned = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 424)
)
evntHsNoBtsAssigned.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHsNoBtsAssigned.setStatus(
        "current"
    )

setHsConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 425)
)
setHsConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHsConfigError.setStatus(
        "current"
    )

evntHsInTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 430)
)
evntHsInTest.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHsInTest.setStatus(
        "current"
    )

evntHsOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 431)
)
evntHsOutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHsOutOfService.setStatus(
        "current"
    )

clearHsRcvFIFOError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 441)
)
clearHsRcvFIFOError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHsRcvFIFOError.setStatus(
        "current"
    )

clearHsXmtFIFOError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 442)
)
clearHsXmtFIFOError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHsXmtFIFOError.setStatus(
        "current"
    )

clearHsClockEdgeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 443)
)
clearHsClockEdgeError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHsClockEdgeError.setStatus(
        "current"
    )

clearHsCarrierFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 444)
)
clearHsCarrierFailure.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHsCarrierFailure.setStatus(
        "current"
    )

evntHsNearEndLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 447)
)
evntHsNearEndLoopOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHsNearEndLoopOff.setStatus(
        "current"
    )

evntHsBtsAssigned = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 464)
)
evntHsBtsAssigned.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHsBtsAssigned.setStatus(
        "current"
    )

clearHsConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 465)
)
clearHsConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHsConfigError.setStatus(
        "current"
    )

evntHsTestOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 470)
)
evntHsTestOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHsTestOff.setStatus(
        "current"
    )

evntHsInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 471)
)
evntHsInService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHsInService.setStatus(
        "current"
    )

setT3RcvFarEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 501)
)
setT3RcvFarEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3RcvFarEndLOF.setStatus(
        "current"
    )

setT3NearEndSendLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 502)
)
setT3NearEndSendLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3NearEndSendLOF.setStatus(
        "current"
    )

setT3FarEndSendingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 503)
)
setT3FarEndSendingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3FarEndSendingAIS.setStatus(
        "current"
    )

setT3NearEndSendingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 504)
)
setT3NearEndSendingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3NearEndSendingAIS.setStatus(
        "current"
    )

setT3NearEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 505)
)
setT3NearEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3NearEndLOF.setStatus(
        "current"
    )

setT3NearEndLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 506)
)
setT3NearEndLossOfSignal.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3NearEndLossOfSignal.setStatus(
        "current"
    )

evntT3NearEndLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 507)
)
evntT3NearEndLooped.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT3NearEndLooped.setStatus(
        "current"
    )

setT3OtherLineStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 512)
)
setT3OtherLineStatus.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3OtherLineStatus.setStatus(
        "current"
    )

setT3NearEndUnavailableSig = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 513)
)
setT3NearEndUnavailableSig.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3NearEndUnavailableSig.setStatus(
        "current"
    )

evntT3CarrierEquipOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 514)
)
evntT3CarrierEquipOutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT3CarrierEquipOutOfService.setStatus(
        "current"
    )

setT3NearEndSeverErroredFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 515)
)
setT3NearEndSeverErroredFrame.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3NearEndSeverErroredFrame.setStatus(
        "current"
    )

setT3TxRxClockFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 516)
)
setT3TxRxClockFailure.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3TxRxClockFailure.setStatus(
        "current"
    )

setT3FarEndBlockError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 517)
)
setT3FarEndBlockError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3FarEndBlockError.setStatus(
        "current"
    )

setT3PbitCbitParityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 518)
)
setT3PbitCbitParityError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3PbitCbitParityError.setStatus(
        "current"
    )

setT3MbitsInError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 519)
)
setT3MbitsInError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3MbitsInError.setStatus(
        "current"
    )

setT3LIUOtherStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 520)
)
setT3LIUOtherStatus.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3LIUOtherStatus.setStatus(
        "current"
    )

setT3LIUExcessZeros = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 522)
)
setT3LIUExcessZeros.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3LIUExcessZeros.setStatus(
        "current"
    )

setT3LIUCodingViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 523)
)
setT3LIUCodingViolation.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3LIUCodingViolation.setStatus(
        "current"
    )

setT3LIUPrbsError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 524)
)
setT3LIUPrbsError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3LIUPrbsError.setStatus(
        "current"
    )

setT3ConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 525)
)
setT3ConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setT3ConfigError.setStatus(
        "current"
    )

evntT3InTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 530)
)
evntT3InTest.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT3InTest.setStatus(
        "current"
    )

evntT3OutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 531)
)
evntT3OutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT3OutOfService.setStatus(
        "current"
    )

clearT3RcvFarEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 541)
)
clearT3RcvFarEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3RcvFarEndLOF.setStatus(
        "current"
    )

clearT3NearEndSendLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 542)
)
clearT3NearEndSendLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3NearEndSendLOF.setStatus(
        "current"
    )

clearT3FarEndSendingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 543)
)
clearT3FarEndSendingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3FarEndSendingAIS.setStatus(
        "current"
    )

clearT3NearEndSendingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 544)
)
clearT3NearEndSendingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3NearEndSendingAIS.setStatus(
        "current"
    )

clearT3NearEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 545)
)
clearT3NearEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3NearEndLOF.setStatus(
        "current"
    )

clearT3NearEndLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 546)
)
clearT3NearEndLossOfSignal.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3NearEndLossOfSignal.setStatus(
        "current"
    )

evntT3NearEndLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 547)
)
evntT3NearEndLoopOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT3NearEndLoopOff.setStatus(
        "current"
    )

clearT3OtherLineStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 552)
)
clearT3OtherLineStatus.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3OtherLineStatus.setStatus(
        "current"
    )

clearT3NearEndUnavailableSig = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 553)
)
clearT3NearEndUnavailableSig.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3NearEndUnavailableSig.setStatus(
        "current"
    )

evntT3CarrierEquipInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 554)
)
evntT3CarrierEquipInService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT3CarrierEquipInService.setStatus(
        "current"
    )

clearT3NearEndSeverErroredFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 555)
)
clearT3NearEndSeverErroredFrame.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3NearEndSeverErroredFrame.setStatus(
        "current"
    )

clearT3TxRxClockFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 556)
)
clearT3TxRxClockFailure.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3TxRxClockFailure.setStatus(
        "current"
    )

clearT3FarEndBlockError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 557)
)
clearT3FarEndBlockError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3FarEndBlockError.setStatus(
        "current"
    )

clearT3PbitCbitParityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 558)
)
clearT3PbitCbitParityError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3PbitCbitParityError.setStatus(
        "current"
    )

clearT3MbitsInError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 559)
)
clearT3MbitsInError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3MbitsInError.setStatus(
        "current"
    )

clearT3LIUOtherStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 560)
)
clearT3LIUOtherStatus.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3LIUOtherStatus.setStatus(
        "current"
    )

clearT3LIUExcessZeros = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 562)
)
clearT3LIUExcessZeros.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3LIUExcessZeros.setStatus(
        "current"
    )

clearT3LIUCodingViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 563)
)
clearT3LIUCodingViolation.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3LIUCodingViolation.setStatus(
        "current"
    )

clearT3LIUPrbsError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 564)
)
clearT3LIUPrbsError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3LIUPrbsError.setStatus(
        "current"
    )

clearT3ConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 565)
)
clearT3ConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearT3ConfigError.setStatus(
        "current"
    )

evntT3TestOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 570)
)
evntT3TestOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT3TestOff.setStatus(
        "current"
    )

evntT3InService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 571)
)
evntT3InService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntT3InService.setStatus(
        "current"
    )

setPowerSupplyNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 601)
)
setPowerSupplyNotPresent.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setPowerSupplyNotPresent.setStatus(
        "current"
    )

setPowerSupplyProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 602)
)
setPowerSupplyProblem.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setPowerSupplyProblem.setStatus(
        "current"
    )

clearPowerSupplyNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 641)
)
clearPowerSupplyNotPresent.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearPowerSupplyNotPresent.setStatus(
        "current"
    )

clearPowerSupplyProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 642)
)
clearPowerSupplyProblem.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearPowerSupplyProblem.setStatus(
        "current"
    )

setOcuNearEndLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 706)
)
setOcuNearEndLOS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOcuNearEndLOS.setStatus(
        "current"
    )

setOcuOtherLineStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 712)
)
setOcuOtherLineStatus.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOcuOtherLineStatus.setStatus(
        "current"
    )

setOcuNearEndSeverErroredFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 723)
)
setOcuNearEndSeverErroredFrame.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOcuNearEndSeverErroredFrame.setStatus(
        "current"
    )

setOcuConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 725)
)
setOcuConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOcuConfigError.setStatus(
        "current"
    )

evntOcuOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 731)
)
evntOcuOutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntOcuOutOfService.setStatus(
        "current"
    )

clearOcuNearEndLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 746)
)
clearOcuNearEndLOS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOcuNearEndLOS.setStatus(
        "current"
    )

clearOcuOtherLineStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 752)
)
clearOcuOtherLineStatus.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOcuOtherLineStatus.setStatus(
        "current"
    )

clearOcuNearEndSeverErroredFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 763)
)
clearOcuNearEndSeverErroredFrame.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOcuNearEndSeverErroredFrame.setStatus(
        "current"
    )

clearOcuConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 765)
)
clearOcuConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOcuConfigError.setStatus(
        "current"
    )

evntOcuInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 771)
)
evntOcuInService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntOcuInService.setStatus(
        "current"
    )

setTamConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 825)
)
setTamConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setTamConfigError.setStatus(
        "current"
    )

evntTamOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 831)
)
evntTamOutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntTamOutOfService.setStatus(
        "current"
    )

clearTamConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 865)
)
clearTamConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearTamConfigError.setStatus(
        "current"
    )

evntTamInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 871)
)
evntTamInService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntTamInService.setStatus(
        "current"
    )

setVoiceConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 925)
)
setVoiceConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setVoiceConfigError.setStatus(
        "current"
    )

evntVoiceOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 931)
)
evntVoiceOutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntVoiceOutOfService.setStatus(
        "current"
    )

clearVoiceConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 965)
)
clearVoiceConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearVoiceConfigError.setStatus(
        "current"
    )

evntVoiceInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 971)
)
evntVoiceInService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntVoiceInService.setStatus(
        "current"
    )

evntPsxDevOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1001)
)
evntPsxDevOnline.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxDevOnline.setStatus(
        "current"
    )

setPsxPowerSupplyANotOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1003)
)
setPsxPowerSupplyANotOk.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setPsxPowerSupplyANotOk.setStatus(
        "current"
    )

setPsxPowerSupplyBNotOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1004)
)
setPsxPowerSupplyBNotOk.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setPsxPowerSupplyBNotOk.setStatus(
        "current"
    )

setPsxFan01NotOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1005)
)
setPsxFan01NotOk.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setPsxFan01NotOk.setStatus(
        "current"
    )

setPsxFan02NotOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1006)
)
setPsxFan02NotOk.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setPsxFan02NotOk.setStatus(
        "current"
    )

setPsxFan03NotOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1007)
)
setPsxFan03NotOk.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setPsxFan03NotOk.setStatus(
        "current"
    )

setPsxDualBroadbandNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1008)
)
setPsxDualBroadbandNotSupported.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setPsxDualBroadbandNotSupported.setStatus(
        "current"
    )

evntPsxNewControllerRev = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1009)
)
evntPsxNewControllerRev.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxNewControllerRev.setStatus(
        "current"
    )

evntPsxLineCard01Missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1014)
)
evntPsxLineCard01Missing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard01Missing.setStatus(
        "current"
    )

evntPsxLineCard02Missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1015)
)
evntPsxLineCard02Missing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard02Missing.setStatus(
        "current"
    )

evntPsxLineCard03Missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1016)
)
evntPsxLineCard03Missing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard03Missing.setStatus(
        "current"
    )

evntPsxLineCard04Missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1017)
)
evntPsxLineCard04Missing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard04Missing.setStatus(
        "current"
    )

evntPsxLineCard05Missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1018)
)
evntPsxLineCard05Missing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard05Missing.setStatus(
        "current"
    )

evntPsxLineCard06Missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1019)
)
evntPsxLineCard06Missing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard06Missing.setStatus(
        "current"
    )

evntPsxLineCard07Missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1020)
)
evntPsxLineCard07Missing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard07Missing.setStatus(
        "current"
    )

evntPsxLineCard08Missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1021)
)
evntPsxLineCard08Missing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard08Missing.setStatus(
        "current"
    )

evntPsxLineCard09Missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1022)
)
evntPsxLineCard09Missing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard09Missing.setStatus(
        "current"
    )

evntPsxLineCard10Missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1023)
)
evntPsxLineCard10Missing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard10Missing.setStatus(
        "current"
    )

evntPsxLineCard11Missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1024)
)
evntPsxLineCard11Missing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard11Missing.setStatus(
        "current"
    )

clearPsxPowerSupplyANotOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1043)
)
clearPsxPowerSupplyANotOk.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearPsxPowerSupplyANotOk.setStatus(
        "current"
    )

clearPsxPowerSupplyBNotOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1044)
)
clearPsxPowerSupplyBNotOk.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearPsxPowerSupplyBNotOk.setStatus(
        "current"
    )

clearPsxFan01NotOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1045)
)
clearPsxFan01NotOk.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearPsxFan01NotOk.setStatus(
        "current"
    )

clearPsxFan02NotOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1046)
)
clearPsxFan02NotOk.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearPsxFan02NotOk.setStatus(
        "current"
    )

clearPsxFan03NotOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1047)
)
clearPsxFan03NotOk.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearPsxFan03NotOk.setStatus(
        "current"
    )

clearPsxDualBroadbandNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1048)
)
clearPsxDualBroadbandNotSupported.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearPsxDualBroadbandNotSupported.setStatus(
        "current"
    )

evntPsxLineCard01Present = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1054)
)
evntPsxLineCard01Present.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard01Present.setStatus(
        "current"
    )

evntPsxLineCard02Present = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1055)
)
evntPsxLineCard02Present.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard02Present.setStatus(
        "current"
    )

evntPsxLineCard03Present = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1056)
)
evntPsxLineCard03Present.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard03Present.setStatus(
        "current"
    )

evntPsxLineCard04Present = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1057)
)
evntPsxLineCard04Present.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard04Present.setStatus(
        "current"
    )

evntPsxLineCard05Present = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1058)
)
evntPsxLineCard05Present.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard05Present.setStatus(
        "current"
    )

evntPsxLineCard06Present = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1059)
)
evntPsxLineCard06Present.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard06Present.setStatus(
        "current"
    )

evntPsxLineCard07Present = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1060)
)
evntPsxLineCard07Present.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard07Present.setStatus(
        "current"
    )

evntPsxLineCard08Present = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1061)
)
evntPsxLineCard08Present.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard08Present.setStatus(
        "current"
    )

evntPsxLineCard09Present = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1062)
)
evntPsxLineCard09Present.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard09Present.setStatus(
        "current"
    )

evntPsxLineCard10Present = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1063)
)
evntPsxLineCard10Present.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard10Present.setStatus(
        "current"
    )

evntPsxLineCard11Present = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1064)
)
evntPsxLineCard11Present.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPsxLineCard11Present.setStatus(
        "current"
    )

setPsxLineCardRelaySwitchToSpare = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1102)
)
setPsxLineCardRelaySwitchToSpare.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setPsxLineCardRelaySwitchToSpare.setStatus(
        "current"
    )

setPsxLineCardCableMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1103)
)
setPsxLineCardCableMissing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setPsxLineCardCableMissing.setStatus(
        "current"
    )

setPsxLineCardMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1106)
)
setPsxLineCardMissing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setPsxLineCardMissing.setStatus(
        "current"
    )

setPsxLineCardMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1107)
)
setPsxLineCardMismatch.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setPsxLineCardMismatch.setStatus(
        "current"
    )

setPsxLineCardRelayMalfunction = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1108)
)
setPsxLineCardRelayMalfunction.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setPsxLineCardRelayMalfunction.setStatus(
        "current"
    )

clearPsxLineCardRelaySwitchToSpare = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1142)
)
clearPsxLineCardRelaySwitchToSpare.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearPsxLineCardRelaySwitchToSpare.setStatus(
        "current"
    )

clearPsxLineCardCableMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1143)
)
clearPsxLineCardCableMissing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearPsxLineCardCableMissing.setStatus(
        "current"
    )

clearPsxLineCardMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1146)
)
clearPsxLineCardMissing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearPsxLineCardMissing.setStatus(
        "current"
    )

clearPsxLineCardMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1147)
)
clearPsxLineCardMismatch.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearPsxLineCardMismatch.setStatus(
        "current"
    )

clearPsxLineCardRelayMalfunction = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1148)
)
clearPsxLineCardRelayMalfunction.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearPsxLineCardRelayMalfunction.setStatus(
        "current"
    )

setRtrUserAlarm1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1201)
)
setRtrUserAlarm1.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setRtrUserAlarm1.setStatus(
        "current"
    )

setRtrUserAlarm2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1202)
)
setRtrUserAlarm2.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setRtrUserAlarm2.setStatus(
        "current"
    )

setRtrUserAlarm3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1203)
)
setRtrUserAlarm3.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setRtrUserAlarm3.setStatus(
        "current"
    )

setRtrConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1225)
)
setRtrConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setRtrConfigError.setStatus(
        "current"
    )

evntRtrOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1231)
)
evntRtrOutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntRtrOutOfService.setStatus(
        "current"
    )

clearRtrUserAlarm1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1241)
)
clearRtrUserAlarm1.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearRtrUserAlarm1.setStatus(
        "current"
    )

clearRtrUserAlarm2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1242)
)
clearRtrUserAlarm2.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearRtrUserAlarm2.setStatus(
        "current"
    )

clearRtrUserAlarm3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1243)
)
clearRtrUserAlarm3.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearRtrUserAlarm3.setStatus(
        "current"
    )

clearRtrConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1265)
)
clearRtrConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearRtrConfigError.setStatus(
        "current"
    )

evntRtrInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1271)
)
evntRtrInService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntRtrInService.setStatus(
        "current"
    )

setSts1RcvFarEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1301)
)
setSts1RcvFarEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1RcvFarEndLOF.setStatus(
        "current"
    )

setSts1NearEndSendLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1302)
)
setSts1NearEndSendLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1NearEndSendLOF.setStatus(
        "current"
    )

evntSts1RcvingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1303)
)
evntSts1RcvingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntSts1RcvingAIS.setStatus(
        "current"
    )

setSts1NearEndSendingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1304)
)
setSts1NearEndSendingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1NearEndSendingAIS.setStatus(
        "current"
    )

setSts1NearEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1305)
)
setSts1NearEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1NearEndLOF.setStatus(
        "current"
    )

evntSts1NearEndLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1307)
)
evntSts1NearEndLooped.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntSts1NearEndLooped.setStatus(
        "current"
    )

setSts1NearEndLOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1308)
)
setSts1NearEndLOP.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1NearEndLOP.setStatus(
        "current"
    )

setSts1NearEndOOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1309)
)
setSts1NearEndOOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1NearEndOOF.setStatus(
        "current"
    )

setSts1NearEndAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1310)
)
setSts1NearEndAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1NearEndAIS.setStatus(
        "current"
    )

setSts1OtherLineStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1312)
)
setSts1OtherLineStatus.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1OtherLineStatus.setStatus(
        "current"
    )

setSts1NearEndUnavailableSig = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1313)
)
setSts1NearEndUnavailableSig.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1NearEndUnavailableSig.setStatus(
        "current"
    )

evntSts1CarrierEquipOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1314)
)
evntSts1CarrierEquipOutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntSts1CarrierEquipOutOfService.setStatus(
        "current"
    )

setSts1TxRxClockFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1316)
)
setSts1TxRxClockFailure.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1TxRxClockFailure.setStatus(
        "current"
    )

setSts1NearEndLOMF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1317)
)
setSts1NearEndLOMF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1NearEndLOMF.setStatus(
        "current"
    )

setSts1NearEndTraceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1318)
)
setSts1NearEndTraceError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1NearEndTraceError.setStatus(
        "current"
    )

setSts1LIUDigitalLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1320)
)
setSts1LIUDigitalLOS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1LIUDigitalLOS.setStatus(
        "current"
    )

setSts1LIUAnalogLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1321)
)
setSts1LIUAnalogLOS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1LIUAnalogLOS.setStatus(
        "current"
    )

setSts1LIUExcessZeros = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1322)
)
setSts1LIUExcessZeros.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1LIUExcessZeros.setStatus(
        "current"
    )

setSts1LIUCodingViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1323)
)
setSts1LIUCodingViolation.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1LIUCodingViolation.setStatus(
        "current"
    )

setSts1LIUPrbsError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1324)
)
setSts1LIUPrbsError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1LIUPrbsError.setStatus(
        "current"
    )

setSts1ConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1325)
)
setSts1ConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setSts1ConfigError.setStatus(
        "current"
    )

evntSts1InTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1330)
)
evntSts1InTest.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntSts1InTest.setStatus(
        "current"
    )

evntSts1OutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1331)
)
evntSts1OutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntSts1OutOfService.setStatus(
        "current"
    )

clearSts1RcvFarEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1341)
)
clearSts1RcvFarEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1RcvFarEndLOF.setStatus(
        "current"
    )

clearSts1NearEndSendLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1342)
)
clearSts1NearEndSendLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1NearEndSendLOF.setStatus(
        "current"
    )

evntSts1StoppedRcvingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1343)
)
evntSts1StoppedRcvingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntSts1StoppedRcvingAIS.setStatus(
        "current"
    )

clearSts1NearEndSendingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1344)
)
clearSts1NearEndSendingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1NearEndSendingAIS.setStatus(
        "current"
    )

clearSts1NearEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1345)
)
clearSts1NearEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1NearEndLOF.setStatus(
        "current"
    )

evntSts1NearEndLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1347)
)
evntSts1NearEndLoopOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntSts1NearEndLoopOff.setStatus(
        "current"
    )

clearSts1NearEndLOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1348)
)
clearSts1NearEndLOP.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1NearEndLOP.setStatus(
        "current"
    )

clearSts1NearEndOOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1349)
)
clearSts1NearEndOOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1NearEndOOF.setStatus(
        "current"
    )

clearSts1NearEndAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1350)
)
clearSts1NearEndAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1NearEndAIS.setStatus(
        "current"
    )

clearSts1OtherLineStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1352)
)
clearSts1OtherLineStatus.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1OtherLineStatus.setStatus(
        "current"
    )

clearSts1NearEndUnavailableSig = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1353)
)
clearSts1NearEndUnavailableSig.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1NearEndUnavailableSig.setStatus(
        "current"
    )

evntSts1CarrierEquipInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1354)
)
evntSts1CarrierEquipInService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntSts1CarrierEquipInService.setStatus(
        "current"
    )

clearSts1TxRxClockFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1356)
)
clearSts1TxRxClockFailure.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1TxRxClockFailure.setStatus(
        "current"
    )

clearSts1NearEndLOMF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1357)
)
clearSts1NearEndLOMF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1NearEndLOMF.setStatus(
        "current"
    )

clearSts1NearEndTraceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1358)
)
clearSts1NearEndTraceError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1NearEndTraceError.setStatus(
        "current"
    )

clearSts1LIUDigitalLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1360)
)
clearSts1LIUDigitalLOS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1LIUDigitalLOS.setStatus(
        "current"
    )

clearSts1LIUAnalogLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1361)
)
clearSts1LIUAnalogLOS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1LIUAnalogLOS.setStatus(
        "current"
    )

clearSts1LIUExcessZeros = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1362)
)
clearSts1LIUExcessZeros.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1LIUExcessZeros.setStatus(
        "current"
    )

clearSts1LIUCodingViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1363)
)
clearSts1LIUCodingViolation.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1LIUCodingViolation.setStatus(
        "current"
    )

clearSts1LIUPrbsError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1364)
)
clearSts1LIUPrbsError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1LIUPrbsError.setStatus(
        "current"
    )

clearSts1ConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1365)
)
clearSts1ConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearSts1ConfigError.setStatus(
        "current"
    )

evntSts1TestOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1370)
)
evntSts1TestOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntSts1TestOff.setStatus(
        "current"
    )

evntSts1InService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1371)
)
evntSts1InService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntSts1InService.setStatus(
        "current"
    )

evntHt3RcvingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1403)
)
evntHt3RcvingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHt3RcvingAIS.setStatus(
        "current"
    )

setHt3NearEndSendingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1404)
)
setHt3NearEndSendingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHt3NearEndSendingAIS.setStatus(
        "current"
    )

setHt3NearEndOOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1405)
)
setHt3NearEndOOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHt3NearEndOOF.setStatus(
        "current"
    )

setHt3NearEndLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1406)
)
setHt3NearEndLossOfSignal.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHt3NearEndLossOfSignal.setStatus(
        "current"
    )

evntHt3NearEndLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1407)
)
evntHt3NearEndLooped.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHt3NearEndLooped.setStatus(
        "current"
    )

setHt3NearEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1408)
)
setHt3NearEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHt3NearEndLOF.setStatus(
        "current"
    )

setHt3FarEndRcvFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1409)
)
setHt3FarEndRcvFailure.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHt3FarEndRcvFailure.setStatus(
        "current"
    )

setHt3NearEndLCVError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1411)
)
setHt3NearEndLCVError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHt3NearEndLCVError.setStatus(
        "current"
    )

setHt3NearEndFERRError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1412)
)
setHt3NearEndFERRError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHt3NearEndFERRError.setStatus(
        "current"
    )

setHt3NearEndExcessZeros = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1413)
)
setHt3NearEndExcessZeros.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHt3NearEndExcessZeros.setStatus(
        "current"
    )

evntHt3CarrierEquipOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1414)
)
evntHt3CarrierEquipOutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHt3CarrierEquipOutOfService.setStatus(
        "current"
    )

setHt3FarEndBlockError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1417)
)
setHt3FarEndBlockError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHt3FarEndBlockError.setStatus(
        "current"
    )

setHt3PbitCbitParityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1418)
)
setHt3PbitCbitParityError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHt3PbitCbitParityError.setStatus(
        "current"
    )

setHt3ChangeInFrameAlignment = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1419)
)
setHt3ChangeInFrameAlignment.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHt3ChangeInFrameAlignment.setStatus(
        "current"
    )

setHt3LIUDigitalLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1420)
)
setHt3LIUDigitalLOS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHt3LIUDigitalLOS.setStatus(
        "current"
    )

setHt3LIUAnalogLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1421)
)
setHt3LIUAnalogLOS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHt3LIUAnalogLOS.setStatus(
        "current"
    )

setHt3LIUExcessZeros = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1422)
)
setHt3LIUExcessZeros.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHt3LIUExcessZeros.setStatus(
        "current"
    )

setHt3LIUCodingViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1423)
)
setHt3LIUCodingViolation.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHt3LIUCodingViolation.setStatus(
        "current"
    )

setHt3LIUPrbsError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1424)
)
setHt3LIUPrbsError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHt3LIUPrbsError.setStatus(
        "current"
    )

setHt3ConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1425)
)
setHt3ConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setHt3ConfigError.setStatus(
        "current"
    )

evntHt3InTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1430)
)
evntHt3InTest.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHt3InTest.setStatus(
        "current"
    )

evntHt3OutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1431)
)
evntHt3OutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHt3OutOfService.setStatus(
        "current"
    )

evntHt3StoppedRcvingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1443)
)
evntHt3StoppedRcvingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHt3StoppedRcvingAIS.setStatus(
        "current"
    )

clearHt3NearEndSendingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1444)
)
clearHt3NearEndSendingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHt3NearEndSendingAIS.setStatus(
        "current"
    )

clearHt3NearEndOOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1445)
)
clearHt3NearEndOOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHt3NearEndOOF.setStatus(
        "current"
    )

clearHt3NearEndLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1446)
)
clearHt3NearEndLossOfSignal.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHt3NearEndLossOfSignal.setStatus(
        "current"
    )

evntHt3NearEndLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1447)
)
evntHt3NearEndLoopOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHt3NearEndLoopOff.setStatus(
        "current"
    )

clearHt3NearEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1448)
)
clearHt3NearEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHt3NearEndLOF.setStatus(
        "current"
    )

clearHt3FarEndRcvFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1449)
)
clearHt3FarEndRcvFailure.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHt3FarEndRcvFailure.setStatus(
        "current"
    )

clearHt3NearEndLCVError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1451)
)
clearHt3NearEndLCVError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHt3NearEndLCVError.setStatus(
        "current"
    )

clearHt3NearEndFERRError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1452)
)
clearHt3NearEndFERRError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHt3NearEndFERRError.setStatus(
        "current"
    )

clearHt3NearEndExcessZeros = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1453)
)
clearHt3NearEndExcessZeros.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHt3NearEndExcessZeros.setStatus(
        "current"
    )

evntHt3CarrierEquipInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1454)
)
evntHt3CarrierEquipInService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHt3CarrierEquipInService.setStatus(
        "current"
    )

clearHt3FarEndBlockError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1457)
)
clearHt3FarEndBlockError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHt3FarEndBlockError.setStatus(
        "current"
    )

clearHt3PbitCbitParityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1458)
)
clearHt3PbitCbitParityError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHt3PbitCbitParityError.setStatus(
        "current"
    )

clearHt3ChangeInFrameAlignment = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1459)
)
clearHt3ChangeInFrameAlignment.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHt3ChangeInFrameAlignment.setStatus(
        "current"
    )

clearHt3LIUDigitalLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1460)
)
clearHt3LIUDigitalLOS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHt3LIUDigitalLOS.setStatus(
        "current"
    )

clearHt3LIUAnalogLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1461)
)
clearHt3LIUAnalogLOS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHt3LIUAnalogLOS.setStatus(
        "current"
    )

clearHt3LIUExcessZeros = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1462)
)
clearHt3LIUExcessZeros.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHt3LIUExcessZeros.setStatus(
        "current"
    )

clearHt3LIUCodingViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1463)
)
clearHt3LIUCodingViolation.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHt3LIUCodingViolation.setStatus(
        "current"
    )

clearHt3LIUPrbsError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1464)
)
clearHt3LIUPrbsError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHt3LIUPrbsError.setStatus(
        "current"
    )

clearHt3ConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1465)
)
clearHt3ConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearHt3ConfigError.setStatus(
        "current"
    )

evntHt3TestOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1470)
)
evntHt3TestOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHt3TestOff.setStatus(
        "current"
    )

evntHt3InService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1471)
)
evntHt3InService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntHt3InService.setStatus(
        "current"
    )

evntGr303OutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1531)
)
evntGr303OutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntGr303OutOfService.setStatus(
        "current"
    )

evntGr303InService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1571)
)
evntGr303InService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntGr303InService.setStatus(
        "current"
    )

setXlinkCableMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1606)
)
setXlinkCableMismatch.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setXlinkCableMismatch.setStatus(
        "current"
    )

setXlinkSerializerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1615)
)
setXlinkSerializerError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setXlinkSerializerError.setStatus(
        "current"
    )

setXlinkFramerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1616)
)
setXlinkFramerError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setXlinkFramerError.setStatus(
        "current"
    )

setXlinkBertError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1617)
)
setXlinkBertError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setXlinkBertError.setStatus(
        "current"
    )

setXlinkClockError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1618)
)
setXlinkClockError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setXlinkClockError.setStatus(
        "current"
    )

setXlinkInUseError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1620)
)
setXlinkInUseError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setXlinkInUseError.setStatus(
        "current"
    )

setXlinkCrcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1621)
)
setXlinkCrcError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setXlinkCrcError.setStatus(
        "current"
    )

clearXlinkCableMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1646)
)
clearXlinkCableMismatch.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearXlinkCableMismatch.setStatus(
        "current"
    )

clearXlinkSerializerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1655)
)
clearXlinkSerializerError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearXlinkSerializerError.setStatus(
        "current"
    )

clearXlinkFramerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1656)
)
clearXlinkFramerError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearXlinkFramerError.setStatus(
        "current"
    )

clearXlinkBertError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1657)
)
clearXlinkBertError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearXlinkBertError.setStatus(
        "current"
    )

clearXlinkClockError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1658)
)
clearXlinkClockError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearXlinkClockError.setStatus(
        "current"
    )

clearXlinkInUseError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1660)
)
clearXlinkInUseError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearXlinkInUseError.setStatus(
        "current"
    )

clearXlinkCrcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1661)
)
clearXlinkCrcError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearXlinkCrcError.setStatus(
        "current"
    )

setNestMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1701)
)
setNestMismatch.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setNestMismatch.setStatus(
        "current"
    )

setNestMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1702)
)
setNestMissing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setNestMissing.setStatus(
        "current"
    )

setNestOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1705)
)
setNestOffline.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setNestOffline.setStatus(
        "current"
    )

setNestCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1706)
)
setNestCriticalAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setNestCriticalAlarm.setStatus(
        "current"
    )

setNestMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1707)
)
setNestMajorAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setNestMajorAlarm.setStatus(
        "current"
    )

setNestMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1708)
)
setNestMinorAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setNestMinorAlarm.setStatus(
        "current"
    )

setNestSwMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1709)
)
setNestSwMismatch.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setNestSwMismatch.setStatus(
        "current"
    )

clearNestMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1741)
)
clearNestMismatch.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearNestMismatch.setStatus(
        "current"
    )

clearNestMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1742)
)
clearNestMissing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearNestMissing.setStatus(
        "current"
    )

clearNestOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1745)
)
clearNestOffline.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearNestOffline.setStatus(
        "current"
    )

clearNestCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1746)
)
clearNestCriticalAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearNestCriticalAlarm.setStatus(
        "current"
    )

clearNestMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1747)
)
clearNestMajorAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearNestMajorAlarm.setStatus(
        "current"
    )

clearNestMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1748)
)
clearNestMinorAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearNestMinorAlarm.setStatus(
        "current"
    )

clearNestSwMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1749)
)
clearNestSwMismatch.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearNestSwMismatch.setStatus(
        "current"
    )

setNodeCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1801)
)
setNodeCriticalAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setNodeCriticalAlarm.setStatus(
        "current"
    )

setNodeMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1802)
)
setNodeMajorAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setNodeMajorAlarm.setStatus(
        "current"
    )

setNodeMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1803)
)
setNodeMinorAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setNodeMinorAlarm.setStatus(
        "current"
    )

clearNodeCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1841)
)
clearNodeCriticalAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearNodeCriticalAlarm.setStatus(
        "current"
    )

clearNodeMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1842)
)
clearNodeMajorAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearNodeMajorAlarm.setStatus(
        "current"
    )

clearNodeMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1843)
)
clearNodeMinorAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearNodeMinorAlarm.setStatus(
        "current"
    )

setDs0DpPortLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1901)
)
setDs0DpPortLossOfSignal.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setDs0DpPortLossOfSignal.setStatus(
        "current"
    )

setDs0DpPortBPV = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1902)
)
setDs0DpPortBPV.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setDs0DpPortBPV.setStatus(
        "current"
    )

setDs0DpPortConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1925)
)
setDs0DpPortConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setDs0DpPortConfigError.setStatus(
        "current"
    )

evntDs0DpPortInTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1930)
)
evntDs0DpPortInTest.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntDs0DpPortInTest.setStatus(
        "current"
    )

evntDs0DpPortOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1931)
)
evntDs0DpPortOutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntDs0DpPortOutOfService.setStatus(
        "current"
    )

clearDs0DpPortLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1941)
)
clearDs0DpPortLossOfSignal.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearDs0DpPortLossOfSignal.setStatus(
        "current"
    )

clearDs0DpPortBPV = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1942)
)
clearDs0DpPortBPV.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearDs0DpPortBPV.setStatus(
        "current"
    )

clearDs0DpPortConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1965)
)
clearDs0DpPortConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearDs0DpPortConfigError.setStatus(
        "current"
    )

evntDs0DpPortTestOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1970)
)
evntDs0DpPortTestOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntDs0DpPortTestOff.setStatus(
        "current"
    )

evntDs0DpPortInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 1971)
)
evntDs0DpPortInService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntDs0DpPortInService.setStatus(
        "current"
    )

setDs0DpBitsLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2001)
)
setDs0DpBitsLossOfSignal.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setDs0DpBitsLossOfSignal.setStatus(
        "current"
    )

setDs0DpBitsBPV = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2002)
)
setDs0DpBitsBPV.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setDs0DpBitsBPV.setStatus(
        "current"
    )

clearDs0DpBitsLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2041)
)
clearDs0DpBitsLossOfSignal.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearDs0DpBitsLossOfSignal.setStatus(
        "current"
    )

clearDs0DpBitsBPV = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2042)
)
clearDs0DpBitsBPV.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearDs0DpBitsBPV.setStatus(
        "current"
    )

setOpticalT1E1RedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2201)
)
setOpticalT1E1RedAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOpticalT1E1RedAlarm.setStatus(
        "current"
    )

setOpticalT1E1NearEndSendLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2202)
)
setOpticalT1E1NearEndSendLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOpticalT1E1NearEndSendLOF.setStatus(
        "current"
    )

evntOpticalT1E1RcvingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2203)
)
evntOpticalT1E1RcvingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntOpticalT1E1RcvingAIS.setStatus(
        "current"
    )

setOpticalT1E1NearEndSendingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2204)
)
setOpticalT1E1NearEndSendingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOpticalT1E1NearEndSendingAIS.setStatus(
        "current"
    )

setOpticalT1E1NearEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2205)
)
setOpticalT1E1NearEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOpticalT1E1NearEndLOF.setStatus(
        "current"
    )

evntOpticalT1E1NearEndLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2207)
)
evntOpticalT1E1NearEndLooped.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntOpticalT1E1NearEndLooped.setStatus(
        "current"
    )

setOpticalT1E1LossOfPointer = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2208)
)
setOpticalT1E1LossOfPointer.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOpticalT1E1LossOfPointer.setStatus(
        "current"
    )

setOpticalT1E1OutOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2209)
)
setOpticalT1E1OutOfFrame.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOpticalT1E1OutOfFrame.setStatus(
        "current"
    )

setOpticalT1E1DetectedAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2210)
)
setOpticalT1E1DetectedAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOpticalT1E1DetectedAIS.setStatus(
        "current"
    )

setOpticalT1E1NearEndLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2213)
)
setOpticalT1E1NearEndLOS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOpticalT1E1NearEndLOS.setStatus(
        "current"
    )

evntOpticalE1NationalSa4TxRxSame = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2216)
)
evntOpticalE1NationalSa4TxRxSame.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntOpticalE1NationalSa4TxRxSame.setStatus(
        "current"
    )

setOpticalT1E1RcvFarEndYellow = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2217)
)
setOpticalT1E1RcvFarEndYellow.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOpticalT1E1RcvFarEndYellow.setStatus(
        "current"
    )

setOpticalT1E1NearEndSEF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2218)
)
setOpticalT1E1NearEndSEF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOpticalT1E1NearEndSEF.setStatus(
        "current"
    )

setOpticalT1E1Tug2LOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2219)
)
setOpticalT1E1Tug2LOP.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOpticalT1E1Tug2LOP.setStatus(
        "current"
    )

setOpticalT1E1Tug2RDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2220)
)
setOpticalT1E1Tug2RDI.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOpticalT1E1Tug2RDI.setStatus(
        "current"
    )

setOpticalT1E1Tug2RFI = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2221)
)
setOpticalT1E1Tug2RFI.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOpticalT1E1Tug2RFI.setStatus(
        "current"
    )

setOpticalT1E1Tug2AIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2222)
)
setOpticalT1E1Tug2AIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOpticalT1E1Tug2AIS.setStatus(
        "current"
    )

setOpticalT1E1Tug2PSLM = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2223)
)
setOpticalT1E1Tug2PSLM.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOpticalT1E1Tug2PSLM.setStatus(
        "current"
    )

setOpticalT1E1Tug2PSLU = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2224)
)
setOpticalT1E1Tug2PSLU.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOpticalT1E1Tug2PSLU.setStatus(
        "current"
    )

setOpticalT1E1ConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2225)
)
setOpticalT1E1ConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setOpticalT1E1ConfigError.setStatus(
        "current"
    )

evntOpticalT1E1InTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2230)
)
evntOpticalT1E1InTest.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntOpticalT1E1InTest.setStatus(
        "current"
    )

evntOpticalT1E1OutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2231)
)
evntOpticalT1E1OutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntOpticalT1E1OutOfService.setStatus(
        "current"
    )

clearOpticalT1E1RedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2241)
)
clearOpticalT1E1RedAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOpticalT1E1RedAlarm.setStatus(
        "current"
    )

clearOpticalT1E1NearEndSendLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2242)
)
clearOpticalT1E1NearEndSendLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOpticalT1E1NearEndSendLOF.setStatus(
        "current"
    )

evntOpticalT1E1StoppedRcvingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2243)
)
evntOpticalT1E1StoppedRcvingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntOpticalT1E1StoppedRcvingAIS.setStatus(
        "current"
    )

clearOpticalT1E1NearEndSendingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2244)
)
clearOpticalT1E1NearEndSendingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOpticalT1E1NearEndSendingAIS.setStatus(
        "current"
    )

clearOpticalT1E1NearEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2245)
)
clearOpticalT1E1NearEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOpticalT1E1NearEndLOF.setStatus(
        "current"
    )

evntOpticalT1E1NearEndLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2247)
)
evntOpticalT1E1NearEndLoopOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntOpticalT1E1NearEndLoopOff.setStatus(
        "current"
    )

clearOpticalT1E1LossOfPointer = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2248)
)
clearOpticalT1E1LossOfPointer.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOpticalT1E1LossOfPointer.setStatus(
        "current"
    )

clearOpticalT1E1OutOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2249)
)
clearOpticalT1E1OutOfFrame.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOpticalT1E1OutOfFrame.setStatus(
        "current"
    )

clearOpticalT1E1DetectedAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2250)
)
clearOpticalT1E1DetectedAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOpticalT1E1DetectedAIS.setStatus(
        "current"
    )

clearOpticalT1E1NearEndLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2253)
)
clearOpticalT1E1NearEndLOS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOpticalT1E1NearEndLOS.setStatus(
        "current"
    )

evntOpticalE1NationalSa4TxRxDiff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2256)
)
evntOpticalE1NationalSa4TxRxDiff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntOpticalE1NationalSa4TxRxDiff.setStatus(
        "current"
    )

clearOpticalT1E1RcvFarEndYellow = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2257)
)
clearOpticalT1E1RcvFarEndYellow.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOpticalT1E1RcvFarEndYellow.setStatus(
        "current"
    )

clearOpticalT1E1NearEndSEF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2258)
)
clearOpticalT1E1NearEndSEF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOpticalT1E1NearEndSEF.setStatus(
        "current"
    )

clearOpticalT1E1Tug2LOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2259)
)
clearOpticalT1E1Tug2LOP.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOpticalT1E1Tug2LOP.setStatus(
        "current"
    )

clearOpticalT1E1Tug2RDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2260)
)
clearOpticalT1E1Tug2RDI.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOpticalT1E1Tug2RDI.setStatus(
        "current"
    )

clearOpticalT1E1Tug2RFI = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2261)
)
clearOpticalT1E1Tug2RFI.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOpticalT1E1Tug2RFI.setStatus(
        "current"
    )

clearOpticalT1E1Tug2AIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2262)
)
clearOpticalT1E1Tug2AIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOpticalT1E1Tug2AIS.setStatus(
        "current"
    )

clearOpticalT1E1Tug2PSLM = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2263)
)
clearOpticalT1E1Tug2PSLM.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOpticalT1E1Tug2PSLM.setStatus(
        "current"
    )

clearOpticalT1E1Tug2PSLU = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2264)
)
clearOpticalT1E1Tug2PSLU.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOpticalT1E1Tug2PSLU.setStatus(
        "current"
    )

clearOpticalT1E1ConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2265)
)
clearOpticalT1E1ConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearOpticalT1E1ConfigError.setStatus(
        "current"
    )

evntOpticalT1E1TestOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2270)
)
evntOpticalT1E1TestOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntOpticalT1E1TestOff.setStatus(
        "current"
    )

evntOpticalT1E1InService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2271)
)
evntOpticalT1E1InService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntOpticalT1E1InService.setStatus(
        "current"
    )

setVtNearEndLOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2301)
)
setVtNearEndLOP.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setVtNearEndLOP.setStatus(
        "current"
    )

setVtNearEndAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2302)
)
setVtNearEndAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setVtNearEndAIS.setStatus(
        "current"
    )

setPayloadPathLOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2303)
)
setPayloadPathLOP.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setPayloadPathLOP.setStatus(
        "current"
    )

setPayloadPathAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2304)
)
setPayloadPathAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setPayloadPathAIS.setStatus(
        "current"
    )

setPayloadPathRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2305)
)
setPayloadPathRDI.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setPayloadPathRDI.setStatus(
        "current"
    )

evntPayloadNearEndLineLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2307)
)
evntPayloadNearEndLineLooped.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPayloadNearEndLineLooped.setStatus(
        "current"
    )

evntPayloadNearEndLocalLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2308)
)
evntPayloadNearEndLocalLooped.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPayloadNearEndLocalLooped.setStatus(
        "current"
    )

evntPayloadInTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2330)
)
evntPayloadInTest.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPayloadInTest.setStatus(
        "current"
    )

clearVtNearEndLOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2341)
)
clearVtNearEndLOP.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearVtNearEndLOP.setStatus(
        "current"
    )

clearVtNearEndAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2342)
)
clearVtNearEndAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearVtNearEndAIS.setStatus(
        "current"
    )

clearPayloadPathLOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2343)
)
clearPayloadPathLOP.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearPayloadPathLOP.setStatus(
        "current"
    )

clearPayloadPathAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2344)
)
clearPayloadPathAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearPayloadPathAIS.setStatus(
        "current"
    )

clearPayloadPathRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2345)
)
clearPayloadPathRDI.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearPayloadPathRDI.setStatus(
        "current"
    )

evntPayloadNearEndLineLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2347)
)
evntPayloadNearEndLineLoopOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPayloadNearEndLineLoopOff.setStatus(
        "current"
    )

evntPayloadNearEndLocalLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2348)
)
evntPayloadNearEndLocalLoopOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPayloadNearEndLocalLoopOff.setStatus(
        "current"
    )

evntPayloadTestOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2370)
)
evntPayloadTestOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntPayloadTestOff.setStatus(
        "current"
    )

setTransOverheadAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2401)
)
setTransOverheadAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setTransOverheadAIS.setStatus(
        "current"
    )

setTransOverheadRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2402)
)
setTransOverheadRDI.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setTransOverheadRDI.setStatus(
        "current"
    )

setTransOverheadOOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2403)
)
setTransOverheadOOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setTransOverheadOOF.setStatus(
        "current"
    )

setTransOverheadLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2404)
)
setTransOverheadLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setTransOverheadLOF.setStatus(
        "current"
    )

setTransOverheadLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2405)
)
setTransOverheadLOS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setTransOverheadLOS.setStatus(
        "current"
    )

evntTransOverheadNearEndSysLineLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2407)
)
evntTransOverheadNearEndSysLineLooped.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntTransOverheadNearEndSysLineLooped.setStatus(
        "current"
    )

evntTransOverheadNearEndPathLineLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2408)
)
evntTransOverheadNearEndPathLineLooped.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntTransOverheadNearEndPathLineLooped.setStatus(
        "current"
    )

evntTransOverheadNearEndLocalLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2409)
)
evntTransOverheadNearEndLocalLooped.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntTransOverheadNearEndLocalLooped.setStatus(
        "current"
    )

setTransOverheadSfDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2413)
)
setTransOverheadSfDetect.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setTransOverheadSfDetect.setStatus(
        "current"
    )

setTransOverheadSdDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2414)
)
setTransOverheadSdDetect.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setTransOverheadSdDetect.setStatus(
        "current"
    )

setTransOverheadDetectLaserOffDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2415)
)
setTransOverheadDetectLaserOffDetect.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setTransOverheadDetectLaserOffDetect.setStatus(
        "current"
    )

evntTransOverheadInTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2430)
)
evntTransOverheadInTest.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntTransOverheadInTest.setStatus(
        "current"
    )

clearTransOverheadAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2441)
)
clearTransOverheadAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearTransOverheadAIS.setStatus(
        "current"
    )

clearTransOverheadRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2442)
)
clearTransOverheadRDI.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearTransOverheadRDI.setStatus(
        "current"
    )

clearTransOverheadOOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2443)
)
clearTransOverheadOOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearTransOverheadOOF.setStatus(
        "current"
    )

clearTransOverheadLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2444)
)
clearTransOverheadLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearTransOverheadLOF.setStatus(
        "current"
    )

clearTransOverheadLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2445)
)
clearTransOverheadLOS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearTransOverheadLOS.setStatus(
        "current"
    )

evntTransOverheadNearEndSysLineLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2447)
)
evntTransOverheadNearEndSysLineLoopOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntTransOverheadNearEndSysLineLoopOff.setStatus(
        "current"
    )

evntTransOverheadNearEndPathLineLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2448)
)
evntTransOverheadNearEndPathLineLoopOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntTransOverheadNearEndPathLineLoopOff.setStatus(
        "current"
    )

evntTransOverheadNearEndLocalLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2449)
)
evntTransOverheadNearEndLocalLoopOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntTransOverheadNearEndLocalLoopOff.setStatus(
        "current"
    )

clearTransOverheadSfDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2453)
)
clearTransOverheadSfDetect.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearTransOverheadSfDetect.setStatus(
        "current"
    )

clearTransOverheadSdDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2454)
)
clearTransOverheadSdDetect.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearTransOverheadSdDetect.setStatus(
        "current"
    )

clearTransOverheadLaserOffDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2455)
)
clearTransOverheadLaserOffDetect.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearTransOverheadLaserOffDetect.setStatus(
        "current"
    )

evntTransOverheadTestOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2470)
)
evntTransOverheadTestOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntTransOverheadTestOff.setStatus(
        "current"
    )

setE3RcvFarEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2501)
)
setE3RcvFarEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setE3RcvFarEndLOF.setStatus(
        "current"
    )

setE3NearEndSendLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2502)
)
setE3NearEndSendLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setE3NearEndSendLOF.setStatus(
        "current"
    )

evntE3RcvingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2503)
)
evntE3RcvingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntE3RcvingAIS.setStatus(
        "current"
    )

setE3NearEndSendingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2504)
)
setE3NearEndSendingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setE3NearEndSendingAIS.setStatus(
        "current"
    )

setE3NearEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2505)
)
setE3NearEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setE3NearEndLOF.setStatus(
        "current"
    )

setE3NearEndLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2506)
)
setE3NearEndLossOfSignal.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setE3NearEndLossOfSignal.setStatus(
        "current"
    )

evntE3NearEndLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2507)
)
evntE3NearEndLooped.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntE3NearEndLooped.setStatus(
        "current"
    )

setE3OtherLineStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2512)
)
setE3OtherLineStatus.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setE3OtherLineStatus.setStatus(
        "current"
    )

setE3NearEndUnavailableSig = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2513)
)
setE3NearEndUnavailableSig.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setE3NearEndUnavailableSig.setStatus(
        "current"
    )

evntE3CarrierEquipOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2514)
)
evntE3CarrierEquipOutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntE3CarrierEquipOutOfService.setStatus(
        "current"
    )

setE3NearEndSeverErroredFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2515)
)
setE3NearEndSeverErroredFrame.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setE3NearEndSeverErroredFrame.setStatus(
        "current"
    )

setE3TxRxClockFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2516)
)
setE3TxRxClockFailure.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setE3TxRxClockFailure.setStatus(
        "current"
    )

setE3FarEndBlockError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2517)
)
setE3FarEndBlockError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setE3FarEndBlockError.setStatus(
        "current"
    )

setE3MbitsInError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2519)
)
setE3MbitsInError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setE3MbitsInError.setStatus(
        "current"
    )

setE3LIUOtherStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2520)
)
setE3LIUOtherStatus.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setE3LIUOtherStatus.setStatus(
        "current"
    )

setE3LIUCodingViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2523)
)
setE3LIUCodingViolation.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setE3LIUCodingViolation.setStatus(
        "current"
    )

setE3ConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2525)
)
setE3ConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setE3ConfigError.setStatus(
        "current"
    )

evntE3InTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2530)
)
evntE3InTest.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntE3InTest.setStatus(
        "current"
    )

evntE3OutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2531)
)
evntE3OutOfService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntE3OutOfService.setStatus(
        "current"
    )

clearE3RcvFarEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2541)
)
clearE3RcvFarEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearE3RcvFarEndLOF.setStatus(
        "current"
    )

clearE3NearEndSendLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2542)
)
clearE3NearEndSendLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearE3NearEndSendLOF.setStatus(
        "current"
    )

evntE3StoppedRcvingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2543)
)
evntE3StoppedRcvingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntE3StoppedRcvingAIS.setStatus(
        "current"
    )

clearE3NearEndSendingAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2544)
)
clearE3NearEndSendingAIS.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearE3NearEndSendingAIS.setStatus(
        "current"
    )

clearE3NearEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2545)
)
clearE3NearEndLOF.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearE3NearEndLOF.setStatus(
        "current"
    )

clearE3NearEndLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2546)
)
clearE3NearEndLossOfSignal.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearE3NearEndLossOfSignal.setStatus(
        "current"
    )

evntE3NearEndLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2547)
)
evntE3NearEndLoopOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntE3NearEndLoopOff.setStatus(
        "current"
    )

clearE3OtherLineStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2552)
)
clearE3OtherLineStatus.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearE3OtherLineStatus.setStatus(
        "current"
    )

clearE3NearEndUnavailableSig = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2553)
)
clearE3NearEndUnavailableSig.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearE3NearEndUnavailableSig.setStatus(
        "current"
    )

evntE3CarrierEquipInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2554)
)
evntE3CarrierEquipInService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntE3CarrierEquipInService.setStatus(
        "current"
    )

clearE3NearEndSeverErroredFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2555)
)
clearE3NearEndSeverErroredFrame.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearE3NearEndSeverErroredFrame.setStatus(
        "current"
    )

clearE3TxRxClockFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2556)
)
clearE3TxRxClockFailure.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearE3TxRxClockFailure.setStatus(
        "current"
    )

clearE3FarEndBlockError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2557)
)
clearE3FarEndBlockError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearE3FarEndBlockError.setStatus(
        "current"
    )

clearE3MbitsInError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2559)
)
clearE3MbitsInError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearE3MbitsInError.setStatus(
        "current"
    )

clearE3LIUOtherStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2560)
)
clearE3LIUOtherStatus.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearE3LIUOtherStatus.setStatus(
        "current"
    )

clearE3LIUCodingViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2563)
)
clearE3LIUCodingViolation.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearE3LIUCodingViolation.setStatus(
        "current"
    )

clearE3ConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2565)
)
clearE3ConfigError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearE3ConfigError.setStatus(
        "current"
    )

evntE3TestOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2570)
)
evntE3TestOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntE3TestOff.setStatus(
        "current"
    )

evntE3InService = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2571)
)
evntE3InService.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evntE3InService.setStatus(
        "current"
    )

setContactClosureInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2601)
)
setContactClosureInputAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setContactClosureInputAlarm.setStatus(
        "current"
    )

setContactClosureCfgError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2625)
)
setContactClosureCfgError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setContactClosureCfgError.setStatus(
        "current"
    )

clearContactClosureInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2641)
)
clearContactClosureInputAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearContactClosureInputAlarm.setStatus(
        "current"
    )

clearContactClosureCfgError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2665)
)
clearContactClosureCfgError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearContactClosureCfgError.setStatus(
        "current"
    )

setVoltMeasureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2701)
)
setVoltMeasureAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setVoltMeasureAlarm.setStatus(
        "current"
    )

setVoltMeasureCfgError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2725)
)
setVoltMeasureCfgError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setVoltMeasureCfgError.setStatus(
        "current"
    )

clearVoltMeasureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2741)
)
clearVoltMeasureAlarm.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearVoltMeasureAlarm.setStatus(
        "current"
    )

clearVoltMeasureCfgError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2765)
)
clearVoltMeasureCfgError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearVoltMeasureCfgError.setStatus(
        "current"
    )

setAsyncRxFifoError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2801)
)
setAsyncRxFifoError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setAsyncRxFifoError.setStatus(
        "current"
    )

setAsyncTxFifoError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2802)
)
setAsyncTxFifoError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setAsyncTxFifoError.setStatus(
        "current"
    )

setAsyncOverrunError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2803)
)
setAsyncOverrunError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setAsyncOverrunError.setStatus(
        "current"
    )

setAsyncParityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2804)
)
setAsyncParityError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setAsyncParityError.setStatus(
        "current"
    )

setAsyncFramingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2805)
)
setAsyncFramingError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setAsyncFramingError.setStatus(
        "current"
    )

clearAsyncRxFifoError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2841)
)
clearAsyncRxFifoError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearAsyncRxFifoError.setStatus(
        "current"
    )

clearAsyncTxFifoError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2842)
)
clearAsyncTxFifoError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearAsyncTxFifoError.setStatus(
        "current"
    )

clearAsyncOverrunError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2843)
)
clearAsyncOverrunError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearAsyncOverrunError.setStatus(
        "current"
    )

clearAsyncParityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2844)
)
clearAsyncParityError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearAsyncParityError.setStatus(
        "current"
    )

clearAsyncFramingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2845)
)
clearAsyncFramingError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearAsyncFramingError.setStatus(
        "current"
    )

setTempSensorOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2901)
)
setTempSensorOutOfRange.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setTempSensorOutOfRange.setStatus(
        "current"
    )

clearTempSensorOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 2941)
)
clearTempSensorOutOfRange.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearTempSensorOutOfRange.setStatus(
        "current"
    )

setVWanError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 3001)
)
setVWanError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setVWanError.setStatus(
        "current"
    )

setVWanCfgError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 3025)
)
setVWanCfgError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    setVWanCfgError.setStatus(
        "current"
    )

clearVWanError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 3041)
)
clearVWanError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearVWanError.setStatus(
        "current"
    )

clearVWanCfgError = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 3065)
)
clearVWanCfgError.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clearVWanCfgError.setStatus(
        "current"
    )

set1uPowerSupplyOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 3108)
)
set1uPowerSupplyOffline.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    set1uPowerSupplyOffline.setStatus(
        "current"
    )

set1uPowerSupplyDefective = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 3109)
)
set1uPowerSupplyDefective.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    set1uPowerSupplyDefective.setStatus(
        "current"
    )

set1uPowerSupplyFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 3110)
)
set1uPowerSupplyFanFailure.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    set1uPowerSupplyFanFailure.setStatus(
        "current"
    )

evnt1uPowerSupplyFanOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 3116)
)
evnt1uPowerSupplyFanOn.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evnt1uPowerSupplyFanOn.setStatus(
        "current"
    )

set1uPowerSupplyCircuitMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 3119)
)
set1uPowerSupplyCircuitMissing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    set1uPowerSupplyCircuitMissing.setStatus(
        "current"
    )

set1uPowerSupplyCfgMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 3125)
)
set1uPowerSupplyCfgMismatch.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    set1uPowerSupplyCfgMismatch.setStatus(
        "current"
    )

clear1uPowerSupplyOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 3148)
)
clear1uPowerSupplyOffline.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clear1uPowerSupplyOffline.setStatus(
        "current"
    )

clear1uPowerSupplyDefective = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 3149)
)
clear1uPowerSupplyDefective.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clear1uPowerSupplyDefective.setStatus(
        "current"
    )

clear1uPowerSupplyFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 3150)
)
clear1uPowerSupplyFanFailure.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clear1uPowerSupplyFanFailure.setStatus(
        "current"
    )

evnt1uPowerSupplyFanOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 3156)
)
evnt1uPowerSupplyFanOff.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    evnt1uPowerSupplyFanOff.setStatus(
        "current"
    )

clear1uPowerSupplyCircuitMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 3159)
)
clear1uPowerSupplyCircuitMissing.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clear1uPowerSupplyCircuitMissing.setStatus(
        "current"
    )

clear1uPowerSupplyCfgMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 3165)
)
clear1uPowerSupplyCfgMismatch.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    clear1uPowerSupplyCfgMismatch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERI-DNX-ALARM-TRAP-MIB",
    **{"evntDevColdStart": evntDevColdStart,
       "evntDevWarmStart": evntDevWarmStart,
       "setSlotMismatch": setSlotMismatch,
       "setSlotMissing": setSlotMissing,
       "clearSlotMismatch": clearSlotMismatch,
       "clearSlotMissing": clearSlotMissing,
       "evntDevOnline": evntDevOnline,
       "evntDevStandby": evntDevStandby,
       "setDevFrameSyncNotPresent": setDevFrameSyncNotPresent,
       "setDevSystemClockNotPresent": setDevSystemClockNotPresent,
       "setDevDataBaseNotInsync": setDevDataBaseNotInsync,
       "setDevFreeRunError": setDevFreeRunError,
       "setDevOffline": setDevOffline,
       "setDevDefective": setDevDefective,
       "setDevBusError": setDevBusError,
       "setDevStratum3ClkFailure": setDevStratum3ClkFailure,
       "setDevCircuitCardMissing": setDevCircuitCardMissing,
       "setDevConfigError": setDevConfigError,
       "setDevNoRearCard": setDevNoRearCard,
       "evntDevOutOfService": evntDevOutOfService,
       "evntDevNotOnline": evntDevNotOnline,
       "evntDevNotStandby": evntDevNotStandby,
       "clearDevFrameSyncNotPresent": clearDevFrameSyncNotPresent,
       "clearDevSystemClockNotPresent": clearDevSystemClockNotPresent,
       "clearDevDataBaseNotInsync": clearDevDataBaseNotInsync,
       "clearDevFreeRunError": clearDevFreeRunError,
       "clearDevOffline": clearDevOffline,
       "clearDevDefective": clearDevDefective,
       "clearDevBusError": clearDevBusError,
       "clearDevStratum3ClkFailure": clearDevStratum3ClkFailure,
       "clearDevCircuitCardMissing": clearDevCircuitCardMissing,
       "clearDevConfigError": clearDevConfigError,
       "clearDevNoRearCard": clearDevNoRearCard,
       "evntDevInService": evntDevInService,
       "setT1E1RcvFarEndLOF": setT1E1RcvFarEndLOF,
       "setT1E1NearEndSendLOF": setT1E1NearEndSendLOF,
       "evntT1E1RcvingAIS": evntT1E1RcvingAIS,
       "setT1E1NearEndSendingAIS": setT1E1NearEndSendingAIS,
       "setT1E1NearEndLOF": setT1E1NearEndLOF,
       "setT1E1NearEndLossOfSignal": setT1E1NearEndLossOfSignal,
       "evntT1E1NearEndLooped": evntT1E1NearEndLooped,
       "setT1E1Ts16AIS": setT1E1Ts16AIS,
       "setT1E1FarEndSendingTs16LOMF": setT1E1FarEndSendingTs16LOMF,
       "setT1E1NearEndSendingTs16LOMF": setT1E1NearEndSendingTs16LOMF,
       "setT1E1OtherLineStatus": setT1E1OtherLineStatus,
       "setT1E1NearEndUnavailableSig": setT1E1NearEndUnavailableSig,
       "evntT1E1CarrierEquipOutOfService": evntT1E1CarrierEquipOutOfService,
       "evntE1NationalSa4TxRxSame": evntE1NationalSa4TxRxSame,
       "setT1E1NearEndTxSlip": setT1E1NearEndTxSlip,
       "setT1E1NearEndRxSlip": setT1E1NearEndRxSlip,
       "setT1E1NearEndSeverErroredFrame": setT1E1NearEndSeverErroredFrame,
       "setT1E1ChangeFrameAlignment": setT1E1ChangeFrameAlignment,
       "setT1E1ConfigError": setT1E1ConfigError,
       "evntT1E1InTest": evntT1E1InTest,
       "evntT1E1OutOfService": evntT1E1OutOfService,
       "clearT1E1RcvFarEndLOF": clearT1E1RcvFarEndLOF,
       "clearT1E1NearEndSendLOF": clearT1E1NearEndSendLOF,
       "evntT1E1StoppedRcvingAIS": evntT1E1StoppedRcvingAIS,
       "clearT1E1NearEndSendingAIS": clearT1E1NearEndSendingAIS,
       "clearT1E1NearEndLOF": clearT1E1NearEndLOF,
       "clearT1E1NearEndLossOfSignal": clearT1E1NearEndLossOfSignal,
       "evntT1E1NearEndLoopOff": evntT1E1NearEndLoopOff,
       "clearT1E1Ts16AIS": clearT1E1Ts16AIS,
       "clearT1E1FarEndSendingTs16LOMF": clearT1E1FarEndSendingTs16LOMF,
       "clearT1E1NearEndSendingTs16LOMF": clearT1E1NearEndSendingTs16LOMF,
       "clearT1E1OtherLineStatus": clearT1E1OtherLineStatus,
       "clearT1E1NearEndUnavailableSig": clearT1E1NearEndUnavailableSig,
       "evntT1E1CarrierEquipInService": evntT1E1CarrierEquipInService,
       "evntE1NationalSa4TxRxDiff": evntE1NationalSa4TxRxDiff,
       "clearT1E1NearEndTxSlip": clearT1E1NearEndTxSlip,
       "clearT1E1NearEndRxSlip": clearT1E1NearEndRxSlip,
       "clearT1E1NearEndSeverErroredFrame": clearT1E1NearEndSeverErroredFrame,
       "clearT1E1ChangeFrameAlignment": clearT1E1ChangeFrameAlignment,
       "clearT1E1ConfigError": clearT1E1ConfigError,
       "evntT1E1TestOff": evntT1E1TestOff,
       "evntT1E1InService": evntT1E1InService,
       "setHsRcvFIFOError": setHsRcvFIFOError,
       "setHsXmtFIFOError": setHsXmtFIFOError,
       "setHsClockEdgeError": setHsClockEdgeError,
       "setHsCarrierFailure": setHsCarrierFailure,
       "evntHsNearEndLooped": evntHsNearEndLooped,
       "evntHsNoBtsAssigned": evntHsNoBtsAssigned,
       "setHsConfigError": setHsConfigError,
       "evntHsInTest": evntHsInTest,
       "evntHsOutOfService": evntHsOutOfService,
       "clearHsRcvFIFOError": clearHsRcvFIFOError,
       "clearHsXmtFIFOError": clearHsXmtFIFOError,
       "clearHsClockEdgeError": clearHsClockEdgeError,
       "clearHsCarrierFailure": clearHsCarrierFailure,
       "evntHsNearEndLoopOff": evntHsNearEndLoopOff,
       "evntHsBtsAssigned": evntHsBtsAssigned,
       "clearHsConfigError": clearHsConfigError,
       "evntHsTestOff": evntHsTestOff,
       "evntHsInService": evntHsInService,
       "setT3RcvFarEndLOF": setT3RcvFarEndLOF,
       "setT3NearEndSendLOF": setT3NearEndSendLOF,
       "setT3FarEndSendingAIS": setT3FarEndSendingAIS,
       "setT3NearEndSendingAIS": setT3NearEndSendingAIS,
       "setT3NearEndLOF": setT3NearEndLOF,
       "setT3NearEndLossOfSignal": setT3NearEndLossOfSignal,
       "evntT3NearEndLooped": evntT3NearEndLooped,
       "setT3OtherLineStatus": setT3OtherLineStatus,
       "setT3NearEndUnavailableSig": setT3NearEndUnavailableSig,
       "evntT3CarrierEquipOutOfService": evntT3CarrierEquipOutOfService,
       "setT3NearEndSeverErroredFrame": setT3NearEndSeverErroredFrame,
       "setT3TxRxClockFailure": setT3TxRxClockFailure,
       "setT3FarEndBlockError": setT3FarEndBlockError,
       "setT3PbitCbitParityError": setT3PbitCbitParityError,
       "setT3MbitsInError": setT3MbitsInError,
       "setT3LIUOtherStatus": setT3LIUOtherStatus,
       "setT3LIUExcessZeros": setT3LIUExcessZeros,
       "setT3LIUCodingViolation": setT3LIUCodingViolation,
       "setT3LIUPrbsError": setT3LIUPrbsError,
       "setT3ConfigError": setT3ConfigError,
       "evntT3InTest": evntT3InTest,
       "evntT3OutOfService": evntT3OutOfService,
       "clearT3RcvFarEndLOF": clearT3RcvFarEndLOF,
       "clearT3NearEndSendLOF": clearT3NearEndSendLOF,
       "clearT3FarEndSendingAIS": clearT3FarEndSendingAIS,
       "clearT3NearEndSendingAIS": clearT3NearEndSendingAIS,
       "clearT3NearEndLOF": clearT3NearEndLOF,
       "clearT3NearEndLossOfSignal": clearT3NearEndLossOfSignal,
       "evntT3NearEndLoopOff": evntT3NearEndLoopOff,
       "clearT3OtherLineStatus": clearT3OtherLineStatus,
       "clearT3NearEndUnavailableSig": clearT3NearEndUnavailableSig,
       "evntT3CarrierEquipInService": evntT3CarrierEquipInService,
       "clearT3NearEndSeverErroredFrame": clearT3NearEndSeverErroredFrame,
       "clearT3TxRxClockFailure": clearT3TxRxClockFailure,
       "clearT3FarEndBlockError": clearT3FarEndBlockError,
       "clearT3PbitCbitParityError": clearT3PbitCbitParityError,
       "clearT3MbitsInError": clearT3MbitsInError,
       "clearT3LIUOtherStatus": clearT3LIUOtherStatus,
       "clearT3LIUExcessZeros": clearT3LIUExcessZeros,
       "clearT3LIUCodingViolation": clearT3LIUCodingViolation,
       "clearT3LIUPrbsError": clearT3LIUPrbsError,
       "clearT3ConfigError": clearT3ConfigError,
       "evntT3TestOff": evntT3TestOff,
       "evntT3InService": evntT3InService,
       "setPowerSupplyNotPresent": setPowerSupplyNotPresent,
       "setPowerSupplyProblem": setPowerSupplyProblem,
       "clearPowerSupplyNotPresent": clearPowerSupplyNotPresent,
       "clearPowerSupplyProblem": clearPowerSupplyProblem,
       "setOcuNearEndLOS": setOcuNearEndLOS,
       "setOcuOtherLineStatus": setOcuOtherLineStatus,
       "setOcuNearEndSeverErroredFrame": setOcuNearEndSeverErroredFrame,
       "setOcuConfigError": setOcuConfigError,
       "evntOcuOutOfService": evntOcuOutOfService,
       "clearOcuNearEndLOS": clearOcuNearEndLOS,
       "clearOcuOtherLineStatus": clearOcuOtherLineStatus,
       "clearOcuNearEndSeverErroredFrame": clearOcuNearEndSeverErroredFrame,
       "clearOcuConfigError": clearOcuConfigError,
       "evntOcuInService": evntOcuInService,
       "setTamConfigError": setTamConfigError,
       "evntTamOutOfService": evntTamOutOfService,
       "clearTamConfigError": clearTamConfigError,
       "evntTamInService": evntTamInService,
       "setVoiceConfigError": setVoiceConfigError,
       "evntVoiceOutOfService": evntVoiceOutOfService,
       "clearVoiceConfigError": clearVoiceConfigError,
       "evntVoiceInService": evntVoiceInService,
       "evntPsxDevOnline": evntPsxDevOnline,
       "setPsxPowerSupplyANotOk": setPsxPowerSupplyANotOk,
       "setPsxPowerSupplyBNotOk": setPsxPowerSupplyBNotOk,
       "setPsxFan01NotOk": setPsxFan01NotOk,
       "setPsxFan02NotOk": setPsxFan02NotOk,
       "setPsxFan03NotOk": setPsxFan03NotOk,
       "setPsxDualBroadbandNotSupported": setPsxDualBroadbandNotSupported,
       "evntPsxNewControllerRev": evntPsxNewControllerRev,
       "evntPsxLineCard01Missing": evntPsxLineCard01Missing,
       "evntPsxLineCard02Missing": evntPsxLineCard02Missing,
       "evntPsxLineCard03Missing": evntPsxLineCard03Missing,
       "evntPsxLineCard04Missing": evntPsxLineCard04Missing,
       "evntPsxLineCard05Missing": evntPsxLineCard05Missing,
       "evntPsxLineCard06Missing": evntPsxLineCard06Missing,
       "evntPsxLineCard07Missing": evntPsxLineCard07Missing,
       "evntPsxLineCard08Missing": evntPsxLineCard08Missing,
       "evntPsxLineCard09Missing": evntPsxLineCard09Missing,
       "evntPsxLineCard10Missing": evntPsxLineCard10Missing,
       "evntPsxLineCard11Missing": evntPsxLineCard11Missing,
       "clearPsxPowerSupplyANotOk": clearPsxPowerSupplyANotOk,
       "clearPsxPowerSupplyBNotOk": clearPsxPowerSupplyBNotOk,
       "clearPsxFan01NotOk": clearPsxFan01NotOk,
       "clearPsxFan02NotOk": clearPsxFan02NotOk,
       "clearPsxFan03NotOk": clearPsxFan03NotOk,
       "clearPsxDualBroadbandNotSupported": clearPsxDualBroadbandNotSupported,
       "evntPsxLineCard01Present": evntPsxLineCard01Present,
       "evntPsxLineCard02Present": evntPsxLineCard02Present,
       "evntPsxLineCard03Present": evntPsxLineCard03Present,
       "evntPsxLineCard04Present": evntPsxLineCard04Present,
       "evntPsxLineCard05Present": evntPsxLineCard05Present,
       "evntPsxLineCard06Present": evntPsxLineCard06Present,
       "evntPsxLineCard07Present": evntPsxLineCard07Present,
       "evntPsxLineCard08Present": evntPsxLineCard08Present,
       "evntPsxLineCard09Present": evntPsxLineCard09Present,
       "evntPsxLineCard10Present": evntPsxLineCard10Present,
       "evntPsxLineCard11Present": evntPsxLineCard11Present,
       "setPsxLineCardRelaySwitchToSpare": setPsxLineCardRelaySwitchToSpare,
       "setPsxLineCardCableMissing": setPsxLineCardCableMissing,
       "setPsxLineCardMissing": setPsxLineCardMissing,
       "setPsxLineCardMismatch": setPsxLineCardMismatch,
       "setPsxLineCardRelayMalfunction": setPsxLineCardRelayMalfunction,
       "clearPsxLineCardRelaySwitchToSpare": clearPsxLineCardRelaySwitchToSpare,
       "clearPsxLineCardCableMissing": clearPsxLineCardCableMissing,
       "clearPsxLineCardMissing": clearPsxLineCardMissing,
       "clearPsxLineCardMismatch": clearPsxLineCardMismatch,
       "clearPsxLineCardRelayMalfunction": clearPsxLineCardRelayMalfunction,
       "setRtrUserAlarm1": setRtrUserAlarm1,
       "setRtrUserAlarm2": setRtrUserAlarm2,
       "setRtrUserAlarm3": setRtrUserAlarm3,
       "setRtrConfigError": setRtrConfigError,
       "evntRtrOutOfService": evntRtrOutOfService,
       "clearRtrUserAlarm1": clearRtrUserAlarm1,
       "clearRtrUserAlarm2": clearRtrUserAlarm2,
       "clearRtrUserAlarm3": clearRtrUserAlarm3,
       "clearRtrConfigError": clearRtrConfigError,
       "evntRtrInService": evntRtrInService,
       "setSts1RcvFarEndLOF": setSts1RcvFarEndLOF,
       "setSts1NearEndSendLOF": setSts1NearEndSendLOF,
       "evntSts1RcvingAIS": evntSts1RcvingAIS,
       "setSts1NearEndSendingAIS": setSts1NearEndSendingAIS,
       "setSts1NearEndLOF": setSts1NearEndLOF,
       "evntSts1NearEndLooped": evntSts1NearEndLooped,
       "setSts1NearEndLOP": setSts1NearEndLOP,
       "setSts1NearEndOOF": setSts1NearEndOOF,
       "setSts1NearEndAIS": setSts1NearEndAIS,
       "setSts1OtherLineStatus": setSts1OtherLineStatus,
       "setSts1NearEndUnavailableSig": setSts1NearEndUnavailableSig,
       "evntSts1CarrierEquipOutOfService": evntSts1CarrierEquipOutOfService,
       "setSts1TxRxClockFailure": setSts1TxRxClockFailure,
       "setSts1NearEndLOMF": setSts1NearEndLOMF,
       "setSts1NearEndTraceError": setSts1NearEndTraceError,
       "setSts1LIUDigitalLOS": setSts1LIUDigitalLOS,
       "setSts1LIUAnalogLOS": setSts1LIUAnalogLOS,
       "setSts1LIUExcessZeros": setSts1LIUExcessZeros,
       "setSts1LIUCodingViolation": setSts1LIUCodingViolation,
       "setSts1LIUPrbsError": setSts1LIUPrbsError,
       "setSts1ConfigError": setSts1ConfigError,
       "evntSts1InTest": evntSts1InTest,
       "evntSts1OutOfService": evntSts1OutOfService,
       "clearSts1RcvFarEndLOF": clearSts1RcvFarEndLOF,
       "clearSts1NearEndSendLOF": clearSts1NearEndSendLOF,
       "evntSts1StoppedRcvingAIS": evntSts1StoppedRcvingAIS,
       "clearSts1NearEndSendingAIS": clearSts1NearEndSendingAIS,
       "clearSts1NearEndLOF": clearSts1NearEndLOF,
       "evntSts1NearEndLoopOff": evntSts1NearEndLoopOff,
       "clearSts1NearEndLOP": clearSts1NearEndLOP,
       "clearSts1NearEndOOF": clearSts1NearEndOOF,
       "clearSts1NearEndAIS": clearSts1NearEndAIS,
       "clearSts1OtherLineStatus": clearSts1OtherLineStatus,
       "clearSts1NearEndUnavailableSig": clearSts1NearEndUnavailableSig,
       "evntSts1CarrierEquipInService": evntSts1CarrierEquipInService,
       "clearSts1TxRxClockFailure": clearSts1TxRxClockFailure,
       "clearSts1NearEndLOMF": clearSts1NearEndLOMF,
       "clearSts1NearEndTraceError": clearSts1NearEndTraceError,
       "clearSts1LIUDigitalLOS": clearSts1LIUDigitalLOS,
       "clearSts1LIUAnalogLOS": clearSts1LIUAnalogLOS,
       "clearSts1LIUExcessZeros": clearSts1LIUExcessZeros,
       "clearSts1LIUCodingViolation": clearSts1LIUCodingViolation,
       "clearSts1LIUPrbsError": clearSts1LIUPrbsError,
       "clearSts1ConfigError": clearSts1ConfigError,
       "evntSts1TestOff": evntSts1TestOff,
       "evntSts1InService": evntSts1InService,
       "evntHt3RcvingAIS": evntHt3RcvingAIS,
       "setHt3NearEndSendingAIS": setHt3NearEndSendingAIS,
       "setHt3NearEndOOF": setHt3NearEndOOF,
       "setHt3NearEndLossOfSignal": setHt3NearEndLossOfSignal,
       "evntHt3NearEndLooped": evntHt3NearEndLooped,
       "setHt3NearEndLOF": setHt3NearEndLOF,
       "setHt3FarEndRcvFailure": setHt3FarEndRcvFailure,
       "setHt3NearEndLCVError": setHt3NearEndLCVError,
       "setHt3NearEndFERRError": setHt3NearEndFERRError,
       "setHt3NearEndExcessZeros": setHt3NearEndExcessZeros,
       "evntHt3CarrierEquipOutOfService": evntHt3CarrierEquipOutOfService,
       "setHt3FarEndBlockError": setHt3FarEndBlockError,
       "setHt3PbitCbitParityError": setHt3PbitCbitParityError,
       "setHt3ChangeInFrameAlignment": setHt3ChangeInFrameAlignment,
       "setHt3LIUDigitalLOS": setHt3LIUDigitalLOS,
       "setHt3LIUAnalogLOS": setHt3LIUAnalogLOS,
       "setHt3LIUExcessZeros": setHt3LIUExcessZeros,
       "setHt3LIUCodingViolation": setHt3LIUCodingViolation,
       "setHt3LIUPrbsError": setHt3LIUPrbsError,
       "setHt3ConfigError": setHt3ConfigError,
       "evntHt3InTest": evntHt3InTest,
       "evntHt3OutOfService": evntHt3OutOfService,
       "evntHt3StoppedRcvingAIS": evntHt3StoppedRcvingAIS,
       "clearHt3NearEndSendingAIS": clearHt3NearEndSendingAIS,
       "clearHt3NearEndOOF": clearHt3NearEndOOF,
       "clearHt3NearEndLossOfSignal": clearHt3NearEndLossOfSignal,
       "evntHt3NearEndLoopOff": evntHt3NearEndLoopOff,
       "clearHt3NearEndLOF": clearHt3NearEndLOF,
       "clearHt3FarEndRcvFailure": clearHt3FarEndRcvFailure,
       "clearHt3NearEndLCVError": clearHt3NearEndLCVError,
       "clearHt3NearEndFERRError": clearHt3NearEndFERRError,
       "clearHt3NearEndExcessZeros": clearHt3NearEndExcessZeros,
       "evntHt3CarrierEquipInService": evntHt3CarrierEquipInService,
       "clearHt3FarEndBlockError": clearHt3FarEndBlockError,
       "clearHt3PbitCbitParityError": clearHt3PbitCbitParityError,
       "clearHt3ChangeInFrameAlignment": clearHt3ChangeInFrameAlignment,
       "clearHt3LIUDigitalLOS": clearHt3LIUDigitalLOS,
       "clearHt3LIUAnalogLOS": clearHt3LIUAnalogLOS,
       "clearHt3LIUExcessZeros": clearHt3LIUExcessZeros,
       "clearHt3LIUCodingViolation": clearHt3LIUCodingViolation,
       "clearHt3LIUPrbsError": clearHt3LIUPrbsError,
       "clearHt3ConfigError": clearHt3ConfigError,
       "evntHt3TestOff": evntHt3TestOff,
       "evntHt3InService": evntHt3InService,
       "evntGr303OutOfService": evntGr303OutOfService,
       "evntGr303InService": evntGr303InService,
       "setXlinkCableMismatch": setXlinkCableMismatch,
       "setXlinkSerializerError": setXlinkSerializerError,
       "setXlinkFramerError": setXlinkFramerError,
       "setXlinkBertError": setXlinkBertError,
       "setXlinkClockError": setXlinkClockError,
       "setXlinkInUseError": setXlinkInUseError,
       "setXlinkCrcError": setXlinkCrcError,
       "clearXlinkCableMismatch": clearXlinkCableMismatch,
       "clearXlinkSerializerError": clearXlinkSerializerError,
       "clearXlinkFramerError": clearXlinkFramerError,
       "clearXlinkBertError": clearXlinkBertError,
       "clearXlinkClockError": clearXlinkClockError,
       "clearXlinkInUseError": clearXlinkInUseError,
       "clearXlinkCrcError": clearXlinkCrcError,
       "setNestMismatch": setNestMismatch,
       "setNestMissing": setNestMissing,
       "setNestOffline": setNestOffline,
       "setNestCriticalAlarm": setNestCriticalAlarm,
       "setNestMajorAlarm": setNestMajorAlarm,
       "setNestMinorAlarm": setNestMinorAlarm,
       "setNestSwMismatch": setNestSwMismatch,
       "clearNestMismatch": clearNestMismatch,
       "clearNestMissing": clearNestMissing,
       "clearNestOffline": clearNestOffline,
       "clearNestCriticalAlarm": clearNestCriticalAlarm,
       "clearNestMajorAlarm": clearNestMajorAlarm,
       "clearNestMinorAlarm": clearNestMinorAlarm,
       "clearNestSwMismatch": clearNestSwMismatch,
       "setNodeCriticalAlarm": setNodeCriticalAlarm,
       "setNodeMajorAlarm": setNodeMajorAlarm,
       "setNodeMinorAlarm": setNodeMinorAlarm,
       "clearNodeCriticalAlarm": clearNodeCriticalAlarm,
       "clearNodeMajorAlarm": clearNodeMajorAlarm,
       "clearNodeMinorAlarm": clearNodeMinorAlarm,
       "setDs0DpPortLossOfSignal": setDs0DpPortLossOfSignal,
       "setDs0DpPortBPV": setDs0DpPortBPV,
       "setDs0DpPortConfigError": setDs0DpPortConfigError,
       "evntDs0DpPortInTest": evntDs0DpPortInTest,
       "evntDs0DpPortOutOfService": evntDs0DpPortOutOfService,
       "clearDs0DpPortLossOfSignal": clearDs0DpPortLossOfSignal,
       "clearDs0DpPortBPV": clearDs0DpPortBPV,
       "clearDs0DpPortConfigError": clearDs0DpPortConfigError,
       "evntDs0DpPortTestOff": evntDs0DpPortTestOff,
       "evntDs0DpPortInService": evntDs0DpPortInService,
       "setDs0DpBitsLossOfSignal": setDs0DpBitsLossOfSignal,
       "setDs0DpBitsBPV": setDs0DpBitsBPV,
       "clearDs0DpBitsLossOfSignal": clearDs0DpBitsLossOfSignal,
       "clearDs0DpBitsBPV": clearDs0DpBitsBPV,
       "setOpticalT1E1RedAlarm": setOpticalT1E1RedAlarm,
       "setOpticalT1E1NearEndSendLOF": setOpticalT1E1NearEndSendLOF,
       "evntOpticalT1E1RcvingAIS": evntOpticalT1E1RcvingAIS,
       "setOpticalT1E1NearEndSendingAIS": setOpticalT1E1NearEndSendingAIS,
       "setOpticalT1E1NearEndLOF": setOpticalT1E1NearEndLOF,
       "evntOpticalT1E1NearEndLooped": evntOpticalT1E1NearEndLooped,
       "setOpticalT1E1LossOfPointer": setOpticalT1E1LossOfPointer,
       "setOpticalT1E1OutOfFrame": setOpticalT1E1OutOfFrame,
       "setOpticalT1E1DetectedAIS": setOpticalT1E1DetectedAIS,
       "setOpticalT1E1NearEndLOS": setOpticalT1E1NearEndLOS,
       "evntOpticalE1NationalSa4TxRxSame": evntOpticalE1NationalSa4TxRxSame,
       "setOpticalT1E1RcvFarEndYellow": setOpticalT1E1RcvFarEndYellow,
       "setOpticalT1E1NearEndSEF": setOpticalT1E1NearEndSEF,
       "setOpticalT1E1Tug2LOP": setOpticalT1E1Tug2LOP,
       "setOpticalT1E1Tug2RDI": setOpticalT1E1Tug2RDI,
       "setOpticalT1E1Tug2RFI": setOpticalT1E1Tug2RFI,
       "setOpticalT1E1Tug2AIS": setOpticalT1E1Tug2AIS,
       "setOpticalT1E1Tug2PSLM": setOpticalT1E1Tug2PSLM,
       "setOpticalT1E1Tug2PSLU": setOpticalT1E1Tug2PSLU,
       "setOpticalT1E1ConfigError": setOpticalT1E1ConfigError,
       "evntOpticalT1E1InTest": evntOpticalT1E1InTest,
       "evntOpticalT1E1OutOfService": evntOpticalT1E1OutOfService,
       "clearOpticalT1E1RedAlarm": clearOpticalT1E1RedAlarm,
       "clearOpticalT1E1NearEndSendLOF": clearOpticalT1E1NearEndSendLOF,
       "evntOpticalT1E1StoppedRcvingAIS": evntOpticalT1E1StoppedRcvingAIS,
       "clearOpticalT1E1NearEndSendingAIS": clearOpticalT1E1NearEndSendingAIS,
       "clearOpticalT1E1NearEndLOF": clearOpticalT1E1NearEndLOF,
       "evntOpticalT1E1NearEndLoopOff": evntOpticalT1E1NearEndLoopOff,
       "clearOpticalT1E1LossOfPointer": clearOpticalT1E1LossOfPointer,
       "clearOpticalT1E1OutOfFrame": clearOpticalT1E1OutOfFrame,
       "clearOpticalT1E1DetectedAIS": clearOpticalT1E1DetectedAIS,
       "clearOpticalT1E1NearEndLOS": clearOpticalT1E1NearEndLOS,
       "evntOpticalE1NationalSa4TxRxDiff": evntOpticalE1NationalSa4TxRxDiff,
       "clearOpticalT1E1RcvFarEndYellow": clearOpticalT1E1RcvFarEndYellow,
       "clearOpticalT1E1NearEndSEF": clearOpticalT1E1NearEndSEF,
       "clearOpticalT1E1Tug2LOP": clearOpticalT1E1Tug2LOP,
       "clearOpticalT1E1Tug2RDI": clearOpticalT1E1Tug2RDI,
       "clearOpticalT1E1Tug2RFI": clearOpticalT1E1Tug2RFI,
       "clearOpticalT1E1Tug2AIS": clearOpticalT1E1Tug2AIS,
       "clearOpticalT1E1Tug2PSLM": clearOpticalT1E1Tug2PSLM,
       "clearOpticalT1E1Tug2PSLU": clearOpticalT1E1Tug2PSLU,
       "clearOpticalT1E1ConfigError": clearOpticalT1E1ConfigError,
       "evntOpticalT1E1TestOff": evntOpticalT1E1TestOff,
       "evntOpticalT1E1InService": evntOpticalT1E1InService,
       "setVtNearEndLOP": setVtNearEndLOP,
       "setVtNearEndAIS": setVtNearEndAIS,
       "setPayloadPathLOP": setPayloadPathLOP,
       "setPayloadPathAIS": setPayloadPathAIS,
       "setPayloadPathRDI": setPayloadPathRDI,
       "evntPayloadNearEndLineLooped": evntPayloadNearEndLineLooped,
       "evntPayloadNearEndLocalLooped": evntPayloadNearEndLocalLooped,
       "evntPayloadInTest": evntPayloadInTest,
       "clearVtNearEndLOP": clearVtNearEndLOP,
       "clearVtNearEndAIS": clearVtNearEndAIS,
       "clearPayloadPathLOP": clearPayloadPathLOP,
       "clearPayloadPathAIS": clearPayloadPathAIS,
       "clearPayloadPathRDI": clearPayloadPathRDI,
       "evntPayloadNearEndLineLoopOff": evntPayloadNearEndLineLoopOff,
       "evntPayloadNearEndLocalLoopOff": evntPayloadNearEndLocalLoopOff,
       "evntPayloadTestOff": evntPayloadTestOff,
       "setTransOverheadAIS": setTransOverheadAIS,
       "setTransOverheadRDI": setTransOverheadRDI,
       "setTransOverheadOOF": setTransOverheadOOF,
       "setTransOverheadLOF": setTransOverheadLOF,
       "setTransOverheadLOS": setTransOverheadLOS,
       "evntTransOverheadNearEndSysLineLooped": evntTransOverheadNearEndSysLineLooped,
       "evntTransOverheadNearEndPathLineLooped": evntTransOverheadNearEndPathLineLooped,
       "evntTransOverheadNearEndLocalLooped": evntTransOverheadNearEndLocalLooped,
       "setTransOverheadSfDetect": setTransOverheadSfDetect,
       "setTransOverheadSdDetect": setTransOverheadSdDetect,
       "setTransOverheadDetectLaserOffDetect": setTransOverheadDetectLaserOffDetect,
       "evntTransOverheadInTest": evntTransOverheadInTest,
       "clearTransOverheadAIS": clearTransOverheadAIS,
       "clearTransOverheadRDI": clearTransOverheadRDI,
       "clearTransOverheadOOF": clearTransOverheadOOF,
       "clearTransOverheadLOF": clearTransOverheadLOF,
       "clearTransOverheadLOS": clearTransOverheadLOS,
       "evntTransOverheadNearEndSysLineLoopOff": evntTransOverheadNearEndSysLineLoopOff,
       "evntTransOverheadNearEndPathLineLoopOff": evntTransOverheadNearEndPathLineLoopOff,
       "evntTransOverheadNearEndLocalLoopOff": evntTransOverheadNearEndLocalLoopOff,
       "clearTransOverheadSfDetect": clearTransOverheadSfDetect,
       "clearTransOverheadSdDetect": clearTransOverheadSdDetect,
       "clearTransOverheadLaserOffDetect": clearTransOverheadLaserOffDetect,
       "evntTransOverheadTestOff": evntTransOverheadTestOff,
       "setE3RcvFarEndLOF": setE3RcvFarEndLOF,
       "setE3NearEndSendLOF": setE3NearEndSendLOF,
       "evntE3RcvingAIS": evntE3RcvingAIS,
       "setE3NearEndSendingAIS": setE3NearEndSendingAIS,
       "setE3NearEndLOF": setE3NearEndLOF,
       "setE3NearEndLossOfSignal": setE3NearEndLossOfSignal,
       "evntE3NearEndLooped": evntE3NearEndLooped,
       "setE3OtherLineStatus": setE3OtherLineStatus,
       "setE3NearEndUnavailableSig": setE3NearEndUnavailableSig,
       "evntE3CarrierEquipOutOfService": evntE3CarrierEquipOutOfService,
       "setE3NearEndSeverErroredFrame": setE3NearEndSeverErroredFrame,
       "setE3TxRxClockFailure": setE3TxRxClockFailure,
       "setE3FarEndBlockError": setE3FarEndBlockError,
       "setE3MbitsInError": setE3MbitsInError,
       "setE3LIUOtherStatus": setE3LIUOtherStatus,
       "setE3LIUCodingViolation": setE3LIUCodingViolation,
       "setE3ConfigError": setE3ConfigError,
       "evntE3InTest": evntE3InTest,
       "evntE3OutOfService": evntE3OutOfService,
       "clearE3RcvFarEndLOF": clearE3RcvFarEndLOF,
       "clearE3NearEndSendLOF": clearE3NearEndSendLOF,
       "evntE3StoppedRcvingAIS": evntE3StoppedRcvingAIS,
       "clearE3NearEndSendingAIS": clearE3NearEndSendingAIS,
       "clearE3NearEndLOF": clearE3NearEndLOF,
       "clearE3NearEndLossOfSignal": clearE3NearEndLossOfSignal,
       "evntE3NearEndLoopOff": evntE3NearEndLoopOff,
       "clearE3OtherLineStatus": clearE3OtherLineStatus,
       "clearE3NearEndUnavailableSig": clearE3NearEndUnavailableSig,
       "evntE3CarrierEquipInService": evntE3CarrierEquipInService,
       "clearE3NearEndSeverErroredFrame": clearE3NearEndSeverErroredFrame,
       "clearE3TxRxClockFailure": clearE3TxRxClockFailure,
       "clearE3FarEndBlockError": clearE3FarEndBlockError,
       "clearE3MbitsInError": clearE3MbitsInError,
       "clearE3LIUOtherStatus": clearE3LIUOtherStatus,
       "clearE3LIUCodingViolation": clearE3LIUCodingViolation,
       "clearE3ConfigError": clearE3ConfigError,
       "evntE3TestOff": evntE3TestOff,
       "evntE3InService": evntE3InService,
       "setContactClosureInputAlarm": setContactClosureInputAlarm,
       "setContactClosureCfgError": setContactClosureCfgError,
       "clearContactClosureInputAlarm": clearContactClosureInputAlarm,
       "clearContactClosureCfgError": clearContactClosureCfgError,
       "setVoltMeasureAlarm": setVoltMeasureAlarm,
       "setVoltMeasureCfgError": setVoltMeasureCfgError,
       "clearVoltMeasureAlarm": clearVoltMeasureAlarm,
       "clearVoltMeasureCfgError": clearVoltMeasureCfgError,
       "setAsyncRxFifoError": setAsyncRxFifoError,
       "setAsyncTxFifoError": setAsyncTxFifoError,
       "setAsyncOverrunError": setAsyncOverrunError,
       "setAsyncParityError": setAsyncParityError,
       "setAsyncFramingError": setAsyncFramingError,
       "clearAsyncRxFifoError": clearAsyncRxFifoError,
       "clearAsyncTxFifoError": clearAsyncTxFifoError,
       "clearAsyncOverrunError": clearAsyncOverrunError,
       "clearAsyncParityError": clearAsyncParityError,
       "clearAsyncFramingError": clearAsyncFramingError,
       "setTempSensorOutOfRange": setTempSensorOutOfRange,
       "clearTempSensorOutOfRange": clearTempSensorOutOfRange,
       "setVWanError": setVWanError,
       "setVWanCfgError": setVWanCfgError,
       "clearVWanError": clearVWanError,
       "clearVWanCfgError": clearVWanCfgError,
       "set1uPowerSupplyOffline": set1uPowerSupplyOffline,
       "set1uPowerSupplyDefective": set1uPowerSupplyDefective,
       "set1uPowerSupplyFanFailure": set1uPowerSupplyFanFailure,
       "evnt1uPowerSupplyFanOn": evnt1uPowerSupplyFanOn,
       "set1uPowerSupplyCircuitMissing": set1uPowerSupplyCircuitMissing,
       "set1uPowerSupplyCfgMismatch": set1uPowerSupplyCfgMismatch,
       "clear1uPowerSupplyOffline": clear1uPowerSupplyOffline,
       "clear1uPowerSupplyDefective": clear1uPowerSupplyDefective,
       "clear1uPowerSupplyFanFailure": clear1uPowerSupplyFanFailure,
       "evnt1uPowerSupplyFanOff": evnt1uPowerSupplyFanOff,
       "clear1uPowerSupplyCircuitMissing": clear1uPowerSupplyCircuitMissing,
       "clear1uPowerSupplyCfgMismatch": clear1uPowerSupplyCfgMismatch,
       "eriDNXAlarmTrapMIB": eriDNXAlarmTrapMIB}
)
