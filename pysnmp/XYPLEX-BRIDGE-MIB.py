# SNMP MIB module (XYPLEX-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYPLEX-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:42 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Xyplex_ObjectIdentity = ObjectIdentity
xyplex = _Xyplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33)
)
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 5)
)
_Brsys_ObjectIdentity = ObjectIdentity
brsys = _Brsys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 5, 1)
)


class _BrsysName_Type(DisplayString):
    """Custom type brsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrsysName_Type.__name__ = "DisplayString"
_BrsysName_Object = MibScalar
brsysName = _BrsysName_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 1, 1),
    _BrsysName_Type()
)
brsysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brsysName.setStatus("mandatory")
_BrsysMacAddress_Type = OctetString
_BrsysMacAddress_Object = MibScalar
brsysMacAddress = _BrsysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 1, 2),
    _BrsysMacAddress_Type()
)
brsysMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brsysMacAddress.setStatus("mandatory")
_BrsysUpTime_Type = TimeTicks
_BrsysUpTime_Object = MibScalar
brsysUpTime = _BrsysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 1, 3),
    _BrsysUpTime_Type()
)
brsysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brsysUpTime.setStatus("mandatory")


class _BrsysLatEnhance_Type(Integer32):
    """Custom type brsysLatEnhance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BrsysLatEnhance_Type.__name__ = "Integer32"
_BrsysLatEnhance_Object = MibScalar
brsysLatEnhance = _BrsysLatEnhance_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 1, 4),
    _BrsysLatEnhance_Type()
)
brsysLatEnhance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brsysLatEnhance.setStatus("mandatory")
_BrsysLatAnnceCompTblSize_Type = Integer32
_BrsysLatAnnceCompTblSize_Object = MibScalar
brsysLatAnnceCompTblSize = _BrsysLatAnnceCompTblSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 1, 5),
    _BrsysLatAnnceCompTblSize_Type()
)
brsysLatAnnceCompTblSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brsysLatAnnceCompTblSize.setStatus("mandatory")
_BrsysPcktCompTblSize_Type = Integer32
_BrsysPcktCompTblSize_Object = MibScalar
brsysPcktCompTblSize = _BrsysPcktCompTblSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 1, 6),
    _BrsysPcktCompTblSize_Type()
)
brsysPcktCompTblSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brsysPcktCompTblSize.setStatus("mandatory")
_BrsysForwardQueueDisc_Type = Counter32
_BrsysForwardQueueDisc_Object = MibScalar
brsysForwardQueueDisc = _BrsysForwardQueueDisc_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 1, 7),
    _BrsysForwardQueueDisc_Type()
)
brsysForwardQueueDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brsysForwardQueueDisc.setStatus("mandatory")
_BrsysLocalQueueDisc_Type = Counter32
_BrsysLocalQueueDisc_Object = MibScalar
brsysLocalQueueDisc = _BrsysLocalQueueDisc_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 1, 8),
    _BrsysLocalQueueDisc_Type()
)
brsysLocalQueueDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brsysLocalQueueDisc.setStatus("mandatory")
_BrsysVitalinkMacAddress_Type = OctetString
_BrsysVitalinkMacAddress_Object = MibScalar
brsysVitalinkMacAddress = _BrsysVitalinkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 1, 9),
    _BrsysVitalinkMacAddress_Type()
)
brsysVitalinkMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brsysVitalinkMacAddress.setStatus("mandatory")
_BrsysLatAnnceCompTblUseSize_Type = Gauge32
_BrsysLatAnnceCompTblUseSize_Object = MibScalar
brsysLatAnnceCompTblUseSize = _BrsysLatAnnceCompTblUseSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 1, 10),
    _BrsysLatAnnceCompTblUseSize_Type()
)
brsysLatAnnceCompTblUseSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brsysLatAnnceCompTblUseSize.setStatus("mandatory")
_BrsysLatAnnceCompTblUseHigh_Type = Gauge32
_BrsysLatAnnceCompTblUseHigh_Object = MibScalar
brsysLatAnnceCompTblUseHigh = _BrsysLatAnnceCompTblUseHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 1, 11),
    _BrsysLatAnnceCompTblUseHigh_Type()
)
brsysLatAnnceCompTblUseHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brsysLatAnnceCompTblUseHigh.setStatus("mandatory")
_BrsysPcktCompTblUseSize_Type = Gauge32
_BrsysPcktCompTblUseSize_Object = MibScalar
brsysPcktCompTblUseSize = _BrsysPcktCompTblUseSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 1, 12),
    _BrsysPcktCompTblUseSize_Type()
)
brsysPcktCompTblUseSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brsysPcktCompTblUseSize.setStatus("mandatory")
_BrsysPcktCompTblUseHigh_Type = Gauge32
_BrsysPcktCompTblUseHigh_Object = MibScalar
brsysPcktCompTblUseHigh = _BrsysPcktCompTblUseHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 1, 13),
    _BrsysPcktCompTblUseHigh_Type()
)
brsysPcktCompTblUseHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brsysPcktCompTblUseHigh.setStatus("mandatory")
_Stp_ObjectIdentity = ObjectIdentity
stp = _Stp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 5, 2)
)


class _StpStp_Type(Integer32):
    """Custom type stpStp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_StpStp_Type.__name__ = "Integer32"
_StpStp_Object = MibScalar
stpStp = _StpStp_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 1),
    _StpStp_Type()
)
stpStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpStp.setStatus("mandatory")


class _StpForwardTimer_Type(Integer32):
    """Custom type stpForwardTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_StpForwardTimer_Type.__name__ = "Integer32"
_StpForwardTimer_Object = MibScalar
stpForwardTimer = _StpForwardTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 2),
    _StpForwardTimer_Type()
)
stpForwardTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpForwardTimer.setStatus("mandatory")


class _StpHelloTimer_Type(Integer32):
    """Custom type stpHelloTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_StpHelloTimer_Type.__name__ = "Integer32"
_StpHelloTimer_Object = MibScalar
stpHelloTimer = _StpHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 3),
    _StpHelloTimer_Type()
)
stpHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpHelloTimer.setStatus("mandatory")


class _StpMaxAgeTimer_Type(Integer32):
    """Custom type stpMaxAgeTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_StpMaxAgeTimer_Type.__name__ = "Integer32"
_StpMaxAgeTimer_Object = MibScalar
stpMaxAgeTimer = _StpMaxAgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 4),
    _StpMaxAgeTimer_Type()
)
stpMaxAgeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpMaxAgeTimer.setStatus("mandatory")
_StpMulticastAddress_Type = OctetString
_StpMulticastAddress_Object = MibScalar
stpMulticastAddress = _StpMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 5),
    _StpMulticastAddress_Type()
)
stpMulticastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpMulticastAddress.setStatus("mandatory")


class _StpPriority_Type(Integer32):
    """Custom type stpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StpPriority_Type.__name__ = "Integer32"
_StpPriority_Object = MibScalar
stpPriority = _StpPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 6),
    _StpPriority_Type()
)
stpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPriority.setStatus("mandatory")
_StpTopChngTimer_Type = Integer32
_StpTopChngTimer_Object = MibScalar
stpTopChngTimer = _StpTopChngTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 7),
    _StpTopChngTimer_Type()
)
stpTopChngTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpTopChngTimer.setStatus("mandatory")
_StpDesigRoot_Type = OctetString
_StpDesigRoot_Object = MibScalar
stpDesigRoot = _StpDesigRoot_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 8),
    _StpDesigRoot_Type()
)
stpDesigRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpDesigRoot.setStatus("mandatory")
_StpDesigRootCost_Type = Integer32
_StpDesigRootCost_Object = MibScalar
stpDesigRootCost = _StpDesigRootCost_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 9),
    _StpDesigRootCost_Type()
)
stpDesigRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpDesigRootCost.setStatus("mandatory")
_StpDesigForwardTimer_Type = Integer32
_StpDesigForwardTimer_Object = MibScalar
stpDesigForwardTimer = _StpDesigForwardTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 10),
    _StpDesigForwardTimer_Type()
)
stpDesigForwardTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpDesigForwardTimer.setStatus("mandatory")
_StpDesigHelloTimer_Type = Integer32
_StpDesigHelloTimer_Object = MibScalar
stpDesigHelloTimer = _StpDesigHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 11),
    _StpDesigHelloTimer_Type()
)
stpDesigHelloTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpDesigHelloTimer.setStatus("mandatory")
_StpDesigMaxAgeTimer_Type = Integer32
_StpDesigMaxAgeTimer_Object = MibScalar
stpDesigMaxAgeTimer = _StpDesigMaxAgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 12),
    _StpDesigMaxAgeTimer_Type()
)
stpDesigMaxAgeTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpDesigMaxAgeTimer.setStatus("mandatory")
_StpDesigRootLink_Type = Integer32
_StpDesigRootLink_Object = MibScalar
stpDesigRootLink = _StpDesigRootLink_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 13),
    _StpDesigRootLink_Type()
)
stpDesigRootLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpDesigRootLink.setStatus("mandatory")
_StpDesigRootPriority_Type = Integer32
_StpDesigRootPriority_Object = MibScalar
stpDesigRootPriority = _StpDesigRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 14),
    _StpDesigRootPriority_Type()
)
stpDesigRootPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpDesigRootPriority.setStatus("mandatory")
_StpTopChngCount_Type = Gauge32
_StpTopChngCount_Object = MibScalar
stpTopChngCount = _StpTopChngCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 15),
    _StpTopChngCount_Type()
)
stpTopChngCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpTopChngCount.setStatus("mandatory")
_StpTopStableTime_Type = TimeTicks
_StpTopStableTime_Object = MibScalar
stpTopStableTime = _StpTopStableTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 16),
    _StpTopStableTime_Type()
)
stpTopStableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpTopStableTime.setStatus("mandatory")


class _StpTopState_Type(Integer32):
    """Custom type stpTopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changing", 2),
          ("stable", 1))
    )


