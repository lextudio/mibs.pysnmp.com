# SNMP MIB module (RAPID-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAPID-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:40 2024
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

(rapidstream,) = mibBuilder.importSymbols(
    "RAPID-MIB",
    "rapidstream")

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


# MODULE-IDENTITY

rsPolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 4)
)
rsPolicyMIB.setRevisions(
        ("2001-05-21 12:00",
         "2002-11-01 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsPolicyToTunnel_ObjectIdentity = ObjectIdentity
rsPolicyToTunnel = _RsPolicyToTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 4, 1)
)
if mibBuilder.loadTexts:
    rsPolicyToTunnel.setStatus("current")
_RsPolicyToTunnelNum_Type = Unsigned32
_RsPolicyToTunnelNum_Object = MibScalar
rsPolicyToTunnelNum = _RsPolicyToTunnelNum_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 1, 1),
    _RsPolicyToTunnelNum_Type()
)
rsPolicyToTunnelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyToTunnelNum.setStatus("current")
_RsPolicyToTunnelTable_Object = MibTable
rsPolicyToTunnelTable = _RsPolicyToTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 1, 2)
)
if mibBuilder.loadTexts:
    rsPolicyToTunnelTable.setStatus("current")
_RsPolicyToTunnelEntry_Object = MibTableRow
rsPolicyToTunnelEntry = _RsPolicyToTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 1, 2, 1)
)
rsPolicyToTunnelEntry.setIndexNames(
    (0, "RAPID-POLICY-MIB", "rsPolicyToTunnelPolicyID"),
    (0, "RAPID-POLICY-MIB", "rsPolicyToTunnelTunnelID"),
)
if mibBuilder.loadTexts:
    rsPolicyToTunnelEntry.setStatus("current")
_RsPolicyToTunnelPolicyID_Type = Integer32
_RsPolicyToTunnelPolicyID_Object = MibTableColumn
rsPolicyToTunnelPolicyID = _RsPolicyToTunnelPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 1, 2, 1, 1),
    _RsPolicyToTunnelPolicyID_Type()
)
rsPolicyToTunnelPolicyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyToTunnelPolicyID.setStatus("current")
_RsPolicyToTunnelTunnelID_Type = Integer32
_RsPolicyToTunnelTunnelID_Object = MibTableColumn
rsPolicyToTunnelTunnelID = _RsPolicyToTunnelTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 1, 2, 1, 2),
    _RsPolicyToTunnelTunnelID_Type()
)
rsPolicyToTunnelTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyToTunnelTunnelID.setStatus("current")
_RsPolicyStatistics_ObjectIdentity = ObjectIdentity
rsPolicyStatistics = _RsPolicyStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2)
)
if mibBuilder.loadTexts:
    rsPolicyStatistics.setStatus("current")
_RsPolicyTableNum_Type = Unsigned32
_RsPolicyTableNum_Object = MibScalar
rsPolicyTableNum = _RsPolicyTableNum_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 1),
    _RsPolicyTableNum_Type()
)
rsPolicyTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyTableNum.setStatus("current")
_RsPolicyTable_Object = MibTable
rsPolicyTable = _RsPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2)
)
if mibBuilder.loadTexts:
    rsPolicyTable.setStatus("current")
_RsPolicyEntry_Object = MibTableRow
rsPolicyEntry = _RsPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1)
)
rsPolicyEntry.setIndexNames(
    (0, "RAPID-POLICY-MIB", "rsPolicyID"),
)
if mibBuilder.loadTexts:
    rsPolicyEntry.setStatus("current")
_RsPolicyID_Type = Integer32
_RsPolicyID_Object = MibTableColumn
rsPolicyID = _RsPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 1),
    _RsPolicyID_Type()
)
rsPolicyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyID.setStatus("current")


