# SNMP MIB module (APDD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APDD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:13 2024
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

(ApTransportType,) = mibBuilder.importSymbols(
    "ACMEPACKET-TC",
    "ApTransportType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

apDDModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApDDMIBObjects_ObjectIdentity = ObjectIdentity
apDDMIBObjects = _ApDDMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1)
)
_ApDDMIBGeneralObjects_ObjectIdentity = ObjectIdentity
apDDMIBGeneralObjects = _ApDDMIBGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1)
)
_ApDdInterfaceNumber_Type = Integer32
_ApDdInterfaceNumber_Object = MibScalar
apDdInterfaceNumber = _ApDdInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 1),
    _ApDdInterfaceNumber_Type()
)
apDdInterfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdInterfaceNumber.setStatus("current")
_ApDdCurrentTransRate_Type = Gauge32
_ApDdCurrentTransRate_Object = MibScalar
apDdCurrentTransRate = _ApDdCurrentTransRate_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 2),
    _ApDdCurrentTransRate_Type()
)
apDdCurrentTransRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdCurrentTransRate.setStatus("current")
if mibBuilder.loadTexts:
    apDdCurrentTransRate.setUnits("per10Seconds")
_ApDdHighTransRate_Type = Gauge32
_ApDdHighTransRate_Object = MibScalar
apDdHighTransRate = _ApDdHighTransRate_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 3),
    _ApDdHighTransRate_Type()
)
apDdHighTransRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdHighTransRate.setStatus("current")
if mibBuilder.loadTexts:
    apDdHighTransRate.setUnits("per10Seconds")
_ApDdLowTransRate_Type = Gauge32
_ApDdLowTransRate_Object = MibScalar
apDdLowTransRate = _ApDdLowTransRate_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 4),
    _ApDdLowTransRate_Type()
)
apDdLowTransRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdLowTransRate.setStatus("current")
if mibBuilder.loadTexts:
    apDdLowTransRate.setUnits("per10Seconds")
_ApDdAgentNumber_Type = Integer32
_ApDdAgentNumber_Object = MibScalar
apDdAgentNumber = _ApDdAgentNumber_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 5),
    _ApDdAgentNumber_Type()
)
apDdAgentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentNumber.setStatus("current")
_ApDdSessionPeriodActive_Type = Integer32
_ApDdSessionPeriodActive_Object = MibScalar
apDdSessionPeriodActive = _ApDdSessionPeriodActive_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 6),
    _ApDdSessionPeriodActive_Type()
)
apDdSessionPeriodActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessionPeriodActive.setStatus("current")
_ApDdSessionPeriodHigh_Type = Integer32
_ApDdSessionPeriodHigh_Object = MibScalar
apDdSessionPeriodHigh = _ApDdSessionPeriodHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 7),
    _ApDdSessionPeriodHigh_Type()
)
apDdSessionPeriodHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessionPeriodHigh.setStatus("current")
_ApDdSessionPeriodTotal_Type = Integer32
_ApDdSessionPeriodTotal_Object = MibScalar
apDdSessionPeriodTotal = _ApDdSessionPeriodTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 8),
    _ApDdSessionPeriodTotal_Type()
)
apDdSessionPeriodTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessionPeriodTotal.setStatus("current")
_ApDdSessionLifeTotal_Type = Integer32
_ApDdSessionLifeTotal_Object = MibScalar
apDdSessionLifeTotal = _ApDdSessionLifeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 9),
    _ApDdSessionLifeTotal_Type()
)
apDdSessionLifeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessionLifeTotal.setStatus("current")
_ApDdSessionLifePerMax_Type = Integer32
_ApDdSessionLifePerMax_Object = MibScalar
apDdSessionLifePerMax = _ApDdSessionLifePerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 10),
    _ApDdSessionLifePerMax_Type()
)
apDdSessionLifePerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessionLifePerMax.setStatus("current")
_ApDdSessionLifeHigh_Type = Integer32
_ApDdSessionLifeHigh_Object = MibScalar
apDdSessionLifeHigh = _ApDdSessionLifeHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 11),
    _ApDdSessionLifeHigh_Type()
)
apDdSessionLifeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessionLifeHigh.setStatus("current")
_ApDdSessInitPeriodActive_Type = Integer32
_ApDdSessInitPeriodActive_Object = MibScalar
apDdSessInitPeriodActive = _ApDdSessInitPeriodActive_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 12),
    _ApDdSessInitPeriodActive_Type()
)
apDdSessInitPeriodActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessInitPeriodActive.setStatus("current")
_ApDdSessInitPeriodHigh_Type = Integer32
_ApDdSessInitPeriodHigh_Object = MibScalar
apDdSessInitPeriodHigh = _ApDdSessInitPeriodHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 13),
    _ApDdSessInitPeriodHigh_Type()
)
apDdSessInitPeriodHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessInitPeriodHigh.setStatus("current")
_ApDdSessInitPeriodTotal_Type = Integer32
_ApDdSessInitPeriodTotal_Object = MibScalar
apDdSessInitPeriodTotal = _ApDdSessInitPeriodTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 14),
    _ApDdSessInitPeriodTotal_Type()
)
apDdSessInitPeriodTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessInitPeriodTotal.setStatus("current")
_ApDdSessInitLifeTotal_Type = Integer32
_ApDdSessInitLifeTotal_Object = MibScalar
apDdSessInitLifeTotal = _ApDdSessInitLifeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 15),
    _ApDdSessInitLifeTotal_Type()
)
apDdSessInitLifeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessInitLifeTotal.setStatus("current")
_ApDdSessInitLifePerMax_Type = Integer32
_ApDdSessInitLifePerMax_Object = MibScalar
apDdSessInitLifePerMax = _ApDdSessInitLifePerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 16),
    _ApDdSessInitLifePerMax_Type()
)
apDdSessInitLifePerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessInitLifePerMax.setStatus("current")
_ApDdSessInitLifeHigh_Type = Integer32
_ApDdSessInitLifeHigh_Object = MibScalar
apDdSessInitLifeHigh = _ApDdSessInitLifeHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 17),
    _ApDdSessInitLifeHigh_Type()
)
apDdSessInitLifeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessInitLifeHigh.setStatus("current")
_ApDdSessEstablishedPeriodActive_Type = Integer32
_ApDdSessEstablishedPeriodActive_Object = MibScalar
apDdSessEstablishedPeriodActive = _ApDdSessEstablishedPeriodActive_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 18),
    _ApDdSessEstablishedPeriodActive_Type()
)
apDdSessEstablishedPeriodActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessEstablishedPeriodActive.setStatus("current")
_ApDdSessEstablishedPeriodHigh_Type = Integer32
_ApDdSessEstablishedPeriodHigh_Object = MibScalar
apDdSessEstablishedPeriodHigh = _ApDdSessEstablishedPeriodHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 19),
    _ApDdSessEstablishedPeriodHigh_Type()
)
apDdSessEstablishedPeriodHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessEstablishedPeriodHigh.setStatus("current")
_ApDdSessEstablishedPeriodTotal_Type = Integer32
_ApDdSessEstablishedPeriodTotal_Object = MibScalar
apDdSessEstablishedPeriodTotal = _ApDdSessEstablishedPeriodTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 20),
    _ApDdSessEstablishedPeriodTotal_Type()
)
apDdSessEstablishedPeriodTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessEstablishedPeriodTotal.setStatus("current")
_ApDdSessEstablishedLifeTotal_Type = Integer32
_ApDdSessEstablishedLifeTotal_Object = MibScalar
apDdSessEstablishedLifeTotal = _ApDdSessEstablishedLifeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 21),
    _ApDdSessEstablishedLifeTotal_Type()
)
apDdSessEstablishedLifeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessEstablishedLifeTotal.setStatus("current")
_ApDdSessEstablishedLifePerMax_Type = Integer32
_ApDdSessEstablishedLifePerMax_Object = MibScalar
apDdSessEstablishedLifePerMax = _ApDdSessEstablishedLifePerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 22),
    _ApDdSessEstablishedLifePerMax_Type()
)
apDdSessEstablishedLifePerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessEstablishedLifePerMax.setStatus("current")
_ApDdSessEstablishedLifeHigh_Type = Integer32
_ApDdSessEstablishedLifeHigh_Object = MibScalar
apDdSessEstablishedLifeHigh = _ApDdSessEstablishedLifeHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 23),
    _ApDdSessEstablishedLifeHigh_Type()
)
apDdSessEstablishedLifeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessEstablishedLifeHigh.setStatus("current")
_ApDdSessTerminatedPeriodActive_Type = Integer32
_ApDdSessTerminatedPeriodActive_Object = MibScalar
apDdSessTerminatedPeriodActive = _ApDdSessTerminatedPeriodActive_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 24),
    _ApDdSessTerminatedPeriodActive_Type()
)
apDdSessTerminatedPeriodActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessTerminatedPeriodActive.setStatus("current")
_ApDdSessTerminatedPeriodHigh_Type = Integer32
_ApDdSessTerminatedPeriodHigh_Object = MibScalar
apDdSessTerminatedPeriodHigh = _ApDdSessTerminatedPeriodHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 25),
    _ApDdSessTerminatedPeriodHigh_Type()
)
apDdSessTerminatedPeriodHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessTerminatedPeriodHigh.setStatus("current")
_ApDdSessTerminatedPeriodTotal_Type = Integer32
_ApDdSessTerminatedPeriodTotal_Object = MibScalar
apDdSessTerminatedPeriodTotal = _ApDdSessTerminatedPeriodTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 26),
    _ApDdSessTerminatedPeriodTotal_Type()
)
apDdSessTerminatedPeriodTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessTerminatedPeriodTotal.setStatus("current")
_ApDdSessTerminatedLifeTotal_Type = Integer32
_ApDdSessTerminatedLifeTotal_Object = MibScalar
apDdSessTerminatedLifeTotal = _ApDdSessTerminatedLifeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 27),
    _ApDdSessTerminatedLifeTotal_Type()
)
apDdSessTerminatedLifeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessTerminatedLifeTotal.setStatus("current")
_ApDdSessTerminatedLifePerMax_Type = Integer32
_ApDdSessTerminatedLifePerMax_Object = MibScalar
apDdSessTerminatedLifePerMax = _ApDdSessTerminatedLifePerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 28),
    _ApDdSessTerminatedLifePerMax_Type()
)
apDdSessTerminatedLifePerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessTerminatedLifePerMax.setStatus("current")
_ApDdSessTerminatedLifeHigh_Type = Integer32
_ApDdSessTerminatedLifeHigh_Object = MibScalar
apDdSessTerminatedLifeHigh = _ApDdSessTerminatedLifeHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 29),
    _ApDdSessTerminatedLifeHigh_Type()
)
apDdSessTerminatedLifeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessTerminatedLifeHigh.setStatus("current")
_ApDdSessTimeoutPeriodTotal_Type = Integer32
_ApDdSessTimeoutPeriodTotal_Object = MibScalar
apDdSessTimeoutPeriodTotal = _ApDdSessTimeoutPeriodTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 30),
    _ApDdSessTimeoutPeriodTotal_Type()
)
apDdSessTimeoutPeriodTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessTimeoutPeriodTotal.setStatus("current")
_ApDdSessTimeoutLifeTotal_Type = Integer32
_ApDdSessTimeoutLifeTotal_Object = MibScalar
apDdSessTimeoutLifeTotal = _ApDdSessTimeoutLifeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 31),
    _ApDdSessTimeoutLifeTotal_Type()
)
apDdSessTimeoutLifeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessTimeoutLifeTotal.setStatus("current")
_ApDdSessTimeoutLifePerMax_Type = Integer32
_ApDdSessTimeoutLifePerMax_Object = MibScalar
apDdSessTimeoutLifePerMax = _ApDdSessTimeoutLifePerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 32),
    _ApDdSessTimeoutLifePerMax_Type()
)
apDdSessTimeoutLifePerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessTimeoutLifePerMax.setStatus("current")
_ApDdSessErrorsPeriodTotal_Type = Integer32
_ApDdSessErrorsPeriodTotal_Object = MibScalar
apDdSessErrorsPeriodTotal = _ApDdSessErrorsPeriodTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 33),
    _ApDdSessErrorsPeriodTotal_Type()
)
apDdSessErrorsPeriodTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessErrorsPeriodTotal.setStatus("current")
_ApDdSessErrorsLifeTotal_Type = Integer32
_ApDdSessErrorsLifeTotal_Object = MibScalar
apDdSessErrorsLifeTotal = _ApDdSessErrorsLifeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 34),
    _ApDdSessErrorsLifeTotal_Type()
)
apDdSessErrorsLifeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessErrorsLifeTotal.setStatus("current")
_ApDdSessErrorsLifePerMax_Type = Integer32
_ApDdSessErrorsLifePerMax_Object = MibScalar
apDdSessErrorsLifePerMax = _ApDdSessErrorsLifePerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 35),
    _ApDdSessErrorsLifePerMax_Type()
)
apDdSessErrorsLifePerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessErrorsLifePerMax.setStatus("current")
_ApDdSessMissPeriodTotal_Type = Integer32
_ApDdSessMissPeriodTotal_Object = MibScalar
apDdSessMissPeriodTotal = _ApDdSessMissPeriodTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 36),
    _ApDdSessMissPeriodTotal_Type()
)
apDdSessMissPeriodTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessMissPeriodTotal.setStatus("current")
_ApDdSessMissLifeTotal_Type = Integer32
_ApDdSessMissLifeTotal_Object = MibScalar
apDdSessMissLifeTotal = _ApDdSessMissLifeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 37),
    _ApDdSessMissLifeTotal_Type()
)
apDdSessMissLifeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessMissLifeTotal.setStatus("current")
_ApDdSessMissLifePerMax_Type = Integer32
_ApDdSessMissLifePerMax_Object = MibScalar
apDdSessMissLifePerMax = _ApDdSessMissLifePerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 38),
    _ApDdSessMissLifePerMax_Type()
)
apDdSessMissLifePerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSessMissLifePerMax.setStatus("current")
_ApDdSubscriberPeriodActive_Type = Integer32
_ApDdSubscriberPeriodActive_Object = MibScalar
apDdSubscriberPeriodActive = _ApDdSubscriberPeriodActive_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 100),
    _ApDdSubscriberPeriodActive_Type()
)
apDdSubscriberPeriodActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSubscriberPeriodActive.setStatus("current")
_ApDdSubscriberPeriodHigh_Type = Integer32
_ApDdSubscriberPeriodHigh_Object = MibScalar
apDdSubscriberPeriodHigh = _ApDdSubscriberPeriodHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 101),
    _ApDdSubscriberPeriodHigh_Type()
)
apDdSubscriberPeriodHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSubscriberPeriodHigh.setStatus("current")
_ApDdSubscriberPeriodTotal_Type = Integer32
_ApDdSubscriberPeriodTotal_Object = MibScalar
apDdSubscriberPeriodTotal = _ApDdSubscriberPeriodTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 102),
    _ApDdSubscriberPeriodTotal_Type()
)
apDdSubscriberPeriodTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSubscriberPeriodTotal.setStatus("current")
_ApDdSubscriberLifeTotal_Type = Integer32
_ApDdSubscriberLifeTotal_Object = MibScalar
apDdSubscriberLifeTotal = _ApDdSubscriberLifeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 103),
    _ApDdSubscriberLifeTotal_Type()
)
apDdSubscriberLifeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSubscriberLifeTotal.setStatus("current")
_ApDdSubscriberLifePerMax_Type = Integer32
_ApDdSubscriberLifePerMax_Object = MibScalar
apDdSubscriberLifePerMax = _ApDdSubscriberLifePerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 104),
    _ApDdSubscriberLifePerMax_Type()
)
apDdSubscriberLifePerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSubscriberLifePerMax.setStatus("current")
_ApDdSubscriberLifeHigh_Type = Integer32
_ApDdSubscriberLifeHigh_Object = MibScalar
apDdSubscriberLifeHigh = _ApDdSubscriberLifeHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 105),
    _ApDdSubscriberLifeHigh_Type()
)
apDdSubscriberLifeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSubscriberLifeHigh.setStatus("current")
_ApDdSubscribePeriodActive_Type = Integer32
_ApDdSubscribePeriodActive_Object = MibScalar
apDdSubscribePeriodActive = _ApDdSubscribePeriodActive_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 106),
    _ApDdSubscribePeriodActive_Type()
)
apDdSubscribePeriodActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSubscribePeriodActive.setStatus("current")
_ApDdSubscribePeriodHigh_Type = Integer32
_ApDdSubscribePeriodHigh_Object = MibScalar
apDdSubscribePeriodHigh = _ApDdSubscribePeriodHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 107),
    _ApDdSubscribePeriodHigh_Type()
)
apDdSubscribePeriodHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSubscribePeriodHigh.setStatus("current")
_ApDdSubscribePeriodTotal_Type = Integer32
_ApDdSubscribePeriodTotal_Object = MibScalar
apDdSubscribePeriodTotal = _ApDdSubscribePeriodTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 108),
    _ApDdSubscribePeriodTotal_Type()
)
apDdSubscribePeriodTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSubscribePeriodTotal.setStatus("current")
_ApDdSubscribeLifeTotal_Type = Integer32
_ApDdSubscribeLifeTotal_Object = MibScalar
apDdSubscribeLifeTotal = _ApDdSubscribeLifeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 109),
    _ApDdSubscribeLifeTotal_Type()
)
apDdSubscribeLifeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSubscribeLifeTotal.setStatus("current")
_ApDdSubscribeLifePerMax_Type = Integer32
_ApDdSubscribeLifePerMax_Object = MibScalar
apDdSubscribeLifePerMax = _ApDdSubscribeLifePerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 110),
    _ApDdSubscribeLifePerMax_Type()
)
apDdSubscribeLifePerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSubscribeLifePerMax.setStatus("current")
_ApDdSubscribeLifeHigh_Type = Integer32
_ApDdSubscribeLifeHigh_Object = MibScalar
apDdSubscribeLifeHigh = _ApDdSubscribeLifeHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 111),
    _ApDdSubscribeLifeHigh_Type()
)
apDdSubscribeLifeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSubscribeLifeHigh.setStatus("current")
_ApDdUnsubscribePeriodActive_Type = Integer32
_ApDdUnsubscribePeriodActive_Object = MibScalar
apDdUnsubscribePeriodActive = _ApDdUnsubscribePeriodActive_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 112),
    _ApDdUnsubscribePeriodActive_Type()
)
apDdUnsubscribePeriodActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdUnsubscribePeriodActive.setStatus("current")
_ApDdUnsubscribePeriodHigh_Type = Integer32
_ApDdUnsubscribePeriodHigh_Object = MibScalar
apDdUnsubscribePeriodHigh = _ApDdUnsubscribePeriodHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 113),
    _ApDdUnsubscribePeriodHigh_Type()
)
apDdUnsubscribePeriodHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdUnsubscribePeriodHigh.setStatus("current")
_ApDdUnsubscribePeriodTotal_Type = Integer32
_ApDdUnsubscribePeriodTotal_Object = MibScalar
apDdUnsubscribePeriodTotal = _ApDdUnsubscribePeriodTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 114),
    _ApDdUnsubscribePeriodTotal_Type()
)
apDdUnsubscribePeriodTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdUnsubscribePeriodTotal.setStatus("current")
_ApDdUnsubscribeLifeTotal_Type = Integer32
_ApDdUnsubscribeLifeTotal_Object = MibScalar
apDdUnsubscribeLifeTotal = _ApDdUnsubscribeLifeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 115),
    _ApDdUnsubscribeLifeTotal_Type()
)
apDdUnsubscribeLifeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdUnsubscribeLifeTotal.setStatus("current")
_ApDdUnsubscribeLifePerMax_Type = Integer32
_ApDdUnsubscribeLifePerMax_Object = MibScalar
apDdUnsubscribeLifePerMax = _ApDdUnsubscribeLifePerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 116),
    _ApDdUnsubscribeLifePerMax_Type()
)
apDdUnsubscribeLifePerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdUnsubscribeLifePerMax.setStatus("current")
_ApDdUnsubscribeLifeHigh_Type = Integer32
_ApDdUnsubscribeLifeHigh_Object = MibScalar
apDdUnsubscribeLifeHigh = _ApDdUnsubscribeLifeHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 117),
    _ApDdUnsubscribeLifeHigh_Type()
)
apDdUnsubscribeLifeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdUnsubscribeLifeHigh.setStatus("current")
_ApDdPolicyHitPeriodActive_Type = Integer32
_ApDdPolicyHitPeriodActive_Object = MibScalar
apDdPolicyHitPeriodActive = _ApDdPolicyHitPeriodActive_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 118),
    _ApDdPolicyHitPeriodActive_Type()
)
apDdPolicyHitPeriodActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdPolicyHitPeriodActive.setStatus("current")
_ApDdPolicyHitPeriodHigh_Type = Integer32
_ApDdPolicyHitPeriodHigh_Object = MibScalar
apDdPolicyHitPeriodHigh = _ApDdPolicyHitPeriodHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 119),
    _ApDdPolicyHitPeriodHigh_Type()
)
apDdPolicyHitPeriodHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdPolicyHitPeriodHigh.setStatus("current")
_ApDdPolicyHitPeriodTotal_Type = Integer32
_ApDdPolicyHitPeriodTotal_Object = MibScalar
apDdPolicyHitPeriodTotal = _ApDdPolicyHitPeriodTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 120),
    _ApDdPolicyHitPeriodTotal_Type()
)
apDdPolicyHitPeriodTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdPolicyHitPeriodTotal.setStatus("current")
_ApDdPolicyHitLifeTotal_Type = Integer32
_ApDdPolicyHitLifeTotal_Object = MibScalar
apDdPolicyHitLifeTotal = _ApDdPolicyHitLifeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 121),
    _ApDdPolicyHitLifeTotal_Type()
)
apDdPolicyHitLifeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdPolicyHitLifeTotal.setStatus("current")
_ApDdPolicyHitLifePerMax_Type = Integer32
_ApDdPolicyHitLifePerMax_Object = MibScalar
apDdPolicyHitLifePerMax = _ApDdPolicyHitLifePerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 122),
    _ApDdPolicyHitLifePerMax_Type()
)
apDdPolicyHitLifePerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdPolicyHitLifePerMax.setStatus("current")
_ApDdPolicyHitLifeHigh_Type = Integer32
_ApDdPolicyHitLifeHigh_Object = MibScalar
apDdPolicyHitLifeHigh = _ApDdPolicyHitLifeHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 123),
    _ApDdPolicyHitLifeHigh_Type()
)
apDdPolicyHitLifeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdPolicyHitLifeHigh.setStatus("current")
_ApDdPolicyMissPeriodActive_Type = Integer32
_ApDdPolicyMissPeriodActive_Object = MibScalar
apDdPolicyMissPeriodActive = _ApDdPolicyMissPeriodActive_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 124),
    _ApDdPolicyMissPeriodActive_Type()
)
apDdPolicyMissPeriodActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdPolicyMissPeriodActive.setStatus("current")
_ApDdPolicyMissPeriodHigh_Type = Integer32
_ApDdPolicyMissPeriodHigh_Object = MibScalar
apDdPolicyMissPeriodHigh = _ApDdPolicyMissPeriodHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 125),
    _ApDdPolicyMissPeriodHigh_Type()
)
apDdPolicyMissPeriodHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdPolicyMissPeriodHigh.setStatus("current")
_ApDdPolicyMissPeriodTotal_Type = Integer32
_ApDdPolicyMissPeriodTotal_Object = MibScalar
apDdPolicyMissPeriodTotal = _ApDdPolicyMissPeriodTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 126),
    _ApDdPolicyMissPeriodTotal_Type()
)
apDdPolicyMissPeriodTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdPolicyMissPeriodTotal.setStatus("current")
_ApDdPolicyMissLifeTotal_Type = Integer32
_ApDdPolicyMissLifeTotal_Object = MibScalar
apDdPolicyMissLifeTotal = _ApDdPolicyMissLifeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 127),
    _ApDdPolicyMissLifeTotal_Type()
)
apDdPolicyMissLifeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdPolicyMissLifeTotal.setStatus("current")
_ApDdPolicyMissLifePerMax_Type = Integer32
_ApDdPolicyMissLifePerMax_Object = MibScalar
apDdPolicyMissLifePerMax = _ApDdPolicyMissLifePerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 128),
    _ApDdPolicyMissLifePerMax_Type()
)
apDdPolicyMissLifePerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdPolicyMissLifePerMax.setStatus("current")
_ApDdPolicyMissLifeHigh_Type = Integer32
_ApDdPolicyMissLifeHigh_Object = MibScalar
apDdPolicyMissLifeHigh = _ApDdPolicyMissLifeHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 129),
    _ApDdPolicyMissLifeHigh_Type()
)
apDdPolicyMissLifeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdPolicyMissLifeHigh.setStatus("current")
_ApDdSubscriberMissPeriodTotal_Type = Integer32
_ApDdSubscriberMissPeriodTotal_Object = MibScalar
apDdSubscriberMissPeriodTotal = _ApDdSubscriberMissPeriodTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 130),
    _ApDdSubscriberMissPeriodTotal_Type()
)
apDdSubscriberMissPeriodTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSubscriberMissPeriodTotal.setStatus("current")
_ApDdSubscriberMissLifeTotal_Type = Integer32
_ApDdSubscriberMissLifeTotal_Object = MibScalar
apDdSubscriberMissLifeTotal = _ApDdSubscriberMissLifeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 131),
    _ApDdSubscriberMissLifeTotal_Type()
)
apDdSubscriberMissLifeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSubscriberMissLifeTotal.setStatus("current")
_ApDdSubscriberMissLifePerMax_Type = Integer32
_ApDdSubscriberMissLifePerMax_Object = MibScalar
apDdSubscriberMissLifePerMax = _ApDdSubscriberMissLifePerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 1, 132),
    _ApDdSubscriberMissLifePerMax_Type()
)
apDdSubscriberMissLifePerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdSubscriberMissLifePerMax.setStatus("current")
_ApDDMIBTabularObjects_ObjectIdentity = ObjectIdentity
apDDMIBTabularObjects = _ApDDMIBTabularObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2)
)
_ApDdInterfaceStatsTable_Object = MibTable
apDdInterfaceStatsTable = _ApDdInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    apDdInterfaceStatsTable.setStatus("current")
_ApDdInterfaceStatsEntry_Object = MibTableRow
apDdInterfaceStatsEntry = _ApDdInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1)
)
apDdInterfaceStatsEntry.setIndexNames(
    (0, "APDD-MIB", "apDdInterfaceIndex"),
)
if mibBuilder.loadTexts:
    apDdInterfaceStatsEntry.setStatus("current")


