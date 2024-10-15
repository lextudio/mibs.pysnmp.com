# SNMP MIB module (F10-FIPSNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/F10-FIPSNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:22 2024
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

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(dot1qVlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qVlanIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

dF10FipSnooping = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22)
)
dF10FipSnooping.setRevisions(
        ("2011-12-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DF10FIPSCfgGroup_ObjectIdentity = ObjectIdentity
dF10FIPSCfgGroup = _DF10FIPSCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1)
)


class _DF10FIPSAdminMode_Type(Integer32):
    """Custom type dF10FIPSAdminMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DF10FIPSAdminMode_Type.__name__ = "Integer32"
_DF10FIPSAdminMode_Object = MibScalar
dF10FIPSAdminMode = _DF10FIPSAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 1),
    _DF10FIPSAdminMode_Type()
)
dF10FIPSAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dF10FIPSAdminMode.setStatus("current")


class _DF10FIPSFCMAP_Type(OctetString):
    """Custom type dF10FIPSFCMAP based on OctetString"""
    defaultValue = OctetString("0x0EFC00")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_DF10FIPSFCMAP_Type.__name__ = "OctetString"
_DF10FIPSFCMAP_Object = MibScalar
dF10FIPSFCMAP = _DF10FIPSFCMAP_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 2),
    _DF10FIPSFCMAP_Type()
)
dF10FIPSFCMAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dF10FIPSFCMAP.setStatus("current")
_DF10FIPSVlanCfgTable_Object = MibTable
dF10FIPSVlanCfgTable = _DF10FIPSVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 3)
)
if mibBuilder.loadTexts:
    dF10FIPSVlanCfgTable.setStatus("current")
_DF10FIPSVlanCfgEntry_Object = MibTableRow
dF10FIPSVlanCfgEntry = _DF10FIPSVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 3, 1)
)
dF10FIPSVlanCfgEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dF10FIPSVlanCfgEntry.setStatus("current")


class _DF10FIPSVlanAdminMode_Type(Integer32):
    """Custom type dF10FIPSVlanAdminMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DF10FIPSVlanAdminMode_Type.__name__ = "Integer32"
_DF10FIPSVlanAdminMode_Object = MibTableColumn
dF10FIPSVlanAdminMode = _DF10FIPSVlanAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 3, 1, 1),
    _DF10FIPSVlanAdminMode_Type()
)
dF10FIPSVlanAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dF10FIPSVlanAdminMode.setStatus("current")


class _DF10FIPSVlanFCMAP_Type(OctetString):
    """Custom type dF10FIPSVlanFCMAP based on OctetString"""
    defaultValue = OctetString("0x0EFC00")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_DF10FIPSVlanFCMAP_Type.__name__ = "OctetString"
_DF10FIPSVlanFCMAP_Object = MibTableColumn
dF10FIPSVlanFCMAP = _DF10FIPSVlanFCMAP_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 3, 1, 2),
    _DF10FIPSVlanFCMAP_Type()
)
dF10FIPSVlanFCMAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dF10FIPSVlanFCMAP.setStatus("current")


class _DF10FIPSVlanStatsClear_Type(Integer32):
    """Custom type dF10FIPSVlanStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("ignore", 1))
    )


_DF10FIPSVlanStatsClear_Type.__name__ = "Integer32"
_DF10FIPSVlanStatsClear_Object = MibTableColumn
dF10FIPSVlanStatsClear = _DF10FIPSVlanStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 3, 1, 3),
    _DF10FIPSVlanStatsClear_Type()
)
dF10FIPSVlanStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dF10FIPSVlanStatsClear.setStatus("current")
_DF10FIPSIntfTable_Object = MibTable
dF10FIPSIntfTable = _DF10FIPSIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 4)
)
if mibBuilder.loadTexts:
    dF10FIPSIntfTable.setStatus("current")
_DF10FIPSIntfEntry_Object = MibTableRow
dF10FIPSIntfEntry = _DF10FIPSIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 4, 1)
)
dF10FIPSIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dF10FIPSIntfEntry.setStatus("current")


class _DF10FIPSIntfPortModeFcf_Type(Integer32):
    """Custom type dF10FIPSIntfPortModeFcf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("fcf", 1),
          ("fcoetrusted", 2))
    )


_DF10FIPSIntfPortModeFcf_Type.__name__ = "Integer32"
_DF10FIPSIntfPortModeFcf_Object = MibTableColumn
dF10FIPSIntfPortModeFcf = _DF10FIPSIntfPortModeFcf_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 4, 1, 2),
    _DF10FIPSIntfPortModeFcf_Type()
)
dF10FIPSIntfPortModeFcf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dF10FIPSIntfPortModeFcf.setStatus("current")


class _DF10FIPSIntfStatsClear_Type(Integer32):
    """Custom type dF10FIPSIntfStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("ignore", 1))
    )


_DF10FIPSIntfStatsClear_Type.__name__ = "Integer32"
_DF10FIPSIntfStatsClear_Object = MibTableColumn
dF10FIPSIntfStatsClear = _DF10FIPSIntfStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 4, 1, 3),
    _DF10FIPSIntfStatsClear_Type()
)
dF10FIPSIntfStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dF10FIPSIntfStatsClear.setStatus("current")


class _DF10FIPSStatsClear_Type(Integer32):
    """Custom type dF10FIPSStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("ignore", 1))
    )


_DF10FIPSStatsClear_Type.__name__ = "Integer32"
_DF10FIPSStatsClear_Object = MibScalar
dF10FIPSStatsClear = _DF10FIPSStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 5),
    _DF10FIPSStatsClear_Type()
)
dF10FIPSStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dF10FIPSStatsClear.setStatus("current")
_DF10FIPSStatusGroup_ObjectIdentity = ObjectIdentity
dF10FIPSStatusGroup = _DF10FIPSStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2)
)
_DF10FIPSSessionTable_Object = MibTable
dF10FIPSSessionTable = _DF10FIPSSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1)
)
if mibBuilder.loadTexts:
    dF10FIPSSessionTable.setStatus("current")
_DF10FIPSSessionEntry_Object = MibTableRow
dF10FIPSSessionEntry = _DF10FIPSSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1)
)
dF10FIPSSessionEntry.setIndexNames(
    (0, "F10-FIPSNOOPING-MIB", "dF10FIPSSessionVlanIndex"),
    (0, "F10-FIPSNOOPING-MIB", "dF10FIPSSessionFCFMacAddr"),
    (0, "F10-FIPSNOOPING-MIB", "dF10FIPSSessionENodeMacAddr"),
    (0, "F10-FIPSNOOPING-MIB", "dF10FIPSSessionLoginType"),
    (0, "F10-FIPSNOOPING-MIB", "dF10FIPSFCoEMacAddr"),
    (0, "F10-FIPSNOOPING-MIB", "dF10FIPSSessionTentativeIndex"),
    (0, "F10-FIPSNOOPING-MIB", "dF10FIPSSessionFCID"),
)
if mibBuilder.loadTexts:
    dF10FIPSSessionEntry.setStatus("current")
_DF10FIPSSessionVlanIndex_Type = Unsigned32
_DF10FIPSSessionVlanIndex_Object = MibTableColumn
dF10FIPSSessionVlanIndex = _DF10FIPSSessionVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 1),
    _DF10FIPSSessionVlanIndex_Type()
)
dF10FIPSSessionVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dF10FIPSSessionVlanIndex.setStatus("current")
_DF10FIPSSessionFCFMacAddr_Type = MacAddress
_DF10FIPSSessionFCFMacAddr_Object = MibTableColumn
dF10FIPSSessionFCFMacAddr = _DF10FIPSSessionFCFMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 2),
    _DF10FIPSSessionFCFMacAddr_Type()
)
dF10FIPSSessionFCFMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dF10FIPSSessionFCFMacAddr.setStatus("current")
_DF10FIPSSessionENodeMacAddr_Type = MacAddress
_DF10FIPSSessionENodeMacAddr_Object = MibTableColumn
dF10FIPSSessionENodeMacAddr = _DF10FIPSSessionENodeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 3),
    _DF10FIPSSessionENodeMacAddr_Type()
)
dF10FIPSSessionENodeMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dF10FIPSSessionENodeMacAddr.setStatus("current")


