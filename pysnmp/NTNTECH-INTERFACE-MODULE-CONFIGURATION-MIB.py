# SNMP MIB module (NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:43 2024
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

(NtnDisplayString,
 ntntechInterfaceModule) = mibBuilder.importSymbols(
    "NTNTECH-ROOT-MIB",
    "NtnDisplayString",
    "ntntechInterfaceModule")

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

ntntechInterfaceModuleConfigurationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1)
)
ntntechInterfaceModuleConfigurationMIB.setRevisions(
        ("1902-08-06 11:50",
         "1902-08-28 10:23",
         "1902-10-11 09:40",
         "1902-10-22 02:00",
         "1903-09-30 10:59",
         "1904-10-11 09:32",
         "1904-11-17 10:59")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IfModCfgMIBObjects_ObjectIdentity = ObjectIdentity
ifModCfgMIBObjects = _IfModCfgMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1)
)
_IfModCfgParameterConfiguration_ObjectIdentity = ObjectIdentity
ifModCfgParameterConfiguration = _IfModCfgParameterConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1)
)
_PrmCfgInterface_ObjectIdentity = ObjectIdentity
prmCfgInterface = _PrmCfgInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 1)
)
_PrmCfgInterfacePort_ObjectIdentity = ObjectIdentity
prmCfgInterfacePort = _PrmCfgInterfacePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2)
)
_IfCfgPortTable_Object = MibTable
ifCfgPortTable = _IfCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ifCfgPortTable.setStatus("current")
_IfCfgPortEntry_Object = MibTableRow
ifCfgPortEntry = _IfCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 1, 1)
)
ifCfgPortEntry.setIndexNames(
    (0, "NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB", "ifCfgSlotIndex"),
    (0, "NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB", "ifCfgPortIndex"),
)
if mibBuilder.loadTexts:
    ifCfgPortEntry.setStatus("current")


class _IfCfgSlotIndex_Type(Integer32):
    """Custom type ifCfgSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_IfCfgSlotIndex_Type.__name__ = "Integer32"
_IfCfgSlotIndex_Object = MibTableColumn
ifCfgSlotIndex = _IfCfgSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 1, 1, 1),
    _IfCfgSlotIndex_Type()
)
ifCfgSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgSlotIndex.setStatus("current")


class _IfCfgPortIndex_Type(Integer32):
    """Custom type ifCfgPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IfCfgPortIndex_Type.__name__ = "Integer32"
_IfCfgPortIndex_Object = MibTableColumn
ifCfgPortIndex = _IfCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 1, 1, 2),
    _IfCfgPortIndex_Type()
)
ifCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgPortIndex.setStatus("current")


class _IfCfgPortCircuitID_Type(OctetString):
    """Custom type ifCfgPortCircuitID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IfCfgPortCircuitID_Type.__name__ = "OctetString"
_IfCfgPortCircuitID_Object = MibTableColumn
ifCfgPortCircuitID = _IfCfgPortCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 1, 1, 3),
    _IfCfgPortCircuitID_Type()
)
ifCfgPortCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortCircuitID.setStatus("current")
_IfCfgPortFltrIp1Start_Type = IpAddress
_IfCfgPortFltrIp1Start_Object = MibTableColumn
ifCfgPortFltrIp1Start = _IfCfgPortFltrIp1Start_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 1, 1, 4),
    _IfCfgPortFltrIp1Start_Type()
)
ifCfgPortFltrIp1Start.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortFltrIp1Start.setStatus("current")
_IfCfgPortFltrIp1End_Type = IpAddress
_IfCfgPortFltrIp1End_Object = MibTableColumn
ifCfgPortFltrIp1End = _IfCfgPortFltrIp1End_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 1, 1, 5),
    _IfCfgPortFltrIp1End_Type()
)
ifCfgPortFltrIp1End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortFltrIp1End.setStatus("current")
_IfCfgPortFltrIp2Start_Type = IpAddress
_IfCfgPortFltrIp2Start_Object = MibTableColumn
ifCfgPortFltrIp2Start = _IfCfgPortFltrIp2Start_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 1, 1, 6),
    _IfCfgPortFltrIp2Start_Type()
)
ifCfgPortFltrIp2Start.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortFltrIp2Start.setStatus("current")
_IfCfgPortFltrIp2End_Type = IpAddress
_IfCfgPortFltrIp2End_Object = MibTableColumn
ifCfgPortFltrIp2End = _IfCfgPortFltrIp2End_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 1, 1, 7),
    _IfCfgPortFltrIp2End_Type()
)
ifCfgPortFltrIp2End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortFltrIp2End.setStatus("current")


class _IfCfgPortBackboneVlan_Type(Integer32):
    """Custom type ifCfgPortBackboneVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4085),
    )


_IfCfgPortBackboneVlan_Type.__name__ = "Integer32"
_IfCfgPortBackboneVlan_Object = MibTableColumn
ifCfgPortBackboneVlan = _IfCfgPortBackboneVlan_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 1, 1, 8),
    _IfCfgPortBackboneVlan_Type()
)
ifCfgPortBackboneVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortBackboneVlan.setStatus("current")


class _IfCfgPortVlanPriority_Type(Integer32):
    """Custom type ifCfgPortVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IfCfgPortVlanPriority_Type.__name__ = "Integer32"
_IfCfgPortVlanPriority_Object = MibTableColumn
ifCfgPortVlanPriority = _IfCfgPortVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 1, 1, 9),
    _IfCfgPortVlanPriority_Type()
)
ifCfgPortVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortVlanPriority.setStatus("current")


class _IfCfgPortFloodMde_Type(Integer32):
    """Custom type ifCfgPortFloodMde based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uplFlood", 1),
          ("vlnFlood", 2))
    )


