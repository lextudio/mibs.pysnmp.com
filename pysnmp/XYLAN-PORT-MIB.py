# SNMP MIB module (XYLAN-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:10 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

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

(xylanVportArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanVportArch")


# MODULE-IDENTITY


# Types definitions



class XylanPortFuncCodes(Integer32):
    """Custom type XylanPortFuncCodes based on Integer32"""
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
              10,
              12,
              13,
              14,
              15,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215)
        )
    )
    namedValues = NamedValues(
        *(("atmLANE", 7),
          ("atmMUX", 9),
          ("atmtrunk", 6),
          ("bridge", 4),
          ("cip", 8),
          ("frtrunking", 12),
          ("lsm", 15),
          ("other", 2),
          ("phyatm25", 209),
          ("phyatm50", 210),
          ("phycddi", 208),
          ("phyds1", 211),
          ("phyds3", 212),
          ("phyeth", 203),
          ("phyfddi", 207),
          ("phyoc12", 214),
          ("phyoc3", 213),
          ("phyoc48", 215),
          ("phytr16m", 206),
          ("phytr4m", 205),
          ("phyx100eth", 204),
          ("router", 3),
          ("trunk", 5),
          ("unknown", 1),
          ("vlmp80210", 10),
          ("vlmp8021q", 14),
          ("vlmpDBr", 13))
    )





class XylanVportAdminStatCodes(Integer32):
    """Custom type XylanVportAdminStatCodes based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("disable", 1),
          ("enable", 2),
          ("modify", 5))
    )





class XylanPortOperStatCodes(Integer32):
    """Custom type XylanPortOperStatCodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("portDown", 2),
          ("portUp", 3),
          ("unknown", 1))
    )





class XylanVportEncapsulationCodes(Integer32):
    """Custom type XylanVportEncapsulationCodes based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ethII", 8),
          ("ethIIllc", 3),
          ("llc", 6),
          ("mediaDefault", 2),
          ("snap", 9),
          ("snapllc", 7),
          ("switch", 1),
          ("tunnelOption1", 4),
          ("tunnelOption2", 5))
    )





class XylanVportTranslationCodes(Integer32):
    """Custom type XylanVportTranslationCodes based on Integer32"""
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
        *(("ethertype", 1),
          ("llc", 2),
          ("prop", 4),
          ("snap", 3),
          ("tunnel1", 5),
          ("tunnel2", 6))
    )





class XylanPhyPortTypeCodes(Integer32):
    """Custom type XylanPhyPortTypeCodes based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              18,
              19,
              21)
        )
    )
    namedValues = NamedValues(
        *(("atm25", 9),
          ("atm50", 10),
          ("cddi", 8),
          ("ds1", 11),
          ("ds3", 12),
          ("e1", 18),
          ("e3", 19),
          ("eth", 3),
          ("fddi", 7),
          ("oc12", 14),
          ("oc3", 13),
          ("oc48", 15),
          ("other", 2),
          ("serial", 21),
          ("tr16m", 6),
          ("tr4m", 5),
          ("unknown", 1),
          ("wsm", 16),
          ("x100eth", 4))
    )





class XylanPhyPortAdminStatCodes(Integer32):
    """Custom type XylanPhyPortAdminStatCodes based on Integer32"""
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





class XylanMirrorEnableCodes(Integer32):
    """Custom type XylanMirrorEnableCodes based on Integer32"""
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VirtualPort_ObjectIdentity = ObjectIdentity
virtualPort = _VirtualPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1)
)
_VportTable_Object = MibTable
vportTable = _VportTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    vportTable.setStatus("mandatory")
_VportEntry_Object = MibTableRow
vportEntry = _VportEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1)
)
vportEntry.setIndexNames(
    (0, "XYLAN-PORT-MIB", "vportSlot"),
    (0, "XYLAN-PORT-MIB", "vportIF"),
    (0, "XYLAN-PORT-MIB", "vportFuncType"),
    (0, "XYLAN-PORT-MIB", "vportFuncTypeInstance"),
)
if mibBuilder.loadTexts:
    vportEntry.setStatus("mandatory")


class _VportNumber_Type(Integer32):
    """Custom type vportNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VportNumber_Type.__name__ = "Integer32"
_VportNumber_Object = MibTableColumn
vportNumber = _VportNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 1),
    _VportNumber_Type()
)
vportNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportNumber.setStatus("mandatory")


class _VportSlot_Type(Integer32):
    """Custom type vportSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_VportSlot_Type.__name__ = "Integer32"
_VportSlot_Object = MibTableColumn
vportSlot = _VportSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 2),
    _VportSlot_Type()
)
vportSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSlot.setStatus("mandatory")


class _VportIF_Type(Integer32):
    """Custom type vportIF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VportIF_Type.__name__ = "Integer32"
_VportIF_Object = MibTableColumn
vportIF = _VportIF_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 3),
    _VportIF_Type()
)
vportIF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportIF.setStatus("mandatory")
_VportFuncType_Type = XylanPortFuncCodes
_VportFuncType_Object = MibTableColumn
vportFuncType = _VportFuncType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 4),
    _VportFuncType_Type()
)
vportFuncType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportFuncType.setStatus("mandatory")


class _VportFuncTypeInstance_Type(Integer32):
    """Custom type vportFuncTypeInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VportFuncTypeInstance_Type.__name__ = "Integer32"
_VportFuncTypeInstance_Object = MibTableColumn
vportFuncTypeInstance = _VportFuncTypeInstance_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 5),
    _VportFuncTypeInstance_Type()
)
vportFuncTypeInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportFuncTypeInstance.setStatus("mandatory")


