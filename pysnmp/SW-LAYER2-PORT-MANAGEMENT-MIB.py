# SNMP MIB module (SW-LAYER2-PORT-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW-LAYER2-PORT-MANAGEMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:52 2024
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
 NotificationType,
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
    "NotificationType",
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

_Marconi_ObjectIdentity = ObjectIdentity
marconi = _Marconi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2)
)
_External_ObjectIdentity = ObjectIdentity
external = _External_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20)
)
_Dlink_ObjectIdentity = ObjectIdentity
dlink = _Dlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1)
)
_Dlinkcommon_ObjectIdentity = ObjectIdentity
dlinkcommon = _Dlinkcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 1)
)
_Golf_ObjectIdentity = ObjectIdentity
golf = _Golf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2)
)
_Golfproducts_ObjectIdentity = ObjectIdentity
golfproducts = _Golfproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1)
)
_Es2000_ObjectIdentity = ObjectIdentity
es2000 = _Es2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3)
)
_Golfcommon_ObjectIdentity = ObjectIdentity
golfcommon = _Golfcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2)
)
_Marconi_products_ObjectIdentity = ObjectIdentity
marconi_products = _Marconi_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1)
)
_Marconi_es2000Prod_ObjectIdentity = ObjectIdentity
marconi_es2000Prod = _Marconi_es2000Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 28)
)
_SwProperty_ObjectIdentity = ObjectIdentity
swProperty = _SwProperty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 28, 1)
)
_Marconi_mgmt_ObjectIdentity = ObjectIdentity
marconi_mgmt = _Marconi_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2)
)
_Es2000Mgmt_ObjectIdentity = ObjectIdentity
es2000Mgmt = _Es2000Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28)
)
_SwL2Mgmt_ObjectIdentity = ObjectIdentity
swL2Mgmt = _SwL2Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2)
)
_SwL2PortMgmt_ObjectIdentity = ObjectIdentity
swL2PortMgmt = _SwL2PortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4)
)
_SwL2PortInfoTable_Object = MibTable
swL2PortInfoTable = _SwL2PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1)
)
if mibBuilder.loadTexts:
    swL2PortInfoTable.setStatus("mandatory")
_SwL2PortInfoEntry_Object = MibTableRow
swL2PortInfoEntry = _SwL2PortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1, 1)
)
swL2PortInfoEntry.setIndexNames(
    (0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoUnitIndex"),
    (0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoModuleIndex"),
    (0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoIndex"),
)
if mibBuilder.loadTexts:
    swL2PortInfoEntry.setStatus("mandatory")
_SwL2PortInfoUnitIndex_Type = Integer32
_SwL2PortInfoUnitIndex_Object = MibTableColumn
swL2PortInfoUnitIndex = _SwL2PortInfoUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1, 1, 1),
    _SwL2PortInfoUnitIndex_Type()
)
swL2PortInfoUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoUnitIndex.setStatus("mandatory")
_SwL2PortInfoModuleIndex_Type = Integer32
_SwL2PortInfoModuleIndex_Object = MibTableColumn
swL2PortInfoModuleIndex = _SwL2PortInfoModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1, 1, 2),
    _SwL2PortInfoModuleIndex_Type()
)
swL2PortInfoModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoModuleIndex.setStatus("mandatory")
_SwL2PortInfoIndex_Type = Integer32
_SwL2PortInfoIndex_Object = MibTableColumn
swL2PortInfoIndex = _SwL2PortInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1, 1, 3),
    _SwL2PortInfoIndex_Type()
)
swL2PortInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoIndex.setStatus("mandatory")


class _SwL2PortInfoType_Type(Integer32):
    """Custom type swL2PortInfoType based on Integer32"""
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
        *(("other", 7),
          ("portType-100FX", 2),
          ("portType-100TX", 1),
          ("portType-GIGA-MTRJLX", 4),
          ("portType-GIGA-MTRJSX", 3),
          ("portType-GIGA-SCLX", 6),
          ("portType-GIGA-SCSX", 5))
    )


