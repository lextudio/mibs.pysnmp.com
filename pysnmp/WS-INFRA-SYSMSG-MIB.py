# SNMP MIB module (WS-INFRA-SYSMSG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WS-INFRA-SYSMSG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:30 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(wsInfraSysMsg,) = mibBuilder.importSymbols(
    "WS-INFRA-SMI-MIB",
    "wsInfraSysMsg")

(DoActionNow,) = mibBuilder.importSymbols(
    "WS-TYPE-MIB",
    "DoActionNow")


# MODULE-IDENTITY

wsInfraSysMsgModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1)
)
wsInfraSysMsgModule.setRevisions(
        ("2006-05-24 15:51",
         "2005-11-03 15:13",
         "2005-07-28 16:59",
         "2005-05-11 14:21",
         "2005-05-09 11:11",
         "2005-05-05 17:46",
         "2005-05-04 17:36",
         "2005-05-04 12:02")
)


# Types definitions



class SysMsgSeverity(Integer32):
    """Custom type SysMsgSeverity based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsInfraSysMsgEnable_Type = TruthValue
_WsInfraSysMsgEnable_Object = MibScalar
wsInfraSysMsgEnable = _WsInfraSysMsgEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 1),
    _WsInfraSysMsgEnable_Type()
)
wsInfraSysMsgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraSysMsgEnable.setStatus("current")


class _WsInfraSysMsgAggTime_Type(Integer32):
    """Custom type wsInfraSysMsgAggTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_WsInfraSysMsgAggTime_Type.__name__ = "Integer32"
_WsInfraSysMsgAggTime_Object = MibScalar
wsInfraSysMsgAggTime = _WsInfraSysMsgAggTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 2),
    _WsInfraSysMsgAggTime_Type()
)
wsInfraSysMsgAggTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraSysMsgAggTime.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraSysMsgAggTime.setUnits("second")
_WsInfraSysMsgBuffer_ObjectIdentity = ObjectIdentity
wsInfraSysMsgBuffer = _WsInfraSysMsgBuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 3)
)
_WsInfraSysMsgBufferEnable_Type = TruthValue
_WsInfraSysMsgBufferEnable_Object = MibScalar
wsInfraSysMsgBufferEnable = _WsInfraSysMsgBufferEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 3, 1),
    _WsInfraSysMsgBufferEnable_Type()
)
wsInfraSysMsgBufferEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraSysMsgBufferEnable.setStatus("current")
_WsInfraSysMsgBufferSeverity_Type = SysMsgSeverity
_WsInfraSysMsgBufferSeverity_Object = MibScalar
wsInfraSysMsgBufferSeverity = _WsInfraSysMsgBufferSeverity_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 3, 2),
    _WsInfraSysMsgBufferSeverity_Type()
)
wsInfraSysMsgBufferSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraSysMsgBufferSeverity.setStatus("current")
_WsInfraSysMsgBufferClear_Type = DoActionNow
_WsInfraSysMsgBufferClear_Object = MibScalar
wsInfraSysMsgBufferClear = _WsInfraSysMsgBufferClear_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 3, 3),
    _WsInfraSysMsgBufferClear_Type()
)
wsInfraSysMsgBufferClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraSysMsgBufferClear.setStatus("current")
_WsInfraSysMsgRemoteSvr_ObjectIdentity = ObjectIdentity
wsInfraSysMsgRemoteSvr = _WsInfraSysMsgRemoteSvr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 4)
)
_WsInfraSysMsgRemoteSvrEnable_Type = TruthValue
_WsInfraSysMsgRemoteSvrEnable_Object = MibScalar
wsInfraSysMsgRemoteSvrEnable = _WsInfraSysMsgRemoteSvrEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 4, 1),
    _WsInfraSysMsgRemoteSvrEnable_Type()
)
wsInfraSysMsgRemoteSvrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraSysMsgRemoteSvrEnable.setStatus("current")
_WsInfraSysMsgRemoteSvrSeverity_Type = SysMsgSeverity
_WsInfraSysMsgRemoteSvrSeverity_Object = MibScalar
wsInfraSysMsgRemoteSvrSeverity = _WsInfraSysMsgRemoteSvrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 4, 2),
    _WsInfraSysMsgRemoteSvrSeverity_Type()
)
wsInfraSysMsgRemoteSvrSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraSysMsgRemoteSvrSeverity.setStatus("current")


