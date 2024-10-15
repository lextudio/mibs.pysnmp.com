# SNMP MIB module (WWP-LEOS-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:00 2024
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

(dot3adAggPortActorAdminKey,
 dot3adAggPortListPorts) = mibBuilder.importSymbols(
    "IEEE8023-LAG-MIB",
    "dot3adAggPortActorAdminKey",
    "dot3adAggPortListPorts")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation",
    "sysName")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModules,
 wwpModulesLeos) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosPortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2)
)
wwpLeosPortMIB.setRevisions(
        ("2012-05-25 00:00",
         "2011-02-02 00:00",
         "2010-11-01 00:00",
         "2010-07-28 00:00",
         "2010-05-05 17:00",
         "2008-11-14 00:00",
         "2008-07-21 00:00",
         "2007-08-11 00:00",
         "2007-06-20 00:00",
         "2006-05-26 00:00",
         "2006-05-18 00:00",
         "2006-03-15 00:00",
         "2005-07-28 00:00",
         "2004-04-18 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class PortEgressFrameCosPolicy(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingore", 1),
          ("rcosToL2OuterPcpMap", 2))
    )



class PortIngressFixedColor(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2))
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosPortMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosPortMIBObjects = _WwpLeosPortMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1)
)
_WwpLeosEtherPort_ObjectIdentity = ObjectIdentity
wwpLeosEtherPort = _WwpLeosEtherPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1)
)
_WwpLeosEtherPortTable_Object = MibTable
wwpLeosEtherPortTable = _WwpLeosEtherPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpLeosEtherPortTable.setStatus("current")
_WwpLeosEtherPortEntry_Object = MibTableRow
wwpLeosEtherPortEntry = _WwpLeosEtherPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1)
)
wwpLeosEtherPortEntry.setIndexNames(
    (0, "WWP-LEOS-PORT-MIB", "wwpLeosEtherPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosEtherPortEntry.setStatus("current")


class _WwpLeosEtherPortId_Type(Integer32):
    """Custom type wwpLeosEtherPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosEtherPortId_Type.__name__ = "Integer32"
_WwpLeosEtherPortId_Object = MibTableColumn
wwpLeosEtherPortId = _WwpLeosEtherPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 1),
    _WwpLeosEtherPortId_Type()
)
wwpLeosEtherPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortId.setStatus("current")


class _WwpLeosEtherPortName_Type(DisplayString):
    """Custom type wwpLeosEtherPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_WwpLeosEtherPortName_Type.__name__ = "DisplayString"
_WwpLeosEtherPortName_Object = MibTableColumn
wwpLeosEtherPortName = _WwpLeosEtherPortName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 2),
    _WwpLeosEtherPortName_Type()
)
wwpLeosEtherPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortName.setStatus("current")


class _WwpLeosEtherPortDesc_Type(DisplayString):
    """Custom type wwpLeosEtherPortDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WwpLeosEtherPortDesc_Type.__name__ = "DisplayString"
_WwpLeosEtherPortDesc_Object = MibTableColumn
wwpLeosEtherPortDesc = _WwpLeosEtherPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 3),
    _WwpLeosEtherPortDesc_Type()
)
wwpLeosEtherPortDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortDesc.setStatus("current")


class _WwpLeosEtherPortType_Type(Integer32):
    """Custom type wwpLeosEtherPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("fastEthernet", 2),
          ("gigEthernet", 4),
          ("gigHundredFx", 7),
          ("gigTenGigEthernet", 10),
          ("hundredFx", 3),
          ("lagPort", 5),
          ("tenGigEthernet", 9),
          ("tripleSpeed", 8),
          ("unknown", 6))
    )


_WwpLeosEtherPortType_Type.__name__ = "Integer32"
_WwpLeosEtherPortType_Object = MibTableColumn
wwpLeosEtherPortType = _WwpLeosEtherPortType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 4),
    _WwpLeosEtherPortType_Type()
)
wwpLeosEtherPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortType.setStatus("current")
_WwpLeosEtherPortPhysAddr_Type = MacAddress
_WwpLeosEtherPortPhysAddr_Object = MibTableColumn
wwpLeosEtherPortPhysAddr = _WwpLeosEtherPortPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 5),
    _WwpLeosEtherPortPhysAddr_Type()
)
wwpLeosEtherPortPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortPhysAddr.setStatus("current")
_WwpLeosEtherPortAutoNeg_Type = TruthValue
_WwpLeosEtherPortAutoNeg_Object = MibTableColumn
wwpLeosEtherPortAutoNeg = _WwpLeosEtherPortAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 6),
    _WwpLeosEtherPortAutoNeg_Type()
)
wwpLeosEtherPortAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortAutoNeg.setStatus("current")


class _WwpLeosEtherPortAdminStatus_Type(Integer32):
    """Custom type wwpLeosEtherPortAdminStatus based on Integer32"""
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


_WwpLeosEtherPortAdminStatus_Type.__name__ = "Integer32"
_WwpLeosEtherPortAdminStatus_Object = MibTableColumn
wwpLeosEtherPortAdminStatus = _WwpLeosEtherPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 7),
    _WwpLeosEtherPortAdminStatus_Type()
)
wwpLeosEtherPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortAdminStatus.setStatus("current")


class _WwpLeosEtherPortOperStatus_Type(Integer32):
    """Custom type wwpLeosEtherPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("lbrx", 5),
          ("lbtx", 4),
          ("linkflap", 6),
          ("notauth", 3),
          ("up", 1))
    )


_WwpLeosEtherPortOperStatus_Type.__name__ = "Integer32"
_WwpLeosEtherPortOperStatus_Object = MibTableColumn
wwpLeosEtherPortOperStatus = _WwpLeosEtherPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 8),
    _WwpLeosEtherPortOperStatus_Type()
)
wwpLeosEtherPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortOperStatus.setStatus("current")


class _WwpLeosEtherPortAdminSpeed_Type(Integer32):
    """Custom type wwpLeosEtherPortAdminSpeed based on Integer32"""
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
        *(("auto", 4),
          ("gig", 3),
          ("hundredMb", 2),
          ("tenGig", 5),
          ("tenMb", 1))
    )


_WwpLeosEtherPortAdminSpeed_Type.__name__ = "Integer32"
_WwpLeosEtherPortAdminSpeed_Object = MibTableColumn
wwpLeosEtherPortAdminSpeed = _WwpLeosEtherPortAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 9),
    _WwpLeosEtherPortAdminSpeed_Type()
)
wwpLeosEtherPortAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortAdminSpeed.setStatus("current")


class _WwpLeosEtherPortOperSpeed_Type(Integer32):
    """Custom type wwpLeosEtherPortOperSpeed based on Integer32"""
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
        *(("gig", 3),
          ("hundredMb", 2),
          ("tenGig", 4),
          ("tenMb", 1),
          ("unknown", 0))
    )


_WwpLeosEtherPortOperSpeed_Type.__name__ = "Integer32"
_WwpLeosEtherPortOperSpeed_Object = MibTableColumn
wwpLeosEtherPortOperSpeed = _WwpLeosEtherPortOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 10),
    _WwpLeosEtherPortOperSpeed_Type()
)
wwpLeosEtherPortOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortOperSpeed.setStatus("deprecated")


class _WwpLeosEtherPortAdminDuplex_Type(Integer32):
    """Custom type wwpLeosEtherPortAdminDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_WwpLeosEtherPortAdminDuplex_Type.__name__ = "Integer32"
_WwpLeosEtherPortAdminDuplex_Object = MibTableColumn
wwpLeosEtherPortAdminDuplex = _WwpLeosEtherPortAdminDuplex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 11),
    _WwpLeosEtherPortAdminDuplex_Type()
)
wwpLeosEtherPortAdminDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortAdminDuplex.setStatus("current")


