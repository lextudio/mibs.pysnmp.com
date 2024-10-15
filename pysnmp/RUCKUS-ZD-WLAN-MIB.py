# SNMP MIB module (RUCKUS-ZD-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-ZD-WLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:56 2024
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ruckusZDWLANModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusZDWLANModule")

(RuckusAdminStatus,
 RuckusRadioMode,
 RuckusRateLimiting,
 RuckusSSID,
 RuckusdB) = mibBuilder.importSymbols(
    "RUCKUS-TC-MIB",
    "RuckusAdminStatus",
    "RuckusRadioMode",
    "RuckusRateLimiting",
    "RuckusSSID",
    "RuckusdB")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusZDWLANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusZDWLANObjects_ObjectIdentity = ObjectIdentity
ruckusZDWLANObjects = _RuckusZDWLANObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1)
)
_RuckusZDWLANInfo_ObjectIdentity = ObjectIdentity
ruckusZDWLANInfo = _RuckusZDWLANInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1)
)
_RuckusZDWLANTable_Object = MibTable
ruckusZDWLANTable = _RuckusZDWLANTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusZDWLANTable.setStatus("current")
_RuckusZDWLANEntry_Object = MibTableRow
ruckusZDWLANEntry = _RuckusZDWLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1)
)
ruckusZDWLANEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusZDWLANEntry.setStatus("current")
_RuckusZDWLANSSID_Type = RuckusSSID
_RuckusZDWLANSSID_Object = MibTableColumn
ruckusZDWLANSSID = _RuckusZDWLANSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 1),
    _RuckusZDWLANSSID_Type()
)
ruckusZDWLANSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANSSID.setStatus("current")
_RuckusZDWLANDescription_Type = DisplayString
_RuckusZDWLANDescription_Object = MibTableColumn
ruckusZDWLANDescription = _RuckusZDWLANDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 2),
    _RuckusZDWLANDescription_Type()
)
ruckusZDWLANDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANDescription.setStatus("current")
_RuckusZDWLANAuthentication_Type = DisplayString
_RuckusZDWLANAuthentication_Object = MibTableColumn
ruckusZDWLANAuthentication = _RuckusZDWLANAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 3),
    _RuckusZDWLANAuthentication_Type()
)
ruckusZDWLANAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAuthentication.setStatus("current")
_RuckusZDWLANEncryption_Type = DisplayString
_RuckusZDWLANEncryption_Object = MibTableColumn
ruckusZDWLANEncryption = _RuckusZDWLANEncryption_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 4),
    _RuckusZDWLANEncryption_Type()
)
ruckusZDWLANEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANEncryption.setStatus("current")
_RuckusZDWLANIsGuest_Type = TruthValue
_RuckusZDWLANIsGuest_Object = MibTableColumn
ruckusZDWLANIsGuest = _RuckusZDWLANIsGuest_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 5),
    _RuckusZDWLANIsGuest_Type()
)
ruckusZDWLANIsGuest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANIsGuest.setStatus("current")
_RuckusZDWLANSSIDBcastDisable_Type = TruthValue
_RuckusZDWLANSSIDBcastDisable_Object = MibTableColumn
ruckusZDWLANSSIDBcastDisable = _RuckusZDWLANSSIDBcastDisable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 6),
    _RuckusZDWLANSSIDBcastDisable_Type()
)
ruckusZDWLANSSIDBcastDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANSSIDBcastDisable.setStatus("current")


class _RuckusZDWLANVlanID_Type(Integer32):
    """Custom type ruckusZDWLANVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuckusZDWLANVlanID_Type.__name__ = "Integer32"
_RuckusZDWLANVlanID_Object = MibTableColumn
ruckusZDWLANVlanID = _RuckusZDWLANVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 7),
    _RuckusZDWLANVlanID_Type()
)
ruckusZDWLANVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANVlanID.setStatus("current")


class _RuckusZDWLANRateLimitingUp_Type(OctetString):
    """Custom type ruckusZDWLANRateLimitingUp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_RuckusZDWLANRateLimitingUp_Type.__name__ = "OctetString"
_RuckusZDWLANRateLimitingUp_Object = MibTableColumn
ruckusZDWLANRateLimitingUp = _RuckusZDWLANRateLimitingUp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 8),
    _RuckusZDWLANRateLimitingUp_Type()
)
ruckusZDWLANRateLimitingUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANRateLimitingUp.setStatus("current")


class _RuckusZDWLANRateLimitingDown_Type(OctetString):
    """Custom type ruckusZDWLANRateLimitingDown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_RuckusZDWLANRateLimitingDown_Type.__name__ = "OctetString"
_RuckusZDWLANRateLimitingDown_Object = MibTableColumn
ruckusZDWLANRateLimitingDown = _RuckusZDWLANRateLimitingDown_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 9),
    _RuckusZDWLANRateLimitingDown_Type()
)
ruckusZDWLANRateLimitingDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANRateLimitingDown.setStatus("current")
_RuckusZDWLANTunnelWLAN_Type = TruthValue
_RuckusZDWLANTunnelWLAN_Object = MibTableColumn
ruckusZDWLANTunnelWLAN = _RuckusZDWLANTunnelWLAN_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 10),
    _RuckusZDWLANTunnelWLAN_Type()
)
ruckusZDWLANTunnelWLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANTunnelWLAN.setStatus("current")
_RuckusZDWLANNumVAP_Type = Unsigned32
_RuckusZDWLANNumVAP_Object = MibTableColumn
ruckusZDWLANNumVAP = _RuckusZDWLANNumVAP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 11),
    _RuckusZDWLANNumVAP_Type()
)
ruckusZDWLANNumVAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANNumVAP.setStatus("current")
_RuckusZDWLANNumSta_Type = Unsigned32
_RuckusZDWLANNumSta_Object = MibTableColumn
ruckusZDWLANNumSta = _RuckusZDWLANNumSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 12),
    _RuckusZDWLANNumSta_Type()
)
ruckusZDWLANNumSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANNumSta.setStatus("current")
_RuckusZDWLANRxPkts_Type = Counter64
_RuckusZDWLANRxPkts_Object = MibTableColumn
ruckusZDWLANRxPkts = _RuckusZDWLANRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 13),
    _RuckusZDWLANRxPkts_Type()
)
ruckusZDWLANRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANRxPkts.setStatus("current")
_RuckusZDWLANRxBytes_Type = Counter64
_RuckusZDWLANRxBytes_Object = MibTableColumn
ruckusZDWLANRxBytes = _RuckusZDWLANRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 14),
    _RuckusZDWLANRxBytes_Type()
)
ruckusZDWLANRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANRxBytes.setStatus("current")
_RuckusZDWLANTxPkts_Type = Counter64
_RuckusZDWLANTxPkts_Object = MibTableColumn
ruckusZDWLANTxPkts = _RuckusZDWLANTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 15),
    _RuckusZDWLANTxPkts_Type()
)
ruckusZDWLANTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANTxPkts.setStatus("current")
_RuckusZDWLANTxBytes_Type = Counter64
_RuckusZDWLANTxBytes_Object = MibTableColumn
ruckusZDWLANTxBytes = _RuckusZDWLANTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 16),
    _RuckusZDWLANTxBytes_Type()
)
ruckusZDWLANTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANTxBytes.setStatus("current")
_RuckusZDWLANAuthTotal_Type = Counter64
_RuckusZDWLANAuthTotal_Object = MibTableColumn
ruckusZDWLANAuthTotal = _RuckusZDWLANAuthTotal_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 26),
    _RuckusZDWLANAuthTotal_Type()
)
ruckusZDWLANAuthTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAuthTotal.setStatus("current")
_RuckusZDWLANAuthResp_Type = Counter64
_RuckusZDWLANAuthResp_Object = MibTableColumn
ruckusZDWLANAuthResp = _RuckusZDWLANAuthResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 27),
    _RuckusZDWLANAuthResp_Type()
)
ruckusZDWLANAuthResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAuthResp.setStatus("current")
_RuckusZDWLANAuthSuccessTotal_Type = Counter64
_RuckusZDWLANAuthSuccessTotal_Object = MibTableColumn
ruckusZDWLANAuthSuccessTotal = _RuckusZDWLANAuthSuccessTotal_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 28),
    _RuckusZDWLANAuthSuccessTotal_Type()
)
ruckusZDWLANAuthSuccessTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAuthSuccessTotal.setStatus("current")
_RuckusZDWLANAuthFail_Type = Counter64
_RuckusZDWLANAuthFail_Object = MibTableColumn
ruckusZDWLANAuthFail = _RuckusZDWLANAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 29),
    _RuckusZDWLANAuthFail_Type()
)
ruckusZDWLANAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAuthFail.setStatus("current")
_RuckusZDWLANAssocTotal_Type = Counter64
_RuckusZDWLANAssocTotal_Object = MibTableColumn
ruckusZDWLANAssocTotal = _RuckusZDWLANAssocTotal_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 30),
    _RuckusZDWLANAssocTotal_Type()
)
ruckusZDWLANAssocTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAssocTotal.setStatus("current")
_RuckusZDWLANAssocResp_Type = Counter64
_RuckusZDWLANAssocResp_Object = MibTableColumn
ruckusZDWLANAssocResp = _RuckusZDWLANAssocResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 31),
    _RuckusZDWLANAssocResp_Type()
)
ruckusZDWLANAssocResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAssocResp.setStatus("current")
_RuckusZDWLANReassocReq_Type = Counter64
_RuckusZDWLANReassocReq_Object = MibTableColumn
ruckusZDWLANReassocReq = _RuckusZDWLANReassocReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 32),
    _RuckusZDWLANReassocReq_Type()
)
ruckusZDWLANReassocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANReassocReq.setStatus("current")
_RuckusZDWLANReassocResp_Type = Counter64
_RuckusZDWLANReassocResp_Object = MibTableColumn
ruckusZDWLANReassocResp = _RuckusZDWLANReassocResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 33),
    _RuckusZDWLANReassocResp_Type()
)
ruckusZDWLANReassocResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANReassocResp.setStatus("current")
_RuckusZDWLANAssocSuccess_Type = Counter64
_RuckusZDWLANAssocSuccess_Object = MibTableColumn
ruckusZDWLANAssocSuccess = _RuckusZDWLANAssocSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 34),
    _RuckusZDWLANAssocSuccess_Type()
)
ruckusZDWLANAssocSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAssocSuccess.setStatus("current")
_RuckusZDWLANAssocFail_Type = Counter64
_RuckusZDWLANAssocFail_Object = MibTableColumn
ruckusZDWLANAssocFail = _RuckusZDWLANAssocFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 35),
    _RuckusZDWLANAssocFail_Type()
)
ruckusZDWLANAssocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAssocFail.setStatus("current")
_RuckusZDWLANAssocDenied_Type = Counter64
_RuckusZDWLANAssocDenied_Object = MibTableColumn
ruckusZDWLANAssocDenied = _RuckusZDWLANAssocDenied_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 36),
    _RuckusZDWLANAssocDenied_Type()
)
ruckusZDWLANAssocDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAssocDenied.setStatus("current")
_RuckusZDWLANDiassocAbnormal_Type = Counter64
_RuckusZDWLANDiassocAbnormal_Object = MibTableColumn
ruckusZDWLANDiassocAbnormal = _RuckusZDWLANDiassocAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 37),
    _RuckusZDWLANDiassocAbnormal_Type()
)
ruckusZDWLANDiassocAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANDiassocAbnormal.setStatus("current")
_RuckusZDWLANDiassocCapacity_Type = Counter64
_RuckusZDWLANDiassocCapacity_Object = MibTableColumn
ruckusZDWLANDiassocCapacity = _RuckusZDWLANDiassocCapacity_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 38),
    _RuckusZDWLANDiassocCapacity_Type()
)
ruckusZDWLANDiassocCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANDiassocCapacity.setStatus("current")
_RuckusZDWLANDiassocLeave_Type = Counter64
_RuckusZDWLANDiassocLeave_Object = MibTableColumn
ruckusZDWLANDiassocLeave = _RuckusZDWLANDiassocLeave_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 39),
    _RuckusZDWLANDiassocLeave_Type()
)
ruckusZDWLANDiassocLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANDiassocLeave.setStatus("current")
_RuckusZDWLANDiassocMisc_Type = Counter64
_RuckusZDWLANDiassocMisc_Object = MibTableColumn
ruckusZDWLANDiassocMisc = _RuckusZDWLANDiassocMisc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 40),
    _RuckusZDWLANDiassocMisc_Type()
)
ruckusZDWLANDiassocMisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANDiassocMisc.setStatus("current")
_RuckusZDWLANRxByteRate_Type = Unsigned32
_RuckusZDWLANRxByteRate_Object = MibTableColumn
ruckusZDWLANRxByteRate = _RuckusZDWLANRxByteRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 41),
    _RuckusZDWLANRxByteRate_Type()
)
ruckusZDWLANRxByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANRxByteRate.setStatus("current")
_RuckusZDWLANTxByteRate_Type = Unsigned32
_RuckusZDWLANTxByteRate_Object = MibTableColumn
ruckusZDWLANTxByteRate = _RuckusZDWLANTxByteRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 42),
    _RuckusZDWLANTxByteRate_Type()
)
ruckusZDWLANTxByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANTxByteRate.setStatus("current")
_RuckusZDWLANRxDataFrameOnLan_Type = Counter64
_RuckusZDWLANRxDataFrameOnLan_Object = MibTableColumn
ruckusZDWLANRxDataFrameOnLan = _RuckusZDWLANRxDataFrameOnLan_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 43),
    _RuckusZDWLANRxDataFrameOnLan_Type()
)
ruckusZDWLANRxDataFrameOnLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANRxDataFrameOnLan.setStatus("current")
_RuckusZDWLANRxByteOnLan_Type = Counter64
_RuckusZDWLANRxByteOnLan_Object = MibTableColumn
ruckusZDWLANRxByteOnLan = _RuckusZDWLANRxByteOnLan_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 44),
    _RuckusZDWLANRxByteOnLan_Type()
)
ruckusZDWLANRxByteOnLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANRxByteOnLan.setStatus("current")
_RuckusZDWLANTxByteOnLan_Type = Counter64
_RuckusZDWLANTxByteOnLan_Object = MibTableColumn
ruckusZDWLANTxByteOnLan = _RuckusZDWLANTxByteOnLan_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 45),
    _RuckusZDWLANTxByteOnLan_Type()
)
ruckusZDWLANTxByteOnLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANTxByteOnLan.setStatus("current")
_RuckusZDWLANDownDropFrame_Type = Counter64
_RuckusZDWLANDownDropFrame_Object = MibTableColumn
ruckusZDWLANDownDropFrame = _RuckusZDWLANDownDropFrame_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 46),
    _RuckusZDWLANDownDropFrame_Type()
)
ruckusZDWLANDownDropFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANDownDropFrame.setStatus("current")
_RuckusZDWLANDownRetxFrame_Type = Counter64
_RuckusZDWLANDownRetxFrame_Object = MibTableColumn
ruckusZDWLANDownRetxFrame = _RuckusZDWLANDownRetxFrame_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 47),
    _RuckusZDWLANDownRetxFrame_Type()
)
ruckusZDWLANDownRetxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANDownRetxFrame.setStatus("current")
_RuckusZDWLANDownTotalFrame_Type = Counter64
_RuckusZDWLANDownTotalFrame_Object = MibTableColumn
ruckusZDWLANDownTotalFrame = _RuckusZDWLANDownTotalFrame_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 48),
    _RuckusZDWLANDownTotalFrame_Type()
)
ruckusZDWLANDownTotalFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANDownTotalFrame.setStatus("current")
_RuckusZDWLANDownTotalErrFrame_Type = Counter64
_RuckusZDWLANDownTotalErrFrame_Object = MibTableColumn
ruckusZDWLANDownTotalErrFrame = _RuckusZDWLANDownTotalErrFrame_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 49),
    _RuckusZDWLANDownTotalErrFrame_Type()
)
ruckusZDWLANDownTotalErrFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANDownTotalErrFrame.setStatus("current")
_RuckusZDWLANUpTotalFrame_Type = Counter64
_RuckusZDWLANUpTotalFrame_Object = MibTableColumn
ruckusZDWLANUpTotalFrame = _RuckusZDWLANUpTotalFrame_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 50),
    _RuckusZDWLANUpTotalFrame_Type()
)
ruckusZDWLANUpTotalFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANUpTotalFrame.setStatus("current")
_RuckusZDWLANUpDropFrame_Type = Counter64
_RuckusZDWLANUpDropFrame_Object = MibTableColumn
ruckusZDWLANUpDropFrame = _RuckusZDWLANUpDropFrame_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 51),
    _RuckusZDWLANUpDropFrame_Type()
)
ruckusZDWLANUpDropFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANUpDropFrame.setStatus("current")
_RuckusZDWLANUpRetxFrame_Type = Counter64
_RuckusZDWLANUpRetxFrame_Object = MibTableColumn
ruckusZDWLANUpRetxFrame = _RuckusZDWLANUpRetxFrame_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 52),
    _RuckusZDWLANUpRetxFrame_Type()
)
ruckusZDWLANUpRetxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANUpRetxFrame.setStatus("current")
_RuckusZDWLANNAME_Type = RuckusSSID
_RuckusZDWLANNAME_Object = MibTableColumn
ruckusZDWLANNAME = _RuckusZDWLANNAME_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 1, 1, 1, 108),
    _RuckusZDWLANNAME_Type()
)
ruckusZDWLANNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANNAME.setStatus("current")
_RuckusZDWLANAPInfo_ObjectIdentity = ObjectIdentity
ruckusZDWLANAPInfo = _RuckusZDWLANAPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2)
)
_RuckusZDWLANAPTable_Object = MibTable
ruckusZDWLANAPTable = _RuckusZDWLANAPTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruckusZDWLANAPTable.setStatus("current")
_RuckusZDWLANAPEntry_Object = MibTableRow
ruckusZDWLANAPEntry = _RuckusZDWLANAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1)
)
ruckusZDWLANAPEntry.setIndexNames(
    (0, "RUCKUS-ZD-WLAN-MIB", "ruckusZDWLANAPMacAddr"),
)
if mibBuilder.loadTexts:
    ruckusZDWLANAPEntry.setStatus("current")
_RuckusZDWLANAPMacAddr_Type = MacAddress
_RuckusZDWLANAPMacAddr_Object = MibTableColumn
ruckusZDWLANAPMacAddr = _RuckusZDWLANAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 1),
    _RuckusZDWLANAPMacAddr_Type()
)
ruckusZDWLANAPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPMacAddr.setStatus("current")
_RuckusZDWLANAPDescription_Type = DisplayString
_RuckusZDWLANAPDescription_Object = MibTableColumn
ruckusZDWLANAPDescription = _RuckusZDWLANAPDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 2),
    _RuckusZDWLANAPDescription_Type()
)
ruckusZDWLANAPDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPDescription.setStatus("current")


class _RuckusZDWLANAPStatus_Type(Integer32):
    """Custom type ruckusZDWLANAPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("approvalPending", 2),
          ("connected", 1),
          ("disconnected", 0),
          ("provisioning", 4),
          ("upgradingFirmware", 3))
    )