class _WsInfraSysMsgRemoteSvrFacility_Type(Integer32):
    """Custom type wsInfraSysMsgRemoteSvrFacility based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("logLocal0", 0),
          ("logLocal1", 1),
          ("logLocal2", 2),
          ("logLocal3", 3),
          ("logLocal4", 4),
          ("logLocal5", 5),
          ("logLocal6", 6),
          ("logLocal7", 7))
    )


_WsInfraSysMsgRemoteSvrFacility_Type.__name__ = "Integer32"
_WsInfraSysMsgRemoteSvrFacility_Object = MibScalar
wsInfraSysMsgRemoteSvrFacility = _WsInfraSysMsgRemoteSvrFacility_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 4, 3),
    _WsInfraSysMsgRemoteSvrFacility_Type()
)
wsInfraSysMsgRemoteSvrFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraSysMsgRemoteSvrFacility.setStatus("current")
_WsInfraSysMsgRemoteSvrTable_Object = MibTable
wsInfraSysMsgRemoteSvrTable = _WsInfraSysMsgRemoteSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wsInfraSysMsgRemoteSvrTable.setStatus("current")
_WsInfraSysMsgRemoteSvrEntry_Object = MibTableRow
wsInfraSysMsgRemoteSvrEntry = _WsInfraSysMsgRemoteSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 4, 4, 1)
)
wsInfraSysMsgRemoteSvrEntry.setIndexNames(
    (0, "WS-INFRA-SYSMSG-MIB", "wsInfraSysMsgRemoteSvrIndex"),
)
if mibBuilder.loadTexts:
    wsInfraSysMsgRemoteSvrEntry.setStatus("current")


class _WsInfraSysMsgRemoteSvrIndex_Type(Integer32):
    """Custom type wsInfraSysMsgRemoteSvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WsInfraSysMsgRemoteSvrIndex_Type.__name__ = "Integer32"
_WsInfraSysMsgRemoteSvrIndex_Object = MibTableColumn
wsInfraSysMsgRemoteSvrIndex = _WsInfraSysMsgRemoteSvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 4, 4, 1, 1),
    _WsInfraSysMsgRemoteSvrIndex_Type()
)
wsInfraSysMsgRemoteSvrIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wsInfraSysMsgRemoteSvrIndex.setStatus("current")
_WsInfraSysMsgRemoteSvrIp_Type = IpAddress
_WsInfraSysMsgRemoteSvrIp_Object = MibTableColumn
wsInfraSysMsgRemoteSvrIp = _WsInfraSysMsgRemoteSvrIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 4, 4, 1, 2),
    _WsInfraSysMsgRemoteSvrIp_Type()
)
wsInfraSysMsgRemoteSvrIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraSysMsgRemoteSvrIp.setStatus("current")
_WsInfraSysMsgConsole_ObjectIdentity = ObjectIdentity
wsInfraSysMsgConsole = _WsInfraSysMsgConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 5)
)
_WsInfraSysMsgConsoleEnable_Type = TruthValue
_WsInfraSysMsgConsoleEnable_Object = MibScalar
wsInfraSysMsgConsoleEnable = _WsInfraSysMsgConsoleEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 5, 1),
    _WsInfraSysMsgConsoleEnable_Type()
)
wsInfraSysMsgConsoleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraSysMsgConsoleEnable.setStatus("current")
_WsInfraSysMsgConsoleSeverity_Type = SysMsgSeverity
_WsInfraSysMsgConsoleSeverity_Object = MibScalar
wsInfraSysMsgConsoleSeverity = _WsInfraSysMsgConsoleSeverity_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 5, 2),
    _WsInfraSysMsgConsoleSeverity_Type()
)
wsInfraSysMsgConsoleSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraSysMsgConsoleSeverity.setStatus("current")
_WsInfraSysMsgMIBConformance_ObjectIdentity = ObjectIdentity
wsInfraSysMsgMIBConformance = _WsInfraSysMsgMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 6)
)
_WsInfraSysMsgMIBCompliances_ObjectIdentity = ObjectIdentity
wsInfraSysMsgMIBCompliances = _WsInfraSysMsgMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 6, 1)
)
_WsInfraSysMsgMIBGroups_ObjectIdentity = ObjectIdentity
wsInfraSysMsgMIBGroups = _WsInfraSysMsgMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 6, 2)
)