class _VportVlanNumber_Type(Integer32):
    """Custom type vportVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VportVlanNumber_Type.__name__ = "Integer32"
_VportVlanNumber_Object = MibTableColumn
vportVlanNumber = _VportVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 6),
    _VportVlanNumber_Type()
)
vportVlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportVlanNumber.setStatus("mandatory")
_VportMACaddress_Type = MacAddress
_VportMACaddress_Object = MibTableColumn
vportMACaddress = _VportMACaddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 7),
    _VportMACaddress_Type()
)
vportMACaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportMACaddress.setStatus("mandatory")


class _VportBridgeProtocol_Type(Integer32):
    """Custom type vportBridgeProtocol based on Integer32"""
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
        *(("other", 2),
          ("sourcerouting", 4),
          ("srtransparent", 5),
          ("transparent", 3),
          ("unknown", 1))
    )


_VportBridgeProtocol_Type.__name__ = "Integer32"
_VportBridgeProtocol_Object = MibTableColumn
vportBridgeProtocol = _VportBridgeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 8),
    _VportBridgeProtocol_Type()
)
vportBridgeProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportBridgeProtocol.setStatus("mandatory")
_VportEncapsulation_Type = XylanVportEncapsulationCodes
_VportEncapsulation_Object = MibTableColumn
vportEncapsulation = _VportEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 9),
    _VportEncapsulation_Type()
)
vportEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportEncapsulation.setStatus("mandatory")


class _VportBrdgMode_Type(Integer32):
    """Custom type vportBrdgMode based on Integer32"""
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
        *(("autoSwitch", 3),
          ("forceBridge", 4),
          ("forceSwitch", 5),
          ("other", 2),
          ("unknown", 1))
    )


_VportBrdgMode_Type.__name__ = "Integer32"
_VportBrdgMode_Object = MibTableColumn
vportBrdgMode = _VportBrdgMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 10),
    _VportBrdgMode_Type()
)
vportBrdgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportBrdgMode.setStatus("mandatory")


class _VportSwitchTimer_Type(Integer32):
    """Custom type vportSwitchTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VportSwitchTimer_Type.__name__ = "Integer32"
_VportSwitchTimer_Object = MibTableColumn
vportSwitchTimer = _VportSwitchTimer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 11),
    _VportSwitchTimer_Type()
)
vportSwitchTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchTimer.setStatus("mandatory")


class _VportDescription_Type(DisplayString):
    """Custom type vportDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_VportDescription_Type.__name__ = "DisplayString"
_VportDescription_Object = MibTableColumn
vportDescription = _VportDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 12),
    _VportDescription_Type()
)
vportDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportDescription.setStatus("mandatory")
_VportAdmStatus_Type = XylanVportAdminStatCodes
_VportAdmStatus_Object = MibTableColumn
vportAdmStatus = _VportAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 13),
    _VportAdmStatus_Type()
)
vportAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportAdmStatus.setStatus("mandatory")
_VportOperStatus_Type = XylanPortOperStatCodes
_VportOperStatus_Object = MibTableColumn
vportOperStatus = _VportOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 14),
    _VportOperStatus_Type()
)
vportOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportOperStatus.setStatus("mandatory")
_VportFrameIns_Type = Counter32
_VportFrameIns_Object = MibTableColumn
vportFrameIns = _VportFrameIns_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 15),
    _VportFrameIns_Type()
)
vportFrameIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportFrameIns.setStatus("mandatory")
_VportInOctets_Type = Counter32
_VportInOctets_Object = MibTableColumn
vportInOctets = _VportInOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 16),
    _VportInOctets_Type()
)
vportInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportInOctets.setStatus("mandatory")
_VportInUcastPkts_Type = Counter32
_VportInUcastPkts_Object = MibTableColumn
vportInUcastPkts = _VportInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 17),
    _VportInUcastPkts_Type()
)
vportInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportInUcastPkts.setStatus("mandatory")
_VportInNUcastPkts_Type = Counter32
_VportInNUcastPkts_Object = MibTableColumn
vportInNUcastPkts = _VportInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 18),
    _VportInNUcastPkts_Type()
)
vportInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportInNUcastPkts.setStatus("mandatory")
_VportInBufDiscs_Type = Counter32
_VportInBufDiscs_Object = MibTableColumn
vportInBufDiscs = _VportInBufDiscs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 19),
    _VportInBufDiscs_Type()
)
vportInBufDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportInBufDiscs.setStatus("mandatory")
_VportInErrDiscs_Type = Counter32
_VportInErrDiscs_Object = MibTableColumn
vportInErrDiscs = _VportInErrDiscs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 20),
    _VportInErrDiscs_Type()
)
vportInErrDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportInErrDiscs.setStatus("mandatory")
_VportFrameOuts_Type = Counter32
_VportFrameOuts_Object = MibTableColumn
vportFrameOuts = _VportFrameOuts_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 21),
    _VportFrameOuts_Type()
)
vportFrameOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportFrameOuts.setStatus("mandatory")
_VportOutOctets_Type = Counter32
_VportOutOctets_Object = MibTableColumn
vportOutOctets = _VportOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 22),
    _VportOutOctets_Type()
)
vportOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportOutOctets.setStatus("mandatory")
_VportOutUcastPkts_Type = Counter32
_VportOutUcastPkts_Object = MibTableColumn
vportOutUcastPkts = _VportOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 23),
    _VportOutUcastPkts_Type()
)
vportOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportOutUcastPkts.setStatus("mandatory")
_VportOutNUcastPkts_Type = Counter32
_VportOutNUcastPkts_Object = MibTableColumn
vportOutNUcastPkts = _VportOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 24),
    _VportOutNUcastPkts_Type()
)
vportOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportOutNUcastPkts.setStatus("mandatory")
_VportOutBufDiscs_Type = Counter32
_VportOutBufDiscs_Object = MibTableColumn
vportOutBufDiscs = _VportOutBufDiscs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 25),
    _VportOutBufDiscs_Type()
)
vportOutBufDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportOutBufDiscs.setStatus("mandatory")
_VportOutErrDiscs_Type = Counter32
_VportOutErrDiscs_Object = MibTableColumn
vportOutErrDiscs = _VportOutErrDiscs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 26),
    _VportOutErrDiscs_Type()
)
vportOutErrDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportOutErrDiscs.setStatus("mandatory")
_VportFloodLimit_Type = Integer32
_VportFloodLimit_Object = MibTableColumn
vportFloodLimit = _VportFloodLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 27),
    _VportFloodLimit_Type()
)
vportFloodLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportFloodLimit.setStatus("mandatory")
_VportVLANMembership_Type = Integer32
_VportVLANMembership_Object = MibTableColumn
vportVLANMembership = _VportVLANMembership_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 28),
    _VportVLANMembership_Type()
)
vportVLANMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportVLANMembership.setStatus("mandatory")


class _VportManualMode_Type(Integer32):
    """Custom type vportManualMode based on Integer32"""
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
        *(("dynamic", 1),
          ("manual-override-blocking", 3),
          ("manual-override-forwarding", 2),
          ("mode-not-applicable", 4))
    )


_VportManualMode_Type.__name__ = "Integer32"
_VportManualMode_Object = MibTableColumn
vportManualMode = _VportManualMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 29),
    _VportManualMode_Type()
)
vportManualMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportManualMode.setStatus("mandatory")
_VportMVLANMembership_Type = Integer32
_VportMVLANMembership_Object = MibTableColumn
vportMVLANMembership = _VportMVLANMembership_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 30),
    _VportMVLANMembership_Type()
)
vportMVLANMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportMVLANMembership.setStatus("mandatory")
_VportFloodLimitDiscs_Type = Counter32
_VportFloodLimitDiscs_Object = MibTableColumn
vportFloodLimitDiscs = _VportFloodLimitDiscs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 31),
    _VportFloodLimitDiscs_Type()
)
vportFloodLimitDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportFloodLimitDiscs.setStatus("mandatory")
_VportIfIndex_Type = Integer32
_VportIfIndex_Object = MibTableColumn
vportIfIndex = _VportIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 32),
    _VportIfIndex_Type()
)
vportIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportIfIndex.setStatus("mandatory")
_VportSwitchTable_Object = MibTable
vportSwitchTable = _VportSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    vportSwitchTable.setStatus("mandatory")
_VportSwitchEntry_Object = MibTableRow
vportSwitchEntry = _VportSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2)
)
vportSwitchEntry.setIndexNames(
    (0, "XYLAN-PORT-MIB", "vportSwitchSlot"),
    (0, "XYLAN-PORT-MIB", "vportSwitchIF"),
    (0, "XYLAN-PORT-MIB", "vportSwitchFuncType"),
    (0, "XYLAN-PORT-MIB", "vportSwitchFuncTypeInstance"),
)
if mibBuilder.loadTexts:
    vportSwitchEntry.setStatus("mandatory")


class _VportSwitchSlot_Type(Integer32):
    """Custom type vportSwitchSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_VportSwitchSlot_Type.__name__ = "Integer32"