class _WwpLeosEtherPortOperDuplex_Type(Integer32):
    """Custom type wwpLeosEtherPortOperDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_WwpLeosEtherPortOperDuplex_Type.__name__ = "Integer32"
_WwpLeosEtherPortOperDuplex_Object = MibTableColumn
wwpLeosEtherPortOperDuplex = _WwpLeosEtherPortOperDuplex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 12),
    _WwpLeosEtherPortOperDuplex_Type()
)
wwpLeosEtherPortOperDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortOperDuplex.setStatus("current")


class _WwpLeosEtherPortAdminFlowCtrl_Type(Integer32):
    """Custom type wwpLeosEtherPortAdminFlowCtrl based on Integer32"""
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
        *(("asymRx", 4),
          ("asymTx", 3),
          ("off", 2),
          ("sym", 5),
          ("unknown", 1))
    )


_WwpLeosEtherPortAdminFlowCtrl_Type.__name__ = "Integer32"
_WwpLeosEtherPortAdminFlowCtrl_Object = MibTableColumn
wwpLeosEtherPortAdminFlowCtrl = _WwpLeosEtherPortAdminFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 13),
    _WwpLeosEtherPortAdminFlowCtrl_Type()
)
wwpLeosEtherPortAdminFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortAdminFlowCtrl.setStatus("current")


class _WwpLeosEtherPortOperFlowCtrl_Type(Integer32):
    """Custom type wwpLeosEtherPortOperFlowCtrl based on Integer32"""
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
        *(("asymRx", 4),
          ("asymTx", 3),
          ("off", 2),
          ("sym", 5),
          ("unknown", 1))
    )


_WwpLeosEtherPortOperFlowCtrl_Type.__name__ = "Integer32"
_WwpLeosEtherPortOperFlowCtrl_Object = MibTableColumn
wwpLeosEtherPortOperFlowCtrl = _WwpLeosEtherPortOperFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 14),
    _WwpLeosEtherPortOperFlowCtrl_Type()
)
wwpLeosEtherPortOperFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortOperFlowCtrl.setStatus("current")


class _WwpLeosEtherIngressPvid_Type(Integer32):
    """Custom type wwpLeosEtherIngressPvid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )


_WwpLeosEtherIngressPvid_Type.__name__ = "Integer32"
_WwpLeosEtherIngressPvid_Object = MibTableColumn
wwpLeosEtherIngressPvid = _WwpLeosEtherIngressPvid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 15),
    _WwpLeosEtherIngressPvid_Type()
)
wwpLeosEtherIngressPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherIngressPvid.setStatus("current")


class _WwpLeosEtherUntagEgressVlanId_Type(Integer32):
    """Custom type wwpLeosEtherUntagEgressVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24576),
    )


_WwpLeosEtherUntagEgressVlanId_Type.__name__ = "Integer32"
_WwpLeosEtherUntagEgressVlanId_Object = MibTableColumn
wwpLeosEtherUntagEgressVlanId = _WwpLeosEtherUntagEgressVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 16),
    _WwpLeosEtherUntagEgressVlanId_Type()
)
wwpLeosEtherUntagEgressVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherUntagEgressVlanId.setStatus("current")


class _WwpLeosEtherPortAcceptableFrameTypes_Type(Integer32):
    """Custom type wwpLeosEtherPortAcceptableFrameTypes based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admitAll", 1),
          ("admitOnlyUntagged", 3),
          ("admitOnlyVlanTagged", 2))
    )


_WwpLeosEtherPortAcceptableFrameTypes_Type.__name__ = "Integer32"
_WwpLeosEtherPortAcceptableFrameTypes_Object = MibTableColumn
wwpLeosEtherPortAcceptableFrameTypes = _WwpLeosEtherPortAcceptableFrameTypes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 17),
    _WwpLeosEtherPortAcceptableFrameTypes_Type()
)
wwpLeosEtherPortAcceptableFrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortAcceptableFrameTypes.setStatus("current")


class _WwpLeosEtherPortUntaggedPriority_Type(Integer32):
    """Custom type wwpLeosEtherPortUntaggedPriority based on Integer32"""
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
        *(("p0", 0),
          ("p1", 1),
          ("p2", 2),
          ("p3", 3),
          ("p4", 4),
          ("p5", 5),
          ("p6", 6),
          ("p7", 7))
    )


_WwpLeosEtherPortUntaggedPriority_Type.__name__ = "Integer32"
_WwpLeosEtherPortUntaggedPriority_Object = MibTableColumn
wwpLeosEtherPortUntaggedPriority = _WwpLeosEtherPortUntaggedPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 18),
    _WwpLeosEtherPortUntaggedPriority_Type()
)
wwpLeosEtherPortUntaggedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortUntaggedPriority.setStatus("deprecated")


class _WwpLeosEtherPortMaxFrameSize_Type(Integer32):
    """Custom type wwpLeosEtherPortMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1522, 9216),
    )


_WwpLeosEtherPortMaxFrameSize_Type.__name__ = "Integer32"
_WwpLeosEtherPortMaxFrameSize_Object = MibTableColumn
wwpLeosEtherPortMaxFrameSize = _WwpLeosEtherPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 19),
    _WwpLeosEtherPortMaxFrameSize_Type()
)
wwpLeosEtherPortMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortMaxFrameSize.setStatus("current")


class _WwpLeosEtherPortVlanIngressFiltering_Type(TruthValue):
    """Custom type wwpLeosEtherPortVlanIngressFiltering based on TruthValue"""


_WwpLeosEtherPortVlanIngressFiltering_Object = MibTableColumn
wwpLeosEtherPortVlanIngressFiltering = _WwpLeosEtherPortVlanIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 20),
    _WwpLeosEtherPortVlanIngressFiltering_Type()
)
wwpLeosEtherPortVlanIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortVlanIngressFiltering.setStatus("current")


class _WwpLeosEtherPortAdminAdvertisedFlowCtrl_Type(Integer32):
    """Custom type wwpLeosEtherPortAdminAdvertisedFlowCtrl based on Integer32"""
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
        *(("asymTx", 3),
          ("off", 2),
          ("sym", 4),
          ("symAsymRx", 5),
          ("unknown", 1))
    )


_WwpLeosEtherPortAdminAdvertisedFlowCtrl_Type.__name__ = "Integer32"
_WwpLeosEtherPortAdminAdvertisedFlowCtrl_Object = MibTableColumn
wwpLeosEtherPortAdminAdvertisedFlowCtrl = _WwpLeosEtherPortAdminAdvertisedFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 21),
    _WwpLeosEtherPortAdminAdvertisedFlowCtrl_Type()
)
wwpLeosEtherPortAdminAdvertisedFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortAdminAdvertisedFlowCtrl.setStatus("current")


class _WwpLeosEtherPortVplsPortType_Type(Integer32):
    """Custom type wwpLeosEtherPortVplsPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("networkFacing", 3),
          ("notDefined", 1),
          ("subscriber", 2))
    )


_WwpLeosEtherPortVplsPortType_Type.__name__ = "Integer32"
_WwpLeosEtherPortVplsPortType_Object = MibTableColumn
wwpLeosEtherPortVplsPortType = _WwpLeosEtherPortVplsPortType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 22),
    _WwpLeosEtherPortVplsPortType_Type()
)
wwpLeosEtherPortVplsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortVplsPortType.setStatus("current")


class _WwpLeosEtherPortIngressCosPolicy_Type(Integer32):
    """Custom type wwpLeosEtherPortIngressCosPolicy based on Integer32"""
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
        *(("fixed", 2),
          ("ippInherit", 3),
          ("leave", 1),
          ("phbgInherit", 4))
    )


_WwpLeosEtherPortIngressCosPolicy_Type.__name__ = "Integer32"
_WwpLeosEtherPortIngressCosPolicy_Object = MibTableColumn
wwpLeosEtherPortIngressCosPolicy = _WwpLeosEtherPortIngressCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 23),
    _WwpLeosEtherPortIngressCosPolicy_Type()
)
wwpLeosEtherPortIngressCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortIngressCosPolicy.setStatus("current")