class _DF10FIPSSessionLoginType_Type(Integer32):
    """Custom type dF10FIPSSessionLoginType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fdisc", 1),
          ("flogi", 0))
    )


_DF10FIPSSessionLoginType_Type.__name__ = "Integer32"
_DF10FIPSSessionLoginType_Object = MibTableColumn
dF10FIPSSessionLoginType = _DF10FIPSSessionLoginType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 4),
    _DF10FIPSSessionLoginType_Type()
)
dF10FIPSSessionLoginType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dF10FIPSSessionLoginType.setStatus("current")
_DF10FIPSFCoEMacAddr_Type = MacAddress
_DF10FIPSFCoEMacAddr_Object = MibTableColumn
dF10FIPSFCoEMacAddr = _DF10FIPSFCoEMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 5),
    _DF10FIPSFCoEMacAddr_Type()
)
dF10FIPSFCoEMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dF10FIPSFCoEMacAddr.setStatus("current")
_DF10FIPSSessionTentativeIndex_Type = Unsigned32
_DF10FIPSSessionTentativeIndex_Object = MibTableColumn
dF10FIPSSessionTentativeIndex = _DF10FIPSSessionTentativeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 6),
    _DF10FIPSSessionTentativeIndex_Type()
)
dF10FIPSSessionTentativeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dF10FIPSSessionTentativeIndex.setStatus("current")


class _DF10FIPSSessionFCID_Type(OctetString):
    """Custom type dF10FIPSSessionFCID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_DF10FIPSSessionFCID_Type.__name__ = "OctetString"
_DF10FIPSSessionFCID_Object = MibTableColumn
dF10FIPSSessionFCID = _DF10FIPSSessionFCID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 7),
    _DF10FIPSSessionFCID_Type()
)
dF10FIPSSessionFCID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dF10FIPSSessionFCID.setStatus("current")
_DF10FIPSSessionENodeIntf_Type = Unsigned32
_DF10FIPSSessionENodeIntf_Object = MibTableColumn
dF10FIPSSessionENodeIntf = _DF10FIPSSessionENodeIntf_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 8),
    _DF10FIPSSessionENodeIntf_Type()
)
dF10FIPSSessionENodeIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSSessionENodeIntf.setStatus("current")
_DF10FIPSSessionFCFIntf_Type = Unsigned32
_DF10FIPSSessionFCFIntf_Object = MibTableColumn
dF10FIPSSessionFCFIntf = _DF10FIPSSessionFCFIntf_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 9),
    _DF10FIPSSessionFCFIntf_Type()
)
dF10FIPSSessionFCFIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSSessionFCFIntf.setStatus("current")
_DF10FIPSSessionTime_Type = DateAndTime
_DF10FIPSSessionTime_Object = MibTableColumn
dF10FIPSSessionTime = _DF10FIPSSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 10),
    _DF10FIPSSessionTime_Type()
)
dF10FIPSSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSSessionTime.setStatus("current")


class _DF10FIPSSessionExpiryTime_Type(Integer32):
    """Custom type dF10FIPSSessionExpiryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 450),
    )


_DF10FIPSSessionExpiryTime_Type.__name__ = "Integer32"
_DF10FIPSSessionExpiryTime_Object = MibTableColumn
dF10FIPSSessionExpiryTime = _DF10FIPSSessionExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 11),
    _DF10FIPSSessionExpiryTime_Type()
)
dF10FIPSSessionExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSSessionExpiryTime.setStatus("current")
_DF10FIPSSessionState_Type = OctetString
_DF10FIPSSessionState_Object = MibTableColumn
dF10FIPSSessionState = _DF10FIPSSessionState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 12),
    _DF10FIPSSessionState_Type()
)
dF10FIPSSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSSessionState.setStatus("current")
_DF10FIPSENodeTable_Object = MibTable
dF10FIPSENodeTable = _DF10FIPSENodeTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2)
)
if mibBuilder.loadTexts:
    dF10FIPSENodeTable.setStatus("current")
_DF10FIPSENodeEntry_Object = MibTableRow
dF10FIPSENodeEntry = _DF10FIPSENodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1)
)
dF10FIPSENodeEntry.setIndexNames(
    (0, "F10-FIPSNOOPING-MIB", "dF10FIPSENodeVlanIndex"),
    (0, "F10-FIPSNOOPING-MIB", "dF10FIPSENodeMacAddr"),
)
if mibBuilder.loadTexts:
    dF10FIPSENodeEntry.setStatus("current")
_DF10FIPSENodeVlanIndex_Type = Unsigned32
_DF10FIPSENodeVlanIndex_Object = MibTableColumn
dF10FIPSENodeVlanIndex = _DF10FIPSENodeVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 1),
    _DF10FIPSENodeVlanIndex_Type()
)
dF10FIPSENodeVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dF10FIPSENodeVlanIndex.setStatus("current")
_DF10FIPSENodeMacAddr_Type = MacAddress
_DF10FIPSENodeMacAddr_Object = MibTableColumn
dF10FIPSENodeMacAddr = _DF10FIPSENodeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 2),
    _DF10FIPSENodeMacAddr_Type()
)
dF10FIPSENodeMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dF10FIPSENodeMacAddr.setStatus("current")
_DF10FIPSENodeIntf_Type = Unsigned32
_DF10FIPSENodeIntf_Object = MibTableColumn
dF10FIPSENodeIntf = _DF10FIPSENodeIntf_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 3),
    _DF10FIPSENodeIntf_Type()
)
dF10FIPSENodeIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSENodeIntf.setStatus("current")
_DF10FIPSENodeNameID_Type = OctetString
_DF10FIPSENodeNameID_Object = MibTableColumn
dF10FIPSENodeNameID = _DF10FIPSENodeNameID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 4),
    _DF10FIPSENodeNameID_Type()
)
dF10FIPSENodeNameID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSENodeNameID.setStatus("current")
_DF10FIPSENodeMaxFCoESize_Type = Unsigned32
_DF10FIPSENodeMaxFCoESize_Object = MibTableColumn
dF10FIPSENodeMaxFCoESize = _DF10FIPSENodeMaxFCoESize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 5),
    _DF10FIPSENodeMaxFCoESize_Type()
)
dF10FIPSENodeMaxFCoESize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSENodeMaxFCoESize.setStatus("current")
_DF10FIPSENodeConnectedFCFsCount_Type = Unsigned32
_DF10FIPSENodeConnectedFCFsCount_Object = MibTableColumn
dF10FIPSENodeConnectedFCFsCount = _DF10FIPSENodeConnectedFCFsCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 6),
    _DF10FIPSENodeConnectedFCFsCount_Type()
)
dF10FIPSENodeConnectedFCFsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSENodeConnectedFCFsCount.setStatus("current")
_DF10FIPSENodeActiveSessions_Type = Unsigned32
_DF10FIPSENodeActiveSessions_Object = MibTableColumn
dF10FIPSENodeActiveSessions = _DF10FIPSENodeActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 7),
    _DF10FIPSENodeActiveSessions_Type()
)
dF10FIPSENodeActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSENodeActiveSessions.setStatus("current")
_DF10FIPSENodeWaitingSessions_Type = Unsigned32
_DF10FIPSENodeWaitingSessions_Object = MibTableColumn
dF10FIPSENodeWaitingSessions = _DF10FIPSENodeWaitingSessions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 8),
    _DF10FIPSENodeWaitingSessions_Type()
)
dF10FIPSENodeWaitingSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSENodeWaitingSessions.setStatus("current")
_DF10FIPSENodeRejectedSessions_Type = Unsigned32
_DF10FIPSENodeRejectedSessions_Object = MibTableColumn
dF10FIPSENodeRejectedSessions = _DF10FIPSENodeRejectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 9),
    _DF10FIPSENodeRejectedSessions_Type()
)
dF10FIPSENodeRejectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSENodeRejectedSessions.setStatus("current")
_DF10FIPSENodeTimeSinceDiscovered_Type = DateAndTime
_DF10FIPSENodeTimeSinceDiscovered_Object = MibTableColumn
dF10FIPSENodeTimeSinceDiscovered = _DF10FIPSENodeTimeSinceDiscovered_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 10),
    _DF10FIPSENodeTimeSinceDiscovered_Type()
)
dF10FIPSENodeTimeSinceDiscovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSENodeTimeSinceDiscovered.setStatus("current")
_DF10FIPSFCFTable_Object = MibTable
dF10FIPSFCFTable = _DF10FIPSFCFTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3)
)
if mibBuilder.loadTexts:
    dF10FIPSFCFTable.setStatus("current")
_DF10FIPSFCFEntry_Object = MibTableRow
dF10FIPSFCFEntry = _DF10FIPSFCFEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1)
)
dF10FIPSFCFEntry.setIndexNames(
    (0, "F10-FIPSNOOPING-MIB", "dF10FIPSFCFVlanIndex"),
    (0, "F10-FIPSNOOPING-MIB", "dF10FIPSFCFMacAddr"),
)
if mibBuilder.loadTexts:
    dF10FIPSFCFEntry.setStatus("current")
_DF10FIPSFCFVlanIndex_Type = Unsigned32
_DF10FIPSFCFVlanIndex_Object = MibTableColumn
dF10FIPSFCFVlanIndex = _DF10FIPSFCFVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 1),
    _DF10FIPSFCFVlanIndex_Type()
)
dF10FIPSFCFVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dF10FIPSFCFVlanIndex.setStatus("current")
_DF10FIPSFCFMacAddr_Type = MacAddress
_DF10FIPSFCFMacAddr_Object = MibTableColumn
dF10FIPSFCFMacAddr = _DF10FIPSFCFMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 2),
    _DF10FIPSFCFMacAddr_Type()
)
dF10FIPSFCFMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dF10FIPSFCFMacAddr.setStatus("current")
_DF10FIPSFCFIntf_Type = Unsigned32
_DF10FIPSFCFIntf_Object = MibTableColumn
dF10FIPSFCFIntf = _DF10FIPSFCFIntf_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 3),
    _DF10FIPSFCFIntf_Type()
)
dF10FIPSFCFIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSFCFIntf.setStatus("current")
_DF10FIPSFCFNameID_Type = OctetString
_DF10FIPSFCFNameID_Object = MibTableColumn
dF10FIPSFCFNameID = _DF10FIPSFCFNameID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 4),
    _DF10FIPSFCFNameID_Type()
)
dF10FIPSFCFNameID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSFCFNameID.setStatus("current")
_DF10FIPSFCFFabricName_Type = OctetString
_DF10FIPSFCFFabricName_Object = MibTableColumn
dF10FIPSFCFFabricName = _DF10FIPSFCFFabricName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 5),
    _DF10FIPSFCFFabricName_Type()
)
dF10FIPSFCFFabricName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSFCFFabricName.setStatus("current")


class _DF10FIPSFCFAddressingMode_Type(Integer32):
    """Custom type dF10FIPSFCFAddressingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("fpma", 1),
          ("spma", 2))
    )