_SwL2PortInfoType_Type.__name__ = "Integer32"
_SwL2PortInfoType_Object = MibTableColumn
swL2PortInfoType = _SwL2PortInfoType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1, 1, 4),
    _SwL2PortInfoType_Type()
)
swL2PortInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoType.setStatus("mandatory")


class _SwL2PortInfoDescr_Type(DisplayString):
    """Custom type swL2PortInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwL2PortInfoDescr_Type.__name__ = "DisplayString"
_SwL2PortInfoDescr_Object = MibTableColumn
swL2PortInfoDescr = _SwL2PortInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1, 1, 5),
    _SwL2PortInfoDescr_Type()
)
swL2PortInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoDescr.setStatus("mandatory")


class _SwL2PortInfoLinkStatus_Type(Integer32):
    """Custom type swL2PortInfoLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("link-fail", 3),
          ("link-pass", 2),
          ("other", 1))
    )


_SwL2PortInfoLinkStatus_Type.__name__ = "Integer32"
_SwL2PortInfoLinkStatus_Object = MibTableColumn
swL2PortInfoLinkStatus = _SwL2PortInfoLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1, 1, 6),
    _SwL2PortInfoLinkStatus_Type()
)
swL2PortInfoLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoLinkStatus.setStatus("mandatory")


class _SwL2PortInfoNwayStatus_Type(Integer32):
    """Custom type swL2PortInfoNwayStatus based on Integer32"""
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
        *(("full-100Mbps", 5),
          ("full-10Mbps", 3),
          ("full-1Gigabps", 7),
          ("half-100Mbps", 4),
          ("half-10Mbps", 2),
          ("half-1Gigabps", 6),
          ("other", 1))
    )


_SwL2PortInfoNwayStatus_Type.__name__ = "Integer32"
_SwL2PortInfoNwayStatus_Object = MibTableColumn
swL2PortInfoNwayStatus = _SwL2PortInfoNwayStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1, 1, 7),
    _SwL2PortInfoNwayStatus_Type()
)
swL2PortInfoNwayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoNwayStatus.setStatus("mandatory")
_SwL2PortCtrlTable_Object = MibTable
swL2PortCtrlTable = _SwL2PortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2)
)
if mibBuilder.loadTexts:
    swL2PortCtrlTable.setStatus("mandatory")
_SwL2PortCtrlEntry_Object = MibTableRow
swL2PortCtrlEntry = _SwL2PortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1)
)
swL2PortCtrlEntry.setIndexNames(
    (0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortCtrlUnitIndex"),
    (0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortCtrlModuleIndex"),
    (0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortCtrlIndex"),
)
if mibBuilder.loadTexts:
    swL2PortCtrlEntry.setStatus("mandatory")
_SwL2PortCtrlUnitIndex_Type = Integer32
_SwL2PortCtrlUnitIndex_Object = MibTableColumn
swL2PortCtrlUnitIndex = _SwL2PortCtrlUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 1),
    _SwL2PortCtrlUnitIndex_Type()
)
swL2PortCtrlUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlUnitIndex.setStatus("mandatory")
_SwL2PortCtrlModuleIndex_Type = Integer32
_SwL2PortCtrlModuleIndex_Object = MibTableColumn
swL2PortCtrlModuleIndex = _SwL2PortCtrlModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 2),
    _SwL2PortCtrlModuleIndex_Type()
)
swL2PortCtrlModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlModuleIndex.setStatus("mandatory")
_SwL2PortCtrlIndex_Type = Integer32
_SwL2PortCtrlIndex_Object = MibTableColumn
swL2PortCtrlIndex = _SwL2PortCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 3),
    _SwL2PortCtrlIndex_Type()
)
swL2PortCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlIndex.setStatus("mandatory")