class _WwpLeosEtherPortIngressFixedDot1dPri_Type(Integer32):
    """Custom type wwpLeosEtherPortIngressFixedDot1dPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosEtherPortIngressFixedDot1dPri_Type.__name__ = "Integer32"
_WwpLeosEtherPortIngressFixedDot1dPri_Object = MibTableColumn
wwpLeosEtherPortIngressFixedDot1dPri = _WwpLeosEtherPortIngressFixedDot1dPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 24),
    _WwpLeosEtherPortIngressFixedDot1dPri_Type()
)
wwpLeosEtherPortIngressFixedDot1dPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortIngressFixedDot1dPri.setStatus("current")


class _WwpLeosEtherPortUntagDataVsi_Type(Integer32):
    """Custom type wwpLeosEtherPortUntagDataVsi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosEtherPortUntagDataVsi_Type.__name__ = "Integer32"
_WwpLeosEtherPortUntagDataVsi_Object = MibTableColumn
wwpLeosEtherPortUntagDataVsi = _WwpLeosEtherPortUntagDataVsi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 25),
    _WwpLeosEtherPortUntagDataVsi_Type()
)
wwpLeosEtherPortUntagDataVsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortUntagDataVsi.setStatus("current")
_WwpLeosEtherPortOperationalSpeed_Type = Gauge32
_WwpLeosEtherPortOperationalSpeed_Object = MibTableColumn
wwpLeosEtherPortOperationalSpeed = _WwpLeosEtherPortOperationalSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 26),
    _WwpLeosEtherPortOperationalSpeed_Type()
)
wwpLeosEtherPortOperationalSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortOperationalSpeed.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosEtherPortOperationalSpeed.setUnits("kbps")


class _WwpLeosEtherPortUntagCtrlVsi_Type(Integer32):
    """Custom type wwpLeosEtherPortUntagCtrlVsi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosEtherPortUntagCtrlVsi_Type.__name__ = "Integer32"
_WwpLeosEtherPortUntagCtrlVsi_Object = MibTableColumn
wwpLeosEtherPortUntagCtrlVsi = _WwpLeosEtherPortUntagCtrlVsi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 27),
    _WwpLeosEtherPortUntagCtrlVsi_Type()
)
wwpLeosEtherPortUntagCtrlVsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortUntagCtrlVsi.setStatus("current")


class _WwpLeosEtherPortMirrorPort_Type(TruthValue):
    """Custom type wwpLeosEtherPortMirrorPort based on TruthValue"""


_WwpLeosEtherPortMirrorPort_Object = MibTableColumn
wwpLeosEtherPortMirrorPort = _WwpLeosEtherPortMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 28),
    _WwpLeosEtherPortMirrorPort_Type()
)
wwpLeosEtherPortMirrorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortMirrorPort.setStatus("current")


class _WwpLeosEtherPortMirrorIngress_Type(Integer32):
    """Custom type wwpLeosEtherPortMirrorIngress based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosEtherPortMirrorIngress_Type.__name__ = "Integer32"
_WwpLeosEtherPortMirrorIngress_Object = MibTableColumn
wwpLeosEtherPortMirrorIngress = _WwpLeosEtherPortMirrorIngress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 29),
    _WwpLeosEtherPortMirrorIngress_Type()
)
wwpLeosEtherPortMirrorIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortMirrorIngress.setStatus("current")


class _WwpLeosEtherPortMirrorEgress_Type(Integer32):
    """Custom type wwpLeosEtherPortMirrorEgress based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosEtherPortMirrorEgress_Type.__name__ = "Integer32"
_WwpLeosEtherPortMirrorEgress_Object = MibTableColumn
wwpLeosEtherPortMirrorEgress = _WwpLeosEtherPortMirrorEgress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 30),
    _WwpLeosEtherPortMirrorEgress_Type()
)
wwpLeosEtherPortMirrorEgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortMirrorEgress.setStatus("current")


class _WwpLeosEtherPortUntagDataVsiType_Type(Integer32):
    """Custom type wwpLeosEtherPortUntagDataVsiType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("mpls", 2))
    )


_WwpLeosEtherPortUntagDataVsiType_Type.__name__ = "Integer32"
_WwpLeosEtherPortUntagDataVsiType_Object = MibTableColumn
wwpLeosEtherPortUntagDataVsiType = _WwpLeosEtherPortUntagDataVsiType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 31),
    _WwpLeosEtherPortUntagDataVsiType_Type()
)
wwpLeosEtherPortUntagDataVsiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortUntagDataVsiType.setStatus("current")


class _WwpLeosEtherPortUntagCtrlVsiType_Type(Integer32):
    """Custom type wwpLeosEtherPortUntagCtrlVsiType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("mpls", 2))
    )


_WwpLeosEtherPortUntagCtrlVsiType_Type.__name__ = "Integer32"
_WwpLeosEtherPortUntagCtrlVsiType_Object = MibTableColumn
wwpLeosEtherPortUntagCtrlVsiType = _WwpLeosEtherPortUntagCtrlVsiType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 32),
    _WwpLeosEtherPortUntagCtrlVsiType_Type()
)
wwpLeosEtherPortUntagCtrlVsiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortUntagCtrlVsiType.setStatus("current")


class _WwpLeosEtherPortVsIngressFiltering_Type(TruthValue):
    """Custom type wwpLeosEtherPortVsIngressFiltering based on TruthValue"""


_WwpLeosEtherPortVsIngressFiltering_Object = MibTableColumn
wwpLeosEtherPortVsIngressFiltering = _WwpLeosEtherPortVsIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 33),
    _WwpLeosEtherPortVsIngressFiltering_Type()
)
wwpLeosEtherPortVsIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortVsIngressFiltering.setStatus("current")
_WwpLeosEtherPortOperAutoNeg_Type = TruthValue
_WwpLeosEtherPortOperAutoNeg_Object = MibTableColumn
wwpLeosEtherPortOperAutoNeg = _WwpLeosEtherPortOperAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 34),
    _WwpLeosEtherPortOperAutoNeg_Type()
)
wwpLeosEtherPortOperAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortOperAutoNeg.setStatus("current")
_WwpLeosEtherPortUpTime_Type = TimeTicks
_WwpLeosEtherPortUpTime_Object = MibTableColumn
wwpLeosEtherPortUpTime = _WwpLeosEtherPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 35),
    _WwpLeosEtherPortUpTime_Type()
)
wwpLeosEtherPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortUpTime.setStatus("current")


class _WwpLeosEtherPortUntagDataVid_Type(Integer32):
    """Custom type wwpLeosEtherPortUntagDataVid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24576),
    )


_WwpLeosEtherPortUntagDataVid_Type.__name__ = "Integer32"
_WwpLeosEtherPortUntagDataVid_Object = MibTableColumn
wwpLeosEtherPortUntagDataVid = _WwpLeosEtherPortUntagDataVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 36),
    _WwpLeosEtherPortUntagDataVid_Type()
)
wwpLeosEtherPortUntagDataVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortUntagDataVid.setStatus("current")


class _WwpLeosEtherPortPhyLoopback_Type(TruthValue):
    """Custom type wwpLeosEtherPortPhyLoopback based on TruthValue"""


_WwpLeosEtherPortPhyLoopback_Object = MibTableColumn
wwpLeosEtherPortPhyLoopback = _WwpLeosEtherPortPhyLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 37),
    _WwpLeosEtherPortPhyLoopback_Type()
)
wwpLeosEtherPortPhyLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortPhyLoopback.setStatus("current")


class _WwpLeosEtherPortVlanIngressFilterStrict_Type(TruthValue):
    """Custom type wwpLeosEtherPortVlanIngressFilterStrict based on TruthValue"""


_WwpLeosEtherPortVlanIngressFilterStrict_Object = MibTableColumn
wwpLeosEtherPortVlanIngressFilterStrict = _WwpLeosEtherPortVlanIngressFilterStrict_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 38),
    _WwpLeosEtherPortVlanIngressFilterStrict_Type()
)
wwpLeosEtherPortVlanIngressFilterStrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortVlanIngressFilterStrict.setStatus("current")


