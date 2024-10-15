# SNMP MIB module (SYSLOG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYSLOG
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:12 2024
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

(radioConfig,) = mibBuilder.importSymbols(
    "ExaltComProducts",
    "radioConfig")

(SyslogEnableT,
 SyslogFilterSelectT) = mibBuilder.importSymbols(
    "ExaltComm",
    "SyslogEnableT",
    "SyslogFilterSelectT")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdvSystemConfig_ObjectIdentity = ObjectIdentity
advSystemConfig = _AdvSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    advSystemConfig.setStatus("current")
_SyslogCfg_ObjectIdentity = ObjectIdentity
syslogCfg = _SyslogCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6)
)
if mibBuilder.loadTexts:
    syslogCfg.setStatus("current")
_SyslogEnable_Type = SyslogEnableT
_SyslogEnable_Object = MibScalar
syslogEnable = _SyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6, 1),
    _SyslogEnable_Type()
)
syslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogEnable.setStatus("current")
_SyslogRemoteIpAddr_Type = DisplayString
_SyslogRemoteIpAddr_Object = MibScalar
syslogRemoteIpAddr = _SyslogRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6, 2),
    _SyslogRemoteIpAddr_Type()
)
syslogRemoteIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogRemoteIpAddr.setStatus("current")
_SyslogFilterSelect_Type = SyslogFilterSelectT
_SyslogFilterSelect_Object = MibScalar
syslogFilterSelect = _SyslogFilterSelect_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6, 3),
    _SyslogFilterSelect_Type()
)
syslogFilterSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogFilterSelect.setStatus("current")
_CommitSyslogSettings_Type = DisplayString
_CommitSyslogSettings_Object = MibScalar
commitSyslogSettings = _CommitSyslogSettings_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6, 1000),
    _CommitSyslogSettings_Type()
)
commitSyslogSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commitSyslogSettings.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYSLOG",
    **{"advSystemConfig": advSystemConfig,
       "syslogCfg": syslogCfg,
       "syslogEnable": syslogEnable,
       "syslogRemoteIpAddr": syslogRemoteIpAddr,
       "syslogFilterSelect": syslogFilterSelect,
       "commitSyslogSettings": commitSyslogSettings}
)