_RuckusZDWLANAPStatus_Type.__name__ = "Integer32"
_RuckusZDWLANAPStatus_Object = MibTableColumn
ruckusZDWLANAPStatus = _RuckusZDWLANAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 3),
    _RuckusZDWLANAPStatus_Type()
)
ruckusZDWLANAPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPStatus.setStatus("current")
_RuckusZDWLANAPModel_Type = DisplayString
_RuckusZDWLANAPModel_Object = MibTableColumn
ruckusZDWLANAPModel = _RuckusZDWLANAPModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 4),
    _RuckusZDWLANAPModel_Type()
)
ruckusZDWLANAPModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPModel.setStatus("current")
_RuckusZDWLANAPSerialNumber_Type = DisplayString
_RuckusZDWLANAPSerialNumber_Object = MibTableColumn
ruckusZDWLANAPSerialNumber = _RuckusZDWLANAPSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 5),
    _RuckusZDWLANAPSerialNumber_Type()
)
ruckusZDWLANAPSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPSerialNumber.setStatus("current")
_RuckusZDWLANAPUptime_Type = TimeTicks
_RuckusZDWLANAPUptime_Object = MibTableColumn
ruckusZDWLANAPUptime = _RuckusZDWLANAPUptime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 6),
    _RuckusZDWLANAPUptime_Type()
)
ruckusZDWLANAPUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPUptime.setStatus("current")
_RuckusZDWLANAPSWversion_Type = DisplayString
_RuckusZDWLANAPSWversion_Object = MibTableColumn
ruckusZDWLANAPSWversion = _RuckusZDWLANAPSWversion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 7),
    _RuckusZDWLANAPSWversion_Type()
)
ruckusZDWLANAPSWversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPSWversion.setStatus("current")
_RuckusZDWLANAPHWversion_Type = DisplayString
_RuckusZDWLANAPHWversion_Object = MibTableColumn
ruckusZDWLANAPHWversion = _RuckusZDWLANAPHWversion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 8),
    _RuckusZDWLANAPHWversion_Type()
)
ruckusZDWLANAPHWversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPHWversion.setStatus("current")
_RuckusZDWLANAPIPAddr_Type = IpAddress
_RuckusZDWLANAPIPAddr_Object = MibTableColumn
ruckusZDWLANAPIPAddr = _RuckusZDWLANAPIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 10),
    _RuckusZDWLANAPIPAddr_Type()
)
ruckusZDWLANAPIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIPAddr.setStatus("current")
_RuckusZDWLANAPNumRadios_Type = Unsigned32
_RuckusZDWLANAPNumRadios_Object = MibTableColumn
ruckusZDWLANAPNumRadios = _RuckusZDWLANAPNumRadios_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 13),
    _RuckusZDWLANAPNumRadios_Type()
)
ruckusZDWLANAPNumRadios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPNumRadios.setStatus("current")
_RuckusZDWLANAPNumVAP_Type = Unsigned32
_RuckusZDWLANAPNumVAP_Object = MibTableColumn
ruckusZDWLANAPNumVAP = _RuckusZDWLANAPNumVAP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 14),
    _RuckusZDWLANAPNumVAP_Type()
)
ruckusZDWLANAPNumVAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPNumVAP.setStatus("current")
_RuckusZDWLANAPNumSta_Type = Unsigned32
_RuckusZDWLANAPNumSta_Object = MibTableColumn
ruckusZDWLANAPNumSta = _RuckusZDWLANAPNumSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 15),
    _RuckusZDWLANAPNumSta_Type()
)
ruckusZDWLANAPNumSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPNumSta.setStatus("current")
_RuckusZDWLANAPNumRogues_Type = Unsigned32
_RuckusZDWLANAPNumRogues_Object = MibTableColumn
ruckusZDWLANAPNumRogues = _RuckusZDWLANAPNumRogues_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 16),
    _RuckusZDWLANAPNumRogues_Type()
)
ruckusZDWLANAPNumRogues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPNumRogues.setStatus("current")


class _RuckusZDWLANAPConnectionMode_Type(Integer32):
    """Custom type ruckusZDWLANAPConnectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("layer2", 0),
          ("layer3", 1))
    )


_RuckusZDWLANAPConnectionMode_Type.__name__ = "Integer32"
_RuckusZDWLANAPConnectionMode_Object = MibTableColumn
ruckusZDWLANAPConnectionMode = _RuckusZDWLANAPConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 17),
    _RuckusZDWLANAPConnectionMode_Type()
)
ruckusZDWLANAPConnectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPConnectionMode.setStatus("current")
_RuckusZDWLANAPMeshEnable_Type = TruthValue
_RuckusZDWLANAPMeshEnable_Object = MibTableColumn
ruckusZDWLANAPMeshEnable = _RuckusZDWLANAPMeshEnable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 18),
    _RuckusZDWLANAPMeshEnable_Type()
)
ruckusZDWLANAPMeshEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPMeshEnable.setStatus("current")
_RuckusZDWLANAPMeshHops_Type = Unsigned32
_RuckusZDWLANAPMeshHops_Object = MibTableColumn
ruckusZDWLANAPMeshHops = _RuckusZDWLANAPMeshHops_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 19),
    _RuckusZDWLANAPMeshHops_Type()
)
ruckusZDWLANAPMeshHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPMeshHops.setStatus("current")


class _RuckusZDWLANAPMeshType_Type(Integer32):
    """Custom type ruckusZDWLANAPMeshType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forming", 3),
          ("mesh", 2),
          ("root", 1),
          ("unknown", 0))
    )


_RuckusZDWLANAPMeshType_Type.__name__ = "Integer32"
_RuckusZDWLANAPMeshType_Object = MibTableColumn
ruckusZDWLANAPMeshType = _RuckusZDWLANAPMeshType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 20),
    _RuckusZDWLANAPMeshType_Type()
)
ruckusZDWLANAPMeshType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPMeshType.setStatus("current")
_RuckusZDWLANAPLANStatsRXByte_Type = Counter32
_RuckusZDWLANAPLANStatsRXByte_Object = MibTableColumn
ruckusZDWLANAPLANStatsRXByte = _RuckusZDWLANAPLANStatsRXByte_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 21),
    _RuckusZDWLANAPLANStatsRXByte_Type()
)
ruckusZDWLANAPLANStatsRXByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLANStatsRXByte.setStatus("current")
_RuckusZDWLANAPLANStatsRXPkt_Type = Counter32
_RuckusZDWLANAPLANStatsRXPkt_Object = MibTableColumn
ruckusZDWLANAPLANStatsRXPkt = _RuckusZDWLANAPLANStatsRXPkt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 22),
    _RuckusZDWLANAPLANStatsRXPkt_Type()
)
ruckusZDWLANAPLANStatsRXPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLANStatsRXPkt.setStatus("current")
_RuckusZDWLANAPLANStatsRXPktErr_Type = Counter32
_RuckusZDWLANAPLANStatsRXPktErr_Object = MibTableColumn
ruckusZDWLANAPLANStatsRXPktErr = _RuckusZDWLANAPLANStatsRXPktErr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 23),
    _RuckusZDWLANAPLANStatsRXPktErr_Type()
)
ruckusZDWLANAPLANStatsRXPktErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLANStatsRXPktErr.setStatus("current")
_RuckusZDWLANAPLANStatsRXPKTSucc_Type = Counter32
_RuckusZDWLANAPLANStatsRXPKTSucc_Object = MibTableColumn
ruckusZDWLANAPLANStatsRXPKTSucc = _RuckusZDWLANAPLANStatsRXPKTSucc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 24),
    _RuckusZDWLANAPLANStatsRXPKTSucc_Type()
)
ruckusZDWLANAPLANStatsRXPKTSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLANStatsRXPKTSucc.setStatus("current")
_RuckusZDWLANAPLANStatsTXByte_Type = Counter32
_RuckusZDWLANAPLANStatsTXByte_Object = MibTableColumn
ruckusZDWLANAPLANStatsTXByte = _RuckusZDWLANAPLANStatsTXByte_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 25),
    _RuckusZDWLANAPLANStatsTXByte_Type()
)
ruckusZDWLANAPLANStatsTXByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLANStatsTXByte.setStatus("current")
_RuckusZDWLANAPLANStatsTXPkt_Type = Counter32
_RuckusZDWLANAPLANStatsTXPkt_Object = MibTableColumn
ruckusZDWLANAPLANStatsTXPkt = _RuckusZDWLANAPLANStatsTXPkt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 26),
    _RuckusZDWLANAPLANStatsTXPkt_Type()
)
ruckusZDWLANAPLANStatsTXPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLANStatsTXPkt.setStatus("current")
_RuckusZDWLANAPMemUtil_Type = Integer32
_RuckusZDWLANAPMemUtil_Object = MibTableColumn
ruckusZDWLANAPMemUtil = _RuckusZDWLANAPMemUtil_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 27),
    _RuckusZDWLANAPMemUtil_Type()
)
ruckusZDWLANAPMemUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPMemUtil.setStatus("current")
_RuckusZDWLANAPMemTotal_Type = Unsigned32
_RuckusZDWLANAPMemTotal_Object = MibTableColumn
ruckusZDWLANAPMemTotal = _RuckusZDWLANAPMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 28),
    _RuckusZDWLANAPMemTotal_Type()
)
ruckusZDWLANAPMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPMemTotal.setStatus("current")
_RuckusZDWLANAPCPUUtil_Type = Integer32
_RuckusZDWLANAPCPUUtil_Object = MibTableColumn
ruckusZDWLANAPCPUUtil = _RuckusZDWLANAPCPUUtil_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 29),
    _RuckusZDWLANAPCPUUtil_Type()
)
ruckusZDWLANAPCPUUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPCPUUtil.setStatus("current")
_RuckusZDWLANAPFWSize_Type = Unsigned32
_RuckusZDWLANAPFWSize_Object = MibTableColumn
ruckusZDWLANAPFWSize = _RuckusZDWLANAPFWSize_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 30),
    _RuckusZDWLANAPFWSize_Type()
)
ruckusZDWLANAPFWSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPFWSize.setStatus("current")
_RuckusZDWLANAPFWAvail_Type = Unsigned32
_RuckusZDWLANAPFWAvail_Object = MibTableColumn
ruckusZDWLANAPFWAvail = _RuckusZDWLANAPFWAvail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 31),
    _RuckusZDWLANAPFWAvail_Type()
)
ruckusZDWLANAPFWAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPFWAvail.setStatus("current")
_RuckusZDWLANAPMultipleVlanCapability_Type = TruthValue
_RuckusZDWLANAPMultipleVlanCapability_Object = MibTableColumn
ruckusZDWLANAPMultipleVlanCapability = _RuckusZDWLANAPMultipleVlanCapability_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 32),
    _RuckusZDWLANAPMultipleVlanCapability_Type()
)
ruckusZDWLANAPMultipleVlanCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPMultipleVlanCapability.setStatus("current")
_RuckusZDWLANAP11bCapable_Type = TruthValue
_RuckusZDWLANAP11bCapable_Object = MibTableColumn
ruckusZDWLANAP11bCapable = _RuckusZDWLANAP11bCapable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 36),
    _RuckusZDWLANAP11bCapable_Type()
)
ruckusZDWLANAP11bCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAP11bCapable.setStatus("current")
_RuckusZDWLANAP11gCapable_Type = TruthValue
_RuckusZDWLANAP11gCapable_Object = MibTableColumn
ruckusZDWLANAP11gCapable = _RuckusZDWLANAP11gCapable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 37),
    _RuckusZDWLANAP11gCapable_Type()
)
ruckusZDWLANAP11gCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAP11gCapable.setStatus("current")