_StpTopState_Type.__name__ = "Integer32"
_StpTopState_Object = MibScalar
stpTopState = _StpTopState_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 17),
    _StpTopState_Type()
)
stpTopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpTopState.setStatus("mandatory")
_StpNumLinks_Type = Counter32
_StpNumLinks_Object = MibScalar
stpNumLinks = _StpNumLinks_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 18),
    _StpNumLinks_Type()
)
stpNumLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpNumLinks.setStatus("mandatory")
_StpLinkTbl_Object = MibTable
stpLinkTbl = _StpLinkTbl_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 19)
)
if mibBuilder.loadTexts:
    stpLinkTbl.setStatus("mandatory")
_StpLinkTblEnt_Object = MibTableRow
stpLinkTblEnt = _StpLinkTblEnt_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 19, 1)
)
if mibBuilder.loadTexts:
    stpLinkTblEnt.setStatus("mandatory")
_StpLinkID_Type = Integer32
_StpLinkID_Object = MibTableColumn
stpLinkID = _StpLinkID_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 19, 1, 1),
    _StpLinkID_Type()
)
stpLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpLinkID.setStatus("mandatory")
_StpLinkMacAddress_Type = OctetString
_StpLinkMacAddress_Object = MibTableColumn
stpLinkMacAddress = _StpLinkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 19, 1, 2),
    _StpLinkMacAddress_Type()
)
stpLinkMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpLinkMacAddress.setStatus("mandatory")


class _StpLinkpriority_Type(Integer32):
    """Custom type stpLinkpriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StpLinkpriority_Type.__name__ = "Integer32"
_StpLinkpriority_Object = MibScalar
stpLinkpriority = _StpLinkpriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 19, 1, 3),
    _StpLinkpriority_Type()
)
stpLinkpriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpLinkpriority.setStatus("mandatory")


class _StpLinkPathcost_Type(Integer32):
    """Custom type stpLinkPathcost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_StpLinkPathcost_Type.__name__ = "Integer32"
_StpLinkPathcost_Object = MibTableColumn
stpLinkPathcost = _StpLinkPathcost_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 19, 1, 4),
    _StpLinkPathcost_Type()
)
stpLinkPathcost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpLinkPathcost.setStatus("mandatory")
_StpLinkPathcostCur_Type = Integer32
_StpLinkPathcostCur_Object = MibTableColumn
stpLinkPathcostCur = _StpLinkPathcostCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 19, 1, 5),
    _StpLinkPathcostCur_Type()
)
stpLinkPathcostCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpLinkPathcostCur.setStatus("mandatory")


class _StpLinkPathcostWeighted_Type(Integer32):
    """Custom type stpLinkPathcostWeighted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_StpLinkPathcostWeighted_Type.__name__ = "Integer32"
_StpLinkPathcostWeighted_Object = MibTableColumn
stpLinkPathcostWeighted = _StpLinkPathcostWeighted_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 19, 1, 6),
    _StpLinkPathcostWeighted_Type()
)
stpLinkPathcostWeighted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpLinkPathcostWeighted.setStatus("mandatory")


class _StpLinkState_Type(Integer32):
    """Custom type stpLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 2),
          ("disabled", 1),
          ("forwarding", 3),
          ("learning", 4),
          ("listening", 5))
    )


_StpLinkState_Type.__name__ = "Integer32"
_StpLinkState_Object = MibTableColumn
stpLinkState = _StpLinkState_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 19, 1, 7),
    _StpLinkState_Type()
)
stpLinkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpLinkState.setStatus("mandatory")
_StpLinkDesigRoot_Type = OctetString
_StpLinkDesigRoot_Object = MibTableColumn
stpLinkDesigRoot = _StpLinkDesigRoot_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 19, 1, 8),
    _StpLinkDesigRoot_Type()
)
stpLinkDesigRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpLinkDesigRoot.setStatus("mandatory")
_StpLinkDesigCost_Type = Integer32
_StpLinkDesigCost_Object = MibTableColumn
stpLinkDesigCost = _StpLinkDesigCost_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 19, 1, 9),
    _StpLinkDesigCost_Type()
)
stpLinkDesigCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpLinkDesigCost.setStatus("mandatory")
_StpLinkDesigBridge_Type = OctetString
_StpLinkDesigBridge_Object = MibTableColumn
stpLinkDesigBridge = _StpLinkDesigBridge_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 19, 1, 10),
    _StpLinkDesigBridge_Type()
)
stpLinkDesigBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpLinkDesigBridge.setStatus("mandatory")
_StpLinkDesigLink_Type = Integer32
_StpLinkDesigLink_Object = MibTableColumn
stpLinkDesigLink = _StpLinkDesigLink_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 19, 1, 11),
    _StpLinkDesigLink_Type()
)
stpLinkDesigLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpLinkDesigLink.setStatus("mandatory")


class _StpLinkTopChngAck_Type(Integer32):
    """Custom type stpLinkTopChngAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 2),
          ("notAcknowledged", 1))
    )


_StpLinkTopChngAck_Type.__name__ = "Integer32"
_StpLinkTopChngAck_Object = MibTableColumn
stpLinkTopChngAck = _StpLinkTopChngAck_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 19, 1, 12),
    _StpLinkTopChngAck_Type()
)
stpLinkTopChngAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpLinkTopChngAck.setStatus("mandatory")
_StpMaxForwardDelay_Type = Integer32
_StpMaxForwardDelay_Object = MibScalar
stpMaxForwardDelay = _StpMaxForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 20),
    _StpMaxForwardDelay_Type()
)
stpMaxForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpMaxForwardDelay.setStatus("mandatory")
_StpMaxMultiForwardDelay_Type = Integer32
_StpMaxMultiForwardDelay_Object = MibScalar
stpMaxMultiForwardDelay = _StpMaxMultiForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 21),
    _StpMaxMultiForwardDelay_Type()
)
stpMaxMultiForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpMaxMultiForwardDelay.setStatus("mandatory")


class _StpEarlyLoopDetection_Type(Integer32):
    """Custom type stpEarlyLoopDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_StpEarlyLoopDetection_Type.__name__ = "Integer32"
_StpEarlyLoopDetection_Object = MibScalar
stpEarlyLoopDetection = _StpEarlyLoopDetection_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 22),
    _StpEarlyLoopDetection_Type()
)
stpEarlyLoopDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpEarlyLoopDetection.setStatus("mandatory")
_StpEarlyLoopCount_Type = Counter32
_StpEarlyLoopCount_Object = MibScalar
stpEarlyLoopCount = _StpEarlyLoopCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 2, 23),
    _StpEarlyLoopCount_Type()
)
stpEarlyLoopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpEarlyLoopCount.setStatus("mandatory")
_Fl_ObjectIdentity = ObjectIdentity
fl = _Fl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 5, 3)
)


class _FlFiltering_Type(Integer32):
    """Custom type flFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_FlFiltering_Type.__name__ = "Integer32"
_FlFiltering_Object = MibScalar
flFiltering = _FlFiltering_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 1),
    _FlFiltering_Type()
)
flFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flFiltering.setStatus("mandatory")


class _FlTableSize_Type(Integer32):
    """Custom type flTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 4000),
    )


_FlTableSize_Type.__name__ = "Integer32"
_FlTableSize_Object = MibScalar
flTableSize = _FlTableSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 2),
    _FlTableSize_Type()
)
flTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flTableSize.setStatus("mandatory")


class _FlDiscardTimeout_Type(Integer32):
    """Custom type flDiscardTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FlDiscardTimeout_Type.__name__ = "Integer32"
_FlDiscardTimeout_Object = MibScalar
flDiscardTimeout = _FlDiscardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 3),
    _FlDiscardTimeout_Type()
)
flDiscardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDiscardTimeout.setStatus("mandatory")


class _FlUseTimeout_Type(Integer32):
    """Custom type flUseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FlUseTimeout_Type.__name__ = "Integer32"
_FlUseTimeout_Object = MibScalar
flUseTimeout = _FlUseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 4),
    _FlUseTimeout_Type()
)
flUseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flUseTimeout.setStatus("mandatory")
_FlSrcNumSourceCur_Type = Gauge32
_FlSrcNumSourceCur_Object = MibScalar
flSrcNumSourceCur = _FlSrcNumSourceCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 5),
    _FlSrcNumSourceCur_Type()
)
flSrcNumSourceCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSrcNumSourceCur.setStatus("mandatory")
_FlSrcNumSourceHigh_Type = Gauge32
_FlSrcNumSourceHigh_Object = MibScalar
flSrcNumSourceHigh = _FlSrcNumSourceHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 6),
    _FlSrcNumSourceHigh_Type()
)
flSrcNumSourceHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSrcNumSourceHigh.setStatus("mandatory")
_FlSrcNumSourceMax_Type = Gauge32
_FlSrcNumSourceMax_Object = MibScalar
flSrcNumSourceMax = _FlSrcNumSourceMax_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 7),
    _FlSrcNumSourceMax_Type()
)
flSrcNumSourceMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSrcNumSourceMax.setStatus("mandatory")
_FlSrcFilterTbl_Object = MibTable
flSrcFilterTbl = _FlSrcFilterTbl_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 8)
)
if mibBuilder.loadTexts:
    flSrcFilterTbl.setStatus("mandatory")
_FlSrcFilterTblEnt_Object = MibTableRow
flSrcFilterTblEnt = _FlSrcFilterTblEnt_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 8, 1)
)
if mibBuilder.loadTexts:
    flSrcFilterTblEnt.setStatus("mandatory")
_FlSrcEntID_Type = Integer32
_FlSrcEntID_Object = MibTableColumn
flSrcEntID = _FlSrcEntID_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 8, 1, 1),
    _FlSrcEntID_Type()
)
flSrcEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSrcEntID.setStatus("mandatory")
_FlSrcEntMacAddress_Type = OctetString
_FlSrcEntMacAddress_Object = MibTableColumn
flSrcEntMacAddress = _FlSrcEntMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 8, 1, 2),
    _FlSrcEntMacAddress_Type()
)
flSrcEntMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSrcEntMacAddress.setStatus("mandatory")