class _WwpLeosEtherPortMacSaDaSwap_Type(TruthValue):
    """Custom type wwpLeosEtherPortMacSaDaSwap based on TruthValue"""


_WwpLeosEtherPortMacSaDaSwap_Object = MibTableColumn
wwpLeosEtherPortMacSaDaSwap = _WwpLeosEtherPortMacSaDaSwap_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 39),
    _WwpLeosEtherPortMacSaDaSwap_Type()
)
wwpLeosEtherPortMacSaDaSwap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortMacSaDaSwap.setStatus("current")


class _WwpLeosEtherPortMacSaDaSwapVlan_Type(Integer32):
    """Custom type wwpLeosEtherPortMacSaDaSwapVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24576),
    )


_WwpLeosEtherPortMacSaDaSwapVlan_Type.__name__ = "Integer32"
_WwpLeosEtherPortMacSaDaSwapVlan_Object = MibTableColumn
wwpLeosEtherPortMacSaDaSwapVlan = _WwpLeosEtherPortMacSaDaSwapVlan_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 40),
    _WwpLeosEtherPortMacSaDaSwapVlan_Type()
)
wwpLeosEtherPortMacSaDaSwapVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortMacSaDaSwapVlan.setStatus("current")


class _WwpLeosEtherPortResolvedCosPolicy_Type(Integer32):
    """Custom type wwpLeosEtherPortResolvedCosPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("dot1d", 1),
          ("fixedCos", 3),
          ("l3DscpCos", 2),
          ("unknown", 99))
    )


_WwpLeosEtherPortResolvedCosPolicy_Type.__name__ = "Integer32"
_WwpLeosEtherPortResolvedCosPolicy_Object = MibTableColumn
wwpLeosEtherPortResolvedCosPolicy = _WwpLeosEtherPortResolvedCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 41),
    _WwpLeosEtherPortResolvedCosPolicy_Type()
)
wwpLeosEtherPortResolvedCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortResolvedCosPolicy.setStatus("current")


class _WwpLeosEtherPortMode_Type(Integer32):
    """Custom type wwpLeosEtherPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("rj45", 1),
          ("sfp", 2),
          ("unknown", 99))
    )


_WwpLeosEtherPortMode_Type.__name__ = "Integer32"
_WwpLeosEtherPortMode_Object = MibTableColumn
wwpLeosEtherPortMode = _WwpLeosEtherPortMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 42),
    _WwpLeosEtherPortMode_Type()
)
wwpLeosEtherPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortMode.setStatus("current")


class _WwpLeosEtherFixedRcos_Type(Integer32):
    """Custom type wwpLeosEtherFixedRcos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosEtherFixedRcos_Type.__name__ = "Integer32"
_WwpLeosEtherFixedRcos_Object = MibTableColumn
wwpLeosEtherFixedRcos = _WwpLeosEtherFixedRcos_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 43),
    _WwpLeosEtherFixedRcos_Type()
)
wwpLeosEtherFixedRcos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherFixedRcos.setStatus("current")


class _WwpLeosEtherPortEgressPortQueueMapId_Type(Integer32):
    """Custom type wwpLeosEtherPortEgressPortQueueMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosEtherPortEgressPortQueueMapId_Type.__name__ = "Integer32"
_WwpLeosEtherPortEgressPortQueueMapId_Object = MibTableColumn
wwpLeosEtherPortEgressPortQueueMapId = _WwpLeosEtherPortEgressPortQueueMapId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 44),
    _WwpLeosEtherPortEgressPortQueueMapId_Type()
)
wwpLeosEtherPortEgressPortQueueMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortEgressPortQueueMapId.setStatus("current")


class _WwpLeosEtherPortResolvedCosMapId_Type(Integer32):
    """Custom type wwpLeosEtherPortResolvedCosMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosEtherPortResolvedCosMapId_Type.__name__ = "Integer32"
_WwpLeosEtherPortResolvedCosMapId_Object = MibTableColumn
wwpLeosEtherPortResolvedCosMapId = _WwpLeosEtherPortResolvedCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 45),
    _WwpLeosEtherPortResolvedCosMapId_Type()
)
wwpLeosEtherPortResolvedCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortResolvedCosMapId.setStatus("current")
_WwpLeosEtherPortResolvedCosRemarkL2_Type = TruthValue
_WwpLeosEtherPortResolvedCosRemarkL2_Object = MibTableColumn
wwpLeosEtherPortResolvedCosRemarkL2 = _WwpLeosEtherPortResolvedCosRemarkL2_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 46),
    _WwpLeosEtherPortResolvedCosRemarkL2_Type()
)
wwpLeosEtherPortResolvedCosRemarkL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortResolvedCosRemarkL2.setStatus("current")


class _WwpLeosEtherPortL2TransformMode_Type(Integer32):
    """Custom type wwpLeosEtherPortL2TransformMode based on Integer32"""
    defaultValue = 1

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
        *(("iPush-e-Pop", 1),
          ("iPush-e-PopStamp", 3),
          ("iStamp-Push-e-QualifiedPopStamp", 2),
          ("none", 0))
    )


_WwpLeosEtherPortL2TransformMode_Type.__name__ = "Integer32"
_WwpLeosEtherPortL2TransformMode_Object = MibTableColumn
wwpLeosEtherPortL2TransformMode = _WwpLeosEtherPortL2TransformMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 47),
    _WwpLeosEtherPortL2TransformMode_Type()
)
wwpLeosEtherPortL2TransformMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortL2TransformMode.setStatus("current")


class _WwpLeosEtherPortLinkFlapDetection_Type(TruthValue):
    """Custom type wwpLeosEtherPortLinkFlapDetection based on TruthValue"""


_WwpLeosEtherPortLinkFlapDetection_Object = MibTableColumn
wwpLeosEtherPortLinkFlapDetection = _WwpLeosEtherPortLinkFlapDetection_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 48),
    _WwpLeosEtherPortLinkFlapDetection_Type()
)
wwpLeosEtherPortLinkFlapDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortLinkFlapDetection.setStatus("current")


class _WwpLeosEtherPortLinkFlapCount_Type(Integer32):
    """Custom type wwpLeosEtherPortLinkFlapCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WwpLeosEtherPortLinkFlapCount_Type.__name__ = "Integer32"
_WwpLeosEtherPortLinkFlapCount_Object = MibTableColumn
wwpLeosEtherPortLinkFlapCount = _WwpLeosEtherPortLinkFlapCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 49),
    _WwpLeosEtherPortLinkFlapCount_Type()
)
wwpLeosEtherPortLinkFlapCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortLinkFlapCount.setStatus("current")


class _WwpLeosEtherPortLinkFlapDetectTime_Type(Integer32):
    """Custom type wwpLeosEtherPortLinkFlapDetectTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_WwpLeosEtherPortLinkFlapDetectTime_Type.__name__ = "Integer32"
_WwpLeosEtherPortLinkFlapDetectTime_Object = MibTableColumn
wwpLeosEtherPortLinkFlapDetectTime = _WwpLeosEtherPortLinkFlapDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 50),
    _WwpLeosEtherPortLinkFlapDetectTime_Type()
)
wwpLeosEtherPortLinkFlapDetectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortLinkFlapDetectTime.setStatus("current")


class _WwpLeosEtherPortLinkFlapHoldTime_Type(Integer32):
    """Custom type wwpLeosEtherPortLinkFlapHoldTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_WwpLeosEtherPortLinkFlapHoldTime_Type.__name__ = "Integer32"
_WwpLeosEtherPortLinkFlapHoldTime_Object = MibTableColumn
wwpLeosEtherPortLinkFlapHoldTime = _WwpLeosEtherPortLinkFlapHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 51),
    _WwpLeosEtherPortLinkFlapHoldTime_Type()
)
wwpLeosEtherPortLinkFlapHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortLinkFlapHoldTime.setStatus("current")


class _WwpLeosEtherFixedRColor_Type(PortIngressFixedColor):
    """Custom type wwpLeosEtherFixedRColor based on PortIngressFixedColor"""
    defaultValue = 1


_WwpLeosEtherFixedRColor_Object = MibTableColumn
wwpLeosEtherFixedRColor = _WwpLeosEtherFixedRColor_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 52),
    _WwpLeosEtherFixedRColor_Type()
)
wwpLeosEtherFixedRColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherFixedRColor.setStatus("current")


class _WwpLeosEtherPortFrameCosMapId_Type(Integer32):
    """Custom type wwpLeosEtherPortFrameCosMapId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosEtherPortFrameCosMapId_Type.__name__ = "Integer32"