_VportSwitchSlot_Object = MibTableColumn
vportSwitchSlot = _VportSwitchSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 1),
    _VportSwitchSlot_Type()
)
vportSwitchSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchSlot.setStatus("mandatory")


class _VportSwitchIF_Type(Integer32):
    """Custom type vportSwitchIF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VportSwitchIF_Type.__name__ = "Integer32"
_VportSwitchIF_Object = MibTableColumn
vportSwitchIF = _VportSwitchIF_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 2),
    _VportSwitchIF_Type()
)
vportSwitchIF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchIF.setStatus("mandatory")
_VportSwitchFuncType_Type = XylanPortFuncCodes
_VportSwitchFuncType_Object = MibTableColumn
vportSwitchFuncType = _VportSwitchFuncType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 3),
    _VportSwitchFuncType_Type()
)
vportSwitchFuncType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchFuncType.setStatus("mandatory")


class _VportSwitchFuncTypeInstance_Type(Integer32):
    """Custom type vportSwitchFuncTypeInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VportSwitchFuncTypeInstance_Type.__name__ = "Integer32"
_VportSwitchFuncTypeInstance_Object = MibTableColumn
vportSwitchFuncTypeInstance = _VportSwitchFuncTypeInstance_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 4),
    _VportSwitchFuncTypeInstance_Type()
)
vportSwitchFuncTypeInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchFuncTypeInstance.setStatus("mandatory")
_VportSwitchipEthertype_Type = XylanVportTranslationCodes
_VportSwitchipEthertype_Object = MibTableColumn
vportSwitchipEthertype = _VportSwitchipEthertype_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 5),
    _VportSwitchipEthertype_Type()
)
vportSwitchipEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchipEthertype.setStatus("mandatory")
_VportSwitchipSnap_Type = XylanVportTranslationCodes
_VportSwitchipSnap_Object = MibTableColumn
vportSwitchipSnap = _VportSwitchipSnap_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 6),
    _VportSwitchipSnap_Type()
)
vportSwitchipSnap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchipSnap.setStatus("mandatory")
_VportSwitchipxEthertype_Type = XylanVportTranslationCodes
_VportSwitchipxEthertype_Object = MibTableColumn
vportSwitchipxEthertype = _VportSwitchipxEthertype_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 7),
    _VportSwitchipxEthertype_Type()
)
vportSwitchipxEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchipxEthertype.setStatus("mandatory")
_VportSwitchipxProp_Type = XylanVportTranslationCodes
_VportSwitchipxProp_Object = MibTableColumn
vportSwitchipxProp = _VportSwitchipxProp_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 8),
    _VportSwitchipxProp_Type()
)
vportSwitchipxProp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchipxProp.setStatus("mandatory")
_VportSwitchipxLlc_Type = XylanVportTranslationCodes
_VportSwitchipxLlc_Object = MibTableColumn
vportSwitchipxLlc = _VportSwitchipxLlc_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 9),
    _VportSwitchipxLlc_Type()
)
vportSwitchipxLlc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchipxLlc.setStatus("mandatory")
_VportSwitchipxSnap_Type = XylanVportTranslationCodes
_VportSwitchipxSnap_Object = MibTableColumn
vportSwitchipxSnap = _VportSwitchipxSnap_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 10),
    _VportSwitchipxSnap_Type()
)
vportSwitchipxSnap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchipxSnap.setStatus("mandatory")
_VportSwitchDefaultTable_Object = MibTable
vportSwitchDefaultTable = _VportSwitchDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    vportSwitchDefaultTable.setStatus("mandatory")
_VportSwitchDefaultEntry_Object = MibTableRow
vportSwitchDefaultEntry = _VportSwitchDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3, 2)
)
vportSwitchDefaultEntry.setIndexNames(
    (0, "XYLAN-PORT-MIB", "vportSwitchDefaultIndex"),
)
if mibBuilder.loadTexts:
    vportSwitchDefaultEntry.setStatus("mandatory")