_IfCfgPortFloodMde_Type.__name__ = "Integer32"
_IfCfgPortFloodMde_Object = MibTableColumn
ifCfgPortFloodMde = _IfCfgPortFloodMde_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 1, 1, 10),
    _IfCfgPortFloodMde_Type()
)
ifCfgPortFloodMde.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortFloodMde.setStatus("current")


class _IfCfgPortIpFltProtocol_Type(Integer32):
    """Custom type ifCfgPortIpFltProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protocolALL", 1),
          ("protocolIP", 2))
    )


_IfCfgPortIpFltProtocol_Type.__name__ = "Integer32"
_IfCfgPortIpFltProtocol_Object = MibTableColumn
ifCfgPortIpFltProtocol = _IfCfgPortIpFltProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 1, 1, 11),
    _IfCfgPortIpFltProtocol_Type()
)
ifCfgPortIpFltProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortIpFltProtocol.setStatus("current")


class _IfCfgPortReset_Type(Integer32):
    """Custom type ifCfgPortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 2),
          ("reset", 1))
    )


_IfCfgPortReset_Type.__name__ = "Integer32"
_IfCfgPortReset_Object = MibTableColumn
ifCfgPortReset = _IfCfgPortReset_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 1, 1, 12),
    _IfCfgPortReset_Type()
)
ifCfgPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortReset.setStatus("current")


class _IfCfgPortBkBoneEthType_Type(Integer32):
    """Custom type ifCfgPortBkBoneEthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethtype8100", 1),
          ("ethtype9100", 2))
    )


_IfCfgPortBkBoneEthType_Type.__name__ = "Integer32"
_IfCfgPortBkBoneEthType_Object = MibTableColumn
ifCfgPortBkBoneEthType = _IfCfgPortBkBoneEthType_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 1, 1, 13),
    _IfCfgPortBkBoneEthType_Type()
)
ifCfgPortBkBoneEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortBkBoneEthType.setStatus("current")
_IfCfgPortVLANTable_Object = MibTable
ifCfgPortVLANTable = _IfCfgPortVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ifCfgPortVLANTable.setStatus("current")
_IfCfgPortVLANEntry_Object = MibTableRow
ifCfgPortVLANEntry = _IfCfgPortVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 2, 1)
)
ifCfgPortVLANEntry.setIndexNames(
    (0, "NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB", "ifCfgIfSlotIndex"),
    (0, "NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB", "ifCfgIfPortIndex"),
    (0, "NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB", "ifCfgVLANIndex"),
)
if mibBuilder.loadTexts:
    ifCfgPortVLANEntry.setStatus("current")


class _IfCfgIfSlotIndex_Type(Integer32):
    """Custom type ifCfgIfSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_IfCfgIfSlotIndex_Type.__name__ = "Integer32"
_IfCfgIfSlotIndex_Object = MibTableColumn
ifCfgIfSlotIndex = _IfCfgIfSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 2, 1, 1),
    _IfCfgIfSlotIndex_Type()
)
ifCfgIfSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgIfSlotIndex.setStatus("current")


class _IfCfgIfPortIndex_Type(Integer32):
    """Custom type ifCfgIfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IfCfgIfPortIndex_Type.__name__ = "Integer32"
_IfCfgIfPortIndex_Object = MibTableColumn
ifCfgIfPortIndex = _IfCfgIfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 2, 1, 2),
    _IfCfgIfPortIndex_Type()
)
ifCfgIfPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgIfPortIndex.setStatus("current")


class _IfCfgVLANIndex_Type(Integer32):
    """Custom type ifCfgVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IfCfgVLANIndex_Type.__name__ = "Integer32"
_IfCfgVLANIndex_Object = MibTableColumn
ifCfgVLANIndex = _IfCfgVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 2, 1, 3),
    _IfCfgVLANIndex_Type()
)
ifCfgVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgVLANIndex.setStatus("current")


class _IfCfgVLANIdStart_Type(Integer32):
    """Custom type ifCfgVLANIdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4085),
    )


_IfCfgVLANIdStart_Type.__name__ = "Integer32"
_IfCfgVLANIdStart_Object = MibTableColumn
ifCfgVLANIdStart = _IfCfgVLANIdStart_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 2, 1, 4),
    _IfCfgVLANIdStart_Type()
)
ifCfgVLANIdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgVLANIdStart.setStatus("current")


class _IfCfgVLANIdEnd_Type(Integer32):
    """Custom type ifCfgVLANIdEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4085),
    )


_IfCfgVLANIdEnd_Type.__name__ = "Integer32"
_IfCfgVLANIdEnd_Object = MibTableColumn
ifCfgVLANIdEnd = _IfCfgVLANIdEnd_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 2, 1, 5),
    _IfCfgVLANIdEnd_Type()
)
ifCfgVLANIdEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgVLANIdEnd.setStatus("current")
_IfCfgPortAdslTable_Object = MibTable
ifCfgPortAdslTable = _IfCfgPortAdslTable_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ifCfgPortAdslTable.setStatus("current")
_IfCfgPortAdslEntry_Object = MibTableRow
ifCfgPortAdslEntry = _IfCfgPortAdslEntry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1)
)
ifCfgPortAdslEntry.setIndexNames(
    (0, "NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB", "ifCfgAdslSlotIndex"),
    (0, "NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB", "ifCfgAdslPortIndex"),
)
if mibBuilder.loadTexts:
    ifCfgPortAdslEntry.setStatus("current")


class _IfCfgAdslSlotIndex_Type(Integer32):
    """Custom type ifCfgAdslSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_IfCfgAdslSlotIndex_Type.__name__ = "Integer32"
_IfCfgAdslSlotIndex_Object = MibTableColumn
ifCfgAdslSlotIndex = _IfCfgAdslSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 1),
    _IfCfgAdslSlotIndex_Type()
)
ifCfgAdslSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgAdslSlotIndex.setStatus("current")


class _IfCfgAdslPortIndex_Type(Integer32):
    """Custom type ifCfgAdslPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IfCfgAdslPortIndex_Type.__name__ = "Integer32"