class _ApDdInterfaceIndex_Type(Integer32):
    """Custom type apDdInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApDdInterfaceIndex_Type.__name__ = "Integer32"
_ApDdInterfaceIndex_Object = MibTableColumn
apDdInterfaceIndex = _ApDdInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 1),
    _ApDdInterfaceIndex_Type()
)
apDdInterfaceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDdInterfaceIndex.setStatus("current")


class _ApDdInterfaceRealmName_Type(DisplayString):
    """Custom type apDdInterfaceRealmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApDdInterfaceRealmName_Type.__name__ = "DisplayString"
_ApDdInterfaceRealmName_Object = MibTableColumn
apDdInterfaceRealmName = _ApDdInterfaceRealmName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 2),
    _ApDdInterfaceRealmName_Type()
)
apDdInterfaceRealmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdInterfaceRealmName.setStatus("current")
_ApDdClientTransCPActive_Type = Gauge32
_ApDdClientTransCPActive_Object = MibTableColumn
apDdClientTransCPActive = _ApDdClientTransCPActive_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 3),
    _ApDdClientTransCPActive_Type()
)
apDdClientTransCPActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdClientTransCPActive.setStatus("current")
_ApDdClientTransCPHigh_Type = Counter32
_ApDdClientTransCPHigh_Object = MibTableColumn
apDdClientTransCPHigh = _ApDdClientTransCPHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 4),
    _ApDdClientTransCPHigh_Type()
)
apDdClientTransCPHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdClientTransCPHigh.setStatus("current")
_ApDdClientTransCPTotal_Type = Counter32
_ApDdClientTransCPTotal_Object = MibTableColumn
apDdClientTransCPTotal = _ApDdClientTransCPTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 5),
    _ApDdClientTransCPTotal_Type()
)
apDdClientTransCPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdClientTransCPTotal.setStatus("current")
_ApDdClientTransLTTotal_Type = Counter32
_ApDdClientTransLTTotal_Object = MibTableColumn
apDdClientTransLTTotal = _ApDdClientTransLTTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 6),
    _ApDdClientTransLTTotal_Type()
)
apDdClientTransLTTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdClientTransLTTotal.setStatus("current")
_ApDdClientTransLTPerMax_Type = Counter32
_ApDdClientTransLTPerMax_Object = MibTableColumn
apDdClientTransLTPerMax = _ApDdClientTransLTPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 7),
    _ApDdClientTransLTPerMax_Type()
)
apDdClientTransLTPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdClientTransLTPerMax.setStatus("current")
_ApDdClientTransLTHigh_Type = Counter32
_ApDdClientTransLTHigh_Object = MibTableColumn
apDdClientTransLTHigh = _ApDdClientTransLTHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 8),
    _ApDdClientTransLTHigh_Type()
)
apDdClientTransLTHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdClientTransLTHigh.setStatus("current")
_ApDdServerTransCPActive_Type = Gauge32
_ApDdServerTransCPActive_Object = MibTableColumn
apDdServerTransCPActive = _ApDdServerTransCPActive_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 9),
    _ApDdServerTransCPActive_Type()
)
apDdServerTransCPActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdServerTransCPActive.setStatus("current")
_ApDdServerTransCPHigh_Type = Counter32
_ApDdServerTransCPHigh_Object = MibTableColumn
apDdServerTransCPHigh = _ApDdServerTransCPHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 10),
    _ApDdServerTransCPHigh_Type()
)
apDdServerTransCPHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdServerTransCPHigh.setStatus("current")
_ApDdServerTransCPTotal_Type = Counter32
_ApDdServerTransCPTotal_Object = MibTableColumn
apDdServerTransCPTotal = _ApDdServerTransCPTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 11),
    _ApDdServerTransCPTotal_Type()
)
apDdServerTransCPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdServerTransCPTotal.setStatus("current")
_ApDdServerTransLTTotal_Type = Counter32
_ApDdServerTransLTTotal_Object = MibTableColumn
apDdServerTransLTTotal = _ApDdServerTransLTTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 12),
    _ApDdServerTransLTTotal_Type()
)
apDdServerTransLTTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdServerTransLTTotal.setStatus("current")
_ApDdServerTransLTPerMax_Type = Counter32
_ApDdServerTransLTPerMax_Object = MibTableColumn
apDdServerTransLTPerMax = _ApDdServerTransLTPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 13),
    _ApDdServerTransLTPerMax_Type()
)
apDdServerTransLTPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdServerTransLTPerMax.setStatus("current")
_ApDdServerTransLTHigh_Type = Counter32
_ApDdServerTransLTHigh_Object = MibTableColumn
apDdServerTransLTHigh = _ApDdServerTransLTHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 14),
    _ApDdServerTransLTHigh_Type()
)
apDdServerTransLTHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdServerTransLTHigh.setStatus("current")
_ApDdGenSocketsCPActive_Type = Gauge32
_ApDdGenSocketsCPActive_Object = MibTableColumn
apDdGenSocketsCPActive = _ApDdGenSocketsCPActive_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 15),
    _ApDdGenSocketsCPActive_Type()
)
apDdGenSocketsCPActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdGenSocketsCPActive.setStatus("current")
_ApDdGenSocketsCPHigh_Type = Counter32
_ApDdGenSocketsCPHigh_Object = MibTableColumn
apDdGenSocketsCPHigh = _ApDdGenSocketsCPHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 16),
    _ApDdGenSocketsCPHigh_Type()
)
apDdGenSocketsCPHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdGenSocketsCPHigh.setStatus("current")
_ApDdGenSocketsCPTotal_Type = Counter32
_ApDdGenSocketsCPTotal_Object = MibTableColumn
apDdGenSocketsCPTotal = _ApDdGenSocketsCPTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 17),
    _ApDdGenSocketsCPTotal_Type()
)
apDdGenSocketsCPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdGenSocketsCPTotal.setStatus("current")
_ApDdGenSocketsLTTotal_Type = Counter32
_ApDdGenSocketsLTTotal_Object = MibTableColumn
apDdGenSocketsLTTotal = _ApDdGenSocketsLTTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 18),
    _ApDdGenSocketsLTTotal_Type()
)
apDdGenSocketsLTTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdGenSocketsLTTotal.setStatus("current")
_ApDdGenSocketsLTPerMax_Type = Counter32
_ApDdGenSocketsLTPerMax_Object = MibTableColumn
apDdGenSocketsLTPerMax = _ApDdGenSocketsLTPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 19),
    _ApDdGenSocketsLTPerMax_Type()
)
apDdGenSocketsLTPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdGenSocketsLTPerMax.setStatus("current")
_ApDdGenSocketsLTHigh_Type = Counter32
_ApDdGenSocketsLTHigh_Object = MibTableColumn
apDdGenSocketsLTHigh = _ApDdGenSocketsLTHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 20),
    _ApDdGenSocketsLTHigh_Type()
)
apDdGenSocketsLTHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdGenSocketsLTHigh.setStatus("current")
_ApDdGenConnectsCPActive_Type = Gauge32
_ApDdGenConnectsCPActive_Object = MibTableColumn
apDdGenConnectsCPActive = _ApDdGenConnectsCPActive_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 21),
    _ApDdGenConnectsCPActive_Type()
)
apDdGenConnectsCPActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdGenConnectsCPActive.setStatus("current")
_ApDdGenConnectsCPHigh_Type = Counter32
_ApDdGenConnectsCPHigh_Object = MibTableColumn
apDdGenConnectsCPHigh = _ApDdGenConnectsCPHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 22),
    _ApDdGenConnectsCPHigh_Type()
)
apDdGenConnectsCPHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdGenConnectsCPHigh.setStatus("current")
_ApDdGenConnectsCPTotal_Type = Counter32
_ApDdGenConnectsCPTotal_Object = MibTableColumn
apDdGenConnectsCPTotal = _ApDdGenConnectsCPTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 23),
    _ApDdGenConnectsCPTotal_Type()
)
apDdGenConnectsCPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdGenConnectsCPTotal.setStatus("current")
_ApDdGenConnectsLTTotal_Type = Counter32
_ApDdGenConnectsLTTotal_Object = MibTableColumn
apDdGenConnectsLTTotal = _ApDdGenConnectsLTTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 24),
    _ApDdGenConnectsLTTotal_Type()
)
apDdGenConnectsLTTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdGenConnectsLTTotal.setStatus("current")
_ApDdGenConnectsLTPerMax_Type = Counter32
_ApDdGenConnectsLTPerMax_Object = MibTableColumn
apDdGenConnectsLTPerMax = _ApDdGenConnectsLTPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 25),
    _ApDdGenConnectsLTPerMax_Type()
)
apDdGenConnectsLTPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdGenConnectsLTPerMax.setStatus("current")
_ApDdGenConnectsLTHigh_Type = Counter32
_ApDdGenConnectsLTHigh_Object = MibTableColumn
apDdGenConnectsLTHigh = _ApDdGenConnectsLTHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 1, 1, 26),
    _ApDdGenConnectsLTHigh_Type()
)
apDdGenConnectsLTHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdGenConnectsLTHigh.setStatus("current")
_ApDdErrorStatusTable_Object = MibTable
apDdErrorStatusTable = _ApDdErrorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    apDdErrorStatusTable.setStatus("current")
_ApDdErrorStatusEntry_Object = MibTableRow
apDdErrorStatusEntry = _ApDdErrorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1)
)
apDdErrorStatusEntry.setIndexNames(
    (0, "APDD-MIB", "apDdInterfaceIndex"),
)
if mibBuilder.loadTexts:
    apDdErrorStatusEntry.setStatus("current")