# Managed Objects groups

wsInfraSysMsgMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 6, 2, 1)
)
wsInfraSysMsgMIBGroup.setObjects(
      *(("WS-INFRA-SYSMSG-MIB", "wsInfraSysMsgEnable"),
        ("WS-INFRA-SYSMSG-MIB", "wsInfraSysMsgBufferEnable"),
        ("WS-INFRA-SYSMSG-MIB", "wsInfraSysMsgBufferSeverity"),
        ("WS-INFRA-SYSMSG-MIB", "wsInfraSysMsgBufferClear"),
        ("WS-INFRA-SYSMSG-MIB", "wsInfraSysMsgRemoteSvrEnable"),
        ("WS-INFRA-SYSMSG-MIB", "wsInfraSysMsgRemoteSvrSeverity"),
        ("WS-INFRA-SYSMSG-MIB", "wsInfraSysMsgRemoteSvrFacility"),
        ("WS-INFRA-SYSMSG-MIB", "wsInfraSysMsgConsoleEnable"),
        ("WS-INFRA-SYSMSG-MIB", "wsInfraSysMsgConsoleSeverity"),
        ("WS-INFRA-SYSMSG-MIB", "wsInfraSysMsgRemoteSvrIndex"),
        ("WS-INFRA-SYSMSG-MIB", "wsInfraSysMsgRemoteSvrIp"),
        ("WS-INFRA-SYSMSG-MIB", "wsInfraSysMsgAggTime"))
)
if mibBuilder.loadTexts:
    wsInfraSysMsgMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wsInfraSysMsgMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    wsInfraSysMsgMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WS-INFRA-SYSMSG-MIB",
    **{"SysMsgSeverity": SysMsgSeverity,
       "wsInfraSysMsgModule": wsInfraSysMsgModule,
       "wsInfraSysMsgEnable": wsInfraSysMsgEnable,
       "wsInfraSysMsgAggTime": wsInfraSysMsgAggTime,
       "wsInfraSysMsgBuffer": wsInfraSysMsgBuffer,
       "wsInfraSysMsgBufferEnable": wsInfraSysMsgBufferEnable,
       "wsInfraSysMsgBufferSeverity": wsInfraSysMsgBufferSeverity,
       "wsInfraSysMsgBufferClear": wsInfraSysMsgBufferClear,
       "wsInfraSysMsgRemoteSvr": wsInfraSysMsgRemoteSvr,
       "wsInfraSysMsgRemoteSvrEnable": wsInfraSysMsgRemoteSvrEnable,
       "wsInfraSysMsgRemoteSvrSeverity": wsInfraSysMsgRemoteSvrSeverity,
       "wsInfraSysMsgRemoteSvrFacility": wsInfraSysMsgRemoteSvrFacility,
       "wsInfraSysMsgRemoteSvrTable": wsInfraSysMsgRemoteSvrTable,
       "wsInfraSysMsgRemoteSvrEntry": wsInfraSysMsgRemoteSvrEntry,
       "wsInfraSysMsgRemoteSvrIndex": wsInfraSysMsgRemoteSvrIndex,
       "wsInfraSysMsgRemoteSvrIp": wsInfraSysMsgRemoteSvrIp,
       "wsInfraSysMsgConsole": wsInfraSysMsgConsole,
       "wsInfraSysMsgConsoleEnable": wsInfraSysMsgConsoleEnable,
       "wsInfraSysMsgConsoleSeverity": wsInfraSysMsgConsoleSeverity,
       "wsInfraSysMsgMIBConformance": wsInfraSysMsgMIBConformance,
       "wsInfraSysMsgMIBCompliances": wsInfraSysMsgMIBCompliances,
       "wsInfraSysMsgMIBCompliance": wsInfraSysMsgMIBCompliance,
       "wsInfraSysMsgMIBGroups": wsInfraSysMsgMIBGroups,
       "wsInfraSysMsgMIBGroup": wsInfraSysMsgMIBGroup}
)