_IfCfgAdslPortIndex_Object = MibTableColumn
ifCfgAdslPortIndex = _IfCfgAdslPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 2),
    _IfCfgAdslPortIndex_Type()
)
ifCfgAdslPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgAdslPortIndex.setStatus("current")


class _IfCfgPortAdslPortMode_Type(Integer32):
    """Custom type ifCfgPortAdslPortMode based on Integer32"""
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
        *(("adaptive", 3),
          ("fixedadaptive", 4),
          ("off", 2),
          ("on", 1))
    )


_IfCfgPortAdslPortMode_Type.__name__ = "Integer32"
_IfCfgPortAdslPortMode_Object = MibTableColumn
ifCfgPortAdslPortMode = _IfCfgPortAdslPortMode_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 3),
    _IfCfgPortAdslPortMode_Type()
)
ifCfgPortAdslPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortAdslPortMode.setStatus("current")


class _IfCfgPortAdslVpiVciDetect_Type(Integer32):
    """Custom type ifCfgPortAdslVpiVciDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_IfCfgPortAdslVpiVciDetect_Type.__name__ = "Integer32"
_IfCfgPortAdslVpiVciDetect_Object = MibTableColumn
ifCfgPortAdslVpiVciDetect = _IfCfgPortAdslVpiVciDetect_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 4),
    _IfCfgPortAdslVpiVciDetect_Type()
)
ifCfgPortAdslVpiVciDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortAdslVpiVciDetect.setStatus("current")


class _IfCfgPortAdslRxRate_Type(Integer32):
    """Custom type ifCfgPortAdslRxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IfCfgPortAdslRxRate_Type.__name__ = "Integer32"
_IfCfgPortAdslRxRate_Object = MibTableColumn
ifCfgPortAdslRxRate = _IfCfgPortAdslRxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 5),
    _IfCfgPortAdslRxRate_Type()
)
ifCfgPortAdslRxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortAdslRxRate.setStatus("current")
if mibBuilder.loadTexts:
    ifCfgPortAdslRxRate.setUnits("Kbps")


class _IfCfgPortAdslTxRate_Type(Integer32):
    """Custom type ifCfgPortAdslTxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 252),
    )


_IfCfgPortAdslTxRate_Type.__name__ = "Integer32"
_IfCfgPortAdslTxRate_Object = MibTableColumn
ifCfgPortAdslTxRate = _IfCfgPortAdslTxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 6),
    _IfCfgPortAdslTxRate_Type()
)
ifCfgPortAdslTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortAdslTxRate.setStatus("current")
if mibBuilder.loadTexts:
    ifCfgPortAdslTxRate.setUnits("Kbps")


class _IfCfgPortAdslFrameType_Type(Integer32):
    """Custom type ifCfgPortAdslFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frameType1483LLC", 1),
          ("frameType1483VCM", 2))
    )


_IfCfgPortAdslFrameType_Type.__name__ = "Integer32"
_IfCfgPortAdslFrameType_Object = MibTableColumn
ifCfgPortAdslFrameType = _IfCfgPortAdslFrameType_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 7),
    _IfCfgPortAdslFrameType_Type()
)
ifCfgPortAdslFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortAdslFrameType.setStatus("current")


class _IfCfgPortAdslVpi_Type(Integer32):
    """Custom type ifCfgPortAdslVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IfCfgPortAdslVpi_Type.__name__ = "Integer32"
_IfCfgPortAdslVpi_Object = MibTableColumn
ifCfgPortAdslVpi = _IfCfgPortAdslVpi_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 8),
    _IfCfgPortAdslVpi_Type()
)
ifCfgPortAdslVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortAdslVpi.setStatus("current")


class _IfCfgPortAdslVci_Type(Integer32):
    """Custom type ifCfgPortAdslVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IfCfgPortAdslVci_Type.__name__ = "Integer32"
_IfCfgPortAdslVci_Object = MibTableColumn
ifCfgPortAdslVci = _IfCfgPortAdslVci_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 9),
    _IfCfgPortAdslVci_Type()
)
ifCfgPortAdslVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortAdslVci.setStatus("current")