class _VportSwitchDefaultIndex_Type(Integer32):
    """Custom type vportSwitchDefaultIndex based on Integer32"""
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
        *(("ethLanEmulation", 4),
          ("ethernet", 1),
          ("fddi", 2),
          ("tokenLanEmulation", 5),
          ("tokenring", 3))
    )


_VportSwitchDefaultIndex_Type.__name__ = "Integer32"
_VportSwitchDefaultIndex_Object = MibTableColumn
vportSwitchDefaultIndex = _VportSwitchDefaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3, 2, 1),
    _VportSwitchDefaultIndex_Type()
)
vportSwitchDefaultIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchDefaultIndex.setStatus("mandatory")
_VportSwitchDefaultipEthertype_Type = XylanVportTranslationCodes
_VportSwitchDefaultipEthertype_Object = MibTableColumn
vportSwitchDefaultipEthertype = _VportSwitchDefaultipEthertype_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3, 2, 2),
    _VportSwitchDefaultipEthertype_Type()
)
vportSwitchDefaultipEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchDefaultipEthertype.setStatus("mandatory")
_VportSwitchDefaultipSnap_Type = XylanVportTranslationCodes
_VportSwitchDefaultipSnap_Object = MibTableColumn
vportSwitchDefaultipSnap = _VportSwitchDefaultipSnap_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3, 2, 3),
    _VportSwitchDefaultipSnap_Type()
)
vportSwitchDefaultipSnap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchDefaultipSnap.setStatus("mandatory")
_VportSwitchDefaultipxEthertype_Type = XylanVportTranslationCodes
_VportSwitchDefaultipxEthertype_Object = MibTableColumn
vportSwitchDefaultipxEthertype = _VportSwitchDefaultipxEthertype_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3, 2, 4),
    _VportSwitchDefaultipxEthertype_Type()
)
vportSwitchDefaultipxEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchDefaultipxEthertype.setStatus("mandatory")
_VportSwitchDefaultipxProp_Type = XylanVportTranslationCodes
_VportSwitchDefaultipxProp_Object = MibTableColumn
vportSwitchDefaultipxProp = _VportSwitchDefaultipxProp_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3, 2, 5),
    _VportSwitchDefaultipxProp_Type()
)
vportSwitchDefaultipxProp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchDefaultipxProp.setStatus("mandatory")
_VportSwitchDefaultipxLlc_Type = XylanVportTranslationCodes
_VportSwitchDefaultipxLlc_Object = MibTableColumn
vportSwitchDefaultipxLlc = _VportSwitchDefaultipxLlc_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3, 2, 6),
    _VportSwitchDefaultipxLlc_Type()
)
vportSwitchDefaultipxLlc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchDefaultipxLlc.setStatus("mandatory")
_VportSwitchDefaultipxSnap_Type = XylanVportTranslationCodes
_VportSwitchDefaultipxSnap_Object = MibTableColumn
vportSwitchDefaultipxSnap = _VportSwitchDefaultipxSnap_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3, 2, 7),
    _VportSwitchDefaultipxSnap_Type()
)
vportSwitchDefaultipxSnap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vportSwitchDefaultipxSnap.setStatus("mandatory")
_LogicalPort_ObjectIdentity = ObjectIdentity
logicalPort = _LogicalPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 2)
)
_PhysicalPort_ObjectIdentity = ObjectIdentity
physicalPort = _PhysicalPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3)
)
_PhyPortTable_Object = MibTable
phyPortTable = _PhyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    phyPortTable.setStatus("mandatory")
_PhyPortEntry_Object = MibTableRow
phyPortEntry = _PhyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1)
)
phyPortEntry.setIndexNames(
    (0, "XYLAN-PORT-MIB", "phyPortSlot"),
    (0, "XYLAN-PORT-MIB", "phyPortIF"),
)
if mibBuilder.loadTexts:
    phyPortEntry.setStatus("mandatory")


class _PhyPortSlot_Type(Integer32):
    """Custom type phyPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_PhyPortSlot_Type.__name__ = "Integer32"
_PhyPortSlot_Object = MibTableColumn
phyPortSlot = _PhyPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 1),
    _PhyPortSlot_Type()
)
phyPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortSlot.setStatus("mandatory")


class _PhyPortIF_Type(Integer32):
    """Custom type phyPortIF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PhyPortIF_Type.__name__ = "Integer32"