class _RuckusZDWLANAPMultiModeAccessStatus_Type(TruthValue):
    """Custom type ruckusZDWLANAPMultiModeAccessStatus based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_RuckusZDWLANAPMultiModeAccessStatus_Type.__name__ = "TruthValue"
_RuckusZDWLANAPMultiModeAccessStatus_Object = MibTableColumn
ruckusZDWLANAPMultiModeAccessStatus = _RuckusZDWLANAPMultiModeAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 38),
    _RuckusZDWLANAPMultiModeAccessStatus_Type()
)
ruckusZDWLANAPMultiModeAccessStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANAPMultiModeAccessStatus.setStatus("current")
_RuckusZDWLANAPEthStateChange_Type = Counter32
_RuckusZDWLANAPEthStateChange_Object = MibTableColumn
ruckusZDWLANAPEthStateChange = _RuckusZDWLANAPEthStateChange_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 39),
    _RuckusZDWLANAPEthStateChange_Type()
)
ruckusZDWLANAPEthStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPEthStateChange.setStatus("current")
_RuckusZDWLANAPSyncConf_Type = TruthValue
_RuckusZDWLANAPSyncConf_Object = MibTableColumn
ruckusZDWLANAPSyncConf = _RuckusZDWLANAPSyncConf_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 41),
    _RuckusZDWLANAPSyncConf_Type()
)
ruckusZDWLANAPSyncConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPSyncConf.setStatus("current")
_RuckusZDWLANAPUpgrade_Type = TruthValue
_RuckusZDWLANAPUpgrade_Object = MibTableColumn
ruckusZDWLANAPUpgrade = _RuckusZDWLANAPUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 42),
    _RuckusZDWLANAPUpgrade_Type()
)
ruckusZDWLANAPUpgrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPUpgrade.setStatus("current")
_RuckusZDWLANAPFirstJoinTime_Type = DisplayString
_RuckusZDWLANAPFirstJoinTime_Object = MibTableColumn
ruckusZDWLANAPFirstJoinTime = _RuckusZDWLANAPFirstJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 43),
    _RuckusZDWLANAPFirstJoinTime_Type()
)
ruckusZDWLANAPFirstJoinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPFirstJoinTime.setStatus("current")
_RuckusZDWLANAPLastBootTime_Type = DisplayString
_RuckusZDWLANAPLastBootTime_Object = MibTableColumn
ruckusZDWLANAPLastBootTime = _RuckusZDWLANAPLastBootTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 44),
    _RuckusZDWLANAPLastBootTime_Type()
)
ruckusZDWLANAPLastBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLastBootTime.setStatus("current")
_RuckusZDWLANAPLastUpgradeTime_Type = DisplayString
_RuckusZDWLANAPLastUpgradeTime_Object = MibTableColumn
ruckusZDWLANAPLastUpgradeTime = _RuckusZDWLANAPLastUpgradeTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 45),
    _RuckusZDWLANAPLastUpgradeTime_Type()
)
ruckusZDWLANAPLastUpgradeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLastUpgradeTime.setStatus("current")
_RuckusZDWLANAPLastConfSyncTime_Type = DisplayString
_RuckusZDWLANAPLastConfSyncTime_Object = MibTableColumn
ruckusZDWLANAPLastConfSyncTime = _RuckusZDWLANAPLastConfSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 46),
    _RuckusZDWLANAPLastConfSyncTime_Type()
)
ruckusZDWLANAPLastConfSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLastConfSyncTime.setStatus("current")
_RuckusZDWLANAPLANStatsRXPKTBcast_Type = Counter32
_RuckusZDWLANAPLANStatsRXPKTBcast_Object = MibTableColumn
ruckusZDWLANAPLANStatsRXPKTBcast = _RuckusZDWLANAPLANStatsRXPKTBcast_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 47),
    _RuckusZDWLANAPLANStatsRXPKTBcast_Type()
)
ruckusZDWLANAPLANStatsRXPKTBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLANStatsRXPKTBcast.setStatus("current")
_RuckusZDWLANAPLANStatsRXPKTMcast_Type = Counter32
_RuckusZDWLANAPLANStatsRXPKTMcast_Object = MibTableColumn
ruckusZDWLANAPLANStatsRXPKTMcast = _RuckusZDWLANAPLANStatsRXPKTMcast_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 48),
    _RuckusZDWLANAPLANStatsRXPKTMcast_Type()
)
ruckusZDWLANAPLANStatsRXPKTMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLANStatsRXPKTMcast.setStatus("current")
_RuckusZDWLANAPLANStatsRXPKTUcast_Type = Counter32
_RuckusZDWLANAPLANStatsRXPKTUcast_Object = MibTableColumn
ruckusZDWLANAPLANStatsRXPKTUcast = _RuckusZDWLANAPLANStatsRXPKTUcast_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 49),
    _RuckusZDWLANAPLANStatsRXPKTUcast_Type()
)
ruckusZDWLANAPLANStatsRXPKTUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLANStatsRXPKTUcast.setStatus("current")
_RuckusZDWLANAPLANStatsTXPKTBcast_Type = Counter32
_RuckusZDWLANAPLANStatsTXPKTBcast_Object = MibTableColumn
ruckusZDWLANAPLANStatsTXPKTBcast = _RuckusZDWLANAPLANStatsTXPKTBcast_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 50),
    _RuckusZDWLANAPLANStatsTXPKTBcast_Type()
)
ruckusZDWLANAPLANStatsTXPKTBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLANStatsTXPKTBcast.setStatus("current")
_RuckusZDWLANAPLANStatsTXPKTMcast_Type = Counter32
_RuckusZDWLANAPLANStatsTXPKTMcast_Object = MibTableColumn
ruckusZDWLANAPLANStatsTXPKTMcast = _RuckusZDWLANAPLANStatsTXPKTMcast_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 51),
    _RuckusZDWLANAPLANStatsTXPKTMcast_Type()
)
ruckusZDWLANAPLANStatsTXPKTMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLANStatsTXPKTMcast.setStatus("current")
_RuckusZDWLANAPLANStatsTXPKTUcast_Type = Counter32
_RuckusZDWLANAPLANStatsTXPKTUcast_Object = MibTableColumn
ruckusZDWLANAPLANStatsTXPKTUcast = _RuckusZDWLANAPLANStatsTXPKTUcast_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 52),
    _RuckusZDWLANAPLANStatsTXPKTUcast_Type()
)
ruckusZDWLANAPLANStatsTXPKTUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLANStatsTXPKTUcast.setStatus("current")
_RuckusZDWLANAPLANStatsDropped_Type = Counter32
_RuckusZDWLANAPLANStatsDropped_Object = MibTableColumn
ruckusZDWLANAPLANStatsDropped = _RuckusZDWLANAPLANStatsDropped_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 53),
    _RuckusZDWLANAPLANStatsDropped_Type()
)
ruckusZDWLANAPLANStatsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLANStatsDropped.setStatus("current")
_RuckusZDWLANAPMeshUpPortCntUpdown_Type = Counter32
_RuckusZDWLANAPMeshUpPortCntUpdown_Object = MibTableColumn
ruckusZDWLANAPMeshUpPortCntUpdown = _RuckusZDWLANAPMeshUpPortCntUpdown_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 54),
    _RuckusZDWLANAPMeshUpPortCntUpdown_Type()
)
ruckusZDWLANAPMeshUpPortCntUpdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPMeshUpPortCntUpdown.setStatus("current")
_RuckusZDWLANAPMeshDownPortCntUpdown_Type = Counter32
_RuckusZDWLANAPMeshDownPortCntUpdown_Object = MibTableColumn
ruckusZDWLANAPMeshDownPortCntUpdown = _RuckusZDWLANAPMeshDownPortCntUpdown_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 55),
    _RuckusZDWLANAPMeshDownPortCntUpdown_Type()
)
ruckusZDWLANAPMeshDownPortCntUpdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPMeshDownPortCntUpdown.setStatus("current")
_RuckusZDWLANAPTxFrameDropped_Type = Counter32
_RuckusZDWLANAPTxFrameDropped_Object = MibTableColumn
ruckusZDWLANAPTxFrameDropped = _RuckusZDWLANAPTxFrameDropped_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 57),
    _RuckusZDWLANAPTxFrameDropped_Type()
)
ruckusZDWLANAPTxFrameDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPTxFrameDropped.setStatus("current")
_RuckusZDWLANAPTxFrameError_Type = Counter32
_RuckusZDWLANAPTxFrameError_Object = MibTableColumn
ruckusZDWLANAPTxFrameError = _RuckusZDWLANAPTxFrameError_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 58),
    _RuckusZDWLANAPTxFrameError_Type()
)
ruckusZDWLANAPTxFrameError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPTxFrameError.setStatus("current")


class _RuckusZDWLANAPCoverageTech_Type(Integer32):
    """Custom type ruckusZDWLANAPCoverageTech based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("indoor", 1),
          ("indoor-distribute", 2),
          ("outdoor", 3))
    )


_RuckusZDWLANAPCoverageTech_Type.__name__ = "Integer32"
_RuckusZDWLANAPCoverageTech_Object = MibTableColumn
ruckusZDWLANAPCoverageTech = _RuckusZDWLANAPCoverageTech_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 59),
    _RuckusZDWLANAPCoverageTech_Type()
)
ruckusZDWLANAPCoverageTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPCoverageTech.setStatus("current")
_RuckusZDWLANAPStaTxBytes_Type = Counter32
_RuckusZDWLANAPStaTxBytes_Object = MibTableColumn
ruckusZDWLANAPStaTxBytes = _RuckusZDWLANAPStaTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 61),
    _RuckusZDWLANAPStaTxBytes_Type()
)
ruckusZDWLANAPStaTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPStaTxBytes.setStatus("current")
_RuckusZDWLANAPStaRxBytes_Type = Counter32
_RuckusZDWLANAPStaRxBytes_Object = MibTableColumn
ruckusZDWLANAPStaRxBytes = _RuckusZDWLANAPStaRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 62),
    _RuckusZDWLANAPStaRxBytes_Type()
)
ruckusZDWLANAPStaRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPStaRxBytes.setStatus("current")
_RuckusZDWLANAPNetmask_Type = IpAddress
_RuckusZDWLANAPNetmask_Object = MibTableColumn
ruckusZDWLANAPNetmask = _RuckusZDWLANAPNetmask_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 100),
    _RuckusZDWLANAPNetmask_Type()
)
ruckusZDWLANAPNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPNetmask.setStatus("current")
_RuckusZDWLANAPGateway_Type = IpAddress
_RuckusZDWLANAPGateway_Object = MibTableColumn
ruckusZDWLANAPGateway = _RuckusZDWLANAPGateway_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 101),
    _RuckusZDWLANAPGateway_Type()
)
ruckusZDWLANAPGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPGateway.setStatus("current")
_RuckusZDWLANAPDNS1_Type = IpAddress
_RuckusZDWLANAPDNS1_Object = MibTableColumn
ruckusZDWLANAPDNS1 = _RuckusZDWLANAPDNS1_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 105),
    _RuckusZDWLANAPDNS1_Type()
)
ruckusZDWLANAPDNS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPDNS1.setStatus("current")
_RuckusZDWLANAPDNS2_Type = IpAddress
_RuckusZDWLANAPDNS2_Object = MibTableColumn
ruckusZDWLANAPDNS2 = _RuckusZDWLANAPDNS2_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 106),
    _RuckusZDWLANAPDNS2_Type()
)
ruckusZDWLANAPDNS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPDNS2.setStatus("current")
_RuckusZDWLANAPTotalUser_Type = Unsigned32
_RuckusZDWLANAPTotalUser_Object = MibTableColumn
ruckusZDWLANAPTotalUser = _RuckusZDWLANAPTotalUser_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 110),
    _RuckusZDWLANAPTotalUser_Type()
)
ruckusZDWLANAPTotalUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPTotalUser.setStatus("current")
_RuckusZDWLANAPLANStatsRXByteRate_Type = Counter32
_RuckusZDWLANAPLANStatsRXByteRate_Object = MibTableColumn
ruckusZDWLANAPLANStatsRXByteRate = _RuckusZDWLANAPLANStatsRXByteRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 111),
    _RuckusZDWLANAPLANStatsRXByteRate_Type()
)
ruckusZDWLANAPLANStatsRXByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLANStatsRXByteRate.setStatus("current")
_RuckusZDWLANAPLANStatsTXByteRate_Type = Counter32
_RuckusZDWLANAPLANStatsTXByteRate_Object = MibTableColumn
ruckusZDWLANAPLANStatsTXByteRate = _RuckusZDWLANAPLANStatsTXByteRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 1, 1, 112),
    _RuckusZDWLANAPLANStatsTXByteRate_Type()
)
ruckusZDWLANAPLANStatsTXByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPLANStatsTXByteRate.setStatus("current")
_RuckusZDWLANAPRadioStatsTable_Object = MibTable
ruckusZDWLANAPRadioStatsTable = _RuckusZDWLANAPRadioStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsTable.setStatus("current")
_RuckusZDWLANAPRadioStatsEntry_Object = MibTableRow
ruckusZDWLANAPRadioStatsEntry = _RuckusZDWLANAPRadioStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1)
)
ruckusZDWLANAPRadioStatsEntry.setIndexNames(
    (0, "RUCKUS-ZD-WLAN-MIB", "ruckusZDWLANAPRadioStatsAPMacAddr"),
    (0, "RUCKUS-ZD-WLAN-MIB", "ruckusZDWLANAPRadioStatsRadioIndex"),
)
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsEntry.setStatus("current")
_RuckusZDWLANAPRadioStatsAPMacAddr_Type = MacAddress
_RuckusZDWLANAPRadioStatsAPMacAddr_Object = MibTableColumn
ruckusZDWLANAPRadioStatsAPMacAddr = _RuckusZDWLANAPRadioStatsAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 1),
    _RuckusZDWLANAPRadioStatsAPMacAddr_Type()
)
ruckusZDWLANAPRadioStatsAPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsAPMacAddr.setStatus("current")
_RuckusZDWLANAPRadioStatsRadioIndex_Type = Unsigned32
_RuckusZDWLANAPRadioStatsRadioIndex_Object = MibTableColumn
ruckusZDWLANAPRadioStatsRadioIndex = _RuckusZDWLANAPRadioStatsRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 2),
    _RuckusZDWLANAPRadioStatsRadioIndex_Type()
)
ruckusZDWLANAPRadioStatsRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsRadioIndex.setStatus("current")


class _RuckusZDWLANAPRadioStatsRadioType_Type(Integer32):
    """Custom type ruckusZDWLANAPRadioStatsRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("radio11a", 1),
          ("radio11bg", 0),
          ("radio11na", 3),
          ("radio11ng", 2))
    )


_RuckusZDWLANAPRadioStatsRadioType_Type.__name__ = "Integer32"
_RuckusZDWLANAPRadioStatsRadioType_Object = MibTableColumn
ruckusZDWLANAPRadioStatsRadioType = _RuckusZDWLANAPRadioStatsRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 3),
    _RuckusZDWLANAPRadioStatsRadioType_Type()
)
ruckusZDWLANAPRadioStatsRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsRadioType.setStatus("current")
_RuckusZDWLANAPRadioStatsChannel_Type = Unsigned32
_RuckusZDWLANAPRadioStatsChannel_Object = MibTableColumn
ruckusZDWLANAPRadioStatsChannel = _RuckusZDWLANAPRadioStatsChannel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 4),
    _RuckusZDWLANAPRadioStatsChannel_Type()
)
ruckusZDWLANAPRadioStatsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsChannel.setStatus("current")


class _RuckusZDWLANAPRadioStatsTxPower_Type(Integer32):
    """Custom type ruckusZDWLANAPRadioStatsTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eighth", 3),
          ("full", 0),
          ("half", 1),
          ("quarter", 2))
    )