class _IfCfgPortAdslStandardMde_Type(Integer32):
    """Custom type ifCfgPortAdslStandardMde based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("aLCATEL", 5),
          ("gDMT", 3),
          ("gDMT-BIS", 6),
          ("gDMT-BIS-Annex-L", 8),
          ("gDMT-BIS-Annex-M", 9),
          ("gDMT-BISplus", 7),
          ("gLite", 2),
          ("multiMode", 4),
          ("stdMdeNoLink", 255),
          ("t1413", 1))
    )


_IfCfgPortAdslStandardMde_Type.__name__ = "Integer32"
_IfCfgPortAdslStandardMde_Object = MibTableColumn
ifCfgPortAdslStandardMde = _IfCfgPortAdslStandardMde_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 10),
    _IfCfgPortAdslStandardMde_Type()
)
ifCfgPortAdslStandardMde.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortAdslStandardMde.setStatus("current")


class _IfCfgPortAdslCorrectionUp_Type(Integer32):
    """Custom type ifCfgPortAdslCorrectionUp based on Integer32"""
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
        *(("corr125us", 1),
          ("corr1ms", 4),
          ("corr250us", 2),
          ("corr2ms", 5),
          ("corr4ms", 6),
          ("corr500us", 3))
    )


_IfCfgPortAdslCorrectionUp_Type.__name__ = "Integer32"
_IfCfgPortAdslCorrectionUp_Object = MibTableColumn
ifCfgPortAdslCorrectionUp = _IfCfgPortAdslCorrectionUp_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 11),
    _IfCfgPortAdslCorrectionUp_Type()
)
ifCfgPortAdslCorrectionUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortAdslCorrectionUp.setStatus("current")


class _IfCfgPortAdslCorrectionDn_Type(Integer32):
    """Custom type ifCfgPortAdslCorrectionDn based on Integer32"""
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
        *(("corr125us", 1),
          ("corr1ms", 4),
          ("corr250us", 2),
          ("corr2ms", 5),
          ("corr4ms", 6),
          ("corr500us", 3))
    )


_IfCfgPortAdslCorrectionDn_Type.__name__ = "Integer32"
_IfCfgPortAdslCorrectionDn_Object = MibTableColumn
ifCfgPortAdslCorrectionDn = _IfCfgPortAdslCorrectionDn_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 12),
    _IfCfgPortAdslCorrectionDn_Type()
)
ifCfgPortAdslCorrectionDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortAdslCorrectionDn.setStatus("current")


class _IfCfgPortAdslDelayUp_Type(Integer32):
    """Custom type ifCfgPortAdslDelayUp based on Integer32"""
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
        *(("delay16ms", 5),
          ("delay1ms", 1),
          ("delay2ms", 2),
          ("delay32ms", 6),
          ("delay4ms", 3),
          ("delay64ms", 7),
          ("delay8ms", 4))
    )


_IfCfgPortAdslDelayUp_Type.__name__ = "Integer32"
_IfCfgPortAdslDelayUp_Object = MibTableColumn
ifCfgPortAdslDelayUp = _IfCfgPortAdslDelayUp_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 13),
    _IfCfgPortAdslDelayUp_Type()
)
ifCfgPortAdslDelayUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortAdslDelayUp.setStatus("current")


class _IfCfgPortAdslDelayDn_Type(Integer32):
    """Custom type ifCfgPortAdslDelayDn based on Integer32"""
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
        *(("delay16ms", 5),
          ("delay1ms", 1),
          ("delay2ms", 2),
          ("delay32ms", 6),
          ("delay4ms", 3),
          ("delay64ms", 7),
          ("delay8ms", 4))
    )


_IfCfgPortAdslDelayDn_Type.__name__ = "Integer32"
_IfCfgPortAdslDelayDn_Object = MibTableColumn
ifCfgPortAdslDelayDn = _IfCfgPortAdslDelayDn_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 14),
    _IfCfgPortAdslDelayDn_Type()
)
ifCfgPortAdslDelayDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortAdslDelayDn.setStatus("current")


class _IfCfgPortAdslEcFdm_Type(Integer32):
    """Custom type ifCfgPortAdslEcFdm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ec", 1),
          ("fdm", 2))
    )


_IfCfgPortAdslEcFdm_Type.__name__ = "Integer32"
_IfCfgPortAdslEcFdm_Object = MibTableColumn
ifCfgPortAdslEcFdm = _IfCfgPortAdslEcFdm_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 15),
    _IfCfgPortAdslEcFdm_Type()
)
ifCfgPortAdslEcFdm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortAdslEcFdm.setStatus("current")


class _IfCfgPortAdslFastBuffer_Type(Integer32):
    """Custom type ifCfgPortAdslFastBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_IfCfgPortAdslFastBuffer_Type.__name__ = "Integer32"
_IfCfgPortAdslFastBuffer_Object = MibTableColumn
ifCfgPortAdslFastBuffer = _IfCfgPortAdslFastBuffer_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 16),
    _IfCfgPortAdslFastBuffer_Type()
)
ifCfgPortAdslFastBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortAdslFastBuffer.setStatus("current")


class _IfCfgPortAdslSnrUp_Type(Integer32):
    """Custom type ifCfgPortAdslSnrUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_IfCfgPortAdslSnrUp_Type.__name__ = "Integer32"
_IfCfgPortAdslSnrUp_Object = MibTableColumn
ifCfgPortAdslSnrUp = _IfCfgPortAdslSnrUp_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 17),
    _IfCfgPortAdslSnrUp_Type()
)
ifCfgPortAdslSnrUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortAdslSnrUp.setStatus("current")


class _IfCfgPortAdslSnrDn_Type(Integer32):
    """Custom type ifCfgPortAdslSnrDn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_IfCfgPortAdslSnrDn_Type.__name__ = "Integer32"
_IfCfgPortAdslSnrDn_Object = MibTableColumn
ifCfgPortAdslSnrDn = _IfCfgPortAdslSnrDn_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 18),
    _IfCfgPortAdslSnrDn_Type()
)
ifCfgPortAdslSnrDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortAdslSnrDn.setStatus("current")


class _IfCfgPortAdslActualRxRate_Type(Integer32):
    """Custom type ifCfgPortAdslActualRxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_IfCfgPortAdslActualRxRate_Type.__name__ = "Integer32"
_IfCfgPortAdslActualRxRate_Object = MibTableColumn
ifCfgPortAdslActualRxRate = _IfCfgPortAdslActualRxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 19),
    _IfCfgPortAdslActualRxRate_Type()
)
ifCfgPortAdslActualRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgPortAdslActualRxRate.setStatus("current")
if mibBuilder.loadTexts:
    ifCfgPortAdslActualRxRate.setUnits("Kbps")


class _IfCfgPortAdslActualTxRate_Type(Integer32):
    """Custom type ifCfgPortAdslActualTxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_IfCfgPortAdslActualTxRate_Type.__name__ = "Integer32"
_IfCfgPortAdslActualTxRate_Object = MibTableColumn
ifCfgPortAdslActualTxRate = _IfCfgPortAdslActualTxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 20),
    _IfCfgPortAdslActualTxRate_Type()
)
ifCfgPortAdslActualTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgPortAdslActualTxRate.setStatus("current")
if mibBuilder.loadTexts:
    ifCfgPortAdslActualTxRate.setUnits("Kbps")


class _IfCfgPortAdslActualStandardMde_Type(Integer32):
    """Custom type ifCfgPortAdslActualStandardMde based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("aLCATEL", 5),
          ("gDMT", 3),
          ("gDMT-BIS", 6),
          ("gDMT-BIS-Annex-L", 8),
          ("gDMT-BIS-Annex-M", 9),
          ("gDMT-BISplus", 7),
          ("gLite", 2),
          ("multiMode", 4),
          ("stdMdeNoLink", 255),
          ("t1413", 1))
    )


