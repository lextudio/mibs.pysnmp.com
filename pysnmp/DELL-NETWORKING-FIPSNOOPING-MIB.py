# SNMP MIB module (DELL-NETWORKING-FIPSNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-NETWORKING-FIPSNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:53 2024
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

(dellNetMgmt,) = mibBuilder.importSymbols(
    "DELL-NETWORKING-SMI",
    "dellNetMgmt")

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

dellNetFipSnooping = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22)
)
dellNetFipSnooping.setRevisions(
        ("2011-12-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DellNetFIPSCfgGroup_ObjectIdentity = ObjectIdentity
dellNetFIPSCfgGroup = _DellNetFIPSCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1)
)


class _DellNetFIPSAdminMode_Type(Integer32):
    """Custom type dellNetFIPSAdminMode based on Integer32"""
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


_DellNetFIPSAdminMode_Type.__name__ = "Integer32"
_DellNetFIPSAdminMode_Object = MibScalar
dellNetFIPSAdminMode = _DellNetFIPSAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 1),
    _DellNetFIPSAdminMode_Type()
)
dellNetFIPSAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetFIPSAdminMode.setStatus("current")


class _DellNetFIPSFCMAP_Type(OctetString):
    """Custom type dellNetFIPSFCMAP based on OctetString"""
    defaultValue = OctetString("0x0EFC00")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_DellNetFIPSFCMAP_Type.__name__ = "OctetString"
_DellNetFIPSFCMAP_Object = MibScalar
dellNetFIPSFCMAP = _DellNetFIPSFCMAP_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 2),
    _DellNetFIPSFCMAP_Type()
)
dellNetFIPSFCMAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetFIPSFCMAP.setStatus("current")
_DellNetFIPSVlanCfgTable_Object = MibTable
dellNetFIPSVlanCfgTable = _DellNetFIPSVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 3)
)
if mibBuilder.loadTexts:
    dellNetFIPSVlanCfgTable.setStatus("current")
_DellNetFIPSVlanCfgEntry_Object = MibTableRow
dellNetFIPSVlanCfgEntry = _DellNetFIPSVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 3, 1)
)
dellNetFIPSVlanCfgEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dellNetFIPSVlanCfgEntry.setStatus("current")


class _DellNetFIPSVlanAdminMode_Type(Integer32):
    """Custom type dellNetFIPSVlanAdminMode based on Integer32"""
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


_DellNetFIPSVlanAdminMode_Type.__name__ = "Integer32"
_DellNetFIPSVlanAdminMode_Object = MibTableColumn
dellNetFIPSVlanAdminMode = _DellNetFIPSVlanAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 3, 1, 1),
    _DellNetFIPSVlanAdminMode_Type()
)
dellNetFIPSVlanAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetFIPSVlanAdminMode.setStatus("current")


class _DellNetFIPSVlanFCMAP_Type(OctetString):
    """Custom type dellNetFIPSVlanFCMAP based on OctetString"""
    defaultValue = OctetString("0x0EFC00")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_DellNetFIPSVlanFCMAP_Type.__name__ = "OctetString"
_DellNetFIPSVlanFCMAP_Object = MibTableColumn
dellNetFIPSVlanFCMAP = _DellNetFIPSVlanFCMAP_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 3, 1, 2),
    _DellNetFIPSVlanFCMAP_Type()
)
dellNetFIPSVlanFCMAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetFIPSVlanFCMAP.setStatus("current")


class _DellNetFIPSVlanStatsClear_Type(Integer32):
    """Custom type dellNetFIPSVlanStatsClear based on Integer32"""
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


_DellNetFIPSVlanStatsClear_Type.__name__ = "Integer32"
_DellNetFIPSVlanStatsClear_Object = MibTableColumn
dellNetFIPSVlanStatsClear = _DellNetFIPSVlanStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 3, 1, 3),
    _DellNetFIPSVlanStatsClear_Type()
)
dellNetFIPSVlanStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetFIPSVlanStatsClear.setStatus("current")
_DellNetFIPSIntfTable_Object = MibTable
dellNetFIPSIntfTable = _DellNetFIPSIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 4)
)
if mibBuilder.loadTexts:
    dellNetFIPSIntfTable.setStatus("current")
_DellNetFIPSIntfEntry_Object = MibTableRow
dellNetFIPSIntfEntry = _DellNetFIPSIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 4, 1)
)
dellNetFIPSIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dellNetFIPSIntfEntry.setStatus("current")


class _DellNetFIPSIntfPortModeFcf_Type(Integer32):
    """Custom type dellNetFIPSIntfPortModeFcf based on Integer32"""
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


_DellNetFIPSIntfPortModeFcf_Type.__name__ = "Integer32"
_DellNetFIPSIntfPortModeFcf_Object = MibTableColumn
dellNetFIPSIntfPortModeFcf = _DellNetFIPSIntfPortModeFcf_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 4, 1, 2),
    _DellNetFIPSIntfPortModeFcf_Type()
)
dellNetFIPSIntfPortModeFcf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetFIPSIntfPortModeFcf.setStatus("current")


class _DellNetFIPSIntfStatsClear_Type(Integer32):
    """Custom type dellNetFIPSIntfStatsClear based on Integer32"""
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


_DellNetFIPSIntfStatsClear_Type.__name__ = "Integer32"
_DellNetFIPSIntfStatsClear_Object = MibTableColumn
dellNetFIPSIntfStatsClear = _DellNetFIPSIntfStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 4, 1, 3),
    _DellNetFIPSIntfStatsClear_Type()
)
dellNetFIPSIntfStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetFIPSIntfStatsClear.setStatus("current")


class _DellNetFIPSStatsClear_Type(Integer32):
    """Custom type dellNetFIPSStatsClear based on Integer32"""
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


_DellNetFIPSStatsClear_Type.__name__ = "Integer32"
_DellNetFIPSStatsClear_Object = MibScalar
dellNetFIPSStatsClear = _DellNetFIPSStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 1, 5),
    _DellNetFIPSStatsClear_Type()
)
dellNetFIPSStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetFIPSStatsClear.setStatus("current")
_DellNetFIPSStatusGroup_ObjectIdentity = ObjectIdentity
dellNetFIPSStatusGroup = _DellNetFIPSStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2)
)
_DellNetFIPSSessionTable_Object = MibTable
dellNetFIPSSessionTable = _DellNetFIPSSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1)
)
if mibBuilder.loadTexts:
    dellNetFIPSSessionTable.setStatus("current")
_DellNetFIPSSessionEntry_Object = MibTableRow
dellNetFIPSSessionEntry = _DellNetFIPSSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1)
)
dellNetFIPSSessionEntry.setIndexNames(
    (0, "DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSSessionVlanIndex"),
    (0, "DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSSessionFCFMacAddr"),
    (0, "DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSSessionENodeMacAddr"),
    (0, "DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSSessionLoginType"),
    (0, "DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSFCoEMacAddr"),
    (0, "DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSSessionTentativeIndex"),
    (0, "DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSSessionFCID"),
)
if mibBuilder.loadTexts:
    dellNetFIPSSessionEntry.setStatus("current")
_DellNetFIPSSessionVlanIndex_Type = Unsigned32
_DellNetFIPSSessionVlanIndex_Object = MibTableColumn
dellNetFIPSSessionVlanIndex = _DellNetFIPSSessionVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 1),
    _DellNetFIPSSessionVlanIndex_Type()
)
dellNetFIPSSessionVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetFIPSSessionVlanIndex.setStatus("current")
_DellNetFIPSSessionFCFMacAddr_Type = MacAddress
_DellNetFIPSSessionFCFMacAddr_Object = MibTableColumn
dellNetFIPSSessionFCFMacAddr = _DellNetFIPSSessionFCFMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 2),
    _DellNetFIPSSessionFCFMacAddr_Type()
)
dellNetFIPSSessionFCFMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetFIPSSessionFCFMacAddr.setStatus("current")
_DellNetFIPSSessionENodeMacAddr_Type = MacAddress
_DellNetFIPSSessionENodeMacAddr_Object = MibTableColumn
dellNetFIPSSessionENodeMacAddr = _DellNetFIPSSessionENodeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 3),
    _DellNetFIPSSessionENodeMacAddr_Type()
)
dellNetFIPSSessionENodeMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetFIPSSessionENodeMacAddr.setStatus("current")


class _DellNetFIPSSessionLoginType_Type(Integer32):
    """Custom type dellNetFIPSSessionLoginType based on Integer32"""
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


