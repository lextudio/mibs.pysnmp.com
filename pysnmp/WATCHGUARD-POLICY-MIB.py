# SNMP MIB module (WATCHGUARD-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WATCHGUARD-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:37 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")

(watchguard,) = mibBuilder.importSymbols(
    "WATCHGUARD-MIB",
    "watchguard")


# MODULE-IDENTITY

wgPolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 4)
)
wgPolicyMIB.setRevisions(
        ("2007-01-25 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WgPolicyToTunnel_ObjectIdentity = ObjectIdentity
wgPolicyToTunnel = _WgPolicyToTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 4, 1)
)
if mibBuilder.loadTexts:
    wgPolicyToTunnel.setStatus("current")
_WgPolicyToTunnelNum_Type = Unsigned32
_WgPolicyToTunnelNum_Object = MibScalar
wgPolicyToTunnelNum = _WgPolicyToTunnelNum_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 1, 1),
    _WgPolicyToTunnelNum_Type()
)
wgPolicyToTunnelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyToTunnelNum.setStatus("current")
_WgPolicyToTunnelTable_Object = MibTable
wgPolicyToTunnelTable = _WgPolicyToTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 1, 2)
)
if mibBuilder.loadTexts:
    wgPolicyToTunnelTable.setStatus("current")
_WgPolicyToTunnelEntry_Object = MibTableRow
wgPolicyToTunnelEntry = _WgPolicyToTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 1, 2, 1)
)
wgPolicyToTunnelEntry.setIndexNames(
    (0, "WATCHGUARD-POLICY-MIB", "wgPolicyToTunnelPolicyID"),
    (0, "WATCHGUARD-POLICY-MIB", "wgPolicyToTunnelTunnelID"),
)
if mibBuilder.loadTexts:
    wgPolicyToTunnelEntry.setStatus("current")
_WgPolicyToTunnelPolicyID_Type = Integer32
_WgPolicyToTunnelPolicyID_Object = MibTableColumn
wgPolicyToTunnelPolicyID = _WgPolicyToTunnelPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 1, 2, 1, 1),
    _WgPolicyToTunnelPolicyID_Type()
)
wgPolicyToTunnelPolicyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyToTunnelPolicyID.setStatus("current")
_WgPolicyToTunnelTunnelID_Type = Integer32
_WgPolicyToTunnelTunnelID_Object = MibTableColumn
wgPolicyToTunnelTunnelID = _WgPolicyToTunnelTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 1, 2, 1, 2),
    _WgPolicyToTunnelTunnelID_Type()
)
wgPolicyToTunnelTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyToTunnelTunnelID.setStatus("current")
_WgPolicyStatistics_ObjectIdentity = ObjectIdentity
wgPolicyStatistics = _WgPolicyStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2)
)
if mibBuilder.loadTexts:
    wgPolicyStatistics.setStatus("current")
_WgPolicyTableNum_Type = Unsigned32
_WgPolicyTableNum_Object = MibScalar
wgPolicyTableNum = _WgPolicyTableNum_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 1),
    _WgPolicyTableNum_Type()
)
wgPolicyTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyTableNum.setStatus("current")
_WgPolicyTable_Object = MibTable
wgPolicyTable = _WgPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2)
)
if mibBuilder.loadTexts:
    wgPolicyTable.setStatus("current")
_WgPolicyEntry_Object = MibTableRow
wgPolicyEntry = _WgPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1)
)
wgPolicyEntry.setIndexNames(
    (0, "WATCHGUARD-POLICY-MIB", "wgPolicyID"),
)
if mibBuilder.loadTexts:
    wgPolicyEntry.setStatus("current")
_WgPolicyID_Type = Integer32
_WgPolicyID_Object = MibTableColumn
wgPolicyID = _WgPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 1),
    _WgPolicyID_Type()
)
wgPolicyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyID.setStatus("current")