_IfCfgPortAdslActualStandardMde_Type.__name__ = "Integer32"
_IfCfgPortAdslActualStandardMde_Object = MibTableColumn
ifCfgPortAdslActualStandardMde = _IfCfgPortAdslActualStandardMde_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 21),
    _IfCfgPortAdslActualStandardMde_Type()
)
ifCfgPortAdslActualStandardMde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgPortAdslActualStandardMde.setStatus("current")


class _IfCfgPortAdslActualDepthUp_Type(Integer32):
    """Custom type ifCfgPortAdslActualDepthUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_IfCfgPortAdslActualDepthUp_Type.__name__ = "Integer32"
_IfCfgPortAdslActualDepthUp_Object = MibTableColumn
ifCfgPortAdslActualDepthUp = _IfCfgPortAdslActualDepthUp_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 22),
    _IfCfgPortAdslActualDepthUp_Type()
)
ifCfgPortAdslActualDepthUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgPortAdslActualDepthUp.setStatus("current")


class _IfCfgPortAdslActualDepthDn_Type(Integer32):
    """Custom type ifCfgPortAdslActualDepthDn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_IfCfgPortAdslActualDepthDn_Type.__name__ = "Integer32"
_IfCfgPortAdslActualDepthDn_Object = MibTableColumn
ifCfgPortAdslActualDepthDn = _IfCfgPortAdslActualDepthDn_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 3, 1, 23),
    _IfCfgPortAdslActualDepthDn_Type()
)
ifCfgPortAdslActualDepthDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgPortAdslActualDepthDn.setStatus("current")
_IfCfgPortIdslTable_Object = MibTable
ifCfgPortIdslTable = _IfCfgPortIdslTable_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ifCfgPortIdslTable.setStatus("current")
_IfCfgPortIdslEntry_Object = MibTableRow
ifCfgPortIdslEntry = _IfCfgPortIdslEntry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 4, 1)
)
ifCfgPortIdslEntry.setIndexNames(
    (0, "NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB", "ifCfgIdslSlotIndex"),
    (0, "NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB", "ifCfgIdslPortIndex"),
)
if mibBuilder.loadTexts:
    ifCfgPortIdslEntry.setStatus("current")


class _IfCfgIdslSlotIndex_Type(Integer32):
    """Custom type ifCfgIdslSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_IfCfgIdslSlotIndex_Type.__name__ = "Integer32"
_IfCfgIdslSlotIndex_Object = MibTableColumn
ifCfgIdslSlotIndex = _IfCfgIdslSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 4, 1, 1),
    _IfCfgIdslSlotIndex_Type()
)
ifCfgIdslSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgIdslSlotIndex.setStatus("current")


class _IfCfgIdslPortIndex_Type(Integer32):
    """Custom type ifCfgIdslPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IfCfgIdslPortIndex_Type.__name__ = "Integer32"
_IfCfgIdslPortIndex_Object = MibTableColumn
ifCfgIdslPortIndex = _IfCfgIdslPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 4, 1, 2),
    _IfCfgIdslPortIndex_Type()
)
ifCfgIdslPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgIdslPortIndex.setStatus("current")


class _IfCfgPortIdslRxTxRate_Type(Integer32):
    """Custom type ifCfgPortIdslRxTxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("idslRxTxRate128", 1),
          ("idslRxTxRate144", 2),
          ("idslRxTxRateDefect", 0),
          ("idslRxTxRateOff", 255))
    )


_IfCfgPortIdslRxTxRate_Type.__name__ = "Integer32"
_IfCfgPortIdslRxTxRate_Object = MibTableColumn
ifCfgPortIdslRxTxRate = _IfCfgPortIdslRxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 4, 1, 3),
    _IfCfgPortIdslRxTxRate_Type()
)
ifCfgPortIdslRxTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortIdslRxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    ifCfgPortIdslRxTxRate.setUnits("Kbps")
_IfCfgPortSdslTable_Object = MibTable
ifCfgPortSdslTable = _IfCfgPortSdslTable_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ifCfgPortSdslTable.setStatus("current")
_IfCfgPortSdslEntry_Object = MibTableRow
ifCfgPortSdslEntry = _IfCfgPortSdslEntry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 5, 1)
)
ifCfgPortSdslEntry.setIndexNames(
    (0, "NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB", "ifCfgSdslSlotIndex"),
    (0, "NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB", "ifCfgSdslPortIndex"),
)
if mibBuilder.loadTexts:
    ifCfgPortSdslEntry.setStatus("current")


class _IfCfgSdslSlotIndex_Type(Integer32):
    """Custom type ifCfgSdslSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_IfCfgSdslSlotIndex_Type.__name__ = "Integer32"
_IfCfgSdslSlotIndex_Object = MibTableColumn
ifCfgSdslSlotIndex = _IfCfgSdslSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 5, 1, 1),
    _IfCfgSdslSlotIndex_Type()
)
ifCfgSdslSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgSdslSlotIndex.setStatus("current")