class _FlSrcEntForwardFlag_Type(Integer32):
    """Custom type flSrcEntForwardFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_FlSrcEntForwardFlag_Type.__name__ = "Integer32"
_FlSrcEntForwardFlag_Object = MibTableColumn
flSrcEntForwardFlag = _FlSrcEntForwardFlag_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 8, 1, 3),
    _FlSrcEntForwardFlag_Type()
)
flSrcEntForwardFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSrcEntForwardFlag.setStatus("mandatory")
_FlSrcEntUseCount_Type = Counter32
_FlSrcEntUseCount_Object = MibTableColumn
flSrcEntUseCount = _FlSrcEntUseCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 8, 1, 4),
    _FlSrcEntUseCount_Type()
)
flSrcEntUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSrcEntUseCount.setStatus("mandatory")
_FlDstInactiveNumCur_Type = Gauge32
_FlDstInactiveNumCur_Object = MibScalar
flDstInactiveNumCur = _FlDstInactiveNumCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 9),
    _FlDstInactiveNumCur_Type()
)
flDstInactiveNumCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDstInactiveNumCur.setStatus("mandatory")
_FlDstInactiveNumHigh_Type = Gauge32
_FlDstInactiveNumHigh_Object = MibScalar
flDstInactiveNumHigh = _FlDstInactiveNumHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 10),
    _FlDstInactiveNumHigh_Type()
)
flDstInactiveNumHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDstInactiveNumHigh.setStatus("mandatory")
_FlDstInactiveNumMax_Type = Gauge32
_FlDstInactiveNumMax_Object = MibScalar
flDstInactiveNumMax = _FlDstInactiveNumMax_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 11),
    _FlDstInactiveNumMax_Type()
)
flDstInactiveNumMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDstInactiveNumMax.setStatus("mandatory")
_FlDstLearnedNumCur_Type = Gauge32
_FlDstLearnedNumCur_Object = MibScalar
flDstLearnedNumCur = _FlDstLearnedNumCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 12),
    _FlDstLearnedNumCur_Type()
)
flDstLearnedNumCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDstLearnedNumCur.setStatus("mandatory")
_FlDstLearnedNumHigh_Type = Gauge32
_FlDstLearnedNumHigh_Object = MibScalar
flDstLearnedNumHigh = _FlDstLearnedNumHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 13),
    _FlDstLearnedNumHigh_Type()
)
flDstLearnedNumHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDstLearnedNumHigh.setStatus("mandatory")
_FlDstLearnedNumMax_Type = Gauge32
_FlDstLearnedNumMax_Object = MibScalar
flDstLearnedNumMax = _FlDstLearnedNumMax_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 14),
    _FlDstLearnedNumMax_Type()
)
flDstLearnedNumMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDstLearnedNumMax.setStatus("mandatory")
_FlDstLearnedNumErrors_Type = Counter32
_FlDstLearnedNumErrors_Object = MibScalar
flDstLearnedNumErrors = _FlDstLearnedNumErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 15),
    _FlDstLearnedNumErrors_Type()
)
flDstLearnedNumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDstLearnedNumErrors.setStatus("mandatory")
_FlDstStaticNumCur_Type = Gauge32
_FlDstStaticNumCur_Object = MibScalar
flDstStaticNumCur = _FlDstStaticNumCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 16),
    _FlDstStaticNumCur_Type()
)
flDstStaticNumCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDstStaticNumCur.setStatus("mandatory")
_FlDstStaticNumHigh_Type = Gauge32
_FlDstStaticNumHigh_Object = MibScalar
flDstStaticNumHigh = _FlDstStaticNumHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 17),
    _FlDstStaticNumHigh_Type()
)
flDstStaticNumHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDstStaticNumHigh.setStatus("mandatory")
_FlDstStaticNumMax_Type = Gauge32
_FlDstStaticNumMax_Object = MibScalar
flDstStaticNumMax = _FlDstStaticNumMax_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 18),
    _FlDstStaticNumMax_Type()
)
flDstStaticNumMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDstStaticNumMax.setStatus("mandatory")
_FlDstFilterTbl_Object = MibTable
flDstFilterTbl = _FlDstFilterTbl_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 19)
)
if mibBuilder.loadTexts:
    flDstFilterTbl.setStatus("mandatory")
_FlDstFilterTblEnt_Object = MibTableRow
flDstFilterTblEnt = _FlDstFilterTblEnt_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 19, 1)
)
if mibBuilder.loadTexts:
    flDstFilterTblEnt.setStatus("mandatory")
_FlDstEntID_Type = Integer32
_FlDstEntID_Object = MibTableColumn
flDstEntID = _FlDstEntID_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 19, 1, 1),
    _FlDstEntID_Type()
)
flDstEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDstEntID.setStatus("mandatory")
_FlDstEntMacAddress_Type = OctetString
_FlDstEntMacAddress_Object = MibTableColumn
flDstEntMacAddress = _FlDstEntMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 19, 1, 2),
    _FlDstEntMacAddress_Type()
)
flDstEntMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDstEntMacAddress.setStatus("mandatory")
_FlDstEntLinkMap_Type = OctetString
_FlDstEntLinkMap_Object = MibTableColumn
flDstEntLinkMap = _FlDstEntLinkMap_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 19, 1, 3),
    _FlDstEntLinkMap_Type()
)
flDstEntLinkMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDstEntLinkMap.setStatus("mandatory")


class _FlDstEntStatus_Type(Integer32):
    """Custom type flDstEntStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 3),
          ("learned", 2),
          ("static", 1))
    )


_FlDstEntStatus_Type.__name__ = "Integer32"
_FlDstEntStatus_Object = MibTableColumn
flDstEntStatus = _FlDstEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 19, 1, 4),
    _FlDstEntStatus_Type()
)
flDstEntStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDstEntStatus.setStatus("mandatory")
_FlDstEntTtl_Type = Gauge32
_FlDstEntTtl_Object = MibTableColumn
flDstEntTtl = _FlDstEntTtl_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 19, 1, 5),
    _FlDstEntTtl_Type()
)
flDstEntTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDstEntTtl.setStatus("mandatory")
_FlDstEntUseCount_Type = Counter32
_FlDstEntUseCount_Object = MibTableColumn
flDstEntUseCount = _FlDstEntUseCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 19, 1, 6),
    _FlDstEntUseCount_Type()
)
flDstEntUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDstEntUseCount.setStatus("mandatory")
_FlLinkTbl_Object = MibTable
flLinkTbl = _FlLinkTbl_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 20)
)
if mibBuilder.loadTexts:
    flLinkTbl.setStatus("mandatory")
_FlLinkTblEnt_Object = MibTableRow
flLinkTblEnt = _FlLinkTblEnt_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 20, 1)
)
if mibBuilder.loadTexts:
    flLinkTblEnt.setStatus("mandatory")
_FlLinkEntID_Type = Integer32
_FlLinkEntID_Object = MibTableColumn
flLinkEntID = _FlLinkEntID_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 20, 1, 1),
    _FlLinkEntID_Type()
)
flLinkEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLinkEntID.setStatus("mandatory")


class _FlLinkEntLearning_Type(Integer32):
    """Custom type flLinkEntLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_FlLinkEntLearning_Type.__name__ = "Integer32"
_FlLinkEntLearning_Object = MibTableColumn
flLinkEntLearning = _FlLinkEntLearning_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 3, 20, 1, 2),
    _FlLinkEntLearning_Type()
)
flLinkEntLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLinkEntLearning.setStatus("mandatory")
_Prtcl_ObjectIdentity = ObjectIdentity
prtcl = _Prtcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 5, 4)
)


class _PrtclProtocol_Type(Integer32):
    """Custom type prtclProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PrtclProtocol_Type.__name__ = "Integer32"
_PrtclProtocol_Object = MibScalar
prtclProtocol = _PrtclProtocol_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 4, 1),
    _PrtclProtocol_Type()
)
prtclProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtclProtocol.setStatus("mandatory")
_PrtclNumCur_Type = Gauge32
_PrtclNumCur_Object = MibScalar
prtclNumCur = _PrtclNumCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 4, 2),
    _PrtclNumCur_Type()
)
prtclNumCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtclNumCur.setStatus("mandatory")
_PrtclNumMax_Type = Gauge32
_PrtclNumMax_Object = MibScalar
prtclNumMax = _PrtclNumMax_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 4, 3),
    _PrtclNumMax_Type()
)
prtclNumMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtclNumMax.setStatus("mandatory")
_PrtclTbl_Object = MibTable
prtclTbl = _PrtclTbl_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 4, 4)
)
if mibBuilder.loadTexts:
    prtclTbl.setStatus("mandatory")
_PrtclTblEnt_Object = MibTableRow
prtclTblEnt = _PrtclTblEnt_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 4, 4, 1)
)
if mibBuilder.loadTexts:
    prtclTblEnt.setStatus("mandatory")
_PrtclEntID_Type = Integer32
_PrtclEntID_Object = MibTableColumn
prtclEntID = _PrtclEntID_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 4, 4, 1, 1),
    _PrtclEntID_Type()
)
prtclEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtclEntID.setStatus("mandatory")
_PrtclEntProtocolID_Type = Integer32
_PrtclEntProtocolID_Object = MibTableColumn
prtclEntProtocolID = _PrtclEntProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 4, 4, 1, 2),
    _PrtclEntProtocolID_Type()
)
prtclEntProtocolID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtclEntProtocolID.setStatus("mandatory")


class _PrtclEntMac_Type(Integer32):
    """Custom type prtclEntMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac", 2),
          ("non-Mac", 1))
    )


_PrtclEntMac_Type.__name__ = "Integer32"
_PrtclEntMac_Object = MibTableColumn
prtclEntMac = _PrtclEntMac_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 4, 4, 1, 3),
    _PrtclEntMac_Type()
)
prtclEntMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtclEntMac.setStatus("mandatory")


class _PrtclEntName_Type(DisplayString):
    """Custom type prtclEntName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_PrtclEntName_Type.__name__ = "DisplayString"
