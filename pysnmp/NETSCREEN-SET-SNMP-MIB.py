# SNMP MIB module (NETSCREEN-SET-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-SET-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:58 2024
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

(netscreenSetting,
 netscreenSettingMibModule) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenSetting",
    "netscreenSettingMibModule")

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

netscreenSetSnmpMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 0, 9)
)
netscreenSetSnmpMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-10 00:00",
         "2001-09-28 00:00",
         "2001-05-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsSetSNMP_ObjectIdentity = ObjectIdentity
nsSetSNMP = _NsSetSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 9)
)


class _NsSetSnmpSysName_Type(DisplayString):
    """Custom type nsSetSnmpSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsSetSnmpSysName_Type.__name__ = "DisplayString"
_NsSetSnmpSysName_Object = MibScalar
nsSetSnmpSysName = _NsSetSnmpSysName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 9, 1),
    _NsSetSnmpSysName_Type()
)
nsSetSnmpSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetSnmpSysName.setStatus("current")


class _NsSetSnmpContact_Type(DisplayString):
    """Custom type nsSetSnmpContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsSetSnmpContact_Type.__name__ = "DisplayString"
_NsSetSnmpContact_Object = MibScalar
nsSetSnmpContact = _NsSetSnmpContact_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 9, 2),
    _NsSetSnmpContact_Type()
)
nsSetSnmpContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetSnmpContact.setStatus("current")


class _NsSetSnmpLocation_Type(DisplayString):
    """Custom type nsSetSnmpLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsSetSnmpLocation_Type.__name__ = "DisplayString"
_NsSetSnmpLocation_Object = MibScalar
nsSetSnmpLocation = _NsSetSnmpLocation_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 9, 3),
    _NsSetSnmpLocation_Type()
)
nsSetSnmpLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetSnmpLocation.setStatus("current")


class _NsSetSnmpVPNEnable_Type(Integer32):
    """Custom type nsSetSnmpVPNEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetSnmpVPNEnable_Type.__name__ = "Integer32"
_NsSetSnmpVPNEnable_Object = MibScalar
nsSetSnmpVPNEnable = _NsSetSnmpVPNEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 9, 4),
    _NsSetSnmpVPNEnable_Type()
)
nsSetSnmpVPNEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetSnmpVPNEnable.setStatus("current")
_NsSetSnmpCommHostTable_Object = MibTable
nsSetSnmpCommHostTable = _NsSetSnmpCommHostTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 9, 5)
)
if mibBuilder.loadTexts:
    nsSetSnmpCommHostTable.setStatus("current")
_NsSetSnmpCommHostEntry_Object = MibTableRow
nsSetSnmpCommHostEntry = _NsSetSnmpCommHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 9, 5, 1)
)
nsSetSnmpCommHostEntry.setIndexNames(
    (0, "NETSCREEN-SET-SNMP-MIB", "nsSetSnmpCommHostIndex"),
)
if mibBuilder.loadTexts:
    nsSetSnmpCommHostEntry.setStatus("current")


class _NsSetSnmpCommHostIndex_Type(Integer32):
    """Custom type nsSetSnmpCommHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsSetSnmpCommHostIndex_Type.__name__ = "Integer32"
_NsSetSnmpCommHostIndex_Object = MibTableColumn
nsSetSnmpCommHostIndex = _NsSetSnmpCommHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 9, 5, 1, 1),
    _NsSetSnmpCommHostIndex_Type()
)
nsSetSnmpCommHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetSnmpCommHostIndex.setStatus("current")


class _NsSetSnmpCommunity_Type(DisplayString):
    """Custom type nsSetSnmpCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSetSnmpCommunity_Type.__name__ = "DisplayString"
_NsSetSnmpCommunity_Object = MibTableColumn
nsSetSnmpCommunity = _NsSetSnmpCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 9, 5, 1, 2),
    _NsSetSnmpCommunity_Type()
)
nsSetSnmpCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetSnmpCommunity.setStatus("current")
_NsSetSnmpHostInComm_Type = IpAddress
_NsSetSnmpHostInComm_Object = MibTableColumn
nsSetSnmpHostInComm = _NsSetSnmpHostInComm_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 9, 5, 1, 3),
    _NsSetSnmpHostInComm_Type()
)
nsSetSnmpHostInComm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetSnmpHostInComm.setStatus("current")


class _NsSetSnmpWritePermit_Type(Integer32):
    """Custom type nsSetSnmpWritePermit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NsSetSnmpWritePermit_Type.__name__ = "Integer32"
_NsSetSnmpWritePermit_Object = MibTableColumn
nsSetSnmpWritePermit = _NsSetSnmpWritePermit_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 9, 5, 1, 4),
    _NsSetSnmpWritePermit_Type()
)
nsSetSnmpWritePermit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetSnmpWritePermit.setStatus("current")


class _NsSetSnmpTrapPermit_Type(Integer32):
    """Custom type nsSetSnmpTrapPermit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NsSetSnmpTrapPermit_Type.__name__ = "Integer32"
_NsSetSnmpTrapPermit_Object = MibTableColumn
nsSetSnmpTrapPermit = _NsSetSnmpTrapPermit_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 9, 5, 1, 5),
    _NsSetSnmpTrapPermit_Type()
)
nsSetSnmpTrapPermit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetSnmpTrapPermit.setStatus("current")


class _NsSetSnmpTrafficAlarmPermit_Type(Integer32):
    """Custom type nsSetSnmpTrafficAlarmPermit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NsSetSnmpTrafficAlarmPermit_Type.__name__ = "Integer32"
_NsSetSnmpTrafficAlarmPermit_Object = MibTableColumn
nsSetSnmpTrafficAlarmPermit = _NsSetSnmpTrafficAlarmPermit_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 9, 5, 1, 6),
    _NsSetSnmpTrafficAlarmPermit_Type()
)
nsSetSnmpTrafficAlarmPermit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetSnmpTrafficAlarmPermit.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-SET-SNMP-MIB",
    **{"netscreenSetSnmpMibModule": netscreenSetSnmpMibModule,
       "nsSetSNMP": nsSetSNMP,
       "nsSetSnmpSysName": nsSetSnmpSysName,
       "nsSetSnmpContact": nsSetSnmpContact,
       "nsSetSnmpLocation": nsSetSnmpLocation,
       "nsSetSnmpVPNEnable": nsSetSnmpVPNEnable,
       "nsSetSnmpCommHostTable": nsSetSnmpCommHostTable,
       "nsSetSnmpCommHostEntry": nsSetSnmpCommHostEntry,
       "nsSetSnmpCommHostIndex": nsSetSnmpCommHostIndex,
       "nsSetSnmpCommunity": nsSetSnmpCommunity,
       "nsSetSnmpHostInComm": nsSetSnmpHostInComm,
       "nsSetSnmpWritePermit": nsSetSnmpWritePermit,
       "nsSetSnmpTrapPermit": nsSetSnmpTrapPermit,
       "nsSetSnmpTrafficAlarmPermit": nsSetSnmpTrafficAlarmPermit}
)