_DellNetFIPSSessionLoginType_Type.__name__ = "Integer32"
_DellNetFIPSSessionLoginType_Object = MibTableColumn
dellNetFIPSSessionLoginType = _DellNetFIPSSessionLoginType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 4),
    _DellNetFIPSSessionLoginType_Type()
)
dellNetFIPSSessionLoginType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetFIPSSessionLoginType.setStatus("current")
_DellNetFIPSFCoEMacAddr_Type = MacAddress
_DellNetFIPSFCoEMacAddr_Object = MibTableColumn
dellNetFIPSFCoEMacAddr = _DellNetFIPSFCoEMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 5),
    _DellNetFIPSFCoEMacAddr_Type()
)
dellNetFIPSFCoEMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetFIPSFCoEMacAddr.setStatus("current")
_DellNetFIPSSessionTentativeIndex_Type = Unsigned32
_DellNetFIPSSessionTentativeIndex_Object = MibTableColumn
dellNetFIPSSessionTentativeIndex = _DellNetFIPSSessionTentativeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 6),
    _DellNetFIPSSessionTentativeIndex_Type()
)
dellNetFIPSSessionTentativeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetFIPSSessionTentativeIndex.setStatus("current")


class _DellNetFIPSSessionFCID_Type(OctetString):
    """Custom type dellNetFIPSSessionFCID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_DellNetFIPSSessionFCID_Type.__name__ = "OctetString"
_DellNetFIPSSessionFCID_Object = MibTableColumn
dellNetFIPSSessionFCID = _DellNetFIPSSessionFCID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 7),
    _DellNetFIPSSessionFCID_Type()
)
dellNetFIPSSessionFCID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetFIPSSessionFCID.setStatus("current")
_DellNetFIPSSessionENodeIntf_Type = Unsigned32
_DellNetFIPSSessionENodeIntf_Object = MibTableColumn
dellNetFIPSSessionENodeIntf = _DellNetFIPSSessionENodeIntf_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 8),
    _DellNetFIPSSessionENodeIntf_Type()
)
dellNetFIPSSessionENodeIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSSessionENodeIntf.setStatus("current")
_DellNetFIPSSessionFCFIntf_Type = Unsigned32
_DellNetFIPSSessionFCFIntf_Object = MibTableColumn
dellNetFIPSSessionFCFIntf = _DellNetFIPSSessionFCFIntf_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 9),
    _DellNetFIPSSessionFCFIntf_Type()
)
dellNetFIPSSessionFCFIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSSessionFCFIntf.setStatus("current")
_DellNetFIPSSessionTime_Type = DateAndTime
_DellNetFIPSSessionTime_Object = MibTableColumn
dellNetFIPSSessionTime = _DellNetFIPSSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 10),
    _DellNetFIPSSessionTime_Type()
)
dellNetFIPSSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSSessionTime.setStatus("current")


class _DellNetFIPSSessionExpiryTime_Type(Integer32):
    """Custom type dellNetFIPSSessionExpiryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 450),
    )


_DellNetFIPSSessionExpiryTime_Type.__name__ = "Integer32"
_DellNetFIPSSessionExpiryTime_Object = MibTableColumn
dellNetFIPSSessionExpiryTime = _DellNetFIPSSessionExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 11),
    _DellNetFIPSSessionExpiryTime_Type()
)
dellNetFIPSSessionExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSSessionExpiryTime.setStatus("current")
_DellNetFIPSSessionState_Type = OctetString
_DellNetFIPSSessionState_Object = MibTableColumn
dellNetFIPSSessionState = _DellNetFIPSSessionState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 1, 1, 12),
    _DellNetFIPSSessionState_Type()
)
dellNetFIPSSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSSessionState.setStatus("current")
_DellNetFIPSENodeTable_Object = MibTable
dellNetFIPSENodeTable = _DellNetFIPSENodeTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2)
)
if mibBuilder.loadTexts:
    dellNetFIPSENodeTable.setStatus("current")
_DellNetFIPSENodeEntry_Object = MibTableRow
dellNetFIPSENodeEntry = _DellNetFIPSENodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1)
)
dellNetFIPSENodeEntry.setIndexNames(
    (0, "DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSENodeVlanIndex"),
    (0, "DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSENodeMacAddr"),
)
if mibBuilder.loadTexts:
    dellNetFIPSENodeEntry.setStatus("current")
_DellNetFIPSENodeVlanIndex_Type = Unsigned32
_DellNetFIPSENodeVlanIndex_Object = MibTableColumn
dellNetFIPSENodeVlanIndex = _DellNetFIPSENodeVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 1),
    _DellNetFIPSENodeVlanIndex_Type()
)
dellNetFIPSENodeVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetFIPSENodeVlanIndex.setStatus("current")
_DellNetFIPSENodeMacAddr_Type = MacAddress
_DellNetFIPSENodeMacAddr_Object = MibTableColumn
dellNetFIPSENodeMacAddr = _DellNetFIPSENodeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 2),
    _DellNetFIPSENodeMacAddr_Type()
)
dellNetFIPSENodeMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetFIPSENodeMacAddr.setStatus("current")
_DellNetFIPSENodeIntf_Type = Unsigned32
_DellNetFIPSENodeIntf_Object = MibTableColumn
dellNetFIPSENodeIntf = _DellNetFIPSENodeIntf_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 3),
    _DellNetFIPSENodeIntf_Type()
)
dellNetFIPSENodeIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSENodeIntf.setStatus("current")
_DellNetFIPSENodeNameID_Type = OctetString
_DellNetFIPSENodeNameID_Object = MibTableColumn
dellNetFIPSENodeNameID = _DellNetFIPSENodeNameID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 4),
    _DellNetFIPSENodeNameID_Type()
)
dellNetFIPSENodeNameID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSENodeNameID.setStatus("current")
_DellNetFIPSENodeMaxFCoESize_Type = Unsigned32
_DellNetFIPSENodeMaxFCoESize_Object = MibTableColumn
dellNetFIPSENodeMaxFCoESize = _DellNetFIPSENodeMaxFCoESize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 5),
    _DellNetFIPSENodeMaxFCoESize_Type()
)
dellNetFIPSENodeMaxFCoESize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSENodeMaxFCoESize.setStatus("current")
_DellNetFIPSENodeConnectedFCFsCount_Type = Unsigned32
_DellNetFIPSENodeConnectedFCFsCount_Object = MibTableColumn
dellNetFIPSENodeConnectedFCFsCount = _DellNetFIPSENodeConnectedFCFsCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 6),
    _DellNetFIPSENodeConnectedFCFsCount_Type()
)
dellNetFIPSENodeConnectedFCFsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSENodeConnectedFCFsCount.setStatus("current")
_DellNetFIPSENodeActiveSessions_Type = Unsigned32
_DellNetFIPSENodeActiveSessions_Object = MibTableColumn
dellNetFIPSENodeActiveSessions = _DellNetFIPSENodeActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 7),
    _DellNetFIPSENodeActiveSessions_Type()
)
dellNetFIPSENodeActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSENodeActiveSessions.setStatus("current")
_DellNetFIPSENodeWaitingSessions_Type = Unsigned32
_DellNetFIPSENodeWaitingSessions_Object = MibTableColumn
dellNetFIPSENodeWaitingSessions = _DellNetFIPSENodeWaitingSessions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 8),
    _DellNetFIPSENodeWaitingSessions_Type()
)
dellNetFIPSENodeWaitingSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSENodeWaitingSessions.setStatus("current")
_DellNetFIPSENodeRejectedSessions_Type = Unsigned32
_DellNetFIPSENodeRejectedSessions_Object = MibTableColumn
dellNetFIPSENodeRejectedSessions = _DellNetFIPSENodeRejectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 9),
    _DellNetFIPSENodeRejectedSessions_Type()
)
dellNetFIPSENodeRejectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSENodeRejectedSessions.setStatus("current")
_DellNetFIPSENodeTimeSinceDiscovered_Type = DateAndTime
_DellNetFIPSENodeTimeSinceDiscovered_Object = MibTableColumn
dellNetFIPSENodeTimeSinceDiscovered = _DellNetFIPSENodeTimeSinceDiscovered_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 2, 1, 10),
    _DellNetFIPSENodeTimeSinceDiscovered_Type()
)
dellNetFIPSENodeTimeSinceDiscovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSENodeTimeSinceDiscovered.setStatus("current")
_DellNetFIPSFCFTable_Object = MibTable
dellNetFIPSFCFTable = _DellNetFIPSFCFTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3)
)
if mibBuilder.loadTexts:
    dellNetFIPSFCFTable.setStatus("current")