_PrtclEntName_Object = MibTableColumn
prtclEntName = _PrtclEntName_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 4, 4, 1, 4),
    _PrtclEntName_Type()
)
prtclEntName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtclEntName.setStatus("mandatory")


class _PrtclEntPriority_Type(Integer32):
    """Custom type prtclEntPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              101)
        )
    )
    namedValues = NamedValues(
        *(("discard", 101),
          ("high", 5),
          ("low", 1),
          ("medium", 3))
    )


_PrtclEntPriority_Type.__name__ = "Integer32"
_PrtclEntPriority_Object = MibTableColumn
prtclEntPriority = _PrtclEntPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 4, 4, 1, 5),
    _PrtclEntPriority_Type()
)
prtclEntPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtclEntPriority.setStatus("mandatory")
_PrtclEntUseCount_Type = Counter32
_PrtclEntUseCount_Object = MibTableColumn
prtclEntUseCount = _PrtclEntUseCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 4, 4, 1, 6),
    _PrtclEntUseCount_Type()
)
prtclEntUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtclEntUseCount.setStatus("mandatory")


class _PrtclDefaultPriority_Type(Integer32):
    """Custom type prtclDefaultPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              101)
        )
    )
    namedValues = NamedValues(
        *(("discard", 101),
          ("high", 5),
          ("low", 1),
          ("medium", 3))
    )


_PrtclDefaultPriority_Type.__name__ = "Integer32"
_PrtclDefaultPriority_Object = MibScalar
prtclDefaultPriority = _PrtclDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 4, 5),
    _PrtclDefaultPriority_Type()
)
prtclDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtclDefaultPriority.setStatus("mandatory")
_PrtclDefaultUseCount_Type = Counter32
_PrtclDefaultUseCount_Object = MibScalar
prtclDefaultUseCount = _PrtclDefaultUseCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 4, 6),
    _PrtclDefaultUseCount_Type()
)
prtclDefaultUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtclDefaultUseCount.setStatus("mandatory")
_Lks_ObjectIdentity = ObjectIdentity
lks = _Lks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 5, 5)
)
_LksNum_Type = Counter32
_LksNum_Object = MibScalar
lksNum = _LksNum_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 1),
    _LksNum_Type()
)
lksNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksNum.setStatus("mandatory")
_LksTbl_Object = MibTable
lksTbl = _LksTbl_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2)
)
if mibBuilder.loadTexts:
    lksTbl.setStatus("mandatory")
_LksTblEnt_Object = MibTableRow
lksTblEnt = _LksTblEnt_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1)
)
if mibBuilder.loadTexts:
    lksTblEnt.setStatus("mandatory")
_LksEntID_Type = Integer32
_LksEntID_Object = MibTableColumn
lksEntID = _LksEntID_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 1),
    _LksEntID_Type()
)
lksEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntID.setStatus("mandatory")


class _LksEntStateConfig_Type(Integer32):
    """Custom type lksEntStateConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("standby", 3))
    )


_LksEntStateConfig_Type.__name__ = "Integer32"
_LksEntStateConfig_Object = MibTableColumn
lksEntStateConfig = _LksEntStateConfig_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 2),
    _LksEntStateConfig_Type()
)
lksEntStateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lksEntStateConfig.setStatus("mandatory")


class _LksEntStateActive_Type(Integer32):
    """Custom type lksEntStateActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              136,
              138,
              139,
              140)
        )
    )
    namedValues = NamedValues(
        *(("down", 135),
          ("down1", 132),
          ("initWait", 130),
          ("initWaitDSR", 129),
          ("loop", 136),
          ("purging", 136),
          ("purging1", 133),
          ("running", 134),
          ("running1", 131),
          ("testLoop", 140),
          ("testReceive", 139),
          ("testSend", 138))
    )


_LksEntStateActive_Type.__name__ = "Integer32"
_LksEntStateActive_Object = MibTableColumn
lksEntStateActive = _LksEntStateActive_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 3),
    _LksEntStateActive_Type()
)
lksEntStateActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntStateActive.setStatus("mandatory")


class _LksEntType_Type(Integer32):
    """Custom type lksEntType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("lan", 4),
          ("unknown", 1),
          ("wan", 3))
    )


_LksEntType_Type.__name__ = "Integer32"
_LksEntType_Object = MibTableColumn
lksEntType = _LksEntType_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 4),
    _LksEntType_Type()
)
lksEntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntType.setStatus("mandatory")
_LksEntTypeSpecific_Type = ObjectIdentifier
_LksEntTypeSpecific_Object = MibTableColumn
lksEntTypeSpecific = _LksEntTypeSpecific_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 5),
    _LksEntTypeSpecific_Type()
)
lksEntTypeSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntTypeSpecific.setStatus("mandatory")


class _LksEntName_Type(DisplayString):
    """Custom type lksEntName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_LksEntName_Type.__name__ = "DisplayString"