_PhyPortIF_Object = MibTableColumn
phyPortIF = _PhyPortIF_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 2),
    _PhyPortIF_Type()
)
phyPortIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortIF.setStatus("mandatory")
_PhyPortMediaType_Type = XylanPhyPortTypeCodes
_PhyPortMediaType_Object = MibTableColumn
phyPortMediaType = _PhyPortMediaType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 3),
    _PhyPortMediaType_Type()
)
phyPortMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortMediaType.setStatus("mandatory")


class _PhyPortDescription_Type(DisplayString):
    """Custom type phyPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PhyPortDescription_Type.__name__ = "DisplayString"
_PhyPortDescription_Object = MibTableColumn
phyPortDescription = _PhyPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 4),
    _PhyPortDescription_Type()
)
phyPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phyPortDescription.setStatus("mandatory")
_PhyPortAdmStatus_Type = XylanPhyPortAdminStatCodes
_PhyPortAdmStatus_Object = MibTableColumn
phyPortAdmStatus = _PhyPortAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 5),
    _PhyPortAdmStatus_Type()
)
phyPortAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phyPortAdmStatus.setStatus("mandatory")
_PhyPortOperStatus_Type = XylanPortOperStatCodes
_PhyPortOperStatus_Object = MibTableColumn
phyPortOperStatus = _PhyPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 6),
    _PhyPortOperStatus_Type()
)
phyPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortOperStatus.setStatus("mandatory")
_PhyPortFrameIns_Type = Counter32
_PhyPortFrameIns_Object = MibTableColumn
phyPortFrameIns = _PhyPortFrameIns_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 7),
    _PhyPortFrameIns_Type()
)
phyPortFrameIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortFrameIns.setStatus("mandatory")
_PhyPortInOctets_Type = Counter32
_PhyPortInOctets_Object = MibTableColumn
phyPortInOctets = _PhyPortInOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 8),
    _PhyPortInOctets_Type()
)
phyPortInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortInOctets.setStatus("mandatory")
_PhyPortInUcastPkts_Type = Counter32
_PhyPortInUcastPkts_Object = MibTableColumn
phyPortInUcastPkts = _PhyPortInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 9),
    _PhyPortInUcastPkts_Type()
)
phyPortInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortInUcastPkts.setStatus("mandatory")
_PhyPortInNUcastPkts_Type = Counter32
_PhyPortInNUcastPkts_Object = MibTableColumn
phyPortInNUcastPkts = _PhyPortInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 10),
    _PhyPortInNUcastPkts_Type()
)
phyPortInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortInNUcastPkts.setStatus("mandatory")
_PhyPortInBufDiscs_Type = Counter32
_PhyPortInBufDiscs_Object = MibTableColumn
phyPortInBufDiscs = _PhyPortInBufDiscs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 11),
    _PhyPortInBufDiscs_Type()
)
phyPortInBufDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortInBufDiscs.setStatus("mandatory")
_PhyPortInErrDiscs_Type = Counter32
_PhyPortInErrDiscs_Object = MibTableColumn
phyPortInErrDiscs = _PhyPortInErrDiscs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 12),
    _PhyPortInErrDiscs_Type()
)
phyPortInErrDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortInErrDiscs.setStatus("mandatory")
_PhyPortFrameOuts_Type = Counter32
_PhyPortFrameOuts_Object = MibTableColumn
phyPortFrameOuts = _PhyPortFrameOuts_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 13),
    _PhyPortFrameOuts_Type()
)
phyPortFrameOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortFrameOuts.setStatus("mandatory")
_PhyPortOutOctets_Type = Counter32
_PhyPortOutOctets_Object = MibTableColumn
phyPortOutOctets = _PhyPortOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 14),
    _PhyPortOutOctets_Type()
)
phyPortOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortOutOctets.setStatus("mandatory")
_PhyPortOutUcastPkts_Type = Counter32
_PhyPortOutUcastPkts_Object = MibTableColumn
phyPortOutUcastPkts = _PhyPortOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 15),
    _PhyPortOutUcastPkts_Type()
)
phyPortOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortOutUcastPkts.setStatus("mandatory")
_PhyPortOutNUcastPkts_Type = Counter32
_PhyPortOutNUcastPkts_Object = MibTableColumn
phyPortOutNUcastPkts = _PhyPortOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 16),
    _PhyPortOutNUcastPkts_Type()
)
phyPortOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortOutNUcastPkts.setStatus("mandatory")
_PhyPortOutBufDiscs_Type = Counter32
_PhyPortOutBufDiscs_Object = MibTableColumn
phyPortOutBufDiscs = _PhyPortOutBufDiscs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 17),
    _PhyPortOutBufDiscs_Type()
)
phyPortOutBufDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortOutBufDiscs.setStatus("mandatory")
_PhyPortOutErrDiscs_Type = Counter32
_PhyPortOutErrDiscs_Object = MibTableColumn
phyPortOutErrDiscs = _PhyPortOutErrDiscs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 18),
    _PhyPortOutErrDiscs_Type()
)
phyPortOutErrDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortOutErrDiscs.setStatus("mandatory")
_PhyPortToInterface_Type = Integer32
_PhyPortToInterface_Object = MibTableColumn
phyPortToInterface = _PhyPortToInterface_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 19),
    _PhyPortToInterface_Type()
)
phyPortToInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortToInterface.setStatus("mandatory")


class _PhyPortFddiAdmMode_Type(Integer32):
    """Custom type phyPortFddiAdmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("concentrator", 3),
          ("invalid", 1),
          ("station", 2))
    )


_PhyPortFddiAdmMode_Type.__name__ = "Integer32"
_PhyPortFddiAdmMode_Object = MibTableColumn
phyPortFddiAdmMode = _PhyPortFddiAdmMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 20),
    _PhyPortFddiAdmMode_Type()
)
phyPortFddiAdmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phyPortFddiAdmMode.setStatus("mandatory")