class _IfCfgSdslPortIndex_Type(Integer32):
    """Custom type ifCfgSdslPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IfCfgSdslPortIndex_Type.__name__ = "Integer32"
_IfCfgSdslPortIndex_Object = MibTableColumn
ifCfgSdslPortIndex = _IfCfgSdslPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 5, 1, 2),
    _IfCfgSdslPortIndex_Type()
)
ifCfgSdslPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgSdslPortIndex.setStatus("current")


class _IfCfgPortSdslRxTxRate_Type(Integer32):
    """Custom type ifCfgPortSdslRxTxRate based on Integer32"""
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
              7,
              8,
              9,
              10,
              255)
        )
    )
    namedValues = NamedValues(
        *(("sdslRxTxRate1040", 6),
          ("sdslRxTxRate1168", 7),
          ("sdslRxTxRate144", 1),
          ("sdslRxTxRate1552", 8),
          ("sdslRxTxRate2064", 9),
          ("sdslRxTxRate2320", 10),
          ("sdslRxTxRate272", 2),
          ("sdslRxTxRate400", 3),
          ("sdslRxTxRate528", 4),
          ("sdslRxTxRate784", 5),
          ("sdslRxTxRateDefect", 0),
          ("sdslRxTxRateOff", 255))
    )


_IfCfgPortSdslRxTxRate_Type.__name__ = "Integer32"
_IfCfgPortSdslRxTxRate_Object = MibTableColumn
ifCfgPortSdslRxTxRate = _IfCfgPortSdslRxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 5, 1, 3),
    _IfCfgPortSdslRxTxRate_Type()
)
ifCfgPortSdslRxTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortSdslRxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    ifCfgPortSdslRxTxRate.setUnits("Kbps")


class _IfCfgPortSdslLineCode_Type(Integer32):
    """Custom type ifCfgPortSdslLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lineCode2B1Q", 2),
          ("lineCodeCap", 1),
          ("lineCodeGSHDSL", 3))
    )


_IfCfgPortSdslLineCode_Type.__name__ = "Integer32"
_IfCfgPortSdslLineCode_Object = MibTableColumn
ifCfgPortSdslLineCode = _IfCfgPortSdslLineCode_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 5, 1, 4),
    _IfCfgPortSdslLineCode_Type()
)
ifCfgPortSdslLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortSdslLineCode.setStatus("current")
_IfCfgPortT1Table_Object = MibTable
ifCfgPortT1Table = _IfCfgPortT1Table_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    ifCfgPortT1Table.setStatus("current")
_IfCfgPortT1Entry_Object = MibTableRow
ifCfgPortT1Entry = _IfCfgPortT1Entry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 6, 1)
)
ifCfgPortT1Entry.setIndexNames(
    (0, "NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB", "ifCfgT1SlotIndex"),
    (0, "NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB", "ifCfgT1PortIndex"),
)
if mibBuilder.loadTexts:
    ifCfgPortT1Entry.setStatus("current")


class _IfCfgT1SlotIndex_Type(Integer32):
    """Custom type ifCfgT1SlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_IfCfgT1SlotIndex_Type.__name__ = "Integer32"
_IfCfgT1SlotIndex_Object = MibTableColumn
ifCfgT1SlotIndex = _IfCfgT1SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 6, 1, 1),
    _IfCfgT1SlotIndex_Type()
)
ifCfgT1SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgT1SlotIndex.setStatus("current")


class _IfCfgT1PortIndex_Type(Integer32):
    """Custom type ifCfgT1PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IfCfgT1PortIndex_Type.__name__ = "Integer32"
_IfCfgT1PortIndex_Object = MibTableColumn
ifCfgT1PortIndex = _IfCfgT1PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 6, 1, 2),
    _IfCfgT1PortIndex_Type()
)
ifCfgT1PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgT1PortIndex.setStatus("current")


class _IfCfgPortT1RxTxRate_Type(Integer32):
    """Custom type ifCfgPortT1RxTxRate based on Integer32"""
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
              7,
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("t1RxTxRate1152", 6),
          ("t1RxTxRate1344", 7),
          ("t1RxTxRate1536", 8),
          ("t1RxTxRate192", 1),
          ("t1RxTxRate384", 2),
          ("t1RxTxRate576", 3),
          ("t1RxTxRate768", 4),
          ("t1RxTxRate960", 5),
          ("t1RxTxRateDefect", 0),
          ("t1RxTxRateOff", 255))
    )


_IfCfgPortT1RxTxRate_Type.__name__ = "Integer32"
_IfCfgPortT1RxTxRate_Object = MibTableColumn
ifCfgPortT1RxTxRate = _IfCfgPortT1RxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 6, 1, 3),
    _IfCfgPortT1RxTxRate_Type()
)
ifCfgPortT1RxTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortT1RxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    ifCfgPortT1RxTxRate.setUnits("Kbps")


class _IfCfgPortT1FrameType_Type(Integer32):
    """Custom type ifCfgPortT1FrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t1frameTypeESF", 1),
          ("t1frameTypeSFD4", 2))
    )


_IfCfgPortT1FrameType_Type.__name__ = "Integer32"
_IfCfgPortT1FrameType_Object = MibTableColumn
ifCfgPortT1FrameType = _IfCfgPortT1FrameType_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 6, 1, 4),
    _IfCfgPortT1FrameType_Type()
)
ifCfgPortT1FrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortT1FrameType.setStatus("current")


class _IfCfgPortT1LineCode_Type(Integer32):
    """Custom type ifCfgPortT1LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t1lineCodeAMI", 2),
          ("t1lineCodeB8ZS", 1))
    )


_IfCfgPortT1LineCode_Type.__name__ = "Integer32"
_IfCfgPortT1LineCode_Object = MibTableColumn
ifCfgPortT1LineCode = _IfCfgPortT1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 6, 1, 5),
    _IfCfgPortT1LineCode_Type()
)
ifCfgPortT1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortT1LineCode.setStatus("current")


class _IfCfgPortT1TxBuildOut_Type(Integer32):
    """Custom type ifCfgPortT1TxBuildOut based on Integer32"""
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
        *(("t1TxBuildOut0db", 1),
          ("t1TxBuildOutN15db", 3),
          ("t1TxBuildOutN22db", 4),
          ("t1TxBuildOutN7p5db", 2))
    )