class _WgPolicyName_Type(OctetString):
    """Custom type wgPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_WgPolicyName_Type.__name__ = "OctetString"
_WgPolicyName_Object = MibTableColumn
wgPolicyName = _WgPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 2),
    _WgPolicyName_Type()
)
wgPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyName.setStatus("current")
_WgPolicyBytes_Type = Counter64
_WgPolicyBytes_Object = MibTableColumn
wgPolicyBytes = _WgPolicyBytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 3),
    _WgPolicyBytes_Type()
)
wgPolicyBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyBytes.setStatus("current")
_WgPolicyPackets_Type = Counter64
_WgPolicyPackets_Object = MibTableColumn
wgPolicyPackets = _WgPolicyPackets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 4),
    _WgPolicyPackets_Type()
)
wgPolicyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyPackets.setStatus("current")
_WgPolicyIpsecDecryptErr_Type = Counter64
_WgPolicyIpsecDecryptErr_Object = MibTableColumn
wgPolicyIpsecDecryptErr = _WgPolicyIpsecDecryptErr_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 5),
    _WgPolicyIpsecDecryptErr_Type()
)
wgPolicyIpsecDecryptErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyIpsecDecryptErr.setStatus("current")
_WgPolicyIpsecAuthErr_Type = Counter64
_WgPolicyIpsecAuthErr_Object = MibTableColumn
wgPolicyIpsecAuthErr = _WgPolicyIpsecAuthErr_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 6),
    _WgPolicyIpsecAuthErr_Type()
)
wgPolicyIpsecAuthErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyIpsecAuthErr.setStatus("current")
_WgPolicyIpsecReplayErr_Type = Counter64
_WgPolicyIpsecReplayErr_Object = MibTableColumn
wgPolicyIpsecReplayErr = _WgPolicyIpsecReplayErr_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 7),
    _WgPolicyIpsecReplayErr_Type()
)
wgPolicyIpsecReplayErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyIpsecReplayErr.setStatus("current")
_WgPolicyIpsecPadErr_Type = Counter64
_WgPolicyIpsecPadErr_Object = MibTableColumn
wgPolicyIpsecPadErr = _WgPolicyIpsecPadErr_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 8),
    _WgPolicyIpsecPadErr_Type()
)
wgPolicyIpsecPadErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyIpsecPadErr.setStatus("current")
_WgPolicyIpsecPolicyErr_Type = Counter64
_WgPolicyIpsecPolicyErr_Object = MibTableColumn
wgPolicyIpsecPolicyErr = _WgPolicyIpsecPolicyErr_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 9),
    _WgPolicyIpsecPolicyErr_Type()
)
wgPolicyIpsecPolicyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyIpsecPolicyErr.setStatus("current")
_WgPolicyFwDisc_Type = Counter64
_WgPolicyFwDisc_Object = MibTableColumn
wgPolicyFwDisc = _WgPolicyFwDisc_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 10),
    _WgPolicyFwDisc_Type()
)
wgPolicyFwDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyFwDisc.setStatus("current")
_WgPolicyOtherDisc_Type = Counter64
_WgPolicyOtherDisc_Object = MibTableColumn
wgPolicyOtherDisc = _WgPolicyOtherDisc_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 11),
    _WgPolicyOtherDisc_Type()
)
wgPolicyOtherDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyOtherDisc.setStatus("current")
_WgPolicyActiveStreams_Type = Counter64
_WgPolicyActiveStreams_Object = MibTableColumn
wgPolicyActiveStreams = _WgPolicyActiveStreams_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 12),
    _WgPolicyActiveStreams_Type()
)
wgPolicyActiveStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyActiveStreams.setStatus("current")
_WgPolicyIpsecDisc_Type = Counter64
_WgPolicyIpsecDisc_Object = MibTableColumn
wgPolicyIpsecDisc = _WgPolicyIpsecDisc_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 13),
    _WgPolicyIpsecDisc_Type()
)
wgPolicyIpsecDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyIpsecDisc.setStatus("current")
_WgPolicyDisc_Type = Counter64
_WgPolicyDisc_Object = MibTableColumn
wgPolicyDisc = _WgPolicyDisc_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 14),
    _WgPolicyDisc_Type()
)
wgPolicyDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyDisc.setStatus("current")
_WgPolicyNumTunl_Type = Counter64
_WgPolicyNumTunl_Object = MibTableColumn
wgPolicyNumTunl = _WgPolicyNumTunl_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 15),
    _WgPolicyNumTunl_Type()
)
wgPolicyNumTunl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyNumTunl.setStatus("current")
_WgPolicySingleCntrNum_Type = Counter64
_WgPolicySingleCntrNum_Object = MibTableColumn
wgPolicySingleCntrNum = _WgPolicySingleCntrNum_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 16),
    _WgPolicySingleCntrNum_Type()
)
wgPolicySingleCntrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicySingleCntrNum.setStatus("current")


class _WgPolicyLogging_Type(Integer32):
    """Custom type wgPolicyLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WgPolicyLogging_Type.__name__ = "Integer32"