_RuckusZDWLANAPRadioStatsTxPower_Type.__name__ = "Integer32"
_RuckusZDWLANAPRadioStatsTxPower_Object = MibTableColumn
ruckusZDWLANAPRadioStatsTxPower = _RuckusZDWLANAPRadioStatsTxPower_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 5),
    _RuckusZDWLANAPRadioStatsTxPower_Type()
)
ruckusZDWLANAPRadioStatsTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsTxPower.setStatus("current")
_RuckusZDWLANAPRadioStatsMeshEnable_Type = TruthValue
_RuckusZDWLANAPRadioStatsMeshEnable_Object = MibTableColumn
ruckusZDWLANAPRadioStatsMeshEnable = _RuckusZDWLANAPRadioStatsMeshEnable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 6),
    _RuckusZDWLANAPRadioStatsMeshEnable_Type()
)
ruckusZDWLANAPRadioStatsMeshEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsMeshEnable.setStatus("current")
_RuckusZDWLANAPRadioStatsNumVAP_Type = Unsigned32
_RuckusZDWLANAPRadioStatsNumVAP_Object = MibTableColumn
ruckusZDWLANAPRadioStatsNumVAP = _RuckusZDWLANAPRadioStatsNumVAP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 7),
    _RuckusZDWLANAPRadioStatsNumVAP_Type()
)
ruckusZDWLANAPRadioStatsNumVAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsNumVAP.setStatus("current")
_RuckusZDWLANAPRadioStatsNumSta_Type = Unsigned32
_RuckusZDWLANAPRadioStatsNumSta_Object = MibTableColumn
ruckusZDWLANAPRadioStatsNumSta = _RuckusZDWLANAPRadioStatsNumSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 8),
    _RuckusZDWLANAPRadioStatsNumSta_Type()
)
ruckusZDWLANAPRadioStatsNumSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsNumSta.setStatus("current")
_RuckusZDWLANAPRadioStatsAvgStaRSSI_Type = Integer32
_RuckusZDWLANAPRadioStatsAvgStaRSSI_Object = MibTableColumn
ruckusZDWLANAPRadioStatsAvgStaRSSI = _RuckusZDWLANAPRadioStatsAvgStaRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 9),
    _RuckusZDWLANAPRadioStatsAvgStaRSSI_Type()
)
ruckusZDWLANAPRadioStatsAvgStaRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsAvgStaRSSI.setStatus("current")
_RuckusZDWLANAPRadioStatsRxPkts_Type = Counter64
_RuckusZDWLANAPRadioStatsRxPkts_Object = MibTableColumn
ruckusZDWLANAPRadioStatsRxPkts = _RuckusZDWLANAPRadioStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 10),
    _RuckusZDWLANAPRadioStatsRxPkts_Type()
)
ruckusZDWLANAPRadioStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsRxPkts.setStatus("current")
_RuckusZDWLANAPRadioStatsRxBytes_Type = Counter64
_RuckusZDWLANAPRadioStatsRxBytes_Object = MibTableColumn
ruckusZDWLANAPRadioStatsRxBytes = _RuckusZDWLANAPRadioStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 11),
    _RuckusZDWLANAPRadioStatsRxBytes_Type()
)
ruckusZDWLANAPRadioStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsRxBytes.setStatus("current")
_RuckusZDWLANAPRadioStatsRxMulticast_Type = Counter64
_RuckusZDWLANAPRadioStatsRxMulticast_Object = MibTableColumn
ruckusZDWLANAPRadioStatsRxMulticast = _RuckusZDWLANAPRadioStatsRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 12),
    _RuckusZDWLANAPRadioStatsRxMulticast_Type()
)
ruckusZDWLANAPRadioStatsRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsRxMulticast.setStatus("current")
_RuckusZDWLANAPRadioStatsTxPkts_Type = Counter64
_RuckusZDWLANAPRadioStatsTxPkts_Object = MibTableColumn
ruckusZDWLANAPRadioStatsTxPkts = _RuckusZDWLANAPRadioStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 13),
    _RuckusZDWLANAPRadioStatsTxPkts_Type()
)
ruckusZDWLANAPRadioStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsTxPkts.setStatus("current")
_RuckusZDWLANAPRadioStatsTxBytes_Type = Counter64
_RuckusZDWLANAPRadioStatsTxBytes_Object = MibTableColumn
ruckusZDWLANAPRadioStatsTxBytes = _RuckusZDWLANAPRadioStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 14),
    _RuckusZDWLANAPRadioStatsTxBytes_Type()
)
ruckusZDWLANAPRadioStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsTxBytes.setStatus("current")
_RuckusZDWLANAPRadioStatsTxMulticast_Type = Counter64
_RuckusZDWLANAPRadioStatsTxMulticast_Object = MibTableColumn
ruckusZDWLANAPRadioStatsTxMulticast = _RuckusZDWLANAPRadioStatsTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 15),
    _RuckusZDWLANAPRadioStatsTxMulticast_Type()
)
ruckusZDWLANAPRadioStatsTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsTxMulticast.setStatus("current")
_RuckusZDWLANAPRadioStatsTxFail_Type = Counter64
_RuckusZDWLANAPRadioStatsTxFail_Object = MibTableColumn
ruckusZDWLANAPRadioStatsTxFail = _RuckusZDWLANAPRadioStatsTxFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 16),
    _RuckusZDWLANAPRadioStatsTxFail_Type()
)
ruckusZDWLANAPRadioStatsTxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsTxFail.setStatus("current")
_RuckusZDWLANAPRadioStatsTxRetries_Type = Counter64
_RuckusZDWLANAPRadioStatsTxRetries_Object = MibTableColumn
ruckusZDWLANAPRadioStatsTxRetries = _RuckusZDWLANAPRadioStatsTxRetries_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 17),
    _RuckusZDWLANAPRadioStatsTxRetries_Type()
)
ruckusZDWLANAPRadioStatsTxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsTxRetries.setStatus("current")
_RuckusZDWLANAPRadioStatsPowerMgmt_Type = TruthValue
_RuckusZDWLANAPRadioStatsPowerMgmt_Object = MibTableColumn
ruckusZDWLANAPRadioStatsPowerMgmt = _RuckusZDWLANAPRadioStatsPowerMgmt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 18),
    _RuckusZDWLANAPRadioStatsPowerMgmt_Type()
)
ruckusZDWLANAPRadioStatsPowerMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsPowerMgmt.setStatus("current")
_RuckusZDWLANAPRadioStatsMaxSta_Type = Unsigned32
_RuckusZDWLANAPRadioStatsMaxSta_Object = MibTableColumn
ruckusZDWLANAPRadioStatsMaxSta = _RuckusZDWLANAPRadioStatsMaxSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 19),
    _RuckusZDWLANAPRadioStatsMaxSta_Type()
)
ruckusZDWLANAPRadioStatsMaxSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsMaxSta.setStatus("current")
_RuckusZDWLANAPRadioStatsFrameErrorRate_Type = Unsigned32
_RuckusZDWLANAPRadioStatsFrameErrorRate_Object = MibTableColumn
ruckusZDWLANAPRadioStatsFrameErrorRate = _RuckusZDWLANAPRadioStatsFrameErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 20),
    _RuckusZDWLANAPRadioStatsFrameErrorRate_Type()
)
ruckusZDWLANAPRadioStatsFrameErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsFrameErrorRate.setStatus("current")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsFrameErrorRate.setUnits("1/10000")
_RuckusZDWLANAPRadioStatsFrameRetryRate_Type = Unsigned32
_RuckusZDWLANAPRadioStatsFrameRetryRate_Object = MibTableColumn
ruckusZDWLANAPRadioStatsFrameRetryRate = _RuckusZDWLANAPRadioStatsFrameRetryRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 21),
    _RuckusZDWLANAPRadioStatsFrameRetryRate_Type()
)
ruckusZDWLANAPRadioStatsFrameRetryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsFrameRetryRate.setStatus("current")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsFrameRetryRate.setUnits("1/10000")
_RuckusZDWLANAPRadioStatsMonitoredTime_Type = TimeTicks
_RuckusZDWLANAPRadioStatsMonitoredTime_Object = MibTableColumn
ruckusZDWLANAPRadioStatsMonitoredTime = _RuckusZDWLANAPRadioStatsMonitoredTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 22),
    _RuckusZDWLANAPRadioStatsMonitoredTime_Type()
)
ruckusZDWLANAPRadioStatsMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsMonitoredTime.setStatus("current")
_RuckusZDWLANAPRadioStatsTotalAssocTime_Type = Counter64
_RuckusZDWLANAPRadioStatsTotalAssocTime_Object = MibTableColumn
ruckusZDWLANAPRadioStatsTotalAssocTime = _RuckusZDWLANAPRadioStatsTotalAssocTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 24),
    _RuckusZDWLANAPRadioStatsTotalAssocTime_Type()
)
ruckusZDWLANAPRadioStatsTotalAssocTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsTotalAssocTime.setStatus("current")
_RuckusZDWLANAPRadioStatsAuthReq_Type = Counter64
_RuckusZDWLANAPRadioStatsAuthReq_Object = MibTableColumn
ruckusZDWLANAPRadioStatsAuthReq = _RuckusZDWLANAPRadioStatsAuthReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 25),
    _RuckusZDWLANAPRadioStatsAuthReq_Type()
)
ruckusZDWLANAPRadioStatsAuthReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsAuthReq.setStatus("current")
_RuckusZDWLANAPRadioStatsAuthResp_Type = Counter64
_RuckusZDWLANAPRadioStatsAuthResp_Object = MibTableColumn
ruckusZDWLANAPRadioStatsAuthResp = _RuckusZDWLANAPRadioStatsAuthResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 26),
    _RuckusZDWLANAPRadioStatsAuthResp_Type()
)
ruckusZDWLANAPRadioStatsAuthResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsAuthResp.setStatus("current")
_RuckusZDWLANAPRadioStatsAuthSuccess_Type = Counter64
_RuckusZDWLANAPRadioStatsAuthSuccess_Object = MibTableColumn
ruckusZDWLANAPRadioStatsAuthSuccess = _RuckusZDWLANAPRadioStatsAuthSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 27),
    _RuckusZDWLANAPRadioStatsAuthSuccess_Type()
)
ruckusZDWLANAPRadioStatsAuthSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsAuthSuccess.setStatus("current")
_RuckusZDWLANAPRadioStatsAuthFail_Type = Counter64
_RuckusZDWLANAPRadioStatsAuthFail_Object = MibTableColumn
ruckusZDWLANAPRadioStatsAuthFail = _RuckusZDWLANAPRadioStatsAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 28),
    _RuckusZDWLANAPRadioStatsAuthFail_Type()
)
ruckusZDWLANAPRadioStatsAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsAuthFail.setStatus("current")
_RuckusZDWLANAPRadioStatsAssocReq_Type = Counter64
_RuckusZDWLANAPRadioStatsAssocReq_Object = MibTableColumn
ruckusZDWLANAPRadioStatsAssocReq = _RuckusZDWLANAPRadioStatsAssocReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 29),
    _RuckusZDWLANAPRadioStatsAssocReq_Type()
)
ruckusZDWLANAPRadioStatsAssocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsAssocReq.setStatus("current")
_RuckusZDWLANAPRadioStatsAssocResp_Type = Counter64
_RuckusZDWLANAPRadioStatsAssocResp_Object = MibTableColumn
ruckusZDWLANAPRadioStatsAssocResp = _RuckusZDWLANAPRadioStatsAssocResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 30),
    _RuckusZDWLANAPRadioStatsAssocResp_Type()
)
ruckusZDWLANAPRadioStatsAssocResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsAssocResp.setStatus("current")
_RuckusZDWLANAPRadioStatsReassocReq_Type = Counter64
_RuckusZDWLANAPRadioStatsReassocReq_Object = MibTableColumn
ruckusZDWLANAPRadioStatsReassocReq = _RuckusZDWLANAPRadioStatsReassocReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 31),
    _RuckusZDWLANAPRadioStatsReassocReq_Type()
)
ruckusZDWLANAPRadioStatsReassocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsReassocReq.setStatus("current")
_RuckusZDWLANAPRadioStatsReassocResp_Type = Counter64
_RuckusZDWLANAPRadioStatsReassocResp_Object = MibTableColumn
ruckusZDWLANAPRadioStatsReassocResp = _RuckusZDWLANAPRadioStatsReassocResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 32),
    _RuckusZDWLANAPRadioStatsReassocResp_Type()
)
ruckusZDWLANAPRadioStatsReassocResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsReassocResp.setStatus("current")
_RuckusZDWLANAPRadioStatsAssocSuccess_Type = Counter64
_RuckusZDWLANAPRadioStatsAssocSuccess_Object = MibTableColumn
ruckusZDWLANAPRadioStatsAssocSuccess = _RuckusZDWLANAPRadioStatsAssocSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 33),
    _RuckusZDWLANAPRadioStatsAssocSuccess_Type()
)
ruckusZDWLANAPRadioStatsAssocSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsAssocSuccess.setStatus("current")
_RuckusZDWLANAPRadioStatsAssocFail_Type = Counter64
_RuckusZDWLANAPRadioStatsAssocFail_Object = MibTableColumn
ruckusZDWLANAPRadioStatsAssocFail = _RuckusZDWLANAPRadioStatsAssocFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 34),
    _RuckusZDWLANAPRadioStatsAssocFail_Type()
)
ruckusZDWLANAPRadioStatsAssocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsAssocFail.setStatus("current")
_RuckusZDWLANAPRadioStatsAssocDenied_Type = Counter64
_RuckusZDWLANAPRadioStatsAssocDenied_Object = MibTableColumn
ruckusZDWLANAPRadioStatsAssocDenied = _RuckusZDWLANAPRadioStatsAssocDenied_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 35),
    _RuckusZDWLANAPRadioStatsAssocDenied_Type()
)
ruckusZDWLANAPRadioStatsAssocDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsAssocDenied.setStatus("current")
_RuckusZDWLANAPRadioStatsDiassocAbnormal_Type = Counter64
_RuckusZDWLANAPRadioStatsDiassocAbnormal_Object = MibTableColumn
ruckusZDWLANAPRadioStatsDiassocAbnormal = _RuckusZDWLANAPRadioStatsDiassocAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 36),
    _RuckusZDWLANAPRadioStatsDiassocAbnormal_Type()
)
ruckusZDWLANAPRadioStatsDiassocAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsDiassocAbnormal.setStatus("current")
_RuckusZDWLANAPRadioStatsDiassocCapacity_Type = Counter64
_RuckusZDWLANAPRadioStatsDiassocCapacity_Object = MibTableColumn
ruckusZDWLANAPRadioStatsDiassocCapacity = _RuckusZDWLANAPRadioStatsDiassocCapacity_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 37),
    _RuckusZDWLANAPRadioStatsDiassocCapacity_Type()
)
ruckusZDWLANAPRadioStatsDiassocCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsDiassocCapacity.setStatus("current")
_RuckusZDWLANAPRadioStatsDiassocLeave_Type = Counter64
_RuckusZDWLANAPRadioStatsDiassocLeave_Object = MibTableColumn
ruckusZDWLANAPRadioStatsDiassocLeave = _RuckusZDWLANAPRadioStatsDiassocLeave_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 38),
    _RuckusZDWLANAPRadioStatsDiassocLeave_Type()
)
ruckusZDWLANAPRadioStatsDiassocLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsDiassocLeave.setStatus("current")
_RuckusZDWLANAPRadioStatsDiassocMisc_Type = Counter64
_RuckusZDWLANAPRadioStatsDiassocMisc_Object = MibTableColumn
ruckusZDWLANAPRadioStatsDiassocMisc = _RuckusZDWLANAPRadioStatsDiassocMisc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 39),
    _RuckusZDWLANAPRadioStatsDiassocMisc_Type()
)
ruckusZDWLANAPRadioStatsDiassocMisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsDiassocMisc.setStatus("current")
_RuckusZDWLANAPRadioStatsResourceUtil_Type = Unsigned32
_RuckusZDWLANAPRadioStatsResourceUtil_Object = MibTableColumn
ruckusZDWLANAPRadioStatsResourceUtil = _RuckusZDWLANAPRadioStatsResourceUtil_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 40),
    _RuckusZDWLANAPRadioStatsResourceUtil_Type()
)
ruckusZDWLANAPRadioStatsResourceUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsResourceUtil.setStatus("current")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsResourceUtil.setUnits("percentage")
_RuckusZDWLANAPRadioStatsRxSignalFrm_Type = Counter64
_RuckusZDWLANAPRadioStatsRxSignalFrm_Object = MibTableColumn
ruckusZDWLANAPRadioStatsRxSignalFrm = _RuckusZDWLANAPRadioStatsRxSignalFrm_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 41),
    _RuckusZDWLANAPRadioStatsRxSignalFrm_Type()
)
ruckusZDWLANAPRadioStatsRxSignalFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsRxSignalFrm.setStatus("current")
_RuckusZDWLANAPRadioStatsTxSignalFrm_Type = Counter64
_RuckusZDWLANAPRadioStatsTxSignalFrm_Object = MibTableColumn
ruckusZDWLANAPRadioStatsTxSignalFrm = _RuckusZDWLANAPRadioStatsTxSignalFrm_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 42),
    _RuckusZDWLANAPRadioStatsTxSignalFrm_Type()
)
ruckusZDWLANAPRadioStatsTxSignalFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsTxSignalFrm.setStatus("current")
_RuckusZDWLANAPRadioStatsTotalSignalFrm_Type = Counter64
_RuckusZDWLANAPRadioStatsTotalSignalFrm_Object = MibTableColumn
ruckusZDWLANAPRadioStatsTotalSignalFrm = _RuckusZDWLANAPRadioStatsTotalSignalFrm_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 43),
    _RuckusZDWLANAPRadioStatsTotalSignalFrm_Type()
)
ruckusZDWLANAPRadioStatsTotalSignalFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsTotalSignalFrm.setStatus("current")
_RuckusZDWLANAPRadioStatsAntennaGain_Type = Unsigned32
_RuckusZDWLANAPRadioStatsAntennaGain_Object = MibTableColumn
ruckusZDWLANAPRadioStatsAntennaGain = _RuckusZDWLANAPRadioStatsAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 44),
    _RuckusZDWLANAPRadioStatsAntennaGain_Type()
)
ruckusZDWLANAPRadioStatsAntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsAntennaGain.setStatus("current")
_RuckusZDWLANAPRadioStatsBeaconPeriod_Type = Unsigned32
_RuckusZDWLANAPRadioStatsBeaconPeriod_Object = MibTableColumn
ruckusZDWLANAPRadioStatsBeaconPeriod = _RuckusZDWLANAPRadioStatsBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 45),
    _RuckusZDWLANAPRadioStatsBeaconPeriod_Type()
)
ruckusZDWLANAPRadioStatsBeaconPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsBeaconPeriod.setStatus("current")
_RuckusZDWLANAPRadioStatsRTSThreshold_Type = Unsigned32
_RuckusZDWLANAPRadioStatsRTSThreshold_Object = MibTableColumn
ruckusZDWLANAPRadioStatsRTSThreshold = _RuckusZDWLANAPRadioStatsRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 46),
    _RuckusZDWLANAPRadioStatsRTSThreshold_Type()
)
ruckusZDWLANAPRadioStatsRTSThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsRTSThreshold.setStatus("current")
_RuckusZDWLANAPRadioStatsFragThreshold_Type = Unsigned32
_RuckusZDWLANAPRadioStatsFragThreshold_Object = MibTableColumn
ruckusZDWLANAPRadioStatsFragThreshold = _RuckusZDWLANAPRadioStatsFragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 2, 1, 47),
    _RuckusZDWLANAPRadioStatsFragThreshold_Type()
)
ruckusZDWLANAPRadioStatsFragThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPRadioStatsFragThreshold.setStatus("current")
_RuckusZDWLANVapTable_Object = MibTable
ruckusZDWLANVapTable = _RuckusZDWLANVapTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ruckusZDWLANVapTable.setStatus("current")
_RuckusZDWLANVapEntry_Object = MibTableRow
ruckusZDWLANVapEntry = _RuckusZDWLANVapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 3, 1)
)
ruckusZDWLANVapEntry.setIndexNames(
    (0, "RUCKUS-ZD-WLAN-MIB", "ruckusZDWLANVapBSSID"),
)
if mibBuilder.loadTexts:
    ruckusZDWLANVapEntry.setStatus("current")