_DellNetFIPSFCFEntry_Object = MibTableRow
dellNetFIPSFCFEntry = _DellNetFIPSFCFEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1)
)
dellNetFIPSFCFEntry.setIndexNames(
    (0, "DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSFCFVlanIndex"),
    (0, "DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSFCFMacAddr"),
)
if mibBuilder.loadTexts:
    dellNetFIPSFCFEntry.setStatus("current")
_DellNetFIPSFCFVlanIndex_Type = Unsigned32
_DellNetFIPSFCFVlanIndex_Object = MibTableColumn
dellNetFIPSFCFVlanIndex = _DellNetFIPSFCFVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 1),
    _DellNetFIPSFCFVlanIndex_Type()
)
dellNetFIPSFCFVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetFIPSFCFVlanIndex.setStatus("current")
_DellNetFIPSFCFMacAddr_Type = MacAddress
_DellNetFIPSFCFMacAddr_Object = MibTableColumn
dellNetFIPSFCFMacAddr = _DellNetFIPSFCFMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 2),
    _DellNetFIPSFCFMacAddr_Type()
)
dellNetFIPSFCFMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetFIPSFCFMacAddr.setStatus("current")
_DellNetFIPSFCFIntf_Type = Unsigned32
_DellNetFIPSFCFIntf_Object = MibTableColumn
dellNetFIPSFCFIntf = _DellNetFIPSFCFIntf_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 3),
    _DellNetFIPSFCFIntf_Type()
)
dellNetFIPSFCFIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSFCFIntf.setStatus("current")
_DellNetFIPSFCFNameID_Type = OctetString
_DellNetFIPSFCFNameID_Object = MibTableColumn
dellNetFIPSFCFNameID = _DellNetFIPSFCFNameID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 4),
    _DellNetFIPSFCFNameID_Type()
)
dellNetFIPSFCFNameID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSFCFNameID.setStatus("current")
_DellNetFIPSFCFFabricName_Type = OctetString
_DellNetFIPSFCFFabricName_Object = MibTableColumn
dellNetFIPSFCFFabricName = _DellNetFIPSFCFFabricName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 5),
    _DellNetFIPSFCFFabricName_Type()
)
dellNetFIPSFCFFabricName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSFCFFabricName.setStatus("current")


class _DellNetFIPSFCFAddressingMode_Type(Integer32):
    """Custom type dellNetFIPSFCFAddressingMode based on Integer32"""
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


_DellNetFIPSFCFAddressingMode_Type.__name__ = "Integer32"
_DellNetFIPSFCFAddressingMode_Object = MibTableColumn
dellNetFIPSFCFAddressingMode = _DellNetFIPSFCFAddressingMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 6),
    _DellNetFIPSFCFAddressingMode_Type()
)
dellNetFIPSFCFAddressingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSFCFAddressingMode.setStatus("current")


class _DellNetFIPSFCFPriority_Type(Integer32):
    """Custom type dellNetFIPSFCFPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DellNetFIPSFCFPriority_Type.__name__ = "Integer32"
_DellNetFIPSFCFPriority_Object = MibTableColumn
dellNetFIPSFCFPriority = _DellNetFIPSFCFPriority_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 7),
    _DellNetFIPSFCFPriority_Type()
)
dellNetFIPSFCFPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSFCFPriority.setStatus("current")


class _DellNetFIPSFCFDbit_Type(Integer32):
    """Custom type dellNetFIPSFCFDbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DellNetFIPSFCFDbit_Type.__name__ = "Integer32"
_DellNetFIPSFCFDbit_Object = MibTableColumn
dellNetFIPSFCFDbit = _DellNetFIPSFCFDbit_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 8),
    _DellNetFIPSFCFDbit_Type()
)
dellNetFIPSFCFDbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSFCFDbit.setStatus("current")


class _DellNetFIPSFCFIsAvailableForLogin_Type(Integer32):
    """Custom type dellNetFIPSFCFIsAvailableForLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DellNetFIPSFCFIsAvailableForLogin_Type.__name__ = "Integer32"
_DellNetFIPSFCFIsAvailableForLogin_Object = MibTableColumn
dellNetFIPSFCFIsAvailableForLogin = _DellNetFIPSFCFIsAvailableForLogin_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 9),
    _DellNetFIPSFCFIsAvailableForLogin_Type()
)
dellNetFIPSFCFIsAvailableForLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSFCFIsAvailableForLogin.setStatus("current")


class _DellNetFIPSFCFConfiguredFKA_Type(Integer32):
    """Custom type dellNetFIPSFCFConfiguredFKA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 450),
    )


_DellNetFIPSFCFConfiguredFKA_Type.__name__ = "Integer32"
_DellNetFIPSFCFConfiguredFKA_Object = MibTableColumn
dellNetFIPSFCFConfiguredFKA = _DellNetFIPSFCFConfiguredFKA_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 10),
    _DellNetFIPSFCFConfiguredFKA_Type()
)
dellNetFIPSFCFConfiguredFKA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSFCFConfiguredFKA.setStatus("current")
_DellNetFIPSFCFTimeSinceDiscovered_Type = DateAndTime
_DellNetFIPSFCFTimeSinceDiscovered_Object = MibTableColumn
dellNetFIPSFCFTimeSinceDiscovered = _DellNetFIPSFCFTimeSinceDiscovered_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 11),
    _DellNetFIPSFCFTimeSinceDiscovered_Type()
)
dellNetFIPSFCFTimeSinceDiscovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSFCFTimeSinceDiscovered.setStatus("current")
_DellNetFIPSFCFConnectedENodesCount_Type = Unsigned32
_DellNetFIPSFCFConnectedENodesCount_Object = MibTableColumn
dellNetFIPSFCFConnectedENodesCount = _DellNetFIPSFCFConnectedENodesCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 12),
    _DellNetFIPSFCFConnectedENodesCount_Type()
)
dellNetFIPSFCFConnectedENodesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSFCFConnectedENodesCount.setStatus("current")
_DellNetFIPSFCFSessions_Type = Unsigned32
_DellNetFIPSFCFSessions_Object = MibTableColumn
dellNetFIPSFCFSessions = _DellNetFIPSFCFSessions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 13),
    _DellNetFIPSFCFSessions_Type()
)
dellNetFIPSFCFSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSFCFSessions.setStatus("current")
_DellNetFIPSFCFExpiryTime_Type = Unsigned32
_DellNetFIPSFCFExpiryTime_Object = MibTableColumn
dellNetFIPSFCFExpiryTime = _DellNetFIPSFCFExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 2, 3, 1, 14),
    _DellNetFIPSFCFExpiryTime_Type()
)
dellNetFIPSFCFExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSFCFExpiryTime.setStatus("current")
_DellNetFIPSStatisticsGroup_ObjectIdentity = ObjectIdentity
dellNetFIPSStatisticsGroup = _DellNetFIPSStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3)
)
_DellNetFIPSVlanStatsTable_Object = MibTable
dellNetFIPSVlanStatsTable = _DellNetFIPSVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1)
)
if mibBuilder.loadTexts:
    dellNetFIPSVlanStatsTable.setStatus("current")