_WwpLeosEtherPortFrameCosMapId_Object = MibTableColumn
wwpLeosEtherPortFrameCosMapId = _WwpLeosEtherPortFrameCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 53),
    _WwpLeosEtherPortFrameCosMapId_Type()
)
wwpLeosEtherPortFrameCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortFrameCosMapId.setStatus("current")


class _WwpLeosEtherPortEgressCosPolicy_Type(PortEgressFrameCosPolicy):
    """Custom type wwpLeosEtherPortEgressCosPolicy based on PortEgressFrameCosPolicy"""
    defaultValue = 1


_WwpLeosEtherPortEgressCosPolicy_Object = MibTableColumn
wwpLeosEtherPortEgressCosPolicy = _WwpLeosEtherPortEgressCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 54),
    _WwpLeosEtherPortEgressCosPolicy_Type()
)
wwpLeosEtherPortEgressCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortEgressCosPolicy.setStatus("current")
_WwpLeosEtherPortEgressSpeed_Type = Gauge32
_WwpLeosEtherPortEgressSpeed_Object = MibTableColumn
wwpLeosEtherPortEgressSpeed = _WwpLeosEtherPortEgressSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 55),
    _WwpLeosEtherPortEgressSpeed_Type()
)
wwpLeosEtherPortEgressSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortEgressSpeed.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosEtherPortEgressSpeed.setUnits("kbps")
_WwpLeosEtherPortAdaptiveRateSpeed_Type = Gauge32
_WwpLeosEtherPortAdaptiveRateSpeed_Object = MibTableColumn
wwpLeosEtherPortAdaptiveRateSpeed = _WwpLeosEtherPortAdaptiveRateSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 56),
    _WwpLeosEtherPortAdaptiveRateSpeed_Type()
)
wwpLeosEtherPortAdaptiveRateSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortAdaptiveRateSpeed.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosEtherPortAdaptiveRateSpeed.setUnits("kbps")


class _WwpLeosEtherPortMirrorEncap_Type(Integer32):
    """Custom type wwpLeosEtherPortMirrorEncap based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("vlanTag", 1))
    )


_WwpLeosEtherPortMirrorEncap_Type.__name__ = "Integer32"
_WwpLeosEtherPortMirrorEncap_Object = MibTableColumn
wwpLeosEtherPortMirrorEncap = _WwpLeosEtherPortMirrorEncap_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 57),
    _WwpLeosEtherPortMirrorEncap_Type()
)
wwpLeosEtherPortMirrorEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortMirrorEncap.setStatus("current")


class _WwpLeosEtherPortMirrorEncapVid_Type(Integer32):
    """Custom type wwpLeosEtherPortMirrorEncapVid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24576),
    )


_WwpLeosEtherPortMirrorEncapVid_Type.__name__ = "Integer32"
_WwpLeosEtherPortMirrorEncapVid_Object = MibTableColumn
wwpLeosEtherPortMirrorEncapVid = _WwpLeosEtherPortMirrorEncapVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 58),
    _WwpLeosEtherPortMirrorEncapVid_Type()
)
wwpLeosEtherPortMirrorEncapVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortMirrorEncapVid.setStatus("current")


class _WwpLeosEtherPortMirrorEncapTpid_Type(Integer32):
    """Custom type wwpLeosEtherPortMirrorEncapTpid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tpid8100", 1),
          ("tpid88A8", 3),
          ("tpid9100", 2))
    )


_WwpLeosEtherPortMirrorEncapTpid_Type.__name__ = "Integer32"
_WwpLeosEtherPortMirrorEncapTpid_Object = MibTableColumn
wwpLeosEtherPortMirrorEncapTpid = _WwpLeosEtherPortMirrorEncapTpid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 59),
    _WwpLeosEtherPortMirrorEncapTpid_Type()
)
wwpLeosEtherPortMirrorEncapTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortMirrorEncapTpid.setStatus("current")


class _WwpLeosEtherPortIfgDecrease_Type(Integer32):
    """Custom type wwpLeosEtherPortIfgDecrease based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_WwpLeosEtherPortIfgDecrease_Type.__name__ = "Integer32"
_WwpLeosEtherPortIfgDecrease_Object = MibTableColumn
wwpLeosEtherPortIfgDecrease = _WwpLeosEtherPortIfgDecrease_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 60),
    _WwpLeosEtherPortIfgDecrease_Type()
)
wwpLeosEtherPortIfgDecrease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortIfgDecrease.setStatus("current")


class _WwpLeosEtherPortAdvertSpeed_Type(Integer32):
    """Custom type wwpLeosEtherPortAdvertSpeed based on Integer32"""
    defaultValue = 5

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
        *(("gigabit", 4),
          ("hundred", 3),
          ("not-applicable", 1),
          ("ten", 2),
          ("ten-hundred-gigabit", 5))
    )


_WwpLeosEtherPortAdvertSpeed_Type.__name__ = "Integer32"
_WwpLeosEtherPortAdvertSpeed_Object = MibTableColumn
wwpLeosEtherPortAdvertSpeed = _WwpLeosEtherPortAdvertSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 61),
    _WwpLeosEtherPortAdvertSpeed_Type()
)
wwpLeosEtherPortAdvertSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortAdvertSpeed.setStatus("current")


class _WwpLeosEtherPortAdvertDuplex_Type(Integer32):
    """Custom type wwpLeosEtherPortAdvertDuplex based on Integer32"""
    defaultValue = 4

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
        *(("full", 3),
          ("half", 2),
          ("half-full", 4),
          ("not-applicable", 1))
    )