class _RsPolicyName_Type(OctetString):
    """Custom type rsPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_RsPolicyName_Type.__name__ = "OctetString"
_RsPolicyName_Object = MibTableColumn
rsPolicyName = _RsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 2),
    _RsPolicyName_Type()
)
rsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyName.setStatus("current")
_RsPolicyBytes_Type = Counter64
_RsPolicyBytes_Object = MibTableColumn
rsPolicyBytes = _RsPolicyBytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 3),
    _RsPolicyBytes_Type()
)
rsPolicyBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyBytes.setStatus("current")
_RsPolicyPackets_Type = Counter64
_RsPolicyPackets_Object = MibTableColumn
rsPolicyPackets = _RsPolicyPackets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 4),
    _RsPolicyPackets_Type()
)
rsPolicyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyPackets.setStatus("current")
_RsPolicyIpsecDecryptErr_Type = Counter64
_RsPolicyIpsecDecryptErr_Object = MibTableColumn
rsPolicyIpsecDecryptErr = _RsPolicyIpsecDecryptErr_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 5),
    _RsPolicyIpsecDecryptErr_Type()
)
rsPolicyIpsecDecryptErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyIpsecDecryptErr.setStatus("current")
_RsPolicyIpsecAuthErr_Type = Counter64
_RsPolicyIpsecAuthErr_Object = MibTableColumn
rsPolicyIpsecAuthErr = _RsPolicyIpsecAuthErr_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 6),
    _RsPolicyIpsecAuthErr_Type()
)
rsPolicyIpsecAuthErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyIpsecAuthErr.setStatus("current")
_RsPolicyIpsecReplayErr_Type = Counter64
_RsPolicyIpsecReplayErr_Object = MibTableColumn
rsPolicyIpsecReplayErr = _RsPolicyIpsecReplayErr_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 7),
    _RsPolicyIpsecReplayErr_Type()
)
rsPolicyIpsecReplayErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyIpsecReplayErr.setStatus("current")
_RsPolicyIpsecPadErr_Type = Counter64
_RsPolicyIpsecPadErr_Object = MibTableColumn
rsPolicyIpsecPadErr = _RsPolicyIpsecPadErr_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 8),
    _RsPolicyIpsecPadErr_Type()
)
rsPolicyIpsecPadErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyIpsecPadErr.setStatus("current")
_RsPolicyIpsecPolicyErr_Type = Counter64
_RsPolicyIpsecPolicyErr_Object = MibTableColumn
rsPolicyIpsecPolicyErr = _RsPolicyIpsecPolicyErr_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 9),
    _RsPolicyIpsecPolicyErr_Type()
)
rsPolicyIpsecPolicyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyIpsecPolicyErr.setStatus("current")
_RsPolicyFwDisc_Type = Counter64
_RsPolicyFwDisc_Object = MibTableColumn
rsPolicyFwDisc = _RsPolicyFwDisc_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 10),
    _RsPolicyFwDisc_Type()
)
rsPolicyFwDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyFwDisc.setStatus("current")
_RsPolicyOtherDisc_Type = Counter64
_RsPolicyOtherDisc_Object = MibTableColumn
rsPolicyOtherDisc = _RsPolicyOtherDisc_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 11),
    _RsPolicyOtherDisc_Type()
)
rsPolicyOtherDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyOtherDisc.setStatus("current")
_RsPolicyActiveStreams_Type = Counter64
_RsPolicyActiveStreams_Object = MibTableColumn
rsPolicyActiveStreams = _RsPolicyActiveStreams_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 12),
    _RsPolicyActiveStreams_Type()
)
rsPolicyActiveStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyActiveStreams.setStatus("current")
_RsPolicyIpsecDisc_Type = Counter64
_RsPolicyIpsecDisc_Object = MibTableColumn
rsPolicyIpsecDisc = _RsPolicyIpsecDisc_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 13),
    _RsPolicyIpsecDisc_Type()
)
rsPolicyIpsecDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyIpsecDisc.setStatus("current")
_RsPolicyDisc_Type = Counter64
_RsPolicyDisc_Object = MibTableColumn
rsPolicyDisc = _RsPolicyDisc_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 14),
    _RsPolicyDisc_Type()
)
rsPolicyDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyDisc.setStatus("current")
_RsPolicyNumTunl_Type = Counter64
_RsPolicyNumTunl_Object = MibTableColumn
rsPolicyNumTunl = _RsPolicyNumTunl_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 15),
    _RsPolicyNumTunl_Type()
)
rsPolicyNumTunl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyNumTunl.setStatus("current")
_RsPolicySingleCntrNum_Type = Counter64
_RsPolicySingleCntrNum_Object = MibTableColumn
rsPolicySingleCntrNum = _RsPolicySingleCntrNum_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 16),
    _RsPolicySingleCntrNum_Type()
)
rsPolicySingleCntrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicySingleCntrNum.setStatus("current")


class _RsPolicyLogging_Type(Integer32):
    """Custom type rsPolicyLogging based on Integer32"""
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


_RsPolicyLogging_Type.__name__ = "Integer32"
_RsPolicyLogging_Object = MibTableColumn
rsPolicyLogging = _RsPolicyLogging_Object(
    (1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 17),
    _RsPolicyLogging_Type()
)
rsPolicyLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPolicyLogging.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAPID-POLICY-MIB",
    **{"rsPolicyMIB": rsPolicyMIB,
       "rsPolicyToTunnel": rsPolicyToTunnel,
       "rsPolicyToTunnelNum": rsPolicyToTunnelNum,
       "rsPolicyToTunnelTable": rsPolicyToTunnelTable,
       "rsPolicyToTunnelEntry": rsPolicyToTunnelEntry,
       "rsPolicyToTunnelPolicyID": rsPolicyToTunnelPolicyID,
       "rsPolicyToTunnelTunnelID": rsPolicyToTunnelTunnelID,
       "rsPolicyStatistics": rsPolicyStatistics,
       "rsPolicyTableNum": rsPolicyTableNum,
       "rsPolicyTable": rsPolicyTable,
       "rsPolicyEntry": rsPolicyEntry,
       "rsPolicyID": rsPolicyID,
       "rsPolicyName": rsPolicyName,
       "rsPolicyBytes": rsPolicyBytes,
       "rsPolicyPackets": rsPolicyPackets,
       "rsPolicyIpsecDecryptErr": rsPolicyIpsecDecryptErr,
       "rsPolicyIpsecAuthErr": rsPolicyIpsecAuthErr,
       "rsPolicyIpsecReplayErr": rsPolicyIpsecReplayErr,
       "rsPolicyIpsecPadErr": rsPolicyIpsecPadErr,
       "rsPolicyIpsecPolicyErr": rsPolicyIpsecPolicyErr,
       "rsPolicyFwDisc": rsPolicyFwDisc,
       "rsPolicyOtherDisc": rsPolicyOtherDisc,
       "rsPolicyActiveStreams": rsPolicyActiveStreams,
       "rsPolicyIpsecDisc": rsPolicyIpsecDisc,
       "rsPolicyDisc": rsPolicyDisc,
       "rsPolicyNumTunl": rsPolicyNumTunl,
       "rsPolicySingleCntrNum": rsPolicySingleCntrNum,
       "rsPolicyLogging": rsPolicyLogging}
)