_DellNetFIPSVlanStatsEntry_Object = MibTableRow
dellNetFIPSVlanStatsEntry = _DellNetFIPSVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1)
)
dellNetFIPSVlanStatsEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dellNetFIPSVlanStatsEntry.setStatus("current")
_DellNetFIPSVlanVlanRequests_Type = Counter32
_DellNetFIPSVlanVlanRequests_Object = MibTableColumn
dellNetFIPSVlanVlanRequests = _DellNetFIPSVlanVlanRequests_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 1),
    _DellNetFIPSVlanVlanRequests_Type()
)
dellNetFIPSVlanVlanRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanVlanRequests.setStatus("current")
_DellNetFIPSVlanVlanNotifications_Type = Counter32
_DellNetFIPSVlanVlanNotifications_Object = MibTableColumn
dellNetFIPSVlanVlanNotifications = _DellNetFIPSVlanVlanNotifications_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 2),
    _DellNetFIPSVlanVlanNotifications_Type()
)
dellNetFIPSVlanVlanNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanVlanNotifications.setStatus("current")
_DellNetFIPSVlanMCDiscSolicits_Type = Counter32
_DellNetFIPSVlanMCDiscSolicits_Object = MibTableColumn
dellNetFIPSVlanMCDiscSolicits = _DellNetFIPSVlanMCDiscSolicits_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 3),
    _DellNetFIPSVlanMCDiscSolicits_Type()
)
dellNetFIPSVlanMCDiscSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanMCDiscSolicits.setStatus("current")
_DellNetFIPSVlanUnicastDiscSolicits_Type = Counter32
_DellNetFIPSVlanUnicastDiscSolicits_Object = MibTableColumn
dellNetFIPSVlanUnicastDiscSolicits = _DellNetFIPSVlanUnicastDiscSolicits_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 4),
    _DellNetFIPSVlanUnicastDiscSolicits_Type()
)
dellNetFIPSVlanUnicastDiscSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanUnicastDiscSolicits.setStatus("current")
_DellNetFIPSVlanFLogis_Type = Counter32
_DellNetFIPSVlanFLogis_Object = MibTableColumn
dellNetFIPSVlanFLogis = _DellNetFIPSVlanFLogis_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 5),
    _DellNetFIPSVlanFLogis_Type()
)
dellNetFIPSVlanFLogis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanFLogis.setStatus("current")
_DellNetFIPSVlanFDiscs_Type = Counter32
_DellNetFIPSVlanFDiscs_Object = MibTableColumn
dellNetFIPSVlanFDiscs = _DellNetFIPSVlanFDiscs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 6),
    _DellNetFIPSVlanFDiscs_Type()
)
dellNetFIPSVlanFDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanFDiscs.setStatus("current")
_DellNetFIPSVlanFLogouts_Type = Counter32
_DellNetFIPSVlanFLogouts_Object = MibTableColumn
dellNetFIPSVlanFLogouts = _DellNetFIPSVlanFLogouts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 7),
    _DellNetFIPSVlanFLogouts_Type()
)
dellNetFIPSVlanFLogouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanFLogouts.setStatus("current")
_DellNetFIPSVlanVnPortKeepAlives_Type = Counter32
_DellNetFIPSVlanVnPortKeepAlives_Object = MibTableColumn
dellNetFIPSVlanVnPortKeepAlives = _DellNetFIPSVlanVnPortKeepAlives_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 8),
    _DellNetFIPSVlanVnPortKeepAlives_Type()
)
dellNetFIPSVlanVnPortKeepAlives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanVnPortKeepAlives.setStatus("current")
_DellNetFIPSVlanMCDiscAdverts_Type = Counter32
_DellNetFIPSVlanMCDiscAdverts_Object = MibTableColumn
dellNetFIPSVlanMCDiscAdverts = _DellNetFIPSVlanMCDiscAdverts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 9),
    _DellNetFIPSVlanMCDiscAdverts_Type()
)
dellNetFIPSVlanMCDiscAdverts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanMCDiscAdverts.setStatus("current")
_DellNetFIPSVlanUnicastDiscAdverts_Type = Counter32
_DellNetFIPSVlanUnicastDiscAdverts_Object = MibTableColumn
dellNetFIPSVlanUnicastDiscAdverts = _DellNetFIPSVlanUnicastDiscAdverts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 10),
    _DellNetFIPSVlanUnicastDiscAdverts_Type()
)
dellNetFIPSVlanUnicastDiscAdverts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanUnicastDiscAdverts.setStatus("current")
_DellNetFIPSVlanFLogiAccepts_Type = Counter32
_DellNetFIPSVlanFLogiAccepts_Object = MibTableColumn
dellNetFIPSVlanFLogiAccepts = _DellNetFIPSVlanFLogiAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 11),
    _DellNetFIPSVlanFLogiAccepts_Type()
)
dellNetFIPSVlanFLogiAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanFLogiAccepts.setStatus("current")
_DellNetFIPSVlanFLogiRejects_Type = Counter32
_DellNetFIPSVlanFLogiRejects_Object = MibTableColumn
dellNetFIPSVlanFLogiRejects = _DellNetFIPSVlanFLogiRejects_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 12),
    _DellNetFIPSVlanFLogiRejects_Type()
)
dellNetFIPSVlanFLogiRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanFLogiRejects.setStatus("current")
_DellNetFIPSVlanFDiscAccepts_Type = Counter32
_DellNetFIPSVlanFDiscAccepts_Object = MibTableColumn
dellNetFIPSVlanFDiscAccepts = _DellNetFIPSVlanFDiscAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 13),
    _DellNetFIPSVlanFDiscAccepts_Type()
)
dellNetFIPSVlanFDiscAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanFDiscAccepts.setStatus("current")
_DellNetFIPSVlanFDiscRejects_Type = Counter32
_DellNetFIPSVlanFDiscRejects_Object = MibTableColumn
dellNetFIPSVlanFDiscRejects = _DellNetFIPSVlanFDiscRejects_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 14),
    _DellNetFIPSVlanFDiscRejects_Type()
)
dellNetFIPSVlanFDiscRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanFDiscRejects.setStatus("current")
_DellNetFIPSVlanFLogoutAccepts_Type = Counter32
_DellNetFIPSVlanFLogoutAccepts_Object = MibTableColumn
dellNetFIPSVlanFLogoutAccepts = _DellNetFIPSVlanFLogoutAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 15),
    _DellNetFIPSVlanFLogoutAccepts_Type()
)
dellNetFIPSVlanFLogoutAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanFLogoutAccepts.setStatus("current")
_DellNetFIPSVlanFLogoutRejects_Type = Counter32
_DellNetFIPSVlanFLogoutRejects_Object = MibTableColumn
dellNetFIPSVlanFLogoutRejects = _DellNetFIPSVlanFLogoutRejects_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 16),
    _DellNetFIPSVlanFLogoutRejects_Type()
)
dellNetFIPSVlanFLogoutRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanFLogoutRejects.setStatus("current")
_DellNetFIPSVlanClearVirtLinks_Type = Counter32
_DellNetFIPSVlanClearVirtLinks_Object = MibTableColumn
dellNetFIPSVlanClearVirtLinks = _DellNetFIPSVlanClearVirtLinks_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 17),
    _DellNetFIPSVlanClearVirtLinks_Type()
)
dellNetFIPSVlanClearVirtLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanClearVirtLinks.setStatus("current")
_DellNetFIPSVlanVnPortSeshTimeouts_Type = Counter32
_DellNetFIPSVlanVnPortSeshTimeouts_Object = MibTableColumn
dellNetFIPSVlanVnPortSeshTimeouts = _DellNetFIPSVlanVnPortSeshTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 18),
    _DellNetFIPSVlanVnPortSeshTimeouts_Type()
)
dellNetFIPSVlanVnPortSeshTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanVnPortSeshTimeouts.setStatus("current")
_DellNetFIPSVlanFcfDiscAdvTimeouts_Type = Counter32
_DellNetFIPSVlanFcfDiscAdvTimeouts_Object = MibTableColumn
dellNetFIPSVlanFcfDiscAdvTimeouts = _DellNetFIPSVlanFcfDiscAdvTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 19),
    _DellNetFIPSVlanFcfDiscAdvTimeouts_Type()
)
dellNetFIPSVlanFcfDiscAdvTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanFcfDiscAdvTimeouts.setStatus("current")
_DellNetFIPSVlanSeshFailsDueToHwCfg_Type = Counter32
_DellNetFIPSVlanSeshFailsDueToHwCfg_Object = MibTableColumn
dellNetFIPSVlanSeshFailsDueToHwCfg = _DellNetFIPSVlanSeshFailsDueToHwCfg_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 20),
    _DellNetFIPSVlanSeshFailsDueToHwCfg_Type()
)
dellNetFIPSVlanSeshFailsDueToHwCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanSeshFailsDueToHwCfg.setStatus("current")
_DellNetFIPSVlanSeshDenyFcfLmtRch_Type = Counter32
_DellNetFIPSVlanSeshDenyFcfLmtRch_Object = MibTableColumn
dellNetFIPSVlanSeshDenyFcfLmtRch = _DellNetFIPSVlanSeshDenyFcfLmtRch_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 21),
    _DellNetFIPSVlanSeshDenyFcfLmtRch_Type()
)
dellNetFIPSVlanSeshDenyFcfLmtRch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanSeshDenyFcfLmtRch.setStatus("current")
_DellNetFIPSVlanSeshDenyENodeLmtRch_Type = Counter32
_DellNetFIPSVlanSeshDenyENodeLmtRch_Object = MibTableColumn
dellNetFIPSVlanSeshDenyENodeLmtRch = _DellNetFIPSVlanSeshDenyENodeLmtRch_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 22),
    _DellNetFIPSVlanSeshDenyENodeLmtRch_Type()
)
dellNetFIPSVlanSeshDenyENodeLmtRch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanSeshDenyENodeLmtRch.setStatus("current")
_DellNetFIPSVlanSeshDenySysLmtRch_Type = Counter32
_DellNetFIPSVlanSeshDenySysLmtRch_Object = MibTableColumn
dellNetFIPSVlanSeshDenySysLmtRch = _DellNetFIPSVlanSeshDenySysLmtRch_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 1, 1, 23),
    _DellNetFIPSVlanSeshDenySysLmtRch_Type()
)
dellNetFIPSVlanSeshDenySysLmtRch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSVlanSeshDenySysLmtRch.setStatus("current")
_DellNetFIPSIntfStatsTable_Object = MibTable
dellNetFIPSIntfStatsTable = _DellNetFIPSIntfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2)
)
if mibBuilder.loadTexts:
    dellNetFIPSIntfStatsTable.setStatus("current")