_ApDdNoRouteFoundRecent_Type = Gauge32
_ApDdNoRouteFoundRecent_Object = MibTableColumn
apDdNoRouteFoundRecent = _ApDdNoRouteFoundRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 1),
    _ApDdNoRouteFoundRecent_Type()
)
apDdNoRouteFoundRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdNoRouteFoundRecent.setStatus("current")
_ApDdNoRouteFoundTotal_Type = Counter32
_ApDdNoRouteFoundTotal_Object = MibTableColumn
apDdNoRouteFoundTotal = _ApDdNoRouteFoundTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 2),
    _ApDdNoRouteFoundTotal_Type()
)
apDdNoRouteFoundTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdNoRouteFoundTotal.setStatus("current")
_ApDdNoRouteFoundPerMax_Type = Counter32
_ApDdNoRouteFoundPerMax_Object = MibTableColumn
apDdNoRouteFoundPerMax = _ApDdNoRouteFoundPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 3),
    _ApDdNoRouteFoundPerMax_Type()
)
apDdNoRouteFoundPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdNoRouteFoundPerMax.setStatus("current")
_ApDdMalformedMsgRecent_Type = Gauge32
_ApDdMalformedMsgRecent_Object = MibTableColumn
apDdMalformedMsgRecent = _ApDdMalformedMsgRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 4),
    _ApDdMalformedMsgRecent_Type()
)
apDdMalformedMsgRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMalformedMsgRecent.setStatus("current")
_ApDdMalformedMsgTotal_Type = Counter32
_ApDdMalformedMsgTotal_Object = MibTableColumn
apDdMalformedMsgTotal = _ApDdMalformedMsgTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 5),
    _ApDdMalformedMsgTotal_Type()
)
apDdMalformedMsgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMalformedMsgTotal.setStatus("current")
_ApDdMalformedMsgPerMax_Type = Counter32
_ApDdMalformedMsgPerMax_Object = MibTableColumn
apDdMalformedMsgPerMax = _ApDdMalformedMsgPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 6),
    _ApDdMalformedMsgPerMax_Type()
)
apDdMalformedMsgPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMalformedMsgPerMax.setStatus("current")
_ApDdRejectedMsgRecent_Type = Gauge32
_ApDdRejectedMsgRecent_Object = MibTableColumn
apDdRejectedMsgRecent = _ApDdRejectedMsgRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 7),
    _ApDdRejectedMsgRecent_Type()
)
apDdRejectedMsgRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdRejectedMsgRecent.setStatus("current")
_ApDdRejectedMsgTotal_Type = Counter32
_ApDdRejectedMsgTotal_Object = MibTableColumn
apDdRejectedMsgTotal = _ApDdRejectedMsgTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 8),
    _ApDdRejectedMsgTotal_Type()
)
apDdRejectedMsgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdRejectedMsgTotal.setStatus("current")
_ApDdRejectedMsgPerMax_Type = Counter32
_ApDdRejectedMsgPerMax_Object = MibTableColumn
apDdRejectedMsgPerMax = _ApDdRejectedMsgPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 9),
    _ApDdRejectedMsgPerMax_Type()
)
apDdRejectedMsgPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdRejectedMsgPerMax.setStatus("current")
_ApDdDroppedMsgRecent_Type = Gauge32
_ApDdDroppedMsgRecent_Object = MibTableColumn
apDdDroppedMsgRecent = _ApDdDroppedMsgRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 10),
    _ApDdDroppedMsgRecent_Type()
)
apDdDroppedMsgRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdDroppedMsgRecent.setStatus("current")
_ApDdDroppedMsgTotal_Type = Counter32
_ApDdDroppedMsgTotal_Object = MibTableColumn
apDdDroppedMsgTotal = _ApDdDroppedMsgTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 11),
    _ApDdDroppedMsgTotal_Type()
)
apDdDroppedMsgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdDroppedMsgTotal.setStatus("current")
_ApDdDroppedMsgPerMax_Type = Counter32
_ApDdDroppedMsgPerMax_Object = MibTableColumn
apDdDroppedMsgPerMax = _ApDdDroppedMsgPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 12),
    _ApDdDroppedMsgPerMax_Type()
)
apDdDroppedMsgPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdDroppedMsgPerMax.setStatus("current")
_ApDdInboundConstraintsRecent_Type = Gauge32
_ApDdInboundConstraintsRecent_Object = MibTableColumn
apDdInboundConstraintsRecent = _ApDdInboundConstraintsRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 13),
    _ApDdInboundConstraintsRecent_Type()
)
apDdInboundConstraintsRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdInboundConstraintsRecent.setStatus("current")
_ApDdInboundConstraintsTotal_Type = Counter32
_ApDdInboundConstraintsTotal_Object = MibTableColumn
apDdInboundConstraintsTotal = _ApDdInboundConstraintsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 14),
    _ApDdInboundConstraintsTotal_Type()
)
apDdInboundConstraintsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdInboundConstraintsTotal.setStatus("current")
_ApDdInboundConstraintsPerMax_Type = Counter32
_ApDdInboundConstraintsPerMax_Object = MibTableColumn
apDdInboundConstraintsPerMax = _ApDdInboundConstraintsPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 15),
    _ApDdInboundConstraintsPerMax_Type()
)
apDdInboundConstraintsPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdInboundConstraintsPerMax.setStatus("current")
_ApDdOutboundConstraintsRecent_Type = Gauge32
_ApDdOutboundConstraintsRecent_Object = MibTableColumn
apDdOutboundConstraintsRecent = _ApDdOutboundConstraintsRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 16),
    _ApDdOutboundConstraintsRecent_Type()
)
apDdOutboundConstraintsRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdOutboundConstraintsRecent.setStatus("current")
_ApDdOutboundConstraintsTotal_Type = Counter32
_ApDdOutboundConstraintsTotal_Object = MibTableColumn
apDdOutboundConstraintsTotal = _ApDdOutboundConstraintsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 17),
    _ApDdOutboundConstraintsTotal_Type()
)
apDdOutboundConstraintsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdOutboundConstraintsTotal.setStatus("current")
_ApDdOutboundConstraintsPerMax_Type = Counter32
_ApDdOutboundConstraintsPerMax_Object = MibTableColumn
apDdOutboundConstraintsPerMax = _ApDdOutboundConstraintsPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 2, 1, 18),
    _ApDdOutboundConstraintsPerMax_Type()
)
apDdOutboundConstraintsPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdOutboundConstraintsPerMax.setStatus("current")
_ApDdMsgTypeInfoTable_Object = MibTable
apDdMsgTypeInfoTable = _ApDdMsgTypeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 3)
)
if mibBuilder.loadTexts:
    apDdMsgTypeInfoTable.setStatus("current")
_ApDdMsgTypeInfoEntry_Object = MibTableRow
apDdMsgTypeInfoEntry = _ApDdMsgTypeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 3, 1)
)
apDdMsgTypeInfoEntry.setIndexNames(
    (0, "APDD-MIB", "apDdMsgTypeIndex"),
)
if mibBuilder.loadTexts:
    apDdMsgTypeInfoEntry.setStatus("current")


class _ApDdMsgTypeIndex_Type(Integer32):
    """Custom type apDdMsgTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApDdMsgTypeIndex_Type.__name__ = "Integer32"
_ApDdMsgTypeIndex_Object = MibTableColumn
apDdMsgTypeIndex = _ApDdMsgTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 3, 1, 1),
    _ApDdMsgTypeIndex_Type()
)
apDdMsgTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apDdMsgTypeIndex.setStatus("current")


class _ApDdMsgTypeMsgName_Type(DisplayString):
    """Custom type apDdMsgTypeMsgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApDdMsgTypeMsgName_Type.__name__ = "DisplayString"
_ApDdMsgTypeMsgName_Object = MibTableColumn
apDdMsgTypeMsgName = _ApDdMsgTypeMsgName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 3, 1, 2),
    _ApDdMsgTypeMsgName_Type()
)
apDdMsgTypeMsgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeMsgName.setStatus("current")
_ApDdMsgTypeStatsTable_Object = MibTable
apDdMsgTypeStatsTable = _ApDdMsgTypeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4)
)
if mibBuilder.loadTexts:
    apDdMsgTypeStatsTable.setStatus("current")
_ApDdMsgTypeStatsEntry_Object = MibTableRow
apDdMsgTypeStatsEntry = _ApDdMsgTypeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1)
)
apDdMsgTypeStatsEntry.setIndexNames(
    (0, "APDD-MIB", "apDdInterfaceIndex"),
    (0, "APDD-MIB", "apDdMsgTypeIndex"),
)
if mibBuilder.loadTexts:
    apDdMsgTypeStatsEntry.setStatus("current")
_ApDdMsgTypeServerReqRecent_Type = Gauge32
_ApDdMsgTypeServerReqRecent_Object = MibTableColumn
apDdMsgTypeServerReqRecent = _ApDdMsgTypeServerReqRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 3),
    _ApDdMsgTypeServerReqRecent_Type()
)
apDdMsgTypeServerReqRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeServerReqRecent.setStatus("current")
_ApDdMsgTypeServerReqTotal_Type = Counter32
_ApDdMsgTypeServerReqTotal_Object = MibTableColumn
apDdMsgTypeServerReqTotal = _ApDdMsgTypeServerReqTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 4),
    _ApDdMsgTypeServerReqTotal_Type()
)
apDdMsgTypeServerReqTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeServerReqTotal.setStatus("current")
_ApDdMsgTypeServerReqPerMax_Type = Counter32
_ApDdMsgTypeServerReqPerMax_Object = MibTableColumn
apDdMsgTypeServerReqPerMax = _ApDdMsgTypeServerReqPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 5),
    _ApDdMsgTypeServerReqPerMax_Type()
)
apDdMsgTypeServerReqPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeServerReqPerMax.setStatus("current")
_ApDdMsgTypeClientReqRecent_Type = Gauge32
_ApDdMsgTypeClientReqRecent_Object = MibTableColumn
apDdMsgTypeClientReqRecent = _ApDdMsgTypeClientReqRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 6),
    _ApDdMsgTypeClientReqRecent_Type()
)
apDdMsgTypeClientReqRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeClientReqRecent.setStatus("current")
_ApDdMsgTypeClientReqTotal_Type = Counter32
_ApDdMsgTypeClientReqTotal_Object = MibTableColumn
apDdMsgTypeClientReqTotal = _ApDdMsgTypeClientReqTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 7),
    _ApDdMsgTypeClientReqTotal_Type()
)
apDdMsgTypeClientReqTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeClientReqTotal.setStatus("current")
_ApDdMsgTypeClientReqPerMax_Type = Counter32
_ApDdMsgTypeClientReqPerMax_Object = MibTableColumn
apDdMsgTypeClientReqPerMax = _ApDdMsgTypeClientReqPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 8),
    _ApDdMsgTypeClientReqPerMax_Type()
)
apDdMsgTypeClientReqPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeClientReqPerMax.setStatus("current")
_ApDdMsgTypeServerRetransRecent_Type = Gauge32
_ApDdMsgTypeServerRetransRecent_Object = MibTableColumn
apDdMsgTypeServerRetransRecent = _ApDdMsgTypeServerRetransRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 9),
    _ApDdMsgTypeServerRetransRecent_Type()
)
apDdMsgTypeServerRetransRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeServerRetransRecent.setStatus("current")
_ApDdMsgTypeServerRetransTotal_Type = Counter32
_ApDdMsgTypeServerRetransTotal_Object = MibTableColumn
apDdMsgTypeServerRetransTotal = _ApDdMsgTypeServerRetransTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 10),
    _ApDdMsgTypeServerRetransTotal_Type()
)
apDdMsgTypeServerRetransTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeServerRetransTotal.setStatus("current")
_ApDdMsgTypeServerRetransPerMax_Type = Counter32
_ApDdMsgTypeServerRetransPerMax_Object = MibTableColumn
apDdMsgTypeServerRetransPerMax = _ApDdMsgTypeServerRetransPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 11),
    _ApDdMsgTypeServerRetransPerMax_Type()
)
apDdMsgTypeServerRetransPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeServerRetransPerMax.setStatus("current")
_ApDdMsgTypeClientRetransRecent_Type = Gauge32
_ApDdMsgTypeClientRetransRecent_Object = MibTableColumn
apDdMsgTypeClientRetransRecent = _ApDdMsgTypeClientRetransRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 12),
    _ApDdMsgTypeClientRetransRecent_Type()
)
apDdMsgTypeClientRetransRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeClientRetransRecent.setStatus("current")
_ApDdMsgTypeClientRetransTotal_Type = Counter32
_ApDdMsgTypeClientRetransTotal_Object = MibTableColumn
apDdMsgTypeClientRetransTotal = _ApDdMsgTypeClientRetransTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 13),
    _ApDdMsgTypeClientRetransTotal_Type()
)
apDdMsgTypeClientRetransTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeClientRetransTotal.setStatus("current")
_ApDdMsgTypeClientRetransPerMax_Type = Counter32
_ApDdMsgTypeClientRetransPerMax_Object = MibTableColumn
apDdMsgTypeClientRetransPerMax = _ApDdMsgTypeClientRetransPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 14),
    _ApDdMsgTypeClientRetransPerMax_Type()
)
apDdMsgTypeClientRetransPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeClientRetransPerMax.setStatus("current")
_ApDdMsgTypeServerRespRetransRecent_Type = Gauge32
_ApDdMsgTypeServerRespRetransRecent_Object = MibTableColumn
apDdMsgTypeServerRespRetransRecent = _ApDdMsgTypeServerRespRetransRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 15),
    _ApDdMsgTypeServerRespRetransRecent_Type()
)
apDdMsgTypeServerRespRetransRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeServerRespRetransRecent.setStatus("current")
_ApDdMsgTypeServerRespRetransTotal_Type = Counter32
_ApDdMsgTypeServerRespRetransTotal_Object = MibTableColumn
apDdMsgTypeServerRespRetransTotal = _ApDdMsgTypeServerRespRetransTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 16),
    _ApDdMsgTypeServerRespRetransTotal_Type()
)
apDdMsgTypeServerRespRetransTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeServerRespRetransTotal.setStatus("current")
_ApDdMsgTypeServerRespRetransPerMax_Type = Counter32
_ApDdMsgTypeServerRespRetransPerMax_Object = MibTableColumn
apDdMsgTypeServerRespRetransPerMax = _ApDdMsgTypeServerRespRetransPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 17),
    _ApDdMsgTypeServerRespRetransPerMax_Type()
)
apDdMsgTypeServerRespRetransPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeServerRespRetransPerMax.setStatus("current")
_ApDdMsgTypeClientRespRetransRecent_Type = Gauge32
_ApDdMsgTypeClientRespRetransRecent_Object = MibTableColumn
apDdMsgTypeClientRespRetransRecent = _ApDdMsgTypeClientRespRetransRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 21),
    _ApDdMsgTypeClientRespRetransRecent_Type()
)
apDdMsgTypeClientRespRetransRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeClientRespRetransRecent.setStatus("current")
_ApDdMsgTypeClientRespRetransTotal_Type = Counter32
_ApDdMsgTypeClientRespRetransTotal_Object = MibTableColumn
apDdMsgTypeClientRespRetransTotal = _ApDdMsgTypeClientRespRetransTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 22),
    _ApDdMsgTypeClientRespRetransTotal_Type()
)
apDdMsgTypeClientRespRetransTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeClientRespRetransTotal.setStatus("current")
_ApDdMsgTypeClientRespRetransPerMax_Type = Counter32
_ApDdMsgTypeClientRespRetransPerMax_Object = MibTableColumn
apDdMsgTypeClientRespRetransPerMax = _ApDdMsgTypeClientRespRetransPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 23),
    _ApDdMsgTypeClientRespRetransPerMax_Type()
)
apDdMsgTypeClientRespRetransPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeClientRespRetransPerMax.setStatus("current")
_ApDdMsgTypeClientTimeoutRecent_Type = Gauge32
_ApDdMsgTypeClientTimeoutRecent_Object = MibTableColumn
apDdMsgTypeClientTimeoutRecent = _ApDdMsgTypeClientTimeoutRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 27),
    _ApDdMsgTypeClientTimeoutRecent_Type()
)
apDdMsgTypeClientTimeoutRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeClientTimeoutRecent.setStatus("current")
_ApDdMsgTypeClientTimeoutTotal_Type = Counter32
_ApDdMsgTypeClientTimeoutTotal_Object = MibTableColumn
apDdMsgTypeClientTimeoutTotal = _ApDdMsgTypeClientTimeoutTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 28),
    _ApDdMsgTypeClientTimeoutTotal_Type()
)
apDdMsgTypeClientTimeoutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeClientTimeoutTotal.setStatus("current")
_ApDdMsgTypeClientTimeoutPerMax_Type = Counter32
_ApDdMsgTypeClientTimeoutPerMax_Object = MibTableColumn
apDdMsgTypeClientTimeoutPerMax = _ApDdMsgTypeClientTimeoutPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 29),
    _ApDdMsgTypeClientTimeoutPerMax_Type()
)
apDdMsgTypeClientTimeoutPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeClientTimeoutPerMax.setStatus("current")
_ApDdMsgTypeClientThrottledRecent_Type = Gauge32
_ApDdMsgTypeClientThrottledRecent_Object = MibTableColumn
apDdMsgTypeClientThrottledRecent = _ApDdMsgTypeClientThrottledRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 33),
    _ApDdMsgTypeClientThrottledRecent_Type()
)
apDdMsgTypeClientThrottledRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeClientThrottledRecent.setStatus("current")
_ApDdMsgTypeClientThrottledTotal_Type = Counter32
_ApDdMsgTypeClientThrottledTotal_Object = MibTableColumn
apDdMsgTypeClientThrottledTotal = _ApDdMsgTypeClientThrottledTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 34),
    _ApDdMsgTypeClientThrottledTotal_Type()
)
apDdMsgTypeClientThrottledTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeClientThrottledTotal.setStatus("current")
_ApDdMsgTypeClientThrottledPerMax_Type = Counter32
_ApDdMsgTypeClientThrottledPerMax_Object = MibTableColumn
apDdMsgTypeClientThrottledPerMax = _ApDdMsgTypeClientThrottledPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 35),
    _ApDdMsgTypeClientThrottledPerMax_Type()
)
apDdMsgTypeClientThrottledPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeClientThrottledPerMax.setStatus("current")
_ApDdMsgTypeAverageLatency_Type = Gauge32
_ApDdMsgTypeAverageLatency_Object = MibTableColumn
apDdMsgTypeAverageLatency = _ApDdMsgTypeAverageLatency_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 36),
    _ApDdMsgTypeAverageLatency_Type()
)
apDdMsgTypeAverageLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeAverageLatency.setStatus("current")
_ApDdMsgTypeMaximumLatency_Type = Gauge32
_ApDdMsgTypeMaximumLatency_Object = MibTableColumn
apDdMsgTypeMaximumLatency = _ApDdMsgTypeMaximumLatency_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 37),
    _ApDdMsgTypeMaximumLatency_Type()
)
apDdMsgTypeMaximumLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeMaximumLatency.setStatus("current")
_ApDdMsgTypeLatencyWindow_Type = Integer32
_ApDdMsgTypeLatencyWindow_Object = MibTableColumn
apDdMsgTypeLatencyWindow = _ApDdMsgTypeLatencyWindow_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 4, 1, 38),
    _ApDdMsgTypeLatencyWindow_Type()
)
apDdMsgTypeLatencyWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgTypeLatencyWindow.setStatus("current")
if mibBuilder.loadTexts:
    apDdMsgTypeLatencyWindow.setUnits("second")