_DF10FIPSFCFAddressingMode_Type.__name__ = "Integer32"
_DF10FIPSFCFAddressingMode_Object = MibTableColumn
dF10FIPSFCFAddressingMode = _DF10FIPSFCFAddressingMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 6),
    _DF10FIPSFCFAddressingMode_Type()
)
dF10FIPSFCFAddressingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSFCFAddressingMode.setStatus("current")


class _DF10FIPSFCFPriority_Type(Integer32):
    """Custom type dF10FIPSFCFPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DF10FIPSFCFPriority_Type.__name__ = "Integer32"
_DF10FIPSFCFPriority_Object = MibTableColumn
dF10FIPSFCFPriority = _DF10FIPSFCFPriority_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 7),
    _DF10FIPSFCFPriority_Type()
)
dF10FIPSFCFPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSFCFPriority.setStatus("current")


class _DF10FIPSFCFDbit_Type(Integer32):
    """Custom type dF10FIPSFCFDbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DF10FIPSFCFDbit_Type.__name__ = "Integer32"
_DF10FIPSFCFDbit_Object = MibTableColumn
dF10FIPSFCFDbit = _DF10FIPSFCFDbit_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 8),
    _DF10FIPSFCFDbit_Type()
)
dF10FIPSFCFDbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSFCFDbit.setStatus("current")


class _DF10FIPSFCFIsAvailableForLogin_Type(Integer32):
    """Custom type dF10FIPSFCFIsAvailableForLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DF10FIPSFCFIsAvailableForLogin_Type.__name__ = "Integer32"
_DF10FIPSFCFIsAvailableForLogin_Object = MibTableColumn
dF10FIPSFCFIsAvailableForLogin = _DF10FIPSFCFIsAvailableForLogin_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 9),
    _DF10FIPSFCFIsAvailableForLogin_Type()
)
dF10FIPSFCFIsAvailableForLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSFCFIsAvailableForLogin.setStatus("current")


class _DF10FIPSFCFConfiguredFKA_Type(Integer32):
    """Custom type dF10FIPSFCFConfiguredFKA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 450),
    )


_DF10FIPSFCFConfiguredFKA_Type.__name__ = "Integer32"
_DF10FIPSFCFConfiguredFKA_Object = MibTableColumn
dF10FIPSFCFConfiguredFKA = _DF10FIPSFCFConfiguredFKA_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 10),
    _DF10FIPSFCFConfiguredFKA_Type()
)
dF10FIPSFCFConfiguredFKA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSFCFConfiguredFKA.setStatus("current")
_DF10FIPSFCFTimeSinceDiscovered_Type = DateAndTime
_DF10FIPSFCFTimeSinceDiscovered_Object = MibTableColumn
dF10FIPSFCFTimeSinceDiscovered = _DF10FIPSFCFTimeSinceDiscovered_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 11),
    _DF10FIPSFCFTimeSinceDiscovered_Type()
)
dF10FIPSFCFTimeSinceDiscovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSFCFTimeSinceDiscovered.setStatus("current")
_DF10FIPSFCFConnectedENodesCount_Type = Unsigned32
_DF10FIPSFCFConnectedENodesCount_Object = MibTableColumn
dF10FIPSFCFConnectedENodesCount = _DF10FIPSFCFConnectedENodesCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 12),
    _DF10FIPSFCFConnectedENodesCount_Type()
)
dF10FIPSFCFConnectedENodesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSFCFConnectedENodesCount.setStatus("current")
_DF10FIPSFCFSessions_Type = Unsigned32
_DF10FIPSFCFSessions_Object = MibTableColumn
dF10FIPSFCFSessions = _DF10FIPSFCFSessions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 13),
    _DF10FIPSFCFSessions_Type()
)
dF10FIPSFCFSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSFCFSessions.setStatus("current")
_DF10FIPSFCFExpiryTime_Type = Unsigned32
_DF10FIPSFCFExpiryTime_Object = MibTableColumn
dF10FIPSFCFExpiryTime = _DF10FIPSFCFExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 14),
    _DF10FIPSFCFExpiryTime_Type()
)
dF10FIPSFCFExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSFCFExpiryTime.setStatus("current")
_DF10FIPSStatisticsGroup_ObjectIdentity = ObjectIdentity
dF10FIPSStatisticsGroup = _DF10FIPSStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3)
)
_DF10FIPSVlanStatsTable_Object = MibTable
dF10FIPSVlanStatsTable = _DF10FIPSVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1)
)
if mibBuilder.loadTexts:
    dF10FIPSVlanStatsTable.setStatus("current")