_DellNetFIPSIntfStatsEntry_Object = MibTableRow
dellNetFIPSIntfStatsEntry = _DellNetFIPSIntfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1)
)
dellNetFIPSIntfStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dellNetFIPSIntfStatsEntry.setStatus("current")
_DellNetFIPSIntfVlanRequests_Type = Counter32
_DellNetFIPSIntfVlanRequests_Object = MibTableColumn
dellNetFIPSIntfVlanRequests = _DellNetFIPSIntfVlanRequests_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 1),
    _DellNetFIPSIntfVlanRequests_Type()
)
dellNetFIPSIntfVlanRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfVlanRequests.setStatus("current")
_DellNetFIPSIntfVlanNotifications_Type = Counter32
_DellNetFIPSIntfVlanNotifications_Object = MibTableColumn
dellNetFIPSIntfVlanNotifications = _DellNetFIPSIntfVlanNotifications_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 2),
    _DellNetFIPSIntfVlanNotifications_Type()
)
dellNetFIPSIntfVlanNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfVlanNotifications.setStatus("current")
_DellNetFIPSIntfMCDiscSolicits_Type = Counter32
_DellNetFIPSIntfMCDiscSolicits_Object = MibTableColumn
dellNetFIPSIntfMCDiscSolicits = _DellNetFIPSIntfMCDiscSolicits_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 3),
    _DellNetFIPSIntfMCDiscSolicits_Type()
)
dellNetFIPSIntfMCDiscSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfMCDiscSolicits.setStatus("current")
_DellNetFIPSIntfUnicastDiscSolicits_Type = Counter32
_DellNetFIPSIntfUnicastDiscSolicits_Object = MibTableColumn
dellNetFIPSIntfUnicastDiscSolicits = _DellNetFIPSIntfUnicastDiscSolicits_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 4),
    _DellNetFIPSIntfUnicastDiscSolicits_Type()
)
dellNetFIPSIntfUnicastDiscSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfUnicastDiscSolicits.setStatus("current")
_DellNetFIPSIntfFLogis_Type = Counter32
_DellNetFIPSIntfFLogis_Object = MibTableColumn
dellNetFIPSIntfFLogis = _DellNetFIPSIntfFLogis_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 5),
    _DellNetFIPSIntfFLogis_Type()
)
dellNetFIPSIntfFLogis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfFLogis.setStatus("current")
_DellNetFIPSIntfFDiscs_Type = Counter32
_DellNetFIPSIntfFDiscs_Object = MibTableColumn
dellNetFIPSIntfFDiscs = _DellNetFIPSIntfFDiscs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 6),
    _DellNetFIPSIntfFDiscs_Type()
)
dellNetFIPSIntfFDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfFDiscs.setStatus("current")
_DellNetFIPSIntfFLogouts_Type = Counter32
_DellNetFIPSIntfFLogouts_Object = MibTableColumn
dellNetFIPSIntfFLogouts = _DellNetFIPSIntfFLogouts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 7),
    _DellNetFIPSIntfFLogouts_Type()
)
dellNetFIPSIntfFLogouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfFLogouts.setStatus("current")
_DellNetFIPSIntfVnPortKeepAlives_Type = Counter32
_DellNetFIPSIntfVnPortKeepAlives_Object = MibTableColumn
dellNetFIPSIntfVnPortKeepAlives = _DellNetFIPSIntfVnPortKeepAlives_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 8),
    _DellNetFIPSIntfVnPortKeepAlives_Type()
)
dellNetFIPSIntfVnPortKeepAlives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfVnPortKeepAlives.setStatus("current")
_DellNetFIPSIntfMCDiscAdverts_Type = Counter32
_DellNetFIPSIntfMCDiscAdverts_Object = MibTableColumn
dellNetFIPSIntfMCDiscAdverts = _DellNetFIPSIntfMCDiscAdverts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 9),
    _DellNetFIPSIntfMCDiscAdverts_Type()
)
dellNetFIPSIntfMCDiscAdverts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfMCDiscAdverts.setStatus("current")
_DellNetFIPSIntfUnicastDiscAdverts_Type = Counter32
_DellNetFIPSIntfUnicastDiscAdverts_Object = MibTableColumn
dellNetFIPSIntfUnicastDiscAdverts = _DellNetFIPSIntfUnicastDiscAdverts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 10),
    _DellNetFIPSIntfUnicastDiscAdverts_Type()
)
dellNetFIPSIntfUnicastDiscAdverts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfUnicastDiscAdverts.setStatus("current")
_DellNetFIPSIntfFLogiAccepts_Type = Counter32
_DellNetFIPSIntfFLogiAccepts_Object = MibTableColumn
dellNetFIPSIntfFLogiAccepts = _DellNetFIPSIntfFLogiAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 11),
    _DellNetFIPSIntfFLogiAccepts_Type()
)
dellNetFIPSIntfFLogiAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfFLogiAccepts.setStatus("current")
_DellNetFIPSIntfFLogiRejects_Type = Counter32
_DellNetFIPSIntfFLogiRejects_Object = MibTableColumn
dellNetFIPSIntfFLogiRejects = _DellNetFIPSIntfFLogiRejects_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 12),
    _DellNetFIPSIntfFLogiRejects_Type()
)
dellNetFIPSIntfFLogiRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfFLogiRejects.setStatus("current")
_DellNetFIPSIntfFDiscAccepts_Type = Counter32
_DellNetFIPSIntfFDiscAccepts_Object = MibTableColumn
dellNetFIPSIntfFDiscAccepts = _DellNetFIPSIntfFDiscAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 13),
    _DellNetFIPSIntfFDiscAccepts_Type()
)
dellNetFIPSIntfFDiscAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfFDiscAccepts.setStatus("current")
_DellNetFIPSIntfFDiscRejects_Type = Counter32
_DellNetFIPSIntfFDiscRejects_Object = MibTableColumn
dellNetFIPSIntfFDiscRejects = _DellNetFIPSIntfFDiscRejects_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 14),
    _DellNetFIPSIntfFDiscRejects_Type()
)
dellNetFIPSIntfFDiscRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfFDiscRejects.setStatus("current")
_DellNetFIPSIntfFLogoutAccepts_Type = Counter32
_DellNetFIPSIntfFLogoutAccepts_Object = MibTableColumn
dellNetFIPSIntfFLogoutAccepts = _DellNetFIPSIntfFLogoutAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 15),
    _DellNetFIPSIntfFLogoutAccepts_Type()
)
dellNetFIPSIntfFLogoutAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfFLogoutAccepts.setStatus("current")
_DellNetFIPSIntfFLogoutRejects_Type = Counter32
_DellNetFIPSIntfFLogoutRejects_Object = MibTableColumn
dellNetFIPSIntfFLogoutRejects = _DellNetFIPSIntfFLogoutRejects_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 16),
    _DellNetFIPSIntfFLogoutRejects_Type()
)
dellNetFIPSIntfFLogoutRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfFLogoutRejects.setStatus("current")
_DellNetFIPSIntfClearVirtLinks_Type = Counter32
_DellNetFIPSIntfClearVirtLinks_Object = MibTableColumn
dellNetFIPSIntfClearVirtLinks = _DellNetFIPSIntfClearVirtLinks_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 17),
    _DellNetFIPSIntfClearVirtLinks_Type()
)
dellNetFIPSIntfClearVirtLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfClearVirtLinks.setStatus("current")
_DellNetFIPSIntfVnPortSeshTimeouts_Type = Counter32
_DellNetFIPSIntfVnPortSeshTimeouts_Object = MibTableColumn
dellNetFIPSIntfVnPortSeshTimeouts = _DellNetFIPSIntfVnPortSeshTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 18),
    _DellNetFIPSIntfVnPortSeshTimeouts_Type()
)
dellNetFIPSIntfVnPortSeshTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfVnPortSeshTimeouts.setStatus("current")
_DellNetFIPSIntfFcfDiscAdvTimeouts_Type = Counter32
_DellNetFIPSIntfFcfDiscAdvTimeouts_Object = MibTableColumn
dellNetFIPSIntfFcfDiscAdvTimeouts = _DellNetFIPSIntfFcfDiscAdvTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 19),
    _DellNetFIPSIntfFcfDiscAdvTimeouts_Type()
)
dellNetFIPSIntfFcfDiscAdvTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfFcfDiscAdvTimeouts.setStatus("current")
_DellNetFIPSIntfSeshFailsDueToHwCfg_Type = Counter32
_DellNetFIPSIntfSeshFailsDueToHwCfg_Object = MibTableColumn
dellNetFIPSIntfSeshFailsDueToHwCfg = _DellNetFIPSIntfSeshFailsDueToHwCfg_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 20),
    _DellNetFIPSIntfSeshFailsDueToHwCfg_Type()
)
dellNetFIPSIntfSeshFailsDueToHwCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfSeshFailsDueToHwCfg.setStatus("current")
_DellNetFIPSIntfSeshDenyFcfLmtRch_Type = Counter32
_DellNetFIPSIntfSeshDenyFcfLmtRch_Object = MibTableColumn
dellNetFIPSIntfSeshDenyFcfLmtRch = _DellNetFIPSIntfSeshDenyFcfLmtRch_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 21),
    _DellNetFIPSIntfSeshDenyFcfLmtRch_Type()
)
dellNetFIPSIntfSeshDenyFcfLmtRch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfSeshDenyFcfLmtRch.setStatus("current")
_DellNetFIPSIntfSeshDenyENodeLmtRch_Type = Counter32
_DellNetFIPSIntfSeshDenyENodeLmtRch_Object = MibTableColumn
dellNetFIPSIntfSeshDenyENodeLmtRch = _DellNetFIPSIntfSeshDenyENodeLmtRch_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 22),
    _DellNetFIPSIntfSeshDenyENodeLmtRch_Type()
)
dellNetFIPSIntfSeshDenyENodeLmtRch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfSeshDenyENodeLmtRch.setStatus("current")
_DellNetFIPSIntfSeshDenySysLmtRch_Type = Counter32
_DellNetFIPSIntfSeshDenySysLmtRch_Object = MibTableColumn
dellNetFIPSIntfSeshDenySysLmtRch = _DellNetFIPSIntfSeshDenySysLmtRch_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 3, 2, 1, 23),
    _DellNetFIPSIntfSeshDenySysLmtRch_Type()
)
dellNetFIPSIntfSeshDenySysLmtRch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFIPSIntfSeshDenySysLmtRch.setStatus("current")
_DellNetFIPSNotifications_ObjectIdentity = ObjectIdentity
dellNetFIPSNotifications = _DellNetFIPSNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4)
)
_DellNetFIPSTraps_ObjectIdentity = ObjectIdentity
dellNetFIPSTraps = _DellNetFIPSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 0)
)
_DellNetFIPSTrapObjects_ObjectIdentity = ObjectIdentity
dellNetFIPSTrapObjects = _DellNetFIPSTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 1)
)
_DellNetFIPSTrapVlanIndex_Type = Unsigned32
_DellNetFIPSTrapVlanIndex_Object = MibScalar
dellNetFIPSTrapVlanIndex = _DellNetFIPSTrapVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 1, 1),
    _DellNetFIPSTrapVlanIndex_Type()
)
dellNetFIPSTrapVlanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dellNetFIPSTrapVlanIndex.setStatus("current")
_DellNetFIPSTrapMacAddr_Type = MacAddress
_DellNetFIPSTrapMacAddr_Object = MibScalar
dellNetFIPSTrapMacAddr = _DellNetFIPSTrapMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 1, 2),
    _DellNetFIPSTrapMacAddr_Type()
)
dellNetFIPSTrapMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dellNetFIPSTrapMacAddr.setStatus("current")
_DellNetFIPSMibConformance_ObjectIdentity = ObjectIdentity
dellNetFIPSMibConformance = _DellNetFIPSMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5)
)
_DellNetFIPSMibCompliances_ObjectIdentity = ObjectIdentity
dellNetFIPSMibCompliances = _DellNetFIPSMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 1)
)
_DellNetFIPSMibGroups_ObjectIdentity = ObjectIdentity
dellNetFIPSMibGroups = _DellNetFIPSMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2)
)