_RuckusZDWLANVapBSSID_Type = MacAddress
_RuckusZDWLANVapBSSID_Object = MibTableColumn
ruckusZDWLANVapBSSID = _RuckusZDWLANVapBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 3, 1, 1),
    _RuckusZDWLANVapBSSID_Type()
)
ruckusZDWLANVapBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANVapBSSID.setStatus("current")
_RuckusZDWLANVapPAPAddr_Type = MacAddress
_RuckusZDWLANVapPAPAddr_Object = MibTableColumn
ruckusZDWLANVapPAPAddr = _RuckusZDWLANVapPAPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 3, 1, 2),
    _RuckusZDWLANVapPAPAddr_Type()
)
ruckusZDWLANVapPAPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANVapPAPAddr.setStatus("current")
_RuckusZDWLANVapSSID_Type = RuckusSSID
_RuckusZDWLANVapSSID_Object = MibTableColumn
ruckusZDWLANVapSSID = _RuckusZDWLANVapSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 3, 1, 3),
    _RuckusZDWLANVapSSID_Type()
)
ruckusZDWLANVapSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANVapSSID.setStatus("current")
_RuckusZDWLANVapLanRxBytes_Type = Counter64
_RuckusZDWLANVapLanRxBytes_Object = MibTableColumn
ruckusZDWLANVapLanRxBytes = _RuckusZDWLANVapLanRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 3, 1, 6),
    _RuckusZDWLANVapLanRxBytes_Type()
)
ruckusZDWLANVapLanRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANVapLanRxBytes.setStatus("current")
_RuckusZDWLANVapLanTxBytes_Type = Counter64
_RuckusZDWLANVapLanTxBytes_Object = MibTableColumn
ruckusZDWLANVapLanTxBytes = _RuckusZDWLANVapLanTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 3, 1, 7),
    _RuckusZDWLANVapLanTxBytes_Type()
)
ruckusZDWLANVapLanTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANVapLanTxBytes.setStatus("current")
_RuckusZDWLANVapWlanRxBytes_Type = Counter64
_RuckusZDWLANVapWlanRxBytes_Object = MibTableColumn
ruckusZDWLANVapWlanRxBytes = _RuckusZDWLANVapWlanRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 3, 1, 8),
    _RuckusZDWLANVapWlanRxBytes_Type()
)
ruckusZDWLANVapWlanRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANVapWlanRxBytes.setStatus("current")
_RuckusZDWLANVapWlanTxBytes_Type = Counter64
_RuckusZDWLANVapWlanTxBytes_Object = MibTableColumn
ruckusZDWLANVapWlanTxBytes = _RuckusZDWLANVapWlanTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 3, 1, 9),
    _RuckusZDWLANVapWlanTxBytes_Type()
)
ruckusZDWLANVapWlanTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANVapWlanTxBytes.setStatus("current")
_RuckusZDWLANVapWlanRxErrorPkt_Type = Counter64
_RuckusZDWLANVapWlanRxErrorPkt_Object = MibTableColumn
ruckusZDWLANVapWlanRxErrorPkt = _RuckusZDWLANVapWlanRxErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 3, 1, 11),
    _RuckusZDWLANVapWlanRxErrorPkt_Type()
)
ruckusZDWLANVapWlanRxErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANVapWlanRxErrorPkt.setStatus("current")
_RuckusZDWLANVapWlanRxUnicastPkt_Type = Counter64
_RuckusZDWLANVapWlanRxUnicastPkt_Object = MibTableColumn
ruckusZDWLANVapWlanRxUnicastPkt = _RuckusZDWLANVapWlanRxUnicastPkt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 3, 1, 12),
    _RuckusZDWLANVapWlanRxUnicastPkt_Type()
)
ruckusZDWLANVapWlanRxUnicastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANVapWlanRxUnicastPkt.setStatus("current")
_RuckusZDWLANVapWlanTxUnicastPkt_Type = Counter64
_RuckusZDWLANVapWlanTxUnicastPkt_Object = MibTableColumn
ruckusZDWLANVapWlanTxUnicastPkt = _RuckusZDWLANVapWlanTxUnicastPkt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 3, 1, 13),
    _RuckusZDWLANVapWlanTxUnicastPkt_Type()
)
ruckusZDWLANVapWlanTxUnicastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANVapWlanTxUnicastPkt.setStatus("current")
_RuckusZDWLANVapWlanRxPkt_Type = Counter64
_RuckusZDWLANVapWlanRxPkt_Object = MibTableColumn
ruckusZDWLANVapWlanRxPkt = _RuckusZDWLANVapWlanRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 3, 1, 14),
    _RuckusZDWLANVapWlanRxPkt_Type()
)
ruckusZDWLANVapWlanRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANVapWlanRxPkt.setStatus("current")
_RuckusZDWLANVapWlanRxDropPkt_Type = Counter64
_RuckusZDWLANVapWlanRxDropPkt_Object = MibTableColumn
ruckusZDWLANVapWlanRxDropPkt = _RuckusZDWLANVapWlanRxDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 3, 1, 15),
    _RuckusZDWLANVapWlanRxDropPkt_Type()
)
ruckusZDWLANVapWlanRxDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANVapWlanRxDropPkt.setStatus("current")
_RuckusZDWLANVapWlanTxErrPkt_Type = Counter64
_RuckusZDWLANVapWlanTxErrPkt_Object = MibTableColumn
ruckusZDWLANVapWlanTxErrPkt = _RuckusZDWLANVapWlanTxErrPkt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 3, 1, 16),
    _RuckusZDWLANVapWlanTxErrPkt_Type()
)
ruckusZDWLANVapWlanTxErrPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANVapWlanTxErrPkt.setStatus("current")
_RuckusZDWLANVapWlanTxPkt_Type = Counter64
_RuckusZDWLANVapWlanTxPkt_Object = MibTableColumn
ruckusZDWLANVapWlanTxPkt = _RuckusZDWLANVapWlanTxPkt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 3, 1, 17),
    _RuckusZDWLANVapWlanTxPkt_Type()
)
ruckusZDWLANVapWlanTxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANVapWlanTxPkt.setStatus("current")
_RuckusZDWLANVapWlanTxDropPkt_Type = Counter64
_RuckusZDWLANVapWlanTxDropPkt_Object = MibTableColumn
ruckusZDWLANVapWlanTxDropPkt = _RuckusZDWLANVapWlanTxDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 3, 1, 18),
    _RuckusZDWLANVapWlanTxDropPkt_Type()
)
ruckusZDWLANVapWlanTxDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANVapWlanTxDropPkt.setStatus("current")
_RuckusZDWLANIfTable_Object = MibTable
ruckusZDWLANIfTable = _RuckusZDWLANIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ruckusZDWLANIfTable.setStatus("current")
_RuckusZDWLANIfEntry_Object = MibTableRow
ruckusZDWLANIfEntry = _RuckusZDWLANIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1)
)
ruckusZDWLANIfEntry.setIndexNames(
    (0, "RUCKUS-ZD-WLAN-MIB", "ruckusZDWLANAPMac"),
    (0, "RUCKUS-ZD-WLAN-MIB", "ruckusZDWLANAPIfIndex"),
)
if mibBuilder.loadTexts:
    ruckusZDWLANIfEntry.setStatus("current")
_RuckusZDWLANAPMac_Type = MacAddress
_RuckusZDWLANAPMac_Object = MibTableColumn
ruckusZDWLANAPMac = _RuckusZDWLANAPMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 1),
    _RuckusZDWLANAPMac_Type()
)
ruckusZDWLANAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPMac.setStatus("current")
_RuckusZDWLANAPIfIndex_Type = InterfaceIndex
_RuckusZDWLANAPIfIndex_Object = MibTableColumn
ruckusZDWLANAPIfIndex = _RuckusZDWLANAPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 2),
    _RuckusZDWLANAPIfIndex_Type()
)
ruckusZDWLANAPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfIndex.setStatus("current")
_RuckusZDWLANAPIfDescr_Type = DisplayString
_RuckusZDWLANAPIfDescr_Object = MibTableColumn
ruckusZDWLANAPIfDescr = _RuckusZDWLANAPIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 3),
    _RuckusZDWLANAPIfDescr_Type()
)
ruckusZDWLANAPIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfDescr.setStatus("current")
_RuckusZDWLANAPIfType_Type = IANAifType
_RuckusZDWLANAPIfType_Object = MibTableColumn
ruckusZDWLANAPIfType = _RuckusZDWLANAPIfType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 4),
    _RuckusZDWLANAPIfType_Type()
)
ruckusZDWLANAPIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfType.setStatus("current")
_RuckusZDWLANAPIfMtu_Type = Integer32
_RuckusZDWLANAPIfMtu_Object = MibTableColumn
ruckusZDWLANAPIfMtu = _RuckusZDWLANAPIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 5),
    _RuckusZDWLANAPIfMtu_Type()
)
ruckusZDWLANAPIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfMtu.setStatus("current")
_RuckusZDWLANAPIfSpeed_Type = DisplayString
_RuckusZDWLANAPIfSpeed_Object = MibTableColumn
ruckusZDWLANAPIfSpeed = _RuckusZDWLANAPIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 6),
    _RuckusZDWLANAPIfSpeed_Type()
)
ruckusZDWLANAPIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfSpeed.setStatus("current")
_RuckusZDWLANAPIfPhysAddress_Type = DisplayString
_RuckusZDWLANAPIfPhysAddress_Object = MibTableColumn
ruckusZDWLANAPIfPhysAddress = _RuckusZDWLANAPIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 7),
    _RuckusZDWLANAPIfPhysAddress_Type()
)
ruckusZDWLANAPIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfPhysAddress.setStatus("current")


class _RuckusZDWLANAPIfAdminStatus_Type(Integer32):
    """Custom type ruckusZDWLANAPIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_RuckusZDWLANAPIfAdminStatus_Type.__name__ = "Integer32"
_RuckusZDWLANAPIfAdminStatus_Object = MibTableColumn
ruckusZDWLANAPIfAdminStatus = _RuckusZDWLANAPIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 8),
    _RuckusZDWLANAPIfAdminStatus_Type()
)
ruckusZDWLANAPIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfAdminStatus.setStatus("current")


class _RuckusZDWLANAPIfOperStatus_Type(Integer32):
    """Custom type ruckusZDWLANAPIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_RuckusZDWLANAPIfOperStatus_Type.__name__ = "Integer32"