_DF10FIPSVlanStatsEntry_Object = MibTableRow
dF10FIPSVlanStatsEntry = _DF10FIPSVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1)
)
dF10FIPSVlanStatsEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dF10FIPSVlanStatsEntry.setStatus("current")
_DF10FIPSVlanVlanRequests_Type = Counter32
_DF10FIPSVlanVlanRequests_Object = MibTableColumn
dF10FIPSVlanVlanRequests = _DF10FIPSVlanVlanRequests_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 1),
    _DF10FIPSVlanVlanRequests_Type()
)
dF10FIPSVlanVlanRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanVlanRequests.setStatus("current")
_DF10FIPSVlanVlanNotifications_Type = Counter32
_DF10FIPSVlanVlanNotifications_Object = MibTableColumn
dF10FIPSVlanVlanNotifications = _DF10FIPSVlanVlanNotifications_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 2),
    _DF10FIPSVlanVlanNotifications_Type()
)
dF10FIPSVlanVlanNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanVlanNotifications.setStatus("current")
_DF10FIPSVlanMCDiscSolicits_Type = Counter32
_DF10FIPSVlanMCDiscSolicits_Object = MibTableColumn
dF10FIPSVlanMCDiscSolicits = _DF10FIPSVlanMCDiscSolicits_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 3),
    _DF10FIPSVlanMCDiscSolicits_Type()
)
dF10FIPSVlanMCDiscSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanMCDiscSolicits.setStatus("current")
_DF10FIPSVlanUnicastDiscSolicits_Type = Counter32
_DF10FIPSVlanUnicastDiscSolicits_Object = MibTableColumn
dF10FIPSVlanUnicastDiscSolicits = _DF10FIPSVlanUnicastDiscSolicits_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 4),
    _DF10FIPSVlanUnicastDiscSolicits_Type()
)
dF10FIPSVlanUnicastDiscSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanUnicastDiscSolicits.setStatus("current")
_DF10FIPSVlanFLogis_Type = Counter32
_DF10FIPSVlanFLogis_Object = MibTableColumn
dF10FIPSVlanFLogis = _DF10FIPSVlanFLogis_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 5),
    _DF10FIPSVlanFLogis_Type()
)
dF10FIPSVlanFLogis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanFLogis.setStatus("current")
_DF10FIPSVlanFDiscs_Type = Counter32
_DF10FIPSVlanFDiscs_Object = MibTableColumn
dF10FIPSVlanFDiscs = _DF10FIPSVlanFDiscs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 6),
    _DF10FIPSVlanFDiscs_Type()
)
dF10FIPSVlanFDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanFDiscs.setStatus("current")
_DF10FIPSVlanFLogouts_Type = Counter32
_DF10FIPSVlanFLogouts_Object = MibTableColumn
dF10FIPSVlanFLogouts = _DF10FIPSVlanFLogouts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 7),
    _DF10FIPSVlanFLogouts_Type()
)
dF10FIPSVlanFLogouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanFLogouts.setStatus("current")
_DF10FIPSVlanVnPortKeepAlives_Type = Counter32
_DF10FIPSVlanVnPortKeepAlives_Object = MibTableColumn
dF10FIPSVlanVnPortKeepAlives = _DF10FIPSVlanVnPortKeepAlives_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 8),
    _DF10FIPSVlanVnPortKeepAlives_Type()
)
dF10FIPSVlanVnPortKeepAlives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanVnPortKeepAlives.setStatus("current")
_DF10FIPSVlanMCDiscAdverts_Type = Counter32
_DF10FIPSVlanMCDiscAdverts_Object = MibTableColumn
dF10FIPSVlanMCDiscAdverts = _DF10FIPSVlanMCDiscAdverts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 9),
    _DF10FIPSVlanMCDiscAdverts_Type()
)
dF10FIPSVlanMCDiscAdverts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanMCDiscAdverts.setStatus("current")
_DF10FIPSVlanUnicastDiscAdverts_Type = Counter32
_DF10FIPSVlanUnicastDiscAdverts_Object = MibTableColumn
dF10FIPSVlanUnicastDiscAdverts = _DF10FIPSVlanUnicastDiscAdverts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 10),
    _DF10FIPSVlanUnicastDiscAdverts_Type()
)
dF10FIPSVlanUnicastDiscAdverts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanUnicastDiscAdverts.setStatus("current")
_DF10FIPSVlanFLogiAccepts_Type = Counter32
_DF10FIPSVlanFLogiAccepts_Object = MibTableColumn
dF10FIPSVlanFLogiAccepts = _DF10FIPSVlanFLogiAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 11),
    _DF10FIPSVlanFLogiAccepts_Type()
)
dF10FIPSVlanFLogiAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanFLogiAccepts.setStatus("current")
_DF10FIPSVlanFLogiRejects_Type = Counter32
_DF10FIPSVlanFLogiRejects_Object = MibTableColumn
dF10FIPSVlanFLogiRejects = _DF10FIPSVlanFLogiRejects_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 12),
    _DF10FIPSVlanFLogiRejects_Type()
)
dF10FIPSVlanFLogiRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanFLogiRejects.setStatus("current")
_DF10FIPSVlanFDiscAccepts_Type = Counter32
_DF10FIPSVlanFDiscAccepts_Object = MibTableColumn
dF10FIPSVlanFDiscAccepts = _DF10FIPSVlanFDiscAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 13),
    _DF10FIPSVlanFDiscAccepts_Type()
)
dF10FIPSVlanFDiscAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanFDiscAccepts.setStatus("current")
_DF10FIPSVlanFDiscRejects_Type = Counter32
_DF10FIPSVlanFDiscRejects_Object = MibTableColumn
dF10FIPSVlanFDiscRejects = _DF10FIPSVlanFDiscRejects_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 14),
    _DF10FIPSVlanFDiscRejects_Type()
)
dF10FIPSVlanFDiscRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanFDiscRejects.setStatus("current")
_DF10FIPSVlanFLogoutAccepts_Type = Counter32
_DF10FIPSVlanFLogoutAccepts_Object = MibTableColumn
dF10FIPSVlanFLogoutAccepts = _DF10FIPSVlanFLogoutAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 15),
    _DF10FIPSVlanFLogoutAccepts_Type()
)
dF10FIPSVlanFLogoutAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanFLogoutAccepts.setStatus("current")
_DF10FIPSVlanFLogoutRejects_Type = Counter32
_DF10FIPSVlanFLogoutRejects_Object = MibTableColumn
dF10FIPSVlanFLogoutRejects = _DF10FIPSVlanFLogoutRejects_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 16),
    _DF10FIPSVlanFLogoutRejects_Type()
)
dF10FIPSVlanFLogoutRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanFLogoutRejects.setStatus("current")
_DF10FIPSVlanClearVirtLinks_Type = Counter32
_DF10FIPSVlanClearVirtLinks_Object = MibTableColumn
dF10FIPSVlanClearVirtLinks = _DF10FIPSVlanClearVirtLinks_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 17),
    _DF10FIPSVlanClearVirtLinks_Type()
)
dF10FIPSVlanClearVirtLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanClearVirtLinks.setStatus("current")
_DF10FIPSVlanVnPortSeshTimeouts_Type = Counter32
_DF10FIPSVlanVnPortSeshTimeouts_Object = MibTableColumn
dF10FIPSVlanVnPortSeshTimeouts = _DF10FIPSVlanVnPortSeshTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 18),
    _DF10FIPSVlanVnPortSeshTimeouts_Type()
)
dF10FIPSVlanVnPortSeshTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanVnPortSeshTimeouts.setStatus("current")
_DF10FIPSVlanFcfDiscAdvTimeouts_Type = Counter32
_DF10FIPSVlanFcfDiscAdvTimeouts_Object = MibTableColumn
dF10FIPSVlanFcfDiscAdvTimeouts = _DF10FIPSVlanFcfDiscAdvTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 19),
    _DF10FIPSVlanFcfDiscAdvTimeouts_Type()
)
dF10FIPSVlanFcfDiscAdvTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanFcfDiscAdvTimeouts.setStatus("current")
_DF10FIPSVlanSeshFailsDueToHwCfg_Type = Counter32
_DF10FIPSVlanSeshFailsDueToHwCfg_Object = MibTableColumn
dF10FIPSVlanSeshFailsDueToHwCfg = _DF10FIPSVlanSeshFailsDueToHwCfg_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 20),
    _DF10FIPSVlanSeshFailsDueToHwCfg_Type()
)
dF10FIPSVlanSeshFailsDueToHwCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanSeshFailsDueToHwCfg.setStatus("current")
_DF10FIPSVlanSeshDenyFcfLmtRch_Type = Counter32
_DF10FIPSVlanSeshDenyFcfLmtRch_Object = MibTableColumn
dF10FIPSVlanSeshDenyFcfLmtRch = _DF10FIPSVlanSeshDenyFcfLmtRch_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 21),
    _DF10FIPSVlanSeshDenyFcfLmtRch_Type()
)
dF10FIPSVlanSeshDenyFcfLmtRch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanSeshDenyFcfLmtRch.setStatus("current")
_DF10FIPSVlanSeshDenyENodeLmtRch_Type = Counter32
_DF10FIPSVlanSeshDenyENodeLmtRch_Object = MibTableColumn
dF10FIPSVlanSeshDenyENodeLmtRch = _DF10FIPSVlanSeshDenyENodeLmtRch_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 22),
    _DF10FIPSVlanSeshDenyENodeLmtRch_Type()
)
dF10FIPSVlanSeshDenyENodeLmtRch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanSeshDenyENodeLmtRch.setStatus("current")
_DF10FIPSVlanSeshDenySysLmtRch_Type = Counter32
_DF10FIPSVlanSeshDenySysLmtRch_Object = MibTableColumn
dF10FIPSVlanSeshDenySysLmtRch = _DF10FIPSVlanSeshDenySysLmtRch_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 23),
    _DF10FIPSVlanSeshDenySysLmtRch_Type()
)
dF10FIPSVlanSeshDenySysLmtRch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSVlanSeshDenySysLmtRch.setStatus("current")
_DF10FIPSIntfStatsTable_Object = MibTable
dF10FIPSIntfStatsTable = _DF10FIPSIntfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2)
)
if mibBuilder.loadTexts:
    dF10FIPSIntfStatsTable.setStatus("current")