_IfCfgPortT1TxBuildOut_Type.__name__ = "Integer32"
_IfCfgPortT1TxBuildOut_Object = MibTableColumn
ifCfgPortT1TxBuildOut = _IfCfgPortT1TxBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 6, 1, 6),
    _IfCfgPortT1TxBuildOut_Type()
)
ifCfgPortT1TxBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortT1TxBuildOut.setStatus("current")


class _IfCfgPortT1ClockSrc_Type(Integer32):
    """Custom type ifCfgPortT1ClockSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t1ClockSrcLocal", 1),
          ("t1ClockSrcLoop", 2))
    )


_IfCfgPortT1ClockSrc_Type.__name__ = "Integer32"
_IfCfgPortT1ClockSrc_Object = MibTableColumn
ifCfgPortT1ClockSrc = _IfCfgPortT1ClockSrc_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 6, 1, 7),
    _IfCfgPortT1ClockSrc_Type()
)
ifCfgPortT1ClockSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortT1ClockSrc.setStatus("current")
_IfCfgPortE1Table_Object = MibTable
ifCfgPortE1Table = _IfCfgPortE1Table_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    ifCfgPortE1Table.setStatus("current")
_IfCfgPortE1Entry_Object = MibTableRow
ifCfgPortE1Entry = _IfCfgPortE1Entry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 7, 1)
)
ifCfgPortE1Entry.setIndexNames(
    (0, "NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB", "ifCfgE1SlotIndex"),
    (0, "NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB", "ifCfgE1PortIndex"),
)
if mibBuilder.loadTexts:
    ifCfgPortE1Entry.setStatus("current")


class _IfCfgE1SlotIndex_Type(Integer32):
    """Custom type ifCfgE1SlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_IfCfgE1SlotIndex_Type.__name__ = "Integer32"
_IfCfgE1SlotIndex_Object = MibTableColumn
ifCfgE1SlotIndex = _IfCfgE1SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 7, 1, 1),
    _IfCfgE1SlotIndex_Type()
)
ifCfgE1SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgE1SlotIndex.setStatus("current")


class _IfCfgE1PortIndex_Type(Integer32):
    """Custom type ifCfgE1PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IfCfgE1PortIndex_Type.__name__ = "Integer32"
_IfCfgE1PortIndex_Object = MibTableColumn
ifCfgE1PortIndex = _IfCfgE1PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 7, 1, 2),
    _IfCfgE1PortIndex_Type()
)
ifCfgE1PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCfgE1PortIndex.setStatus("current")


class _IfCfgPortE1RxTxRate_Type(Integer32):
    """Custom type ifCfgPortE1RxTxRate based on Integer32"""
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
              7,
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("e1RxTxRate1024", 4),
          ("e1RxTxRate1280", 5),
          ("e1RxTxRate1536", 6),
          ("e1RxTxRate1792", 7),
          ("e1RxTxRate1984", 8),
          ("e1RxTxRate256", 1),
          ("e1RxTxRate512", 2),
          ("e1RxTxRate768", 3),
          ("e1RxTxRateDefect", 0),
          ("e1RxTxRateOff", 255))
    )


_IfCfgPortE1RxTxRate_Type.__name__ = "Integer32"
_IfCfgPortE1RxTxRate_Object = MibTableColumn
ifCfgPortE1RxTxRate = _IfCfgPortE1RxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 7, 1, 3),
    _IfCfgPortE1RxTxRate_Type()
)
ifCfgPortE1RxTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortE1RxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    ifCfgPortE1RxTxRate.setUnits("Kbps")


class _IfCfgPortE1FrameType_Type(Integer32):
    """Custom type ifCfgPortE1FrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1frameTypeCRC", 1),
          ("e1frameTypeNoCRC", 2))
    )


_IfCfgPortE1FrameType_Type.__name__ = "Integer32"
_IfCfgPortE1FrameType_Object = MibTableColumn
ifCfgPortE1FrameType = _IfCfgPortE1FrameType_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 7, 1, 4),
    _IfCfgPortE1FrameType_Type()
)
ifCfgPortE1FrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortE1FrameType.setStatus("current")


class _IfCfgPortE1LineCode_Type(Integer32):
    """Custom type ifCfgPortE1LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1lineCodeAMI", 2),
          ("e1lineCodeHDB3", 1))
    )


_IfCfgPortE1LineCode_Type.__name__ = "Integer32"
_IfCfgPortE1LineCode_Object = MibTableColumn
ifCfgPortE1LineCode = _IfCfgPortE1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 7, 1, 5),
    _IfCfgPortE1LineCode_Type()
)
ifCfgPortE1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortE1LineCode.setStatus("current")


class _IfCfgPortE1ClockSrc_Type(Integer32):
    """Custom type ifCfgPortE1ClockSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1ClockSrcLocal", 1),
          ("e1ClockSrcLoop", 2))
    )


