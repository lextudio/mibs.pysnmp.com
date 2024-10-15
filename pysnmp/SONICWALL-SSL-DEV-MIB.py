# SNMP MIB module (SONICWALL-SSL-DEV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONICWALL-SSL-DEV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:37 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

sonicSSLDev = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonicWALL_ObjectIdentity = ObjectIdentity
sonicWALL = _SonicWALL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8714)
)
_SonicSEC_ObjectIdentity = ObjectIdentity
sonicSEC = _SonicSEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8714, 2)
)
_SonicSSL_ObjectIdentity = ObjectIdentity
sonicSSL = _SonicSSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1)
)
_SslDevInfo_ObjectIdentity = ObjectIdentity
sslDevInfo = _SslDevInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 6, 0)
)
_LastCfgChgInitiator_Type = IpAddress
_LastCfgChgInitiator_Object = MibScalar
lastCfgChgInitiator = _LastCfgChgInitiator_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 6, 0, 1),
    _LastCfgChgInitiator_Type()
)
lastCfgChgInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastCfgChgInitiator.setStatus("mandatory")
_LastCfgChgCmd_Type = Integer32
_LastCfgChgCmd_Object = MibScalar
lastCfgChgCmd = _LastCfgChgCmd_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 6, 0, 2),
    _LastCfgChgCmd_Type()
)
lastCfgChgCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastCfgChgCmd.setStatus("mandatory")
_SslDevUtil_ObjectIdentity = ObjectIdentity
sslDevUtil = _SslDevUtil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 6, 1)
)
_CpuUtilLoThresh_Type = Integer32
_CpuUtilLoThresh_Object = MibScalar
cpuUtilLoThresh = _CpuUtilLoThresh_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 6, 1, 1),
    _CpuUtilLoThresh_Type()
)
cpuUtilLoThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilLoThresh.setStatus("mandatory")
_CpuUtilHiThresh_Type = Integer32
_CpuUtilHiThresh_Object = MibScalar
cpuUtilHiThresh = _CpuUtilHiThresh_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 6, 1, 2),
    _CpuUtilHiThresh_Type()
)
cpuUtilHiThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilHiThresh.setStatus("mandatory")
_SslDevStats_ObjectIdentity = ObjectIdentity
sslDevStats = _SslDevStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 6, 2)
)
_CpuUtilStatus_Type = Integer32
_CpuUtilStatus_Object = MibScalar
cpuUtilStatus = _CpuUtilStatus_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 6, 2, 1),
    _CpuUtilStatus_Type()
)
cpuUtilStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilStatus.setStatus("mandatory")
_SslDevEvents_ObjectIdentity = ObjectIdentity
sslDevEvents = _SslDevEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 6, 10)
)

# Managed Objects groups


# Notification objects

cpuUtilChangeHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 6, 10, 0, 1)
)
if mibBuilder.loadTexts:
    cpuUtilChangeHi.setStatus(
        ""
    )

cpuUtilChangeLo = NotificationType(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 6, 10, 0, 2)
)
if mibBuilder.loadTexts:
    cpuUtilChangeLo.setStatus(
        ""
    )

configChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 6, 10, 0, 7)
)
configChange.setObjects(
      *(("SONICWALL-SSL-DEV-MIB", "lastCfgChgInitiator"),
        ("SONICWALL-SSL-DEV-MIB", "lastCfgChgCmd"))
)
if mibBuilder.loadTexts:
    configChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONICWALL-SSL-DEV-MIB",
    **{"sonicWALL": sonicWALL,
       "sonicSEC": sonicSEC,
       "sonicSSL": sonicSSL,
       "sonicSSLDev": sonicSSLDev,
       "sslDevInfo": sslDevInfo,
       "lastCfgChgInitiator": lastCfgChgInitiator,
       "lastCfgChgCmd": lastCfgChgCmd,
       "sslDevUtil": sslDevUtil,
       "cpuUtilLoThresh": cpuUtilLoThresh,
       "cpuUtilHiThresh": cpuUtilHiThresh,
       "sslDevStats": sslDevStats,
       "cpuUtilStatus": cpuUtilStatus,
       "sslDevEvents": sslDevEvents,
       "cpuUtilChangeHi": cpuUtilChangeHi,
       "cpuUtilChangeLo": cpuUtilChangeLo,
       "configChange": configChange}
)