_WgPolicyLogging_Object = MibTableColumn
wgPolicyLogging = _WgPolicyLogging_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 17),
    _WgPolicyLogging_Type()
)
wgPolicyLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyLogging.setStatus("current")
_WgPolicyCurrActiveConns_Type = Counter64
_WgPolicyCurrActiveConns_Object = MibTableColumn
wgPolicyCurrActiveConns = _WgPolicyCurrActiveConns_Object(
    (1, 3, 6, 1, 4, 1, 3097, 4, 2, 2, 1, 18),
    _WgPolicyCurrActiveConns_Type()
)
wgPolicyCurrActiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPolicyCurrActiveConns.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WATCHGUARD-POLICY-MIB",
    **{"wgPolicyMIB": wgPolicyMIB,
       "wgPolicyToTunnel": wgPolicyToTunnel,
       "wgPolicyToTunnelNum": wgPolicyToTunnelNum,
       "wgPolicyToTunnelTable": wgPolicyToTunnelTable,
       "wgPolicyToTunnelEntry": wgPolicyToTunnelEntry,
       "wgPolicyToTunnelPolicyID": wgPolicyToTunnelPolicyID,
       "wgPolicyToTunnelTunnelID": wgPolicyToTunnelTunnelID,
       "wgPolicyStatistics": wgPolicyStatistics,
       "wgPolicyTableNum": wgPolicyTableNum,
       "wgPolicyTable": wgPolicyTable,
       "wgPolicyEntry": wgPolicyEntry,
       "wgPolicyID": wgPolicyID,
       "wgPolicyName": wgPolicyName,
       "wgPolicyBytes": wgPolicyBytes,
       "wgPolicyPackets": wgPolicyPackets,
       "wgPolicyIpsecDecryptErr": wgPolicyIpsecDecryptErr,
       "wgPolicyIpsecAuthErr": wgPolicyIpsecAuthErr,
       "wgPolicyIpsecReplayErr": wgPolicyIpsecReplayErr,
       "wgPolicyIpsecPadErr": wgPolicyIpsecPadErr,
       "wgPolicyIpsecPolicyErr": wgPolicyIpsecPolicyErr,
       "wgPolicyFwDisc": wgPolicyFwDisc,
       "wgPolicyOtherDisc": wgPolicyOtherDisc,
       "wgPolicyActiveStreams": wgPolicyActiveStreams,
       "wgPolicyIpsecDisc": wgPolicyIpsecDisc,
       "wgPolicyDisc": wgPolicyDisc,
       "wgPolicyNumTunl": wgPolicyNumTunl,
       "wgPolicySingleCntrNum": wgPolicySingleCntrNum,
       "wgPolicyLogging": wgPolicyLogging,
       "wgPolicyCurrActiveConns": wgPolicyCurrActiveConns}
)
