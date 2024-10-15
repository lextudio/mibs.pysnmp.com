# SNMP MIB module (RUCKUS-WLINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-WLINK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:51 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ruckusCommonWLINKModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusCommonWLINKModule")

(RuckusSSID,) = mibBuilder.importSymbols(
    "RUCKUS-TC-MIB",
    "RuckusSSID")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruckusWLINKMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusWLINKObjects_ObjectIdentity = ObjectIdentity
ruckusWLINKObjects = _RuckusWLINKObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1)
)
_RuckusWLINKInfo_ObjectIdentity = ObjectIdentity
ruckusWLINKInfo = _RuckusWLINKInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1)
)
_RuckusWLINKTable_Object = MibTable
ruckusWLINKTable = _RuckusWLINKTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusWLINKTable.setStatus("current")
_RuckusWLINKEntry_Object = MibTableRow
ruckusWLINKEntry = _RuckusWLINKEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1)
)
ruckusWLINKEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusWLINKEntry.setStatus("current")
_RuckusWLINKSSID_Type = RuckusSSID
_RuckusWLINKSSID_Object = MibTableColumn
ruckusWLINKSSID = _RuckusWLINKSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 1),
    _RuckusWLINKSSID_Type()
)
ruckusWLINKSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKSSID.setStatus("current")


class _RuckusWLINKRole_Type(Integer32):
    """Custom type ruckusWLINKRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("nonRootBridge", 2),
          ("notAvailable", 4),
          ("notDecided", 3),
          ("rootBridge", 1))
    )


_RuckusWLINKRole_Type.__name__ = "Integer32"
_RuckusWLINKRole_Object = MibTableColumn
ruckusWLINKRole = _RuckusWLINKRole_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 2),
    _RuckusWLINKRole_Type()
)
ruckusWLINKRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKRole.setStatus("current")
_RuckusWLINKLocalMAC_Type = MacAddress
_RuckusWLINKLocalMAC_Object = MibTableColumn
ruckusWLINKLocalMAC = _RuckusWLINKLocalMAC_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 3),
    _RuckusWLINKLocalMAC_Type()
)
ruckusWLINKLocalMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKLocalMAC.setStatus("current")
_RuckusWLINKRemoteMAC_Type = MacAddress
_RuckusWLINKRemoteMAC_Object = MibTableColumn
ruckusWLINKRemoteMAC = _RuckusWLINKRemoteMAC_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 4),
    _RuckusWLINKRemoteMAC_Type()
)
ruckusWLINKRemoteMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKRemoteMAC.setStatus("current")
_RuckusWLINKTxPkts_Type = Counter32
_RuckusWLINKTxPkts_Object = MibTableColumn
ruckusWLINKTxPkts = _RuckusWLINKTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 5),
    _RuckusWLINKTxPkts_Type()
)
ruckusWLINKTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKTxPkts.setStatus("current")
_RuckusWLINKTxBytes_Type = Counter32
_RuckusWLINKTxBytes_Object = MibTableColumn
ruckusWLINKTxBytes = _RuckusWLINKTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 6),
    _RuckusWLINKTxBytes_Type()
)
ruckusWLINKTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKTxBytes.setStatus("current")
_RuckusWLINKRxPkts_Type = Counter32
_RuckusWLINKRxPkts_Object = MibTableColumn
ruckusWLINKRxPkts = _RuckusWLINKRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 7),
    _RuckusWLINKRxPkts_Type()
)
ruckusWLINKRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKRxPkts.setStatus("current")
_RuckusWLINKRxBytes_Type = Counter32
_RuckusWLINKRxBytes_Object = MibTableColumn
ruckusWLINKRxBytes = _RuckusWLINKRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 8),
    _RuckusWLINKRxBytes_Type()
)
ruckusWLINKRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKRxBytes.setStatus("current")


class _RuckusWLINKEstablishTime_Type(DisplayString):
    """Custom type ruckusWLINKEstablishTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusWLINKEstablishTime_Type.__name__ = "DisplayString"
_RuckusWLINKEstablishTime_Object = MibTableColumn
ruckusWLINKEstablishTime = _RuckusWLINKEstablishTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 9),
    _RuckusWLINKEstablishTime_Type()
)
ruckusWLINKEstablishTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKEstablishTime.setStatus("current")
_RuckusWLINKUpTime_Type = Unsigned32
_RuckusWLINKUpTime_Object = MibTableColumn
ruckusWLINKUpTime = _RuckusWLINKUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 10),
    _RuckusWLINKUpTime_Type()
)
ruckusWLINKUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKUpTime.setStatus("current")
_RuckusWLINKRssi_Type = Integer32
_RuckusWLINKRssi_Object = MibTableColumn
ruckusWLINKRssi = _RuckusWLINKRssi_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 11),
    _RuckusWLINKRssi_Type()
)
ruckusWLINKRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKRssi.setStatus("current")
_RuckusWLINKUpCount_Type = Integer32
_RuckusWLINKUpCount_Object = MibTableColumn
ruckusWLINKUpCount = _RuckusWLINKUpCount_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 12),
    _RuckusWLINKUpCount_Type()
)
ruckusWLINKUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKUpCount.setStatus("current")
_RuckusWLINKDownCount_Type = Integer32
_RuckusWLINKDownCount_Object = MibTableColumn
ruckusWLINKDownCount = _RuckusWLINKDownCount_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 13),
    _RuckusWLINKDownCount_Type()
)
ruckusWLINKDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLINKDownCount.setStatus("current")
_RuckusWLINKEvents_ObjectIdentity = ObjectIdentity
ruckusWLINKEvents = _RuckusWLINKEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-WLINK-MIB",
    **{"ruckusWLINKMIB": ruckusWLINKMIB,
       "ruckusWLINKObjects": ruckusWLINKObjects,
       "ruckusWLINKInfo": ruckusWLINKInfo,
       "ruckusWLINKTable": ruckusWLINKTable,
       "ruckusWLINKEntry": ruckusWLINKEntry,
       "ruckusWLINKSSID": ruckusWLINKSSID,
       "ruckusWLINKRole": ruckusWLINKRole,
       "ruckusWLINKLocalMAC": ruckusWLINKLocalMAC,
       "ruckusWLINKRemoteMAC": ruckusWLINKRemoteMAC,
       "ruckusWLINKTxPkts": ruckusWLINKTxPkts,
       "ruckusWLINKTxBytes": ruckusWLINKTxBytes,
       "ruckusWLINKRxPkts": ruckusWLINKRxPkts,
       "ruckusWLINKRxBytes": ruckusWLINKRxBytes,
       "ruckusWLINKEstablishTime": ruckusWLINKEstablishTime,
       "ruckusWLINKUpTime": ruckusWLINKUpTime,
       "ruckusWLINKRssi": ruckusWLINKRssi,
       "ruckusWLINKUpCount": ruckusWLINKUpCount,
       "ruckusWLINKDownCount": ruckusWLINKDownCount,
       "ruckusWLINKEvents": ruckusWLINKEvents}
)