class _PhyPortFddiOpMode_Type(Integer32):
    """Custom type phyPortFddiOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("concentrator", 3),
          ("invalid", 1),
          ("station", 2))
    )


_PhyPortFddiOpMode_Type.__name__ = "Integer32"
_PhyPortFddiOpMode_Object = MibTableColumn
phyPortFddiOpMode = _PhyPortFddiOpMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 21),
    _PhyPortFddiOpMode_Type()
)
phyPortFddiOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPortFddiOpMode.setStatus("mandatory")


class _PhyPortFddiMacFlushMode_Type(Integer32):
    """Custom type phyPortFddiMacFlushMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("invalid", 1))
    )


_PhyPortFddiMacFlushMode_Type.__name__ = "Integer32"
_PhyPortFddiMacFlushMode_Object = MibTableColumn
phyPortFddiMacFlushMode = _PhyPortFddiMacFlushMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 22),
    _PhyPortFddiMacFlushMode_Type()
)
phyPortFddiMacFlushMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phyPortFddiMacFlushMode.setStatus("mandatory")
_MesmConfTable_Object = MibTable
mesmConfTable = _MesmConfTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    mesmConfTable.setStatus("mandatory")
_MesmConfEntry_Object = MibTableRow
mesmConfEntry = _MesmConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2, 1)
)
mesmConfEntry.setIndexNames(
    (0, "XYLAN-PORT-MIB", "mesmPortSlot"),
    (0, "XYLAN-PORT-MIB", "mesmPortIF"),
)
if mibBuilder.loadTexts:
    mesmConfEntry.setStatus("mandatory")


class _MesmPortSlot_Type(Integer32):
    """Custom type mesmPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_MesmPortSlot_Type.__name__ = "Integer32"
_MesmPortSlot_Object = MibTableColumn
mesmPortSlot = _MesmPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2, 1, 1),
    _MesmPortSlot_Type()
)
mesmPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesmPortSlot.setStatus("mandatory")


class _MesmPortIF_Type(Integer32):
    """Custom type mesmPortIF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_MesmPortIF_Type.__name__ = "Integer32"
_MesmPortIF_Object = MibTableColumn
mesmPortIF = _MesmPortIF_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2, 1, 2),
    _MesmPortIF_Type()
)
mesmPortIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesmPortIF.setStatus("mandatory")


class _MesmPortAutoNegotiate_Type(Integer32):
    """Custom type mesmPortAutoNegotiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("non-appl", 3))
    )


_MesmPortAutoNegotiate_Type.__name__ = "Integer32"
_MesmPortAutoNegotiate_Object = MibTableColumn
mesmPortAutoNegotiate = _MesmPortAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2, 1, 3),
    _MesmPortAutoNegotiate_Type()
)
mesmPortAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesmPortAutoNegotiate.setStatus("mandatory")


class _MesmPortAutoSpeed_Type(Integer32):
    """Custom type mesmPortAutoSpeed based on Integer32"""
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
        *(("speed-10", 2),
          ("speed-100", 1),
          ("speed-1000", 5),
          ("speed-auto", 3),
          ("unknown", 4))
    )


_MesmPortAutoSpeed_Type.__name__ = "Integer32"
_MesmPortAutoSpeed_Object = MibTableColumn
mesmPortAutoSpeed = _MesmPortAutoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2, 1, 4),
    _MesmPortAutoSpeed_Type()
)
mesmPortAutoSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesmPortAutoSpeed.setStatus("mandatory")


class _MesmPortAutoDuplexMode_Type(Integer32):
    """Custom type mesmPortAutoDuplexMode based on Integer32"""
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
        *(("auto-duplex", 3),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("unknown", 4))
    )


_MesmPortAutoDuplexMode_Type.__name__ = "Integer32"
_MesmPortAutoDuplexMode_Object = MibTableColumn
mesmPortAutoDuplexMode = _MesmPortAutoDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2, 1, 5),
    _MesmPortAutoDuplexMode_Type()
)
mesmPortAutoDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesmPortAutoDuplexMode.setStatus("mandatory")


class _MesmPortCfgSpeed_Type(Integer32):
    """Custom type mesmPortCfgSpeed based on Integer32"""
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
        *(("speed-10", 2),
          ("speed-100", 1),
          ("speed-1000", 5),
          ("speed-auto", 3),
          ("unknown", 4))
    )


_MesmPortCfgSpeed_Type.__name__ = "Integer32"
_MesmPortCfgSpeed_Object = MibTableColumn
mesmPortCfgSpeed = _MesmPortCfgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2, 1, 6),
    _MesmPortCfgSpeed_Type()
)
mesmPortCfgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesmPortCfgSpeed.setStatus("mandatory")


class _MesmPortCfgDuplexMode_Type(Integer32):
    """Custom type mesmPortCfgDuplexMode based on Integer32"""
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
        *(("auto-duplex", 3),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("unknown", 4))
    )


_MesmPortCfgDuplexMode_Type.__name__ = "Integer32"
_MesmPortCfgDuplexMode_Object = MibTableColumn
mesmPortCfgDuplexMode = _MesmPortCfgDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2, 1, 7),
    _MesmPortCfgDuplexMode_Type()
)
mesmPortCfgDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesmPortCfgDuplexMode.setStatus("mandatory")


class _PhyPortPCause_Type(Integer32):
    """Custom type phyPortPCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("excess-retries", 2),
          ("excess-runts", 3),
          ("flood-q-stalled", 1))
    )


