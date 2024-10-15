# SNMP MIB module (G3-AVAYA-TRAP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/G3-AVAYA-TRAP
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:31 2024
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

(g3_products,
 g3alarmsAlarmNumber,
 g3alarmsAlarmType,
 g3alarmsMaintName,
 g3alarmsOnBrd,
 g3alarmsPort,
 g3alarmsProductID,
 g3clientExternalName,
 g3extdevAddress,
 g3extdevAltName,
 g3extdevBuilding,
 g3extdevDescription,
 g3extdevID,
 g3restartCarrier,
 g3restartCause,
 g3restartCraftDemand,
 g3restartDateTime,
 g3restartEscalated,
 g3restartInterchange,
 g3restartLevel,
 g3restartUnavailable,
 g3vintageSpeArelease,
 g3vintageSpeAupID,
 g3vintageSpeBrelease,
 g3vintageSpeBupID) = mibBuilder.importSymbols(
    "G3-AVAYA-MIB",
    "g3-products",
    "g3alarmsAlarmNumber",
    "g3alarmsAlarmType",
    "g3alarmsMaintName",
    "g3alarmsOnBrd",
    "g3alarmsPort",
    "g3alarmsProductID",
    "g3clientExternalName",
    "g3extdevAddress",
    "g3extdevAltName",
    "g3extdevBuilding",
    "g3extdevDescription",
    "g3extdevID",
    "g3restartCarrier",
    "g3restartCause",
    "g3restartCraftDemand",
    "g3restartDateTime",
    "g3restartEscalated",
    "g3restartInterchange",
    "g3restartLevel",
    "g3restartUnavailable",
    "g3vintageSpeArelease",
    "g3vintageSpeAupID",
    "g3vintageSpeBrelease",
    "g3vintageSpeBupID")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

alarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 0)
)
alarmClear.setObjects(
      *(("G3-AVAYA-MIB", "g3clientExternalName"),
        ("G3-AVAYA-MIB", "g3alarmsProductID"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmNumber"))
)
if mibBuilder.loadTexts:
    alarmClear.setStatus(
        ""
    )

alarmCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 1)
)
alarmCritical.setObjects(
      *(("G3-AVAYA-MIB", "g3clientExternalName"),
        ("G3-AVAYA-MIB", "g3alarmsProductID"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmNumber"),
        ("G3-AVAYA-MIB", "g3alarmsPort"),
        ("G3-AVAYA-MIB", "g3alarmsMaintName"),
        ("G3-AVAYA-MIB", "g3alarmsOnBrd"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmType"))
)
if mibBuilder.loadTexts:
    alarmCritical.setStatus(
        ""
    )

alarmMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 2)
)
alarmMajor.setObjects(
      *(("G3-AVAYA-MIB", "g3clientExternalName"),
        ("G3-AVAYA-MIB", "g3alarmsProductID"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmNumber"),
        ("G3-AVAYA-MIB", "g3alarmsPort"),
        ("G3-AVAYA-MIB", "g3alarmsMaintName"),
        ("G3-AVAYA-MIB", "g3alarmsOnBrd"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmType"))
)
if mibBuilder.loadTexts:
    alarmMajor.setStatus(
        ""
    )

alarmMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 3)
)
alarmMinor.setObjects(
      *(("G3-AVAYA-MIB", "g3clientExternalName"),
        ("G3-AVAYA-MIB", "g3alarmsProductID"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmNumber"),
        ("G3-AVAYA-MIB", "g3alarmsPort"),
        ("G3-AVAYA-MIB", "g3alarmsMaintName"),
        ("G3-AVAYA-MIB", "g3alarmsOnBrd"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmType"))
)
if mibBuilder.loadTexts:
    alarmMinor.setStatus(
        ""
    )

alarmWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 4)
)
alarmWarning.setObjects(
      *(("G3-AVAYA-MIB", "g3clientExternalName"),
        ("G3-AVAYA-MIB", "g3alarmsProductID"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmNumber"),
        ("G3-AVAYA-MIB", "g3alarmsPort"),
        ("G3-AVAYA-MIB", "g3alarmsMaintName"),
        ("G3-AVAYA-MIB", "g3alarmsOnBrd"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmType"))
)
if mibBuilder.loadTexts:
    alarmWarning.setStatus(
        ""
    )

extalarmMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 5)
)
extalarmMajor.setObjects(
      *(("G3-AVAYA-MIB", "g3clientExternalName"),
        ("G3-AVAYA-MIB", "g3alarmsProductID"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmNumber"),
        ("G3-AVAYA-MIB", "g3alarmsPort"),
        ("G3-AVAYA-MIB", "g3alarmsMaintName"),
        ("G3-AVAYA-MIB", "g3alarmsOnBrd"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmType"),
        ("G3-AVAYA-MIB", "g3extdevAltName"),
        ("G3-AVAYA-MIB", "g3extdevDescription"),
        ("G3-AVAYA-MIB", "g3extdevID"),
        ("G3-AVAYA-MIB", "g3extdevBuilding"),
        ("G3-AVAYA-MIB", "g3extdevAddress"))
)
if mibBuilder.loadTexts:
    extalarmMajor.setStatus(
        ""
    )

extalarmMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 6)
)
extalarmMinor.setObjects(
      *(("G3-AVAYA-MIB", "g3clientExternalName"),
        ("G3-AVAYA-MIB", "g3alarmsProductID"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmNumber"),
        ("G3-AVAYA-MIB", "g3alarmsPort"),
        ("G3-AVAYA-MIB", "g3alarmsMaintName"),
        ("G3-AVAYA-MIB", "g3alarmsOnBrd"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmType"),
        ("G3-AVAYA-MIB", "g3extdevAltName"),
        ("G3-AVAYA-MIB", "g3extdevDescription"),
        ("G3-AVAYA-MIB", "g3extdevID"),
        ("G3-AVAYA-MIB", "g3extdevBuilding"),
        ("G3-AVAYA-MIB", "g3extdevAddress"))
)
if mibBuilder.loadTexts:
    extalarmMinor.setStatus(
        ""
    )

alarmDispatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 7)
)
alarmDispatch.setObjects(
      *(("G3-AVAYA-MIB", "g3clientExternalName"),
        ("G3-AVAYA-MIB", "g3alarmsProductID"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmNumber"))
)
if mibBuilder.loadTexts:
    alarmDispatch.setStatus(
        ""
    )

alarmClose = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 8)
)
alarmClose.setObjects(
      *(("G3-AVAYA-MIB", "g3clientExternalName"),
        ("G3-AVAYA-MIB", "g3alarmsProductID"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmNumber"))
)
if mibBuilder.loadTexts:
    alarmClose.setStatus(
        ""
    )

alarmRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 9)
)
alarmRestart.setObjects(
      *(("G3-AVAYA-MIB", "g3clientExternalName"),
        ("G3-AVAYA-MIB", "g3alarmsProductID"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmNumber"),
        ("G3-AVAYA-MIB", "g3restartDateTime"),
        ("G3-AVAYA-MIB", "g3restartLevel"),
        ("G3-AVAYA-MIB", "g3restartCarrier"),
        ("G3-AVAYA-MIB", "g3restartCraftDemand"),
        ("G3-AVAYA-MIB", "g3restartEscalated"),
        ("G3-AVAYA-MIB", "g3restartInterchange"),
        ("G3-AVAYA-MIB", "g3restartUnavailable"),
        ("G3-AVAYA-MIB", "g3restartCause"),
        ("G3-AVAYA-MIB", "g3vintageSpeArelease"),
        ("G3-AVAYA-MIB", "g3vintageSpeBrelease"),
        ("G3-AVAYA-MIB", "g3vintageSpeAupID"),
        ("G3-AVAYA-MIB", "g3vintageSpeBupID"))
)
if mibBuilder.loadTexts:
    alarmRestart.setStatus(
        ""
    )

alarmNak = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 10)
)
alarmNak.setObjects(
      *(("G3-AVAYA-MIB", "g3clientExternalName"),
        ("G3-AVAYA-MIB", "g3alarmsProductID"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmNumber"))
)
if mibBuilder.loadTexts:
    alarmNak.setStatus(
        ""
    )

alarmNoAck = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 11)
)
alarmNoAck.setObjects(
      *(("G3-AVAYA-MIB", "g3clientExternalName"),
        ("G3-AVAYA-MIB", "g3alarmsProductID"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmNumber"))
)
if mibBuilder.loadTexts:
    alarmNoAck.setStatus(
        ""
    )

alarmResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 12)
)
alarmResolved.setObjects(
      *(("G3-AVAYA-MIB", "g3clientExternalName"),
        ("G3-AVAYA-MIB", "g3alarmsProductID"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmNumber"),
        ("G3-AVAYA-MIB", "g3alarmsPort"),
        ("G3-AVAYA-MIB", "g3alarmsMaintName"),
        ("G3-AVAYA-MIB", "g3alarmsOnBrd"),
        ("G3-AVAYA-MIB", "g3alarmsAlarmType"))
)
if mibBuilder.loadTexts:
    alarmResolved.setStatus(
        ""
    )

connectOther = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 101)
)
connectOther.setObjects(
    ("G3-AVAYA-MIB", "g3clientExternalName")
)
if mibBuilder.loadTexts:
    connectOther.setStatus(
        ""
    )

connectOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 102)
)
connectOff.setObjects(
    ("G3-AVAYA-MIB", "g3clientExternalName")
)
if mibBuilder.loadTexts:
    connectOff.setStatus(
        ""
    )

connectDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 103)
)
connectDown.setObjects(
    ("G3-AVAYA-MIB", "g3clientExternalName")
)
if mibBuilder.loadTexts:
    connectDown.setStatus(
        ""
    )

connectInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 104)
)
connectInit.setObjects(
    ("G3-AVAYA-MIB", "g3clientExternalName")
)
if mibBuilder.loadTexts:
    connectInit.setStatus(
        ""
    )

connectUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 105)
)
connectUp.setObjects(
    ("G3-AVAYA-MIB", "g3clientExternalName")
)
if mibBuilder.loadTexts:
    connectUp.setStatus(
        ""
    )

connectIdle = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 106)
)
connectIdle.setObjects(
    ("G3-AVAYA-MIB", "g3clientExternalName")
)
if mibBuilder.loadTexts:
    connectIdle.setStatus(
        ""
    )

connectMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 110)
)
connectMax.setObjects(
    ("G3-AVAYA-MIB", "g3clientExternalName")
)
if mibBuilder.loadTexts:
    connectMax.setStatus(
        ""
    )

proxyDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 150)
)
proxyDown.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    proxyDown.setStatus(
        ""
    )

proxyUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 1, 8, 1, 0, 151)
)
proxyUp.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    proxyUp.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G3-AVAYA-TRAP",
    **{"alarmClear": alarmClear,
       "alarmCritical": alarmCritical,
       "alarmMajor": alarmMajor,
       "alarmMinor": alarmMinor,
       "alarmWarning": alarmWarning,
       "extalarmMajor": extalarmMajor,
       "extalarmMinor": extalarmMinor,
       "alarmDispatch": alarmDispatch,
       "alarmClose": alarmClose,
       "alarmRestart": alarmRestart,
       "alarmNak": alarmNak,
       "alarmNoAck": alarmNoAck,
       "alarmResolved": alarmResolved,
       "connectOther": connectOther,
       "connectOff": connectOff,
       "connectDown": connectDown,
       "connectInit": connectInit,
       "connectUp": connectUp,
       "connectIdle": connectIdle,
       "connectMax": connectMax,
       "proxyDown": proxyDown,
       "proxyUp": proxyUp}
)