class _SwL2PortCtrlAdminState_Type(Integer32):
    """Custom type swL2PortCtrlAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2PortCtrlAdminState_Type.__name__ = "Integer32"
_SwL2PortCtrlAdminState_Object = MibTableColumn
swL2PortCtrlAdminState = _SwL2PortCtrlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 4),
    _SwL2PortCtrlAdminState_Type()
)
swL2PortCtrlAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlAdminState.setStatus("mandatory")


class _SwL2PortCtrlLinkStatusAlarmState_Type(Integer32):
    """Custom type swL2PortCtrlLinkStatusAlarmState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2PortCtrlLinkStatusAlarmState_Type.__name__ = "Integer32"
_SwL2PortCtrlLinkStatusAlarmState_Object = MibTableColumn
swL2PortCtrlLinkStatusAlarmState = _SwL2PortCtrlLinkStatusAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 5),
    _SwL2PortCtrlLinkStatusAlarmState_Type()
)
swL2PortCtrlLinkStatusAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlLinkStatusAlarmState.setStatus("mandatory")


class _SwL2PortCtrlNwayState_Type(Integer32):
    """Custom type swL2PortCtrlNwayState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 10),
          ("nway-disabled-100Mbps-Full", 6),
          ("nway-disabled-100Mbps-Half", 5),
          ("nway-disabled-10Mbps-Full", 4),
          ("nway-disabled-10Mbps-Half", 3),
          ("nway-disabled-1Gigabps-Full", 8),
          ("nway-disabled-1Gigabps-Half", 7),
          ("nway-enabled", 2),
          ("other", 1))
    )


_SwL2PortCtrlNwayState_Type.__name__ = "Integer32"
_SwL2PortCtrlNwayState_Object = MibTableColumn
swL2PortCtrlNwayState = _SwL2PortCtrlNwayState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 6),
    _SwL2PortCtrlNwayState_Type()
)
swL2PortCtrlNwayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlNwayState.setStatus("mandatory")


class _SwL2PortCtrlFlowCtrlState_Type(Integer32):
    """Custom type swL2PortCtrlFlowCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2PortCtrlFlowCtrlState_Type.__name__ = "Integer32"
_SwL2PortCtrlFlowCtrlState_Object = MibTableColumn
swL2PortCtrlFlowCtrlState = _SwL2PortCtrlFlowCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 7),
    _SwL2PortCtrlFlowCtrlState_Type()
)
swL2PortCtrlFlowCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlFlowCtrlState.setStatus("mandatory")


class _SwL2PortCtrlBackPressState_Type(Integer32):
    """Custom type swL2PortCtrlBackPressState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2PortCtrlBackPressState_Type.__name__ = "Integer32"
_SwL2PortCtrlBackPressState_Object = MibTableColumn
swL2PortCtrlBackPressState = _SwL2PortCtrlBackPressState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 8),
    _SwL2PortCtrlBackPressState_Type()
)
swL2PortCtrlBackPressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlBackPressState.setStatus("mandatory")


class _SwL2PortCtrlLockState_Type(Integer32):
    """Custom type swL2PortCtrlLockState based on Integer32"""
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
        *(("disable", 2),
          ("enable", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2PortCtrlLockState_Type.__name__ = "Integer32"
_SwL2PortCtrlLockState_Object = MibTableColumn
swL2PortCtrlLockState = _SwL2PortCtrlLockState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 9),
    _SwL2PortCtrlLockState_Type()
)
swL2PortCtrlLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlLockState.setStatus("mandatory")


class _SwL2PortCtrlPriority_Type(Integer32):
    """Custom type swL2PortCtrlPriority based on Integer32"""
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
        *(("default", 2),
          ("force-high-priority", 4),
          ("force-low-priority", 3),
          ("notAvailable", 5),
          ("other", 1))
    )


_SwL2PortCtrlPriority_Type.__name__ = "Integer32"
_SwL2PortCtrlPriority_Object = MibTableColumn
swL2PortCtrlPriority = _SwL2PortCtrlPriority_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 10),
    _SwL2PortCtrlPriority_Type()
)
swL2PortCtrlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlPriority.setStatus("mandatory")


class _SwL2PortCtrlStpState_Type(Integer32):
    """Custom type swL2PortCtrlStpState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2PortCtrlStpState_Type.__name__ = "Integer32"