_PhyPortPCause_Type.__name__ = "Integer32"
_PhyPortPCause_Object = MibScalar
phyPortPCause = _PhyPortPCause_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 3),
    _PhyPortPCause_Type()
)
phyPortPCause.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    phyPortPCause.setStatus("mandatory")
_MirrorPort_ObjectIdentity = ObjectIdentity
mirrorPort = _MirrorPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 4)
)
_MirrorTable_Object = MibTable
mirrorTable = _MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    mirrorTable.setStatus("mandatory")
_MirrorEntry_Object = MibTableRow
mirrorEntry = _MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1)
)
mirrorEntry.setIndexNames(
    (0, "XYLAN-PORT-MIB", "mirrorSlot"),
    (0, "XYLAN-PORT-MIB", "mirrorIF"),
    (0, "XYLAN-PORT-MIB", "mirrorFuncType"),
    (0, "XYLAN-PORT-MIB", "mirrorFuncTypeInstance"),
)
if mibBuilder.loadTexts:
    mirrorEntry.setStatus("mandatory")


class _MirrorNumber_Type(Integer32):
    """Custom type mirrorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_MirrorNumber_Type.__name__ = "Integer32"
_MirrorNumber_Object = MibTableColumn
mirrorNumber = _MirrorNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 1),
    _MirrorNumber_Type()
)
mirrorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirrorNumber.setStatus("mandatory")


class _MirrorSlot_Type(Integer32):
    """Custom type mirrorSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_MirrorSlot_Type.__name__ = "Integer32"
_MirrorSlot_Object = MibTableColumn
mirrorSlot = _MirrorSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 2),
    _MirrorSlot_Type()
)
mirrorSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirrorSlot.setStatus("mandatory")


class _MirrorIF_Type(Integer32):
    """Custom type mirrorIF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_MirrorIF_Type.__name__ = "Integer32"
_MirrorIF_Object = MibTableColumn
mirrorIF = _MirrorIF_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 3),
    _MirrorIF_Type()
)
mirrorIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirrorIF.setStatus("mandatory")
_MirrorFuncType_Type = XylanPortFuncCodes
_MirrorFuncType_Object = MibTableColumn
mirrorFuncType = _MirrorFuncType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 4),
    _MirrorFuncType_Type()
)
mirrorFuncType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirrorFuncType.setStatus("mandatory")


class _MirrorFuncTypeInstance_Type(Integer32):
    """Custom type mirrorFuncTypeInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_MirrorFuncTypeInstance_Type.__name__ = "Integer32"
_MirrorFuncTypeInstance_Object = MibTableColumn
mirrorFuncTypeInstance = _MirrorFuncTypeInstance_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 5),
    _MirrorFuncTypeInstance_Type()
)
mirrorFuncTypeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirrorFuncTypeInstance.setStatus("mandatory")


class _MirrorMirroringSlot_Type(Integer32):
    """Custom type mirrorMirroringSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_MirrorMirroringSlot_Type.__name__ = "Integer32"
_MirrorMirroringSlot_Object = MibTableColumn
mirrorMirroringSlot = _MirrorMirroringSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 6),
    _MirrorMirroringSlot_Type()
)
mirrorMirroringSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorMirroringSlot.setStatus("mandatory")


class _MirrorMirroringIF_Type(Integer32):
    """Custom type mirrorMirroringIF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_MirrorMirroringIF_Type.__name__ = "Integer32"
_MirrorMirroringIF_Object = MibTableColumn
mirrorMirroringIF = _MirrorMirroringIF_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 7),
    _MirrorMirroringIF_Type()
)
mirrorMirroringIF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorMirroringIF.setStatus("mandatory")
_MirrorMirroringFuncType_Type = XylanPortFuncCodes
_MirrorMirroringFuncType_Object = MibTableColumn
mirrorMirroringFuncType = _MirrorMirroringFuncType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 8),
    _MirrorMirroringFuncType_Type()
)
mirrorMirroringFuncType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorMirroringFuncType.setStatus("mandatory")