_WwpLeosEtherPortAdvertDuplex_Type.__name__ = "Integer32"
_WwpLeosEtherPortAdvertDuplex_Object = MibTableColumn
wwpLeosEtherPortAdvertDuplex = _WwpLeosEtherPortAdvertDuplex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 1, 1, 62),
    _WwpLeosEtherPortAdvertDuplex_Type()
)
wwpLeosEtherPortAdvertDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortAdvertDuplex.setStatus("current")
_WwpLeosEtherPortFlushTable_Object = MibTable
wwpLeosEtherPortFlushTable = _WwpLeosEtherPortFlushTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpLeosEtherPortFlushTable.setStatus("current")
_WwpLeosEtherPortFlushEntry_Object = MibTableRow
wwpLeosEtherPortFlushEntry = _WwpLeosEtherPortFlushEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 2, 1)
)
wwpLeosEtherPortFlushEntry.setIndexNames(
    (0, "WWP-LEOS-PORT-MIB", "wwpLeosEtherPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosEtherPortFlushEntry.setStatus("current")


class _WwpLeosEtherPortFlushActivate_Type(TruthValue):
    """Custom type wwpLeosEtherPortFlushActivate based on TruthValue"""


_WwpLeosEtherPortFlushActivate_Object = MibTableColumn
wwpLeosEtherPortFlushActivate = _WwpLeosEtherPortFlushActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 2, 1, 1),
    _WwpLeosEtherPortFlushActivate_Type()
)
wwpLeosEtherPortFlushActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortFlushActivate.setStatus("current")
_WwpLeosEtherPortTrapsTable_Object = MibTable
wwpLeosEtherPortTrapsTable = _WwpLeosEtherPortTrapsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpLeosEtherPortTrapsTable.setStatus("current")
_WwpLeosEtherPortTrapsEntry_Object = MibTableRow
wwpLeosEtherPortTrapsEntry = _WwpLeosEtherPortTrapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 3, 1)
)
wwpLeosEtherPortTrapsEntry.setIndexNames(
    (0, "WWP-LEOS-PORT-MIB", "wwpLeosEtherPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosEtherPortTrapsEntry.setStatus("current")


class _WwpLeosEtherPortTrapsState_Type(Integer32):
    """Custom type wwpLeosEtherPortTrapsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_WwpLeosEtherPortTrapsState_Type.__name__ = "Integer32"
_WwpLeosEtherPortTrapsState_Object = MibTableColumn
wwpLeosEtherPortTrapsState = _WwpLeosEtherPortTrapsState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 3, 1, 1),
    _WwpLeosEtherPortTrapsState_Type()
)
wwpLeosEtherPortTrapsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortTrapsState.setStatus("current")
_WwpLeosEtherPortStateMirrorGroupTable_Object = MibTable
wwpLeosEtherPortStateMirrorGroupTable = _WwpLeosEtherPortStateMirrorGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wwpLeosEtherPortStateMirrorGroupTable.setStatus("current")
_WwpLeosEtherPortStateMirrorGroupEntry_Object = MibTableRow
wwpLeosEtherPortStateMirrorGroupEntry = _WwpLeosEtherPortStateMirrorGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 4, 1)
)
wwpLeosEtherPortStateMirrorGroupEntry.setIndexNames(
    (0, "WWP-LEOS-PORT-MIB", "wwpLeosEtherPortStateMirrorGroupId"),
)
if mibBuilder.loadTexts:
    wwpLeosEtherPortStateMirrorGroupEntry.setStatus("current")


class _WwpLeosEtherPortStateMirrorGroupId_Type(Integer32):
    """Custom type wwpLeosEtherPortStateMirrorGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosEtherPortStateMirrorGroupId_Type.__name__ = "Integer32"
_WwpLeosEtherPortStateMirrorGroupId_Object = MibTableColumn
wwpLeosEtherPortStateMirrorGroupId = _WwpLeosEtherPortStateMirrorGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 4, 1, 1),
    _WwpLeosEtherPortStateMirrorGroupId_Type()
)
wwpLeosEtherPortStateMirrorGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortStateMirrorGroupId.setStatus("current")


class _WwpLeosEtherPortStateMirrorGroupName_Type(DisplayString):
    """Custom type wwpLeosEtherPortStateMirrorGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_WwpLeosEtherPortStateMirrorGroupName_Type.__name__ = "DisplayString"
_WwpLeosEtherPortStateMirrorGroupName_Object = MibTableColumn
wwpLeosEtherPortStateMirrorGroupName = _WwpLeosEtherPortStateMirrorGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 4, 1, 2),
    _WwpLeosEtherPortStateMirrorGroupName_Type()
)
wwpLeosEtherPortStateMirrorGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosEtherPortStateMirrorGroupName.setStatus("current")


class _WwpLeosEtherPortStateMirrorGroupOperStatus_Type(Integer32):
    """Custom type wwpLeosEtherPortStateMirrorGroupOperStatus based on Integer32"""
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


_WwpLeosEtherPortStateMirrorGroupOperStatus_Type.__name__ = "Integer32"
_WwpLeosEtherPortStateMirrorGroupOperStatus_Object = MibTableColumn
wwpLeosEtherPortStateMirrorGroupOperStatus = _WwpLeosEtherPortStateMirrorGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 4, 1, 3),
    _WwpLeosEtherPortStateMirrorGroupOperStatus_Type()
)
wwpLeosEtherPortStateMirrorGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortStateMirrorGroupOperStatus.setStatus("current")
_WwpLeosEtherPortStateMirrorGroupNumSrcPorts_Type = Counter32
_WwpLeosEtherPortStateMirrorGroupNumSrcPorts_Object = MibTableColumn
wwpLeosEtherPortStateMirrorGroupNumSrcPorts = _WwpLeosEtherPortStateMirrorGroupNumSrcPorts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 4, 1, 4),
    _WwpLeosEtherPortStateMirrorGroupNumSrcPorts_Type()
)
wwpLeosEtherPortStateMirrorGroupNumSrcPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortStateMirrorGroupNumSrcPorts.setStatus("current")
_WwpLeosEtherPortStateMirrorGroupNumDstPorts_Type = Counter32
_WwpLeosEtherPortStateMirrorGroupNumDstPorts_Object = MibTableColumn
wwpLeosEtherPortStateMirrorGroupNumDstPorts = _WwpLeosEtherPortStateMirrorGroupNumDstPorts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 4, 1, 5),
    _WwpLeosEtherPortStateMirrorGroupNumDstPorts_Type()
)
wwpLeosEtherPortStateMirrorGroupNumDstPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortStateMirrorGroupNumDstPorts.setStatus("current")
_WwpLeosEtherPortStateMirrorGroupStatus_Type = RowStatus
_WwpLeosEtherPortStateMirrorGroupStatus_Object = MibTableColumn
wwpLeosEtherPortStateMirrorGroupStatus = _WwpLeosEtherPortStateMirrorGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 4, 1, 6),
    _WwpLeosEtherPortStateMirrorGroupStatus_Type()
)
wwpLeosEtherPortStateMirrorGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosEtherPortStateMirrorGroupStatus.setStatus("current")


class _WwpLeosEtherPortStateMirrorGroupType_Type(Integer32):
    """Custom type wwpLeosEtherPortStateMirrorGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 2),
          ("unidirectional", 1))
    )