_LksEntName_Object = MibTableColumn
lksEntName = _LksEntName_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 6),
    _LksEntName_Type()
)
lksEntName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lksEntName.setStatus("mandatory")
_LksEntUtilizationCur_Type = Gauge32
_LksEntUtilizationCur_Object = MibTableColumn
lksEntUtilizationCur = _LksEntUtilizationCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 7),
    _LksEntUtilizationCur_Type()
)
lksEntUtilizationCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntUtilizationCur.setStatus("mandatory")
_LksEntUtilizationHigh_Type = Gauge32
_LksEntUtilizationHigh_Object = MibTableColumn
lksEntUtilizationHigh = _LksEntUtilizationHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 8),
    _LksEntUtilizationHigh_Type()
)
lksEntUtilizationHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntUtilizationHigh.setStatus("mandatory")
_LksEntUtilizationAvg_Type = Gauge32
_LksEntUtilizationAvg_Object = MibTableColumn
lksEntUtilizationAvg = _LksEntUtilizationAvg_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 9),
    _LksEntUtilizationAvg_Type()
)
lksEntUtilizationAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntUtilizationAvg.setStatus("mandatory")
_LksEntForwardingCur_Type = Gauge32
_LksEntForwardingCur_Object = MibTableColumn
lksEntForwardingCur = _LksEntForwardingCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 10),
    _LksEntForwardingCur_Type()
)
lksEntForwardingCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntForwardingCur.setStatus("mandatory")
_LksEntForwardingHigh_Type = Gauge32
_LksEntForwardingHigh_Object = MibTableColumn
lksEntForwardingHigh = _LksEntForwardingHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 11),
    _LksEntForwardingHigh_Type()
)
lksEntForwardingHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntForwardingHigh.setStatus("mandatory")
_LksEntForwardingAvg_Type = Gauge32
_LksEntForwardingAvg_Object = MibTableColumn
lksEntForwardingAvg = _LksEntForwardingAvg_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 12),
    _LksEntForwardingAvg_Type()
)
lksEntForwardingAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntForwardingAvg.setStatus("mandatory")
_LksEntFilteringCur_Type = Gauge32
_LksEntFilteringCur_Object = MibTableColumn
lksEntFilteringCur = _LksEntFilteringCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 13),
    _LksEntFilteringCur_Type()
)
lksEntFilteringCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntFilteringCur.setStatus("mandatory")
_LksEntFilteringHigh_Type = Gauge32
_LksEntFilteringHigh_Object = MibTableColumn
lksEntFilteringHigh = _LksEntFilteringHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 14),
    _LksEntFilteringHigh_Type()
)
lksEntFilteringHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntFilteringHigh.setStatus("mandatory")
_LksEntFilteringAvg_Type = Gauge32
_LksEntFilteringAvg_Object = MibTableColumn
lksEntFilteringAvg = _LksEntFilteringAvg_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 15),
    _LksEntFilteringAvg_Type()
)
lksEntFilteringAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntFilteringAvg.setStatus("mandatory")
_LksEntOutputQCur_Type = Gauge32
_LksEntOutputQCur_Object = MibTableColumn
lksEntOutputQCur = _LksEntOutputQCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 16),
    _LksEntOutputQCur_Type()
)
lksEntOutputQCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntOutputQCur.setStatus("mandatory")
_LksEntOutputQHigh_Type = Gauge32
_LksEntOutputQHigh_Object = MibTableColumn
lksEntOutputQHigh = _LksEntOutputQHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 17),
    _LksEntOutputQHigh_Type()
)
lksEntOutputQHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntOutputQHigh.setStatus("mandatory")
_LksEntOutputQTotal_Type = Gauge32
_LksEntOutputQTotal_Object = MibTableColumn
lksEntOutputQTotal = _LksEntOutputQTotal_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 18),
    _LksEntOutputQTotal_Type()
)
lksEntOutputQTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntOutputQTotal.setStatus("mandatory")
_LksEntTransmitLinkSpeed_Type = Gauge32
_LksEntTransmitLinkSpeed_Object = MibTableColumn
lksEntTransmitLinkSpeed = _LksEntTransmitLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 19),
    _LksEntTransmitLinkSpeed_Type()
)
lksEntTransmitLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntTransmitLinkSpeed.setStatus("mandatory")
_LksEntReceiveLinkSpeed_Type = Gauge32
_LksEntReceiveLinkSpeed_Object = MibTableColumn
lksEntReceiveLinkSpeed = _LksEntReceiveLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 20),
    _LksEntReceiveLinkSpeed_Type()
)
lksEntReceiveLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntReceiveLinkSpeed.setStatus("mandatory")
_LksEntTraffic_ObjectIdentity = ObjectIdentity
lksEntTraffic = _LksEntTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 21)
)
_LksEntTrafficPacketsIn_Type = Counter32
_LksEntTrafficPacketsIn_Object = MibScalar
lksEntTrafficPacketsIn = _LksEntTrafficPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 21, 1),
    _LksEntTrafficPacketsIn_Type()
)
lksEntTrafficPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntTrafficPacketsIn.setStatus("mandatory")
_LksEntTrafficPacketsOut_Type = Counter32
_LksEntTrafficPacketsOut_Object = MibScalar
lksEntTrafficPacketsOut = _LksEntTrafficPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 21, 2),
    _LksEntTrafficPacketsOut_Type()
)
lksEntTrafficPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntTrafficPacketsOut.setStatus("mandatory")
_LksEntTrafficMulticastsIn_Type = Counter32
_LksEntTrafficMulticastsIn_Object = MibScalar
lksEntTrafficMulticastsIn = _LksEntTrafficMulticastsIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 21, 3),
    _LksEntTrafficMulticastsIn_Type()
)
lksEntTrafficMulticastsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntTrafficMulticastsIn.setStatus("mandatory")
_LksEntTrafficMulticastsOut_Type = Counter32
_LksEntTrafficMulticastsOut_Object = MibScalar
lksEntTrafficMulticastsOut = _LksEntTrafficMulticastsOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 21, 4),
    _LksEntTrafficMulticastsOut_Type()
)
lksEntTrafficMulticastsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntTrafficMulticastsOut.setStatus("mandatory")
_LksEntTrafficUnicastsIn_Type = Counter32
_LksEntTrafficUnicastsIn_Object = MibScalar
lksEntTrafficUnicastsIn = _LksEntTrafficUnicastsIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 21, 5),
    _LksEntTrafficUnicastsIn_Type()
)
lksEntTrafficUnicastsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntTrafficUnicastsIn.setStatus("mandatory")
_LksEntTrafficUnicastsOut_Type = Counter32
_LksEntTrafficUnicastsOut_Object = MibScalar
lksEntTrafficUnicastsOut = _LksEntTrafficUnicastsOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 21, 6),
    _LksEntTrafficUnicastsOut_Type()
)
lksEntTrafficUnicastsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntTrafficUnicastsOut.setStatus("mandatory")
_LksEntTrafficStpIn_Type = Counter32
_LksEntTrafficStpIn_Object = MibScalar
lksEntTrafficStpIn = _LksEntTrafficStpIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 21, 7),
    _LksEntTrafficStpIn_Type()
)
lksEntTrafficStpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntTrafficStpIn.setStatus("mandatory")
_LksEntTrafficStpOut_Type = Counter32
_LksEntTrafficStpOut_Object = MibScalar
lksEntTrafficStpOut = _LksEntTrafficStpOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 21, 8),
    _LksEntTrafficStpOut_Type()
)
lksEntTrafficStpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntTrafficStpOut.setStatus("mandatory")
_LksEntTrafficBytesIn_Type = Counter32
_LksEntTrafficBytesIn_Object = MibScalar
lksEntTrafficBytesIn = _LksEntTrafficBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 21, 9),
    _LksEntTrafficBytesIn_Type()
)
lksEntTrafficBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntTrafficBytesIn.setStatus("mandatory")
_LksEntTrafficBytesOut_Type = Counter32
_LksEntTrafficBytesOut_Object = MibScalar
lksEntTrafficBytesOut = _LksEntTrafficBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 21, 10),
    _LksEntTrafficBytesOut_Type()
)
lksEntTrafficBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntTrafficBytesOut.setStatus("mandatory")
_LksEntDiscards_ObjectIdentity = ObjectIdentity
lksEntDiscards = _LksEntDiscards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 22)
)
_LksEntDiscardCrcError_Type = Counter32
_LksEntDiscardCrcError_Object = MibScalar
lksEntDiscardCrcError = _LksEntDiscardCrcError_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 22, 1),
    _LksEntDiscardCrcError_Type()
)
lksEntDiscardCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntDiscardCrcError.setStatus("mandatory")
_LksEntDiscardFiltering_Type = Counter32
_LksEntDiscardFiltering_Object = MibScalar
lksEntDiscardFiltering = _LksEntDiscardFiltering_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 22, 2),
    _LksEntDiscardFiltering_Type()
)
lksEntDiscardFiltering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntDiscardFiltering.setStatus("mandatory")
_LksEntDiscardnoBuffers_Type = Counter32
_LksEntDiscardnoBuffers_Object = MibScalar
lksEntDiscardnoBuffers = _LksEntDiscardnoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 22, 3),
    _LksEntDiscardnoBuffers_Type()
)
lksEntDiscardnoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntDiscardnoBuffers.setStatus("mandatory")
_LksEntDiscardPriority_Type = Counter32
_LksEntDiscardPriority_Object = MibScalar
lksEntDiscardPriority = _LksEntDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 22, 4),
    _LksEntDiscardPriority_Type()
)
lksEntDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntDiscardPriority.setStatus("mandatory")
_LksEntDiscardLatGroupAnnce_Type = Counter32
_LksEntDiscardLatGroupAnnce_Object = MibScalar
lksEntDiscardLatGroupAnnce = _LksEntDiscardLatGroupAnnce_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 22, 5),
    _LksEntDiscardLatGroupAnnce_Type()
)
lksEntDiscardLatGroupAnnce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntDiscardLatGroupAnnce.setStatus("mandatory")
_LksEntDiscardLostBuffers_Type = Counter32
_LksEntDiscardLostBuffers_Object = MibScalar
lksEntDiscardLostBuffers = _LksEntDiscardLostBuffers_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 22, 6),
    _LksEntDiscardLostBuffers_Type()
)
lksEntDiscardLostBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntDiscardLostBuffers.setStatus("mandatory")
_LksEntDiscardOutputQueueFull_Type = Counter32
_LksEntDiscardOutputQueueFull_Object = MibScalar
lksEntDiscardOutputQueueFull = _LksEntDiscardOutputQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 22, 7),
    _LksEntDiscardOutputQueueFull_Type()
)
lksEntDiscardOutputQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntDiscardOutputQueueFull.setStatus("mandatory")
_LksEntDiscardDelayExceeded_Type = Counter32
_LksEntDiscardDelayExceeded_Object = MibScalar
lksEntDiscardDelayExceeded = _LksEntDiscardDelayExceeded_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 5, 2, 1, 22, 8),
    _LksEntDiscardDelayExceeded_Type()
)
lksEntDiscardDelayExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lksEntDiscardDelayExceeded.setStatus("mandatory")
_Wan_ObjectIdentity = ObjectIdentity
wan = _Wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 5, 6)
)
_WanNullClock_Type = Integer32
_WanNullClock_Object = MibScalar
wanNullClock = _WanNullClock_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 1),
    _WanNullClock_Type()
)
wanNullClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanNullClock.setStatus("mandatory")
_WanNum_Type = Counter32
_WanNum_Object = MibScalar
wanNum = _WanNum_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 2),
    _WanNum_Type()
)
wanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanNum.setStatus("mandatory")
_WanTbl_Object = MibTable
wanTbl = _WanTbl_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3)
)
if mibBuilder.loadTexts:
    wanTbl.setStatus("mandatory")
_WanTblEnt_Object = MibTableRow
wanTblEnt = _WanTblEnt_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1)
)
if mibBuilder.loadTexts:
    wanTblEnt.setStatus("mandatory")
_WanEntID_Type = Integer32
_WanEntID_Object = MibTableColumn
wanEntID = _WanEntID_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 1),
    _WanEntID_Type()
)
wanEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntID.setStatus("mandatory")


class _WanEntCompression_Type(Integer32):
    """Custom type wanEntCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              256)
        )
    )
    namedValues = NamedValues(
        *(("auto", 256),
          ("disabled", 2),
          ("enabled", 1))
    )


_WanEntCompression_Type.__name__ = "Integer32"
_WanEntCompression_Object = MibTableColumn
wanEntCompression = _WanEntCompression_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 2),
    _WanEntCompression_Type()
)
wanEntCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanEntCompression.setStatus("mandatory")


class _WanEntDsrTimeout_Type(Integer32):
    """Custom type wanEntDsrTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WanEntDsrTimeout_Type.__name__ = "Integer32"
_WanEntDsrTimeout_Object = MibTableColumn
wanEntDsrTimeout = _WanEntDsrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 3),
    _WanEntDsrTimeout_Type()
)
wanEntDsrTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanEntDsrTimeout.setStatus("mandatory")


class _WanEntLocalPhone_Type(DisplayString):
    """Custom type wanEntLocalPhone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_WanEntLocalPhone_Type.__name__ = "DisplayString"
_WanEntLocalPhone_Object = MibTableColumn
wanEntLocalPhone = _WanEntLocalPhone_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 4),
    _WanEntLocalPhone_Type()
)
wanEntLocalPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanEntLocalPhone.setStatus("mandatory")
_WanEntDialPhoneNumMax_Type = Integer32
_WanEntDialPhoneNumMax_Object = MibTableColumn
wanEntDialPhoneNumMax = _WanEntDialPhoneNumMax_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 5),
    _WanEntDialPhoneNumMax_Type()
)
wanEntDialPhoneNumMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntDialPhoneNumMax.setStatus("mandatory")
_WanEntDialPhoneTbl_Object = MibTable
wanEntDialPhoneTbl = _WanEntDialPhoneTbl_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 6)
)
if mibBuilder.loadTexts:
    wanEntDialPhoneTbl.setStatus("mandatory")
_WanEntDialPhoneEnt_Object = MibTableRow
wanEntDialPhoneEnt = _WanEntDialPhoneEnt_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    wanEntDialPhoneEnt.setStatus("mandatory")
_WanEntDialPhoneEntID_Type = Integer32
_WanEntDialPhoneEntID_Object = MibTableColumn
wanEntDialPhoneEntID = _WanEntDialPhoneEntID_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 6, 1, 1),
    _WanEntDialPhoneEntID_Type()
)
wanEntDialPhoneEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntDialPhoneEntID.setStatus("mandatory")


class _WanEntDialPhoneEntPhone_Type(DisplayString):
    """Custom type wanEntDialPhoneEntPhone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_WanEntDialPhoneEntPhone_Type.__name__ = "DisplayString"