_ApDdMsgReturnCodeInfoTable_Object = MibTable
apDdMsgReturnCodeInfoTable = _ApDdMsgReturnCodeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 5)
)
if mibBuilder.loadTexts:
    apDdMsgReturnCodeInfoTable.setStatus("current")
_ApDdMsgReturnCodeInfoEntry_Object = MibTableRow
apDdMsgReturnCodeInfoEntry = _ApDdMsgReturnCodeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 5, 1)
)
apDdMsgReturnCodeInfoEntry.setIndexNames(
    (0, "APDD-MIB", "apDdMsgReturnCodeIndex"),
)
if mibBuilder.loadTexts:
    apDdMsgReturnCodeInfoEntry.setStatus("current")


class _ApDdMsgReturnCodeIndex_Type(Integer32):
    """Custom type apDdMsgReturnCodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApDdMsgReturnCodeIndex_Type.__name__ = "Integer32"
_ApDdMsgReturnCodeIndex_Object = MibTableColumn
apDdMsgReturnCodeIndex = _ApDdMsgReturnCodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 5, 1, 1),
    _ApDdMsgReturnCodeIndex_Type()
)
apDdMsgReturnCodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apDdMsgReturnCodeIndex.setStatus("current")


class _ApDdMsgReturnCodeName_Type(DisplayString):
    """Custom type apDdMsgReturnCodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApDdMsgReturnCodeName_Type.__name__ = "DisplayString"
_ApDdMsgReturnCodeName_Object = MibTableColumn
apDdMsgReturnCodeName = _ApDdMsgReturnCodeName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 5, 1, 2),
    _ApDdMsgReturnCodeName_Type()
)
apDdMsgReturnCodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgReturnCodeName.setStatus("current")
_ApDdMsgStatsReturnCodeTable_Object = MibTable
apDdMsgStatsReturnCodeTable = _ApDdMsgStatsReturnCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 6)
)
if mibBuilder.loadTexts:
    apDdMsgStatsReturnCodeTable.setStatus("current")
_ApDdMsgStatsReturnCodeEntry_Object = MibTableRow
apDdMsgStatsReturnCodeEntry = _ApDdMsgStatsReturnCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 6, 1)
)
apDdMsgStatsReturnCodeEntry.setIndexNames(
    (0, "APDD-MIB", "apDdInterfaceIndex"),
    (0, "APDD-MIB", "apDdMsgTypeIndex"),
    (0, "APDD-MIB", "apDdMsgReturnCodeIndex"),
)
if mibBuilder.loadTexts:
    apDdMsgStatsReturnCodeEntry.setStatus("current")
_ApDdMsgReturnCodeServerRecent_Type = Gauge32
_ApDdMsgReturnCodeServerRecent_Object = MibTableColumn
apDdMsgReturnCodeServerRecent = _ApDdMsgReturnCodeServerRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 6, 1, 3),
    _ApDdMsgReturnCodeServerRecent_Type()
)
apDdMsgReturnCodeServerRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgReturnCodeServerRecent.setStatus("current")
_ApDdMsgReturnCodeServerTotal_Type = Counter32
_ApDdMsgReturnCodeServerTotal_Object = MibTableColumn
apDdMsgReturnCodeServerTotal = _ApDdMsgReturnCodeServerTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 6, 1, 4),
    _ApDdMsgReturnCodeServerTotal_Type()
)
apDdMsgReturnCodeServerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgReturnCodeServerTotal.setStatus("current")
_ApDdMsgReturnCodeServerPerMax_Type = Counter32
_ApDdMsgReturnCodeServerPerMax_Object = MibTableColumn
apDdMsgReturnCodeServerPerMax = _ApDdMsgReturnCodeServerPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 6, 1, 5),
    _ApDdMsgReturnCodeServerPerMax_Type()
)
apDdMsgReturnCodeServerPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgReturnCodeServerPerMax.setStatus("current")
_ApDdMsgReturnCodeClientRecent_Type = Gauge32
_ApDdMsgReturnCodeClientRecent_Object = MibTableColumn
apDdMsgReturnCodeClientRecent = _ApDdMsgReturnCodeClientRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 6, 1, 6),
    _ApDdMsgReturnCodeClientRecent_Type()
)
apDdMsgReturnCodeClientRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgReturnCodeClientRecent.setStatus("current")
_ApDdMsgReturnCodeClientTotal_Type = Counter32
_ApDdMsgReturnCodeClientTotal_Object = MibTableColumn
apDdMsgReturnCodeClientTotal = _ApDdMsgReturnCodeClientTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 6, 1, 7),
    _ApDdMsgReturnCodeClientTotal_Type()
)
apDdMsgReturnCodeClientTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgReturnCodeClientTotal.setStatus("current")
_ApDdMsgReturnCodeClientPerMax_Type = Counter32
_ApDdMsgReturnCodeClientPerMax_Object = MibTableColumn
apDdMsgReturnCodeClientPerMax = _ApDdMsgReturnCodeClientPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 6, 1, 8),
    _ApDdMsgReturnCodeClientPerMax_Type()
)
apDdMsgReturnCodeClientPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdMsgReturnCodeClientPerMax.setStatus("current")
_ApDdAgentStatsTable_Object = MibTable
apDdAgentStatsTable = _ApDdAgentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7)
)
if mibBuilder.loadTexts:
    apDdAgentStatsTable.setStatus("current")
_ApDdAgentStatsEntry_Object = MibTableRow
apDdAgentStatsEntry = _ApDdAgentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1)
)
apDdAgentStatsEntry.setIndexNames(
    (0, "APDD-MIB", "apDdAgentIndex"),
)
if mibBuilder.loadTexts:
    apDdAgentStatsEntry.setStatus("current")


class _ApDdAgentIndex_Type(Integer32):
    """Custom type apDdAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApDdAgentIndex_Type.__name__ = "Integer32"
_ApDdAgentIndex_Object = MibTableColumn
apDdAgentIndex = _ApDdAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 1),
    _ApDdAgentIndex_Type()
)
apDdAgentIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDdAgentIndex.setStatus("current")


class _ApDdAgentRealmName_Type(DisplayString):
    """Custom type apDdAgentRealmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApDdAgentRealmName_Type.__name__ = "DisplayString"
_ApDdAgentRealmName_Object = MibTableColumn
apDdAgentRealmName = _ApDdAgentRealmName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 2),
    _ApDdAgentRealmName_Type()
)
apDdAgentRealmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentRealmName.setStatus("current")
_ApDdAgentClientTransCPActive_Type = Gauge32
_ApDdAgentClientTransCPActive_Object = MibTableColumn
apDdAgentClientTransCPActive = _ApDdAgentClientTransCPActive_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 3),
    _ApDdAgentClientTransCPActive_Type()
)
apDdAgentClientTransCPActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentClientTransCPActive.setStatus("current")
_ApDdAgentClientTransCPHigh_Type = Counter32
_ApDdAgentClientTransCPHigh_Object = MibTableColumn
apDdAgentClientTransCPHigh = _ApDdAgentClientTransCPHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 4),
    _ApDdAgentClientTransCPHigh_Type()
)
apDdAgentClientTransCPHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentClientTransCPHigh.setStatus("current")
_ApDdAgentClientTransCPTotal_Type = Counter32
_ApDdAgentClientTransCPTotal_Object = MibTableColumn
apDdAgentClientTransCPTotal = _ApDdAgentClientTransCPTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 5),
    _ApDdAgentClientTransCPTotal_Type()
)
apDdAgentClientTransCPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentClientTransCPTotal.setStatus("current")
_ApDdAgentClientTransLTTotal_Type = Counter32
_ApDdAgentClientTransLTTotal_Object = MibTableColumn
apDdAgentClientTransLTTotal = _ApDdAgentClientTransLTTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 6),
    _ApDdAgentClientTransLTTotal_Type()
)
apDdAgentClientTransLTTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentClientTransLTTotal.setStatus("current")
_ApDdAgentClientTransLTPerMax_Type = Counter32
_ApDdAgentClientTransLTPerMax_Object = MibTableColumn
apDdAgentClientTransLTPerMax = _ApDdAgentClientTransLTPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 7),
    _ApDdAgentClientTransLTPerMax_Type()
)
apDdAgentClientTransLTPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentClientTransLTPerMax.setStatus("current")
_ApDdAgentClientTransLTHigh_Type = Counter32
_ApDdAgentClientTransLTHigh_Object = MibTableColumn
apDdAgentClientTransLTHigh = _ApDdAgentClientTransLTHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 8),
    _ApDdAgentClientTransLTHigh_Type()
)
apDdAgentClientTransLTHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentClientTransLTHigh.setStatus("current")
_ApDdAgentServerTransCPActive_Type = Gauge32
_ApDdAgentServerTransCPActive_Object = MibTableColumn
apDdAgentServerTransCPActive = _ApDdAgentServerTransCPActive_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 9),
    _ApDdAgentServerTransCPActive_Type()
)
apDdAgentServerTransCPActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentServerTransCPActive.setStatus("current")
_ApDdAgentServerTransCPHigh_Type = Counter32
_ApDdAgentServerTransCPHigh_Object = MibTableColumn
apDdAgentServerTransCPHigh = _ApDdAgentServerTransCPHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 10),
    _ApDdAgentServerTransCPHigh_Type()
)
apDdAgentServerTransCPHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentServerTransCPHigh.setStatus("current")
_ApDdAgentServerTransCPTotal_Type = Counter32
_ApDdAgentServerTransCPTotal_Object = MibTableColumn
apDdAgentServerTransCPTotal = _ApDdAgentServerTransCPTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 11),
    _ApDdAgentServerTransCPTotal_Type()
)
apDdAgentServerTransCPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentServerTransCPTotal.setStatus("current")
_ApDdAgentServerTransLTTotal_Type = Counter32
_ApDdAgentServerTransLTTotal_Object = MibTableColumn
apDdAgentServerTransLTTotal = _ApDdAgentServerTransLTTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 12),
    _ApDdAgentServerTransLTTotal_Type()
)
apDdAgentServerTransLTTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentServerTransLTTotal.setStatus("current")
_ApDdAgentServerTransLTPerMax_Type = Counter32
_ApDdAgentServerTransLTPerMax_Object = MibTableColumn
apDdAgentServerTransLTPerMax = _ApDdAgentServerTransLTPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 13),
    _ApDdAgentServerTransLTPerMax_Type()
)
apDdAgentServerTransLTPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentServerTransLTPerMax.setStatus("current")
_ApDdAgentServerTransLTHigh_Type = Counter32
_ApDdAgentServerTransLTHigh_Object = MibTableColumn
apDdAgentServerTransLTHigh = _ApDdAgentServerTransLTHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 14),
    _ApDdAgentServerTransLTHigh_Type()
)
apDdAgentServerTransLTHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentServerTransLTHigh.setStatus("current")
_ApDdAgentGenSocketsCPActive_Type = Gauge32
_ApDdAgentGenSocketsCPActive_Object = MibTableColumn
apDdAgentGenSocketsCPActive = _ApDdAgentGenSocketsCPActive_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 15),
    _ApDdAgentGenSocketsCPActive_Type()
)
apDdAgentGenSocketsCPActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentGenSocketsCPActive.setStatus("current")
_ApDdAgentGenSocketsCPHigh_Type = Counter32
_ApDdAgentGenSocketsCPHigh_Object = MibTableColumn
apDdAgentGenSocketsCPHigh = _ApDdAgentGenSocketsCPHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 16),
    _ApDdAgentGenSocketsCPHigh_Type()
)
apDdAgentGenSocketsCPHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentGenSocketsCPHigh.setStatus("current")
_ApDdAgentGenSocketsCPTotal_Type = Counter32
_ApDdAgentGenSocketsCPTotal_Object = MibTableColumn
apDdAgentGenSocketsCPTotal = _ApDdAgentGenSocketsCPTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 17),
    _ApDdAgentGenSocketsCPTotal_Type()
)
apDdAgentGenSocketsCPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentGenSocketsCPTotal.setStatus("current")
_ApDdAgentGenSocketsLTTotal_Type = Counter32
_ApDdAgentGenSocketsLTTotal_Object = MibTableColumn
apDdAgentGenSocketsLTTotal = _ApDdAgentGenSocketsLTTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 18),
    _ApDdAgentGenSocketsLTTotal_Type()
)
apDdAgentGenSocketsLTTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentGenSocketsLTTotal.setStatus("current")
_ApDdAgentGenSocketsLTPerMax_Type = Counter32
_ApDdAgentGenSocketsLTPerMax_Object = MibTableColumn
apDdAgentGenSocketsLTPerMax = _ApDdAgentGenSocketsLTPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 19),
    _ApDdAgentGenSocketsLTPerMax_Type()
)
apDdAgentGenSocketsLTPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentGenSocketsLTPerMax.setStatus("current")
_ApDdAgentGenSocketsLTHigh_Type = Counter32
_ApDdAgentGenSocketsLTHigh_Object = MibTableColumn
apDdAgentGenSocketsLTHigh = _ApDdAgentGenSocketsLTHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 20),
    _ApDdAgentGenSocketsLTHigh_Type()
)
apDdAgentGenSocketsLTHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentGenSocketsLTHigh.setStatus("current")
_ApDdAgentGenConnectsCPActive_Type = Gauge32
_ApDdAgentGenConnectsCPActive_Object = MibTableColumn
apDdAgentGenConnectsCPActive = _ApDdAgentGenConnectsCPActive_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 21),
    _ApDdAgentGenConnectsCPActive_Type()
)
apDdAgentGenConnectsCPActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentGenConnectsCPActive.setStatus("current")
_ApDdAgentGenConnectsCPHigh_Type = Counter32
_ApDdAgentGenConnectsCPHigh_Object = MibTableColumn
apDdAgentGenConnectsCPHigh = _ApDdAgentGenConnectsCPHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 22),
    _ApDdAgentGenConnectsCPHigh_Type()
)
apDdAgentGenConnectsCPHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentGenConnectsCPHigh.setStatus("current")
_ApDdAgentGenConnectsCPTotal_Type = Counter32
_ApDdAgentGenConnectsCPTotal_Object = MibTableColumn
apDdAgentGenConnectsCPTotal = _ApDdAgentGenConnectsCPTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 23),
    _ApDdAgentGenConnectsCPTotal_Type()
)
apDdAgentGenConnectsCPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentGenConnectsCPTotal.setStatus("current")
_ApDdAgentGenConnectsLTTotal_Type = Counter32
_ApDdAgentGenConnectsLTTotal_Object = MibTableColumn
apDdAgentGenConnectsLTTotal = _ApDdAgentGenConnectsLTTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 24),
    _ApDdAgentGenConnectsLTTotal_Type()
)
apDdAgentGenConnectsLTTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentGenConnectsLTTotal.setStatus("current")
_ApDdAgentGenConnectsLTPerMax_Type = Counter32
_ApDdAgentGenConnectsLTPerMax_Object = MibTableColumn
apDdAgentGenConnectsLTPerMax = _ApDdAgentGenConnectsLTPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 25),
    _ApDdAgentGenConnectsLTPerMax_Type()
)
apDdAgentGenConnectsLTPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentGenConnectsLTPerMax.setStatus("current")
_ApDdAgentGenConnectsLTHigh_Type = Counter32
_ApDdAgentGenConnectsLTHigh_Object = MibTableColumn
apDdAgentGenConnectsLTHigh = _ApDdAgentGenConnectsLTHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 7, 1, 26),
    _ApDdAgentGenConnectsLTHigh_Type()
)
apDdAgentGenConnectsLTHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentGenConnectsLTHigh.setStatus("current")
_ApDdAgentErrorStatusTable_Object = MibTable
apDdAgentErrorStatusTable = _ApDdAgentErrorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8)
)
if mibBuilder.loadTexts:
    apDdAgentErrorStatusTable.setStatus("current")
_ApDdAgentErrorStatusEntry_Object = MibTableRow
apDdAgentErrorStatusEntry = _ApDdAgentErrorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1)
)
apDdAgentErrorStatusEntry.setIndexNames(
    (0, "APDD-MIB", "apDdAgentIndex"),
)
if mibBuilder.loadTexts:
    apDdAgentErrorStatusEntry.setStatus("current")