_WwpLeosEtherPortStateMirrorGroupType_Type.__name__ = "Integer32"
_WwpLeosEtherPortStateMirrorGroupType_Object = MibTableColumn
wwpLeosEtherPortStateMirrorGroupType = _WwpLeosEtherPortStateMirrorGroupType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 4, 1, 7),
    _WwpLeosEtherPortStateMirrorGroupType_Type()
)
wwpLeosEtherPortStateMirrorGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortStateMirrorGroupType.setStatus("current")
_WwpLeosEtherPortStateMirrorGroupMemTable_Object = MibTable
wwpLeosEtherPortStateMirrorGroupMemTable = _WwpLeosEtherPortStateMirrorGroupMemTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wwpLeosEtherPortStateMirrorGroupMemTable.setStatus("current")
_WwpLeosEtherPortStateMirrorGroupMemEntry_Object = MibTableRow
wwpLeosEtherPortStateMirrorGroupMemEntry = _WwpLeosEtherPortStateMirrorGroupMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 5, 1)
)
wwpLeosEtherPortStateMirrorGroupMemEntry.setIndexNames(
    (0, "WWP-LEOS-PORT-MIB", "wwpLeosEtherPortStateMirrorGroupId"),
    (0, "WWP-LEOS-PORT-MIB", "wwpLeosEtherPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosEtherPortStateMirrorGroupMemEntry.setStatus("current")


class _WwpLeosEtherPortStateMirrorGroupMemType_Type(Integer32):
    """Custom type wwpLeosEtherPortStateMirrorGroupMemType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dstPort", 2),
          ("srcPort", 1))
    )


_WwpLeosEtherPortStateMirrorGroupMemType_Type.__name__ = "Integer32"
_WwpLeosEtherPortStateMirrorGroupMemType_Object = MibTableColumn
wwpLeosEtherPortStateMirrorGroupMemType = _WwpLeosEtherPortStateMirrorGroupMemType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 5, 1, 1),
    _WwpLeosEtherPortStateMirrorGroupMemType_Type()
)
wwpLeosEtherPortStateMirrorGroupMemType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosEtherPortStateMirrorGroupMemType.setStatus("current")


class _WwpLeosEtherPortStateMirrorGroupMemOperState_Type(Integer32):
    """Custom type wwpLeosEtherPortStateMirrorGroupMemOperState based on Integer32"""
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


_WwpLeosEtherPortStateMirrorGroupMemOperState_Type.__name__ = "Integer32"
_WwpLeosEtherPortStateMirrorGroupMemOperState_Object = MibTableColumn
wwpLeosEtherPortStateMirrorGroupMemOperState = _WwpLeosEtherPortStateMirrorGroupMemOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 5, 1, 2),
    _WwpLeosEtherPortStateMirrorGroupMemOperState_Type()
)
wwpLeosEtherPortStateMirrorGroupMemOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosEtherPortStateMirrorGroupMemOperState.setStatus("current")
_WwpLeosEtherPortStateMirrorGroupMemStatus_Type = RowStatus
_WwpLeosEtherPortStateMirrorGroupMemStatus_Object = MibTableColumn
wwpLeosEtherPortStateMirrorGroupMemStatus = _WwpLeosEtherPortStateMirrorGroupMemStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 1, 5, 1, 3),
    _WwpLeosEtherPortStateMirrorGroupMemStatus_Type()
)
wwpLeosEtherPortStateMirrorGroupMemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosEtherPortStateMirrorGroupMemStatus.setStatus("current")
_WwpLeosEtherPortNotif_ObjectIdentity = ObjectIdentity
wwpLeosEtherPortNotif = _WwpLeosEtherPortNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 2)
)


class _WwpLeosEtherStndLinkUpDownTrapsEnable_Type(TruthValue):
    """Custom type wwpLeosEtherStndLinkUpDownTrapsEnable based on TruthValue"""


_WwpLeosEtherStndLinkUpDownTrapsEnable_Object = MibScalar
wwpLeosEtherStndLinkUpDownTrapsEnable = _WwpLeosEtherStndLinkUpDownTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 2, 1),
    _WwpLeosEtherStndLinkUpDownTrapsEnable_Type()
)
wwpLeosEtherStndLinkUpDownTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherStndLinkUpDownTrapsEnable.setStatus("current")


class _WwpLeosEtherPortLinkUpDownTrapsEnable_Type(TruthValue):
    """Custom type wwpLeosEtherPortLinkUpDownTrapsEnable based on TruthValue"""


_WwpLeosEtherPortLinkUpDownTrapsEnable_Object = MibScalar
wwpLeosEtherPortLinkUpDownTrapsEnable = _WwpLeosEtherPortLinkUpDownTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 2, 2),
    _WwpLeosEtherPortLinkUpDownTrapsEnable_Type()
)
wwpLeosEtherPortLinkUpDownTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherPortLinkUpDownTrapsEnable.setStatus("current")


class _WwpLeosEtherAggPortLinkUpDownTrapsEnable_Type(TruthValue):
    """Custom type wwpLeosEtherAggPortLinkUpDownTrapsEnable based on TruthValue"""


_WwpLeosEtherAggPortLinkUpDownTrapsEnable_Object = MibScalar
wwpLeosEtherAggPortLinkUpDownTrapsEnable = _WwpLeosEtherAggPortLinkUpDownTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 1, 2, 3),
    _WwpLeosEtherAggPortLinkUpDownTrapsEnable_Type()
)
wwpLeosEtherAggPortLinkUpDownTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosEtherAggPortLinkUpDownTrapsEnable.setStatus("current")
_WwpLeosPortMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosPortMIBNotificationPrefix = _WwpLeosPortMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 2)
)
_WwpLeosPortMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosPortMIBNotifications = _WwpLeosPortMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 2, 0)
)
_WwpLeosPortMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosPortMIBConformance = _WwpLeosPortMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 3)
)
_WwpLeosPortMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosPortMIBCompliances = _WwpLeosPortMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 3, 1)
)
_WwpLeosPortMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosPortMIBGroups = _WwpLeosPortMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpLeosEthLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 2, 0, 3)
)
wwpLeosEthLinkUp.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortId"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortName"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortType"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortAdminStatus"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortOperStatus"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortDesc"))
)
if mibBuilder.loadTexts:
    wwpLeosEthLinkUp.setStatus(
        "current"
    )

wwpLeosEthLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 2, 0, 4)
)
wwpLeosEthLinkDown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortId"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortType"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortName"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortAdminStatus"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortOperStatus"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortDesc"))
)
if mibBuilder.loadTexts:
    wwpLeosEthLinkDown.setStatus(
        "current"
    )

wwpLeosEthAdminSpeedIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 2, 0, 5)
)
wwpLeosEthAdminSpeedIncompatible.setObjects(
    ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortId")
)
if mibBuilder.loadTexts:
    wwpLeosEthAdminSpeedIncompatible.setStatus(
        "current"
    )

wwpLeosEthLinkFlap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 2, 0, 6)
)
wwpLeosEthLinkFlap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortId"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortType"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortName"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortOperStatus"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortDesc"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortLinkFlapHoldTime"))
)
if mibBuilder.loadTexts:
    wwpLeosEthLinkFlap.setStatus(
        "current"
    )

wwpLeosAggLinkUpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 2, 2, 0, 7)
)
wwpLeosAggLinkUpDown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortId"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortName"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortDesc"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortType"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortAdminStatus"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortOperStatus"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortActorAdminKey"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortListPorts"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortName"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortDesc"))
)
if mibBuilder.loadTexts:
    wwpLeosAggLinkUpDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-PORT-MIB",
    **{"PortList": PortList,
       "PortEgressFrameCosPolicy": PortEgressFrameCosPolicy,
       "PortIngressFixedColor": PortIngressFixedColor,
       "wwpLeosPortMIB": wwpLeosPortMIB,
       "wwpLeosPortMIBObjects": wwpLeosPortMIBObjects,
       "wwpLeosEtherPort": wwpLeosEtherPort,
       "wwpLeosEtherPortTable": wwpLeosEtherPortTable,
       "wwpLeosEtherPortEntry": wwpLeosEtherPortEntry,
       "wwpLeosEtherPortId": wwpLeosEtherPortId,
       "wwpLeosEtherPortName": wwpLeosEtherPortName,
       "wwpLeosEtherPortDesc": wwpLeosEtherPortDesc,
       "wwpLeosEtherPortType": wwpLeosEtherPortType,
       "wwpLeosEtherPortPhysAddr": wwpLeosEtherPortPhysAddr,
       "wwpLeosEtherPortAutoNeg": wwpLeosEtherPortAutoNeg,
       "wwpLeosEtherPortAdminStatus": wwpLeosEtherPortAdminStatus,
       "wwpLeosEtherPortOperStatus": wwpLeosEtherPortOperStatus,
       "wwpLeosEtherPortAdminSpeed": wwpLeosEtherPortAdminSpeed,
       "wwpLeosEtherPortOperSpeed": wwpLeosEtherPortOperSpeed,
       "wwpLeosEtherPortAdminDuplex": wwpLeosEtherPortAdminDuplex,
       "wwpLeosEtherPortOperDuplex": wwpLeosEtherPortOperDuplex,
       "wwpLeosEtherPortAdminFlowCtrl": wwpLeosEtherPortAdminFlowCtrl,
       "wwpLeosEtherPortOperFlowCtrl": wwpLeosEtherPortOperFlowCtrl,
       "wwpLeosEtherIngressPvid": wwpLeosEtherIngressPvid,
       "wwpLeosEtherUntagEgressVlanId": wwpLeosEtherUntagEgressVlanId,
       "wwpLeosEtherPortAcceptableFrameTypes": wwpLeosEtherPortAcceptableFrameTypes,
       "wwpLeosEtherPortUntaggedPriority": wwpLeosEtherPortUntaggedPriority,
       "wwpLeosEtherPortMaxFrameSize": wwpLeosEtherPortMaxFrameSize,
       "wwpLeosEtherPortVlanIngressFiltering": wwpLeosEtherPortVlanIngressFiltering,
       "wwpLeosEtherPortAdminAdvertisedFlowCtrl": wwpLeosEtherPortAdminAdvertisedFlowCtrl,
       "wwpLeosEtherPortVplsPortType": wwpLeosEtherPortVplsPortType,
       "wwpLeosEtherPortIngressCosPolicy": wwpLeosEtherPortIngressCosPolicy,
       "wwpLeosEtherPortIngressFixedDot1dPri": wwpLeosEtherPortIngressFixedDot1dPri,
       "wwpLeosEtherPortUntagDataVsi": wwpLeosEtherPortUntagDataVsi,
       "wwpLeosEtherPortOperationalSpeed": wwpLeosEtherPortOperationalSpeed,
       "wwpLeosEtherPortUntagCtrlVsi": wwpLeosEtherPortUntagCtrlVsi,
       "wwpLeosEtherPortMirrorPort": wwpLeosEtherPortMirrorPort,
       "wwpLeosEtherPortMirrorIngress": wwpLeosEtherPortMirrorIngress,
       "wwpLeosEtherPortMirrorEgress": wwpLeosEtherPortMirrorEgress,
       "wwpLeosEtherPortUntagDataVsiType": wwpLeosEtherPortUntagDataVsiType,
       "wwpLeosEtherPortUntagCtrlVsiType": wwpLeosEtherPortUntagCtrlVsiType,
       "wwpLeosEtherPortVsIngressFiltering": wwpLeosEtherPortVsIngressFiltering,
       "wwpLeosEtherPortOperAutoNeg": wwpLeosEtherPortOperAutoNeg,
       "wwpLeosEtherPortUpTime": wwpLeosEtherPortUpTime,
       "wwpLeosEtherPortUntagDataVid": wwpLeosEtherPortUntagDataVid,
       "wwpLeosEtherPortPhyLoopback": wwpLeosEtherPortPhyLoopback,
       "wwpLeosEtherPortVlanIngressFilterStrict": wwpLeosEtherPortVlanIngressFilterStrict,
       "wwpLeosEtherPortMacSaDaSwap": wwpLeosEtherPortMacSaDaSwap,
       "wwpLeosEtherPortMacSaDaSwapVlan": wwpLeosEtherPortMacSaDaSwapVlan,
       "wwpLeosEtherPortResolvedCosPolicy": wwpLeosEtherPortResolvedCosPolicy,
       "wwpLeosEtherPortMode": wwpLeosEtherPortMode,
       "wwpLeosEtherFixedRcos": wwpLeosEtherFixedRcos,
       "wwpLeosEtherPortEgressPortQueueMapId": wwpLeosEtherPortEgressPortQueueMapId,
       "wwpLeosEtherPortResolvedCosMapId": wwpLeosEtherPortResolvedCosMapId,
       "wwpLeosEtherPortResolvedCosRemarkL2": wwpLeosEtherPortResolvedCosRemarkL2,
       "wwpLeosEtherPortL2TransformMode": wwpLeosEtherPortL2TransformMode,
       "wwpLeosEtherPortLinkFlapDetection": wwpLeosEtherPortLinkFlapDetection,
       "wwpLeosEtherPortLinkFlapCount": wwpLeosEtherPortLinkFlapCount,
       "wwpLeosEtherPortLinkFlapDetectTime": wwpLeosEtherPortLinkFlapDetectTime,
       "wwpLeosEtherPortLinkFlapHoldTime": wwpLeosEtherPortLinkFlapHoldTime,
       "wwpLeosEtherFixedRColor": wwpLeosEtherFixedRColor,
       "wwpLeosEtherPortFrameCosMapId": wwpLeosEtherPortFrameCosMapId,
       "wwpLeosEtherPortEgressCosPolicy": wwpLeosEtherPortEgressCosPolicy,
       "wwpLeosEtherPortEgressSpeed": wwpLeosEtherPortEgressSpeed,
       "wwpLeosEtherPortAdaptiveRateSpeed": wwpLeosEtherPortAdaptiveRateSpeed,
       "wwpLeosEtherPortMirrorEncap": wwpLeosEtherPortMirrorEncap,
       "wwpLeosEtherPortMirrorEncapVid": wwpLeosEtherPortMirrorEncapVid,
       "wwpLeosEtherPortMirrorEncapTpid": wwpLeosEtherPortMirrorEncapTpid,
       "wwpLeosEtherPortIfgDecrease": wwpLeosEtherPortIfgDecrease,
       "wwpLeosEtherPortAdvertSpeed": wwpLeosEtherPortAdvertSpeed,
       "wwpLeosEtherPortAdvertDuplex": wwpLeosEtherPortAdvertDuplex,
       "wwpLeosEtherPortFlushTable": wwpLeosEtherPortFlushTable,
       "wwpLeosEtherPortFlushEntry": wwpLeosEtherPortFlushEntry,
       "wwpLeosEtherPortFlushActivate": wwpLeosEtherPortFlushActivate,
       "wwpLeosEtherPortTrapsTable": wwpLeosEtherPortTrapsTable,
       "wwpLeosEtherPortTrapsEntry": wwpLeosEtherPortTrapsEntry,
       "wwpLeosEtherPortTrapsState": wwpLeosEtherPortTrapsState,
       "wwpLeosEtherPortStateMirrorGroupTable": wwpLeosEtherPortStateMirrorGroupTable,
       "wwpLeosEtherPortStateMirrorGroupEntry": wwpLeosEtherPortStateMirrorGroupEntry,
       "wwpLeosEtherPortStateMirrorGroupId": wwpLeosEtherPortStateMirrorGroupId,
       "wwpLeosEtherPortStateMirrorGroupName": wwpLeosEtherPortStateMirrorGroupName,
       "wwpLeosEtherPortStateMirrorGroupOperStatus": wwpLeosEtherPortStateMirrorGroupOperStatus,
       "wwpLeosEtherPortStateMirrorGroupNumSrcPorts": wwpLeosEtherPortStateMirrorGroupNumSrcPorts,
       "wwpLeosEtherPortStateMirrorGroupNumDstPorts": wwpLeosEtherPortStateMirrorGroupNumDstPorts,
       "wwpLeosEtherPortStateMirrorGroupStatus": wwpLeosEtherPortStateMirrorGroupStatus,
       "wwpLeosEtherPortStateMirrorGroupType": wwpLeosEtherPortStateMirrorGroupType,
       "wwpLeosEtherPortStateMirrorGroupMemTable": wwpLeosEtherPortStateMirrorGroupMemTable,
       "wwpLeosEtherPortStateMirrorGroupMemEntry": wwpLeosEtherPortStateMirrorGroupMemEntry,
       "wwpLeosEtherPortStateMirrorGroupMemType": wwpLeosEtherPortStateMirrorGroupMemType,
       "wwpLeosEtherPortStateMirrorGroupMemOperState": wwpLeosEtherPortStateMirrorGroupMemOperState,
       "wwpLeosEtherPortStateMirrorGroupMemStatus": wwpLeosEtherPortStateMirrorGroupMemStatus,
       "wwpLeosEtherPortNotif": wwpLeosEtherPortNotif,
       "wwpLeosEtherStndLinkUpDownTrapsEnable": wwpLeosEtherStndLinkUpDownTrapsEnable,
       "wwpLeosEtherPortLinkUpDownTrapsEnable": wwpLeosEtherPortLinkUpDownTrapsEnable,
       "wwpLeosEtherAggPortLinkUpDownTrapsEnable": wwpLeosEtherAggPortLinkUpDownTrapsEnable,
       "wwpLeosPortMIBNotificationPrefix": wwpLeosPortMIBNotificationPrefix,
       "wwpLeosPortMIBNotifications": wwpLeosPortMIBNotifications,
       "wwpLeosEthLinkUp": wwpLeosEthLinkUp,
       "wwpLeosEthLinkDown": wwpLeosEthLinkDown,
       "wwpLeosEthAdminSpeedIncompatible": wwpLeosEthAdminSpeedIncompatible,
       "wwpLeosEthLinkFlap": wwpLeosEthLinkFlap,
       "wwpLeosAggLinkUpDown": wwpLeosAggLinkUpDown,
       "wwpLeosPortMIBConformance": wwpLeosPortMIBConformance,
       "wwpLeosPortMIBCompliances": wwpLeosPortMIBCompliances,
       "wwpLeosPortMIBGroups": wwpLeosPortMIBGroups}
)