_RuckusZDWLANAPIfOperStatus_Object = MibTableColumn
ruckusZDWLANAPIfOperStatus = _RuckusZDWLANAPIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 9),
    _RuckusZDWLANAPIfOperStatus_Type()
)
ruckusZDWLANAPIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfOperStatus.setStatus("current")
_RuckusZDWLANAPIfInOctets_Type = Counter32
_RuckusZDWLANAPIfInOctets_Object = MibTableColumn
ruckusZDWLANAPIfInOctets = _RuckusZDWLANAPIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 10),
    _RuckusZDWLANAPIfInOctets_Type()
)
ruckusZDWLANAPIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfInOctets.setStatus("current")
_RuckusZDWLANAPIfInUcastPkts_Type = Counter32
_RuckusZDWLANAPIfInUcastPkts_Object = MibTableColumn
ruckusZDWLANAPIfInUcastPkts = _RuckusZDWLANAPIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 11),
    _RuckusZDWLANAPIfInUcastPkts_Type()
)
ruckusZDWLANAPIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfInUcastPkts.setStatus("current")
_RuckusZDWLANAPIfInNUcastPkts_Type = Counter32
_RuckusZDWLANAPIfInNUcastPkts_Object = MibTableColumn
ruckusZDWLANAPIfInNUcastPkts = _RuckusZDWLANAPIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 12),
    _RuckusZDWLANAPIfInNUcastPkts_Type()
)
ruckusZDWLANAPIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfInNUcastPkts.setStatus("current")
_RuckusZDWLANAPIfInDiscards_Type = Counter32
_RuckusZDWLANAPIfInDiscards_Object = MibTableColumn
ruckusZDWLANAPIfInDiscards = _RuckusZDWLANAPIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 13),
    _RuckusZDWLANAPIfInDiscards_Type()
)
ruckusZDWLANAPIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfInDiscards.setStatus("current")
_RuckusZDWLANAPIfInErrors_Type = Counter32
_RuckusZDWLANAPIfInErrors_Object = MibTableColumn
ruckusZDWLANAPIfInErrors = _RuckusZDWLANAPIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 14),
    _RuckusZDWLANAPIfInErrors_Type()
)
ruckusZDWLANAPIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfInErrors.setStatus("current")
_RuckusZDWLANAPIfInUnknownProtos_Type = Counter32
_RuckusZDWLANAPIfInUnknownProtos_Object = MibTableColumn
ruckusZDWLANAPIfInUnknownProtos = _RuckusZDWLANAPIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 15),
    _RuckusZDWLANAPIfInUnknownProtos_Type()
)
ruckusZDWLANAPIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfInUnknownProtos.setStatus("current")
_RuckusZDWLANAPIfOutOctets_Type = Counter32
_RuckusZDWLANAPIfOutOctets_Object = MibTableColumn
ruckusZDWLANAPIfOutOctets = _RuckusZDWLANAPIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 16),
    _RuckusZDWLANAPIfOutOctets_Type()
)
ruckusZDWLANAPIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfOutOctets.setStatus("current")
_RuckusZDWLANAPIfOutUcastPkts_Type = Counter32
_RuckusZDWLANAPIfOutUcastPkts_Object = MibTableColumn
ruckusZDWLANAPIfOutUcastPkts = _RuckusZDWLANAPIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 17),
    _RuckusZDWLANAPIfOutUcastPkts_Type()
)
ruckusZDWLANAPIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfOutUcastPkts.setStatus("current")
_RuckusZDWLANAPIfOutNUcastPkts_Type = Counter32
_RuckusZDWLANAPIfOutNUcastPkts_Object = MibTableColumn
ruckusZDWLANAPIfOutNUcastPkts = _RuckusZDWLANAPIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 18),
    _RuckusZDWLANAPIfOutNUcastPkts_Type()
)
ruckusZDWLANAPIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfOutNUcastPkts.setStatus("current")
_RuckusZDWLANAPIfOutDiscards_Type = Counter32
_RuckusZDWLANAPIfOutDiscards_Object = MibTableColumn
ruckusZDWLANAPIfOutDiscards = _RuckusZDWLANAPIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 19),
    _RuckusZDWLANAPIfOutDiscards_Type()
)
ruckusZDWLANAPIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfOutDiscards.setStatus("current")
_RuckusZDWLANAPIfOutErrors_Type = Counter32
_RuckusZDWLANAPIfOutErrors_Object = MibTableColumn
ruckusZDWLANAPIfOutErrors = _RuckusZDWLANAPIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 20),
    _RuckusZDWLANAPIfOutErrors_Type()
)
ruckusZDWLANAPIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfOutErrors.setStatus("current")
_RuckusZDWLANAPIfName_Type = DisplayString
_RuckusZDWLANAPIfName_Object = MibTableColumn
ruckusZDWLANAPIfName = _RuckusZDWLANAPIfName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 21),
    _RuckusZDWLANAPIfName_Type()
)
ruckusZDWLANAPIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfName.setStatus("current")
_RuckusZDWLANAPIfNameDefined_Type = DisplayString
_RuckusZDWLANAPIfNameDefined_Object = MibTableColumn
ruckusZDWLANAPIfNameDefined = _RuckusZDWLANAPIfNameDefined_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 4, 1, 22),
    _RuckusZDWLANAPIfNameDefined_Type()
)
ruckusZDWLANAPIfNameDefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPIfNameDefined.setStatus("current")
_RuckusZDWLANAPEthStatusTable_Object = MibTable
ruckusZDWLANAPEthStatusTable = _RuckusZDWLANAPEthStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    ruckusZDWLANAPEthStatusTable.setStatus("current")
_RuckusZDWLANAPEthStatusEntry_Object = MibTableRow
ruckusZDWLANAPEthStatusEntry = _RuckusZDWLANAPEthStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 8, 1)
)
ruckusZDWLANAPEthStatusEntry.setIndexNames(
    (0, "RUCKUS-ZD-WLAN-MIB", "ruckusZDWLANAPMacAddress"),
    (0, "RUCKUS-ZD-WLAN-MIB", "ruckusZDWLANAPEthPortId"),
)
if mibBuilder.loadTexts:
    ruckusZDWLANAPEthStatusEntry.setStatus("current")
_RuckusZDWLANAPMacAddress_Type = MacAddress
_RuckusZDWLANAPMacAddress_Object = MibTableColumn
ruckusZDWLANAPMacAddress = _RuckusZDWLANAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 8, 1, 1),
    _RuckusZDWLANAPMacAddress_Type()
)
ruckusZDWLANAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPMacAddress.setStatus("current")
_RuckusZDWLANAPEthPortId_Type = Integer32
_RuckusZDWLANAPEthPortId_Object = MibTableColumn
ruckusZDWLANAPEthPortId = _RuckusZDWLANAPEthPortId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 8, 1, 2),
    _RuckusZDWLANAPEthPortId_Type()
)
ruckusZDWLANAPEthPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPEthPortId.setStatus("current")
_RuckusZDWLANAPEthIfname_Type = OctetString
_RuckusZDWLANAPEthIfname_Object = MibTableColumn
ruckusZDWLANAPEthIfname = _RuckusZDWLANAPEthIfname_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 8, 1, 5),
    _RuckusZDWLANAPEthIfname_Type()
)
ruckusZDWLANAPEthIfname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPEthIfname.setStatus("current")


class _RuckusZDWLANAPEthDot1xStatus_Type(Integer32):
    """Custom type ruckusZDWLANAPEthDot1xStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auth", 1),
          ("none", 3),
          ("supp", 2))
    )


_RuckusZDWLANAPEthDot1xStatus_Type.__name__ = "Integer32"
_RuckusZDWLANAPEthDot1xStatus_Object = MibTableColumn
ruckusZDWLANAPEthDot1xStatus = _RuckusZDWLANAPEthDot1xStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 8, 1, 6),
    _RuckusZDWLANAPEthDot1xStatus_Type()
)
ruckusZDWLANAPEthDot1xStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPEthDot1xStatus.setStatus("current")


class _RuckusZDWLANAPEthLogicalStatus_Type(Integer32):
    """Custom type ruckusZDWLANAPEthLogicalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_RuckusZDWLANAPEthLogicalStatus_Type.__name__ = "Integer32"
_RuckusZDWLANAPEthLogicalStatus_Object = MibTableColumn
ruckusZDWLANAPEthLogicalStatus = _RuckusZDWLANAPEthLogicalStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 8, 1, 7),
    _RuckusZDWLANAPEthLogicalStatus_Type()
)
ruckusZDWLANAPEthLogicalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPEthLogicalStatus.setStatus("current")


class _RuckusZDWLANAPEthPhyStatus_Type(Integer32):
    """Custom type ruckusZDWLANAPEthPhyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_RuckusZDWLANAPEthPhyStatus_Type.__name__ = "Integer32"
_RuckusZDWLANAPEthPhyStatus_Object = MibTableColumn
ruckusZDWLANAPEthPhyStatus = _RuckusZDWLANAPEthPhyStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 8, 1, 8),
    _RuckusZDWLANAPEthPhyStatus_Type()
)
ruckusZDWLANAPEthPhyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPEthPhyStatus.setStatus("current")
_RuckusZDWLANAPEthPhyIfSpeed_Type = Integer32
_RuckusZDWLANAPEthPhyIfSpeed_Object = MibTableColumn
ruckusZDWLANAPEthPhyIfSpeed = _RuckusZDWLANAPEthPhyIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 8, 1, 9),
    _RuckusZDWLANAPEthPhyIfSpeed_Type()
)
ruckusZDWLANAPEthPhyIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPEthPhyIfSpeed.setStatus("current")


class _RuckusZDWLANAPEthPhyLinkStatus_Type(Integer32):
    """Custom type ruckusZDWLANAPEthPhyLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_RuckusZDWLANAPEthPhyLinkStatus_Type.__name__ = "Integer32"
_RuckusZDWLANAPEthPhyLinkStatus_Object = MibTableColumn
ruckusZDWLANAPEthPhyLinkStatus = _RuckusZDWLANAPEthPhyLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 8, 1, 10),
    _RuckusZDWLANAPEthPhyLinkStatus_Type()
)
ruckusZDWLANAPEthPhyLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPEthPhyLinkStatus.setStatus("current")
_RuckusZDWLANAPEthLabel_Type = OctetString
_RuckusZDWLANAPEthLabel_Object = MibTableColumn
ruckusZDWLANAPEthLabel = _RuckusZDWLANAPEthLabel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 2, 8, 1, 11),
    _RuckusZDWLANAPEthLabel_Type()
)
ruckusZDWLANAPEthLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANAPEthLabel.setStatus("current")
_RuckusZDWLANStaInfo_ObjectIdentity = ObjectIdentity
ruckusZDWLANStaInfo = _RuckusZDWLANStaInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3)
)
_RuckusZDWLANStaTable_Object = MibTable
ruckusZDWLANStaTable = _RuckusZDWLANStaTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruckusZDWLANStaTable.setStatus("current")
_RuckusZDWLANStaEntry_Object = MibTableRow
ruckusZDWLANStaEntry = _RuckusZDWLANStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1)
)
ruckusZDWLANStaEntry.setIndexNames(
    (0, "RUCKUS-ZD-WLAN-MIB", "ruckusZDWLANStaMacAddr"),
)
if mibBuilder.loadTexts:
    ruckusZDWLANStaEntry.setStatus("current")
_RuckusZDWLANStaMacAddr_Type = MacAddress
_RuckusZDWLANStaMacAddr_Object = MibTableColumn
ruckusZDWLANStaMacAddr = _RuckusZDWLANStaMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 1),
    _RuckusZDWLANStaMacAddr_Type()
)
ruckusZDWLANStaMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaMacAddr.setStatus("current")
_RuckusZDWLANStaAPMacAddr_Type = MacAddress
_RuckusZDWLANStaAPMacAddr_Object = MibTableColumn
ruckusZDWLANStaAPMacAddr = _RuckusZDWLANStaAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 2),
    _RuckusZDWLANStaAPMacAddr_Type()
)
ruckusZDWLANStaAPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaAPMacAddr.setStatus("current")
_RuckusZDWLANStaBSSID_Type = MacAddress
_RuckusZDWLANStaBSSID_Object = MibTableColumn
ruckusZDWLANStaBSSID = _RuckusZDWLANStaBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 3),
    _RuckusZDWLANStaBSSID_Type()
)
ruckusZDWLANStaBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaBSSID.setStatus("current")
_RuckusZDWLANStaSSID_Type = RuckusSSID
_RuckusZDWLANStaSSID_Object = MibTableColumn
ruckusZDWLANStaSSID = _RuckusZDWLANStaSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 4),
    _RuckusZDWLANStaSSID_Type()
)
ruckusZDWLANStaSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaSSID.setStatus("current")
_RuckusZDWLANStaUser_Type = DisplayString
_RuckusZDWLANStaUser_Object = MibTableColumn
ruckusZDWLANStaUser = _RuckusZDWLANStaUser_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 5),
    _RuckusZDWLANStaUser_Type()
)
ruckusZDWLANStaUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaUser.setStatus("current")


class _RuckusZDWLANStaRadioType_Type(Integer32):
    """Custom type ruckusZDWLANStaRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("radio11a", 0),
          ("radio11b", 1),
          ("radio11g", 2),
          ("radio11na", 4),
          ("radio11ng", 3))
    )


_RuckusZDWLANStaRadioType_Type.__name__ = "Integer32"
_RuckusZDWLANStaRadioType_Object = MibTableColumn
ruckusZDWLANStaRadioType = _RuckusZDWLANStaRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 6),
    _RuckusZDWLANStaRadioType_Type()
)
ruckusZDWLANStaRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaRadioType.setStatus("current")
_RuckusZDWLANStaChannel_Type = Unsigned32
_RuckusZDWLANStaChannel_Object = MibTableColumn
ruckusZDWLANStaChannel = _RuckusZDWLANStaChannel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 7),
    _RuckusZDWLANStaChannel_Type()
)
ruckusZDWLANStaChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaChannel.setStatus("current")
_RuckusZDWLANStaIPAddr_Type = IpAddress
_RuckusZDWLANStaIPAddr_Object = MibTableColumn
ruckusZDWLANStaIPAddr = _RuckusZDWLANStaIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 8),
    _RuckusZDWLANStaIPAddr_Type()
)
ruckusZDWLANStaIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaIPAddr.setStatus("current")
_RuckusZDWLANStaAvgRSSI_Type = Integer32
_RuckusZDWLANStaAvgRSSI_Object = MibTableColumn
ruckusZDWLANStaAvgRSSI = _RuckusZDWLANStaAvgRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 9),
    _RuckusZDWLANStaAvgRSSI_Type()
)
ruckusZDWLANStaAvgRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaAvgRSSI.setStatus("current")
_RuckusZDWLANStaRxPkts_Type = Counter32
_RuckusZDWLANStaRxPkts_Object = MibTableColumn
ruckusZDWLANStaRxPkts = _RuckusZDWLANStaRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 10),
    _RuckusZDWLANStaRxPkts_Type()
)
ruckusZDWLANStaRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaRxPkts.setStatus("current")
_RuckusZDWLANStaRxBytes_Type = Counter64
_RuckusZDWLANStaRxBytes_Object = MibTableColumn
ruckusZDWLANStaRxBytes = _RuckusZDWLANStaRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 11),
    _RuckusZDWLANStaRxBytes_Type()
)
ruckusZDWLANStaRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaRxBytes.setStatus("current")
_RuckusZDWLANStaTxPkts_Type = Counter32
_RuckusZDWLANStaTxPkts_Object = MibTableColumn
ruckusZDWLANStaTxPkts = _RuckusZDWLANStaTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 12),
    _RuckusZDWLANStaTxPkts_Type()
)
ruckusZDWLANStaTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaTxPkts.setStatus("current")
_RuckusZDWLANStaTxBytes_Type = Counter64
_RuckusZDWLANStaTxBytes_Object = MibTableColumn
ruckusZDWLANStaTxBytes = _RuckusZDWLANStaTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 13),
    _RuckusZDWLANStaTxBytes_Type()
)
ruckusZDWLANStaTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaTxBytes.setStatus("current")
_RuckusZDWLANStaRetries_Type = Counter32
_RuckusZDWLANStaRetries_Object = MibTableColumn
ruckusZDWLANStaRetries = _RuckusZDWLANStaRetries_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 14),
    _RuckusZDWLANStaRetries_Type()
)
ruckusZDWLANStaRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaRetries.setStatus("current")
_RuckusZDWLANStaAssocTime_Type = TimeTicks
_RuckusZDWLANStaAssocTime_Object = MibTableColumn
ruckusZDWLANStaAssocTime = _RuckusZDWLANStaAssocTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 15),
    _RuckusZDWLANStaAssocTime_Type()
)
ruckusZDWLANStaAssocTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaAssocTime.setStatus("current")
_RuckusZDWLANStaRxError_Type = Counter32
_RuckusZDWLANStaRxError_Object = MibTableColumn
ruckusZDWLANStaRxError = _RuckusZDWLANStaRxError_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 16),
    _RuckusZDWLANStaRxError_Type()
)
ruckusZDWLANStaRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaRxError.setStatus("current")
_RuckusZDWLANStaTxSuccess_Type = Counter32
_RuckusZDWLANStaTxSuccess_Object = MibTableColumn
ruckusZDWLANStaTxSuccess = _RuckusZDWLANStaTxSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 17),
    _RuckusZDWLANStaTxSuccess_Type()
)
ruckusZDWLANStaTxSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaTxSuccess.setStatus("current")
_RuckusZDWLANSta11bgReassoc_Type = Counter32
_RuckusZDWLANSta11bgReassoc_Object = MibTableColumn
ruckusZDWLANSta11bgReassoc = _RuckusZDWLANSta11bgReassoc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 18),
    _RuckusZDWLANSta11bgReassoc_Type()
)
ruckusZDWLANSta11bgReassoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANSta11bgReassoc.setStatus("current")
_RuckusZDWLANStaAssocTimestamp_Type = DisplayString
_RuckusZDWLANStaAssocTimestamp_Object = MibTableColumn
ruckusZDWLANStaAssocTimestamp = _RuckusZDWLANStaAssocTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 19),
    _RuckusZDWLANStaAssocTimestamp_Type()
)
ruckusZDWLANStaAssocTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaAssocTimestamp.setStatus("current")
_RuckusZDWLANStaRetryBytes_Type = Counter32
_RuckusZDWLANStaRetryBytes_Object = MibTableColumn
ruckusZDWLANStaRetryBytes = _RuckusZDWLANStaRetryBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 20),
    _RuckusZDWLANStaRetryBytes_Type()
)
ruckusZDWLANStaRetryBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaRetryBytes.setStatus("current")
_RuckusZDWLANStaSNR_Type = Integer32
_RuckusZDWLANStaSNR_Object = MibTableColumn
ruckusZDWLANStaSNR = _RuckusZDWLANStaSNR_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 21),
    _RuckusZDWLANStaSNR_Type()
)
ruckusZDWLANStaSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaSNR.setStatus("current")
_RuckusZDWLANStaRxDrop_Type = Counter32
_RuckusZDWLANStaRxDrop_Object = MibTableColumn
ruckusZDWLANStaRxDrop = _RuckusZDWLANStaRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 22),
    _RuckusZDWLANStaRxDrop_Type()
)
ruckusZDWLANStaRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaRxDrop.setStatus("current")
_RuckusZDWLANStaTxDrop_Type = Counter32
_RuckusZDWLANStaTxDrop_Object = MibTableColumn
ruckusZDWLANStaTxDrop = _RuckusZDWLANStaTxDrop_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 23),
    _RuckusZDWLANStaTxDrop_Type()
)
ruckusZDWLANStaTxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaTxDrop.setStatus("current")
_RuckusZDWLANStaTxError_Type = Counter32
_RuckusZDWLANStaTxError_Object = MibTableColumn
ruckusZDWLANStaTxError = _RuckusZDWLANStaTxError_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 24),
    _RuckusZDWLANStaTxError_Type()
)
ruckusZDWLANStaTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaTxError.setStatus("current")


class _RuckusZDWLANStaVlanID_Type(Integer32):
    """Custom type ruckusZDWLANStaVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuckusZDWLANStaVlanID_Type.__name__ = "Integer32"