_DF10FIPSIntfStatsEntry_Object = MibTableRow
dF10FIPSIntfStatsEntry = _DF10FIPSIntfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1)
)
dF10FIPSIntfStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dF10FIPSIntfStatsEntry.setStatus("current")
_DF10FIPSIntfVlanRequests_Type = Counter32
_DF10FIPSIntfVlanRequests_Object = MibTableColumn
dF10FIPSIntfVlanRequests = _DF10FIPSIntfVlanRequests_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 1),
    _DF10FIPSIntfVlanRequests_Type()
)
dF10FIPSIntfVlanRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfVlanRequests.setStatus("current")
_DF10FIPSIntfVlanNotifications_Type = Counter32
_DF10FIPSIntfVlanNotifications_Object = MibTableColumn
dF10FIPSIntfVlanNotifications = _DF10FIPSIntfVlanNotifications_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 2),
    _DF10FIPSIntfVlanNotifications_Type()
)
dF10FIPSIntfVlanNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfVlanNotifications.setStatus("current")
_DF10FIPSIntfMCDiscSolicits_Type = Counter32
_DF10FIPSIntfMCDiscSolicits_Object = MibTableColumn
dF10FIPSIntfMCDiscSolicits = _DF10FIPSIntfMCDiscSolicits_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 3),
    _DF10FIPSIntfMCDiscSolicits_Type()
)
dF10FIPSIntfMCDiscSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfMCDiscSolicits.setStatus("current")
_DF10FIPSIntfUnicastDiscSolicits_Type = Counter32
_DF10FIPSIntfUnicastDiscSolicits_Object = MibTableColumn
dF10FIPSIntfUnicastDiscSolicits = _DF10FIPSIntfUnicastDiscSolicits_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 4),
    _DF10FIPSIntfUnicastDiscSolicits_Type()
)
dF10FIPSIntfUnicastDiscSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfUnicastDiscSolicits.setStatus("current")
_DF10FIPSIntfFLogis_Type = Counter32
_DF10FIPSIntfFLogis_Object = MibTableColumn
dF10FIPSIntfFLogis = _DF10FIPSIntfFLogis_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 5),
    _DF10FIPSIntfFLogis_Type()
)
dF10FIPSIntfFLogis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfFLogis.setStatus("current")
_DF10FIPSIntfFDiscs_Type = Counter32
_DF10FIPSIntfFDiscs_Object = MibTableColumn
dF10FIPSIntfFDiscs = _DF10FIPSIntfFDiscs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 6),
    _DF10FIPSIntfFDiscs_Type()
)
dF10FIPSIntfFDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfFDiscs.setStatus("current")
_DF10FIPSIntfFLogouts_Type = Counter32
_DF10FIPSIntfFLogouts_Object = MibTableColumn
dF10FIPSIntfFLogouts = _DF10FIPSIntfFLogouts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 7),
    _DF10FIPSIntfFLogouts_Type()
)
dF10FIPSIntfFLogouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfFLogouts.setStatus("current")
_DF10FIPSIntfVnPortKeepAlives_Type = Counter32
_DF10FIPSIntfVnPortKeepAlives_Object = MibTableColumn
dF10FIPSIntfVnPortKeepAlives = _DF10FIPSIntfVnPortKeepAlives_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 8),
    _DF10FIPSIntfVnPortKeepAlives_Type()
)
dF10FIPSIntfVnPortKeepAlives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfVnPortKeepAlives.setStatus("current")
_DF10FIPSIntfMCDiscAdverts_Type = Counter32
_DF10FIPSIntfMCDiscAdverts_Object = MibTableColumn
dF10FIPSIntfMCDiscAdverts = _DF10FIPSIntfMCDiscAdverts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 9),
    _DF10FIPSIntfMCDiscAdverts_Type()
)
dF10FIPSIntfMCDiscAdverts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfMCDiscAdverts.setStatus("current")
_DF10FIPSIntfUnicastDiscAdverts_Type = Counter32
_DF10FIPSIntfUnicastDiscAdverts_Object = MibTableColumn
dF10FIPSIntfUnicastDiscAdverts = _DF10FIPSIntfUnicastDiscAdverts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 10),
    _DF10FIPSIntfUnicastDiscAdverts_Type()
)
dF10FIPSIntfUnicastDiscAdverts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfUnicastDiscAdverts.setStatus("current")
_DF10FIPSIntfFLogiAccepts_Type = Counter32
_DF10FIPSIntfFLogiAccepts_Object = MibTableColumn
dF10FIPSIntfFLogiAccepts = _DF10FIPSIntfFLogiAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 11),
    _DF10FIPSIntfFLogiAccepts_Type()
)
dF10FIPSIntfFLogiAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfFLogiAccepts.setStatus("current")
_DF10FIPSIntfFLogiRejects_Type = Counter32
_DF10FIPSIntfFLogiRejects_Object = MibTableColumn
dF10FIPSIntfFLogiRejects = _DF10FIPSIntfFLogiRejects_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 12),
    _DF10FIPSIntfFLogiRejects_Type()
)
dF10FIPSIntfFLogiRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfFLogiRejects.setStatus("current")
_DF10FIPSIntfFDiscAccepts_Type = Counter32
_DF10FIPSIntfFDiscAccepts_Object = MibTableColumn
dF10FIPSIntfFDiscAccepts = _DF10FIPSIntfFDiscAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 13),
    _DF10FIPSIntfFDiscAccepts_Type()
)
dF10FIPSIntfFDiscAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfFDiscAccepts.setStatus("current")
_DF10FIPSIntfFDiscRejects_Type = Counter32
_DF10FIPSIntfFDiscRejects_Object = MibTableColumn
dF10FIPSIntfFDiscRejects = _DF10FIPSIntfFDiscRejects_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 14),
    _DF10FIPSIntfFDiscRejects_Type()
)
dF10FIPSIntfFDiscRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfFDiscRejects.setStatus("current")
_DF10FIPSIntfFLogoutAccepts_Type = Counter32
_DF10FIPSIntfFLogoutAccepts_Object = MibTableColumn
dF10FIPSIntfFLogoutAccepts = _DF10FIPSIntfFLogoutAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 15),
    _DF10FIPSIntfFLogoutAccepts_Type()
)
dF10FIPSIntfFLogoutAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfFLogoutAccepts.setStatus("current")
_DF10FIPSIntfFLogoutRejects_Type = Counter32
_DF10FIPSIntfFLogoutRejects_Object = MibTableColumn
dF10FIPSIntfFLogoutRejects = _DF10FIPSIntfFLogoutRejects_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 16),
    _DF10FIPSIntfFLogoutRejects_Type()
)
dF10FIPSIntfFLogoutRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfFLogoutRejects.setStatus("current")
_DF10FIPSIntfClearVirtLinks_Type = Counter32
_DF10FIPSIntfClearVirtLinks_Object = MibTableColumn
dF10FIPSIntfClearVirtLinks = _DF10FIPSIntfClearVirtLinks_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 17),
    _DF10FIPSIntfClearVirtLinks_Type()
)
dF10FIPSIntfClearVirtLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfClearVirtLinks.setStatus("current")
_DF10FIPSIntfVnPortSeshTimeouts_Type = Counter32
_DF10FIPSIntfVnPortSeshTimeouts_Object = MibTableColumn
dF10FIPSIntfVnPortSeshTimeouts = _DF10FIPSIntfVnPortSeshTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 18),
    _DF10FIPSIntfVnPortSeshTimeouts_Type()
)
dF10FIPSIntfVnPortSeshTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfVnPortSeshTimeouts.setStatus("current")
_DF10FIPSIntfFcfDiscAdvTimeouts_Type = Counter32
_DF10FIPSIntfFcfDiscAdvTimeouts_Object = MibTableColumn
dF10FIPSIntfFcfDiscAdvTimeouts = _DF10FIPSIntfFcfDiscAdvTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 19),
    _DF10FIPSIntfFcfDiscAdvTimeouts_Type()
)
dF10FIPSIntfFcfDiscAdvTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfFcfDiscAdvTimeouts.setStatus("current")
_DF10FIPSIntfSeshFailsDueToHwCfg_Type = Counter32
_DF10FIPSIntfSeshFailsDueToHwCfg_Object = MibTableColumn
dF10FIPSIntfSeshFailsDueToHwCfg = _DF10FIPSIntfSeshFailsDueToHwCfg_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 20),
    _DF10FIPSIntfSeshFailsDueToHwCfg_Type()
)
dF10FIPSIntfSeshFailsDueToHwCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfSeshFailsDueToHwCfg.setStatus("current")
_DF10FIPSIntfSeshDenyFcfLmtRch_Type = Counter32
_DF10FIPSIntfSeshDenyFcfLmtRch_Object = MibTableColumn
dF10FIPSIntfSeshDenyFcfLmtRch = _DF10FIPSIntfSeshDenyFcfLmtRch_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 21),
    _DF10FIPSIntfSeshDenyFcfLmtRch_Type()
)
dF10FIPSIntfSeshDenyFcfLmtRch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfSeshDenyFcfLmtRch.setStatus("current")
_DF10FIPSIntfSeshDenyENodeLmtRch_Type = Counter32
_DF10FIPSIntfSeshDenyENodeLmtRch_Object = MibTableColumn
dF10FIPSIntfSeshDenyENodeLmtRch = _DF10FIPSIntfSeshDenyENodeLmtRch_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 22),
    _DF10FIPSIntfSeshDenyENodeLmtRch_Type()
)
dF10FIPSIntfSeshDenyENodeLmtRch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfSeshDenyENodeLmtRch.setStatus("current")
_DF10FIPSIntfSeshDenySysLmtRch_Type = Counter32
_DF10FIPSIntfSeshDenySysLmtRch_Object = MibTableColumn
dF10FIPSIntfSeshDenySysLmtRch = _DF10FIPSIntfSeshDenySysLmtRch_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 23),
    _DF10FIPSIntfSeshDenySysLmtRch_Type()
)
dF10FIPSIntfSeshDenySysLmtRch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10FIPSIntfSeshDenySysLmtRch.setStatus("current")
_DF10FIPSNotifications_ObjectIdentity = ObjectIdentity
dF10FIPSNotifications = _DF10FIPSNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4)
)
_DF10FIPSTraps_ObjectIdentity = ObjectIdentity
dF10FIPSTraps = _DF10FIPSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 0)
)
_DF10FIPSTrapObjects_ObjectIdentity = ObjectIdentity
dF10FIPSTrapObjects = _DF10FIPSTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 1)
)
_DF10FIPSTrapVlanIndex_Type = Unsigned32
_DF10FIPSTrapVlanIndex_Object = MibScalar
dF10FIPSTrapVlanIndex = _DF10FIPSTrapVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 1, 1),
    _DF10FIPSTrapVlanIndex_Type()
)
dF10FIPSTrapVlanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dF10FIPSTrapVlanIndex.setStatus("current")
_DF10FIPSTrapMacAddr_Type = MacAddress
_DF10FIPSTrapMacAddr_Object = MibScalar
dF10FIPSTrapMacAddr = _DF10FIPSTrapMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 1, 2),
    _DF10FIPSTrapMacAddr_Type()
)
dF10FIPSTrapMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dF10FIPSTrapMacAddr.setStatus("current")
_DF10FIPSMibConformance_ObjectIdentity = ObjectIdentity
dF10FIPSMibConformance = _DF10FIPSMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5)
)
_DF10FIPSMibCompliances_ObjectIdentity = ObjectIdentity
dF10FIPSMibCompliances = _DF10FIPSMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 1)
)
_DF10FIPSMibGroups_ObjectIdentity = ObjectIdentity
dF10FIPSMibGroups = _DF10FIPSMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2)
)