_WanEntDialPhoneEntPhone_Object = MibTableColumn
wanEntDialPhoneEntPhone = _WanEntDialPhoneEntPhone_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 6, 1, 2),
    _WanEntDialPhoneEntPhone_Type()
)
wanEntDialPhoneEntPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanEntDialPhoneEntPhone.setStatus("mandatory")
_WanEntGroups_Type = OctetString
_WanEntGroups_Object = MibTableColumn
wanEntGroups = _WanEntGroups_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 7),
    _WanEntGroups_Type()
)
wanEntGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanEntGroups.setStatus("mandatory")


class _WanEntModemType_Type(Integer32):
    """Custom type wanEntModemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 1),
          ("dialUp", 2))
    )


_WanEntModemType_Type.__name__ = "Integer32"
_WanEntModemType_Object = MibTableColumn
wanEntModemType = _WanEntModemType_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 8),
    _WanEntModemType_Type()
)
wanEntModemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanEntModemType.setStatus("mandatory")


class _WanEntNullClock_Type(Integer32):
    """Custom type wanEntNullClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WanEntNullClock_Type.__name__ = "Integer32"
_WanEntNullClock_Object = MibTableColumn
wanEntNullClock = _WanEntNullClock_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 9),
    _WanEntNullClock_Type()
)
wanEntNullClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanEntNullClock.setStatus("mandatory")


class _WanEntPathcostWeighted_Type(Integer32):
    """Custom type wanEntPathcostWeighted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WanEntPathcostWeighted_Type.__name__ = "Integer32"
_WanEntPathcostWeighted_Object = MibTableColumn
wanEntPathcostWeighted = _WanEntPathcostWeighted_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 10),
    _WanEntPathcostWeighted_Type()
)
wanEntPathcostWeighted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanEntPathcostWeighted.setStatus("mandatory")
_WanEntErrorRateCur_Type = Gauge32
_WanEntErrorRateCur_Object = MibTableColumn
wanEntErrorRateCur = _WanEntErrorRateCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 11),
    _WanEntErrorRateCur_Type()
)
wanEntErrorRateCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntErrorRateCur.setStatus("mandatory")
_WanEntErrorRateHigh_Type = Gauge32
_WanEntErrorRateHigh_Object = MibTableColumn
wanEntErrorRateHigh = _WanEntErrorRateHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 12),
    _WanEntErrorRateHigh_Type()
)
wanEntErrorRateHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntErrorRateHigh.setStatus("mandatory")
_WanEntErrorRateAvg_Type = Gauge32
_WanEntErrorRateAvg_Object = MibTableColumn
wanEntErrorRateAvg = _WanEntErrorRateAvg_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 13),
    _WanEntErrorRateAvg_Type()
)
wanEntErrorRateAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntErrorRateAvg.setStatus("mandatory")
_WanEntLinkDownCur_Type = Gauge32
_WanEntLinkDownCur_Object = MibTableColumn
wanEntLinkDownCur = _WanEntLinkDownCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 14),
    _WanEntLinkDownCur_Type()
)
wanEntLinkDownCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntLinkDownCur.setStatus("mandatory")
_WanEntLinkDownHigh_Type = Gauge32
_WanEntLinkDownHigh_Object = MibTableColumn
wanEntLinkDownHigh = _WanEntLinkDownHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 15),
    _WanEntLinkDownHigh_Type()
)
wanEntLinkDownHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntLinkDownHigh.setStatus("mandatory")
_WanEntLinkDownTotal_Type = Counter32
_WanEntLinkDownTotal_Object = MibTableColumn
wanEntLinkDownTotal = _WanEntLinkDownTotal_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 16),
    _WanEntLinkDownTotal_Type()
)
wanEntLinkDownTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntLinkDownTotal.setStatus("mandatory")
_WanEntLinkDownCount_Type = Counter32
_WanEntLinkDownCount_Object = MibTableColumn
wanEntLinkDownCount = _WanEntLinkDownCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 17),
    _WanEntLinkDownCount_Type()
)
wanEntLinkDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntLinkDownCount.setStatus("mandatory")


class _WanEntCableType_Type(Integer32):
    """Custom type wanEntCableType based on Integer32"""
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
        *(("cable422", 1),
          ("cable423", 2),
          ("cableV35", 3),
          ("unknown", 4))
    )


_WanEntCableType_Type.__name__ = "Integer32"
_WanEntCableType_Object = MibTableColumn
wanEntCableType = _WanEntCableType_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 18),
    _WanEntCableType_Type()
)
wanEntCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntCableType.setStatus("mandatory")


class _WanEntCtsCur_Type(Integer32):
    """Custom type wanEntCtsCur based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("observed", 2))
    )


_WanEntCtsCur_Type.__name__ = "Integer32"
_WanEntCtsCur_Object = MibTableColumn
wanEntCtsCur = _WanEntCtsCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 19),
    _WanEntCtsCur_Type()
)
wanEntCtsCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntCtsCur.setStatus("mandatory")


class _WanEntRtsCur_Type(Integer32):
    """Custom type wanEntRtsCur based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asserted", 2),
          ("no", 1))
    )


_WanEntRtsCur_Type.__name__ = "Integer32"
_WanEntRtsCur_Object = MibTableColumn
wanEntRtsCur = _WanEntRtsCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 20),
    _WanEntRtsCur_Type()
)
wanEntRtsCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntRtsCur.setStatus("mandatory")


class _WanEntDcdCur_Type(Integer32):
    """Custom type wanEntDcdCur based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("observed", 2))
    )


_WanEntDcdCur_Type.__name__ = "Integer32"
_WanEntDcdCur_Object = MibTableColumn
wanEntDcdCur = _WanEntDcdCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 21),
    _WanEntDcdCur_Type()
)
wanEntDcdCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntDcdCur.setStatus("mandatory")


class _WanEntDsrCur_Type(Integer32):
    """Custom type wanEntDsrCur based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("observed", 2))
    )


_WanEntDsrCur_Type.__name__ = "Integer32"
_WanEntDsrCur_Object = MibTableColumn
wanEntDsrCur = _WanEntDsrCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 22),
    _WanEntDsrCur_Type()
)
wanEntDsrCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntDsrCur.setStatus("mandatory")


class _WanEntDtrCur_Type(Integer32):
    """Custom type wanEntDtrCur based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asserted", 2),
          ("no", 1))
    )


_WanEntDtrCur_Type.__name__ = "Integer32"
_WanEntDtrCur_Object = MibTableColumn
wanEntDtrCur = _WanEntDtrCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 23),
    _WanEntDtrCur_Type()
)
wanEntDtrCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntDtrCur.setStatus("mandatory")


class _WanEntRingCur_Type(Integer32):
    """Custom type wanEntRingCur based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("observed", 2))
    )


_WanEntRingCur_Type.__name__ = "Integer32"
_WanEntRingCur_Object = MibTableColumn
wanEntRingCur = _WanEntRingCur_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 24),
    _WanEntRingCur_Type()
)
wanEntRingCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntRingCur.setStatus("mandatory")
_WanEntCtsChanges_Type = Counter32
_WanEntCtsChanges_Object = MibTableColumn
wanEntCtsChanges = _WanEntCtsChanges_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 25),
    _WanEntCtsChanges_Type()
)
wanEntCtsChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntCtsChanges.setStatus("mandatory")
_WanEntRtsChanges_Type = Counter32
_WanEntRtsChanges_Object = MibTableColumn
wanEntRtsChanges = _WanEntRtsChanges_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 26),
    _WanEntRtsChanges_Type()
)
wanEntRtsChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntRtsChanges.setStatus("mandatory")
_WanEntDcdChanges_Type = Counter32
_WanEntDcdChanges_Object = MibTableColumn
wanEntDcdChanges = _WanEntDcdChanges_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 27),
    _WanEntDcdChanges_Type()
)
wanEntDcdChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntDcdChanges.setStatus("mandatory")
_WanEntDsrChanges_Type = Counter32
_WanEntDsrChanges_Object = MibTableColumn
wanEntDsrChanges = _WanEntDsrChanges_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 28),
    _WanEntDsrChanges_Type()
)
wanEntDsrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntDsrChanges.setStatus("mandatory")
_WanEntDtrChanges_Type = Counter32
_WanEntDtrChanges_Object = MibTableColumn
wanEntDtrChanges = _WanEntDtrChanges_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 29),
    _WanEntDtrChanges_Type()
)
wanEntDtrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntDtrChanges.setStatus("mandatory")
_WanEntRingChanges_Type = Counter32
_WanEntRingChanges_Object = MibTableColumn
wanEntRingChanges = _WanEntRingChanges_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 30),
    _WanEntRingChanges_Type()
)
wanEntRingChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntRingChanges.setStatus("mandatory")
_WanEntCompNum_Type = Counter32
_WanEntCompNum_Object = MibTableColumn
wanEntCompNum = _WanEntCompNum_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 31),
    _WanEntCompNum_Type()
)
wanEntCompNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntCompNum.setStatus("mandatory")
_WanEntCompressionTbl_Object = MibTable
wanEntCompressionTbl = _WanEntCompressionTbl_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 32)
)
if mibBuilder.loadTexts:
    wanEntCompressionTbl.setStatus("mandatory")
_WanEntCompEnt_Object = MibTableRow
wanEntCompEnt = _WanEntCompEnt_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 32, 1)
)
if mibBuilder.loadTexts:
    wanEntCompEnt.setStatus("mandatory")
_WanEntCompEntID_Type = Integer32
_WanEntCompEntID_Object = MibTableColumn
wanEntCompEntID = _WanEntCompEntID_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 32, 1, 1),
    _WanEntCompEntID_Type()
)
wanEntCompEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntCompEntID.setStatus("mandatory")
_WanEntCompEntDescription_Type = DisplayString
_WanEntCompEntDescription_Object = MibTableColumn
wanEntCompEntDescription = _WanEntCompEntDescription_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 32, 1, 2),
    _WanEntCompEntDescription_Type()
)
wanEntCompEntDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntCompEntDescription.setStatus("mandatory")
_WanEntCompEntCurrent_Type = Gauge32
_WanEntCompEntCurrent_Object = MibTableColumn
wanEntCompEntCurrent = _WanEntCompEntCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 32, 1, 3),
    _WanEntCompEntCurrent_Type()
)
wanEntCompEntCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntCompEntCurrent.setStatus("mandatory")
_WanEntCompEntHigh_Type = Gauge32
_WanEntCompEntHigh_Object = MibTableColumn
wanEntCompEntHigh = _WanEntCompEntHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 32, 1, 4),
    _WanEntCompEntHigh_Type()
)
wanEntCompEntHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntCompEntHigh.setStatus("mandatory")
_WanEntCompEntAverage_Type = Gauge32
_WanEntCompEntAverage_Object = MibTableColumn
wanEntCompEntAverage = _WanEntCompEntAverage_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 32, 1, 5),
    _WanEntCompEntAverage_Type()
)
wanEntCompEntAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntCompEntAverage.setStatus("mandatory")


class _WanEntCompressionStatus_Type(Integer32):
    """Custom type wanEntCompressionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WanEntCompressionStatus_Type.__name__ = "Integer32"