_RuckusZDWLANStaVlanID_Object = MibTableColumn
ruckusZDWLANStaVlanID = _RuckusZDWLANStaVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 30),
    _RuckusZDWLANStaVlanID_Type()
)
ruckusZDWLANStaVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaVlanID.setStatus("current")
_RuckusZDWLANStaAuthMode_Type = DisplayString
_RuckusZDWLANStaAuthMode_Object = MibTableColumn
ruckusZDWLANStaAuthMode = _RuckusZDWLANStaAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 80),
    _RuckusZDWLANStaAuthMode_Type()
)
ruckusZDWLANStaAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaAuthMode.setStatus("current")
_RuckusZDWLANStaSignalStrength_Type = Integer32
_RuckusZDWLANStaSignalStrength_Object = MibTableColumn
ruckusZDWLANStaSignalStrength = _RuckusZDWLANStaSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 3, 1, 1, 81),
    _RuckusZDWLANStaSignalStrength_Type()
)
ruckusZDWLANStaSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANStaSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    ruckusZDWLANStaSignalStrength.setUnits("dBm")
_RuckusZDWLANRogueInfo_ObjectIdentity = ObjectIdentity
ruckusZDWLANRogueInfo = _RuckusZDWLANRogueInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 4)
)
_RuckusZDWLANRogueTable_Object = MibTable
ruckusZDWLANRogueTable = _RuckusZDWLANRogueTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ruckusZDWLANRogueTable.setStatus("current")
_RuckusZDWLANRogueEntry_Object = MibTableRow
ruckusZDWLANRogueEntry = _RuckusZDWLANRogueEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 4, 1, 1)
)
ruckusZDWLANRogueEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusZDWLANRogueEntry.setStatus("current")
_RuckusZDWLANRogueMacAddr_Type = MacAddress
_RuckusZDWLANRogueMacAddr_Object = MibTableColumn
ruckusZDWLANRogueMacAddr = _RuckusZDWLANRogueMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 4, 1, 1, 1),
    _RuckusZDWLANRogueMacAddr_Type()
)
ruckusZDWLANRogueMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANRogueMacAddr.setStatus("current")
_RuckusZDWLANRogueSSID_Type = RuckusSSID
_RuckusZDWLANRogueSSID_Object = MibTableColumn
ruckusZDWLANRogueSSID = _RuckusZDWLANRogueSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 4, 1, 1, 2),
    _RuckusZDWLANRogueSSID_Type()
)
ruckusZDWLANRogueSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANRogueSSID.setStatus("current")


class _RuckusZDWLANRogueRadioType_Type(Integer32):
    """Custom type ruckusZDWLANRogueRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("radio11a", 1),
          ("radio11bg", 0),
          ("radio11na", 3),
          ("radio11ng", 2))
    )


_RuckusZDWLANRogueRadioType_Type.__name__ = "Integer32"
_RuckusZDWLANRogueRadioType_Object = MibTableColumn
ruckusZDWLANRogueRadioType = _RuckusZDWLANRogueRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 4, 1, 1, 3),
    _RuckusZDWLANRogueRadioType_Type()
)
ruckusZDWLANRogueRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANRogueRadioType.setStatus("current")
_RuckusZDWLANRogueChannel_Type = Unsigned32
_RuckusZDWLANRogueChannel_Object = MibTableColumn
ruckusZDWLANRogueChannel = _RuckusZDWLANRogueChannel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 4, 1, 1, 4),
    _RuckusZDWLANRogueChannel_Type()
)
ruckusZDWLANRogueChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANRogueChannel.setStatus("current")
_RuckusZDWLANRogueRSSI_Type = Integer32
_RuckusZDWLANRogueRSSI_Object = MibTableColumn
ruckusZDWLANRogueRSSI = _RuckusZDWLANRogueRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 4, 1, 1, 5),
    _RuckusZDWLANRogueRSSI_Type()
)
ruckusZDWLANRogueRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANRogueRSSI.setStatus("current")


class _RuckusZDWLANRogueType_Type(Integer32):
    """Custom type ruckusZDWLANRogueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ad-hoc", 1),
          ("ap", 0))
    )


_RuckusZDWLANRogueType_Type.__name__ = "Integer32"
_RuckusZDWLANRogueType_Object = MibTableColumn
ruckusZDWLANRogueType = _RuckusZDWLANRogueType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 4, 1, 1, 6),
    _RuckusZDWLANRogueType_Type()
)
ruckusZDWLANRogueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANRogueType.setStatus("current")