# Managed Objects groups

dF10FIPSCfgObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 1)
)
dF10FIPSCfgObjectGroup.setObjects(
      *(("F10-FIPSNOOPING-MIB", "dF10FIPSAdminMode"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSFCMAP"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSStatsClear"))
)
if mibBuilder.loadTexts:
    dF10FIPSCfgObjectGroup.setStatus("current")

dF10FIPSVlanCfgObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 2)
)
dF10FIPSVlanCfgObjectGroup.setObjects(
      *(("F10-FIPSNOOPING-MIB", "dF10FIPSVlanAdminMode"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanFCMAP"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanStatsClear"))
)
if mibBuilder.loadTexts:
    dF10FIPSVlanCfgObjectGroup.setStatus("current")

dF10FIPSIntfObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 3)
)
dF10FIPSIntfObjectGroup.setObjects(
      *(("F10-FIPSNOOPING-MIB", "dF10FIPSIntfPortModeFcf"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfStatsClear"))
)
if mibBuilder.loadTexts:
    dF10FIPSIntfObjectGroup.setStatus("current")

dF10FIPSSessionObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 4)
)
dF10FIPSSessionObjectGroup.setObjects(
      *(("F10-FIPSNOOPING-MIB", "dF10FIPSSessionENodeIntf"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSSessionFCFIntf"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSSessionTime"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSSessionExpiryTime"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSSessionState"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfStatsClear"))
)
if mibBuilder.loadTexts:
    dF10FIPSSessionObjectGroup.setStatus("current")

dF10FIPSENodeObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 5)
)
dF10FIPSENodeObjectGroup.setObjects(
      *(("F10-FIPSNOOPING-MIB", "dF10FIPSENodeIntf"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSENodeNameID"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSENodeMaxFCoESize"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSENodeConnectedFCFsCount"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSENodeActiveSessions"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSENodeWaitingSessions"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSENodeRejectedSessions"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSENodeTimeSinceDiscovered"))
)
if mibBuilder.loadTexts:
    dF10FIPSENodeObjectGroup.setStatus("current")

dF10FIPSFCFObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 6)
)
dF10FIPSFCFObjectGroup.setObjects(
      *(("F10-FIPSNOOPING-MIB", "dF10FIPSFCFIntf"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSFCFNameID"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSFCFFabricName"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSFCFAddressingMode"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSFCFPriority"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSFCFDbit"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSFCFIsAvailableForLogin"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSFCFConfiguredFKA"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSFCFTimeSinceDiscovered"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSFCFConnectedENodesCount"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSFCFSessions"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSFCFExpiryTime"))
)
if mibBuilder.loadTexts:
    dF10FIPSFCFObjectGroup.setStatus("current")

dF10FIPSVlanStatsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 7)
)
dF10FIPSVlanStatsObjectGroup.setObjects(
      *(("F10-FIPSNOOPING-MIB", "dF10FIPSVlanVlanRequests"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanVlanNotifications"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanMCDiscSolicits"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanUnicastDiscSolicits"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanFLogis"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanFDiscs"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanFLogouts"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanVnPortKeepAlives"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanMCDiscAdverts"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanUnicastDiscAdverts"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanFLogiAccepts"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanFLogiRejects"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanFDiscAccepts"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanFDiscRejects"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanFLogoutAccepts"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanFLogoutRejects"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanClearVirtLinks"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanVnPortSeshTimeouts"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanFcfDiscAdvTimeouts"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanSeshFailsDueToHwCfg"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanSeshDenyFcfLmtRch"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanSeshDenyENodeLmtRch"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSVlanSeshDenySysLmtRch"))
)
if mibBuilder.loadTexts:
    dF10FIPSVlanStatsObjectGroup.setStatus("current")