_ApDdAgentNoRouteFoundRecent_Type = Gauge32
_ApDdAgentNoRouteFoundRecent_Object = MibTableColumn
apDdAgentNoRouteFoundRecent = _ApDdAgentNoRouteFoundRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 1),
    _ApDdAgentNoRouteFoundRecent_Type()
)
apDdAgentNoRouteFoundRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentNoRouteFoundRecent.setStatus("current")
_ApDdAgentNoRouteFoundTotal_Type = Counter32
_ApDdAgentNoRouteFoundTotal_Object = MibTableColumn
apDdAgentNoRouteFoundTotal = _ApDdAgentNoRouteFoundTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 2),
    _ApDdAgentNoRouteFoundTotal_Type()
)
apDdAgentNoRouteFoundTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentNoRouteFoundTotal.setStatus("current")
_ApDdAgentNoRouteFoundPerMax_Type = Counter32
_ApDdAgentNoRouteFoundPerMax_Object = MibTableColumn
apDdAgentNoRouteFoundPerMax = _ApDdAgentNoRouteFoundPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 3),
    _ApDdAgentNoRouteFoundPerMax_Type()
)
apDdAgentNoRouteFoundPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentNoRouteFoundPerMax.setStatus("current")
_ApDdAgentMalformedMsgRecent_Type = Gauge32
_ApDdAgentMalformedMsgRecent_Object = MibTableColumn
apDdAgentMalformedMsgRecent = _ApDdAgentMalformedMsgRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 4),
    _ApDdAgentMalformedMsgRecent_Type()
)
apDdAgentMalformedMsgRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMalformedMsgRecent.setStatus("current")
_ApDdAgentMalformedMsgTotal_Type = Counter32
_ApDdAgentMalformedMsgTotal_Object = MibTableColumn
apDdAgentMalformedMsgTotal = _ApDdAgentMalformedMsgTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 5),
    _ApDdAgentMalformedMsgTotal_Type()
)
apDdAgentMalformedMsgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMalformedMsgTotal.setStatus("current")
_ApDdAgentMalformedMsgPerMax_Type = Counter32
_ApDdAgentMalformedMsgPerMax_Object = MibTableColumn
apDdAgentMalformedMsgPerMax = _ApDdAgentMalformedMsgPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 6),
    _ApDdAgentMalformedMsgPerMax_Type()
)
apDdAgentMalformedMsgPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMalformedMsgPerMax.setStatus("current")
_ApDdAgentRejectedMsgRecent_Type = Gauge32
_ApDdAgentRejectedMsgRecent_Object = MibTableColumn
apDdAgentRejectedMsgRecent = _ApDdAgentRejectedMsgRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 7),
    _ApDdAgentRejectedMsgRecent_Type()
)
apDdAgentRejectedMsgRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentRejectedMsgRecent.setStatus("current")
_ApDdAgentRejectedMsgTotal_Type = Counter32
_ApDdAgentRejectedMsgTotal_Object = MibTableColumn
apDdAgentRejectedMsgTotal = _ApDdAgentRejectedMsgTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 8),
    _ApDdAgentRejectedMsgTotal_Type()
)
apDdAgentRejectedMsgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentRejectedMsgTotal.setStatus("current")
_ApDdAgentRejectedMsgPerMax_Type = Counter32
_ApDdAgentRejectedMsgPerMax_Object = MibTableColumn
apDdAgentRejectedMsgPerMax = _ApDdAgentRejectedMsgPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 9),
    _ApDdAgentRejectedMsgPerMax_Type()
)
apDdAgentRejectedMsgPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentRejectedMsgPerMax.setStatus("current")
_ApDdAgentDroppedMsgRecent_Type = Gauge32
_ApDdAgentDroppedMsgRecent_Object = MibTableColumn
apDdAgentDroppedMsgRecent = _ApDdAgentDroppedMsgRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 10),
    _ApDdAgentDroppedMsgRecent_Type()
)
apDdAgentDroppedMsgRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentDroppedMsgRecent.setStatus("current")
_ApDdAgentDroppedMsgTotal_Type = Counter32
_ApDdAgentDroppedMsgTotal_Object = MibTableColumn
apDdAgentDroppedMsgTotal = _ApDdAgentDroppedMsgTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 11),
    _ApDdAgentDroppedMsgTotal_Type()
)
apDdAgentDroppedMsgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentDroppedMsgTotal.setStatus("current")
_ApDdAgentDroppedMsgPerMax_Type = Counter32
_ApDdAgentDroppedMsgPerMax_Object = MibTableColumn
apDdAgentDroppedMsgPerMax = _ApDdAgentDroppedMsgPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 12),
    _ApDdAgentDroppedMsgPerMax_Type()
)
apDdAgentDroppedMsgPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentDroppedMsgPerMax.setStatus("current")
_ApDdAgentInboundConstraintsRecent_Type = Gauge32
_ApDdAgentInboundConstraintsRecent_Object = MibTableColumn
apDdAgentInboundConstraintsRecent = _ApDdAgentInboundConstraintsRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 13),
    _ApDdAgentInboundConstraintsRecent_Type()
)
apDdAgentInboundConstraintsRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentInboundConstraintsRecent.setStatus("current")
_ApDdAgentInboundConstraintsTotal_Type = Counter32
_ApDdAgentInboundConstraintsTotal_Object = MibTableColumn
apDdAgentInboundConstraintsTotal = _ApDdAgentInboundConstraintsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 14),
    _ApDdAgentInboundConstraintsTotal_Type()
)
apDdAgentInboundConstraintsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentInboundConstraintsTotal.setStatus("current")
_ApDdAgentInboundConstraintsPerMax_Type = Counter32
_ApDdAgentInboundConstraintsPerMax_Object = MibTableColumn
apDdAgentInboundConstraintsPerMax = _ApDdAgentInboundConstraintsPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 15),
    _ApDdAgentInboundConstraintsPerMax_Type()
)
apDdAgentInboundConstraintsPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentInboundConstraintsPerMax.setStatus("current")
_ApDdAgentOutboundConstraintsRecent_Type = Gauge32
_ApDdAgentOutboundConstraintsRecent_Object = MibTableColumn
apDdAgentOutboundConstraintsRecent = _ApDdAgentOutboundConstraintsRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 16),
    _ApDdAgentOutboundConstraintsRecent_Type()
)
apDdAgentOutboundConstraintsRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentOutboundConstraintsRecent.setStatus("current")
_ApDdAgentOutboundConstraintsTotal_Type = Counter32
_ApDdAgentOutboundConstraintsTotal_Object = MibTableColumn
apDdAgentOutboundConstraintsTotal = _ApDdAgentOutboundConstraintsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 17),
    _ApDdAgentOutboundConstraintsTotal_Type()
)
apDdAgentOutboundConstraintsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentOutboundConstraintsTotal.setStatus("current")
_ApDdAgentOutboundConstraintsPerMax_Type = Counter32
_ApDdAgentOutboundConstraintsPerMax_Object = MibTableColumn
apDdAgentOutboundConstraintsPerMax = _ApDdAgentOutboundConstraintsPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 8, 1, 18),
    _ApDdAgentOutboundConstraintsPerMax_Type()
)
apDdAgentOutboundConstraintsPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentOutboundConstraintsPerMax.setStatus("current")
_ApDdAgentMsgTypeStatsTable_Object = MibTable
apDdAgentMsgTypeStatsTable = _ApDdAgentMsgTypeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9)
)
if mibBuilder.loadTexts:
    apDdAgentMsgTypeStatsTable.setStatus("current")
_ApDdAgentMsgTypeStatsEntry_Object = MibTableRow
apDdAgentMsgTypeStatsEntry = _ApDdAgentMsgTypeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1)
)
apDdAgentMsgTypeStatsEntry.setIndexNames(
    (0, "APDD-MIB", "apDdAgentIndex"),
    (0, "APDD-MIB", "apDdMsgTypeIndex"),
)
if mibBuilder.loadTexts:
    apDdAgentMsgTypeStatsEntry.setStatus("current")
_ApDdAgentMsgTypeServerReqRecent_Type = Gauge32
_ApDdAgentMsgTypeServerReqRecent_Object = MibTableColumn
apDdAgentMsgTypeServerReqRecent = _ApDdAgentMsgTypeServerReqRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 3),
    _ApDdAgentMsgTypeServerReqRecent_Type()
)
apDdAgentMsgTypeServerReqRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeServerReqRecent.setStatus("current")
_ApDdAgentMsgTypeServerReqTotal_Type = Counter32
_ApDdAgentMsgTypeServerReqTotal_Object = MibTableColumn
apDdAgentMsgTypeServerReqTotal = _ApDdAgentMsgTypeServerReqTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 4),
    _ApDdAgentMsgTypeServerReqTotal_Type()
)
apDdAgentMsgTypeServerReqTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeServerReqTotal.setStatus("current")
_ApDdAgentMsgTypeServerReqPerMax_Type = Counter32
_ApDdAgentMsgTypeServerReqPerMax_Object = MibTableColumn
apDdAgentMsgTypeServerReqPerMax = _ApDdAgentMsgTypeServerReqPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 5),
    _ApDdAgentMsgTypeServerReqPerMax_Type()
)
apDdAgentMsgTypeServerReqPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeServerReqPerMax.setStatus("current")
_ApDdAgentMsgTypeClientReqRecent_Type = Gauge32
_ApDdAgentMsgTypeClientReqRecent_Object = MibTableColumn
apDdAgentMsgTypeClientReqRecent = _ApDdAgentMsgTypeClientReqRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 6),
    _ApDdAgentMsgTypeClientReqRecent_Type()
)
apDdAgentMsgTypeClientReqRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeClientReqRecent.setStatus("current")
_ApDdAgentMsgTypeClientReqTotal_Type = Counter32
_ApDdAgentMsgTypeClientReqTotal_Object = MibTableColumn
apDdAgentMsgTypeClientReqTotal = _ApDdAgentMsgTypeClientReqTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 7),
    _ApDdAgentMsgTypeClientReqTotal_Type()
)
apDdAgentMsgTypeClientReqTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeClientReqTotal.setStatus("current")
_ApDdAgentMsgTypeClientReqPerMax_Type = Counter32
_ApDdAgentMsgTypeClientReqPerMax_Object = MibTableColumn
apDdAgentMsgTypeClientReqPerMax = _ApDdAgentMsgTypeClientReqPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 8),
    _ApDdAgentMsgTypeClientReqPerMax_Type()
)
apDdAgentMsgTypeClientReqPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeClientReqPerMax.setStatus("current")
_ApDdAgentMsgTypeServerRetransRecent_Type = Gauge32
_ApDdAgentMsgTypeServerRetransRecent_Object = MibTableColumn
apDdAgentMsgTypeServerRetransRecent = _ApDdAgentMsgTypeServerRetransRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 9),
    _ApDdAgentMsgTypeServerRetransRecent_Type()
)
apDdAgentMsgTypeServerRetransRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeServerRetransRecent.setStatus("current")
_ApDdAgentMsgTypeServerRetransTotal_Type = Counter32
_ApDdAgentMsgTypeServerRetransTotal_Object = MibTableColumn
apDdAgentMsgTypeServerRetransTotal = _ApDdAgentMsgTypeServerRetransTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 10),
    _ApDdAgentMsgTypeServerRetransTotal_Type()
)
apDdAgentMsgTypeServerRetransTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeServerRetransTotal.setStatus("current")
_ApDdAgentMsgTypeServerRetransPerMax_Type = Counter32
_ApDdAgentMsgTypeServerRetransPerMax_Object = MibTableColumn
apDdAgentMsgTypeServerRetransPerMax = _ApDdAgentMsgTypeServerRetransPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 11),
    _ApDdAgentMsgTypeServerRetransPerMax_Type()
)
apDdAgentMsgTypeServerRetransPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeServerRetransPerMax.setStatus("current")
_ApDdAgentMsgTypeClientRetransRecent_Type = Gauge32
_ApDdAgentMsgTypeClientRetransRecent_Object = MibTableColumn
apDdAgentMsgTypeClientRetransRecent = _ApDdAgentMsgTypeClientRetransRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 12),
    _ApDdAgentMsgTypeClientRetransRecent_Type()
)
apDdAgentMsgTypeClientRetransRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeClientRetransRecent.setStatus("current")
_ApDdAgentMsgTypeClientRetransTotal_Type = Counter32
_ApDdAgentMsgTypeClientRetransTotal_Object = MibTableColumn
apDdAgentMsgTypeClientRetransTotal = _ApDdAgentMsgTypeClientRetransTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 13),
    _ApDdAgentMsgTypeClientRetransTotal_Type()
)
apDdAgentMsgTypeClientRetransTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeClientRetransTotal.setStatus("current")
_ApDdAgentMsgTypeClientRetransPerMax_Type = Counter32
_ApDdAgentMsgTypeClientRetransPerMax_Object = MibTableColumn
apDdAgentMsgTypeClientRetransPerMax = _ApDdAgentMsgTypeClientRetransPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 14),
    _ApDdAgentMsgTypeClientRetransPerMax_Type()
)
apDdAgentMsgTypeClientRetransPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeClientRetransPerMax.setStatus("current")
_ApDdAgentMsgTypeServerRespRetransRecent_Type = Gauge32
_ApDdAgentMsgTypeServerRespRetransRecent_Object = MibTableColumn
apDdAgentMsgTypeServerRespRetransRecent = _ApDdAgentMsgTypeServerRespRetransRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 15),
    _ApDdAgentMsgTypeServerRespRetransRecent_Type()
)
apDdAgentMsgTypeServerRespRetransRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeServerRespRetransRecent.setStatus("current")
_ApDdAgentMsgTypeServerRespRetransTotal_Type = Counter32
_ApDdAgentMsgTypeServerRespRetransTotal_Object = MibTableColumn
apDdAgentMsgTypeServerRespRetransTotal = _ApDdAgentMsgTypeServerRespRetransTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 16),
    _ApDdAgentMsgTypeServerRespRetransTotal_Type()
)
apDdAgentMsgTypeServerRespRetransTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeServerRespRetransTotal.setStatus("current")
_ApDdAgentMsgTypeServerRespRetransPerMax_Type = Counter32
_ApDdAgentMsgTypeServerRespRetransPerMax_Object = MibTableColumn
apDdAgentMsgTypeServerRespRetransPerMax = _ApDdAgentMsgTypeServerRespRetransPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 17),
    _ApDdAgentMsgTypeServerRespRetransPerMax_Type()
)
apDdAgentMsgTypeServerRespRetransPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeServerRespRetransPerMax.setStatus("current")
_ApDdAgentMsgTypeClientRespRetransRecent_Type = Gauge32
_ApDdAgentMsgTypeClientRespRetransRecent_Object = MibTableColumn
apDdAgentMsgTypeClientRespRetransRecent = _ApDdAgentMsgTypeClientRespRetransRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 21),
    _ApDdAgentMsgTypeClientRespRetransRecent_Type()
)
apDdAgentMsgTypeClientRespRetransRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeClientRespRetransRecent.setStatus("current")
_ApDdAgentMsgTypeClientRespRetransTotal_Type = Counter32
_ApDdAgentMsgTypeClientRespRetransTotal_Object = MibTableColumn
apDdAgentMsgTypeClientRespRetransTotal = _ApDdAgentMsgTypeClientRespRetransTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 22),
    _ApDdAgentMsgTypeClientRespRetransTotal_Type()
)
apDdAgentMsgTypeClientRespRetransTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeClientRespRetransTotal.setStatus("current")
_ApDdAgentMsgTypeClientRespRetransPerMax_Type = Counter32
_ApDdAgentMsgTypeClientRespRetransPerMax_Object = MibTableColumn
apDdAgentMsgTypeClientRespRetransPerMax = _ApDdAgentMsgTypeClientRespRetransPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 23),
    _ApDdAgentMsgTypeClientRespRetransPerMax_Type()
)
apDdAgentMsgTypeClientRespRetransPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeClientRespRetransPerMax.setStatus("current")
_ApDdAgentMsgTypeClientTimeoutRecent_Type = Gauge32
_ApDdAgentMsgTypeClientTimeoutRecent_Object = MibTableColumn
apDdAgentMsgTypeClientTimeoutRecent = _ApDdAgentMsgTypeClientTimeoutRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 27),
    _ApDdAgentMsgTypeClientTimeoutRecent_Type()
)
apDdAgentMsgTypeClientTimeoutRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeClientTimeoutRecent.setStatus("current")
_ApDdAgentMsgTypeClientTimeoutTotal_Type = Counter32
_ApDdAgentMsgTypeClientTimeoutTotal_Object = MibTableColumn
apDdAgentMsgTypeClientTimeoutTotal = _ApDdAgentMsgTypeClientTimeoutTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 28),
    _ApDdAgentMsgTypeClientTimeoutTotal_Type()
)
apDdAgentMsgTypeClientTimeoutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeClientTimeoutTotal.setStatus("current")
_ApDdAgentMsgTypeClientTimeoutPerMax_Type = Counter32
_ApDdAgentMsgTypeClientTimeoutPerMax_Object = MibTableColumn
apDdAgentMsgTypeClientTimeoutPerMax = _ApDdAgentMsgTypeClientTimeoutPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 29),
    _ApDdAgentMsgTypeClientTimeoutPerMax_Type()
)
apDdAgentMsgTypeClientTimeoutPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeClientTimeoutPerMax.setStatus("current")
_ApDdAgentMsgTypeClientThrottledRecent_Type = Gauge32
_ApDdAgentMsgTypeClientThrottledRecent_Object = MibTableColumn
apDdAgentMsgTypeClientThrottledRecent = _ApDdAgentMsgTypeClientThrottledRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 33),
    _ApDdAgentMsgTypeClientThrottledRecent_Type()
)
apDdAgentMsgTypeClientThrottledRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeClientThrottledRecent.setStatus("current")
_ApDdAgentMsgTypeClientThrottledTotal_Type = Counter32
_ApDdAgentMsgTypeClientThrottledTotal_Object = MibTableColumn
apDdAgentMsgTypeClientThrottledTotal = _ApDdAgentMsgTypeClientThrottledTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 34),
    _ApDdAgentMsgTypeClientThrottledTotal_Type()
)
apDdAgentMsgTypeClientThrottledTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeClientThrottledTotal.setStatus("current")
_ApDdAgentMsgTypeClientThrottledPerMax_Type = Counter32
_ApDdAgentMsgTypeClientThrottledPerMax_Object = MibTableColumn
apDdAgentMsgTypeClientThrottledPerMax = _ApDdAgentMsgTypeClientThrottledPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 35),
    _ApDdAgentMsgTypeClientThrottledPerMax_Type()
)
apDdAgentMsgTypeClientThrottledPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeClientThrottledPerMax.setStatus("current")
_ApDdAgentMsgTypeAverageLatency_Type = Gauge32
_ApDdAgentMsgTypeAverageLatency_Object = MibTableColumn
apDdAgentMsgTypeAverageLatency = _ApDdAgentMsgTypeAverageLatency_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 36),
    _ApDdAgentMsgTypeAverageLatency_Type()
)
apDdAgentMsgTypeAverageLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeAverageLatency.setStatus("current")
_ApDdAgentMsgTypeMaximumLatency_Type = Gauge32
_ApDdAgentMsgTypeMaximumLatency_Object = MibTableColumn
apDdAgentMsgTypeMaximumLatency = _ApDdAgentMsgTypeMaximumLatency_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 37),
    _ApDdAgentMsgTypeMaximumLatency_Type()
)
apDdAgentMsgTypeMaximumLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeMaximumLatency.setStatus("current")
_ApDdAgentMsgTypeLatencyWindow_Type = Integer32
_ApDdAgentMsgTypeLatencyWindow_Object = MibTableColumn
apDdAgentMsgTypeLatencyWindow = _ApDdAgentMsgTypeLatencyWindow_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 9, 1, 38),
    _ApDdAgentMsgTypeLatencyWindow_Type()
)
apDdAgentMsgTypeLatencyWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeLatencyWindow.setStatus("current")
if mibBuilder.loadTexts:
    apDdAgentMsgTypeLatencyWindow.setUnits("second")