class _RuckusZDWLANRogueEncrypted_Type(Integer32):
    """Custom type ruckusZDWLANRogueEncrypted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 1),
          ("open", 0))
    )


_RuckusZDWLANRogueEncrypted_Type.__name__ = "Integer32"
_RuckusZDWLANRogueEncrypted_Object = MibTableColumn
ruckusZDWLANRogueEncrypted = _RuckusZDWLANRogueEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 4, 1, 1, 7),
    _RuckusZDWLANRogueEncrypted_Type()
)
ruckusZDWLANRogueEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANRogueEncrypted.setStatus("current")
_RuckusZDWLANRogueSignalStrength_Type = Integer32
_RuckusZDWLANRogueSignalStrength_Object = MibTableColumn
ruckusZDWLANRogueSignalStrength = _RuckusZDWLANRogueSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 1, 1, 4, 1, 1, 11),
    _RuckusZDWLANRogueSignalStrength_Type()
)
ruckusZDWLANRogueSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANRogueSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    ruckusZDWLANRogueSignalStrength.setUnits("dBm")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-ZD-WLAN-MIB",
    **{"ruckusZDWLANMIB": ruckusZDWLANMIB,
       "ruckusZDWLANObjects": ruckusZDWLANObjects,
       "ruckusZDWLANInfo": ruckusZDWLANInfo,
       "ruckusZDWLANTable": ruckusZDWLANTable,
       "ruckusZDWLANEntry": ruckusZDWLANEntry,
       "ruckusZDWLANSSID": ruckusZDWLANSSID,
       "ruckusZDWLANDescription": ruckusZDWLANDescription,
       "ruckusZDWLANAuthentication": ruckusZDWLANAuthentication,
       "ruckusZDWLANEncryption": ruckusZDWLANEncryption,
       "ruckusZDWLANIsGuest": ruckusZDWLANIsGuest,
       "ruckusZDWLANSSIDBcastDisable": ruckusZDWLANSSIDBcastDisable,
       "ruckusZDWLANVlanID": ruckusZDWLANVlanID,
       "ruckusZDWLANRateLimitingUp": ruckusZDWLANRateLimitingUp,
       "ruckusZDWLANRateLimitingDown": ruckusZDWLANRateLimitingDown,
       "ruckusZDWLANTunnelWLAN": ruckusZDWLANTunnelWLAN,
       "ruckusZDWLANNumVAP": ruckusZDWLANNumVAP,
       "ruckusZDWLANNumSta": ruckusZDWLANNumSta,
       "ruckusZDWLANRxPkts": ruckusZDWLANRxPkts,
       "ruckusZDWLANRxBytes": ruckusZDWLANRxBytes,
       "ruckusZDWLANTxPkts": ruckusZDWLANTxPkts,
       "ruckusZDWLANTxBytes": ruckusZDWLANTxBytes,
       "ruckusZDWLANAuthTotal": ruckusZDWLANAuthTotal,
       "ruckusZDWLANAuthResp": ruckusZDWLANAuthResp,
       "ruckusZDWLANAuthSuccessTotal": ruckusZDWLANAuthSuccessTotal,
       "ruckusZDWLANAuthFail": ruckusZDWLANAuthFail,
       "ruckusZDWLANAssocTotal": ruckusZDWLANAssocTotal,
       "ruckusZDWLANAssocResp": ruckusZDWLANAssocResp,
       "ruckusZDWLANReassocReq": ruckusZDWLANReassocReq,
       "ruckusZDWLANReassocResp": ruckusZDWLANReassocResp,
       "ruckusZDWLANAssocSuccess": ruckusZDWLANAssocSuccess,
       "ruckusZDWLANAssocFail": ruckusZDWLANAssocFail,
       "ruckusZDWLANAssocDenied": ruckusZDWLANAssocDenied,
       "ruckusZDWLANDiassocAbnormal": ruckusZDWLANDiassocAbnormal,
       "ruckusZDWLANDiassocCapacity": ruckusZDWLANDiassocCapacity,
       "ruckusZDWLANDiassocLeave": ruckusZDWLANDiassocLeave,
       "ruckusZDWLANDiassocMisc": ruckusZDWLANDiassocMisc,
       "ruckusZDWLANRxByteRate": ruckusZDWLANRxByteRate,
       "ruckusZDWLANTxByteRate": ruckusZDWLANTxByteRate,
       "ruckusZDWLANRxDataFrameOnLan": ruckusZDWLANRxDataFrameOnLan,
       "ruckusZDWLANRxByteOnLan": ruckusZDWLANRxByteOnLan,
       "ruckusZDWLANTxByteOnLan": ruckusZDWLANTxByteOnLan,
       "ruckusZDWLANDownDropFrame": ruckusZDWLANDownDropFrame,
       "ruckusZDWLANDownRetxFrame": ruckusZDWLANDownRetxFrame,
       "ruckusZDWLANDownTotalFrame": ruckusZDWLANDownTotalFrame,
       "ruckusZDWLANDownTotalErrFrame": ruckusZDWLANDownTotalErrFrame,
       "ruckusZDWLANUpTotalFrame": ruckusZDWLANUpTotalFrame,
       "ruckusZDWLANUpDropFrame": ruckusZDWLANUpDropFrame,
       "ruckusZDWLANUpRetxFrame": ruckusZDWLANUpRetxFrame,
       "ruckusZDWLANNAME": ruckusZDWLANNAME,
       "ruckusZDWLANAPInfo": ruckusZDWLANAPInfo,
       "ruckusZDWLANAPTable": ruckusZDWLANAPTable,
       "ruckusZDWLANAPEntry": ruckusZDWLANAPEntry,
       "ruckusZDWLANAPMacAddr": ruckusZDWLANAPMacAddr,
       "ruckusZDWLANAPDescription": ruckusZDWLANAPDescription,
       "ruckusZDWLANAPStatus": ruckusZDWLANAPStatus,
       "ruckusZDWLANAPModel": ruckusZDWLANAPModel,
       "ruckusZDWLANAPSerialNumber": ruckusZDWLANAPSerialNumber,
       "ruckusZDWLANAPUptime": ruckusZDWLANAPUptime,
       "ruckusZDWLANAPSWversion": ruckusZDWLANAPSWversion,
       "ruckusZDWLANAPHWversion": ruckusZDWLANAPHWversion,
       "ruckusZDWLANAPIPAddr": ruckusZDWLANAPIPAddr,
       "ruckusZDWLANAPNumRadios": ruckusZDWLANAPNumRadios,
       "ruckusZDWLANAPNumVAP": ruckusZDWLANAPNumVAP,
       "ruckusZDWLANAPNumSta": ruckusZDWLANAPNumSta,
       "ruckusZDWLANAPNumRogues": ruckusZDWLANAPNumRogues,
       "ruckusZDWLANAPConnectionMode": ruckusZDWLANAPConnectionMode,
       "ruckusZDWLANAPMeshEnable": ruckusZDWLANAPMeshEnable,
       "ruckusZDWLANAPMeshHops": ruckusZDWLANAPMeshHops,
       "ruckusZDWLANAPMeshType": ruckusZDWLANAPMeshType,
       "ruckusZDWLANAPLANStatsRXByte": ruckusZDWLANAPLANStatsRXByte,
       "ruckusZDWLANAPLANStatsRXPkt": ruckusZDWLANAPLANStatsRXPkt,
       "ruckusZDWLANAPLANStatsRXPktErr": ruckusZDWLANAPLANStatsRXPktErr,
       "ruckusZDWLANAPLANStatsRXPKTSucc": ruckusZDWLANAPLANStatsRXPKTSucc,
       "ruckusZDWLANAPLANStatsTXByte": ruckusZDWLANAPLANStatsTXByte,
       "ruckusZDWLANAPLANStatsTXPkt": ruckusZDWLANAPLANStatsTXPkt,
       "ruckusZDWLANAPMemUtil": ruckusZDWLANAPMemUtil,
       "ruckusZDWLANAPMemTotal": ruckusZDWLANAPMemTotal,
       "ruckusZDWLANAPCPUUtil": ruckusZDWLANAPCPUUtil,
       "ruckusZDWLANAPFWSize": ruckusZDWLANAPFWSize,
       "ruckusZDWLANAPFWAvail": ruckusZDWLANAPFWAvail,
       "ruckusZDWLANAPMultipleVlanCapability": ruckusZDWLANAPMultipleVlanCapability,
       "ruckusZDWLANAP11bCapable": ruckusZDWLANAP11bCapable,
       "ruckusZDWLANAP11gCapable": ruckusZDWLANAP11gCapable,
       "ruckusZDWLANAPMultiModeAccessStatus": ruckusZDWLANAPMultiModeAccessStatus,
       "ruckusZDWLANAPEthStateChange": ruckusZDWLANAPEthStateChange,
       "ruckusZDWLANAPSyncConf": ruckusZDWLANAPSyncConf,
       "ruckusZDWLANAPUpgrade": ruckusZDWLANAPUpgrade,
       "ruckusZDWLANAPFirstJoinTime": ruckusZDWLANAPFirstJoinTime,
       "ruckusZDWLANAPLastBootTime": ruckusZDWLANAPLastBootTime,
       "ruckusZDWLANAPLastUpgradeTime": ruckusZDWLANAPLastUpgradeTime,
       "ruckusZDWLANAPLastConfSyncTime": ruckusZDWLANAPLastConfSyncTime,
       "ruckusZDWLANAPLANStatsRXPKTBcast": ruckusZDWLANAPLANStatsRXPKTBcast,
       "ruckusZDWLANAPLANStatsRXPKTMcast": ruckusZDWLANAPLANStatsRXPKTMcast,
       "ruckusZDWLANAPLANStatsRXPKTUcast": ruckusZDWLANAPLANStatsRXPKTUcast,
       "ruckusZDWLANAPLANStatsTXPKTBcast": ruckusZDWLANAPLANStatsTXPKTBcast,
       "ruckusZDWLANAPLANStatsTXPKTMcast": ruckusZDWLANAPLANStatsTXPKTMcast,
       "ruckusZDWLANAPLANStatsTXPKTUcast": ruckusZDWLANAPLANStatsTXPKTUcast,
       "ruckusZDWLANAPLANStatsDropped": ruckusZDWLANAPLANStatsDropped,
       "ruckusZDWLANAPMeshUpPortCntUpdown": ruckusZDWLANAPMeshUpPortCntUpdown,
       "ruckusZDWLANAPMeshDownPortCntUpdown": ruckusZDWLANAPMeshDownPortCntUpdown,
       "ruckusZDWLANAPTxFrameDropped": ruckusZDWLANAPTxFrameDropped,
       "ruckusZDWLANAPTxFrameError": ruckusZDWLANAPTxFrameError,
       "ruckusZDWLANAPCoverageTech": ruckusZDWLANAPCoverageTech,
       "ruckusZDWLANAPStaTxBytes": ruckusZDWLANAPStaTxBytes,
       "ruckusZDWLANAPStaRxBytes": ruckusZDWLANAPStaRxBytes,
       "ruckusZDWLANAPNetmask": ruckusZDWLANAPNetmask,
       "ruckusZDWLANAPGateway": ruckusZDWLANAPGateway,
       "ruckusZDWLANAPDNS1": ruckusZDWLANAPDNS1,
       "ruckusZDWLANAPDNS2": ruckusZDWLANAPDNS2,
       "ruckusZDWLANAPTotalUser": ruckusZDWLANAPTotalUser,
       "ruckusZDWLANAPLANStatsRXByteRate": ruckusZDWLANAPLANStatsRXByteRate,
       "ruckusZDWLANAPLANStatsTXByteRate": ruckusZDWLANAPLANStatsTXByteRate,
       "ruckusZDWLANAPRadioStatsTable": ruckusZDWLANAPRadioStatsTable,
       "ruckusZDWLANAPRadioStatsEntry": ruckusZDWLANAPRadioStatsEntry,
       "ruckusZDWLANAPRadioStatsAPMacAddr": ruckusZDWLANAPRadioStatsAPMacAddr,
       "ruckusZDWLANAPRadioStatsRadioIndex": ruckusZDWLANAPRadioStatsRadioIndex,
       "ruckusZDWLANAPRadioStatsRadioType": ruckusZDWLANAPRadioStatsRadioType,
       "ruckusZDWLANAPRadioStatsChannel": ruckusZDWLANAPRadioStatsChannel,
       "ruckusZDWLANAPRadioStatsTxPower": ruckusZDWLANAPRadioStatsTxPower,
       "ruckusZDWLANAPRadioStatsMeshEnable": ruckusZDWLANAPRadioStatsMeshEnable,
       "ruckusZDWLANAPRadioStatsNumVAP": ruckusZDWLANAPRadioStatsNumVAP,
       "ruckusZDWLANAPRadioStatsNumSta": ruckusZDWLANAPRadioStatsNumSta,
       "ruckusZDWLANAPRadioStatsAvgStaRSSI": ruckusZDWLANAPRadioStatsAvgStaRSSI,
       "ruckusZDWLANAPRadioStatsRxPkts": ruckusZDWLANAPRadioStatsRxPkts,
       "ruckusZDWLANAPRadioStatsRxBytes": ruckusZDWLANAPRadioStatsRxBytes,
       "ruckusZDWLANAPRadioStatsRxMulticast": ruckusZDWLANAPRadioStatsRxMulticast,
       "ruckusZDWLANAPRadioStatsTxPkts": ruckusZDWLANAPRadioStatsTxPkts,
       "ruckusZDWLANAPRadioStatsTxBytes": ruckusZDWLANAPRadioStatsTxBytes,
       "ruckusZDWLANAPRadioStatsTxMulticast": ruckusZDWLANAPRadioStatsTxMulticast,
       "ruckusZDWLANAPRadioStatsTxFail": ruckusZDWLANAPRadioStatsTxFail,
       "ruckusZDWLANAPRadioStatsTxRetries": ruckusZDWLANAPRadioStatsTxRetries,
       "ruckusZDWLANAPRadioStatsPowerMgmt": ruckusZDWLANAPRadioStatsPowerMgmt,
       "ruckusZDWLANAPRadioStatsMaxSta": ruckusZDWLANAPRadioStatsMaxSta,
       "ruckusZDWLANAPRadioStatsFrameErrorRate": ruckusZDWLANAPRadioStatsFrameErrorRate,
       "ruckusZDWLANAPRadioStatsFrameRetryRate": ruckusZDWLANAPRadioStatsFrameRetryRate,
       "ruckusZDWLANAPRadioStatsMonitoredTime": ruckusZDWLANAPRadioStatsMonitoredTime,
       "ruckusZDWLANAPRadioStatsTotalAssocTime": ruckusZDWLANAPRadioStatsTotalAssocTime,
       "ruckusZDWLANAPRadioStatsAuthReq": ruckusZDWLANAPRadioStatsAuthReq,
       "ruckusZDWLANAPRadioStatsAuthResp": ruckusZDWLANAPRadioStatsAuthResp,
       "ruckusZDWLANAPRadioStatsAuthSuccess": ruckusZDWLANAPRadioStatsAuthSuccess,
       "ruckusZDWLANAPRadioStatsAuthFail": ruckusZDWLANAPRadioStatsAuthFail,
       "ruckusZDWLANAPRadioStatsAssocReq": ruckusZDWLANAPRadioStatsAssocReq,
       "ruckusZDWLANAPRadioStatsAssocResp": ruckusZDWLANAPRadioStatsAssocResp,
       "ruckusZDWLANAPRadioStatsReassocReq": ruckusZDWLANAPRadioStatsReassocReq,
       "ruckusZDWLANAPRadioStatsReassocResp": ruckusZDWLANAPRadioStatsReassocResp,
       "ruckusZDWLANAPRadioStatsAssocSuccess": ruckusZDWLANAPRadioStatsAssocSuccess,
       "ruckusZDWLANAPRadioStatsAssocFail": ruckusZDWLANAPRadioStatsAssocFail,
       "ruckusZDWLANAPRadioStatsAssocDenied": ruckusZDWLANAPRadioStatsAssocDenied,
       "ruckusZDWLANAPRadioStatsDiassocAbnormal": ruckusZDWLANAPRadioStatsDiassocAbnormal,
       "ruckusZDWLANAPRadioStatsDiassocCapacity": ruckusZDWLANAPRadioStatsDiassocCapacity,
       "ruckusZDWLANAPRadioStatsDiassocLeave": ruckusZDWLANAPRadioStatsDiassocLeave,
       "ruckusZDWLANAPRadioStatsDiassocMisc": ruckusZDWLANAPRadioStatsDiassocMisc,
       "ruckusZDWLANAPRadioStatsResourceUtil": ruckusZDWLANAPRadioStatsResourceUtil,
       "ruckusZDWLANAPRadioStatsRxSignalFrm": ruckusZDWLANAPRadioStatsRxSignalFrm,
       "ruckusZDWLANAPRadioStatsTxSignalFrm": ruckusZDWLANAPRadioStatsTxSignalFrm,
       "ruckusZDWLANAPRadioStatsTotalSignalFrm": ruckusZDWLANAPRadioStatsTotalSignalFrm,
       "ruckusZDWLANAPRadioStatsAntennaGain": ruckusZDWLANAPRadioStatsAntennaGain,
       "ruckusZDWLANAPRadioStatsBeaconPeriod": ruckusZDWLANAPRadioStatsBeaconPeriod,
       "ruckusZDWLANAPRadioStatsRTSThreshold": ruckusZDWLANAPRadioStatsRTSThreshold,
       "ruckusZDWLANAPRadioStatsFragThreshold": ruckusZDWLANAPRadioStatsFragThreshold,
       "ruckusZDWLANVapTable": ruckusZDWLANVapTable,
       "ruckusZDWLANVapEntry": ruckusZDWLANVapEntry,
       "ruckusZDWLANVapBSSID": ruckusZDWLANVapBSSID,
       "ruckusZDWLANVapPAPAddr": ruckusZDWLANVapPAPAddr,
       "ruckusZDWLANVapSSID": ruckusZDWLANVapSSID,
       "ruckusZDWLANVapLanRxBytes": ruckusZDWLANVapLanRxBytes,
       "ruckusZDWLANVapLanTxBytes": ruckusZDWLANVapLanTxBytes,
       "ruckusZDWLANVapWlanRxBytes": ruckusZDWLANVapWlanRxBytes,
       "ruckusZDWLANVapWlanTxBytes": ruckusZDWLANVapWlanTxBytes,
       "ruckusZDWLANVapWlanRxErrorPkt": ruckusZDWLANVapWlanRxErrorPkt,
       "ruckusZDWLANVapWlanRxUnicastPkt": ruckusZDWLANVapWlanRxUnicastPkt,
       "ruckusZDWLANVapWlanTxUnicastPkt": ruckusZDWLANVapWlanTxUnicastPkt,
       "ruckusZDWLANVapWlanRxPkt": ruckusZDWLANVapWlanRxPkt,
       "ruckusZDWLANVapWlanRxDropPkt": ruckusZDWLANVapWlanRxDropPkt,
       "ruckusZDWLANVapWlanTxErrPkt": ruckusZDWLANVapWlanTxErrPkt,
       "ruckusZDWLANVapWlanTxPkt": ruckusZDWLANVapWlanTxPkt,
       "ruckusZDWLANVapWlanTxDropPkt": ruckusZDWLANVapWlanTxDropPkt,
       "ruckusZDWLANIfTable": ruckusZDWLANIfTable,
       "ruckusZDWLANIfEntry": ruckusZDWLANIfEntry,
       "ruckusZDWLANAPMac": ruckusZDWLANAPMac,
       "ruckusZDWLANAPIfIndex": ruckusZDWLANAPIfIndex,
       "ruckusZDWLANAPIfDescr": ruckusZDWLANAPIfDescr,
       "ruckusZDWLANAPIfType": ruckusZDWLANAPIfType,
       "ruckusZDWLANAPIfMtu": ruckusZDWLANAPIfMtu,
       "ruckusZDWLANAPIfSpeed": ruckusZDWLANAPIfSpeed,
       "ruckusZDWLANAPIfPhysAddress": ruckusZDWLANAPIfPhysAddress,
       "ruckusZDWLANAPIfAdminStatus": ruckusZDWLANAPIfAdminStatus,
       "ruckusZDWLANAPIfOperStatus": ruckusZDWLANAPIfOperStatus,
       "ruckusZDWLANAPIfInOctets": ruckusZDWLANAPIfInOctets,
       "ruckusZDWLANAPIfInUcastPkts": ruckusZDWLANAPIfInUcastPkts,
       "ruckusZDWLANAPIfInNUcastPkts": ruckusZDWLANAPIfInNUcastPkts,
       "ruckusZDWLANAPIfInDiscards": ruckusZDWLANAPIfInDiscards,
       "ruckusZDWLANAPIfInErrors": ruckusZDWLANAPIfInErrors,
       "ruckusZDWLANAPIfInUnknownProtos": ruckusZDWLANAPIfInUnknownProtos,
       "ruckusZDWLANAPIfOutOctets": ruckusZDWLANAPIfOutOctets,
       "ruckusZDWLANAPIfOutUcastPkts": ruckusZDWLANAPIfOutUcastPkts,
       "ruckusZDWLANAPIfOutNUcastPkts": ruckusZDWLANAPIfOutNUcastPkts,
       "ruckusZDWLANAPIfOutDiscards": ruckusZDWLANAPIfOutDiscards,
       "ruckusZDWLANAPIfOutErrors": ruckusZDWLANAPIfOutErrors,
       "ruckusZDWLANAPIfName": ruckusZDWLANAPIfName,
       "ruckusZDWLANAPIfNameDefined": ruckusZDWLANAPIfNameDefined,
       "ruckusZDWLANAPEthStatusTable": ruckusZDWLANAPEthStatusTable,
       "ruckusZDWLANAPEthStatusEntry": ruckusZDWLANAPEthStatusEntry,
       "ruckusZDWLANAPMacAddress": ruckusZDWLANAPMacAddress,
       "ruckusZDWLANAPEthPortId": ruckusZDWLANAPEthPortId,
       "ruckusZDWLANAPEthIfname": ruckusZDWLANAPEthIfname,
       "ruckusZDWLANAPEthDot1xStatus": ruckusZDWLANAPEthDot1xStatus,
       "ruckusZDWLANAPEthLogicalStatus": ruckusZDWLANAPEthLogicalStatus,
       "ruckusZDWLANAPEthPhyStatus": ruckusZDWLANAPEthPhyStatus,
       "ruckusZDWLANAPEthPhyIfSpeed": ruckusZDWLANAPEthPhyIfSpeed,
       "ruckusZDWLANAPEthPhyLinkStatus": ruckusZDWLANAPEthPhyLinkStatus,
       "ruckusZDWLANAPEthLabel": ruckusZDWLANAPEthLabel,
       "ruckusZDWLANStaInfo": ruckusZDWLANStaInfo,
       "ruckusZDWLANStaTable": ruckusZDWLANStaTable,
       "ruckusZDWLANStaEntry": ruckusZDWLANStaEntry,
       "ruckusZDWLANStaMacAddr": ruckusZDWLANStaMacAddr,
       "ruckusZDWLANStaAPMacAddr": ruckusZDWLANStaAPMacAddr,
       "ruckusZDWLANStaBSSID": ruckusZDWLANStaBSSID,
       "ruckusZDWLANStaSSID": ruckusZDWLANStaSSID,
       "ruckusZDWLANStaUser": ruckusZDWLANStaUser,
       "ruckusZDWLANStaRadioType": ruckusZDWLANStaRadioType,
       "ruckusZDWLANStaChannel": ruckusZDWLANStaChannel,
       "ruckusZDWLANStaIPAddr": ruckusZDWLANStaIPAddr,
       "ruckusZDWLANStaAvgRSSI": ruckusZDWLANStaAvgRSSI,
       "ruckusZDWLANStaRxPkts": ruckusZDWLANStaRxPkts,
       "ruckusZDWLANStaRxBytes": ruckusZDWLANStaRxBytes,
       "ruckusZDWLANStaTxPkts": ruckusZDWLANStaTxPkts,
       "ruckusZDWLANStaTxBytes": ruckusZDWLANStaTxBytes,
       "ruckusZDWLANStaRetries": ruckusZDWLANStaRetries,
       "ruckusZDWLANStaAssocTime": ruckusZDWLANStaAssocTime,
       "ruckusZDWLANStaRxError": ruckusZDWLANStaRxError,
       "ruckusZDWLANStaTxSuccess": ruckusZDWLANStaTxSuccess,
       "ruckusZDWLANSta11bgReassoc": ruckusZDWLANSta11bgReassoc,
       "ruckusZDWLANStaAssocTimestamp": ruckusZDWLANStaAssocTimestamp,
       "ruckusZDWLANStaRetryBytes": ruckusZDWLANStaRetryBytes,
       "ruckusZDWLANStaSNR": ruckusZDWLANStaSNR,
       "ruckusZDWLANStaRxDrop": ruckusZDWLANStaRxDrop,
       "ruckusZDWLANStaTxDrop": ruckusZDWLANStaTxDrop,
       "ruckusZDWLANStaTxError": ruckusZDWLANStaTxError,
       "ruckusZDWLANStaVlanID": ruckusZDWLANStaVlanID,
       "ruckusZDWLANStaAuthMode": ruckusZDWLANStaAuthMode,
       "ruckusZDWLANStaSignalStrength": ruckusZDWLANStaSignalStrength,
       "ruckusZDWLANRogueInfo": ruckusZDWLANRogueInfo,
       "ruckusZDWLANRogueTable": ruckusZDWLANRogueTable,
       "ruckusZDWLANRogueEntry": ruckusZDWLANRogueEntry,
       "ruckusZDWLANRogueMacAddr": ruckusZDWLANRogueMacAddr,
       "ruckusZDWLANRogueSSID": ruckusZDWLANRogueSSID,
       "ruckusZDWLANRogueRadioType": ruckusZDWLANRogueRadioType,
       "ruckusZDWLANRogueChannel": ruckusZDWLANRogueChannel,
       "ruckusZDWLANRogueRSSI": ruckusZDWLANRogueRSSI,
       "ruckusZDWLANRogueType": ruckusZDWLANRogueType,
       "ruckusZDWLANRogueEncrypted": ruckusZDWLANRogueEncrypted,
       "ruckusZDWLANRogueSignalStrength": ruckusZDWLANRogueSignalStrength}
)