_WanEntCompressionStatus_Object = MibTableColumn
wanEntCompressionStatus = _WanEntCompressionStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 3, 1, 33),
    _WanEntCompressionStatus_Type()
)
wanEntCompressionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanEntCompressionStatus.setStatus("mandatory")


class _WanVitalinkCompatibility_Type(Integer32):
    """Custom type wanVitalinkCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("enabled", 2))
    )


_WanVitalinkCompatibility_Type.__name__ = "Integer32"
_WanVitalinkCompatibility_Object = MibScalar
wanVitalinkCompatibility = _WanVitalinkCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 6, 4),
    _WanVitalinkCompatibility_Type()
)
wanVitalinkCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanVitalinkCompatibility.setStatus("mandatory")
_Lan_ObjectIdentity = ObjectIdentity
lan = _Lan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 5, 7)
)
_LanNum_Type = Counter32
_LanNum_Object = MibScalar
lanNum = _LanNum_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 7, 1),
    _LanNum_Type()
)
lanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanNum.setStatus("mandatory")
_LanTbl_Object = MibTable
lanTbl = _LanTbl_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 7, 2)
)
if mibBuilder.loadTexts:
    lanTbl.setStatus("mandatory")
_LanTblEnt_Object = MibTableRow
lanTblEnt = _LanTblEnt_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 7, 2, 1)
)
if mibBuilder.loadTexts:
    lanTblEnt.setStatus("mandatory")
_LanEntID_Type = Integer32
_LanEntID_Object = MibTableColumn
lanEntID = _LanEntID_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 7, 2, 1, 1),
    _LanEntID_Type()
)
lanEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanEntID.setStatus("mandatory")
_LanEntShutdownThreshold_Type = Integer32
_LanEntShutdownThreshold_Object = MibTableColumn
lanEntShutdownThreshold = _LanEntShutdownThreshold_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 7, 2, 1, 2),
    _LanEntShutdownThreshold_Type()
)
lanEntShutdownThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanEntShutdownThreshold.setStatus("mandatory")
_LanEntFramingError_Type = Counter32
_LanEntFramingError_Object = MibTableColumn
lanEntFramingError = _LanEntFramingError_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 7, 2, 1, 3),
    _LanEntFramingError_Type()
)
lanEntFramingError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanEntFramingError.setStatus("mandatory")
_LanEntLostPacketsError_Type = Counter32
_LanEntLostPacketsError_Object = MibTableColumn
lanEntLostPacketsError = _LanEntLostPacketsError_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 7, 2, 1, 4),
    _LanEntLostPacketsError_Type()
)
lanEntLostPacketsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanEntLostPacketsError.setStatus("mandatory")
_LanEntMemoryError_Type = Counter32
_LanEntMemoryError_Object = MibTableColumn
lanEntMemoryError = _LanEntMemoryError_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 7, 2, 1, 5),
    _LanEntMemoryError_Type()
)
lanEntMemoryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanEntMemoryError.setStatus("mandatory")
_LanEntOverflowError_Type = Counter32
_LanEntOverflowError_Object = MibTableColumn
lanEntOverflowError = _LanEntOverflowError_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 7, 2, 1, 6),
    _LanEntOverflowError_Type()
)
lanEntOverflowError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanEntOverflowError.setStatus("mandatory")
_LanEntPacketInTooLongError_Type = Counter32
_LanEntPacketInTooLongError_Object = MibTableColumn
lanEntPacketInTooLongError = _LanEntPacketInTooLongError_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 7, 2, 1, 7),
    _LanEntPacketInTooLongError_Type()
)
lanEntPacketInTooLongError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanEntPacketInTooLongError.setStatus("mandatory")
_LanEntCarrierLossError_Type = Counter32
_LanEntCarrierLossError_Object = MibTableColumn
lanEntCarrierLossError = _LanEntCarrierLossError_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 7, 2, 1, 8),
    _LanEntCarrierLossError_Type()
)
lanEntCarrierLossError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanEntCarrierLossError.setStatus("mandatory")
_LanEntHeartbeatFailureError_Type = Counter32
_LanEntHeartbeatFailureError_Object = MibTableColumn
lanEntHeartbeatFailureError = _LanEntHeartbeatFailureError_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 7, 2, 1, 9),
    _LanEntHeartbeatFailureError_Type()
)
lanEntHeartbeatFailureError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanEntHeartbeatFailureError.setStatus("mandatory")
_LanEntLateCollisionError_Type = Counter32
_LanEntLateCollisionError_Object = MibTableColumn
lanEntLateCollisionError = _LanEntLateCollisionError_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 7, 2, 1, 10),
    _LanEntLateCollisionError_Type()
)
lanEntLateCollisionError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanEntLateCollisionError.setStatus("mandatory")
_LanEntPacketOutTooLongError_Type = Counter32
_LanEntPacketOutTooLongError_Object = MibTableColumn
lanEntPacketOutTooLongError = _LanEntPacketOutTooLongError_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 7, 2, 1, 11),
    _LanEntPacketOutTooLongError_Type()
)
lanEntPacketOutTooLongError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanEntPacketOutTooLongError.setStatus("mandatory")
_LanEntRetryExceedError_Type = Counter32
_LanEntRetryExceedError_Object = MibTableColumn
lanEntRetryExceedError = _LanEntRetryExceedError_Object(
    (1, 3, 6, 1, 4, 1, 33, 5, 7, 2, 1, 12),
    _LanEntRetryExceedError_Type()
)
lanEntRetryExceedError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanEntRetryExceedError.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYPLEX-BRIDGE-MIB",
    **{"xyplex": xyplex,
       "bridge": bridge,
       "brsys": brsys,
       "brsysName": brsysName,
       "brsysMacAddress": brsysMacAddress,
       "brsysUpTime": brsysUpTime,
       "brsysLatEnhance": brsysLatEnhance,
       "brsysLatAnnceCompTblSize": brsysLatAnnceCompTblSize,
       "brsysPcktCompTblSize": brsysPcktCompTblSize,
       "brsysForwardQueueDisc": brsysForwardQueueDisc,
       "brsysLocalQueueDisc": brsysLocalQueueDisc,
       "brsysVitalinkMacAddress": brsysVitalinkMacAddress,
       "brsysLatAnnceCompTblUseSize": brsysLatAnnceCompTblUseSize,
       "brsysLatAnnceCompTblUseHigh": brsysLatAnnceCompTblUseHigh,
       "brsysPcktCompTblUseSize": brsysPcktCompTblUseSize,
       "brsysPcktCompTblUseHigh": brsysPcktCompTblUseHigh,
       "stp": stp,
       "stpStp": stpStp,
       "stpForwardTimer": stpForwardTimer,
       "stpHelloTimer": stpHelloTimer,
       "stpMaxAgeTimer": stpMaxAgeTimer,
       "stpMulticastAddress": stpMulticastAddress,
       "stpPriority": stpPriority,
       "stpTopChngTimer": stpTopChngTimer,
       "stpDesigRoot": stpDesigRoot,
       "stpDesigRootCost": stpDesigRootCost,
       "stpDesigForwardTimer": stpDesigForwardTimer,
       "stpDesigHelloTimer": stpDesigHelloTimer,
       "stpDesigMaxAgeTimer": stpDesigMaxAgeTimer,
       "stpDesigRootLink": stpDesigRootLink,
       "stpDesigRootPriority": stpDesigRootPriority,
       "stpTopChngCount": stpTopChngCount,
       "stpTopStableTime": stpTopStableTime,
       "stpTopState": stpTopState,
       "stpNumLinks": stpNumLinks,
       "stpLinkTbl": stpLinkTbl,
       "stpLinkTblEnt": stpLinkTblEnt,
       "stpLinkID": stpLinkID,
       "stpLinkMacAddress": stpLinkMacAddress,
       "stpLinkpriority": stpLinkpriority,
       "stpLinkPathcost": stpLinkPathcost,
       "stpLinkPathcostCur": stpLinkPathcostCur,
       "stpLinkPathcostWeighted": stpLinkPathcostWeighted,
       "stpLinkState": stpLinkState,
       "stpLinkDesigRoot": stpLinkDesigRoot,
       "stpLinkDesigCost": stpLinkDesigCost,
       "stpLinkDesigBridge": stpLinkDesigBridge,
       "stpLinkDesigLink": stpLinkDesigLink,
       "stpLinkTopChngAck": stpLinkTopChngAck,
       "stpMaxForwardDelay": stpMaxForwardDelay,
       "stpMaxMultiForwardDelay": stpMaxMultiForwardDelay,
       "stpEarlyLoopDetection": stpEarlyLoopDetection,
       "stpEarlyLoopCount": stpEarlyLoopCount,
       "fl": fl,
       "flFiltering": flFiltering,
       "flTableSize": flTableSize,
       "flDiscardTimeout": flDiscardTimeout,
       "flUseTimeout": flUseTimeout,
       "flSrcNumSourceCur": flSrcNumSourceCur,
       "flSrcNumSourceHigh": flSrcNumSourceHigh,
       "flSrcNumSourceMax": flSrcNumSourceMax,
       "flSrcFilterTbl": flSrcFilterTbl,
       "flSrcFilterTblEnt": flSrcFilterTblEnt,
       "flSrcEntID": flSrcEntID,
       "flSrcEntMacAddress": flSrcEntMacAddress,
       "flSrcEntForwardFlag": flSrcEntForwardFlag,
       "flSrcEntUseCount": flSrcEntUseCount,
       "flDstInactiveNumCur": flDstInactiveNumCur,
       "flDstInactiveNumHigh": flDstInactiveNumHigh,
       "flDstInactiveNumMax": flDstInactiveNumMax,
       "flDstLearnedNumCur": flDstLearnedNumCur,
       "flDstLearnedNumHigh": flDstLearnedNumHigh,
       "flDstLearnedNumMax": flDstLearnedNumMax,
       "flDstLearnedNumErrors": flDstLearnedNumErrors,
       "flDstStaticNumCur": flDstStaticNumCur,
       "flDstStaticNumHigh": flDstStaticNumHigh,
       "flDstStaticNumMax": flDstStaticNumMax,
       "flDstFilterTbl": flDstFilterTbl,
       "flDstFilterTblEnt": flDstFilterTblEnt,
       "flDstEntID": flDstEntID,
       "flDstEntMacAddress": flDstEntMacAddress,
       "flDstEntLinkMap": flDstEntLinkMap,
       "flDstEntStatus": flDstEntStatus,
       "flDstEntTtl": flDstEntTtl,
       "flDstEntUseCount": flDstEntUseCount,
       "flLinkTbl": flLinkTbl,
       "flLinkTblEnt": flLinkTblEnt,
       "flLinkEntID": flLinkEntID,
       "flLinkEntLearning": flLinkEntLearning,
       "prtcl": prtcl,
       "prtclProtocol": prtclProtocol,
       "prtclNumCur": prtclNumCur,
       "prtclNumMax": prtclNumMax,
       "prtclTbl": prtclTbl,
       "prtclTblEnt": prtclTblEnt,
       "prtclEntID": prtclEntID,
       "prtclEntProtocolID": prtclEntProtocolID,
       "prtclEntMac": prtclEntMac,
       "prtclEntName": prtclEntName,
       "prtclEntPriority": prtclEntPriority,
       "prtclEntUseCount": prtclEntUseCount,
       "prtclDefaultPriority": prtclDefaultPriority,
       "prtclDefaultUseCount": prtclDefaultUseCount,
       "lks": lks,
       "lksNum": lksNum,
       "lksTbl": lksTbl,
       "lksTblEnt": lksTblEnt,
       "lksEntID": lksEntID,
       "lksEntStateConfig": lksEntStateConfig,
       "lksEntStateActive": lksEntStateActive,
       "lksEntType": lksEntType,
       "lksEntTypeSpecific": lksEntTypeSpecific,
       "lksEntName": lksEntName,
       "lksEntUtilizationCur": lksEntUtilizationCur,
       "lksEntUtilizationHigh": lksEntUtilizationHigh,
       "lksEntUtilizationAvg": lksEntUtilizationAvg,
       "lksEntForwardingCur": lksEntForwardingCur,
       "lksEntForwardingHigh": lksEntForwardingHigh,
       "lksEntForwardingAvg": lksEntForwardingAvg,
       "lksEntFilteringCur": lksEntFilteringCur,
       "lksEntFilteringHigh": lksEntFilteringHigh,
       "lksEntFilteringAvg": lksEntFilteringAvg,
       "lksEntOutputQCur": lksEntOutputQCur,
       "lksEntOutputQHigh": lksEntOutputQHigh,
       "lksEntOutputQTotal": lksEntOutputQTotal,
       "lksEntTransmitLinkSpeed": lksEntTransmitLinkSpeed,
       "lksEntReceiveLinkSpeed": lksEntReceiveLinkSpeed,
       "lksEntTraffic": lksEntTraffic,
       "lksEntTrafficPacketsIn": lksEntTrafficPacketsIn,
       "lksEntTrafficPacketsOut": lksEntTrafficPacketsOut,
       "lksEntTrafficMulticastsIn": lksEntTrafficMulticastsIn,
       "lksEntTrafficMulticastsOut": lksEntTrafficMulticastsOut,
       "lksEntTrafficUnicastsIn": lksEntTrafficUnicastsIn,
       "lksEntTrafficUnicastsOut": lksEntTrafficUnicastsOut,
       "lksEntTrafficStpIn": lksEntTrafficStpIn,
       "lksEntTrafficStpOut": lksEntTrafficStpOut,
       "lksEntTrafficBytesIn": lksEntTrafficBytesIn,
       "lksEntTrafficBytesOut": lksEntTrafficBytesOut,
       "lksEntDiscards": lksEntDiscards,
       "lksEntDiscardCrcError": lksEntDiscardCrcError,
       "lksEntDiscardFiltering": lksEntDiscardFiltering,
       "lksEntDiscardnoBuffers": lksEntDiscardnoBuffers,
       "lksEntDiscardPriority": lksEntDiscardPriority,
       "lksEntDiscardLatGroupAnnce": lksEntDiscardLatGroupAnnce,
       "lksEntDiscardLostBuffers": lksEntDiscardLostBuffers,
       "lksEntDiscardOutputQueueFull": lksEntDiscardOutputQueueFull,
       "lksEntDiscardDelayExceeded": lksEntDiscardDelayExceeded,
       "wan": wan,
       "wanNullClock": wanNullClock,
       "wanNum": wanNum,
       "wanTbl": wanTbl,
       "wanTblEnt": wanTblEnt,
       "wanEntID": wanEntID,
       "wanEntCompression": wanEntCompression,
       "wanEntDsrTimeout": wanEntDsrTimeout,
       "wanEntLocalPhone": wanEntLocalPhone,
       "wanEntDialPhoneNumMax": wanEntDialPhoneNumMax,
       "wanEntDialPhoneTbl": wanEntDialPhoneTbl,
       "wanEntDialPhoneEnt": wanEntDialPhoneEnt,
       "wanEntDialPhoneEntID": wanEntDialPhoneEntID,
       "wanEntDialPhoneEntPhone": wanEntDialPhoneEntPhone,
       "wanEntGroups": wanEntGroups,
       "wanEntModemType": wanEntModemType,
       "wanEntNullClock": wanEntNullClock,
       "wanEntPathcostWeighted": wanEntPathcostWeighted,
       "wanEntErrorRateCur": wanEntErrorRateCur,
       "wanEntErrorRateHigh": wanEntErrorRateHigh,
       "wanEntErrorRateAvg": wanEntErrorRateAvg,
       "wanEntLinkDownCur": wanEntLinkDownCur,
       "wanEntLinkDownHigh": wanEntLinkDownHigh,
       "wanEntLinkDownTotal": wanEntLinkDownTotal,
       "wanEntLinkDownCount": wanEntLinkDownCount,
       "wanEntCableType": wanEntCableType,
       "wanEntCtsCur": wanEntCtsCur,
       "wanEntRtsCur": wanEntRtsCur,
       "wanEntDcdCur": wanEntDcdCur,
       "wanEntDsrCur": wanEntDsrCur,
       "wanEntDtrCur": wanEntDtrCur,
       "wanEntRingCur": wanEntRingCur,
       "wanEntCtsChanges": wanEntCtsChanges,
       "wanEntRtsChanges": wanEntRtsChanges,
       "wanEntDcdChanges": wanEntDcdChanges,
       "wanEntDsrChanges": wanEntDsrChanges,
       "wanEntDtrChanges": wanEntDtrChanges,
       "wanEntRingChanges": wanEntRingChanges,
       "wanEntCompNum": wanEntCompNum,
       "wanEntCompressionTbl": wanEntCompressionTbl,
       "wanEntCompEnt": wanEntCompEnt,
       "wanEntCompEntID": wanEntCompEntID,
       "wanEntCompEntDescription": wanEntCompEntDescription,
       "wanEntCompEntCurrent": wanEntCompEntCurrent,
       "wanEntCompEntHigh": wanEntCompEntHigh,
       "wanEntCompEntAverage": wanEntCompEntAverage,
       "wanEntCompressionStatus": wanEntCompressionStatus,
       "wanVitalinkCompatibility": wanVitalinkCompatibility,
       "lan": lan,
       "lanNum": lanNum,
       "lanTbl": lanTbl,
       "lanTblEnt": lanTblEnt,
       "lanEntID": lanEntID,
       "lanEntShutdownThreshold": lanEntShutdownThreshold,
       "lanEntFramingError": lanEntFramingError,
       "lanEntLostPacketsError": lanEntLostPacketsError,
       "lanEntMemoryError": lanEntMemoryError,
       "lanEntOverflowError": lanEntOverflowError,
       "lanEntPacketInTooLongError": lanEntPacketInTooLongError,
       "lanEntCarrierLossError": lanEntCarrierLossError,
       "lanEntHeartbeatFailureError": lanEntHeartbeatFailureError,
       "lanEntLateCollisionError": lanEntLateCollisionError,
       "lanEntPacketOutTooLongError": lanEntPacketOutTooLongError,
       "lanEntRetryExceedError": lanEntRetryExceedError}
)