dF10FIPSIntfStatsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 8)
)
dF10FIPSIntfStatsObjectGroup.setObjects(
      *(("F10-FIPSNOOPING-MIB", "dF10FIPSIntfVlanRequests"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfVlanNotifications"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfMCDiscSolicits"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfUnicastDiscSolicits"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfFLogis"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfFDiscs"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfFLogouts"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfVnPortKeepAlives"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfMCDiscAdverts"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfUnicastDiscAdverts"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfFLogiAccepts"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfFLogiRejects"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfFDiscAccepts"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfFDiscRejects"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfFLogoutAccepts"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfFLogoutRejects"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfClearVirtLinks"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfVnPortSeshTimeouts"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfFcfDiscAdvTimeouts"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfSeshFailsDueToHwCfg"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfSeshDenyFcfLmtRch"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfSeshDenyENodeLmtRch"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSIntfSeshDenySysLmtRch"))
)
if mibBuilder.loadTexts:
    dF10FIPSIntfStatsObjectGroup.setStatus("current")

dF10FIPSTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 10)
)
dF10FIPSTrapObjectsGroup.setObjects(
      *(("F10-FIPSNOOPING-MIB", "dF10FIPSTrapVlanIndex"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSTrapMacAddr"))
)
if mibBuilder.loadTexts:
    dF10FIPSTrapObjectsGroup.setStatus("current")


# Notification objects

dF10MaxFcfsInVlanLmtRchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 0, 1)
)
dF10MaxFcfsInVlanLmtRchTrap.setObjects(
    ("F10-FIPSNOOPING-MIB", "dF10FIPSTrapVlanIndex")
)
if mibBuilder.loadTexts:
    dF10MaxFcfsInVlanLmtRchTrap.setStatus(
        "current"
    )

dF10MaxENodesLmtRchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 0, 2)
)
if mibBuilder.loadTexts:
    dF10MaxENodesLmtRchTrap.setStatus(
        "current"
    )

dF10MaxSessionLmtRchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 0, 3)
)
if mibBuilder.loadTexts:
    dF10MaxSessionLmtRchTrap.setStatus(
        "current"
    )

dF10FcfDroppedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 0, 4)
)
dF10FcfDroppedTrap.setObjects(
      *(("F10-FIPSNOOPING-MIB", "dF10FIPSTrapVlanIndex"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSFCFIntf"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSTrapMacAddr"))
)
if mibBuilder.loadTexts:
    dF10FcfDroppedTrap.setStatus(
        "current"
    )

dF10ENodeDroppedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 0, 5)
)
dF10ENodeDroppedTrap.setObjects(
      *(("F10-FIPSNOOPING-MIB", "dF10FIPSTrapVlanIndex"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSENodeIntf"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSTrapMacAddr"))
)
if mibBuilder.loadTexts:
    dF10ENodeDroppedTrap.setStatus(
        "current"
    )

dF10SessionRequestDroppedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 0, 6)
)
dF10SessionRequestDroppedTrap.setObjects(
      *(("F10-FIPSNOOPING-MIB", "dF10FIPSTrapVlanIndex"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSENodeIntf"),
        ("F10-FIPSNOOPING-MIB", "dF10FIPSTrapMacAddr"))
)
if mibBuilder.loadTexts:
    dF10SessionRequestDroppedTrap.setStatus(
        "current"
    )

dF10AclInstallationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 0, 7)
)
if mibBuilder.loadTexts:
    dF10AclInstallationFailureTrap.setStatus(
        "current"
    )


# Notifications groups