_ApDdAgentMsgStatsReturnCodeTable_Object = MibTable
apDdAgentMsgStatsReturnCodeTable = _ApDdAgentMsgStatsReturnCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 10)
)
if mibBuilder.loadTexts:
    apDdAgentMsgStatsReturnCodeTable.setStatus("current")
_ApDdAgentMsgStatsReturnCodeEntry_Object = MibTableRow
apDdAgentMsgStatsReturnCodeEntry = _ApDdAgentMsgStatsReturnCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 10, 1)
)
apDdAgentMsgStatsReturnCodeEntry.setIndexNames(
    (0, "APDD-MIB", "apDdAgentIndex"),
    (0, "APDD-MIB", "apDdMsgTypeIndex"),
    (0, "APDD-MIB", "apDdMsgReturnCodeIndex"),
)
if mibBuilder.loadTexts:
    apDdAgentMsgStatsReturnCodeEntry.setStatus("current")
_ApDdAgentMsgReturnCodeServerRecent_Type = Gauge32
_ApDdAgentMsgReturnCodeServerRecent_Object = MibTableColumn
apDdAgentMsgReturnCodeServerRecent = _ApDdAgentMsgReturnCodeServerRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 10, 1, 3),
    _ApDdAgentMsgReturnCodeServerRecent_Type()
)
apDdAgentMsgReturnCodeServerRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgReturnCodeServerRecent.setStatus("current")
_ApDdAgentMsgReturnCodeServerTotal_Type = Counter32
_ApDdAgentMsgReturnCodeServerTotal_Object = MibTableColumn
apDdAgentMsgReturnCodeServerTotal = _ApDdAgentMsgReturnCodeServerTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 10, 1, 4),
    _ApDdAgentMsgReturnCodeServerTotal_Type()
)
apDdAgentMsgReturnCodeServerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgReturnCodeServerTotal.setStatus("current")
_ApDdAgentMsgReturnCodeServerPerMax_Type = Counter32
_ApDdAgentMsgReturnCodeServerPerMax_Object = MibTableColumn
apDdAgentMsgReturnCodeServerPerMax = _ApDdAgentMsgReturnCodeServerPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 10, 1, 5),
    _ApDdAgentMsgReturnCodeServerPerMax_Type()
)
apDdAgentMsgReturnCodeServerPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgReturnCodeServerPerMax.setStatus("current")
_ApDdAgentMsgReturnCodeClientRecent_Type = Gauge32
_ApDdAgentMsgReturnCodeClientRecent_Object = MibTableColumn
apDdAgentMsgReturnCodeClientRecent = _ApDdAgentMsgReturnCodeClientRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 10, 1, 6),
    _ApDdAgentMsgReturnCodeClientRecent_Type()
)
apDdAgentMsgReturnCodeClientRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgReturnCodeClientRecent.setStatus("current")
_ApDdAgentMsgReturnCodeClientTotal_Type = Counter32
_ApDdAgentMsgReturnCodeClientTotal_Object = MibTableColumn
apDdAgentMsgReturnCodeClientTotal = _ApDdAgentMsgReturnCodeClientTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 10, 1, 7),
    _ApDdAgentMsgReturnCodeClientTotal_Type()
)
apDdAgentMsgReturnCodeClientTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgReturnCodeClientTotal.setStatus("current")
_ApDdAgentMsgReturnCodeClientPerMax_Type = Counter32
_ApDdAgentMsgReturnCodeClientPerMax_Object = MibTableColumn
apDdAgentMsgReturnCodeClientPerMax = _ApDdAgentMsgReturnCodeClientPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 1, 2, 10, 1, 8),
    _ApDdAgentMsgReturnCodeClientPerMax_Type()
)
apDdAgentMsgReturnCodeClientPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDdAgentMsgReturnCodeClientPerMax.setStatus("current")
_ApDDNotificationObjects_ObjectIdentity = ObjectIdentity
apDDNotificationObjects = _ApDDNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 2)
)
_ApDDNotifObjects_ObjectIdentity = ObjectIdentity
apDDNotifObjects = _ApDDNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 2, 1)
)


class _ApDdDiameterAgentHostName_Type(DisplayString):
    """Custom type apDdDiameterAgentHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApDdDiameterAgentHostName_Type.__name__ = "DisplayString"
_ApDdDiameterAgentHostName_Object = MibScalar
apDdDiameterAgentHostName = _ApDdDiameterAgentHostName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 2, 1, 1),
    _ApDdDiameterAgentHostName_Type()
)
apDdDiameterAgentHostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDdDiameterAgentHostName.setStatus("current")


class _ApDdDiameterIPPort_Type(DisplayString):
    """Custom type apDdDiameterIPPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApDdDiameterIPPort_Type.__name__ = "DisplayString"
_ApDdDiameterIPPort_Object = MibScalar
apDdDiameterIPPort = _ApDdDiameterIPPort_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 2, 1, 2),
    _ApDdDiameterIPPort_Type()
)
apDdDiameterIPPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDdDiameterIPPort.setStatus("current")


class _ApDdDiameterAgentOriginHostName_Type(DisplayString):
    """Custom type apDdDiameterAgentOriginHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApDdDiameterAgentOriginHostName_Type.__name__ = "DisplayString"
_ApDdDiameterAgentOriginHostName_Object = MibScalar
apDdDiameterAgentOriginHostName = _ApDdDiameterAgentOriginHostName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 2, 1, 3),
    _ApDdDiameterAgentOriginHostName_Type()
)
apDdDiameterAgentOriginHostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDdDiameterAgentOriginHostName.setStatus("current")


class _ApDdDiameterAgentOriginRealmName_Type(DisplayString):
    """Custom type apDdDiameterAgentOriginRealmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApDdDiameterAgentOriginRealmName_Type.__name__ = "DisplayString"
_ApDdDiameterAgentOriginRealmName_Object = MibScalar
apDdDiameterAgentOriginRealmName = _ApDdDiameterAgentOriginRealmName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 2, 1, 4),
    _ApDdDiameterAgentOriginRealmName_Type()
)
apDdDiameterAgentOriginRealmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDdDiameterAgentOriginRealmName.setStatus("current")
_ApDdTransportType_Type = ApTransportType
_ApDdTransportType_Object = MibScalar
apDdTransportType = _ApDdTransportType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 2, 1, 5),
    _ApDdTransportType_Type()
)
apDdTransportType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDdTransportType.setStatus("current")