_IfCfgPortE1ClockSrc_Type.__name__ = "Integer32"
_IfCfgPortE1ClockSrc_Object = MibTableColumn
ifCfgPortE1ClockSrc = _IfCfgPortE1ClockSrc_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1, 1, 1, 2, 7, 1, 6),
    _IfCfgPortE1ClockSrc_Type()
)
ifCfgPortE1ClockSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCfgPortE1ClockSrc.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB",
    **{"ntntechInterfaceModuleConfigurationMIB": ntntechInterfaceModuleConfigurationMIB,
       "ifModCfgMIBObjects": ifModCfgMIBObjects,
       "ifModCfgParameterConfiguration": ifModCfgParameterConfiguration,
       "prmCfgInterface": prmCfgInterface,
       "prmCfgInterfacePort": prmCfgInterfacePort,
       "ifCfgPortTable": ifCfgPortTable,
       "ifCfgPortEntry": ifCfgPortEntry,
       "ifCfgSlotIndex": ifCfgSlotIndex,
       "ifCfgPortIndex": ifCfgPortIndex,
       "ifCfgPortCircuitID": ifCfgPortCircuitID,
       "ifCfgPortFltrIp1Start": ifCfgPortFltrIp1Start,
       "ifCfgPortFltrIp1End": ifCfgPortFltrIp1End,
       "ifCfgPortFltrIp2Start": ifCfgPortFltrIp2Start,
       "ifCfgPortFltrIp2End": ifCfgPortFltrIp2End,
       "ifCfgPortBackboneVlan": ifCfgPortBackboneVlan,
       "ifCfgPortVlanPriority": ifCfgPortVlanPriority,
       "ifCfgPortFloodMde": ifCfgPortFloodMde,
       "ifCfgPortIpFltProtocol": ifCfgPortIpFltProtocol,
       "ifCfgPortReset": ifCfgPortReset,
       "ifCfgPortBkBoneEthType": ifCfgPortBkBoneEthType,
       "ifCfgPortVLANTable": ifCfgPortVLANTable,
       "ifCfgPortVLANEntry": ifCfgPortVLANEntry,
       "ifCfgIfSlotIndex": ifCfgIfSlotIndex,
       "ifCfgIfPortIndex": ifCfgIfPortIndex,
       "ifCfgVLANIndex": ifCfgVLANIndex,
       "ifCfgVLANIdStart": ifCfgVLANIdStart,
       "ifCfgVLANIdEnd": ifCfgVLANIdEnd,
       "ifCfgPortAdslTable": ifCfgPortAdslTable,
       "ifCfgPortAdslEntry": ifCfgPortAdslEntry,
       "ifCfgAdslSlotIndex": ifCfgAdslSlotIndex,
       "ifCfgAdslPortIndex": ifCfgAdslPortIndex,
       "ifCfgPortAdslPortMode": ifCfgPortAdslPortMode,
       "ifCfgPortAdslVpiVciDetect": ifCfgPortAdslVpiVciDetect,
       "ifCfgPortAdslRxRate": ifCfgPortAdslRxRate,
       "ifCfgPortAdslTxRate": ifCfgPortAdslTxRate,
       "ifCfgPortAdslFrameType": ifCfgPortAdslFrameType,
       "ifCfgPortAdslVpi": ifCfgPortAdslVpi,
       "ifCfgPortAdslVci": ifCfgPortAdslVci,
       "ifCfgPortAdslStandardMde": ifCfgPortAdslStandardMde,
       "ifCfgPortAdslCorrectionUp": ifCfgPortAdslCorrectionUp,
       "ifCfgPortAdslCorrectionDn": ifCfgPortAdslCorrectionDn,
       "ifCfgPortAdslDelayUp": ifCfgPortAdslDelayUp,
       "ifCfgPortAdslDelayDn": ifCfgPortAdslDelayDn,
       "ifCfgPortAdslEcFdm": ifCfgPortAdslEcFdm,
       "ifCfgPortAdslFastBuffer": ifCfgPortAdslFastBuffer,
       "ifCfgPortAdslSnrUp": ifCfgPortAdslSnrUp,
       "ifCfgPortAdslSnrDn": ifCfgPortAdslSnrDn,
       "ifCfgPortAdslActualRxRate": ifCfgPortAdslActualRxRate,
       "ifCfgPortAdslActualTxRate": ifCfgPortAdslActualTxRate,
       "ifCfgPortAdslActualStandardMde": ifCfgPortAdslActualStandardMde,
       "ifCfgPortAdslActualDepthUp": ifCfgPortAdslActualDepthUp,
       "ifCfgPortAdslActualDepthDn": ifCfgPortAdslActualDepthDn,
       "ifCfgPortIdslTable": ifCfgPortIdslTable,
       "ifCfgPortIdslEntry": ifCfgPortIdslEntry,
       "ifCfgIdslSlotIndex": ifCfgIdslSlotIndex,
       "ifCfgIdslPortIndex": ifCfgIdslPortIndex,
       "ifCfgPortIdslRxTxRate": ifCfgPortIdslRxTxRate,
       "ifCfgPortSdslTable": ifCfgPortSdslTable,
       "ifCfgPortSdslEntry": ifCfgPortSdslEntry,
       "ifCfgSdslSlotIndex": ifCfgSdslSlotIndex,
       "ifCfgSdslPortIndex": ifCfgSdslPortIndex,
       "ifCfgPortSdslRxTxRate": ifCfgPortSdslRxTxRate,
       "ifCfgPortSdslLineCode": ifCfgPortSdslLineCode,
       "ifCfgPortT1Table": ifCfgPortT1Table,
       "ifCfgPortT1Entry": ifCfgPortT1Entry,
       "ifCfgT1SlotIndex": ifCfgT1SlotIndex,
       "ifCfgT1PortIndex": ifCfgT1PortIndex,
       "ifCfgPortT1RxTxRate": ifCfgPortT1RxTxRate,
       "ifCfgPortT1FrameType": ifCfgPortT1FrameType,
       "ifCfgPortT1LineCode": ifCfgPortT1LineCode,
       "ifCfgPortT1TxBuildOut": ifCfgPortT1TxBuildOut,
       "ifCfgPortT1ClockSrc": ifCfgPortT1ClockSrc,
       "ifCfgPortE1Table": ifCfgPortE1Table,
       "ifCfgPortE1Entry": ifCfgPortE1Entry,
       "ifCfgE1SlotIndex": ifCfgE1SlotIndex,
       "ifCfgE1PortIndex": ifCfgE1PortIndex,
       "ifCfgPortE1RxTxRate": ifCfgPortE1RxTxRate,
       "ifCfgPortE1FrameType": ifCfgPortE1FrameType,
       "ifCfgPortE1LineCode": ifCfgPortE1LineCode,
       "ifCfgPortE1ClockSrc": ifCfgPortE1ClockSrc}
)