dF10FIPSTrapsObjectGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 9)
)
dF10FIPSTrapsObjectGroup.setObjects(
      *(("F10-FIPSNOOPING-MIB", "dF10MaxFcfsInVlanLmtRchTrap"),
        ("F10-FIPSNOOPING-MIB", "dF10MaxENodesLmtRchTrap"),
        ("F10-FIPSNOOPING-MIB", "dF10MaxSessionLmtRchTrap"),
        ("F10-FIPSNOOPING-MIB", "dF10FcfDroppedTrap"),
        ("F10-FIPSNOOPING-MIB", "dF10ENodeDroppedTrap"),
        ("F10-FIPSNOOPING-MIB", "dF10SessionRequestDroppedTrap"),
        ("F10-FIPSNOOPING-MIB", "dF10AclInstallationFailureTrap"))
)
if mibBuilder.loadTexts:
    dF10FIPSTrapsObjectGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dF10FIPSMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 1, 1)
)
if mibBuilder.loadTexts:
    dF10FIPSMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10-FIPSNOOPING-MIB",
    **{"dF10FipSnooping": dF10FipSnooping,
       "dF10FIPSCfgGroup": dF10FIPSCfgGroup,
       "dF10FIPSAdminMode": dF10FIPSAdminMode,
       "dF10FIPSFCMAP": dF10FIPSFCMAP,
       "dF10FIPSVlanCfgTable": dF10FIPSVlanCfgTable,
       "dF10FIPSVlanCfgEntry": dF10FIPSVlanCfgEntry,
       "dF10FIPSVlanAdminMode": dF10FIPSVlanAdminMode,
       "dF10FIPSVlanFCMAP": dF10FIPSVlanFCMAP,
       "dF10FIPSVlanStatsClear": dF10FIPSVlanStatsClear,
       "dF10FIPSIntfTable": dF10FIPSIntfTable,
       "dF10FIPSIntfEntry": dF10FIPSIntfEntry,
       "dF10FIPSIntfPortModeFcf": dF10FIPSIntfPortModeFcf,
       "dF10FIPSIntfStatsClear": dF10FIPSIntfStatsClear,
       "dF10FIPSStatsClear": dF10FIPSStatsClear,
       "dF10FIPSStatusGroup": dF10FIPSStatusGroup,
       "dF10FIPSSessionTable": dF10FIPSSessionTable,
       "dF10FIPSSessionEntry": dF10FIPSSessionEntry,
       "dF10FIPSSessionVlanIndex": dF10FIPSSessionVlanIndex,
       "dF10FIPSSessionFCFMacAddr": dF10FIPSSessionFCFMacAddr,
       "dF10FIPSSessionENodeMacAddr": dF10FIPSSessionENodeMacAddr,
       "dF10FIPSSessionLoginType": dF10FIPSSessionLoginType,
       "dF10FIPSFCoEMacAddr": dF10FIPSFCoEMacAddr,
       "dF10FIPSSessionTentativeIndex": dF10FIPSSessionTentativeIndex,
       "dF10FIPSSessionFCID": dF10FIPSSessionFCID,
       "dF10FIPSSessionENodeIntf": dF10FIPSSessionENodeIntf,
       "dF10FIPSSessionFCFIntf": dF10FIPSSessionFCFIntf,
       "dF10FIPSSessionTime": dF10FIPSSessionTime,
       "dF10FIPSSessionExpiryTime": dF10FIPSSessionExpiryTime,
       "dF10FIPSSessionState": dF10FIPSSessionState,
       "dF10FIPSENodeTable": dF10FIPSENodeTable,
       "dF10FIPSENodeEntry": dF10FIPSENodeEntry,
       "dF10FIPSENodeVlanIndex": dF10FIPSENodeVlanIndex,
       "dF10FIPSENodeMacAddr": dF10FIPSENodeMacAddr,
       "dF10FIPSENodeIntf": dF10FIPSENodeIntf,
       "dF10FIPSENodeNameID": dF10FIPSENodeNameID,
       "dF10FIPSENodeMaxFCoESize": dF10FIPSENodeMaxFCoESize,
       "dF10FIPSENodeConnectedFCFsCount": dF10FIPSENodeConnectedFCFsCount,
       "dF10FIPSENodeActiveSessions": dF10FIPSENodeActiveSessions,
       "dF10FIPSENodeWaitingSessions": dF10FIPSENodeWaitingSessions,
       "dF10FIPSENodeRejectedSessions": dF10FIPSENodeRejectedSessions,
       "dF10FIPSENodeTimeSinceDiscovered": dF10FIPSENodeTimeSinceDiscovered,
       "dF10FIPSFCFTable": dF10FIPSFCFTable,
       "dF10FIPSFCFEntry": dF10FIPSFCFEntry,
       "dF10FIPSFCFVlanIndex": dF10FIPSFCFVlanIndex,
       "dF10FIPSFCFMacAddr": dF10FIPSFCFMacAddr,
       "dF10FIPSFCFIntf": dF10FIPSFCFIntf,
       "dF10FIPSFCFNameID": dF10FIPSFCFNameID,
       "dF10FIPSFCFFabricName": dF10FIPSFCFFabricName,
       "dF10FIPSFCFAddressingMode": dF10FIPSFCFAddressingMode,
       "dF10FIPSFCFPriority": dF10FIPSFCFPriority,
       "dF10FIPSFCFDbit": dF10FIPSFCFDbit,
       "dF10FIPSFCFIsAvailableForLogin": dF10FIPSFCFIsAvailableForLogin,
       "dF10FIPSFCFConfiguredFKA": dF10FIPSFCFConfiguredFKA,
       "dF10FIPSFCFTimeSinceDiscovered": dF10FIPSFCFTimeSinceDiscovered,
       "dF10FIPSFCFConnectedENodesCount": dF10FIPSFCFConnectedENodesCount,
       "dF10FIPSFCFSessions": dF10FIPSFCFSessions,
       "dF10FIPSFCFExpiryTime": dF10FIPSFCFExpiryTime,
       "dF10FIPSStatisticsGroup": dF10FIPSStatisticsGroup,
       "dF10FIPSVlanStatsTable": dF10FIPSVlanStatsTable,
       "dF10FIPSVlanStatsEntry": dF10FIPSVlanStatsEntry,
       "dF10FIPSVlanVlanRequests": dF10FIPSVlanVlanRequests,
       "dF10FIPSVlanVlanNotifications": dF10FIPSVlanVlanNotifications,
       "dF10FIPSVlanMCDiscSolicits": dF10FIPSVlanMCDiscSolicits,
       "dF10FIPSVlanUnicastDiscSolicits": dF10FIPSVlanUnicastDiscSolicits,
       "dF10FIPSVlanFLogis": dF10FIPSVlanFLogis,
       "dF10FIPSVlanFDiscs": dF10FIPSVlanFDiscs,
       "dF10FIPSVlanFLogouts": dF10FIPSVlanFLogouts,
       "dF10FIPSVlanVnPortKeepAlives": dF10FIPSVlanVnPortKeepAlives,
       "dF10FIPSVlanMCDiscAdverts": dF10FIPSVlanMCDiscAdverts,
       "dF10FIPSVlanUnicastDiscAdverts": dF10FIPSVlanUnicastDiscAdverts,
       "dF10FIPSVlanFLogiAccepts": dF10FIPSVlanFLogiAccepts,
       "dF10FIPSVlanFLogiRejects": dF10FIPSVlanFLogiRejects,
       "dF10FIPSVlanFDiscAccepts": dF10FIPSVlanFDiscAccepts,
       "dF10FIPSVlanFDiscRejects": dF10FIPSVlanFDiscRejects,
       "dF10FIPSVlanFLogoutAccepts": dF10FIPSVlanFLogoutAccepts,
       "dF10FIPSVlanFLogoutRejects": dF10FIPSVlanFLogoutRejects,
       "dF10FIPSVlanClearVirtLinks": dF10FIPSVlanClearVirtLinks,
       "dF10FIPSVlanVnPortSeshTimeouts": dF10FIPSVlanVnPortSeshTimeouts,
       "dF10FIPSVlanFcfDiscAdvTimeouts": dF10FIPSVlanFcfDiscAdvTimeouts,
       "dF10FIPSVlanSeshFailsDueToHwCfg": dF10FIPSVlanSeshFailsDueToHwCfg,
       "dF10FIPSVlanSeshDenyFcfLmtRch": dF10FIPSVlanSeshDenyFcfLmtRch,
       "dF10FIPSVlanSeshDenyENodeLmtRch": dF10FIPSVlanSeshDenyENodeLmtRch,
       "dF10FIPSVlanSeshDenySysLmtRch": dF10FIPSVlanSeshDenySysLmtRch,
       "dF10FIPSIntfStatsTable": dF10FIPSIntfStatsTable,
       "dF10FIPSIntfStatsEntry": dF10FIPSIntfStatsEntry,
       "dF10FIPSIntfVlanRequests": dF10FIPSIntfVlanRequests,
       "dF10FIPSIntfVlanNotifications": dF10FIPSIntfVlanNotifications,
       "dF10FIPSIntfMCDiscSolicits": dF10FIPSIntfMCDiscSolicits,
       "dF10FIPSIntfUnicastDiscSolicits": dF10FIPSIntfUnicastDiscSolicits,
       "dF10FIPSIntfFLogis": dF10FIPSIntfFLogis,
       "dF10FIPSIntfFDiscs": dF10FIPSIntfFDiscs,
       "dF10FIPSIntfFLogouts": dF10FIPSIntfFLogouts,
       "dF10FIPSIntfVnPortKeepAlives": dF10FIPSIntfVnPortKeepAlives,
       "dF10FIPSIntfMCDiscAdverts": dF10FIPSIntfMCDiscAdverts,
       "dF10FIPSIntfUnicastDiscAdverts": dF10FIPSIntfUnicastDiscAdverts,
       "dF10FIPSIntfFLogiAccepts": dF10FIPSIntfFLogiAccepts,
       "dF10FIPSIntfFLogiRejects": dF10FIPSIntfFLogiRejects,
       "dF10FIPSIntfFDiscAccepts": dF10FIPSIntfFDiscAccepts,
       "dF10FIPSIntfFDiscRejects": dF10FIPSIntfFDiscRejects,
       "dF10FIPSIntfFLogoutAccepts": dF10FIPSIntfFLogoutAccepts,
       "dF10FIPSIntfFLogoutRejects": dF10FIPSIntfFLogoutRejects,
       "dF10FIPSIntfClearVirtLinks": dF10FIPSIntfClearVirtLinks,
       "dF10FIPSIntfVnPortSeshTimeouts": dF10FIPSIntfVnPortSeshTimeouts,
       "dF10FIPSIntfFcfDiscAdvTimeouts": dF10FIPSIntfFcfDiscAdvTimeouts,
       "dF10FIPSIntfSeshFailsDueToHwCfg": dF10FIPSIntfSeshFailsDueToHwCfg,
       "dF10FIPSIntfSeshDenyFcfLmtRch": dF10FIPSIntfSeshDenyFcfLmtRch,
       "dF10FIPSIntfSeshDenyENodeLmtRch": dF10FIPSIntfSeshDenyENodeLmtRch,
       "dF10FIPSIntfSeshDenySysLmtRch": dF10FIPSIntfSeshDenySysLmtRch,
       "dF10FIPSNotifications": dF10FIPSNotifications,
       "dF10FIPSTraps": dF10FIPSTraps,
       "dF10MaxFcfsInVlanLmtRchTrap": dF10MaxFcfsInVlanLmtRchTrap,
       "dF10MaxENodesLmtRchTrap": dF10MaxENodesLmtRchTrap,
       "dF10MaxSessionLmtRchTrap": dF10MaxSessionLmtRchTrap,
       "dF10FcfDroppedTrap": dF10FcfDroppedTrap,
       "dF10ENodeDroppedTrap": dF10ENodeDroppedTrap,
       "dF10SessionRequestDroppedTrap": dF10SessionRequestDroppedTrap,
       "dF10AclInstallationFailureTrap": dF10AclInstallationFailureTrap,
       "dF10FIPSTrapObjects": dF10FIPSTrapObjects,
       "dF10FIPSTrapVlanIndex": dF10FIPSTrapVlanIndex,
       "dF10FIPSTrapMacAddr": dF10FIPSTrapMacAddr,
       "dF10FIPSMibConformance": dF10FIPSMibConformance,
       "dF10FIPSMibCompliances": dF10FIPSMibCompliances,
       "dF10FIPSMibCompliance": dF10FIPSMibCompliance,
       "dF10FIPSMibGroups": dF10FIPSMibGroups,
       "dF10FIPSCfgObjectGroup": dF10FIPSCfgObjectGroup,
       "dF10FIPSVlanCfgObjectGroup": dF10FIPSVlanCfgObjectGroup,
       "dF10FIPSIntfObjectGroup": dF10FIPSIntfObjectGroup,
       "dF10FIPSSessionObjectGroup": dF10FIPSSessionObjectGroup,
       "dF10FIPSENodeObjectGroup": dF10FIPSENodeObjectGroup,
       "dF10FIPSFCFObjectGroup": dF10FIPSFCFObjectGroup,
       "dF10FIPSVlanStatsObjectGroup": dF10FIPSVlanStatsObjectGroup,
       "dF10FIPSIntfStatsObjectGroup": dF10FIPSIntfStatsObjectGroup,
       "dF10FIPSTrapsObjectGroup": dF10FIPSTrapsObjectGroup,
       "dF10FIPSTrapObjectsGroup": dF10FIPSTrapObjectsGroup}
)