# Managed Objects groups

dellNetFIPSCfgObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 1)
)
dellNetFIPSCfgObjectGroup.setObjects(
      *(("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSAdminMode"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSFCMAP"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSStatsClear"))
)
if mibBuilder.loadTexts:
    dellNetFIPSCfgObjectGroup.setStatus("current")

dellNetFIPSVlanCfgObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 2)
)
dellNetFIPSVlanCfgObjectGroup.setObjects(
      *(("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanAdminMode"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanFCMAP"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanStatsClear"))
)
if mibBuilder.loadTexts:
    dellNetFIPSVlanCfgObjectGroup.setStatus("current")

dellNetFIPSIntfObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 3)
)
dellNetFIPSIntfObjectGroup.setObjects(
      *(("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfPortModeFcf"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfStatsClear"))
)
if mibBuilder.loadTexts:
    dellNetFIPSIntfObjectGroup.setStatus("current")

dellNetFIPSSessionObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 4)
)
dellNetFIPSSessionObjectGroup.setObjects(
      *(("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSSessionENodeIntf"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSSessionFCFIntf"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSSessionTime"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSSessionExpiryTime"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSSessionState"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfStatsClear"))
)
if mibBuilder.loadTexts:
    dellNetFIPSSessionObjectGroup.setStatus("current")

dellNetFIPSENodeObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 5)
)
dellNetFIPSENodeObjectGroup.setObjects(
      *(("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSENodeIntf"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSENodeNameID"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSENodeMaxFCoESize"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSENodeConnectedFCFsCount"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSENodeActiveSessions"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSENodeWaitingSessions"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSENodeRejectedSessions"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSENodeTimeSinceDiscovered"))
)
if mibBuilder.loadTexts:
    dellNetFIPSENodeObjectGroup.setStatus("current")

dellNetFIPSFCFObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 6)
)
dellNetFIPSFCFObjectGroup.setObjects(
      *(("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSFCFIntf"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSFCFNameID"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSFCFFabricName"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSFCFAddressingMode"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSFCFPriority"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSFCFDbit"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSFCFIsAvailableForLogin"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSFCFConfiguredFKA"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSFCFTimeSinceDiscovered"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSFCFConnectedENodesCount"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSFCFSessions"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSFCFExpiryTime"))
)
if mibBuilder.loadTexts:
    dellNetFIPSFCFObjectGroup.setStatus("current")

dellNetFIPSVlanStatsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 7)
)
dellNetFIPSVlanStatsObjectGroup.setObjects(
      *(("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanVlanRequests"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanVlanNotifications"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanMCDiscSolicits"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanUnicastDiscSolicits"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanFLogis"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanFDiscs"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanFLogouts"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanVnPortKeepAlives"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanMCDiscAdverts"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanUnicastDiscAdverts"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanFLogiAccepts"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanFLogiRejects"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanFDiscAccepts"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanFDiscRejects"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanFLogoutAccepts"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanFLogoutRejects"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanClearVirtLinks"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanVnPortSeshTimeouts"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanFcfDiscAdvTimeouts"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanSeshFailsDueToHwCfg"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanSeshDenyFcfLmtRch"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanSeshDenyENodeLmtRch"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSVlanSeshDenySysLmtRch"))
)
if mibBuilder.loadTexts:
    dellNetFIPSVlanStatsObjectGroup.setStatus("current")

dellNetFIPSIntfStatsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 8)
)
dellNetFIPSIntfStatsObjectGroup.setObjects(
      *(("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfVlanRequests"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfVlanNotifications"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfMCDiscSolicits"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfUnicastDiscSolicits"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfFLogis"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfFDiscs"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfFLogouts"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfVnPortKeepAlives"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfMCDiscAdverts"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfUnicastDiscAdverts"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfFLogiAccepts"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfFLogiRejects"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfFDiscAccepts"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfFDiscRejects"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfFLogoutAccepts"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfFLogoutRejects"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfClearVirtLinks"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfVnPortSeshTimeouts"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfFcfDiscAdvTimeouts"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfSeshFailsDueToHwCfg"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfSeshDenyFcfLmtRch"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfSeshDenyENodeLmtRch"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSIntfSeshDenySysLmtRch"))
)
if mibBuilder.loadTexts:
    dellNetFIPSIntfStatsObjectGroup.setStatus("current")

dellNetFIPSTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 10)
)
dellNetFIPSTrapObjectsGroup.setObjects(
      *(("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSTrapVlanIndex"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSTrapMacAddr"))
)
if mibBuilder.loadTexts:
    dellNetFIPSTrapObjectsGroup.setStatus("current")


# Notification objects

dellNetMaxFcfsInVlanLmtRchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 0, 1)
)
dellNetMaxFcfsInVlanLmtRchTrap.setObjects(
    ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSTrapVlanIndex")
)
if mibBuilder.loadTexts:
    dellNetMaxFcfsInVlanLmtRchTrap.setStatus(
        "current"
    )

dellNetMaxENodesLmtRchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 0, 2)
)
if mibBuilder.loadTexts:
    dellNetMaxENodesLmtRchTrap.setStatus(
        "current"
    )

dellNetMaxSessionLmtRchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 0, 3)
)
if mibBuilder.loadTexts:
    dellNetMaxSessionLmtRchTrap.setStatus(
        "current"
    )

dellNetFcfDroppedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 0, 4)
)
dellNetFcfDroppedTrap.setObjects(
      *(("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSTrapVlanIndex"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSFCFIntf"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSTrapMacAddr"))
)
if mibBuilder.loadTexts:
    dellNetFcfDroppedTrap.setStatus(
        "current"
    )

dellNetENodeDroppedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 0, 5)
)
dellNetENodeDroppedTrap.setObjects(
      *(("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSTrapVlanIndex"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSENodeIntf"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSTrapMacAddr"))
)
if mibBuilder.loadTexts:
    dellNetENodeDroppedTrap.setStatus(
        "current"
    )

dellNetSessionRequestDroppedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 0, 6)
)
dellNetSessionRequestDroppedTrap.setObjects(
      *(("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSTrapVlanIndex"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSENodeIntf"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFIPSTrapMacAddr"))
)
if mibBuilder.loadTexts:
    dellNetSessionRequestDroppedTrap.setStatus(
        "current"
    )

dellNetAclInstallationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 4, 0, 7)
)
if mibBuilder.loadTexts:
    dellNetAclInstallationFailureTrap.setStatus(
        "current"
    )


# Notifications groups

dellNetFIPSTrapsObjectGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 2, 9)
)
dellNetFIPSTrapsObjectGroup.setObjects(
      *(("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetMaxFcfsInVlanLmtRchTrap"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetMaxENodesLmtRchTrap"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetMaxSessionLmtRchTrap"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetFcfDroppedTrap"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetENodeDroppedTrap"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetSessionRequestDroppedTrap"),
        ("DELL-NETWORKING-FIPSNOOPING-MIB", "dellNetAclInstallationFailureTrap"))
)
if mibBuilder.loadTexts:
    dellNetFIPSTrapsObjectGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dellNetFIPSMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 22, 5, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetFIPSMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-FIPSNOOPING-MIB",
    **{"dellNetFipSnooping": dellNetFipSnooping,
       "dellNetFIPSCfgGroup": dellNetFIPSCfgGroup,
       "dellNetFIPSAdminMode": dellNetFIPSAdminMode,
       "dellNetFIPSFCMAP": dellNetFIPSFCMAP,
       "dellNetFIPSVlanCfgTable": dellNetFIPSVlanCfgTable,
       "dellNetFIPSVlanCfgEntry": dellNetFIPSVlanCfgEntry,
       "dellNetFIPSVlanAdminMode": dellNetFIPSVlanAdminMode,
       "dellNetFIPSVlanFCMAP": dellNetFIPSVlanFCMAP,
       "dellNetFIPSVlanStatsClear": dellNetFIPSVlanStatsClear,
       "dellNetFIPSIntfTable": dellNetFIPSIntfTable,
       "dellNetFIPSIntfEntry": dellNetFIPSIntfEntry,
       "dellNetFIPSIntfPortModeFcf": dellNetFIPSIntfPortModeFcf,
       "dellNetFIPSIntfStatsClear": dellNetFIPSIntfStatsClear,
       "dellNetFIPSStatsClear": dellNetFIPSStatsClear,
       "dellNetFIPSStatusGroup": dellNetFIPSStatusGroup,
       "dellNetFIPSSessionTable": dellNetFIPSSessionTable,
       "dellNetFIPSSessionEntry": dellNetFIPSSessionEntry,
       "dellNetFIPSSessionVlanIndex": dellNetFIPSSessionVlanIndex,
       "dellNetFIPSSessionFCFMacAddr": dellNetFIPSSessionFCFMacAddr,
       "dellNetFIPSSessionENodeMacAddr": dellNetFIPSSessionENodeMacAddr,
       "dellNetFIPSSessionLoginType": dellNetFIPSSessionLoginType,
       "dellNetFIPSFCoEMacAddr": dellNetFIPSFCoEMacAddr,
       "dellNetFIPSSessionTentativeIndex": dellNetFIPSSessionTentativeIndex,
       "dellNetFIPSSessionFCID": dellNetFIPSSessionFCID,
       "dellNetFIPSSessionENodeIntf": dellNetFIPSSessionENodeIntf,
       "dellNetFIPSSessionFCFIntf": dellNetFIPSSessionFCFIntf,
       "dellNetFIPSSessionTime": dellNetFIPSSessionTime,
       "dellNetFIPSSessionExpiryTime": dellNetFIPSSessionExpiryTime,
       "dellNetFIPSSessionState": dellNetFIPSSessionState,
       "dellNetFIPSENodeTable": dellNetFIPSENodeTable,
       "dellNetFIPSENodeEntry": dellNetFIPSENodeEntry,
       "dellNetFIPSENodeVlanIndex": dellNetFIPSENodeVlanIndex,
       "dellNetFIPSENodeMacAddr": dellNetFIPSENodeMacAddr,
       "dellNetFIPSENodeIntf": dellNetFIPSENodeIntf,
       "dellNetFIPSENodeNameID": dellNetFIPSENodeNameID,
       "dellNetFIPSENodeMaxFCoESize": dellNetFIPSENodeMaxFCoESize,
       "dellNetFIPSENodeConnectedFCFsCount": dellNetFIPSENodeConnectedFCFsCount,
       "dellNetFIPSENodeActiveSessions": dellNetFIPSENodeActiveSessions,
       "dellNetFIPSENodeWaitingSessions": dellNetFIPSENodeWaitingSessions,
       "dellNetFIPSENodeRejectedSessions": dellNetFIPSENodeRejectedSessions,
       "dellNetFIPSENodeTimeSinceDiscovered": dellNetFIPSENodeTimeSinceDiscovered,
       "dellNetFIPSFCFTable": dellNetFIPSFCFTable,
       "dellNetFIPSFCFEntry": dellNetFIPSFCFEntry,
       "dellNetFIPSFCFVlanIndex": dellNetFIPSFCFVlanIndex,
       "dellNetFIPSFCFMacAddr": dellNetFIPSFCFMacAddr,
       "dellNetFIPSFCFIntf": dellNetFIPSFCFIntf,
       "dellNetFIPSFCFNameID": dellNetFIPSFCFNameID,
       "dellNetFIPSFCFFabricName": dellNetFIPSFCFFabricName,
       "dellNetFIPSFCFAddressingMode": dellNetFIPSFCFAddressingMode,
       "dellNetFIPSFCFPriority": dellNetFIPSFCFPriority,
       "dellNetFIPSFCFDbit": dellNetFIPSFCFDbit,
       "dellNetFIPSFCFIsAvailableForLogin": dellNetFIPSFCFIsAvailableForLogin,
       "dellNetFIPSFCFConfiguredFKA": dellNetFIPSFCFConfiguredFKA,
       "dellNetFIPSFCFTimeSinceDiscovered": dellNetFIPSFCFTimeSinceDiscovered,
       "dellNetFIPSFCFConnectedENodesCount": dellNetFIPSFCFConnectedENodesCount,
       "dellNetFIPSFCFSessions": dellNetFIPSFCFSessions,
       "dellNetFIPSFCFExpiryTime": dellNetFIPSFCFExpiryTime,
       "dellNetFIPSStatisticsGroup": dellNetFIPSStatisticsGroup,
       "dellNetFIPSVlanStatsTable": dellNetFIPSVlanStatsTable,
       "dellNetFIPSVlanStatsEntry": dellNetFIPSVlanStatsEntry,
       "dellNetFIPSVlanVlanRequests": dellNetFIPSVlanVlanRequests,
       "dellNetFIPSVlanVlanNotifications": dellNetFIPSVlanVlanNotifications,
       "dellNetFIPSVlanMCDiscSolicits": dellNetFIPSVlanMCDiscSolicits,
       "dellNetFIPSVlanUnicastDiscSolicits": dellNetFIPSVlanUnicastDiscSolicits,
       "dellNetFIPSVlanFLogis": dellNetFIPSVlanFLogis,
       "dellNetFIPSVlanFDiscs": dellNetFIPSVlanFDiscs,
       "dellNetFIPSVlanFLogouts": dellNetFIPSVlanFLogouts,
       "dellNetFIPSVlanVnPortKeepAlives": dellNetFIPSVlanVnPortKeepAlives,
       "dellNetFIPSVlanMCDiscAdverts": dellNetFIPSVlanMCDiscAdverts,
       "dellNetFIPSVlanUnicastDiscAdverts": dellNetFIPSVlanUnicastDiscAdverts,
       "dellNetFIPSVlanFLogiAccepts": dellNetFIPSVlanFLogiAccepts,
       "dellNetFIPSVlanFLogiRejects": dellNetFIPSVlanFLogiRejects,
       "dellNetFIPSVlanFDiscAccepts": dellNetFIPSVlanFDiscAccepts,
       "dellNetFIPSVlanFDiscRejects": dellNetFIPSVlanFDiscRejects,
       "dellNetFIPSVlanFLogoutAccepts": dellNetFIPSVlanFLogoutAccepts,
       "dellNetFIPSVlanFLogoutRejects": dellNetFIPSVlanFLogoutRejects,
       "dellNetFIPSVlanClearVirtLinks": dellNetFIPSVlanClearVirtLinks,
       "dellNetFIPSVlanVnPortSeshTimeouts": dellNetFIPSVlanVnPortSeshTimeouts,
       "dellNetFIPSVlanFcfDiscAdvTimeouts": dellNetFIPSVlanFcfDiscAdvTimeouts,
       "dellNetFIPSVlanSeshFailsDueToHwCfg": dellNetFIPSVlanSeshFailsDueToHwCfg,
       "dellNetFIPSVlanSeshDenyFcfLmtRch": dellNetFIPSVlanSeshDenyFcfLmtRch,
       "dellNetFIPSVlanSeshDenyENodeLmtRch": dellNetFIPSVlanSeshDenyENodeLmtRch,
       "dellNetFIPSVlanSeshDenySysLmtRch": dellNetFIPSVlanSeshDenySysLmtRch,
       "dellNetFIPSIntfStatsTable": dellNetFIPSIntfStatsTable,
       "dellNetFIPSIntfStatsEntry": dellNetFIPSIntfStatsEntry,
       "dellNetFIPSIntfVlanRequests": dellNetFIPSIntfVlanRequests,
       "dellNetFIPSIntfVlanNotifications": dellNetFIPSIntfVlanNotifications,
       "dellNetFIPSIntfMCDiscSolicits": dellNetFIPSIntfMCDiscSolicits,
       "dellNetFIPSIntfUnicastDiscSolicits": dellNetFIPSIntfUnicastDiscSolicits,
       "dellNetFIPSIntfFLogis": dellNetFIPSIntfFLogis,
       "dellNetFIPSIntfFDiscs": dellNetFIPSIntfFDiscs,
       "dellNetFIPSIntfFLogouts": dellNetFIPSIntfFLogouts,
       "dellNetFIPSIntfVnPortKeepAlives": dellNetFIPSIntfVnPortKeepAlives,
       "dellNetFIPSIntfMCDiscAdverts": dellNetFIPSIntfMCDiscAdverts,
       "dellNetFIPSIntfUnicastDiscAdverts": dellNetFIPSIntfUnicastDiscAdverts,
       "dellNetFIPSIntfFLogiAccepts": dellNetFIPSIntfFLogiAccepts,
       "dellNetFIPSIntfFLogiRejects": dellNetFIPSIntfFLogiRejects,
       "dellNetFIPSIntfFDiscAccepts": dellNetFIPSIntfFDiscAccepts,
       "dellNetFIPSIntfFDiscRejects": dellNetFIPSIntfFDiscRejects,
       "dellNetFIPSIntfFLogoutAccepts": dellNetFIPSIntfFLogoutAccepts,
       "dellNetFIPSIntfFLogoutRejects": dellNetFIPSIntfFLogoutRejects,
       "dellNetFIPSIntfClearVirtLinks": dellNetFIPSIntfClearVirtLinks,
       "dellNetFIPSIntfVnPortSeshTimeouts": dellNetFIPSIntfVnPortSeshTimeouts,
       "dellNetFIPSIntfFcfDiscAdvTimeouts": dellNetFIPSIntfFcfDiscAdvTimeouts,
       "dellNetFIPSIntfSeshFailsDueToHwCfg": dellNetFIPSIntfSeshFailsDueToHwCfg,
       "dellNetFIPSIntfSeshDenyFcfLmtRch": dellNetFIPSIntfSeshDenyFcfLmtRch,
       "dellNetFIPSIntfSeshDenyENodeLmtRch": dellNetFIPSIntfSeshDenyENodeLmtRch,
       "dellNetFIPSIntfSeshDenySysLmtRch": dellNetFIPSIntfSeshDenySysLmtRch,
       "dellNetFIPSNotifications": dellNetFIPSNotifications,
       "dellNetFIPSTraps": dellNetFIPSTraps,
       "dellNetMaxFcfsInVlanLmtRchTrap": dellNetMaxFcfsInVlanLmtRchTrap,
       "dellNetMaxENodesLmtRchTrap": dellNetMaxENodesLmtRchTrap,
       "dellNetMaxSessionLmtRchTrap": dellNetMaxSessionLmtRchTrap,
       "dellNetFcfDroppedTrap": dellNetFcfDroppedTrap,
       "dellNetENodeDroppedTrap": dellNetENodeDroppedTrap,
       "dellNetSessionRequestDroppedTrap": dellNetSessionRequestDroppedTrap,
       "dellNetAclInstallationFailureTrap": dellNetAclInstallationFailureTrap,
       "dellNetFIPSTrapObjects": dellNetFIPSTrapObjects,
       "dellNetFIPSTrapVlanIndex": dellNetFIPSTrapVlanIndex,
       "dellNetFIPSTrapMacAddr": dellNetFIPSTrapMacAddr,
       "dellNetFIPSMibConformance": dellNetFIPSMibConformance,
       "dellNetFIPSMibCompliances": dellNetFIPSMibCompliances,
       "dellNetFIPSMibCompliance": dellNetFIPSMibCompliance,
       "dellNetFIPSMibGroups": dellNetFIPSMibGroups,
       "dellNetFIPSCfgObjectGroup": dellNetFIPSCfgObjectGroup,
       "dellNetFIPSVlanCfgObjectGroup": dellNetFIPSVlanCfgObjectGroup,
       "dellNetFIPSIntfObjectGroup": dellNetFIPSIntfObjectGroup,
       "dellNetFIPSSessionObjectGroup": dellNetFIPSSessionObjectGroup,
       "dellNetFIPSENodeObjectGroup": dellNetFIPSENodeObjectGroup,
       "dellNetFIPSFCFObjectGroup": dellNetFIPSFCFObjectGroup,
       "dellNetFIPSVlanStatsObjectGroup": dellNetFIPSVlanStatsObjectGroup,
       "dellNetFIPSIntfStatsObjectGroup": dellNetFIPSIntfStatsObjectGroup,
       "dellNetFIPSTrapsObjectGroup": dellNetFIPSTrapsObjectGroup,
       "dellNetFIPSTrapObjectsGroup": dellNetFIPSTrapObjectsGroup}
)