_SwL2PortCtrlStpState_Object = MibTableColumn
swL2PortCtrlStpState = _SwL2PortCtrlStpState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 11),
    _SwL2PortCtrlStpState_Type()
)
swL2PortCtrlStpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlStpState.setStatus("mandatory")


class _SwL2PortCtrlHOLState_Type(Integer32):
    """Custom type swL2PortCtrlHOLState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2PortCtrlHOLState_Type.__name__ = "Integer32"
_SwL2PortCtrlHOLState_Object = MibTableColumn
swL2PortCtrlHOLState = _SwL2PortCtrlHOLState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 12),
    _SwL2PortCtrlHOLState_Type()
)
swL2PortCtrlHOLState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlHOLState.setStatus("mandatory")


class _SwL2PortCtrlBcastRisingAct_Type(Integer32):
    """Custom type swL2PortCtrlBcastRisingAct based on Integer32"""
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
        *(("blocking", 3),
          ("blocking-trap", 4),
          ("do-nothing", 2),
          ("notAvailable", 5),
          ("other", 1))
    )


_SwL2PortCtrlBcastRisingAct_Type.__name__ = "Integer32"
_SwL2PortCtrlBcastRisingAct_Object = MibTableColumn
swL2PortCtrlBcastRisingAct = _SwL2PortCtrlBcastRisingAct_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 13),
    _SwL2PortCtrlBcastRisingAct_Type()
)
swL2PortCtrlBcastRisingAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlBcastRisingAct.setStatus("mandatory")


class _SwL2PortCtrlBcastFallingAct_Type(Integer32):
    """Custom type swL2PortCtrlBcastFallingAct based on Integer32"""
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
        *(("do-nothing", 2),
          ("forwarding", 3),
          ("forwarding-trap", 4),
          ("notAvailable", 5),
          ("other", 1))
    )


_SwL2PortCtrlBcastFallingAct_Type.__name__ = "Integer32"
_SwL2PortCtrlBcastFallingAct_Object = MibTableColumn
swL2PortCtrlBcastFallingAct = _SwL2PortCtrlBcastFallingAct_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 14),
    _SwL2PortCtrlBcastFallingAct_Type()
)
swL2PortCtrlBcastFallingAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlBcastFallingAct.setStatus("mandatory")
_SwL2PortCtrlClearCounter_Type = Integer32
_SwL2PortCtrlClearCounter_Object = MibScalar
swL2PortCtrlClearCounter = _SwL2PortCtrlClearCounter_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 15),
    _SwL2PortCtrlClearCounter_Type()
)
swL2PortCtrlClearCounter.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    swL2PortCtrlClearCounter.setStatus("mandatory")
_SwL2PortStTable_Object = MibTable
swL2PortStTable = _SwL2PortStTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3)
)
if mibBuilder.loadTexts:
    swL2PortStTable.setStatus("mandatory")
_SwL2PortStEntry_Object = MibTableRow
swL2PortStEntry = _SwL2PortStEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1)
)
swL2PortStEntry.setIndexNames(
    (0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortStUnitIndex"),
    (0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortStModuleIndex"),
    (0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortStIndex"),
)
if mibBuilder.loadTexts:
    swL2PortStEntry.setStatus("mandatory")
_SwL2PortStUnitIndex_Type = Integer32
_SwL2PortStUnitIndex_Object = MibTableColumn
swL2PortStUnitIndex = _SwL2PortStUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 1),
    _SwL2PortStUnitIndex_Type()
)
swL2PortStUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStUnitIndex.setStatus("mandatory")
_SwL2PortStModuleIndex_Type = Integer32
_SwL2PortStModuleIndex_Object = MibTableColumn
swL2PortStModuleIndex = _SwL2PortStModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 2),
    _SwL2PortStModuleIndex_Type()
)
swL2PortStModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStModuleIndex.setStatus("mandatory")
_SwL2PortStIndex_Type = Integer32
_SwL2PortStIndex_Object = MibTableColumn
swL2PortStIndex = _SwL2PortStIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 3),
    _SwL2PortStIndex_Type()
)
swL2PortStIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStIndex.setStatus("mandatory")
_SwL2PortStByteRx_Type = Counter32
_SwL2PortStByteRx_Object = MibTableColumn
swL2PortStByteRx = _SwL2PortStByteRx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 4),
    _SwL2PortStByteRx_Type()
)
swL2PortStByteRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStByteRx.setStatus("mandatory")
_SwL2PortStByteTx_Type = Counter32
_SwL2PortStByteTx_Object = MibTableColumn
swL2PortStByteTx = _SwL2PortStByteTx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 5),
    _SwL2PortStByteTx_Type()
)
swL2PortStByteTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStByteTx.setStatus("mandatory")
_SwL2PortStFrameRx_Type = Counter32
_SwL2PortStFrameRx_Object = MibTableColumn
swL2PortStFrameRx = _SwL2PortStFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 6),
    _SwL2PortStFrameRx_Type()
)
swL2PortStFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFrameRx.setStatus("mandatory")
_SwL2PortStFrameTx_Type = Counter32
_SwL2PortStFrameTx_Object = MibTableColumn
swL2PortStFrameTx = _SwL2PortStFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 7),
    _SwL2PortStFrameTx_Type()
)
swL2PortStFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFrameTx.setStatus("mandatory")
_SwL2PortStTotalBytesRx_Type = Counter32
_SwL2PortStTotalBytesRx_Object = MibTableColumn
swL2PortStTotalBytesRx = _SwL2PortStTotalBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 8),
    _SwL2PortStTotalBytesRx_Type()
)
swL2PortStTotalBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStTotalBytesRx.setStatus("mandatory")
_SwL2PortStTotalFramesRx_Type = Counter32
_SwL2PortStTotalFramesRx_Object = MibTableColumn
swL2PortStTotalFramesRx = _SwL2PortStTotalFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 9),
    _SwL2PortStTotalFramesRx_Type()
)
swL2PortStTotalFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStTotalFramesRx.setStatus("mandatory")
_SwL2PortStBroadcastFramesRx_Type = Counter32
_SwL2PortStBroadcastFramesRx_Object = MibTableColumn
swL2PortStBroadcastFramesRx = _SwL2PortStBroadcastFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 10),
    _SwL2PortStBroadcastFramesRx_Type()
)
swL2PortStBroadcastFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStBroadcastFramesRx.setStatus("mandatory")
_SwL2PortStMulticastFramesRx_Type = Counter32
_SwL2PortStMulticastFramesRx_Object = MibTableColumn
swL2PortStMulticastFramesRx = _SwL2PortStMulticastFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 11),
    _SwL2PortStMulticastFramesRx_Type()
)
swL2PortStMulticastFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStMulticastFramesRx.setStatus("mandatory")
_SwL2PortStCRCError_Type = Counter32
_SwL2PortStCRCError_Object = MibTableColumn
swL2PortStCRCError = _SwL2PortStCRCError_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 12),
    _SwL2PortStCRCError_Type()
)
swL2PortStCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStCRCError.setStatus("mandatory")
_SwL2PortStOversizeFrames_Type = Counter32
_SwL2PortStOversizeFrames_Object = MibTableColumn
swL2PortStOversizeFrames = _SwL2PortStOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 13),
    _SwL2PortStOversizeFrames_Type()
)
swL2PortStOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStOversizeFrames.setStatus("mandatory")
_SwL2PortStFragments_Type = Counter32
_SwL2PortStFragments_Object = MibTableColumn
swL2PortStFragments = _SwL2PortStFragments_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 14),
    _SwL2PortStFragments_Type()
)
swL2PortStFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFragments.setStatus("mandatory")
_SwL2PortStJabber_Type = Counter32
_SwL2PortStJabber_Object = MibTableColumn
swL2PortStJabber = _SwL2PortStJabber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 15),
    _SwL2PortStJabber_Type()
)
swL2PortStJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStJabber.setStatus("mandatory")
_SwL2PortStCollision_Type = Counter32
_SwL2PortStCollision_Object = MibTableColumn
swL2PortStCollision = _SwL2PortStCollision_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 16),
    _SwL2PortStCollision_Type()
)
swL2PortStCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStCollision.setStatus("mandatory")
_SwL2PortStLateCollision_Type = Counter32
_SwL2PortStLateCollision_Object = MibTableColumn
swL2PortStLateCollision = _SwL2PortStLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 17),
    _SwL2PortStLateCollision_Type()
)
swL2PortStLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStLateCollision.setStatus("mandatory")
_SwL2PortStFrames_64_bytes_Type = Counter32
_SwL2PortStFrames_64_bytes_Object = MibScalar
swL2PortStFrames_64_bytes = _SwL2PortStFrames_64_bytes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 18),
    _SwL2PortStFrames_64_bytes_Type()
)
swL2PortStFrames_64_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFrames_64_bytes.setStatus("mandatory")
_SwL2PortStFrames_65_127_bytes_Type = Counter32
_SwL2PortStFrames_65_127_bytes_Object = MibScalar
swL2PortStFrames_65_127_bytes = _SwL2PortStFrames_65_127_bytes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 19),
    _SwL2PortStFrames_65_127_bytes_Type()
)
swL2PortStFrames_65_127_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFrames_65_127_bytes.setStatus("mandatory")
_SwL2PortStFrames_128_255_bytes_Type = Counter32
_SwL2PortStFrames_128_255_bytes_Object = MibScalar
swL2PortStFrames_128_255_bytes = _SwL2PortStFrames_128_255_bytes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 20),
    _SwL2PortStFrames_128_255_bytes_Type()
)
swL2PortStFrames_128_255_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFrames_128_255_bytes.setStatus("mandatory")
_SwL2PortStFrames_256_511_bytes_Type = Counter32
_SwL2PortStFrames_256_511_bytes_Object = MibScalar
swL2PortStFrames_256_511_bytes = _SwL2PortStFrames_256_511_bytes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 21),
    _SwL2PortStFrames_256_511_bytes_Type()
)
swL2PortStFrames_256_511_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFrames_256_511_bytes.setStatus("mandatory")
_SwL2PortStFrames_512_1023_bytes_Type = Counter32
_SwL2PortStFrames_512_1023_bytes_Object = MibScalar
swL2PortStFrames_512_1023_bytes = _SwL2PortStFrames_512_1023_bytes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 22),
    _SwL2PortStFrames_512_1023_bytes_Type()
)
swL2PortStFrames_512_1023_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFrames_512_1023_bytes.setStatus("mandatory")
_SwL2PortStFrames_1024_1536_bytes_Type = Counter32
_SwL2PortStFrames_1024_1536_bytes_Object = MibScalar
swL2PortStFrames_1024_1536_bytes = _SwL2PortStFrames_1024_1536_bytes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 23),
    _SwL2PortStFrames_1024_1536_bytes_Type()
)
swL2PortStFrames_1024_1536_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFrames_1024_1536_bytes.setStatus("mandatory")
_SwL2PortStFramesDroppedFrames_Type = Counter32
_SwL2PortStFramesDroppedFrames_Object = MibTableColumn
swL2PortStFramesDroppedFrames = _SwL2PortStFramesDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 24),
    _SwL2PortStFramesDroppedFrames_Type()
)
swL2PortStFramesDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFramesDroppedFrames.setStatus("mandatory")
_SwL2PortStMulticastFramesTx_Type = Counter32
_SwL2PortStMulticastFramesTx_Object = MibTableColumn
swL2PortStMulticastFramesTx = _SwL2PortStMulticastFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 25),
    _SwL2PortStMulticastFramesTx_Type()
)
swL2PortStMulticastFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStMulticastFramesTx.setStatus("mandatory")
_SwL2PortStBroadcastFramesTx_Type = Counter32
_SwL2PortStBroadcastFramesTx_Object = MibTableColumn
swL2PortStBroadcastFramesTx = _SwL2PortStBroadcastFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 26),
    _SwL2PortStBroadcastFramesTx_Type()
)
swL2PortStBroadcastFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStBroadcastFramesTx.setStatus("mandatory")
_SwL2PortStUndersizeFrames_Type = Counter32
_SwL2PortStUndersizeFrames_Object = MibTableColumn
swL2PortStUndersizeFrames = _SwL2PortStUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 27),
    _SwL2PortStUndersizeFrames_Type()
)
swL2PortStUndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStUndersizeFrames.setStatus("mandatory")

# Managed Objects groups


# Notification objects

swEventPortPartition = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3, 0, 1)
)
swEventPortPartition.setObjects(
      *(("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoUnitIndex"),
        ("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoModuleIndex"),
        ("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoIndex"))
)
if mibBuilder.loadTexts:
    swEventPortPartition.setStatus(
        ""
    )

swEventlinkChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3, 0, 2)
)
swEventlinkChangeEvent.setObjects(
      *(("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoUnitIndex"),
        ("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoModuleIndex"),
        ("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoIndex"))
)
if mibBuilder.loadTexts:
    swEventlinkChangeEvent.setStatus(
        ""
    )

swEventBcastRisingStorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3, 0, 3)
)
swEventBcastRisingStorm.setObjects(
      *(("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoUnitIndex"),
        ("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoModuleIndex"),
        ("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoIndex"))
)
if mibBuilder.loadTexts:
    swEventBcastRisingStorm.setStatus(
        ""
    )

swEventBcastFallingStorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3, 0, 4)
)
swEventBcastFallingStorm.setObjects(
      *(("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoUnitIndex"),
        ("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoModuleIndex"),
        ("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoIndex"))
)
if mibBuilder.loadTexts:
    swEventBcastFallingStorm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW-LAYER2-PORT-MANAGEMENT-MIB",
    **{"marconi": marconi,
       "systems": systems,
       "external": external,
       "dlink": dlink,
       "dlinkcommon": dlinkcommon,
       "golf": golf,
       "golfproducts": golfproducts,
       "es2000": es2000,
       "swEventPortPartition": swEventPortPartition,
       "swEventlinkChangeEvent": swEventlinkChangeEvent,
       "swEventBcastRisingStorm": swEventBcastRisingStorm,
       "swEventBcastFallingStorm": swEventBcastFallingStorm,
       "golfcommon": golfcommon,
       "marconi-products": marconi_products,
       "marconi-es2000Prod": marconi_es2000Prod,
       "swProperty": swProperty,
       "marconi-mgmt": marconi_mgmt,
       "es2000Mgmt": es2000Mgmt,
       "swL2Mgmt": swL2Mgmt,
       "swL2PortMgmt": swL2PortMgmt,
       "swL2PortInfoTable": swL2PortInfoTable,
       "swL2PortInfoEntry": swL2PortInfoEntry,
       "swL2PortInfoUnitIndex": swL2PortInfoUnitIndex,
       "swL2PortInfoModuleIndex": swL2PortInfoModuleIndex,
       "swL2PortInfoIndex": swL2PortInfoIndex,
       "swL2PortInfoType": swL2PortInfoType,
       "swL2PortInfoDescr": swL2PortInfoDescr,
       "swL2PortInfoLinkStatus": swL2PortInfoLinkStatus,
       "swL2PortInfoNwayStatus": swL2PortInfoNwayStatus,
       "swL2PortCtrlTable": swL2PortCtrlTable,
       "swL2PortCtrlEntry": swL2PortCtrlEntry,
       "swL2PortCtrlUnitIndex": swL2PortCtrlUnitIndex,
       "swL2PortCtrlModuleIndex": swL2PortCtrlModuleIndex,
       "swL2PortCtrlIndex": swL2PortCtrlIndex,
       "swL2PortCtrlAdminState": swL2PortCtrlAdminState,
       "swL2PortCtrlLinkStatusAlarmState": swL2PortCtrlLinkStatusAlarmState,
       "swL2PortCtrlNwayState": swL2PortCtrlNwayState,
       "swL2PortCtrlFlowCtrlState": swL2PortCtrlFlowCtrlState,
       "swL2PortCtrlBackPressState": swL2PortCtrlBackPressState,
       "swL2PortCtrlLockState": swL2PortCtrlLockState,
       "swL2PortCtrlPriority": swL2PortCtrlPriority,
       "swL2PortCtrlStpState": swL2PortCtrlStpState,
       "swL2PortCtrlHOLState": swL2PortCtrlHOLState,
       "swL2PortCtrlBcastRisingAct": swL2PortCtrlBcastRisingAct,
       "swL2PortCtrlBcastFallingAct": swL2PortCtrlBcastFallingAct,
       "swL2PortCtrlClearCounter": swL2PortCtrlClearCounter,
       "swL2PortStTable": swL2PortStTable,
       "swL2PortStEntry": swL2PortStEntry,
       "swL2PortStUnitIndex": swL2PortStUnitIndex,
       "swL2PortStModuleIndex": swL2PortStModuleIndex,
       "swL2PortStIndex": swL2PortStIndex,
       "swL2PortStByteRx": swL2PortStByteRx,
       "swL2PortStByteTx": swL2PortStByteTx,
       "swL2PortStFrameRx": swL2PortStFrameRx,
       "swL2PortStFrameTx": swL2PortStFrameTx,
       "swL2PortStTotalBytesRx": swL2PortStTotalBytesRx,
       "swL2PortStTotalFramesRx": swL2PortStTotalFramesRx,
       "swL2PortStBroadcastFramesRx": swL2PortStBroadcastFramesRx,
       "swL2PortStMulticastFramesRx": swL2PortStMulticastFramesRx,
       "swL2PortStCRCError": swL2PortStCRCError,
       "swL2PortStOversizeFrames": swL2PortStOversizeFrames,
       "swL2PortStFragments": swL2PortStFragments,
       "swL2PortStJabber": swL2PortStJabber,
       "swL2PortStCollision": swL2PortStCollision,
       "swL2PortStLateCollision": swL2PortStLateCollision,
       "swL2PortStFrames-64-bytes": swL2PortStFrames_64_bytes,
       "swL2PortStFrames-65-127-bytes": swL2PortStFrames_65_127_bytes,
       "swL2PortStFrames-128-255-bytes": swL2PortStFrames_128_255_bytes,
       "swL2PortStFrames-256-511-bytes": swL2PortStFrames_256_511_bytes,
       "swL2PortStFrames-512-1023-bytes": swL2PortStFrames_512_1023_bytes,
       "swL2PortStFrames-1024-1536-bytes": swL2PortStFrames_1024_1536_bytes,
       "swL2PortStFramesDroppedFrames": swL2PortStFramesDroppedFrames,
       "swL2PortStMulticastFramesTx": swL2PortStMulticastFramesTx,
       "swL2PortStBroadcastFramesTx": swL2PortStBroadcastFramesTx,
       "swL2PortStUndersizeFrames": swL2PortStUndersizeFrames}
)