class _ApDdInterfaceStatusReason_Type(Integer32):
    """Custom type apDdInterfaceStatusReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("diameterAgentUnreachable", 1),
          ("disconnectByRequest", 0),
          ("transportFailure", 2))
    )


_ApDdInterfaceStatusReason_Type.__name__ = "Integer32"
_ApDdInterfaceStatusReason_Object = MibScalar
apDdInterfaceStatusReason = _ApDdInterfaceStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 2, 1, 6),
    _ApDdInterfaceStatusReason_Type()
)
apDdInterfaceStatusReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDdInterfaceStatusReason.setStatus("current")
_ApDDNotifPrefix_ObjectIdentity = ObjectIdentity
apDDNotifPrefix = _ApDDNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 2, 2)
)
_ApDDNotifications_ObjectIdentity = ObjectIdentity
apDDNotifications = _ApDDNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 2, 2, 0)
)
_ApDDConformance_ObjectIdentity = ObjectIdentity
apDDConformance = _ApDDConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 3)
)
_ApDDObjectGroups_ObjectIdentity = ObjectIdentity
apDDObjectGroups = _ApDDObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 3, 1)
)
_ApDDNotificationGroups_ObjectIdentity = ObjectIdentity
apDDNotificationGroups = _ApDDNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 3, 2)
)

# Managed Objects groups

apDdGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 3, 1, 1)
)
apDdGeneralGroup.setObjects(
      *(("APDD-MIB", "apDdInterfaceNumber"),
        ("APDD-MIB", "apDdCurrentTransRate"),
        ("APDD-MIB", "apDdHighTransRate"),
        ("APDD-MIB", "apDdLowTransRate"))
)
if mibBuilder.loadTexts:
    apDdGeneralGroup.setStatus("current")

apDdInterfaceStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 3, 1, 2)
)
apDdInterfaceStatsGroup.setObjects(
      *(("APDD-MIB", "apDdInterfaceRealmName"),
        ("APDD-MIB", "apDdClientTransCPActive"),
        ("APDD-MIB", "apDdClientTransCPHigh"),
        ("APDD-MIB", "apDdClientTransCPTotal"),
        ("APDD-MIB", "apDdClientTransLTTotal"),
        ("APDD-MIB", "apDdClientTransLTPerMax"),
        ("APDD-MIB", "apDdClientTransLTHigh"),
        ("APDD-MIB", "apDdServerTransCPActive"),
        ("APDD-MIB", "apDdServerTransCPHigh"),
        ("APDD-MIB", "apDdServerTransCPTotal"),
        ("APDD-MIB", "apDdServerTransLTTotal"),
        ("APDD-MIB", "apDdServerTransLTPerMax"),
        ("APDD-MIB", "apDdServerTransLTHigh"),
        ("APDD-MIB", "apDdGenSocketsCPActive"),
        ("APDD-MIB", "apDdGenSocketsCPHigh"),
        ("APDD-MIB", "apDdGenSocketsCPTotal"),
        ("APDD-MIB", "apDdGenSocketsLTTotal"),
        ("APDD-MIB", "apDdGenSocketsLTPerMax"),
        ("APDD-MIB", "apDdGenSocketsLTHigh"),
        ("APDD-MIB", "apDdGenConnectsCPActive"),
        ("APDD-MIB", "apDdGenConnectsCPHigh"),
        ("APDD-MIB", "apDdGenConnectsCPTotal"),
        ("APDD-MIB", "apDdGenConnectsLTTotal"),
        ("APDD-MIB", "apDdGenConnectsLTPerMax"),
        ("APDD-MIB", "apDdGenConnectsLTHigh"))
)
if mibBuilder.loadTexts:
    apDdInterfaceStatsGroup.setStatus("current")

apDdErrorStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 3, 1, 3)
)
apDdErrorStatusGroup.setObjects(
      *(("APDD-MIB", "apDdNoRouteFoundRecent"),
        ("APDD-MIB", "apDdNoRouteFoundTotal"),
        ("APDD-MIB", "apDdNoRouteFoundPerMax"),
        ("APDD-MIB", "apDdMalformedMsgRecent"),
        ("APDD-MIB", "apDdMalformedMsgTotal"),
        ("APDD-MIB", "apDdMalformedMsgPerMax"))
)
if mibBuilder.loadTexts:
    apDdErrorStatusGroup.setStatus("current")

apDdMsgTypeStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 3, 1, 4)
)
apDdMsgTypeStatsGroup.setObjects(
      *(("APDD-MIB", "apDdMsgTypeMsgName"),
        ("APDD-MIB", "apDdMsgTypeServerReqRecent"),
        ("APDD-MIB", "apDdMsgTypeServerReqTotal"),
        ("APDD-MIB", "apDdMsgTypeServerReqPerMax"),
        ("APDD-MIB", "apDdMsgTypeClientReqRecent"),
        ("APDD-MIB", "apDdMsgTypeClientReqTotal"),
        ("APDD-MIB", "apDdMsgTypeClientReqPerMax"),
        ("APDD-MIB", "apDdMsgTypeServerRetransRecent"),
        ("APDD-MIB", "apDdMsgTypeServerRetransTotal"),
        ("APDD-MIB", "apDdMsgTypeServerRetransPerMax"),
        ("APDD-MIB", "apDdMsgTypeClientRetransRecent"),
        ("APDD-MIB", "apDdMsgTypeClientRetransTotal"),
        ("APDD-MIB", "apDdMsgTypeClientRetransPerMax"),
        ("APDD-MIB", "apDdMsgTypeServerRespRetransRecent"),
        ("APDD-MIB", "apDdMsgTypeServerRespRetransTotal"),
        ("APDD-MIB", "apDdMsgTypeServerRespRetransPerMax"),
        ("APDD-MIB", "apDdMsgTypeClientRespRetransRecent"),
        ("APDD-MIB", "apDdMsgTypeClientRespRetransTotal"),
        ("APDD-MIB", "apDdMsgTypeClientRespRetransPerMax"),
        ("APDD-MIB", "apDdMsgTypeClientTimeoutRecent"),
        ("APDD-MIB", "apDdMsgTypeClientTimeoutTotal"),
        ("APDD-MIB", "apDdMsgTypeClientTimeoutPerMax"),
        ("APDD-MIB", "apDdMsgTypeClientThrottledRecent"),
        ("APDD-MIB", "apDdMsgTypeClientThrottledTotal"),
        ("APDD-MIB", "apDdMsgTypeClientThrottledPerMax"),
        ("APDD-MIB", "apDdMsgTypeAverageLatency"),
        ("APDD-MIB", "apDdMsgTypeMaximumLatency"),
        ("APDD-MIB", "apDdMsgTypeLatencyWindow"))
)
if mibBuilder.loadTexts:
    apDdMsgTypeStatsGroup.setStatus("current")

apDdMsgStatsReturnCodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 3, 1, 5)
)
apDdMsgStatsReturnCodeGroup.setObjects(
      *(("APDD-MIB", "apDdMsgReturnCodeName"),
        ("APDD-MIB", "apDdMsgReturnCodeServerRecent"),
        ("APDD-MIB", "apDdMsgReturnCodeServerTotal"),
        ("APDD-MIB", "apDdMsgReturnCodeServerPerMax"),
        ("APDD-MIB", "apDdMsgReturnCodeClientRecent"),
        ("APDD-MIB", "apDdMsgReturnCodeClientTotal"),
        ("APDD-MIB", "apDdMsgReturnCodeClientPerMax"))
)
if mibBuilder.loadTexts:
    apDdMsgStatsReturnCodeGroup.setStatus("current")

apDdIntfErrorStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 3, 1, 6)
)
apDdIntfErrorStatusGroup.setObjects(
      *(("APDD-MIB", "apDdRejectedMsgRecent"),
        ("APDD-MIB", "apDdRejectedMsgTotal"),
        ("APDD-MIB", "apDdRejectedMsgPerMax"),
        ("APDD-MIB", "apDdDroppedMsgRecent"),
        ("APDD-MIB", "apDdDroppedMsgTotal"),
        ("APDD-MIB", "apDdDroppedMsgPerMax"),
        ("APDD-MIB", "apDdInboundConstraintsRecent"),
        ("APDD-MIB", "apDdInboundConstraintsTotal"),
        ("APDD-MIB", "apDdInboundConstraintsPerMax"),
        ("APDD-MIB", "apDdOutboundConstraintsRecent"),
        ("APDD-MIB", "apDdOutboundConstraintsTotal"),
        ("APDD-MIB", "apDdOutboundConstraintsPerMax"))
)
if mibBuilder.loadTexts:
    apDdIntfErrorStatusGroup.setStatus("current")

apDdAgentGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 3, 1, 7)
)
apDdAgentGeneralGroup.setObjects(
    ("APDD-MIB", "apDdAgentNumber")
)
if mibBuilder.loadTexts:
    apDdAgentGeneralGroup.setStatus("current")

apDdAgentStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 3, 1, 8)
)
apDdAgentStatsGroup.setObjects(
      *(("APDD-MIB", "apDdAgentRealmName"),
        ("APDD-MIB", "apDdAgentClientTransCPActive"),
        ("APDD-MIB", "apDdAgentClientTransCPHigh"),
        ("APDD-MIB", "apDdAgentClientTransCPTotal"),
        ("APDD-MIB", "apDdAgentClientTransLTTotal"),
        ("APDD-MIB", "apDdAgentClientTransLTPerMax"),
        ("APDD-MIB", "apDdAgentClientTransLTHigh"),
        ("APDD-MIB", "apDdAgentServerTransCPActive"),
        ("APDD-MIB", "apDdAgentServerTransCPHigh"),
        ("APDD-MIB", "apDdAgentServerTransCPTotal"),
        ("APDD-MIB", "apDdAgentServerTransLTTotal"),
        ("APDD-MIB", "apDdAgentServerTransLTPerMax"),
        ("APDD-MIB", "apDdAgentServerTransLTHigh"),
        ("APDD-MIB", "apDdAgentGenSocketsCPActive"),
        ("APDD-MIB", "apDdAgentGenSocketsCPHigh"),
        ("APDD-MIB", "apDdAgentGenSocketsCPTotal"),
        ("APDD-MIB", "apDdAgentGenSocketsLTTotal"),
        ("APDD-MIB", "apDdAgentGenSocketsLTPerMax"),
        ("APDD-MIB", "apDdAgentGenSocketsLTHigh"),
        ("APDD-MIB", "apDdAgentGenConnectsCPActive"),
        ("APDD-MIB", "apDdAgentGenConnectsCPHigh"),
        ("APDD-MIB", "apDdAgentGenConnectsCPTotal"),
        ("APDD-MIB", "apDdAgentGenConnectsLTTotal"),
        ("APDD-MIB", "apDdAgentGenConnectsLTPerMax"),
        ("APDD-MIB", "apDdAgentGenConnectsLTHigh"))
)
if mibBuilder.loadTexts:
    apDdAgentStatsGroup.setStatus("current")

apDdAgentErrorStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 3, 1, 9)
)
apDdAgentErrorStatusGroup.setObjects(
      *(("APDD-MIB", "apDdAgentNoRouteFoundRecent"),
        ("APDD-MIB", "apDdAgentNoRouteFoundTotal"),
        ("APDD-MIB", "apDdAgentNoRouteFoundPerMax"),
        ("APDD-MIB", "apDdAgentMalformedMsgRecent"),
        ("APDD-MIB", "apDdAgentMalformedMsgTotal"),
        ("APDD-MIB", "apDdAgentMalformedMsgPerMax"),
        ("APDD-MIB", "apDdAgentRejectedMsgRecent"),
        ("APDD-MIB", "apDdAgentRejectedMsgTotal"),
        ("APDD-MIB", "apDdAgentRejectedMsgPerMax"),
        ("APDD-MIB", "apDdAgentDroppedMsgRecent"),
        ("APDD-MIB", "apDdAgentDroppedMsgTotal"),
        ("APDD-MIB", "apDdAgentDroppedMsgPerMax"),
        ("APDD-MIB", "apDdAgentInboundConstraintsRecent"),
        ("APDD-MIB", "apDdAgentInboundConstraintsTotal"),
        ("APDD-MIB", "apDdAgentInboundConstraintsPerMax"),
        ("APDD-MIB", "apDdAgentOutboundConstraintsRecent"),
        ("APDD-MIB", "apDdAgentOutboundConstraintsTotal"),
        ("APDD-MIB", "apDdAgentOutboundConstraintsPerMax"))
)
if mibBuilder.loadTexts:
    apDdAgentErrorStatusGroup.setStatus("current")

apDdAgentMsgTypeStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 3, 1, 10)
)
apDdAgentMsgTypeStatsGroup.setObjects(
      *(("APDD-MIB", "apDdMsgTypeMsgName"),
        ("APDD-MIB", "apDdAgentMsgTypeServerReqRecent"),
        ("APDD-MIB", "apDdAgentMsgTypeServerReqTotal"),
        ("APDD-MIB", "apDdAgentMsgTypeServerReqPerMax"),
        ("APDD-MIB", "apDdAgentMsgTypeClientReqRecent"),
        ("APDD-MIB", "apDdAgentMsgTypeClientReqTotal"),
        ("APDD-MIB", "apDdAgentMsgTypeClientReqPerMax"),
        ("APDD-MIB", "apDdAgentMsgTypeServerRetransRecent"),
        ("APDD-MIB", "apDdAgentMsgTypeServerRetransTotal"),
        ("APDD-MIB", "apDdAgentMsgTypeServerRetransPerMax"),
        ("APDD-MIB", "apDdAgentMsgTypeClientRetransRecent"),
        ("APDD-MIB", "apDdAgentMsgTypeClientRetransTotal"),
        ("APDD-MIB", "apDdAgentMsgTypeClientRetransPerMax"),
        ("APDD-MIB", "apDdAgentMsgTypeServerRespRetransRecent"),
        ("APDD-MIB", "apDdAgentMsgTypeServerRespRetransTotal"),
        ("APDD-MIB", "apDdAgentMsgTypeServerRespRetransPerMax"),
        ("APDD-MIB", "apDdAgentMsgTypeClientRespRetransRecent"),
        ("APDD-MIB", "apDdAgentMsgTypeClientRespRetransTotal"),
        ("APDD-MIB", "apDdAgentMsgTypeClientRespRetransPerMax"),
        ("APDD-MIB", "apDdAgentMsgTypeClientTimeoutRecent"),
        ("APDD-MIB", "apDdAgentMsgTypeClientTimeoutTotal"),
        ("APDD-MIB", "apDdAgentMsgTypeClientTimeoutPerMax"),
        ("APDD-MIB", "apDdAgentMsgTypeClientThrottledRecent"),
        ("APDD-MIB", "apDdAgentMsgTypeClientThrottledTotal"),
        ("APDD-MIB", "apDdAgentMsgTypeClientThrottledPerMax"),
        ("APDD-MIB", "apDdAgentMsgTypeAverageLatency"),
        ("APDD-MIB", "apDdAgentMsgTypeMaximumLatency"),
        ("APDD-MIB", "apDdAgentMsgTypeLatencyWindow"))
)
if mibBuilder.loadTexts:
    apDdAgentMsgTypeStatsGroup.setStatus("current")

apDdAgentMsgStatsReturnCodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 3, 1, 11)
)
apDdAgentMsgStatsReturnCodeGroup.setObjects(
      *(("APDD-MIB", "apDdMsgReturnCodeName"),
        ("APDD-MIB", "apDdAgentMsgReturnCodeServerRecent"),
        ("APDD-MIB", "apDdAgentMsgReturnCodeServerTotal"),
        ("APDD-MIB", "apDdAgentMsgReturnCodeServerPerMax"),
        ("APDD-MIB", "apDdAgentMsgReturnCodeClientRecent"),
        ("APDD-MIB", "apDdAgentMsgReturnCodeClientTotal"),
        ("APDD-MIB", "apDdAgentMsgReturnCodeClientPerMax"))
)
if mibBuilder.loadTexts:
    apDdAgentMsgStatsReturnCodeGroup.setStatus("current")

apDdSessionSubscriberGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 3, 1, 12)
)
apDdSessionSubscriberGeneralGroup.setObjects(
      *(("APDD-MIB", "apDdSessionPeriodActive"),
        ("APDD-MIB", "apDdSessionPeriodHigh"),
        ("APDD-MIB", "apDdSessionPeriodTotal"),
        ("APDD-MIB", "apDdSessionLifeTotal"),
        ("APDD-MIB", "apDdSessionLifePerMax"),
        ("APDD-MIB", "apDdSessionLifeHigh"),
        ("APDD-MIB", "apDdSessInitPeriodActive"),
        ("APDD-MIB", "apDdSessInitPeriodHigh"),
        ("APDD-MIB", "apDdSessInitPeriodTotal"),
        ("APDD-MIB", "apDdSessInitLifeTotal"),
        ("APDD-MIB", "apDdSessInitLifePerMax"),
        ("APDD-MIB", "apDdSessInitLifeHigh"),
        ("APDD-MIB", "apDdSessEstablishedPeriodActive"),
        ("APDD-MIB", "apDdSessEstablishedPeriodHigh"),
        ("APDD-MIB", "apDdSessEstablishedPeriodTotal"),
        ("APDD-MIB", "apDdSessEstablishedLifeTotal"),
        ("APDD-MIB", "apDdSessEstablishedLifePerMax"),
        ("APDD-MIB", "apDdSessEstablishedLifeHigh"),
        ("APDD-MIB", "apDdSessTerminatedPeriodActive"),
        ("APDD-MIB", "apDdSessTerminatedPeriodHigh"),
        ("APDD-MIB", "apDdSessTerminatedPeriodTotal"),
        ("APDD-MIB", "apDdSessTerminatedLifeTotal"),
        ("APDD-MIB", "apDdSessTerminatedLifePerMax"),
        ("APDD-MIB", "apDdSessTerminatedLifeHigh"),
        ("APDD-MIB", "apDdSessTimeoutPeriodTotal"),
        ("APDD-MIB", "apDdSessTimeoutLifeTotal"),
        ("APDD-MIB", "apDdSessTimeoutLifePerMax"),
        ("APDD-MIB", "apDdSessErrorsPeriodTotal"),
        ("APDD-MIB", "apDdSessErrorsLifeTotal"),
        ("APDD-MIB", "apDdSessErrorsLifePerMax"),
        ("APDD-MIB", "apDdSessMissPeriodTotal"),
        ("APDD-MIB", "apDdSessMissLifeTotal"),
        ("APDD-MIB", "apDdSessMissLifePerMax"),
        ("APDD-MIB", "apDdSubscriberPeriodActive"),
        ("APDD-MIB", "apDdSubscriberPeriodHigh"),
        ("APDD-MIB", "apDdSubscriberPeriodTotal"),
        ("APDD-MIB", "apDdSubscriberLifeTotal"),
        ("APDD-MIB", "apDdSubscriberLifePerMax"),
        ("APDD-MIB", "apDdSubscriberLifeHigh"),
        ("APDD-MIB", "apDdSubscribePeriodActive"),
        ("APDD-MIB", "apDdSubscribePeriodHigh"),
        ("APDD-MIB", "apDdSubscribePeriodTotal"),
        ("APDD-MIB", "apDdSubscribeLifeTotal"),
        ("APDD-MIB", "apDdSubscribeLifePerMax"),
        ("APDD-MIB", "apDdSubscribeLifeHigh"),
        ("APDD-MIB", "apDdUnsubscribePeriodActive"),
        ("APDD-MIB", "apDdUnsubscribePeriodHigh"),
        ("APDD-MIB", "apDdUnsubscribePeriodTotal"),
        ("APDD-MIB", "apDdUnsubscribeLifeTotal"),
        ("APDD-MIB", "apDdUnsubscribeLifePerMax"),
        ("APDD-MIB", "apDdUnsubscribeLifeHigh"),
        ("APDD-MIB", "apDdPolicyHitPeriodActive"),
        ("APDD-MIB", "apDdPolicyHitPeriodHigh"),
        ("APDD-MIB", "apDdPolicyHitPeriodTotal"),
        ("APDD-MIB", "apDdPolicyHitLifeTotal"),
        ("APDD-MIB", "apDdPolicyHitLifePerMax"),
        ("APDD-MIB", "apDdPolicyHitLifeHigh"),
        ("APDD-MIB", "apDdPolicyMissPeriodActive"),
        ("APDD-MIB", "apDdPolicyMissPeriodHigh"),
        ("APDD-MIB", "apDdPolicyMissPeriodTotal"),
        ("APDD-MIB", "apDdPolicyMissLifeTotal"),
        ("APDD-MIB", "apDdPolicyMissLifePerMax"),
        ("APDD-MIB", "apDdPolicyMissLifeHigh"),
        ("APDD-MIB", "apDdSubscriberMissPeriodTotal"),
        ("APDD-MIB", "apDdSubscriberMissLifeTotal"),
        ("APDD-MIB", "apDdSubscriberMissLifePerMax"))
)
if mibBuilder.loadTexts:
    apDdSessionSubscriberGeneralGroup.setStatus("current")

apDDNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 3, 2, 1)
)
apDDNotifObjectsGroup.setObjects(
      *(("APDD-MIB", "apDdDiameterAgentHostName"),
        ("APDD-MIB", "apDdDiameterIPPort"),
        ("APDD-MIB", "apDdDiameterAgentOriginHostName"),
        ("APDD-MIB", "apDdDiameterAgentOriginRealmName"),
        ("APDD-MIB", "apDdTransportType"),
        ("APDD-MIB", "apDdInterfaceStatusReason"))
)
if mibBuilder.loadTexts:
    apDDNotifObjectsGroup.setStatus("current")


# Notification objects

apDdConnectionFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 2, 2, 0, 1)
)
apDdConnectionFailureTrap.setObjects(
      *(("APDD-MIB", "apDdInterfaceRealmName"),
        ("APDD-MIB", "apDdDiameterAgentHostName"),
        ("APDD-MIB", "apDdDiameterIPPort"),
        ("APDD-MIB", "apDdDiameterAgentOriginHostName"),
        ("APDD-MIB", "apDdDiameterAgentOriginRealmName"),
        ("APDD-MIB", "apDdTransportType"),
        ("APDD-MIB", "apDdInterfaceStatusReason"))
)
if mibBuilder.loadTexts:
    apDdConnectionFailureTrap.setStatus(
        "current"
    )

apDdConnectionFailureClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 2, 2, 0, 2)
)
apDdConnectionFailureClearTrap.setObjects(
      *(("APDD-MIB", "apDdInterfaceRealmName"),
        ("APDD-MIB", "apDdDiameterAgentHostName"),
        ("APDD-MIB", "apDdDiameterIPPort"),
        ("APDD-MIB", "apDdDiameterAgentOriginHostName"),
        ("APDD-MIB", "apDdDiameterAgentOriginRealmName"),
        ("APDD-MIB", "apDdTransportType"),
        ("APDD-MIB", "apDdInterfaceStatusReason"))
)
if mibBuilder.loadTexts:
    apDdConnectionFailureClearTrap.setStatus(
        "current"
    )


# Notifications groups

apDDNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 12, 3, 2, 2)
)
apDDNotificationsGroup.setObjects(
      *(("APDD-MIB", "apDdConnectionFailureTrap"),
        ("APDD-MIB", "apDdConnectionFailureClearTrap"))
)
if mibBuilder.loadTexts:
    apDDNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APDD-MIB",
    **{"apDDModule": apDDModule,
       "apDDMIBObjects": apDDMIBObjects,
       "apDDMIBGeneralObjects": apDDMIBGeneralObjects,
       "apDdInterfaceNumber": apDdInterfaceNumber,
       "apDdCurrentTransRate": apDdCurrentTransRate,
       "apDdHighTransRate": apDdHighTransRate,
       "apDdLowTransRate": apDdLowTransRate,
       "apDdAgentNumber": apDdAgentNumber,
       "apDdSessionPeriodActive": apDdSessionPeriodActive,
       "apDdSessionPeriodHigh": apDdSessionPeriodHigh,
       "apDdSessionPeriodTotal": apDdSessionPeriodTotal,
       "apDdSessionLifeTotal": apDdSessionLifeTotal,
       "apDdSessionLifePerMax": apDdSessionLifePerMax,
       "apDdSessionLifeHigh": apDdSessionLifeHigh,
       "apDdSessInitPeriodActive": apDdSessInitPeriodActive,
       "apDdSessInitPeriodHigh": apDdSessInitPeriodHigh,
       "apDdSessInitPeriodTotal": apDdSessInitPeriodTotal,
       "apDdSessInitLifeTotal": apDdSessInitLifeTotal,
       "apDdSessInitLifePerMax": apDdSessInitLifePerMax,
       "apDdSessInitLifeHigh": apDdSessInitLifeHigh,
       "apDdSessEstablishedPeriodActive": apDdSessEstablishedPeriodActive,
       "apDdSessEstablishedPeriodHigh": apDdSessEstablishedPeriodHigh,
       "apDdSessEstablishedPeriodTotal": apDdSessEstablishedPeriodTotal,
       "apDdSessEstablishedLifeTotal": apDdSessEstablishedLifeTotal,
       "apDdSessEstablishedLifePerMax": apDdSessEstablishedLifePerMax,
       "apDdSessEstablishedLifeHigh": apDdSessEstablishedLifeHigh,
       "apDdSessTerminatedPeriodActive": apDdSessTerminatedPeriodActive,
       "apDdSessTerminatedPeriodHigh": apDdSessTerminatedPeriodHigh,
       "apDdSessTerminatedPeriodTotal": apDdSessTerminatedPeriodTotal,
       "apDdSessTerminatedLifeTotal": apDdSessTerminatedLifeTotal,
       "apDdSessTerminatedLifePerMax": apDdSessTerminatedLifePerMax,
       "apDdSessTerminatedLifeHigh": apDdSessTerminatedLifeHigh,
       "apDdSessTimeoutPeriodTotal": apDdSessTimeoutPeriodTotal,
       "apDdSessTimeoutLifeTotal": apDdSessTimeoutLifeTotal,
       "apDdSessTimeoutLifePerMax": apDdSessTimeoutLifePerMax,
       "apDdSessErrorsPeriodTotal": apDdSessErrorsPeriodTotal,
       "apDdSessErrorsLifeTotal": apDdSessErrorsLifeTotal,
       "apDdSessErrorsLifePerMax": apDdSessErrorsLifePerMax,
       "apDdSessMissPeriodTotal": apDdSessMissPeriodTotal,
       "apDdSessMissLifeTotal": apDdSessMissLifeTotal,
       "apDdSessMissLifePerMax": apDdSessMissLifePerMax,
       "apDdSubscriberPeriodActive": apDdSubscriberPeriodActive,
       "apDdSubscriberPeriodHigh": apDdSubscriberPeriodHigh,
       "apDdSubscriberPeriodTotal": apDdSubscriberPeriodTotal,
       "apDdSubscriberLifeTotal": apDdSubscriberLifeTotal,
       "apDdSubscriberLifePerMax": apDdSubscriberLifePerMax,
       "apDdSubscriberLifeHigh": apDdSubscriberLifeHigh,
       "apDdSubscribePeriodActive": apDdSubscribePeriodActive,
       "apDdSubscribePeriodHigh": apDdSubscribePeriodHigh,
       "apDdSubscribePeriodTotal": apDdSubscribePeriodTotal,
       "apDdSubscribeLifeTotal": apDdSubscribeLifeTotal,
       "apDdSubscribeLifePerMax": apDdSubscribeLifePerMax,
       "apDdSubscribeLifeHigh": apDdSubscribeLifeHigh,
       "apDdUnsubscribePeriodActive": apDdUnsubscribePeriodActive,
       "apDdUnsubscribePeriodHigh": apDdUnsubscribePeriodHigh,
       "apDdUnsubscribePeriodTotal": apDdUnsubscribePeriodTotal,
       "apDdUnsubscribeLifeTotal": apDdUnsubscribeLifeTotal,
       "apDdUnsubscribeLifePerMax": apDdUnsubscribeLifePerMax,
       "apDdUnsubscribeLifeHigh": apDdUnsubscribeLifeHigh,
       "apDdPolicyHitPeriodActive": apDdPolicyHitPeriodActive,
       "apDdPolicyHitPeriodHigh": apDdPolicyHitPeriodHigh,
       "apDdPolicyHitPeriodTotal": apDdPolicyHitPeriodTotal,
       "apDdPolicyHitLifeTotal": apDdPolicyHitLifeTotal,
       "apDdPolicyHitLifePerMax": apDdPolicyHitLifePerMax,
       "apDdPolicyHitLifeHigh": apDdPolicyHitLifeHigh,
       "apDdPolicyMissPeriodActive": apDdPolicyMissPeriodActive,
       "apDdPolicyMissPeriodHigh": apDdPolicyMissPeriodHigh,
       "apDdPolicyMissPeriodTotal": apDdPolicyMissPeriodTotal,
       "apDdPolicyMissLifeTotal": apDdPolicyMissLifeTotal,
       "apDdPolicyMissLifePerMax": apDdPolicyMissLifePerMax,
       "apDdPolicyMissLifeHigh": apDdPolicyMissLifeHigh,
       "apDdSubscriberMissPeriodTotal": apDdSubscriberMissPeriodTotal,
       "apDdSubscriberMissLifeTotal": apDdSubscriberMissLifeTotal,
       "apDdSubscriberMissLifePerMax": apDdSubscriberMissLifePerMax,
       "apDDMIBTabularObjects": apDDMIBTabularObjects,
       "apDdInterfaceStatsTable": apDdInterfaceStatsTable,
       "apDdInterfaceStatsEntry": apDdInterfaceStatsEntry,
       "apDdInterfaceIndex": apDdInterfaceIndex,
       "apDdInterfaceRealmName": apDdInterfaceRealmName,
       "apDdClientTransCPActive": apDdClientTransCPActive,
       "apDdClientTransCPHigh": apDdClientTransCPHigh,
       "apDdClientTransCPTotal": apDdClientTransCPTotal,
       "apDdClientTransLTTotal": apDdClientTransLTTotal,
       "apDdClientTransLTPerMax": apDdClientTransLTPerMax,
       "apDdClientTransLTHigh": apDdClientTransLTHigh,
       "apDdServerTransCPActive": apDdServerTransCPActive,
       "apDdServerTransCPHigh": apDdServerTransCPHigh,
       "apDdServerTransCPTotal": apDdServerTransCPTotal,
       "apDdServerTransLTTotal": apDdServerTransLTTotal,
       "apDdServerTransLTPerMax": apDdServerTransLTPerMax,
       "apDdServerTransLTHigh": apDdServerTransLTHigh,
       "apDdGenSocketsCPActive": apDdGenSocketsCPActive,
       "apDdGenSocketsCPHigh": apDdGenSocketsCPHigh,
       "apDdGenSocketsCPTotal": apDdGenSocketsCPTotal,
       "apDdGenSocketsLTTotal": apDdGenSocketsLTTotal,
       "apDdGenSocketsLTPerMax": apDdGenSocketsLTPerMax,
       "apDdGenSocketsLTHigh": apDdGenSocketsLTHigh,
       "apDdGenConnectsCPActive": apDdGenConnectsCPActive,
       "apDdGenConnectsCPHigh": apDdGenConnectsCPHigh,
       "apDdGenConnectsCPTotal": apDdGenConnectsCPTotal,
       "apDdGenConnectsLTTotal": apDdGenConnectsLTTotal,
       "apDdGenConnectsLTPerMax": apDdGenConnectsLTPerMax,
       "apDdGenConnectsLTHigh": apDdGenConnectsLTHigh,
       "apDdErrorStatusTable": apDdErrorStatusTable,
       "apDdErrorStatusEntry": apDdErrorStatusEntry,
       "apDdNoRouteFoundRecent": apDdNoRouteFoundRecent,
       "apDdNoRouteFoundTotal": apDdNoRouteFoundTotal,
       "apDdNoRouteFoundPerMax": apDdNoRouteFoundPerMax,
       "apDdMalformedMsgRecent": apDdMalformedMsgRecent,
       "apDdMalformedMsgTotal": apDdMalformedMsgTotal,
       "apDdMalformedMsgPerMax": apDdMalformedMsgPerMax,
       "apDdRejectedMsgRecent": apDdRejectedMsgRecent,
       "apDdRejectedMsgTotal": apDdRejectedMsgTotal,
       "apDdRejectedMsgPerMax": apDdRejectedMsgPerMax,
       "apDdDroppedMsgRecent": apDdDroppedMsgRecent,
       "apDdDroppedMsgTotal": apDdDroppedMsgTotal,
       "apDdDroppedMsgPerMax": apDdDroppedMsgPerMax,
       "apDdInboundConstraintsRecent": apDdInboundConstraintsRecent,
       "apDdInboundConstraintsTotal": apDdInboundConstraintsTotal,
       "apDdInboundConstraintsPerMax": apDdInboundConstraintsPerMax,
       "apDdOutboundConstraintsRecent": apDdOutboundConstraintsRecent,
       "apDdOutboundConstraintsTotal": apDdOutboundConstraintsTotal,
       "apDdOutboundConstraintsPerMax": apDdOutboundConstraintsPerMax,
       "apDdMsgTypeInfoTable": apDdMsgTypeInfoTable,
       "apDdMsgTypeInfoEntry": apDdMsgTypeInfoEntry,
       "apDdMsgTypeIndex": apDdMsgTypeIndex,
       "apDdMsgTypeMsgName": apDdMsgTypeMsgName,
       "apDdMsgTypeStatsTable": apDdMsgTypeStatsTable,
       "apDdMsgTypeStatsEntry": apDdMsgTypeStatsEntry,
       "apDdMsgTypeServerReqRecent": apDdMsgTypeServerReqRecent,
       "apDdMsgTypeServerReqTotal": apDdMsgTypeServerReqTotal,
       "apDdMsgTypeServerReqPerMax": apDdMsgTypeServerReqPerMax,
       "apDdMsgTypeClientReqRecent": apDdMsgTypeClientReqRecent,
       "apDdMsgTypeClientReqTotal": apDdMsgTypeClientReqTotal,
       "apDdMsgTypeClientReqPerMax": apDdMsgTypeClientReqPerMax,
       "apDdMsgTypeServerRetransRecent": apDdMsgTypeServerRetransRecent,
       "apDdMsgTypeServerRetransTotal": apDdMsgTypeServerRetransTotal,
       "apDdMsgTypeServerRetransPerMax": apDdMsgTypeServerRetransPerMax,
       "apDdMsgTypeClientRetransRecent": apDdMsgTypeClientRetransRecent,
       "apDdMsgTypeClientRetransTotal": apDdMsgTypeClientRetransTotal,
       "apDdMsgTypeClientRetransPerMax": apDdMsgTypeClientRetransPerMax,
       "apDdMsgTypeServerRespRetransRecent": apDdMsgTypeServerRespRetransRecent,
       "apDdMsgTypeServerRespRetransTotal": apDdMsgTypeServerRespRetransTotal,
       "apDdMsgTypeServerRespRetransPerMax": apDdMsgTypeServerRespRetransPerMax,
       "apDdMsgTypeClientRespRetransRecent": apDdMsgTypeClientRespRetransRecent,
       "apDdMsgTypeClientRespRetransTotal": apDdMsgTypeClientRespRetransTotal,
       "apDdMsgTypeClientRespRetransPerMax": apDdMsgTypeClientRespRetransPerMax,
       "apDdMsgTypeClientTimeoutRecent": apDdMsgTypeClientTimeoutRecent,
       "apDdMsgTypeClientTimeoutTotal": apDdMsgTypeClientTimeoutTotal,
       "apDdMsgTypeClientTimeoutPerMax": apDdMsgTypeClientTimeoutPerMax,
       "apDdMsgTypeClientThrottledRecent": apDdMsgTypeClientThrottledRecent,
       "apDdMsgTypeClientThrottledTotal": apDdMsgTypeClientThrottledTotal,
       "apDdMsgTypeClientThrottledPerMax": apDdMsgTypeClientThrottledPerMax,
       "apDdMsgTypeAverageLatency": apDdMsgTypeAverageLatency,
       "apDdMsgTypeMaximumLatency": apDdMsgTypeMaximumLatency,
       "apDdMsgTypeLatencyWindow": apDdMsgTypeLatencyWindow,
       "apDdMsgReturnCodeInfoTable": apDdMsgReturnCodeInfoTable,
       "apDdMsgReturnCodeInfoEntry": apDdMsgReturnCodeInfoEntry,
       "apDdMsgReturnCodeIndex": apDdMsgReturnCodeIndex,
       "apDdMsgReturnCodeName": apDdMsgReturnCodeName,
       "apDdMsgStatsReturnCodeTable": apDdMsgStatsReturnCodeTable,
       "apDdMsgStatsReturnCodeEntry": apDdMsgStatsReturnCodeEntry,
       "apDdMsgReturnCodeServerRecent": apDdMsgReturnCodeServerRecent,
       "apDdMsgReturnCodeServerTotal": apDdMsgReturnCodeServerTotal,
       "apDdMsgReturnCodeServerPerMax": apDdMsgReturnCodeServerPerMax,
       "apDdMsgReturnCodeClientRecent": apDdMsgReturnCodeClientRecent,
       "apDdMsgReturnCodeClientTotal": apDdMsgReturnCodeClientTotal,
       "apDdMsgReturnCodeClientPerMax": apDdMsgReturnCodeClientPerMax,
       "apDdAgentStatsTable": apDdAgentStatsTable,
       "apDdAgentStatsEntry": apDdAgentStatsEntry,
       "apDdAgentIndex": apDdAgentIndex,
       "apDdAgentRealmName": apDdAgentRealmName,
       "apDdAgentClientTransCPActive": apDdAgentClientTransCPActive,
       "apDdAgentClientTransCPHigh": apDdAgentClientTransCPHigh,
       "apDdAgentClientTransCPTotal": apDdAgentClientTransCPTotal,
       "apDdAgentClientTransLTTotal": apDdAgentClientTransLTTotal,
       "apDdAgentClientTransLTPerMax": apDdAgentClientTransLTPerMax,
       "apDdAgentClientTransLTHigh": apDdAgentClientTransLTHigh,
       "apDdAgentServerTransCPActive": apDdAgentServerTransCPActive,
       "apDdAgentServerTransCPHigh": apDdAgentServerTransCPHigh,
       "apDdAgentServerTransCPTotal": apDdAgentServerTransCPTotal,
       "apDdAgentServerTransLTTotal": apDdAgentServerTransLTTotal,
       "apDdAgentServerTransLTPerMax": apDdAgentServerTransLTPerMax,
       "apDdAgentServerTransLTHigh": apDdAgentServerTransLTHigh,
       "apDdAgentGenSocketsCPActive": apDdAgentGenSocketsCPActive,
       "apDdAgentGenSocketsCPHigh": apDdAgentGenSocketsCPHigh,
       "apDdAgentGenSocketsCPTotal": apDdAgentGenSocketsCPTotal,
       "apDdAgentGenSocketsLTTotal": apDdAgentGenSocketsLTTotal,
       "apDdAgentGenSocketsLTPerMax": apDdAgentGenSocketsLTPerMax,
       "apDdAgentGenSocketsLTHigh": apDdAgentGenSocketsLTHigh,
       "apDdAgentGenConnectsCPActive": apDdAgentGenConnectsCPActive,
       "apDdAgentGenConnectsCPHigh": apDdAgentGenConnectsCPHigh,
       "apDdAgentGenConnectsCPTotal": apDdAgentGenConnectsCPTotal,
       "apDdAgentGenConnectsLTTotal": apDdAgentGenConnectsLTTotal,
       "apDdAgentGenConnectsLTPerMax": apDdAgentGenConnectsLTPerMax,
       "apDdAgentGenConnectsLTHigh": apDdAgentGenConnectsLTHigh,
       "apDdAgentErrorStatusTable": apDdAgentErrorStatusTable,
       "apDdAgentErrorStatusEntry": apDdAgentErrorStatusEntry,
       "apDdAgentNoRouteFoundRecent": apDdAgentNoRouteFoundRecent,
       "apDdAgentNoRouteFoundTotal": apDdAgentNoRouteFoundTotal,
       "apDdAgentNoRouteFoundPerMax": apDdAgentNoRouteFoundPerMax,
       "apDdAgentMalformedMsgRecent": apDdAgentMalformedMsgRecent,
       "apDdAgentMalformedMsgTotal": apDdAgentMalformedMsgTotal,
       "apDdAgentMalformedMsgPerMax": apDdAgentMalformedMsgPerMax,
       "apDdAgentRejectedMsgRecent": apDdAgentRejectedMsgRecent,
       "apDdAgentRejectedMsgTotal": apDdAgentRejectedMsgTotal,
       "apDdAgentRejectedMsgPerMax": apDdAgentRejectedMsgPerMax,
       "apDdAgentDroppedMsgRecent": apDdAgentDroppedMsgRecent,
       "apDdAgentDroppedMsgTotal": apDdAgentDroppedMsgTotal,
       "apDdAgentDroppedMsgPerMax": apDdAgentDroppedMsgPerMax,
       "apDdAgentInboundConstraintsRecent": apDdAgentInboundConstraintsRecent,
       "apDdAgentInboundConstraintsTotal": apDdAgentInboundConstraintsTotal,
       "apDdAgentInboundConstraintsPerMax": apDdAgentInboundConstraintsPerMax,
       "apDdAgentOutboundConstraintsRecent": apDdAgentOutboundConstraintsRecent,
       "apDdAgentOutboundConstraintsTotal": apDdAgentOutboundConstraintsTotal,
       "apDdAgentOutboundConstraintsPerMax": apDdAgentOutboundConstraintsPerMax,
       "apDdAgentMsgTypeStatsTable": apDdAgentMsgTypeStatsTable,
       "apDdAgentMsgTypeStatsEntry": apDdAgentMsgTypeStatsEntry,
       "apDdAgentMsgTypeServerReqRecent": apDdAgentMsgTypeServerReqRecent,
       "apDdAgentMsgTypeServerReqTotal": apDdAgentMsgTypeServerReqTotal,
       "apDdAgentMsgTypeServerReqPerMax": apDdAgentMsgTypeServerReqPerMax,
       "apDdAgentMsgTypeClientReqRecent": apDdAgentMsgTypeClientReqRecent,
       "apDdAgentMsgTypeClientReqTotal": apDdAgentMsgTypeClientReqTotal,
       "apDdAgentMsgTypeClientReqPerMax": apDdAgentMsgTypeClientReqPerMax,
       "apDdAgentMsgTypeServerRetransRecent": apDdAgentMsgTypeServerRetransRecent,
       "apDdAgentMsgTypeServerRetransTotal": apDdAgentMsgTypeServerRetransTotal,
       "apDdAgentMsgTypeServerRetransPerMax": apDdAgentMsgTypeServerRetransPerMax,
       "apDdAgentMsgTypeClientRetransRecent": apDdAgentMsgTypeClientRetransRecent,
       "apDdAgentMsgTypeClientRetransTotal": apDdAgentMsgTypeClientRetransTotal,
       "apDdAgentMsgTypeClientRetransPerMax": apDdAgentMsgTypeClientRetransPerMax,
       "apDdAgentMsgTypeServerRespRetransRecent": apDdAgentMsgTypeServerRespRetransRecent,
       "apDdAgentMsgTypeServerRespRetransTotal": apDdAgentMsgTypeServerRespRetransTotal,
       "apDdAgentMsgTypeServerRespRetransPerMax": apDdAgentMsgTypeServerRespRetransPerMax,
       "apDdAgentMsgTypeClientRespRetransRecent": apDdAgentMsgTypeClientRespRetransRecent,
       "apDdAgentMsgTypeClientRespRetransTotal": apDdAgentMsgTypeClientRespRetransTotal,
       "apDdAgentMsgTypeClientRespRetransPerMax": apDdAgentMsgTypeClientRespRetransPerMax,
       "apDdAgentMsgTypeClientTimeoutRecent": apDdAgentMsgTypeClientTimeoutRecent,
       "apDdAgentMsgTypeClientTimeoutTotal": apDdAgentMsgTypeClientTimeoutTotal,
       "apDdAgentMsgTypeClientTimeoutPerMax": apDdAgentMsgTypeClientTimeoutPerMax,
       "apDdAgentMsgTypeClientThrottledRecent": apDdAgentMsgTypeClientThrottledRecent,
       "apDdAgentMsgTypeClientThrottledTotal": apDdAgentMsgTypeClientThrottledTotal,
       "apDdAgentMsgTypeClientThrottledPerMax": apDdAgentMsgTypeClientThrottledPerMax,
       "apDdAgentMsgTypeAverageLatency": apDdAgentMsgTypeAverageLatency,
       "apDdAgentMsgTypeMaximumLatency": apDdAgentMsgTypeMaximumLatency,
       "apDdAgentMsgTypeLatencyWindow": apDdAgentMsgTypeLatencyWindow,
       "apDdAgentMsgStatsReturnCodeTable": apDdAgentMsgStatsReturnCodeTable,
       "apDdAgentMsgStatsReturnCodeEntry": apDdAgentMsgStatsReturnCodeEntry,
       "apDdAgentMsgReturnCodeServerRecent": apDdAgentMsgReturnCodeServerRecent,
       "apDdAgentMsgReturnCodeServerTotal": apDdAgentMsgReturnCodeServerTotal,
       "apDdAgentMsgReturnCodeServerPerMax": apDdAgentMsgReturnCodeServerPerMax,
       "apDdAgentMsgReturnCodeClientRecent": apDdAgentMsgReturnCodeClientRecent,
       "apDdAgentMsgReturnCodeClientTotal": apDdAgentMsgReturnCodeClientTotal,
       "apDdAgentMsgReturnCodeClientPerMax": apDdAgentMsgReturnCodeClientPerMax,
       "apDDNotificationObjects": apDDNotificationObjects,
       "apDDNotifObjects": apDDNotifObjects,
       "apDdDiameterAgentHostName": apDdDiameterAgentHostName,
       "apDdDiameterIPPort": apDdDiameterIPPort,
       "apDdDiameterAgentOriginHostName": apDdDiameterAgentOriginHostName,
       "apDdDiameterAgentOriginRealmName": apDdDiameterAgentOriginRealmName,
       "apDdTransportType": apDdTransportType,
       "apDdInterfaceStatusReason": apDdInterfaceStatusReason,
       "apDDNotifPrefix": apDDNotifPrefix,
       "apDDNotifications": apDDNotifications,
       "apDdConnectionFailureTrap": apDdConnectionFailureTrap,
       "apDdConnectionFailureClearTrap": apDdConnectionFailureClearTrap,
       "apDDConformance": apDDConformance,
       "apDDObjectGroups": apDDObjectGroups,
       "apDdGeneralGroup": apDdGeneralGroup,
       "apDdInterfaceStatsGroup": apDdInterfaceStatsGroup,
       "apDdErrorStatusGroup": apDdErrorStatusGroup,
       "apDdMsgTypeStatsGroup": apDdMsgTypeStatsGroup,
       "apDdMsgStatsReturnCodeGroup": apDdMsgStatsReturnCodeGroup,
       "apDdIntfErrorStatusGroup": apDdIntfErrorStatusGroup,
       "apDdAgentGeneralGroup": apDdAgentGeneralGroup,
       "apDdAgentStatsGroup": apDdAgentStatsGroup,
       "apDdAgentErrorStatusGroup": apDdAgentErrorStatusGroup,
       "apDdAgentMsgTypeStatsGroup": apDdAgentMsgTypeStatsGroup,
       "apDdAgentMsgStatsReturnCodeGroup": apDdAgentMsgStatsReturnCodeGroup,
       "apDdSessionSubscriberGeneralGroup": apDdSessionSubscriberGeneralGroup,
       "apDDNotificationGroups": apDDNotificationGroups,
       "apDDNotifObjectsGroup": apDDNotifObjectsGroup,
       "apDDNotificationsGroup": apDDNotificationsGroup}
)