class _MirrorMirroringFuncTypeInstance_Type(Integer32):
    """Custom type mirrorMirroringFuncTypeInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_MirrorMirroringFuncTypeInstance_Type.__name__ = "Integer32"
_MirrorMirroringFuncTypeInstance_Object = MibTableColumn
mirrorMirroringFuncTypeInstance = _MirrorMirroringFuncTypeInstance_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 9),
    _MirrorMirroringFuncTypeInstance_Type()
)
mirrorMirroringFuncTypeInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorMirroringFuncTypeInstance.setStatus("mandatory")
_MirrorStatus_Type = XylanMirrorEnableCodes
_MirrorStatus_Object = MibTableColumn
mirrorStatus = _MirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 10),
    _MirrorStatus_Type()
)
mirrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorStatus.setStatus("mandatory")
_EchannelPort_ObjectIdentity = ObjectIdentity
echannelPort = _EchannelPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-PORT-MIB",
    **{"XylanPortFuncCodes": XylanPortFuncCodes,
       "XylanVportAdminStatCodes": XylanVportAdminStatCodes,
       "XylanPortOperStatCodes": XylanPortOperStatCodes,
       "XylanVportEncapsulationCodes": XylanVportEncapsulationCodes,
       "XylanVportTranslationCodes": XylanVportTranslationCodes,
       "XylanPhyPortTypeCodes": XylanPhyPortTypeCodes,
       "XylanPhyPortAdminStatCodes": XylanPhyPortAdminStatCodes,
       "XylanMirrorEnableCodes": XylanMirrorEnableCodes,
       "virtualPort": virtualPort,
       "vportTable": vportTable,
       "vportEntry": vportEntry,
       "vportNumber": vportNumber,
       "vportSlot": vportSlot,
       "vportIF": vportIF,
       "vportFuncType": vportFuncType,
       "vportFuncTypeInstance": vportFuncTypeInstance,
       "vportVlanNumber": vportVlanNumber,
       "vportMACaddress": vportMACaddress,
       "vportBridgeProtocol": vportBridgeProtocol,
       "vportEncapsulation": vportEncapsulation,
       "vportBrdgMode": vportBrdgMode,
       "vportSwitchTimer": vportSwitchTimer,
       "vportDescription": vportDescription,
       "vportAdmStatus": vportAdmStatus,
       "vportOperStatus": vportOperStatus,
       "vportFrameIns": vportFrameIns,
       "vportInOctets": vportInOctets,
       "vportInUcastPkts": vportInUcastPkts,
       "vportInNUcastPkts": vportInNUcastPkts,
       "vportInBufDiscs": vportInBufDiscs,
       "vportInErrDiscs": vportInErrDiscs,
       "vportFrameOuts": vportFrameOuts,
       "vportOutOctets": vportOutOctets,
       "vportOutUcastPkts": vportOutUcastPkts,
       "vportOutNUcastPkts": vportOutNUcastPkts,
       "vportOutBufDiscs": vportOutBufDiscs,
       "vportOutErrDiscs": vportOutErrDiscs,
       "vportFloodLimit": vportFloodLimit,
       "vportVLANMembership": vportVLANMembership,
       "vportManualMode": vportManualMode,
       "vportMVLANMembership": vportMVLANMembership,
       "vportFloodLimitDiscs": vportFloodLimitDiscs,
       "vportIfIndex": vportIfIndex,
       "vportSwitchTable": vportSwitchTable,
       "vportSwitchEntry": vportSwitchEntry,
       "vportSwitchSlot": vportSwitchSlot,
       "vportSwitchIF": vportSwitchIF,
       "vportSwitchFuncType": vportSwitchFuncType,
       "vportSwitchFuncTypeInstance": vportSwitchFuncTypeInstance,
       "vportSwitchipEthertype": vportSwitchipEthertype,
       "vportSwitchipSnap": vportSwitchipSnap,
       "vportSwitchipxEthertype": vportSwitchipxEthertype,
       "vportSwitchipxProp": vportSwitchipxProp,
       "vportSwitchipxLlc": vportSwitchipxLlc,
       "vportSwitchipxSnap": vportSwitchipxSnap,
       "vportSwitchDefaultTable": vportSwitchDefaultTable,
       "vportSwitchDefaultEntry": vportSwitchDefaultEntry,
       "vportSwitchDefaultIndex": vportSwitchDefaultIndex,
       "vportSwitchDefaultipEthertype": vportSwitchDefaultipEthertype,
       "vportSwitchDefaultipSnap": vportSwitchDefaultipSnap,
       "vportSwitchDefaultipxEthertype": vportSwitchDefaultipxEthertype,
       "vportSwitchDefaultipxProp": vportSwitchDefaultipxProp,
       "vportSwitchDefaultipxLlc": vportSwitchDefaultipxLlc,
       "vportSwitchDefaultipxSnap": vportSwitchDefaultipxSnap,
       "logicalPort": logicalPort,
       "physicalPort": physicalPort,
       "phyPortTable": phyPortTable,
       "phyPortEntry": phyPortEntry,
       "phyPortSlot": phyPortSlot,
       "phyPortIF": phyPortIF,
       "phyPortMediaType": phyPortMediaType,
       "phyPortDescription": phyPortDescription,
       "phyPortAdmStatus": phyPortAdmStatus,
       "phyPortOperStatus": phyPortOperStatus,
       "phyPortFrameIns": phyPortFrameIns,
       "phyPortInOctets": phyPortInOctets,
       "phyPortInUcastPkts": phyPortInUcastPkts,
       "phyPortInNUcastPkts": phyPortInNUcastPkts,
       "phyPortInBufDiscs": phyPortInBufDiscs,
       "phyPortInErrDiscs": phyPortInErrDiscs,
       "phyPortFrameOuts": phyPortFrameOuts,
       "phyPortOutOctets": phyPortOutOctets,
       "phyPortOutUcastPkts": phyPortOutUcastPkts,
       "phyPortOutNUcastPkts": phyPortOutNUcastPkts,
       "phyPortOutBufDiscs": phyPortOutBufDiscs,
       "phyPortOutErrDiscs": phyPortOutErrDiscs,
       "phyPortToInterface": phyPortToInterface,
       "phyPortFddiAdmMode": phyPortFddiAdmMode,
       "phyPortFddiOpMode": phyPortFddiOpMode,
       "phyPortFddiMacFlushMode": phyPortFddiMacFlushMode,
       "mesmConfTable": mesmConfTable,
       "mesmConfEntry": mesmConfEntry,
       "mesmPortSlot": mesmPortSlot,
       "mesmPortIF": mesmPortIF,
       "mesmPortAutoNegotiate": mesmPortAutoNegotiate,
       "mesmPortAutoSpeed": mesmPortAutoSpeed,
       "mesmPortAutoDuplexMode": mesmPortAutoDuplexMode,
       "mesmPortCfgSpeed": mesmPortCfgSpeed,
       "mesmPortCfgDuplexMode": mesmPortCfgDuplexMode,
       "phyPortPCause": phyPortPCause,
       "mirrorPort": mirrorPort,
       "mirrorTable": mirrorTable,
       "mirrorEntry": mirrorEntry,
       "mirrorNumber": mirrorNumber,
       "mirrorSlot": mirrorSlot,
       "mirrorIF": mirrorIF,
       "mirrorFuncType": mirrorFuncType,
       "mirrorFuncTypeInstance": mirrorFuncTypeInstance,
       "mirrorMirroringSlot": mirrorMirroringSlot,
       "mirrorMirroringIF": mirrorMirroringIF,
       "mirrorMirroringFuncType": mirrorMirroringFuncType,
       "mirrorMirroringFuncTypeInstance": mirrorMirroringFuncTypeInstance,
       "mirrorStatus": mirrorStatus,
       "echannelPort": echannelPort}
)
