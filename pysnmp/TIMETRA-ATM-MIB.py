# SNMP MIB module (TIMETRA-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:54 2024
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

(aal5VccEntry,
 atmInterfaceConfEntry,
 atmInterfaceConfVccs,
 atmInterfaceConfVpcs,
 atmInterfaceCurrentMaxVciBits,
 atmInterfaceCurrentMaxVpiBits,
 atmInterfaceDs3PlcpAlarmState,
 atmInterfaceMaxActiveVciBits,
 atmInterfaceMaxActiveVpiBits,
 atmInterfaceTCAlarmState,
 atmInterfaceTCEntry,
 atmVclEntry,
 atmVclVci,
 atmVclVpi,
 atmVplEntry,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "aal5VccEntry",
    "atmInterfaceConfEntry",
    "atmInterfaceConfVccs",
    "atmInterfaceConfVpcs",
    "atmInterfaceCurrentMaxVciBits",
    "atmInterfaceCurrentMaxVpiBits",
    "atmInterfaceDs3PlcpAlarmState",
    "atmInterfaceMaxActiveVciBits",
    "atmInterfaceMaxActiveVpiBits",
    "atmInterfaceTCAlarmState",
    "atmInterfaceTCEntry",
    "atmVclEntry",
    "atmVclVci",
    "atmVclVpi",
    "atmVplEntry",
    "atmVplVpi")

(AtmConnCastType,
 AtmConnKind,
 AtmTrafficDescrParamIndex,
 AtmVcIdentifier,
 AtmVorXAdminStatus,
 AtmVorXLastChange,
 AtmVorXOperStatus,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmConnCastType",
    "AtmConnKind",
    "AtmTrafficDescrParamIndex",
    "AtmVcIdentifier",
    "AtmVorXAdminStatus",
    "AtmVorXLastChange",
    "AtmVorXOperStatus",
    "AtmVpIdentifier")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(tmnxCardSlotNum,
 tmnxChassisIndex,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxCardSlotNum",
    "tmnxChassisIndex",
    "tmnxMDASlotNum")

(tmnxConnProfId,) = mibBuilder.importSymbols(
    "TIMETRA-CONN-PROF-MIB",
    "tmnxConnProfId")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")


# MODULE-IDENTITY

timetraATMMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 27)
)
timetraATMMIBModule.setRevisions(
        ("1911-02-01 00:00",
         "1909-02-28 00:00",
         "1906-03-16 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1903-10-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AtmConnectionOwner(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ilmi", 2),
          ("sap", 1))
    )



class AtmOamStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("eteAis", 2),
          ("eteAisLoc", 4),
          ("eteRdi", 3),
          ("up", 1))
    )



class AtmIlmiStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("undefined", 0),
          ("vpiOrVciRangeConflict", 2))
    )



class AtmLlid(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class AtmIlmiLinkUniType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("public", 1),
          ("undefined", 0))
    )



class AtmIlmiLinkDeviceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("node", 2),
          ("undefined", 0),
          ("user", 1))
    )



class AtmIlmiLinkVersion(Integer32, TextualConvention):
    status = "current"
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
        *(("undefined", 0),
          ("version3point0", 3),
          ("version3point1", 1),
          ("version4point0", 2))
    )



class AtmIlmiLinkImeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("networkside", 2),
          ("userside", 1))
    )



# MIB Managed Objects in the order of their OIDs

_TAtmMIBConformance_ObjectIdentity = ObjectIdentity
tAtmMIBConformance = _TAtmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27)
)
_TmnxAtmMIBCompliances_ObjectIdentity = ObjectIdentity
tmnxAtmMIBCompliances = _TmnxAtmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 1)
)
_TmnxAtmMIBGroups_ObjectIdentity = ObjectIdentity
tmnxAtmMIBGroups = _TmnxAtmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2)
)
_TAtmObjs_ObjectIdentity = ObjectIdentity
tAtmObjs = _TAtmObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27)
)
_TAtmMdaObjs_ObjectIdentity = ObjectIdentity
tAtmMdaObjs = _TAtmMdaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 1)
)
_TAtmMdaInfoTable_Object = MibTable
tAtmMdaInfoTable = _TAtmMdaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 1, 1)
)
if mibBuilder.loadTexts:
    tAtmMdaInfoTable.setStatus("obsolete")
_TAtmMdaInfoEntry_Object = MibTableRow
tAtmMdaInfoEntry = _TAtmMdaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 1, 1, 1)
)
tAtmMdaInfoEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tAtmMdaInfoEntry.setStatus("obsolete")
_TAtmMdaMaxSupportedVpcs_Type = Integer32
_TAtmMdaMaxSupportedVpcs_Object = MibTableColumn
tAtmMdaMaxSupportedVpcs = _TAtmMdaMaxSupportedVpcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 1, 1, 1, 1),
    _TAtmMdaMaxSupportedVpcs_Type()
)
tAtmMdaMaxSupportedVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmMdaMaxSupportedVpcs.setStatus("obsolete")
_TAtmMdaMaxSupportedVccs_Type = Integer32
_TAtmMdaMaxSupportedVccs_Object = MibTableColumn
tAtmMdaMaxSupportedVccs = _TAtmMdaMaxSupportedVccs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 1, 1, 1, 2),
    _TAtmMdaMaxSupportedVccs_Type()
)
tAtmMdaMaxSupportedVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmMdaMaxSupportedVccs.setStatus("obsolete")
_TAtmMdaConfiguredVpcs_Type = Integer32
_TAtmMdaConfiguredVpcs_Object = MibTableColumn
tAtmMdaConfiguredVpcs = _TAtmMdaConfiguredVpcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 1, 1, 1, 3),
    _TAtmMdaConfiguredVpcs_Type()
)
tAtmMdaConfiguredVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmMdaConfiguredVpcs.setStatus("obsolete")
_TAtmMdaConfiguredVccs_Type = Integer32
_TAtmMdaConfiguredVccs_Object = MibTableColumn
tAtmMdaConfiguredVccs = _TAtmMdaConfiguredVccs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 1, 1, 1, 4),
    _TAtmMdaConfiguredVccs_Type()
)
tAtmMdaConfiguredVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmMdaConfiguredVccs.setStatus("obsolete")
_TAtmIntfObjs_ObjectIdentity = ObjectIdentity
tAtmIntfObjs = _TAtmIntfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2)
)
_TAtmIntfConfTable_Object = MibTable
tAtmIntfConfTable = _TAtmIntfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1)
)
if mibBuilder.loadTexts:
    tAtmIntfConfTable.setStatus("current")
_TAtmIntfConfEntry_Object = MibTableRow
tAtmIntfConfEntry = _TAtmIntfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tAtmIntfConfEntry.setStatus("current")


class _TAtmIntfCurrentMaxVpcs_Type(Integer32):
    """Custom type tAtmIntfCurrentMaxVpcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_TAtmIntfCurrentMaxVpcs_Type.__name__ = "Integer32"
_TAtmIntfCurrentMaxVpcs_Object = MibTableColumn
tAtmIntfCurrentMaxVpcs = _TAtmIntfCurrentMaxVpcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1, 1),
    _TAtmIntfCurrentMaxVpcs_Type()
)
tAtmIntfCurrentMaxVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfCurrentMaxVpcs.setStatus("current")


class _TAtmIntfCurrentMaxVccs_Type(Integer32):
    """Custom type tAtmIntfCurrentMaxVccs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_TAtmIntfCurrentMaxVccs_Type.__name__ = "Integer32"
_TAtmIntfCurrentMaxVccs_Object = MibTableColumn
tAtmIntfCurrentMaxVccs = _TAtmIntfCurrentMaxVccs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1, 2),
    _TAtmIntfCurrentMaxVccs_Type()
)
tAtmIntfCurrentMaxVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfCurrentMaxVccs.setStatus("current")
_TAtmIntfTotalIngrCbrBandwidth_Type = Unsigned32
_TAtmIntfTotalIngrCbrBandwidth_Object = MibTableColumn
tAtmIntfTotalIngrCbrBandwidth = _TAtmIntfTotalIngrCbrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1, 3),
    _TAtmIntfTotalIngrCbrBandwidth_Type()
)
tAtmIntfTotalIngrCbrBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfTotalIngrCbrBandwidth.setStatus("current")
_TAtmIntfTotalIngrRtVbrBandwidth_Type = Unsigned32
_TAtmIntfTotalIngrRtVbrBandwidth_Object = MibTableColumn
tAtmIntfTotalIngrRtVbrBandwidth = _TAtmIntfTotalIngrRtVbrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1, 4),
    _TAtmIntfTotalIngrRtVbrBandwidth_Type()
)
tAtmIntfTotalIngrRtVbrBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfTotalIngrRtVbrBandwidth.setStatus("current")
_TAtmIntfTotalIngrNrtVbrBandwidth_Type = Unsigned32
_TAtmIntfTotalIngrNrtVbrBandwidth_Object = MibTableColumn
tAtmIntfTotalIngrNrtVbrBandwidth = _TAtmIntfTotalIngrNrtVbrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1, 5),
    _TAtmIntfTotalIngrNrtVbrBandwidth_Type()
)
tAtmIntfTotalIngrNrtVbrBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfTotalIngrNrtVbrBandwidth.setStatus("current")
_TAtmIntfTotalIngrUbrBandwidth_Type = Unsigned32
_TAtmIntfTotalIngrUbrBandwidth_Object = MibTableColumn
tAtmIntfTotalIngrUbrBandwidth = _TAtmIntfTotalIngrUbrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1, 6),
    _TAtmIntfTotalIngrUbrBandwidth_Type()
)
tAtmIntfTotalIngrUbrBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfTotalIngrUbrBandwidth.setStatus("current")
_TAtmIntfTotalEgrCbrBandwidth_Type = Unsigned32
_TAtmIntfTotalEgrCbrBandwidth_Object = MibTableColumn
tAtmIntfTotalEgrCbrBandwidth = _TAtmIntfTotalEgrCbrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1, 7),
    _TAtmIntfTotalEgrCbrBandwidth_Type()
)
tAtmIntfTotalEgrCbrBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfTotalEgrCbrBandwidth.setStatus("current")
_TAtmIntfTotalEgrRtVbrBandwidth_Type = Unsigned32
_TAtmIntfTotalEgrRtVbrBandwidth_Object = MibTableColumn
tAtmIntfTotalEgrRtVbrBandwidth = _TAtmIntfTotalEgrRtVbrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1, 8),
    _TAtmIntfTotalEgrRtVbrBandwidth_Type()
)
tAtmIntfTotalEgrRtVbrBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfTotalEgrRtVbrBandwidth.setStatus("current")
_TAtmIntfTotalEgrNrtVbrBandwidth_Type = Unsigned32
_TAtmIntfTotalEgrNrtVbrBandwidth_Object = MibTableColumn
tAtmIntfTotalEgrNrtVbrBandwidth = _TAtmIntfTotalEgrNrtVbrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1, 9),
    _TAtmIntfTotalEgrNrtVbrBandwidth_Type()
)
tAtmIntfTotalEgrNrtVbrBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfTotalEgrNrtVbrBandwidth.setStatus("current")
_TAtmIntfTotalEgrUbrBandwidth_Type = Unsigned32
_TAtmIntfTotalEgrUbrBandwidth_Object = MibTableColumn
tAtmIntfTotalEgrUbrBandwidth = _TAtmIntfTotalEgrUbrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1, 10),
    _TAtmIntfTotalEgrUbrBandwidth_Type()
)
tAtmIntfTotalEgrUbrBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfTotalEgrUbrBandwidth.setStatus("current")
_TAtmIntfBandwidth_Type = Unsigned32
_TAtmIntfBandwidth_Object = MibTableColumn
tAtmIntfBandwidth = _TAtmIntfBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1, 11),
    _TAtmIntfBandwidth_Type()
)
tAtmIntfBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfBandwidth.setStatus("current")
_TAtmIntfShapedBandwidth_Type = Unsigned32
_TAtmIntfShapedBandwidth_Object = MibTableColumn
tAtmIntfShapedBandwidth = _TAtmIntfShapedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1, 12),
    _TAtmIntfShapedBandwidth_Type()
)
tAtmIntfShapedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfShapedBandwidth.setStatus("current")
_TAtmIntfLastUnknVpi_Type = AtmVpIdentifier
_TAtmIntfLastUnknVpi_Object = MibTableColumn
tAtmIntfLastUnknVpi = _TAtmIntfLastUnknVpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1, 13),
    _TAtmIntfLastUnknVpi_Type()
)
tAtmIntfLastUnknVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfLastUnknVpi.setStatus("current")
_TAtmIntfLastUnknVci_Type = AtmVcIdentifier
_TAtmIntfLastUnknVci_Object = MibTableColumn
tAtmIntfLastUnknVci = _TAtmIntfLastUnknVci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1, 14),
    _TAtmIntfLastUnknVci_Type()
)
tAtmIntfLastUnknVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfLastUnknVci.setStatus("current")


class _TAtmIntfOperStatus_Type(Integer32):
    """Custom type tAtmIntfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowerLayerDown", 2),
          ("up", 1))
    )


_TAtmIntfOperStatus_Type.__name__ = "Integer32"
_TAtmIntfOperStatus_Object = MibTableColumn
tAtmIntfOperStatus = _TAtmIntfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1, 15),
    _TAtmIntfOperStatus_Type()
)
tAtmIntfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfOperStatus.setStatus("current")


class _TAtmIntfConfVtcs_Type(Integer32):
    """Custom type tAtmIntfConfVtcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_TAtmIntfConfVtcs_Type.__name__ = "Integer32"
_TAtmIntfConfVtcs_Object = MibTableColumn
tAtmIntfConfVtcs = _TAtmIntfConfVtcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1, 16),
    _TAtmIntfConfVtcs_Type()
)
tAtmIntfConfVtcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfConfVtcs.setStatus("current")


class _TAtmIntfConfIfcs_Type(Integer32):
    """Custom type tAtmIntfConfIfcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TAtmIntfConfIfcs_Type.__name__ = "Integer32"
_TAtmIntfConfIfcs_Object = MibTableColumn
tAtmIntfConfIfcs = _TAtmIntfConfIfcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 1, 1, 17),
    _TAtmIntfConfIfcs_Type()
)
tAtmIntfConfIfcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfConfIfcs.setStatus("current")
_TAtmIntfStatsTable_Object = MibTable
tAtmIntfStatsTable = _TAtmIntfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 2)
)
if mibBuilder.loadTexts:
    tAtmIntfStatsTable.setStatus("current")
_TAtmIntfStatsEntry_Object = MibTableRow
tAtmIntfStatsEntry = _TAtmIntfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 2, 1)
)
tAtmIntfStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tAtmIntfStatsEntry.setStatus("current")
_TAtmIntfStatsTotalCellsRxd_Type = Counter64
_TAtmIntfStatsTotalCellsRxd_Object = MibTableColumn
tAtmIntfStatsTotalCellsRxd = _TAtmIntfStatsTotalCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 2, 1, 1),
    _TAtmIntfStatsTotalCellsRxd_Type()
)
tAtmIntfStatsTotalCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfStatsTotalCellsRxd.setStatus("current")
_TAtmIntfStatsTotalCellsTxd_Type = Counter64
_TAtmIntfStatsTotalCellsTxd_Object = MibTableColumn
tAtmIntfStatsTotalCellsTxd = _TAtmIntfStatsTotalCellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 2, 1, 2),
    _TAtmIntfStatsTotalCellsTxd_Type()
)
tAtmIntfStatsTotalCellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfStatsTotalCellsTxd.setStatus("current")
_TAtmIntfStatsTotalBytesRxd_Type = Counter64
_TAtmIntfStatsTotalBytesRxd_Object = MibTableColumn
tAtmIntfStatsTotalBytesRxd = _TAtmIntfStatsTotalBytesRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 2, 1, 3),
    _TAtmIntfStatsTotalBytesRxd_Type()
)
tAtmIntfStatsTotalBytesRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfStatsTotalBytesRxd.setStatus("current")
_TAtmIntfStatsTotalBytesTxd_Type = Counter64
_TAtmIntfStatsTotalBytesTxd_Object = MibTableColumn
tAtmIntfStatsTotalBytesTxd = _TAtmIntfStatsTotalBytesTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 2, 1, 4),
    _TAtmIntfStatsTotalBytesTxd_Type()
)
tAtmIntfStatsTotalBytesTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfStatsTotalBytesTxd.setStatus("current")
_TAtmIntfStatsTotalUnknCellsDrp_Type = Counter32
_TAtmIntfStatsTotalUnknCellsDrp_Object = MibTableColumn
tAtmIntfStatsTotalUnknCellsDrp = _TAtmIntfStatsTotalUnknCellsDrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 2, 1, 5),
    _TAtmIntfStatsTotalUnknCellsDrp_Type()
)
tAtmIntfStatsTotalUnknCellsDrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfStatsTotalUnknCellsDrp.setStatus("current")
_TAtmIntfStatsTotalHecErr_Type = Counter32
_TAtmIntfStatsTotalHecErr_Object = MibTableColumn
tAtmIntfStatsTotalHecErr = _TAtmIntfStatsTotalHecErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 2, 1, 6),
    _TAtmIntfStatsTotalHecErr_Type()
)
tAtmIntfStatsTotalHecErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfStatsTotalHecErr.setStatus("obsolete")
_TAtmIntfStatsTotalHecErrFixed_Type = Counter32
_TAtmIntfStatsTotalHecErrFixed_Object = MibTableColumn
tAtmIntfStatsTotalHecErrFixed = _TAtmIntfStatsTotalHecErrFixed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 2, 1, 7),
    _TAtmIntfStatsTotalHecErrFixed_Type()
)
tAtmIntfStatsTotalHecErrFixed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfStatsTotalHecErrFixed.setStatus("obsolete")
_TAtmIntfAal5StatsTable_Object = MibTable
tAtmIntfAal5StatsTable = _TAtmIntfAal5StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 3)
)
if mibBuilder.loadTexts:
    tAtmIntfAal5StatsTable.setStatus("current")
_TAtmIntfAal5StatsEntry_Object = MibTableRow
tAtmIntfAal5StatsEntry = _TAtmIntfAal5StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 3, 1)
)
tAtmIntfAal5StatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tAtmIntfAal5StatsEntry.setStatus("current")
_TAtmIntfAal5StatsTotalPktsRxd_Type = Counter64
_TAtmIntfAal5StatsTotalPktsRxd_Object = MibTableColumn
tAtmIntfAal5StatsTotalPktsRxd = _TAtmIntfAal5StatsTotalPktsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 3, 1, 1),
    _TAtmIntfAal5StatsTotalPktsRxd_Type()
)
tAtmIntfAal5StatsTotalPktsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfAal5StatsTotalPktsRxd.setStatus("current")
_TAtmIntfAal5StatsTotalPktsTxd_Type = Counter64
_TAtmIntfAal5StatsTotalPktsTxd_Object = MibTableColumn
tAtmIntfAal5StatsTotalPktsTxd = _TAtmIntfAal5StatsTotalPktsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 3, 1, 2),
    _TAtmIntfAal5StatsTotalPktsTxd_Type()
)
tAtmIntfAal5StatsTotalPktsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfAal5StatsTotalPktsTxd.setStatus("current")
_TAtmIntfAal5StatsTotalPktsDrpRxd_Type = Counter64
_TAtmIntfAal5StatsTotalPktsDrpRxd_Object = MibTableColumn
tAtmIntfAal5StatsTotalPktsDrpRxd = _TAtmIntfAal5StatsTotalPktsDrpRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 3, 1, 3),
    _TAtmIntfAal5StatsTotalPktsDrpRxd_Type()
)
tAtmIntfAal5StatsTotalPktsDrpRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfAal5StatsTotalPktsDrpRxd.setStatus("current")
_TAtmIntfAal5StatsTotalPktsDrpTxd_Type = Counter64
_TAtmIntfAal5StatsTotalPktsDrpTxd_Object = MibTableColumn
tAtmIntfAal5StatsTotalPktsDrpTxd = _TAtmIntfAal5StatsTotalPktsDrpTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 3, 1, 4),
    _TAtmIntfAal5StatsTotalPktsDrpTxd_Type()
)
tAtmIntfAal5StatsTotalPktsDrpTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfAal5StatsTotalPktsDrpTxd.setStatus("current")
_TAtmIntfAal5StatsTotalCrc32Err_Type = Counter64
_TAtmIntfAal5StatsTotalCrc32Err_Object = MibTableColumn
tAtmIntfAal5StatsTotalCrc32Err = _TAtmIntfAal5StatsTotalCrc32Err_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 3, 1, 5),
    _TAtmIntfAal5StatsTotalCrc32Err_Type()
)
tAtmIntfAal5StatsTotalCrc32Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIntfAal5StatsTotalCrc32Err.setStatus("current")
_TAtmIfcInfoTable_Object = MibTable
tAtmIfcInfoTable = _TAtmIfcInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 4)
)
if mibBuilder.loadTexts:
    tAtmIfcInfoTable.setStatus("current")
_TAtmIfcInfoEntry_Object = MibTableRow
tAtmIfcInfoEntry = _TAtmIfcInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 4, 1)
)
tAtmIfcInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tAtmIfcInfoEntry.setStatus("current")
_TAtmIfcAdminStatus_Type = AtmVorXAdminStatus
_TAtmIfcAdminStatus_Object = MibTableColumn
tAtmIfcAdminStatus = _TAtmIfcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 4, 1, 1),
    _TAtmIfcAdminStatus_Type()
)
tAtmIfcAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcAdminStatus.setStatus("current")
_TAtmIfcOperStatus_Type = AtmVorXOperStatus
_TAtmIfcOperStatus_Object = MibTableColumn
tAtmIfcOperStatus = _TAtmIfcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 4, 1, 2),
    _TAtmIfcOperStatus_Type()
)
tAtmIfcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcOperStatus.setStatus("current")
_TAtmIfcLastChange_Type = AtmVorXLastChange
_TAtmIfcLastChange_Object = MibTableColumn
tAtmIfcLastChange = _TAtmIfcLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 4, 1, 3),
    _TAtmIfcLastChange_Type()
)
tAtmIfcLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcLastChange.setStatus("current")
_TAtmIfcReceiveTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_TAtmIfcReceiveTrafficDescrIndex_Object = MibTableColumn
tAtmIfcReceiveTrafficDescrIndex = _TAtmIfcReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 4, 1, 4),
    _TAtmIfcReceiveTrafficDescrIndex_Type()
)
tAtmIfcReceiveTrafficDescrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcReceiveTrafficDescrIndex.setStatus("current")
_TAtmIfcTransmitTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_TAtmIfcTransmitTrafficDescrIndex_Object = MibTableColumn
tAtmIfcTransmitTrafficDescrIndex = _TAtmIfcTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 4, 1, 5),
    _TAtmIfcTransmitTrafficDescrIndex_Type()
)
tAtmIfcTransmitTrafficDescrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcTransmitTrafficDescrIndex.setStatus("current")
_TAtmIfcRowStatus_Type = RowStatus
_TAtmIfcRowStatus_Object = MibTableColumn
tAtmIfcRowStatus = _TAtmIfcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 4, 1, 6),
    _TAtmIfcRowStatus_Type()
)
tAtmIfcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcRowStatus.setStatus("current")
_TAtmIfcCastType_Type = AtmConnCastType
_TAtmIfcCastType_Object = MibTableColumn
tAtmIfcCastType = _TAtmIfcCastType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 4, 1, 7),
    _TAtmIfcCastType_Type()
)
tAtmIfcCastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcCastType.setStatus("current")
_TAtmIfcConnKind_Type = AtmConnKind
_TAtmIfcConnKind_Object = MibTableColumn
tAtmIfcConnKind = _TAtmIfcConnKind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 4, 1, 8),
    _TAtmIfcConnKind_Type()
)
tAtmIfcConnKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcConnKind.setStatus("current")
_TAtmIfcInfoOwner_Type = AtmConnectionOwner
_TAtmIfcInfoOwner_Object = MibTableColumn
tAtmIfcInfoOwner = _TAtmIfcInfoOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 4, 1, 9),
    _TAtmIfcInfoOwner_Type()
)
tAtmIfcInfoOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcInfoOwner.setStatus("current")
_TAtmIfcStatisticsTable_Object = MibTable
tAtmIfcStatisticsTable = _TAtmIfcStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 5)
)
if mibBuilder.loadTexts:
    tAtmIfcStatisticsTable.setStatus("current")
_TAtmIfcStatisticsEntry_Object = MibTableRow
tAtmIfcStatisticsEntry = _TAtmIfcStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 5, 1)
)
tAtmIfcStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tAtmIfcStatisticsEntry.setStatus("current")
_TAtmIfcStatsTotalCellsRxd_Type = Counter64
_TAtmIfcStatsTotalCellsRxd_Object = MibTableColumn
tAtmIfcStatsTotalCellsRxd = _TAtmIfcStatsTotalCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 5, 1, 1),
    _TAtmIfcStatsTotalCellsRxd_Type()
)
tAtmIfcStatsTotalCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcStatsTotalCellsRxd.setStatus("current")
_TAtmIfcStatsTotalClp0CellsRxd_Type = Counter64
_TAtmIfcStatsTotalClp0CellsRxd_Object = MibTableColumn
tAtmIfcStatsTotalClp0CellsRxd = _TAtmIfcStatsTotalClp0CellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 5, 1, 2),
    _TAtmIfcStatsTotalClp0CellsRxd_Type()
)
tAtmIfcStatsTotalClp0CellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcStatsTotalClp0CellsRxd.setStatus("current")
_TAtmIfcStatsTotalCellsTxd_Type = Counter64
_TAtmIfcStatsTotalCellsTxd_Object = MibTableColumn
tAtmIfcStatsTotalCellsTxd = _TAtmIfcStatsTotalCellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 5, 1, 3),
    _TAtmIfcStatsTotalCellsTxd_Type()
)
tAtmIfcStatsTotalCellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcStatsTotalCellsTxd.setStatus("current")
_TAtmIfcStatsTotalClp0CellsTxd_Type = Counter64
_TAtmIfcStatsTotalClp0CellsTxd_Object = MibTableColumn
tAtmIfcStatsTotalClp0CellsTxd = _TAtmIfcStatsTotalClp0CellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 5, 1, 4),
    _TAtmIfcStatsTotalClp0CellsTxd_Type()
)
tAtmIfcStatsTotalClp0CellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcStatsTotalClp0CellsTxd.setStatus("current")
_TAtmIfcStatsTotalBytesRxd_Type = Counter64
_TAtmIfcStatsTotalBytesRxd_Object = MibTableColumn
tAtmIfcStatsTotalBytesRxd = _TAtmIfcStatsTotalBytesRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 5, 1, 5),
    _TAtmIfcStatsTotalBytesRxd_Type()
)
tAtmIfcStatsTotalBytesRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcStatsTotalBytesRxd.setStatus("current")
_TAtmIfcStatsTotalBytesTxd_Type = Counter64
_TAtmIfcStatsTotalBytesTxd_Object = MibTableColumn
tAtmIfcStatsTotalBytesTxd = _TAtmIfcStatsTotalBytesTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 5, 1, 6),
    _TAtmIfcStatsTotalBytesTxd_Type()
)
tAtmIfcStatsTotalBytesTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcStatsTotalBytesTxd.setStatus("current")
_TAtmIfcStatsDrpCellsRxd_Type = Counter32
_TAtmIfcStatsDrpCellsRxd_Object = MibTableColumn
tAtmIfcStatsDrpCellsRxd = _TAtmIfcStatsDrpCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 5, 1, 7),
    _TAtmIfcStatsDrpCellsRxd_Type()
)
tAtmIfcStatsDrpCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcStatsDrpCellsRxd.setStatus("current")
_TAtmIfcStatsDrpClp0CellsRxd_Type = Counter32
_TAtmIfcStatsDrpClp0CellsRxd_Object = MibTableColumn
tAtmIfcStatsDrpClp0CellsRxd = _TAtmIfcStatsDrpClp0CellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 5, 1, 8),
    _TAtmIfcStatsDrpClp0CellsRxd_Type()
)
tAtmIfcStatsDrpClp0CellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcStatsDrpClp0CellsRxd.setStatus("current")
_TAtmIfcStatsDrpClp0CellsTxd_Type = Counter32
_TAtmIfcStatsDrpClp0CellsTxd_Object = MibTableColumn
tAtmIfcStatsDrpClp0CellsTxd = _TAtmIfcStatsDrpClp0CellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 5, 1, 9),
    _TAtmIfcStatsDrpClp0CellsTxd_Type()
)
tAtmIfcStatsDrpClp0CellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcStatsDrpClp0CellsTxd.setStatus("current")
_TAtmIfcStatsTagCells_Type = Counter32
_TAtmIfcStatsTagCells_Object = MibTableColumn
tAtmIfcStatsTagCells = _TAtmIfcStatsTagCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 2, 5, 1, 10),
    _TAtmIfcStatsTagCells_Type()
)
tAtmIfcStatsTagCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIfcStatsTagCells.setStatus("current")
_TAtmVclObjs_ObjectIdentity = ObjectIdentity
tAtmVclObjs = _TAtmVclObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3)
)
_TAtmVclInfoTable_Object = MibTable
tAtmVclInfoTable = _TAtmVclInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 1)
)
if mibBuilder.loadTexts:
    tAtmVclInfoTable.setStatus("current")
_TAtmVclInfoEntry_Object = MibTableRow
tAtmVclInfoEntry = _TAtmVclInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tAtmVclInfoEntry.setStatus("current")
_TAtmVclInfoOwner_Type = AtmConnectionOwner
_TAtmVclInfoOwner_Object = MibTableColumn
tAtmVclInfoOwner = _TAtmVclInfoOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 1, 1, 1),
    _TAtmVclInfoOwner_Type()
)
tAtmVclInfoOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVclInfoOwner.setStatus("current")
_TAtmVclInfoOamStatus_Type = AtmOamStatus
_TAtmVclInfoOamStatus_Object = MibTableColumn
tAtmVclInfoOamStatus = _TAtmVclInfoOamStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 1, 1, 2),
    _TAtmVclInfoOamStatus_Type()
)
tAtmVclInfoOamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVclInfoOamStatus.setStatus("current")
_TAtmVclInfoIlmiStatus_Type = AtmIlmiStatus
_TAtmVclInfoIlmiStatus_Object = MibTableColumn
tAtmVclInfoIlmiStatus = _TAtmVclInfoIlmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 1, 1, 3),
    _TAtmVclInfoIlmiStatus_Type()
)
tAtmVclInfoIlmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVclInfoIlmiStatus.setStatus("current")


class _TAtmVclInfoRxTrafficDescrIdOvr_Type(AtmTrafficDescrParamIndex):
    """Custom type tAtmVclInfoRxTrafficDescrIdOvr based on AtmTrafficDescrParamIndex"""
    subtypeSpec = AtmTrafficDescrParamIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_TAtmVclInfoRxTrafficDescrIdOvr_Type.__name__ = "AtmTrafficDescrParamIndex"
_TAtmVclInfoRxTrafficDescrIdOvr_Object = MibTableColumn
tAtmVclInfoRxTrafficDescrIdOvr = _TAtmVclInfoRxTrafficDescrIdOvr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 1, 1, 4),
    _TAtmVclInfoRxTrafficDescrIdOvr_Type()
)
tAtmVclInfoRxTrafficDescrIdOvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVclInfoRxTrafficDescrIdOvr.setStatus("current")


class _TAtmVclInfoTxTrafficDescrIdOvr_Type(AtmTrafficDescrParamIndex):
    """Custom type tAtmVclInfoTxTrafficDescrIdOvr based on AtmTrafficDescrParamIndex"""
    subtypeSpec = AtmTrafficDescrParamIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_TAtmVclInfoTxTrafficDescrIdOvr_Type.__name__ = "AtmTrafficDescrParamIndex"
_TAtmVclInfoTxTrafficDescrIdOvr_Object = MibTableColumn
tAtmVclInfoTxTrafficDescrIdOvr = _TAtmVclInfoTxTrafficDescrIdOvr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 1, 1, 5),
    _TAtmVclInfoTxTrafficDescrIdOvr_Type()
)
tAtmVclInfoTxTrafficDescrIdOvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVclInfoTxTrafficDescrIdOvr.setStatus("current")
_TAtmVclStatisticsTable_Object = MibTable
tAtmVclStatisticsTable = _TAtmVclStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 2)
)
if mibBuilder.loadTexts:
    tAtmVclStatisticsTable.setStatus("current")
_TAtmVclStatisticsEntry_Object = MibTableRow
tAtmVclStatisticsEntry = _TAtmVclStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 2, 1)
)
tAtmVclStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    tAtmVclStatisticsEntry.setStatus("current")
_TAtmVclStatsTotalCellsRxd_Type = Counter64
_TAtmVclStatsTotalCellsRxd_Object = MibTableColumn
tAtmVclStatsTotalCellsRxd = _TAtmVclStatsTotalCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 2, 1, 1),
    _TAtmVclStatsTotalCellsRxd_Type()
)
tAtmVclStatsTotalCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVclStatsTotalCellsRxd.setStatus("current")
_TAtmVclStatsTotalCellsTxd_Type = Counter64
_TAtmVclStatsTotalCellsTxd_Object = MibTableColumn
tAtmVclStatsTotalCellsTxd = _TAtmVclStatsTotalCellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 2, 1, 2),
    _TAtmVclStatsTotalCellsTxd_Type()
)
tAtmVclStatsTotalCellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVclStatsTotalCellsTxd.setStatus("current")
_TAtmVclStatsTotalBytesRxd_Type = Counter64
_TAtmVclStatsTotalBytesRxd_Object = MibTableColumn
tAtmVclStatsTotalBytesRxd = _TAtmVclStatsTotalBytesRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 2, 1, 3),
    _TAtmVclStatsTotalBytesRxd_Type()
)
tAtmVclStatsTotalBytesRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVclStatsTotalBytesRxd.setStatus("current")
_TAtmVclStatsTotalBytesTxd_Type = Counter64
_TAtmVclStatsTotalBytesTxd_Object = MibTableColumn
tAtmVclStatsTotalBytesTxd = _TAtmVclStatsTotalBytesTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 2, 1, 4),
    _TAtmVclStatsTotalBytesTxd_Type()
)
tAtmVclStatsTotalBytesTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVclStatsTotalBytesTxd.setStatus("current")
_TAtmOamVclStatisticsTable_Object = MibTable
tAtmOamVclStatisticsTable = _TAtmOamVclStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 3)
)
if mibBuilder.loadTexts:
    tAtmOamVclStatisticsTable.setStatus("current")
_TAtmOamVclStatisticsEntry_Object = MibTableRow
tAtmOamVclStatisticsEntry = _TAtmOamVclStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tAtmOamVclStatisticsEntry.setStatus("current")
_TAtmOamVclStatsAISCellsTxd_Type = Counter32
_TAtmOamVclStatsAISCellsTxd_Object = MibTableColumn
tAtmOamVclStatsAISCellsTxd = _TAtmOamVclStatsAISCellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 3, 1, 1),
    _TAtmOamVclStatsAISCellsTxd_Type()
)
tAtmOamVclStatsAISCellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmOamVclStatsAISCellsTxd.setStatus("current")
_TAtmOamVclStatsRDICellsTxd_Type = Counter32
_TAtmOamVclStatsRDICellsTxd_Object = MibTableColumn
tAtmOamVclStatsRDICellsTxd = _TAtmOamVclStatsRDICellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 3, 1, 2),
    _TAtmOamVclStatsRDICellsTxd_Type()
)
tAtmOamVclStatsRDICellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmOamVclStatsRDICellsTxd.setStatus("current")
_TAtmOamVclStatsLoopbackCellsTxd_Type = Counter32
_TAtmOamVclStatsLoopbackCellsTxd_Object = MibTableColumn
tAtmOamVclStatsLoopbackCellsTxd = _TAtmOamVclStatsLoopbackCellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 3, 1, 3),
    _TAtmOamVclStatsLoopbackCellsTxd_Type()
)
tAtmOamVclStatsLoopbackCellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmOamVclStatsLoopbackCellsTxd.setStatus("current")
_TAtmOamVclStatsAISCellsRxd_Type = Counter32
_TAtmOamVclStatsAISCellsRxd_Object = MibTableColumn
tAtmOamVclStatsAISCellsRxd = _TAtmOamVclStatsAISCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 3, 1, 4),
    _TAtmOamVclStatsAISCellsRxd_Type()
)
tAtmOamVclStatsAISCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmOamVclStatsAISCellsRxd.setStatus("current")
_TAtmOamVclStatsRDICellsRxd_Type = Counter32
_TAtmOamVclStatsRDICellsRxd_Object = MibTableColumn
tAtmOamVclStatsRDICellsRxd = _TAtmOamVclStatsRDICellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 3, 1, 5),
    _TAtmOamVclStatsRDICellsRxd_Type()
)
tAtmOamVclStatsRDICellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmOamVclStatsRDICellsRxd.setStatus("current")
_TAtmOamVclStatsLoopbackCellsRxd_Type = Counter32
_TAtmOamVclStatsLoopbackCellsRxd_Object = MibTableColumn
tAtmOamVclStatsLoopbackCellsRxd = _TAtmOamVclStatsLoopbackCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 3, 1, 6),
    _TAtmOamVclStatsLoopbackCellsRxd_Type()
)
tAtmOamVclStatsLoopbackCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmOamVclStatsLoopbackCellsRxd.setStatus("current")
_TAtmOamVclStatsCrc10Err_Type = Counter32
_TAtmOamVclStatsCrc10Err_Object = MibTableColumn
tAtmOamVclStatsCrc10Err = _TAtmOamVclStatsCrc10Err_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 3, 1, 7),
    _TAtmOamVclStatsCrc10Err_Type()
)
tAtmOamVclStatsCrc10Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmOamVclStatsCrc10Err.setStatus("current")
_TAtmOamVclStatsOtherCellsRxd_Type = Counter32
_TAtmOamVclStatsOtherCellsRxd_Object = MibTableColumn
tAtmOamVclStatsOtherCellsRxd = _TAtmOamVclStatsOtherCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 3, 3, 1, 8),
    _TAtmOamVclStatsOtherCellsRxd_Type()
)
tAtmOamVclStatsOtherCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmOamVclStatsOtherCellsRxd.setStatus("current")
_TAal5VccObjs_ObjectIdentity = ObjectIdentity
tAal5VccObjs = _TAal5VccObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 4)
)
_TAal5VccStatisticsTable_Object = MibTable
tAal5VccStatisticsTable = _TAal5VccStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 4, 1)
)
if mibBuilder.loadTexts:
    tAal5VccStatisticsTable.setStatus("current")
_TAal5VccStatisticsEntry_Object = MibTableRow
tAal5VccStatisticsEntry = _TAal5VccStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 4, 1, 1)
)
if mibBuilder.loadTexts:
    tAal5VccStatisticsEntry.setStatus("current")
_TAal5VccStatsPacketsRxd_Type = Counter64
_TAal5VccStatsPacketsRxd_Object = MibTableColumn
tAal5VccStatsPacketsRxd = _TAal5VccStatsPacketsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 4, 1, 1, 1),
    _TAal5VccStatsPacketsRxd_Type()
)
tAal5VccStatsPacketsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAal5VccStatsPacketsRxd.setStatus("current")
_TAal5VccStatsPacketsTxd_Type = Counter64
_TAal5VccStatsPacketsTxd_Object = MibTableColumn
tAal5VccStatsPacketsTxd = _TAal5VccStatsPacketsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 4, 1, 1, 2),
    _TAal5VccStatsPacketsTxd_Type()
)
tAal5VccStatsPacketsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAal5VccStatsPacketsTxd.setStatus("current")
_TAal5VccStatsDrpPacketsRxd_Type = Counter64
_TAal5VccStatsDrpPacketsRxd_Object = MibTableColumn
tAal5VccStatsDrpPacketsRxd = _TAal5VccStatsDrpPacketsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 4, 1, 1, 3),
    _TAal5VccStatsDrpPacketsRxd_Type()
)
tAal5VccStatsDrpPacketsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAal5VccStatsDrpPacketsRxd.setStatus("current")
_TAal5VccStatsDrpPacketsTxd_Type = Counter64
_TAal5VccStatsDrpPacketsTxd_Object = MibTableColumn
tAal5VccStatsDrpPacketsTxd = _TAal5VccStatsDrpPacketsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 4, 1, 1, 4),
    _TAal5VccStatsDrpPacketsTxd_Type()
)
tAal5VccStatsDrpPacketsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAal5VccStatsDrpPacketsTxd.setStatus("current")
_TAtmTrafficDescObjs_ObjectIdentity = ObjectIdentity
tAtmTrafficDescObjs = _TAtmTrafficDescObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 5)
)
_TAtmVplObjs_ObjectIdentity = ObjectIdentity
tAtmVplObjs = _TAtmVplObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6)
)
_TAtmVplInfoTable_Object = MibTable
tAtmVplInfoTable = _TAtmVplInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 1)
)
if mibBuilder.loadTexts:
    tAtmVplInfoTable.setStatus("current")
_TAtmVplInfoEntry_Object = MibTableRow
tAtmVplInfoEntry = _TAtmVplInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 1, 1)
)
if mibBuilder.loadTexts:
    tAtmVplInfoEntry.setStatus("current")
_TAtmVplInfoOwner_Type = AtmConnectionOwner
_TAtmVplInfoOwner_Object = MibTableColumn
tAtmVplInfoOwner = _TAtmVplInfoOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 1, 1, 1),
    _TAtmVplInfoOwner_Type()
)
tAtmVplInfoOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVplInfoOwner.setStatus("current")
_TAtmVplInfoOamStatus_Type = AtmOamStatus
_TAtmVplInfoOamStatus_Object = MibTableColumn
tAtmVplInfoOamStatus = _TAtmVplInfoOamStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 1, 1, 2),
    _TAtmVplInfoOamStatus_Type()
)
tAtmVplInfoOamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVplInfoOamStatus.setStatus("current")
_TAtmVplInfoIlmiStatus_Type = AtmIlmiStatus
_TAtmVplInfoIlmiStatus_Object = MibTableColumn
tAtmVplInfoIlmiStatus = _TAtmVplInfoIlmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 1, 1, 3),
    _TAtmVplInfoIlmiStatus_Type()
)
tAtmVplInfoIlmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVplInfoIlmiStatus.setStatus("current")
_TAtmVplStatisticsTable_Object = MibTable
tAtmVplStatisticsTable = _TAtmVplStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 2)
)
if mibBuilder.loadTexts:
    tAtmVplStatisticsTable.setStatus("current")
_TAtmVplStatisticsEntry_Object = MibTableRow
tAtmVplStatisticsEntry = _TAtmVplStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 2, 1)
)
tAtmVplStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    tAtmVplStatisticsEntry.setStatus("current")
_TAtmVplStatsTotalCellsRxd_Type = Counter64
_TAtmVplStatsTotalCellsRxd_Object = MibTableColumn
tAtmVplStatsTotalCellsRxd = _TAtmVplStatsTotalCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 2, 1, 1),
    _TAtmVplStatsTotalCellsRxd_Type()
)
tAtmVplStatsTotalCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVplStatsTotalCellsRxd.setStatus("current")
_TAtmVplStatsTotalClp0CellsRxd_Type = Counter64
_TAtmVplStatsTotalClp0CellsRxd_Object = MibTableColumn
tAtmVplStatsTotalClp0CellsRxd = _TAtmVplStatsTotalClp0CellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 2, 1, 2),
    _TAtmVplStatsTotalClp0CellsRxd_Type()
)
tAtmVplStatsTotalClp0CellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVplStatsTotalClp0CellsRxd.setStatus("current")
_TAtmVplStatsTotalCellsTxd_Type = Counter64
_TAtmVplStatsTotalCellsTxd_Object = MibTableColumn
tAtmVplStatsTotalCellsTxd = _TAtmVplStatsTotalCellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 2, 1, 3),
    _TAtmVplStatsTotalCellsTxd_Type()
)
tAtmVplStatsTotalCellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVplStatsTotalCellsTxd.setStatus("current")
_TAtmVplStatsTotalClp0CellsTxd_Type = Counter64
_TAtmVplStatsTotalClp0CellsTxd_Object = MibTableColumn
tAtmVplStatsTotalClp0CellsTxd = _TAtmVplStatsTotalClp0CellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 2, 1, 4),
    _TAtmVplStatsTotalClp0CellsTxd_Type()
)
tAtmVplStatsTotalClp0CellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVplStatsTotalClp0CellsTxd.setStatus("current")
_TAtmVplStatsTotalBytesRxd_Type = Counter64
_TAtmVplStatsTotalBytesRxd_Object = MibTableColumn
tAtmVplStatsTotalBytesRxd = _TAtmVplStatsTotalBytesRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 2, 1, 5),
    _TAtmVplStatsTotalBytesRxd_Type()
)
tAtmVplStatsTotalBytesRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVplStatsTotalBytesRxd.setStatus("current")
_TAtmVplStatsTotalBytesTxd_Type = Counter64
_TAtmVplStatsTotalBytesTxd_Object = MibTableColumn
tAtmVplStatsTotalBytesTxd = _TAtmVplStatsTotalBytesTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 2, 1, 6),
    _TAtmVplStatsTotalBytesTxd_Type()
)
tAtmVplStatsTotalBytesTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVplStatsTotalBytesTxd.setStatus("current")
_TAtmVplStatsDrpCellsRxd_Type = Counter32
_TAtmVplStatsDrpCellsRxd_Object = MibTableColumn
tAtmVplStatsDrpCellsRxd = _TAtmVplStatsDrpCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 2, 1, 7),
    _TAtmVplStatsDrpCellsRxd_Type()
)
tAtmVplStatsDrpCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVplStatsDrpCellsRxd.setStatus("current")
_TAtmVplStatsDrpClp0CellsRxd_Type = Counter32
_TAtmVplStatsDrpClp0CellsRxd_Object = MibTableColumn
tAtmVplStatsDrpClp0CellsRxd = _TAtmVplStatsDrpClp0CellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 2, 1, 8),
    _TAtmVplStatsDrpClp0CellsRxd_Type()
)
tAtmVplStatsDrpClp0CellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVplStatsDrpClp0CellsRxd.setStatus("current")
_TAtmVplStatsDrpClp0CellsTxd_Type = Counter32
_TAtmVplStatsDrpClp0CellsTxd_Object = MibTableColumn
tAtmVplStatsDrpClp0CellsTxd = _TAtmVplStatsDrpClp0CellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 2, 1, 9),
    _TAtmVplStatsDrpClp0CellsTxd_Type()
)
tAtmVplStatsDrpClp0CellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVplStatsDrpClp0CellsTxd.setStatus("current")
_TAtmVplStatsTagCells_Type = Counter32
_TAtmVplStatsTagCells_Object = MibTableColumn
tAtmVplStatsTagCells = _TAtmVplStatsTagCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 2, 1, 10),
    _TAtmVplStatsTagCells_Type()
)
tAtmVplStatsTagCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVplStatsTagCells.setStatus("current")
_TAtmOamVplStatisticsTable_Object = MibTable
tAtmOamVplStatisticsTable = _TAtmOamVplStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 3)
)
if mibBuilder.loadTexts:
    tAtmOamVplStatisticsTable.setStatus("current")
_TAtmOamVplStatisticsEntry_Object = MibTableRow
tAtmOamVplStatisticsEntry = _TAtmOamVplStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 3, 1)
)
tAtmOamVplStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    tAtmOamVplStatisticsEntry.setStatus("current")
_TAtmOamVplStatsAISCellsTxd_Type = Counter32
_TAtmOamVplStatsAISCellsTxd_Object = MibTableColumn
tAtmOamVplStatsAISCellsTxd = _TAtmOamVplStatsAISCellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 3, 1, 1),
    _TAtmOamVplStatsAISCellsTxd_Type()
)
tAtmOamVplStatsAISCellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmOamVplStatsAISCellsTxd.setStatus("current")
_TAtmOamVplStatsRDICellsTxd_Type = Counter32
_TAtmOamVplStatsRDICellsTxd_Object = MibTableColumn
tAtmOamVplStatsRDICellsTxd = _TAtmOamVplStatsRDICellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 3, 1, 2),
    _TAtmOamVplStatsRDICellsTxd_Type()
)
tAtmOamVplStatsRDICellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmOamVplStatsRDICellsTxd.setStatus("current")
_TAtmOamVplStatsLoopbackCellsTxd_Type = Counter32
_TAtmOamVplStatsLoopbackCellsTxd_Object = MibTableColumn
tAtmOamVplStatsLoopbackCellsTxd = _TAtmOamVplStatsLoopbackCellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 3, 1, 3),
    _TAtmOamVplStatsLoopbackCellsTxd_Type()
)
tAtmOamVplStatsLoopbackCellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmOamVplStatsLoopbackCellsTxd.setStatus("current")
_TAtmOamVplStatsAISCellsRxd_Type = Counter32
_TAtmOamVplStatsAISCellsRxd_Object = MibTableColumn
tAtmOamVplStatsAISCellsRxd = _TAtmOamVplStatsAISCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 3, 1, 4),
    _TAtmOamVplStatsAISCellsRxd_Type()
)
tAtmOamVplStatsAISCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmOamVplStatsAISCellsRxd.setStatus("current")
_TAtmOamVplStatsRDICellsRxd_Type = Counter32
_TAtmOamVplStatsRDICellsRxd_Object = MibTableColumn
tAtmOamVplStatsRDICellsRxd = _TAtmOamVplStatsRDICellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 3, 1, 5),
    _TAtmOamVplStatsRDICellsRxd_Type()
)
tAtmOamVplStatsRDICellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmOamVplStatsRDICellsRxd.setStatus("current")
_TAtmOamVplStatsLoopbackCellsRxd_Type = Counter32
_TAtmOamVplStatsLoopbackCellsRxd_Object = MibTableColumn
tAtmOamVplStatsLoopbackCellsRxd = _TAtmOamVplStatsLoopbackCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 3, 1, 6),
    _TAtmOamVplStatsLoopbackCellsRxd_Type()
)
tAtmOamVplStatsLoopbackCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmOamVplStatsLoopbackCellsRxd.setStatus("current")
_TAtmOamVplStatsCrc10Errors_Type = Counter32
_TAtmOamVplStatsCrc10Errors_Object = MibTableColumn
tAtmOamVplStatsCrc10Errors = _TAtmOamVplStatsCrc10Errors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 3, 1, 7),
    _TAtmOamVplStatsCrc10Errors_Type()
)
tAtmOamVplStatsCrc10Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmOamVplStatsCrc10Errors.setStatus("current")
_TAtmOamVplStatsOtherCellsRxd_Type = Counter32
_TAtmOamVplStatsOtherCellsRxd_Object = MibTableColumn
tAtmOamVplStatsOtherCellsRxd = _TAtmOamVplStatsOtherCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 6, 3, 1, 8),
    _TAtmOamVplStatsOtherCellsRxd_Type()
)
tAtmOamVplStatsOtherCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmOamVplStatsOtherCellsRxd.setStatus("current")
_TAtmVtlObjs_ObjectIdentity = ObjectIdentity
tAtmVtlObjs = _TAtmVtlObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7)
)
_TAtmVtlInfoTable_Object = MibTable
tAtmVtlInfoTable = _TAtmVtlInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 1)
)
if mibBuilder.loadTexts:
    tAtmVtlInfoTable.setStatus("current")
_TAtmVtlInfoEntry_Object = MibTableRow
tAtmVtlInfoEntry = _TAtmVtlInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 1, 1)
)
tAtmVtlInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TIMETRA-ATM-MIB", "tAtmVtlStartVpi"),
    (0, "TIMETRA-ATM-MIB", "tAtmVtlEndVpi"),
)
if mibBuilder.loadTexts:
    tAtmVtlInfoEntry.setStatus("current")
_TAtmVtlStartVpi_Type = AtmVpIdentifier
_TAtmVtlStartVpi_Object = MibTableColumn
tAtmVtlStartVpi = _TAtmVtlStartVpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 1, 1, 1),
    _TAtmVtlStartVpi_Type()
)
tAtmVtlStartVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tAtmVtlStartVpi.setStatus("current")
_TAtmVtlEndVpi_Type = AtmVpIdentifier
_TAtmVtlEndVpi_Object = MibTableColumn
tAtmVtlEndVpi = _TAtmVtlEndVpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 1, 1, 2),
    _TAtmVtlEndVpi_Type()
)
tAtmVtlEndVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tAtmVtlEndVpi.setStatus("current")
_TAtmVtlAdminStatus_Type = AtmVorXAdminStatus
_TAtmVtlAdminStatus_Object = MibTableColumn
tAtmVtlAdminStatus = _TAtmVtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 1, 1, 3),
    _TAtmVtlAdminStatus_Type()
)
tAtmVtlAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlAdminStatus.setStatus("current")
_TAtmVtlOperStatus_Type = AtmVorXOperStatus
_TAtmVtlOperStatus_Object = MibTableColumn
tAtmVtlOperStatus = _TAtmVtlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 1, 1, 4),
    _TAtmVtlOperStatus_Type()
)
tAtmVtlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlOperStatus.setStatus("current")
_TAtmVtlLastChange_Type = AtmVorXLastChange
_TAtmVtlLastChange_Object = MibTableColumn
tAtmVtlLastChange = _TAtmVtlLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 1, 1, 5),
    _TAtmVtlLastChange_Type()
)
tAtmVtlLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlLastChange.setStatus("current")
_TAtmVtlReceiveTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_TAtmVtlReceiveTrafficDescrIndex_Object = MibTableColumn
tAtmVtlReceiveTrafficDescrIndex = _TAtmVtlReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 1, 1, 6),
    _TAtmVtlReceiveTrafficDescrIndex_Type()
)
tAtmVtlReceiveTrafficDescrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlReceiveTrafficDescrIndex.setStatus("current")
_TAtmVtlTransmitTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_TAtmVtlTransmitTrafficDescrIndex_Object = MibTableColumn
tAtmVtlTransmitTrafficDescrIndex = _TAtmVtlTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 1, 1, 7),
    _TAtmVtlTransmitTrafficDescrIndex_Type()
)
tAtmVtlTransmitTrafficDescrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlTransmitTrafficDescrIndex.setStatus("current")
_TAtmVtlRowStatus_Type = RowStatus
_TAtmVtlRowStatus_Object = MibTableColumn
tAtmVtlRowStatus = _TAtmVtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 1, 1, 8),
    _TAtmVtlRowStatus_Type()
)
tAtmVtlRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlRowStatus.setStatus("current")


class _TAtmVtlCastType_Type(AtmConnCastType):
    """Custom type tAtmVtlCastType based on AtmConnCastType"""


_TAtmVtlCastType_Object = MibTableColumn
tAtmVtlCastType = _TAtmVtlCastType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 1, 1, 9),
    _TAtmVtlCastType_Type()
)
tAtmVtlCastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlCastType.setStatus("current")
_TAtmVtlConnKind_Type = AtmConnKind
_TAtmVtlConnKind_Object = MibTableColumn
tAtmVtlConnKind = _TAtmVtlConnKind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 1, 1, 10),
    _TAtmVtlConnKind_Type()
)
tAtmVtlConnKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlConnKind.setStatus("current")
_TAtmVtlInfoOwner_Type = AtmConnectionOwner
_TAtmVtlInfoOwner_Object = MibTableColumn
tAtmVtlInfoOwner = _TAtmVtlInfoOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 1, 1, 11),
    _TAtmVtlInfoOwner_Type()
)
tAtmVtlInfoOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlInfoOwner.setStatus("current")
_TAtmVtlStatisticsTable_Object = MibTable
tAtmVtlStatisticsTable = _TAtmVtlStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 2)
)
if mibBuilder.loadTexts:
    tAtmVtlStatisticsTable.setStatus("current")
_TAtmVtlStatisticsEntry_Object = MibTableRow
tAtmVtlStatisticsEntry = _TAtmVtlStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 2, 1)
)
tAtmVtlStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TIMETRA-ATM-MIB", "tAtmVtlStartVpi"),
    (0, "TIMETRA-ATM-MIB", "tAtmVtlEndVpi"),
)
if mibBuilder.loadTexts:
    tAtmVtlStatisticsEntry.setStatus("current")
_TAtmVtlStatsTotalCellsRxd_Type = Counter64
_TAtmVtlStatsTotalCellsRxd_Object = MibTableColumn
tAtmVtlStatsTotalCellsRxd = _TAtmVtlStatsTotalCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 2, 1, 1),
    _TAtmVtlStatsTotalCellsRxd_Type()
)
tAtmVtlStatsTotalCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlStatsTotalCellsRxd.setStatus("current")
_TAtmVtlStatsTotalClp0CellsRxd_Type = Counter64
_TAtmVtlStatsTotalClp0CellsRxd_Object = MibTableColumn
tAtmVtlStatsTotalClp0CellsRxd = _TAtmVtlStatsTotalClp0CellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 2, 1, 2),
    _TAtmVtlStatsTotalClp0CellsRxd_Type()
)
tAtmVtlStatsTotalClp0CellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlStatsTotalClp0CellsRxd.setStatus("current")
_TAtmVtlStatsTotalCellsTxd_Type = Counter64
_TAtmVtlStatsTotalCellsTxd_Object = MibTableColumn
tAtmVtlStatsTotalCellsTxd = _TAtmVtlStatsTotalCellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 2, 1, 3),
    _TAtmVtlStatsTotalCellsTxd_Type()
)
tAtmVtlStatsTotalCellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlStatsTotalCellsTxd.setStatus("current")
_TAtmVtlStatsTotalClp0CellsTxd_Type = Counter64
_TAtmVtlStatsTotalClp0CellsTxd_Object = MibTableColumn
tAtmVtlStatsTotalClp0CellsTxd = _TAtmVtlStatsTotalClp0CellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 2, 1, 4),
    _TAtmVtlStatsTotalClp0CellsTxd_Type()
)
tAtmVtlStatsTotalClp0CellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlStatsTotalClp0CellsTxd.setStatus("current")
_TAtmVtlStatsTotalBytesRxd_Type = Counter64
_TAtmVtlStatsTotalBytesRxd_Object = MibTableColumn
tAtmVtlStatsTotalBytesRxd = _TAtmVtlStatsTotalBytesRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 2, 1, 5),
    _TAtmVtlStatsTotalBytesRxd_Type()
)
tAtmVtlStatsTotalBytesRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlStatsTotalBytesRxd.setStatus("current")
_TAtmVtlStatsTotalBytesTxd_Type = Counter64
_TAtmVtlStatsTotalBytesTxd_Object = MibTableColumn
tAtmVtlStatsTotalBytesTxd = _TAtmVtlStatsTotalBytesTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 2, 1, 6),
    _TAtmVtlStatsTotalBytesTxd_Type()
)
tAtmVtlStatsTotalBytesTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlStatsTotalBytesTxd.setStatus("current")
_TAtmVtlStatsDrpCellsRxd_Type = Counter32
_TAtmVtlStatsDrpCellsRxd_Object = MibTableColumn
tAtmVtlStatsDrpCellsRxd = _TAtmVtlStatsDrpCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 2, 1, 7),
    _TAtmVtlStatsDrpCellsRxd_Type()
)
tAtmVtlStatsDrpCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlStatsDrpCellsRxd.setStatus("current")
_TAtmVtlStatsDrpClp0CellsRxd_Type = Counter32
_TAtmVtlStatsDrpClp0CellsRxd_Object = MibTableColumn
tAtmVtlStatsDrpClp0CellsRxd = _TAtmVtlStatsDrpClp0CellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 2, 1, 8),
    _TAtmVtlStatsDrpClp0CellsRxd_Type()
)
tAtmVtlStatsDrpClp0CellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlStatsDrpClp0CellsRxd.setStatus("current")
_TAtmVtlStatsDrpClp0CellsTxd_Type = Counter32
_TAtmVtlStatsDrpClp0CellsTxd_Object = MibTableColumn
tAtmVtlStatsDrpClp0CellsTxd = _TAtmVtlStatsDrpClp0CellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 2, 1, 9),
    _TAtmVtlStatsDrpClp0CellsTxd_Type()
)
tAtmVtlStatsDrpClp0CellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlStatsDrpClp0CellsTxd.setStatus("current")
_TAtmVtlStatsTagCells_Type = Counter32
_TAtmVtlStatsTagCells_Object = MibTableColumn
tAtmVtlStatsTagCells = _TAtmVtlStatsTagCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 7, 2, 1, 10),
    _TAtmVtlStatsTagCells_Type()
)
tAtmVtlStatsTagCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmVtlStatsTagCells.setStatus("current")
_TAtmCellVclObjs_ObjectIdentity = ObjectIdentity
tAtmCellVclObjs = _TAtmCellVclObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 8)
)
_TAtmCellVclStatisticsTable_Object = MibTable
tAtmCellVclStatisticsTable = _TAtmCellVclStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 8, 1)
)
if mibBuilder.loadTexts:
    tAtmCellVclStatisticsTable.setStatus("current")
_TAtmCellVclStatisticsEntry_Object = MibTableRow
tAtmCellVclStatisticsEntry = _TAtmCellVclStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 8, 1, 1)
)
if mibBuilder.loadTexts:
    tAtmCellVclStatisticsEntry.setStatus("current")
_TAtmCellVclStatsClp0CellsRxd_Type = Counter64
_TAtmCellVclStatsClp0CellsRxd_Object = MibTableColumn
tAtmCellVclStatsClp0CellsRxd = _TAtmCellVclStatsClp0CellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 8, 1, 1, 1),
    _TAtmCellVclStatsClp0CellsRxd_Type()
)
tAtmCellVclStatsClp0CellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCellVclStatsClp0CellsRxd.setStatus("current")
_TAtmCellVclStatsClp0CellsTxd_Type = Counter64
_TAtmCellVclStatsClp0CellsTxd_Object = MibTableColumn
tAtmCellVclStatsClp0CellsTxd = _TAtmCellVclStatsClp0CellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 8, 1, 1, 2),
    _TAtmCellVclStatsClp0CellsTxd_Type()
)
tAtmCellVclStatsClp0CellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCellVclStatsClp0CellsTxd.setStatus("current")
_TAtmCellVclStatsDrpCellsRxd_Type = Counter32
_TAtmCellVclStatsDrpCellsRxd_Object = MibTableColumn
tAtmCellVclStatsDrpCellsRxd = _TAtmCellVclStatsDrpCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 8, 1, 1, 3),
    _TAtmCellVclStatsDrpCellsRxd_Type()
)
tAtmCellVclStatsDrpCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCellVclStatsDrpCellsRxd.setStatus("current")
_TAtmCellVclStatsDrpClp0CellsRxd_Type = Counter32
_TAtmCellVclStatsDrpClp0CellsRxd_Object = MibTableColumn
tAtmCellVclStatsDrpClp0CellsRxd = _TAtmCellVclStatsDrpClp0CellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 8, 1, 1, 4),
    _TAtmCellVclStatsDrpClp0CellsRxd_Type()
)
tAtmCellVclStatsDrpClp0CellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCellVclStatsDrpClp0CellsRxd.setStatus("current")
_TAtmCellVclStatsDrpClp0CellsTxd_Type = Counter32
_TAtmCellVclStatsDrpClp0CellsTxd_Object = MibTableColumn
tAtmCellVclStatsDrpClp0CellsTxd = _TAtmCellVclStatsDrpClp0CellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 8, 1, 1, 5),
    _TAtmCellVclStatsDrpClp0CellsTxd_Type()
)
tAtmCellVclStatsDrpClp0CellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCellVclStatsDrpClp0CellsTxd.setStatus("current")
_TAtmCellVclStatsTagCells_Type = Counter32
_TAtmCellVclStatsTagCells_Object = MibTableColumn
tAtmCellVclStatsTagCells = _TAtmCellVclStatsTagCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 8, 1, 1, 6),
    _TAtmCellVclStatsTagCells_Type()
)
tAtmCellVclStatsTagCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCellVclStatsTagCells.setStatus("current")
_TAtmSystemObjs_ObjectIdentity = ObjectIdentity
tAtmSystemObjs = _TAtmSystemObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 9)
)


class _TAtmSysLlid_Type(AtmLlid):
    """Custom type tAtmSysLlid based on AtmLlid"""
    defaultHexValue = "01000000000000000000000000000000"


_TAtmSysLlid_Object = MibScalar
tAtmSysLlid = _TAtmSysLlid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 9, 1),
    _TAtmSysLlid_Type()
)
tAtmSysLlid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmSysLlid.setStatus("current")


class _TAtmSysOamRetryUp_Type(Integer32):
    """Custom type tAtmSysOamRetryUp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TAtmSysOamRetryUp_Type.__name__ = "Integer32"
_TAtmSysOamRetryUp_Object = MibScalar
tAtmSysOamRetryUp = _TAtmSysOamRetryUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 9, 2),
    _TAtmSysOamRetryUp_Type()
)
tAtmSysOamRetryUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmSysOamRetryUp.setStatus("current")


class _TAtmSysOamRetryDown_Type(Integer32):
    """Custom type tAtmSysOamRetryDown based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TAtmSysOamRetryDown_Type.__name__ = "Integer32"
_TAtmSysOamRetryDown_Object = MibScalar
tAtmSysOamRetryDown = _TAtmSysOamRetryDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 9, 3),
    _TAtmSysOamRetryDown_Type()
)
tAtmSysOamRetryDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmSysOamRetryDown.setStatus("current")


class _TAtmSysOamLoopbackPeriod_Type(Integer32):
    """Custom type tAtmSysOamLoopbackPeriod based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_TAtmSysOamLoopbackPeriod_Type.__name__ = "Integer32"
_TAtmSysOamLoopbackPeriod_Object = MibScalar
tAtmSysOamLoopbackPeriod = _TAtmSysOamLoopbackPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 9, 4),
    _TAtmSysOamLoopbackPeriod_Type()
)
tAtmSysOamLoopbackPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmSysOamLoopbackPeriod.setStatus("current")
if mibBuilder.loadTexts:
    tAtmSysOamLoopbackPeriod.setUnits("seconds")
_TAtmIlmiLinkObjs_ObjectIdentity = ObjectIdentity
tAtmIlmiLinkObjs = _TAtmIlmiLinkObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10)
)
_TAtmIlmiLinkTable_Object = MibTable
tAtmIlmiLinkTable = _TAtmIlmiLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1)
)
if mibBuilder.loadTexts:
    tAtmIlmiLinkTable.setStatus("current")
_TAtmIlmiLinkEntry_Object = MibTableRow
tAtmIlmiLinkEntry = _TAtmIlmiLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1)
)
tAtmIlmiLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tAtmIlmiLinkEntry.setStatus("current")
_TAtmIlmiLinkRowStatus_Type = RowStatus
_TAtmIlmiLinkRowStatus_Object = MibTableColumn
tAtmIlmiLinkRowStatus = _TAtmIlmiLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 1),
    _TAtmIlmiLinkRowStatus_Type()
)
tAtmIlmiLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmIlmiLinkRowStatus.setStatus("current")
_TAtmIlmiLinkLastChanged_Type = TimeStamp
_TAtmIlmiLinkLastChanged_Object = MibTableColumn
tAtmIlmiLinkLastChanged = _TAtmIlmiLinkLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 2),
    _TAtmIlmiLinkLastChanged_Type()
)
tAtmIlmiLinkLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkLastChanged.setStatus("current")


class _TAtmIlmiLinkAdminStatus_Type(Integer32):
    """Custom type tAtmIlmiLinkAdminStatus based on Integer32"""
    defaultValue = 2

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


_TAtmIlmiLinkAdminStatus_Type.__name__ = "Integer32"
_TAtmIlmiLinkAdminStatus_Object = MibTableColumn
tAtmIlmiLinkAdminStatus = _TAtmIlmiLinkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 3),
    _TAtmIlmiLinkAdminStatus_Type()
)
tAtmIlmiLinkAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmIlmiLinkAdminStatus.setStatus("current")


class _TAtmIlmiLinkOperStatus_Type(Integer32):
    """Custom type tAtmIlmiLinkOperStatus based on Integer32"""
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


_TAtmIlmiLinkOperStatus_Type.__name__ = "Integer32"
_TAtmIlmiLinkOperStatus_Object = MibTableColumn
tAtmIlmiLinkOperStatus = _TAtmIlmiLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 4),
    _TAtmIlmiLinkOperStatus_Type()
)
tAtmIlmiLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkOperStatus.setStatus("current")


class _TAtmIlmiLinkVpi_Type(AtmVpIdentifier):
    """Custom type tAtmIlmiLinkVpi based on AtmVpIdentifier"""
    defaultValue = 0


_TAtmIlmiLinkVpi_Object = MibTableColumn
tAtmIlmiLinkVpi = _TAtmIlmiLinkVpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 5),
    _TAtmIlmiLinkVpi_Type()
)
tAtmIlmiLinkVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmIlmiLinkVpi.setStatus("current")


class _TAtmIlmiLinkVci_Type(AtmVcIdentifier):
    """Custom type tAtmIlmiLinkVci based on AtmVcIdentifier"""
    defaultValue = 16


_TAtmIlmiLinkVci_Object = MibTableColumn
tAtmIlmiLinkVci = _TAtmIlmiLinkVci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 6),
    _TAtmIlmiLinkVci_Type()
)
tAtmIlmiLinkVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmIlmiLinkVci.setStatus("current")


class _TAtmIlmiLinkFsmState_Type(Integer32):
    """Custom type tAtmIlmiLinkFsmState based on Integer32"""
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
        *(("configuring", 4),
          ("establishing", 3),
          ("linkFailing", 2),
          ("registeringAddresses", 8),
          ("registeringNetworkPrefixes", 6),
          ("retrievingAddresses", 7),
          ("retrievingNetworkPrefixes", 5),
          ("stopped", 1),
          ("verifying", 9))
    )


_TAtmIlmiLinkFsmState_Type.__name__ = "Integer32"
_TAtmIlmiLinkFsmState_Object = MibTableColumn
tAtmIlmiLinkFsmState = _TAtmIlmiLinkFsmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 7),
    _TAtmIlmiLinkFsmState_Type()
)
tAtmIlmiLinkFsmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkFsmState.setStatus("current")


class _TAtmIlmiLinkReceiveTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type tAtmIlmiLinkReceiveTrafficDescrIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 1


_TAtmIlmiLinkReceiveTrafficDescrIndex_Object = MibTableColumn
tAtmIlmiLinkReceiveTrafficDescrIndex = _TAtmIlmiLinkReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 8),
    _TAtmIlmiLinkReceiveTrafficDescrIndex_Type()
)
tAtmIlmiLinkReceiveTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmIlmiLinkReceiveTrafficDescrIndex.setStatus("current")


class _TAtmIlmiLinkTransmitTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type tAtmIlmiLinkTransmitTrafficDescrIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 1


_TAtmIlmiLinkTransmitTrafficDescrIndex_Object = MibTableColumn
tAtmIlmiLinkTransmitTrafficDescrIndex = _TAtmIlmiLinkTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 9),
    _TAtmIlmiLinkTransmitTrafficDescrIndex_Type()
)
tAtmIlmiLinkTransmitTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmIlmiLinkTransmitTrafficDescrIndex.setStatus("current")


class _TAtmIlmiLinkEstablishConPollIntvl_Type(Integer32):
    """Custom type tAtmIlmiLinkEstablishConPollIntvl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TAtmIlmiLinkEstablishConPollIntvl_Type.__name__ = "Integer32"
_TAtmIlmiLinkEstablishConPollIntvl_Object = MibTableColumn
tAtmIlmiLinkEstablishConPollIntvl = _TAtmIlmiLinkEstablishConPollIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 10),
    _TAtmIlmiLinkEstablishConPollIntvl_Type()
)
tAtmIlmiLinkEstablishConPollIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmIlmiLinkEstablishConPollIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tAtmIlmiLinkEstablishConPollIntvl.setUnits("seconds")


class _TAtmIlmiLinkCheckConPollIntvl_Type(Integer32):
    """Custom type tAtmIlmiLinkCheckConPollIntvl based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TAtmIlmiLinkCheckConPollIntvl_Type.__name__ = "Integer32"
_TAtmIlmiLinkCheckConPollIntvl_Object = MibTableColumn
tAtmIlmiLinkCheckConPollIntvl = _TAtmIlmiLinkCheckConPollIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 11),
    _TAtmIlmiLinkCheckConPollIntvl_Type()
)
tAtmIlmiLinkCheckConPollIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmIlmiLinkCheckConPollIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tAtmIlmiLinkCheckConPollIntvl.setUnits("seconds")


class _TAtmIlmiLinkConPollInactFactor_Type(Integer32):
    """Custom type tAtmIlmiLinkConPollInactFactor based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TAtmIlmiLinkConPollInactFactor_Type.__name__ = "Integer32"
_TAtmIlmiLinkConPollInactFactor_Object = MibTableColumn
tAtmIlmiLinkConPollInactFactor = _TAtmIlmiLinkConPollInactFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 12),
    _TAtmIlmiLinkConPollInactFactor_Type()
)
tAtmIlmiLinkConPollInactFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmIlmiLinkConPollInactFactor.setStatus("current")
_TAtmIlmiLinkUniType_Type = AtmIlmiLinkUniType
_TAtmIlmiLinkUniType_Object = MibTableColumn
tAtmIlmiLinkUniType = _TAtmIlmiLinkUniType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 13),
    _TAtmIlmiLinkUniType_Type()
)
tAtmIlmiLinkUniType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkUniType.setStatus("current")
_TAtmIlmiLinkDeviceType_Type = AtmIlmiLinkDeviceType
_TAtmIlmiLinkDeviceType_Object = MibTableColumn
tAtmIlmiLinkDeviceType = _TAtmIlmiLinkDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 14),
    _TAtmIlmiLinkDeviceType_Type()
)
tAtmIlmiLinkDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkDeviceType.setStatus("current")


class _TAtmIlmiLinkVersion_Type(AtmIlmiLinkVersion):
    """Custom type tAtmIlmiLinkVersion based on AtmIlmiLinkVersion"""


_TAtmIlmiLinkVersion_Object = MibTableColumn
tAtmIlmiLinkVersion = _TAtmIlmiLinkVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 15),
    _TAtmIlmiLinkVersion_Type()
)
tAtmIlmiLinkVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmIlmiLinkVersion.setStatus("current")


class _TAtmIlmiLinkImeType_Type(AtmIlmiLinkImeType):
    """Custom type tAtmIlmiLinkImeType based on AtmIlmiLinkImeType"""


_TAtmIlmiLinkImeType_Object = MibTableColumn
tAtmIlmiLinkImeType = _TAtmIlmiLinkImeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 16),
    _TAtmIlmiLinkImeType_Type()
)
tAtmIlmiLinkImeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmIlmiLinkImeType.setStatus("current")
_TAtmIlmiLinkNegotiatedVersion_Type = AtmIlmiLinkVersion
_TAtmIlmiLinkNegotiatedVersion_Object = MibTableColumn
tAtmIlmiLinkNegotiatedVersion = _TAtmIlmiLinkNegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 17),
    _TAtmIlmiLinkNegotiatedVersion_Type()
)
tAtmIlmiLinkNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkNegotiatedVersion.setStatus("current")
_TAtmIlmiLinkNegotiatedImeType_Type = AtmIlmiLinkImeType
_TAtmIlmiLinkNegotiatedImeType_Object = MibTableColumn
tAtmIlmiLinkNegotiatedImeType = _TAtmIlmiLinkNegotiatedImeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 18),
    _TAtmIlmiLinkNegotiatedImeType_Type()
)
tAtmIlmiLinkNegotiatedImeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkNegotiatedImeType.setStatus("current")


class _TAtmIlmiLinkNeighborIfIdentifier_Type(Integer32):
    """Custom type tAtmIlmiLinkNeighborIfIdentifier based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TAtmIlmiLinkNeighborIfIdentifier_Type.__name__ = "Integer32"
_TAtmIlmiLinkNeighborIfIdentifier_Object = MibTableColumn
tAtmIlmiLinkNeighborIfIdentifier = _TAtmIlmiLinkNeighborIfIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 19),
    _TAtmIlmiLinkNeighborIfIdentifier_Type()
)
tAtmIlmiLinkNeighborIfIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkNeighborIfIdentifier.setStatus("current")


class _TAtmIlmiLinkNeighborSystemIdentifier_Type(OctetString):
    """Custom type tAtmIlmiLinkNeighborSystemIdentifier based on OctetString"""
    defaultHexValue = "00000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TAtmIlmiLinkNeighborSystemIdentifier_Type.__name__ = "OctetString"
_TAtmIlmiLinkNeighborSystemIdentifier_Object = MibTableColumn
tAtmIlmiLinkNeighborSystemIdentifier = _TAtmIlmiLinkNeighborSystemIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 20),
    _TAtmIlmiLinkNeighborSystemIdentifier_Type()
)
tAtmIlmiLinkNeighborSystemIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkNeighborSystemIdentifier.setStatus("current")


class _TAtmIlmiLinkNeighborUniType_Type(AtmIlmiLinkUniType):
    """Custom type tAtmIlmiLinkNeighborUniType based on AtmIlmiLinkUniType"""


_TAtmIlmiLinkNeighborUniType_Object = MibTableColumn
tAtmIlmiLinkNeighborUniType = _TAtmIlmiLinkNeighborUniType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 21),
    _TAtmIlmiLinkNeighborUniType_Type()
)
tAtmIlmiLinkNeighborUniType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkNeighborUniType.setStatus("current")


class _TAtmIlmiLinkNeighborDeviceType_Type(AtmIlmiLinkDeviceType):
    """Custom type tAtmIlmiLinkNeighborDeviceType based on AtmIlmiLinkDeviceType"""


_TAtmIlmiLinkNeighborDeviceType_Object = MibTableColumn
tAtmIlmiLinkNeighborDeviceType = _TAtmIlmiLinkNeighborDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 22),
    _TAtmIlmiLinkNeighborDeviceType_Type()
)
tAtmIlmiLinkNeighborDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkNeighborDeviceType.setStatus("current")


class _TAtmIlmiLinkNeighborVersion_Type(AtmIlmiLinkVersion):
    """Custom type tAtmIlmiLinkNeighborVersion based on AtmIlmiLinkVersion"""


_TAtmIlmiLinkNeighborVersion_Object = MibTableColumn
tAtmIlmiLinkNeighborVersion = _TAtmIlmiLinkNeighborVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 23),
    _TAtmIlmiLinkNeighborVersion_Type()
)
tAtmIlmiLinkNeighborVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkNeighborVersion.setStatus("current")


class _TAtmIlmiLinkNeighborMaxVpcs_Type(Integer32):
    """Custom type tAtmIlmiLinkNeighborMaxVpcs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TAtmIlmiLinkNeighborMaxVpcs_Type.__name__ = "Integer32"
_TAtmIlmiLinkNeighborMaxVpcs_Object = MibTableColumn
tAtmIlmiLinkNeighborMaxVpcs = _TAtmIlmiLinkNeighborMaxVpcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 24),
    _TAtmIlmiLinkNeighborMaxVpcs_Type()
)
tAtmIlmiLinkNeighborMaxVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkNeighborMaxVpcs.setStatus("current")


class _TAtmIlmiLinkNeighborMaxVccs_Type(Integer32):
    """Custom type tAtmIlmiLinkNeighborMaxVccs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_TAtmIlmiLinkNeighborMaxVccs_Type.__name__ = "Integer32"
_TAtmIlmiLinkNeighborMaxVccs_Object = MibTableColumn
tAtmIlmiLinkNeighborMaxVccs = _TAtmIlmiLinkNeighborMaxVccs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 25),
    _TAtmIlmiLinkNeighborMaxVccs_Type()
)
tAtmIlmiLinkNeighborMaxVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkNeighborMaxVccs.setStatus("current")


class _TAtmIlmiLinkNeighborMaxVpiBits_Type(Integer32):
    """Custom type tAtmIlmiLinkNeighborMaxVpiBits based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_TAtmIlmiLinkNeighborMaxVpiBits_Type.__name__ = "Integer32"
_TAtmIlmiLinkNeighborMaxVpiBits_Object = MibTableColumn
tAtmIlmiLinkNeighborMaxVpiBits = _TAtmIlmiLinkNeighborMaxVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 26),
    _TAtmIlmiLinkNeighborMaxVpiBits_Type()
)
tAtmIlmiLinkNeighborMaxVpiBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkNeighborMaxVpiBits.setStatus("current")


class _TAtmIlmiLinkNeighborMaxVciBits_Type(Integer32):
    """Custom type tAtmIlmiLinkNeighborMaxVciBits based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TAtmIlmiLinkNeighborMaxVciBits_Type.__name__ = "Integer32"
_TAtmIlmiLinkNeighborMaxVciBits_Object = MibTableColumn
tAtmIlmiLinkNeighborMaxVciBits = _TAtmIlmiLinkNeighborMaxVciBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 1, 1, 27),
    _TAtmIlmiLinkNeighborMaxVciBits_Type()
)
tAtmIlmiLinkNeighborMaxVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkNeighborMaxVciBits.setStatus("current")
_TAtmIlmiLinkStatisticsTable_Object = MibTable
tAtmIlmiLinkStatisticsTable = _TAtmIlmiLinkStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2)
)
if mibBuilder.loadTexts:
    tAtmIlmiLinkStatisticsTable.setStatus("current")
_TAtmIlmiLinkStatisticsEntry_Object = MibTableRow
tAtmIlmiLinkStatisticsEntry = _TAtmIlmiLinkStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1)
)
tAtmIlmiLinkStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tAtmIlmiLinkStatisticsEntry.setStatus("current")
_TAtmIlmiLinkOutPdus_Type = Counter32
_TAtmIlmiLinkOutPdus_Object = MibTableColumn
tAtmIlmiLinkOutPdus = _TAtmIlmiLinkOutPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 1),
    _TAtmIlmiLinkOutPdus_Type()
)
tAtmIlmiLinkOutPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkOutPdus.setStatus("current")
_TAtmIlmiLinkOutGetRequestPdus_Type = Counter32
_TAtmIlmiLinkOutGetRequestPdus_Object = MibTableColumn
tAtmIlmiLinkOutGetRequestPdus = _TAtmIlmiLinkOutGetRequestPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 2),
    _TAtmIlmiLinkOutGetRequestPdus_Type()
)
tAtmIlmiLinkOutGetRequestPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkOutGetRequestPdus.setStatus("current")
_TAtmIlmiLinkOutGetNextRequestPdus_Type = Counter32
_TAtmIlmiLinkOutGetNextRequestPdus_Object = MibTableColumn
tAtmIlmiLinkOutGetNextRequestPdus = _TAtmIlmiLinkOutGetNextRequestPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 3),
    _TAtmIlmiLinkOutGetNextRequestPdus_Type()
)
tAtmIlmiLinkOutGetNextRequestPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkOutGetNextRequestPdus.setStatus("current")
_TAtmIlmiLinkOutSetRequestPdus_Type = Counter32
_TAtmIlmiLinkOutSetRequestPdus_Object = MibTableColumn
tAtmIlmiLinkOutSetRequestPdus = _TAtmIlmiLinkOutSetRequestPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 4),
    _TAtmIlmiLinkOutSetRequestPdus_Type()
)
tAtmIlmiLinkOutSetRequestPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkOutSetRequestPdus.setStatus("current")
_TAtmIlmiLinkOutGetResponsePdus_Type = Counter32
_TAtmIlmiLinkOutGetResponsePdus_Object = MibTableColumn
tAtmIlmiLinkOutGetResponsePdus = _TAtmIlmiLinkOutGetResponsePdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 5),
    _TAtmIlmiLinkOutGetResponsePdus_Type()
)
tAtmIlmiLinkOutGetResponsePdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkOutGetResponsePdus.setStatus("current")
_TAtmIlmiLinkOutTrapPdus_Type = Counter32
_TAtmIlmiLinkOutTrapPdus_Object = MibTableColumn
tAtmIlmiLinkOutTrapPdus = _TAtmIlmiLinkOutTrapPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 6),
    _TAtmIlmiLinkOutTrapPdus_Type()
)
tAtmIlmiLinkOutTrapPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkOutTrapPdus.setStatus("current")
_TAtmIlmiLinkOutTooBigErrors_Type = Counter32
_TAtmIlmiLinkOutTooBigErrors_Object = MibTableColumn
tAtmIlmiLinkOutTooBigErrors = _TAtmIlmiLinkOutTooBigErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 7),
    _TAtmIlmiLinkOutTooBigErrors_Type()
)
tAtmIlmiLinkOutTooBigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkOutTooBigErrors.setStatus("current")
_TAtmIlmiLinkOutNoSuchNameErrors_Type = Counter32
_TAtmIlmiLinkOutNoSuchNameErrors_Object = MibTableColumn
tAtmIlmiLinkOutNoSuchNameErrors = _TAtmIlmiLinkOutNoSuchNameErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 8),
    _TAtmIlmiLinkOutNoSuchNameErrors_Type()
)
tAtmIlmiLinkOutNoSuchNameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkOutNoSuchNameErrors.setStatus("current")
_TAtmIlmiLinkOutBadValueErrors_Type = Counter32
_TAtmIlmiLinkOutBadValueErrors_Object = MibTableColumn
tAtmIlmiLinkOutBadValueErrors = _TAtmIlmiLinkOutBadValueErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 9),
    _TAtmIlmiLinkOutBadValueErrors_Type()
)
tAtmIlmiLinkOutBadValueErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkOutBadValueErrors.setStatus("current")
_TAtmIlmiLinkOutReadOnlyErrors_Type = Counter32
_TAtmIlmiLinkOutReadOnlyErrors_Object = MibTableColumn
tAtmIlmiLinkOutReadOnlyErrors = _TAtmIlmiLinkOutReadOnlyErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 10),
    _TAtmIlmiLinkOutReadOnlyErrors_Type()
)
tAtmIlmiLinkOutReadOnlyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkOutReadOnlyErrors.setStatus("current")
_TAtmIlmiLinkOutGeneralErrors_Type = Counter32
_TAtmIlmiLinkOutGeneralErrors_Object = MibTableColumn
tAtmIlmiLinkOutGeneralErrors = _TAtmIlmiLinkOutGeneralErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 11),
    _TAtmIlmiLinkOutGeneralErrors_Type()
)
tAtmIlmiLinkOutGeneralErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkOutGeneralErrors.setStatus("current")
_TAtmIlmiLinkInPdus_Type = Counter32
_TAtmIlmiLinkInPdus_Object = MibTableColumn
tAtmIlmiLinkInPdus = _TAtmIlmiLinkInPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 12),
    _TAtmIlmiLinkInPdus_Type()
)
tAtmIlmiLinkInPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkInPdus.setStatus("current")
_TAtmIlmiLinkInGetRequestPdus_Type = Counter32
_TAtmIlmiLinkInGetRequestPdus_Object = MibTableColumn
tAtmIlmiLinkInGetRequestPdus = _TAtmIlmiLinkInGetRequestPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 13),
    _TAtmIlmiLinkInGetRequestPdus_Type()
)
tAtmIlmiLinkInGetRequestPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkInGetRequestPdus.setStatus("current")
_TAtmIlmiLinkInGetNextRequestPdus_Type = Counter32
_TAtmIlmiLinkInGetNextRequestPdus_Object = MibTableColumn
tAtmIlmiLinkInGetNextRequestPdus = _TAtmIlmiLinkInGetNextRequestPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 14),
    _TAtmIlmiLinkInGetNextRequestPdus_Type()
)
tAtmIlmiLinkInGetNextRequestPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkInGetNextRequestPdus.setStatus("current")
_TAtmIlmiLinkInSetRequestPdus_Type = Counter32
_TAtmIlmiLinkInSetRequestPdus_Object = MibTableColumn
tAtmIlmiLinkInSetRequestPdus = _TAtmIlmiLinkInSetRequestPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 15),
    _TAtmIlmiLinkInSetRequestPdus_Type()
)
tAtmIlmiLinkInSetRequestPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkInSetRequestPdus.setStatus("current")
_TAtmIlmiLinkInGetResponsePdus_Type = Counter32
_TAtmIlmiLinkInGetResponsePdus_Object = MibTableColumn
tAtmIlmiLinkInGetResponsePdus = _TAtmIlmiLinkInGetResponsePdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 16),
    _TAtmIlmiLinkInGetResponsePdus_Type()
)
tAtmIlmiLinkInGetResponsePdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkInGetResponsePdus.setStatus("current")
_TAtmIlmiLinkInTrapPdus_Type = Counter32
_TAtmIlmiLinkInTrapPdus_Object = MibTableColumn
tAtmIlmiLinkInTrapPdus = _TAtmIlmiLinkInTrapPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 17),
    _TAtmIlmiLinkInTrapPdus_Type()
)
tAtmIlmiLinkInTrapPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkInTrapPdus.setStatus("current")
_TAtmIlmiLinkInTooBigErrors_Type = Counter32
_TAtmIlmiLinkInTooBigErrors_Object = MibTableColumn
tAtmIlmiLinkInTooBigErrors = _TAtmIlmiLinkInTooBigErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 18),
    _TAtmIlmiLinkInTooBigErrors_Type()
)
tAtmIlmiLinkInTooBigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkInTooBigErrors.setStatus("current")
_TAtmIlmiLinkInNoSuchNameErrors_Type = Counter32
_TAtmIlmiLinkInNoSuchNameErrors_Object = MibTableColumn
tAtmIlmiLinkInNoSuchNameErrors = _TAtmIlmiLinkInNoSuchNameErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 19),
    _TAtmIlmiLinkInNoSuchNameErrors_Type()
)
tAtmIlmiLinkInNoSuchNameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkInNoSuchNameErrors.setStatus("current")
_TAtmIlmiLinkInBadValueErrors_Type = Counter32
_TAtmIlmiLinkInBadValueErrors_Object = MibTableColumn
tAtmIlmiLinkInBadValueErrors = _TAtmIlmiLinkInBadValueErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 20),
    _TAtmIlmiLinkInBadValueErrors_Type()
)
tAtmIlmiLinkInBadValueErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkInBadValueErrors.setStatus("current")
_TAtmIlmiLinkInReadOnlyErrors_Type = Counter32
_TAtmIlmiLinkInReadOnlyErrors_Object = MibTableColumn
tAtmIlmiLinkInReadOnlyErrors = _TAtmIlmiLinkInReadOnlyErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 21),
    _TAtmIlmiLinkInReadOnlyErrors_Type()
)
tAtmIlmiLinkInReadOnlyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkInReadOnlyErrors.setStatus("current")
_TAtmIlmiLinkInGeneralErrors_Type = Counter32
_TAtmIlmiLinkInGeneralErrors_Object = MibTableColumn
tAtmIlmiLinkInGeneralErrors = _TAtmIlmiLinkInGeneralErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 22),
    _TAtmIlmiLinkInGeneralErrors_Type()
)
tAtmIlmiLinkInGeneralErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkInGeneralErrors.setStatus("current")
_TAtmIlmiLinkInInvalidSnmpVersionPdus_Type = Counter32
_TAtmIlmiLinkInInvalidSnmpVersionPdus_Object = MibTableColumn
tAtmIlmiLinkInInvalidSnmpVersionPdus = _TAtmIlmiLinkInInvalidSnmpVersionPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 23),
    _TAtmIlmiLinkInInvalidSnmpVersionPdus_Type()
)
tAtmIlmiLinkInInvalidSnmpVersionPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkInInvalidSnmpVersionPdus.setStatus("current")
_TAtmIlmiLinkInInvalidSnmpCommunityStringPdus_Type = Counter32
_TAtmIlmiLinkInInvalidSnmpCommunityStringPdus_Object = MibTableColumn
tAtmIlmiLinkInInvalidSnmpCommunityStringPdus = _TAtmIlmiLinkInInvalidSnmpCommunityStringPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 24),
    _TAtmIlmiLinkInInvalidSnmpCommunityStringPdus_Type()
)
tAtmIlmiLinkInInvalidSnmpCommunityStringPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkInInvalidSnmpCommunityStringPdus.setStatus("current")
_TAtmIlmiLinkInInvalidSnmpFormatPdus_Type = Counter32
_TAtmIlmiLinkInInvalidSnmpFormatPdus_Object = MibTableColumn
tAtmIlmiLinkInInvalidSnmpFormatPdus = _TAtmIlmiLinkInInvalidSnmpFormatPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 10, 2, 1, 25),
    _TAtmIlmiLinkInInvalidSnmpFormatPdus_Type()
)
tAtmIlmiLinkInInvalidSnmpFormatPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmIlmiLinkInInvalidSnmpFormatPdus.setStatus("current")
_TAtmTCSublayerObjs_ObjectIdentity = ObjectIdentity
tAtmTCSublayerObjs = _TAtmTCSublayerObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 11)
)
_TAtmTCSublayerTable_Object = MibTable
tAtmTCSublayerTable = _TAtmTCSublayerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 11, 1)
)
if mibBuilder.loadTexts:
    tAtmTCSublayerTable.setStatus("current")
_TAtmTCSublayerEntry_Object = MibTableRow
tAtmTCSublayerEntry = _TAtmTCSublayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 11, 1, 1)
)
if mibBuilder.loadTexts:
    tAtmTCSublayerEntry.setStatus("current")
_TAtmTCSublayerHecErrors_Type = Counter32
_TAtmTCSublayerHecErrors_Object = MibTableColumn
tAtmTCSublayerHecErrors = _TAtmTCSublayerHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 11, 1, 1, 1),
    _TAtmTCSublayerHecErrors_Type()
)
tAtmTCSublayerHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmTCSublayerHecErrors.setStatus("current")
_TAtmTCSublayerHecErrorsFixed_Type = Counter32
_TAtmTCSublayerHecErrorsFixed_Object = MibTableColumn
tAtmTCSublayerHecErrorsFixed = _TAtmTCSublayerHecErrorsFixed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 11, 1, 1, 2),
    _TAtmTCSublayerHecErrorsFixed_Type()
)
tAtmTCSublayerHecErrorsFixed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmTCSublayerHecErrorsFixed.setStatus("current")
_TAtmCpObjs_ObjectIdentity = ObjectIdentity
tAtmCpObjs = _TAtmCpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12)
)
_TAtmCpStatisticsTable_Object = MibTable
tAtmCpStatisticsTable = _TAtmCpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1)
)
if mibBuilder.loadTexts:
    tAtmCpStatisticsTable.setStatus("current")
_TAtmCpStatisticsEntry_Object = MibTableRow
tAtmCpStatisticsEntry = _TAtmCpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1, 1)
)
tAtmCpStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TIMETRA-CONN-PROF-MIB", "tmnxConnProfId"),
)
if mibBuilder.loadTexts:
    tAtmCpStatisticsEntry.setStatus("current")
_TAtmCpStatsTotalCellsRxd_Type = Counter64
_TAtmCpStatsTotalCellsRxd_Object = MibTableColumn
tAtmCpStatsTotalCellsRxd = _TAtmCpStatsTotalCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1, 1, 1),
    _TAtmCpStatsTotalCellsRxd_Type()
)
tAtmCpStatsTotalCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCpStatsTotalCellsRxd.setStatus("current")
if mibBuilder.loadTexts:
    tAtmCpStatsTotalCellsRxd.setUnits("cells")
_TAtmCpStatsTotalCellsRxdLo_Type = Counter32
_TAtmCpStatsTotalCellsRxdLo_Object = MibTableColumn
tAtmCpStatsTotalCellsRxdLo = _TAtmCpStatsTotalCellsRxdLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1, 1, 2),
    _TAtmCpStatsTotalCellsRxdLo_Type()
)
tAtmCpStatsTotalCellsRxdLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCpStatsTotalCellsRxdLo.setStatus("current")
if mibBuilder.loadTexts:
    tAtmCpStatsTotalCellsRxdLo.setUnits("cells")
_TAtmCpStatsTotalCellsRxdHi_Type = Counter32
_TAtmCpStatsTotalCellsRxdHi_Object = MibTableColumn
tAtmCpStatsTotalCellsRxdHi = _TAtmCpStatsTotalCellsRxdHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1, 1, 3),
    _TAtmCpStatsTotalCellsRxdHi_Type()
)
tAtmCpStatsTotalCellsRxdHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCpStatsTotalCellsRxdHi.setStatus("current")
if mibBuilder.loadTexts:
    tAtmCpStatsTotalCellsRxdHi.setUnits("cells")
_TAtmCpStatsTotalCellsTxd_Type = Counter64
_TAtmCpStatsTotalCellsTxd_Object = MibTableColumn
tAtmCpStatsTotalCellsTxd = _TAtmCpStatsTotalCellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1, 1, 4),
    _TAtmCpStatsTotalCellsTxd_Type()
)
tAtmCpStatsTotalCellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCpStatsTotalCellsTxd.setStatus("current")
if mibBuilder.loadTexts:
    tAtmCpStatsTotalCellsTxd.setUnits("cells")
_TAtmCpStatsTotalCellsTxdLo_Type = Counter32
_TAtmCpStatsTotalCellsTxdLo_Object = MibTableColumn
tAtmCpStatsTotalCellsTxdLo = _TAtmCpStatsTotalCellsTxdLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1, 1, 5),
    _TAtmCpStatsTotalCellsTxdLo_Type()
)
tAtmCpStatsTotalCellsTxdLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCpStatsTotalCellsTxdLo.setStatus("current")
if mibBuilder.loadTexts:
    tAtmCpStatsTotalCellsTxdLo.setUnits("cells")
_TAtmCpStatsTotalCellsTxdHi_Type = Counter32
_TAtmCpStatsTotalCellsTxdHi_Object = MibTableColumn
tAtmCpStatsTotalCellsTxdHi = _TAtmCpStatsTotalCellsTxdHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1, 1, 6),
    _TAtmCpStatsTotalCellsTxdHi_Type()
)
tAtmCpStatsTotalCellsTxdHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCpStatsTotalCellsTxdHi.setStatus("current")
if mibBuilder.loadTexts:
    tAtmCpStatsTotalCellsTxdHi.setUnits("cells")
_TAtmCpStatsClp0CellsRxd_Type = Counter64
_TAtmCpStatsClp0CellsRxd_Object = MibTableColumn
tAtmCpStatsClp0CellsRxd = _TAtmCpStatsClp0CellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1, 1, 7),
    _TAtmCpStatsClp0CellsRxd_Type()
)
tAtmCpStatsClp0CellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCpStatsClp0CellsRxd.setStatus("current")
if mibBuilder.loadTexts:
    tAtmCpStatsClp0CellsRxd.setUnits("cells")
_TAtmCpStatsClp0CellsRxdLo_Type = Counter32
_TAtmCpStatsClp0CellsRxdLo_Object = MibTableColumn
tAtmCpStatsClp0CellsRxdLo = _TAtmCpStatsClp0CellsRxdLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1, 1, 8),
    _TAtmCpStatsClp0CellsRxdLo_Type()
)
tAtmCpStatsClp0CellsRxdLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCpStatsClp0CellsRxdLo.setStatus("current")
if mibBuilder.loadTexts:
    tAtmCpStatsClp0CellsRxdLo.setUnits("cells")
_TAtmCpStatsClp0CellsRxdHi_Type = Counter32
_TAtmCpStatsClp0CellsRxdHi_Object = MibTableColumn
tAtmCpStatsClp0CellsRxdHi = _TAtmCpStatsClp0CellsRxdHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1, 1, 9),
    _TAtmCpStatsClp0CellsRxdHi_Type()
)
tAtmCpStatsClp0CellsRxdHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCpStatsClp0CellsRxdHi.setStatus("current")
if mibBuilder.loadTexts:
    tAtmCpStatsClp0CellsRxdHi.setUnits("cells")
_TAtmCpStatsClp0CellsTxd_Type = Counter64
_TAtmCpStatsClp0CellsTxd_Object = MibTableColumn
tAtmCpStatsClp0CellsTxd = _TAtmCpStatsClp0CellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1, 1, 10),
    _TAtmCpStatsClp0CellsTxd_Type()
)
tAtmCpStatsClp0CellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCpStatsClp0CellsTxd.setStatus("current")
if mibBuilder.loadTexts:
    tAtmCpStatsClp0CellsTxd.setUnits("cells")
_TAtmCpStatsClp0CellsTxdLo_Type = Counter32
_TAtmCpStatsClp0CellsTxdLo_Object = MibTableColumn
tAtmCpStatsClp0CellsTxdLo = _TAtmCpStatsClp0CellsTxdLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1, 1, 11),
    _TAtmCpStatsClp0CellsTxdLo_Type()
)
tAtmCpStatsClp0CellsTxdLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCpStatsClp0CellsTxdLo.setStatus("current")
if mibBuilder.loadTexts:
    tAtmCpStatsClp0CellsTxdLo.setUnits("cells")
_TAtmCpStatsClp0CellsTxdHi_Type = Counter32
_TAtmCpStatsClp0CellsTxdHi_Object = MibTableColumn
tAtmCpStatsClp0CellsTxdHi = _TAtmCpStatsClp0CellsTxdHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1, 1, 12),
    _TAtmCpStatsClp0CellsTxdHi_Type()
)
tAtmCpStatsClp0CellsTxdHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCpStatsClp0CellsTxdHi.setStatus("current")
if mibBuilder.loadTexts:
    tAtmCpStatsClp0CellsTxdHi.setUnits("cells")
_TAtmCpStatsDrpCellsRxd_Type = Counter32
_TAtmCpStatsDrpCellsRxd_Object = MibTableColumn
tAtmCpStatsDrpCellsRxd = _TAtmCpStatsDrpCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1, 1, 13),
    _TAtmCpStatsDrpCellsRxd_Type()
)
tAtmCpStatsDrpCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCpStatsDrpCellsRxd.setStatus("current")
if mibBuilder.loadTexts:
    tAtmCpStatsDrpCellsRxd.setUnits("cells")
_TAtmCpStatsDrpClp0CellsRxd_Type = Counter32
_TAtmCpStatsDrpClp0CellsRxd_Object = MibTableColumn
tAtmCpStatsDrpClp0CellsRxd = _TAtmCpStatsDrpClp0CellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1, 1, 14),
    _TAtmCpStatsDrpClp0CellsRxd_Type()
)
tAtmCpStatsDrpClp0CellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCpStatsDrpClp0CellsRxd.setStatus("current")
if mibBuilder.loadTexts:
    tAtmCpStatsDrpClp0CellsRxd.setUnits("cells")
_TAtmCpStatsDrpClp0CellsTxd_Type = Counter32
_TAtmCpStatsDrpClp0CellsTxd_Object = MibTableColumn
tAtmCpStatsDrpClp0CellsTxd = _TAtmCpStatsDrpClp0CellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1, 1, 15),
    _TAtmCpStatsDrpClp0CellsTxd_Type()
)
tAtmCpStatsDrpClp0CellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCpStatsDrpClp0CellsTxd.setStatus("current")
if mibBuilder.loadTexts:
    tAtmCpStatsDrpClp0CellsTxd.setUnits("cells")
_TAtmCpStatsTagCells_Type = Counter32
_TAtmCpStatsTagCells_Object = MibTableColumn
tAtmCpStatsTagCells = _TAtmCpStatsTagCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 27, 12, 1, 1, 16),
    _TAtmCpStatsTagCells_Type()
)
tAtmCpStatsTagCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmCpStatsTagCells.setStatus("current")
if mibBuilder.loadTexts:
    tAtmCpStatsTagCells.setUnits("cells")
_TmnxAtmNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxAtmNotifyPrefix = _TmnxAtmNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 27)
)
_TAtmNotifications_ObjectIdentity = ObjectIdentity
tAtmNotifications = _TAtmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 27, 0)
)
atmInterfaceConfEntry.registerAugmentions(
    ("TIMETRA-ATM-MIB",
     "tAtmIntfConfEntry")
)
tAtmIntfConfEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())
atmVclEntry.registerAugmentions(
    ("TIMETRA-ATM-MIB",
     "tAtmVclInfoEntry")
)
tAtmVclInfoEntry.setIndexNames(*atmVclEntry.getIndexNames())
atmVclEntry.registerAugmentions(
    ("TIMETRA-ATM-MIB",
     "tAtmOamVclStatisticsEntry")
)
tAtmOamVclStatisticsEntry.setIndexNames(*atmVclEntry.getIndexNames())
aal5VccEntry.registerAugmentions(
    ("TIMETRA-ATM-MIB",
     "tAal5VccStatisticsEntry")
)
tAal5VccStatisticsEntry.setIndexNames(*aal5VccEntry.getIndexNames())
atmVplEntry.registerAugmentions(
    ("TIMETRA-ATM-MIB",
     "tAtmVplInfoEntry")
)
tAtmVplInfoEntry.setIndexNames(*atmVplEntry.getIndexNames())
atmVclEntry.registerAugmentions(
    ("TIMETRA-ATM-MIB",
     "tAtmCellVclStatisticsEntry")
)
tAtmCellVclStatisticsEntry.setIndexNames(*atmVclEntry.getIndexNames())
atmInterfaceTCEntry.registerAugmentions(
    ("TIMETRA-ATM-MIB",
     "tAtmTCSublayerEntry")
)
tAtmTCSublayerEntry.setIndexNames(*atmInterfaceTCEntry.getIndexNames())

# Managed Objects groups

tmnxAtmVclInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 6)
)
tmnxAtmVclInfoGroup.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmVclInfoOwner"),
        ("TIMETRA-ATM-MIB", "tAtmVclInfoOamStatus"),
        ("TIMETRA-ATM-MIB", "tAtmVclInfoIlmiStatus"))
)
if mibBuilder.loadTexts:
    tmnxAtmVclInfoGroup.setStatus("current")

tmnxAtmVclStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 7)
)
tmnxAtmVclStatisticsGroup.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmVclStatsTotalCellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmVclStatsTotalCellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmVclStatsTotalBytesTxd"),
        ("TIMETRA-ATM-MIB", "tAtmVclStatsTotalBytesRxd"),
        ("TIMETRA-ATM-MIB", "tAtmOamVclStatsAISCellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmOamVclStatsRDICellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmOamVclStatsLoopbackCellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmOamVclStatsAISCellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmOamVclStatsRDICellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmOamVclStatsLoopbackCellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmOamVclStatsCrc10Err"),
        ("TIMETRA-ATM-MIB", "tAtmOamVclStatsOtherCellsRxd"))
)
if mibBuilder.loadTexts:
    tmnxAtmVclStatisticsGroup.setStatus("current")

tmnxAtmAal5VccStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 8)
)
tmnxAtmAal5VccStatisticsGroup.setObjects(
      *(("TIMETRA-ATM-MIB", "tAal5VccStatsPacketsRxd"),
        ("TIMETRA-ATM-MIB", "tAal5VccStatsPacketsTxd"),
        ("TIMETRA-ATM-MIB", "tAal5VccStatsDrpPacketsRxd"),
        ("TIMETRA-ATM-MIB", "tAal5VccStatsDrpPacketsTxd"))
)
if mibBuilder.loadTexts:
    tmnxAtmAal5VccStatisticsGroup.setStatus("current")

tmnxAtmCellVclStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 9)
)
tmnxAtmCellVclStatisticsGroup.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmCellVclStatsClp0CellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmCellVclStatsClp0CellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmCellVclStatsDrpCellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmCellVclStatsDrpClp0CellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmCellVclStatsDrpClp0CellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmCellVclStatsTagCells"))
)
if mibBuilder.loadTexts:
    tmnxAtmCellVclStatisticsGroup.setStatus("current")

tmnxAtmVplInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 11)
)
tmnxAtmVplInfoGroup.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmVplInfoOwner"),
        ("TIMETRA-ATM-MIB", "tAtmVplInfoOamStatus"),
        ("TIMETRA-ATM-MIB", "tAtmVplInfoIlmiStatus"))
)
if mibBuilder.loadTexts:
    tmnxAtmVplInfoGroup.setStatus("current")

tmnxAtmVplStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 12)
)
tmnxAtmVplStatisticsGroup.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmVplStatsTotalCellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmVplStatsTotalClp0CellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmVplStatsTotalCellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmVplStatsTotalClp0CellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmVplStatsTotalBytesTxd"),
        ("TIMETRA-ATM-MIB", "tAtmVplStatsTotalBytesRxd"),
        ("TIMETRA-ATM-MIB", "tAtmVplStatsDrpCellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmVplStatsDrpClp0CellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmVplStatsDrpClp0CellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmVplStatsTagCells"),
        ("TIMETRA-ATM-MIB", "tAtmOamVplStatsAISCellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmOamVplStatsRDICellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmOamVplStatsLoopbackCellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmOamVplStatsAISCellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmOamVplStatsRDICellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmOamVplStatsLoopbackCellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmOamVplStatsCrc10Errors"),
        ("TIMETRA-ATM-MIB", "tAtmOamVplStatsOtherCellsRxd"))
)
if mibBuilder.loadTexts:
    tmnxAtmVplStatisticsGroup.setStatus("current")

tmnxAtmVtlInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 13)
)
tmnxAtmVtlInfoGroup.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmVtlAdminStatus"),
        ("TIMETRA-ATM-MIB", "tAtmVtlOperStatus"),
        ("TIMETRA-ATM-MIB", "tAtmVtlLastChange"),
        ("TIMETRA-ATM-MIB", "tAtmVtlReceiveTrafficDescrIndex"),
        ("TIMETRA-ATM-MIB", "tAtmVtlTransmitTrafficDescrIndex"),
        ("TIMETRA-ATM-MIB", "tAtmVtlRowStatus"),
        ("TIMETRA-ATM-MIB", "tAtmVtlCastType"),
        ("TIMETRA-ATM-MIB", "tAtmVtlConnKind"),
        ("TIMETRA-ATM-MIB", "tAtmVtlInfoOwner"))
)
if mibBuilder.loadTexts:
    tmnxAtmVtlInfoGroup.setStatus("current")

tmnxAtmVtlStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 14)
)
tmnxAtmVtlStatisticsGroup.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmVtlStatsTotalCellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmVtlStatsTotalClp0CellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmVtlStatsTotalCellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmVtlStatsTotalClp0CellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmVtlStatsTotalBytesTxd"),
        ("TIMETRA-ATM-MIB", "tAtmVtlStatsTotalBytesRxd"),
        ("TIMETRA-ATM-MIB", "tAtmVtlStatsDrpCellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmVtlStatsDrpClp0CellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmVtlStatsDrpClp0CellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmVtlStatsTagCells"))
)
if mibBuilder.loadTexts:
    tmnxAtmVtlStatisticsGroup.setStatus("current")

tmnxAtmIfcInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 15)
)
tmnxAtmIfcInfoGroup.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmIfcAdminStatus"),
        ("TIMETRA-ATM-MIB", "tAtmIfcOperStatus"),
        ("TIMETRA-ATM-MIB", "tAtmIfcLastChange"),
        ("TIMETRA-ATM-MIB", "tAtmIfcReceiveTrafficDescrIndex"),
        ("TIMETRA-ATM-MIB", "tAtmIfcTransmitTrafficDescrIndex"),
        ("TIMETRA-ATM-MIB", "tAtmIfcRowStatus"),
        ("TIMETRA-ATM-MIB", "tAtmIfcCastType"),
        ("TIMETRA-ATM-MIB", "tAtmIfcConnKind"),
        ("TIMETRA-ATM-MIB", "tAtmIfcInfoOwner"))
)
if mibBuilder.loadTexts:
    tmnxAtmIfcInfoGroup.setStatus("current")

tmnxAtmIfcStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 16)
)
tmnxAtmIfcStatisticsGroup.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmIfcStatsTotalCellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmIfcStatsTotalClp0CellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmIfcStatsTotalCellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmIfcStatsTotalClp0CellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmIfcStatsTotalBytesTxd"),
        ("TIMETRA-ATM-MIB", "tAtmIfcStatsTotalBytesRxd"),
        ("TIMETRA-ATM-MIB", "tAtmIfcStatsDrpCellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmIfcStatsDrpClp0CellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmIfcStatsDrpClp0CellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmIfcStatsTagCells"))
)
if mibBuilder.loadTexts:
    tmnxAtmIfcStatisticsGroup.setStatus("current")

tmnxAtmObsoleteV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 17)
)
tmnxAtmObsoleteV3v0Group.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmMdaMaxSupportedVpcs"),
        ("TIMETRA-ATM-MIB", "tAtmMdaMaxSupportedVccs"),
        ("TIMETRA-ATM-MIB", "tAtmMdaConfiguredVpcs"),
        ("TIMETRA-ATM-MIB", "tAtmMdaConfiguredVccs"))
)
if mibBuilder.loadTexts:
    tmnxAtmObsoleteV3v0Group.setStatus("current")

tmnxAtmIlmiLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 20)
)
tmnxAtmIlmiLinkGroup.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmIlmiLinkRowStatus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkLastChanged"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkAdminStatus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkOperStatus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkVpi"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkVci"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkFsmState"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkReceiveTrafficDescrIndex"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkTransmitTrafficDescrIndex"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkEstablishConPollIntvl"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkCheckConPollIntvl"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkConPollInactFactor"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkUniType"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkDeviceType"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkVersion"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkImeType"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkNegotiatedVersion"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkNegotiatedImeType"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkNeighborIfIdentifier"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkNeighborSystemIdentifier"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkNeighborUniType"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkNeighborDeviceType"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkNeighborVersion"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkNeighborMaxVpcs"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkNeighborMaxVccs"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkNeighborMaxVpiBits"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkNeighborMaxVciBits"))
)
if mibBuilder.loadTexts:
    tmnxAtmIlmiLinkGroup.setStatus("current")

tmnxAtmIlmiStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 21)
)
tmnxAtmIlmiStatisticsGroup.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmIlmiLinkOutPdus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkOutGetRequestPdus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkOutGetNextRequestPdus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkOutSetRequestPdus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkOutGetResponsePdus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkOutTrapPdus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkOutTooBigErrors"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkOutNoSuchNameErrors"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkOutBadValueErrors"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkOutReadOnlyErrors"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkOutGeneralErrors"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkInPdus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkInGetRequestPdus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkInGetNextRequestPdus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkInSetRequestPdus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkInGetResponsePdus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkInTrapPdus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkInTooBigErrors"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkInNoSuchNameErrors"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkInBadValueErrors"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkInReadOnlyErrors"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkInGeneralErrors"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkInInvalidSnmpVersionPdus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkInInvalidSnmpCommunityStringPdus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkInInvalidSnmpFormatPdus"))
)
if mibBuilder.loadTexts:
    tmnxAtmIlmiStatisticsGroup.setStatus("current")

tmnxAtmIntfConfV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 23)
)
tmnxAtmIntfConfV4v0Group.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmIntfCurrentMaxVpcs"),
        ("TIMETRA-ATM-MIB", "tAtmIntfCurrentMaxVccs"),
        ("TIMETRA-ATM-MIB", "tAtmIntfTotalIngrCbrBandwidth"),
        ("TIMETRA-ATM-MIB", "tAtmIntfTotalIngrRtVbrBandwidth"),
        ("TIMETRA-ATM-MIB", "tAtmIntfTotalIngrNrtVbrBandwidth"),
        ("TIMETRA-ATM-MIB", "tAtmIntfTotalIngrUbrBandwidth"),
        ("TIMETRA-ATM-MIB", "tAtmIntfTotalEgrCbrBandwidth"),
        ("TIMETRA-ATM-MIB", "tAtmIntfTotalEgrRtVbrBandwidth"),
        ("TIMETRA-ATM-MIB", "tAtmIntfTotalEgrNrtVbrBandwidth"),
        ("TIMETRA-ATM-MIB", "tAtmIntfTotalEgrUbrBandwidth"),
        ("TIMETRA-ATM-MIB", "tAtmIntfBandwidth"),
        ("TIMETRA-ATM-MIB", "tAtmIntfShapedBandwidth"),
        ("TIMETRA-ATM-MIB", "tAtmIntfLastUnknVpi"),
        ("TIMETRA-ATM-MIB", "tAtmIntfLastUnknVci"),
        ("TIMETRA-ATM-MIB", "tAtmIntfOperStatus"),
        ("TIMETRA-ATM-MIB", "tAtmIntfConfVtcs"),
        ("TIMETRA-ATM-MIB", "tAtmIntfConfIfcs"))
)
if mibBuilder.loadTexts:
    tmnxAtmIntfConfV4v0Group.setStatus("current")

tmnxAtmSysConfV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 24)
)
tmnxAtmSysConfV4v0Group.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmSysLlid"),
        ("TIMETRA-ATM-MIB", "tAtmSysOamRetryUp"),
        ("TIMETRA-ATM-MIB", "tAtmSysOamRetryDown"),
        ("TIMETRA-ATM-MIB", "tAtmSysOamLoopbackPeriod"))
)
if mibBuilder.loadTexts:
    tmnxAtmSysConfV4v0Group.setStatus("current")

tmnxAtmIntfStatsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 25)
)
tmnxAtmIntfStatsV4v0Group.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmIntfStatsTotalCellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmIntfStatsTotalCellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmIntfStatsTotalBytesRxd"),
        ("TIMETRA-ATM-MIB", "tAtmIntfStatsTotalBytesTxd"),
        ("TIMETRA-ATM-MIB", "tAtmIntfStatsTotalUnknCellsDrp"),
        ("TIMETRA-ATM-MIB", "tAtmIntfAal5StatsTotalPktsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmIntfAal5StatsTotalPktsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmIntfAal5StatsTotalPktsDrpRxd"),
        ("TIMETRA-ATM-MIB", "tAtmIntfAal5StatsTotalPktsDrpTxd"),
        ("TIMETRA-ATM-MIB", "tAtmIntfAal5StatsTotalCrc32Err"))
)
if mibBuilder.loadTexts:
    tmnxAtmIntfStatsV4v0Group.setStatus("current")

tmnxAtmTCSublayerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 26)
)
tmnxAtmTCSublayerGroup.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmTCSublayerHecErrors"),
        ("TIMETRA-ATM-MIB", "tAtmTCSublayerHecErrorsFixed"))
)
if mibBuilder.loadTexts:
    tmnxAtmTCSublayerGroup.setStatus("current")

tmnxAtmObsoleteV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 27)
)
tmnxAtmObsoleteV4v0Group.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmIntfStatsTotalHecErr"),
        ("TIMETRA-ATM-MIB", "tAtmIntfStatsTotalHecErrFixed"))
)
if mibBuilder.loadTexts:
    tmnxAtmObsoleteV4v0Group.setStatus("current")

tmnxAtmCpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 28)
)
tmnxAtmCpStatisticsGroup.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmCpStatsTotalCellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmCpStatsTotalCellsRxdLo"),
        ("TIMETRA-ATM-MIB", "tAtmCpStatsTotalCellsRxdHi"),
        ("TIMETRA-ATM-MIB", "tAtmCpStatsTotalCellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmCpStatsTotalCellsTxdLo"),
        ("TIMETRA-ATM-MIB", "tAtmCpStatsTotalCellsTxdHi"),
        ("TIMETRA-ATM-MIB", "tAtmCpStatsClp0CellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmCpStatsClp0CellsRxdLo"),
        ("TIMETRA-ATM-MIB", "tAtmCpStatsClp0CellsRxdHi"),
        ("TIMETRA-ATM-MIB", "tAtmCpStatsClp0CellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmCpStatsClp0CellsTxdLo"),
        ("TIMETRA-ATM-MIB", "tAtmCpStatsClp0CellsTxdHi"),
        ("TIMETRA-ATM-MIB", "tAtmCpStatsDrpCellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmCpStatsDrpClp0CellsRxd"),
        ("TIMETRA-ATM-MIB", "tAtmCpStatsDrpClp0CellsTxd"),
        ("TIMETRA-ATM-MIB", "tAtmCpStatsTagCells"))
)
if mibBuilder.loadTexts:
    tmnxAtmCpStatisticsGroup.setStatus("current")

tmnxAtmVclInfoGroupV9v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 29)
)
tmnxAtmVclInfoGroupV9v0.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmVclInfoRxTrafficDescrIdOvr"),
        ("TIMETRA-ATM-MIB", "tAtmVclInfoTxTrafficDescrIdOvr"))
)
if mibBuilder.loadTexts:
    tmnxAtmVclInfoGroupV9v0.setStatus("current")


# Notification objects

tAtmTcSubLayerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 27, 0, 1)
)
tAtmTcSubLayerDown.setObjects(
    ("ATM-MIB", "atmInterfaceTCAlarmState")
)
if mibBuilder.loadTexts:
    tAtmTcSubLayerDown.setStatus(
        "current"
    )

tAtmTcSubLayerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 27, 0, 2)
)
tAtmTcSubLayerClear.setObjects(
    ("ATM-MIB", "atmInterfaceTCAlarmState")
)
if mibBuilder.loadTexts:
    tAtmTcSubLayerClear.setStatus(
        "current"
    )

tAtmPlcpSubLayerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 27, 0, 3)
)
tAtmPlcpSubLayerDown.setObjects(
    ("ATM-MIB", "atmInterfaceDs3PlcpAlarmState")
)
if mibBuilder.loadTexts:
    tAtmPlcpSubLayerDown.setStatus(
        "current"
    )

tAtmPlcpSubLayerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 27, 0, 4)
)
tAtmPlcpSubLayerClear.setObjects(
    ("ATM-MIB", "atmInterfaceDs3PlcpAlarmState")
)
if mibBuilder.loadTexts:
    tAtmPlcpSubLayerClear.setStatus(
        "current"
    )

tAtmEpOutOfPeerVpiOrVciRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 27, 0, 5)
)
tAtmEpOutOfPeerVpiOrVciRange.setObjects(
      *(("ATM-MIB", "atmInterfaceCurrentMaxVpiBits"),
        ("ATM-MIB", "atmInterfaceCurrentMaxVciBits"),
        ("ATM-MIB", "atmInterfaceMaxActiveVpiBits"),
        ("ATM-MIB", "atmInterfaceMaxActiveVciBits"))
)
if mibBuilder.loadTexts:
    tAtmEpOutOfPeerVpiOrVciRange.setStatus(
        "current"
    )

tAtmMaxPeerVccsExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 27, 0, 6)
)
tAtmMaxPeerVccsExceeded.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmIntfCurrentMaxVccs"),
        ("ATM-MIB", "atmInterfaceConfVccs"))
)
if mibBuilder.loadTexts:
    tAtmMaxPeerVccsExceeded.setStatus(
        "current"
    )

tAtmMaxPeerVpcsExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 27, 0, 7)
)
tAtmMaxPeerVpcsExceeded.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmIntfCurrentMaxVpcs"),
        ("ATM-MIB", "atmInterfaceConfVpcs"))
)
if mibBuilder.loadTexts:
    tAtmMaxPeerVpcsExceeded.setStatus(
        "current"
    )

tAtmIlmiLinkStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 27, 0, 8)
)
tAtmIlmiLinkStatusChange.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmIlmiLinkAdminStatus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkOperStatus"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkVpi"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkVci"))
)
if mibBuilder.loadTexts:
    tAtmIlmiLinkStatusChange.setStatus(
        "current"
    )


# Notifications groups

tmnxAtmNotificationsR4r0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 2, 22)
)
tmnxAtmNotificationsR4r0Group.setObjects(
      *(("TIMETRA-ATM-MIB", "tAtmTcSubLayerDown"),
        ("TIMETRA-ATM-MIB", "tAtmTcSubLayerClear"),
        ("TIMETRA-ATM-MIB", "tAtmPlcpSubLayerDown"),
        ("TIMETRA-ATM-MIB", "tAtmPlcpSubLayerClear"),
        ("TIMETRA-ATM-MIB", "tAtmEpOutOfPeerVpiOrVciRange"),
        ("TIMETRA-ATM-MIB", "tAtmMaxPeerVccsExceeded"),
        ("TIMETRA-ATM-MIB", "tAtmMaxPeerVpcsExceeded"),
        ("TIMETRA-ATM-MIB", "tAtmIlmiLinkStatusChange"))
)
if mibBuilder.loadTexts:
    tmnxAtmNotificationsR4r0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tAtmMIBV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 1, 3)
)
if mibBuilder.loadTexts:
    tAtmMIBV4v0Compliance.setStatus(
        "obsolete"
    )

tAtmMIBV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 27, 1, 4)
)
if mibBuilder.loadTexts:
    tAtmMIBV9v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-ATM-MIB",
    **{"AtmConnectionOwner": AtmConnectionOwner,
       "AtmOamStatus": AtmOamStatus,
       "AtmIlmiStatus": AtmIlmiStatus,
       "AtmLlid": AtmLlid,
       "AtmIlmiLinkUniType": AtmIlmiLinkUniType,
       "AtmIlmiLinkDeviceType": AtmIlmiLinkDeviceType,
       "AtmIlmiLinkVersion": AtmIlmiLinkVersion,
       "AtmIlmiLinkImeType": AtmIlmiLinkImeType,
       "timetraATMMIBModule": timetraATMMIBModule,
       "tAtmMIBConformance": tAtmMIBConformance,
       "tmnxAtmMIBCompliances": tmnxAtmMIBCompliances,
       "tAtmMIBV4v0Compliance": tAtmMIBV4v0Compliance,
       "tAtmMIBV9v0Compliance": tAtmMIBV9v0Compliance,
       "tmnxAtmMIBGroups": tmnxAtmMIBGroups,
       "tmnxAtmVclInfoGroup": tmnxAtmVclInfoGroup,
       "tmnxAtmVclStatisticsGroup": tmnxAtmVclStatisticsGroup,
       "tmnxAtmAal5VccStatisticsGroup": tmnxAtmAal5VccStatisticsGroup,
       "tmnxAtmCellVclStatisticsGroup": tmnxAtmCellVclStatisticsGroup,
       "tmnxAtmVplInfoGroup": tmnxAtmVplInfoGroup,
       "tmnxAtmVplStatisticsGroup": tmnxAtmVplStatisticsGroup,
       "tmnxAtmVtlInfoGroup": tmnxAtmVtlInfoGroup,
       "tmnxAtmVtlStatisticsGroup": tmnxAtmVtlStatisticsGroup,
       "tmnxAtmIfcInfoGroup": tmnxAtmIfcInfoGroup,
       "tmnxAtmIfcStatisticsGroup": tmnxAtmIfcStatisticsGroup,
       "tmnxAtmObsoleteV3v0Group": tmnxAtmObsoleteV3v0Group,
       "tmnxAtmIlmiLinkGroup": tmnxAtmIlmiLinkGroup,
       "tmnxAtmIlmiStatisticsGroup": tmnxAtmIlmiStatisticsGroup,
       "tmnxAtmNotificationsR4r0Group": tmnxAtmNotificationsR4r0Group,
       "tmnxAtmIntfConfV4v0Group": tmnxAtmIntfConfV4v0Group,
       "tmnxAtmSysConfV4v0Group": tmnxAtmSysConfV4v0Group,
       "tmnxAtmIntfStatsV4v0Group": tmnxAtmIntfStatsV4v0Group,
       "tmnxAtmTCSublayerGroup": tmnxAtmTCSublayerGroup,
       "tmnxAtmObsoleteV4v0Group": tmnxAtmObsoleteV4v0Group,
       "tmnxAtmCpStatisticsGroup": tmnxAtmCpStatisticsGroup,
       "tmnxAtmVclInfoGroupV9v0": tmnxAtmVclInfoGroupV9v0,
       "tAtmObjs": tAtmObjs,
       "tAtmMdaObjs": tAtmMdaObjs,
       "tAtmMdaInfoTable": tAtmMdaInfoTable,
       "tAtmMdaInfoEntry": tAtmMdaInfoEntry,
       "tAtmMdaMaxSupportedVpcs": tAtmMdaMaxSupportedVpcs,
       "tAtmMdaMaxSupportedVccs": tAtmMdaMaxSupportedVccs,
       "tAtmMdaConfiguredVpcs": tAtmMdaConfiguredVpcs,
       "tAtmMdaConfiguredVccs": tAtmMdaConfiguredVccs,
       "tAtmIntfObjs": tAtmIntfObjs,
       "tAtmIntfConfTable": tAtmIntfConfTable,
       "tAtmIntfConfEntry": tAtmIntfConfEntry,
       "tAtmIntfCurrentMaxVpcs": tAtmIntfCurrentMaxVpcs,
       "tAtmIntfCurrentMaxVccs": tAtmIntfCurrentMaxVccs,
       "tAtmIntfTotalIngrCbrBandwidth": tAtmIntfTotalIngrCbrBandwidth,
       "tAtmIntfTotalIngrRtVbrBandwidth": tAtmIntfTotalIngrRtVbrBandwidth,
       "tAtmIntfTotalIngrNrtVbrBandwidth": tAtmIntfTotalIngrNrtVbrBandwidth,
       "tAtmIntfTotalIngrUbrBandwidth": tAtmIntfTotalIngrUbrBandwidth,
       "tAtmIntfTotalEgrCbrBandwidth": tAtmIntfTotalEgrCbrBandwidth,
       "tAtmIntfTotalEgrRtVbrBandwidth": tAtmIntfTotalEgrRtVbrBandwidth,
       "tAtmIntfTotalEgrNrtVbrBandwidth": tAtmIntfTotalEgrNrtVbrBandwidth,
       "tAtmIntfTotalEgrUbrBandwidth": tAtmIntfTotalEgrUbrBandwidth,
       "tAtmIntfBandwidth": tAtmIntfBandwidth,
       "tAtmIntfShapedBandwidth": tAtmIntfShapedBandwidth,
       "tAtmIntfLastUnknVpi": tAtmIntfLastUnknVpi,
       "tAtmIntfLastUnknVci": tAtmIntfLastUnknVci,
       "tAtmIntfOperStatus": tAtmIntfOperStatus,
       "tAtmIntfConfVtcs": tAtmIntfConfVtcs,
       "tAtmIntfConfIfcs": tAtmIntfConfIfcs,
       "tAtmIntfStatsTable": tAtmIntfStatsTable,
       "tAtmIntfStatsEntry": tAtmIntfStatsEntry,
       "tAtmIntfStatsTotalCellsRxd": tAtmIntfStatsTotalCellsRxd,
       "tAtmIntfStatsTotalCellsTxd": tAtmIntfStatsTotalCellsTxd,
       "tAtmIntfStatsTotalBytesRxd": tAtmIntfStatsTotalBytesRxd,
       "tAtmIntfStatsTotalBytesTxd": tAtmIntfStatsTotalBytesTxd,
       "tAtmIntfStatsTotalUnknCellsDrp": tAtmIntfStatsTotalUnknCellsDrp,
       "tAtmIntfStatsTotalHecErr": tAtmIntfStatsTotalHecErr,
       "tAtmIntfStatsTotalHecErrFixed": tAtmIntfStatsTotalHecErrFixed,
       "tAtmIntfAal5StatsTable": tAtmIntfAal5StatsTable,
       "tAtmIntfAal5StatsEntry": tAtmIntfAal5StatsEntry,
       "tAtmIntfAal5StatsTotalPktsRxd": tAtmIntfAal5StatsTotalPktsRxd,
       "tAtmIntfAal5StatsTotalPktsTxd": tAtmIntfAal5StatsTotalPktsTxd,
       "tAtmIntfAal5StatsTotalPktsDrpRxd": tAtmIntfAal5StatsTotalPktsDrpRxd,
       "tAtmIntfAal5StatsTotalPktsDrpTxd": tAtmIntfAal5StatsTotalPktsDrpTxd,
       "tAtmIntfAal5StatsTotalCrc32Err": tAtmIntfAal5StatsTotalCrc32Err,
       "tAtmIfcInfoTable": tAtmIfcInfoTable,
       "tAtmIfcInfoEntry": tAtmIfcInfoEntry,
       "tAtmIfcAdminStatus": tAtmIfcAdminStatus,
       "tAtmIfcOperStatus": tAtmIfcOperStatus,
       "tAtmIfcLastChange": tAtmIfcLastChange,
       "tAtmIfcReceiveTrafficDescrIndex": tAtmIfcReceiveTrafficDescrIndex,
       "tAtmIfcTransmitTrafficDescrIndex": tAtmIfcTransmitTrafficDescrIndex,
       "tAtmIfcRowStatus": tAtmIfcRowStatus,
       "tAtmIfcCastType": tAtmIfcCastType,
       "tAtmIfcConnKind": tAtmIfcConnKind,
       "tAtmIfcInfoOwner": tAtmIfcInfoOwner,
       "tAtmIfcStatisticsTable": tAtmIfcStatisticsTable,
       "tAtmIfcStatisticsEntry": tAtmIfcStatisticsEntry,
       "tAtmIfcStatsTotalCellsRxd": tAtmIfcStatsTotalCellsRxd,
       "tAtmIfcStatsTotalClp0CellsRxd": tAtmIfcStatsTotalClp0CellsRxd,
       "tAtmIfcStatsTotalCellsTxd": tAtmIfcStatsTotalCellsTxd,
       "tAtmIfcStatsTotalClp0CellsTxd": tAtmIfcStatsTotalClp0CellsTxd,
       "tAtmIfcStatsTotalBytesRxd": tAtmIfcStatsTotalBytesRxd,
       "tAtmIfcStatsTotalBytesTxd": tAtmIfcStatsTotalBytesTxd,
       "tAtmIfcStatsDrpCellsRxd": tAtmIfcStatsDrpCellsRxd,
       "tAtmIfcStatsDrpClp0CellsRxd": tAtmIfcStatsDrpClp0CellsRxd,
       "tAtmIfcStatsDrpClp0CellsTxd": tAtmIfcStatsDrpClp0CellsTxd,
       "tAtmIfcStatsTagCells": tAtmIfcStatsTagCells,
       "tAtmVclObjs": tAtmVclObjs,
       "tAtmVclInfoTable": tAtmVclInfoTable,
       "tAtmVclInfoEntry": tAtmVclInfoEntry,
       "tAtmVclInfoOwner": tAtmVclInfoOwner,
       "tAtmVclInfoOamStatus": tAtmVclInfoOamStatus,
       "tAtmVclInfoIlmiStatus": tAtmVclInfoIlmiStatus,
       "tAtmVclInfoRxTrafficDescrIdOvr": tAtmVclInfoRxTrafficDescrIdOvr,
       "tAtmVclInfoTxTrafficDescrIdOvr": tAtmVclInfoTxTrafficDescrIdOvr,
       "tAtmVclStatisticsTable": tAtmVclStatisticsTable,
       "tAtmVclStatisticsEntry": tAtmVclStatisticsEntry,
       "tAtmVclStatsTotalCellsRxd": tAtmVclStatsTotalCellsRxd,
       "tAtmVclStatsTotalCellsTxd": tAtmVclStatsTotalCellsTxd,
       "tAtmVclStatsTotalBytesRxd": tAtmVclStatsTotalBytesRxd,
       "tAtmVclStatsTotalBytesTxd": tAtmVclStatsTotalBytesTxd,
       "tAtmOamVclStatisticsTable": tAtmOamVclStatisticsTable,
       "tAtmOamVclStatisticsEntry": tAtmOamVclStatisticsEntry,
       "tAtmOamVclStatsAISCellsTxd": tAtmOamVclStatsAISCellsTxd,
       "tAtmOamVclStatsRDICellsTxd": tAtmOamVclStatsRDICellsTxd,
       "tAtmOamVclStatsLoopbackCellsTxd": tAtmOamVclStatsLoopbackCellsTxd,
       "tAtmOamVclStatsAISCellsRxd": tAtmOamVclStatsAISCellsRxd,
       "tAtmOamVclStatsRDICellsRxd": tAtmOamVclStatsRDICellsRxd,
       "tAtmOamVclStatsLoopbackCellsRxd": tAtmOamVclStatsLoopbackCellsRxd,
       "tAtmOamVclStatsCrc10Err": tAtmOamVclStatsCrc10Err,
       "tAtmOamVclStatsOtherCellsRxd": tAtmOamVclStatsOtherCellsRxd,
       "tAal5VccObjs": tAal5VccObjs,
       "tAal5VccStatisticsTable": tAal5VccStatisticsTable,
       "tAal5VccStatisticsEntry": tAal5VccStatisticsEntry,
       "tAal5VccStatsPacketsRxd": tAal5VccStatsPacketsRxd,
       "tAal5VccStatsPacketsTxd": tAal5VccStatsPacketsTxd,
       "tAal5VccStatsDrpPacketsRxd": tAal5VccStatsDrpPacketsRxd,
       "tAal5VccStatsDrpPacketsTxd": tAal5VccStatsDrpPacketsTxd,
       "tAtmTrafficDescObjs": tAtmTrafficDescObjs,
       "tAtmVplObjs": tAtmVplObjs,
       "tAtmVplInfoTable": tAtmVplInfoTable,
       "tAtmVplInfoEntry": tAtmVplInfoEntry,
       "tAtmVplInfoOwner": tAtmVplInfoOwner,
       "tAtmVplInfoOamStatus": tAtmVplInfoOamStatus,
       "tAtmVplInfoIlmiStatus": tAtmVplInfoIlmiStatus,
       "tAtmVplStatisticsTable": tAtmVplStatisticsTable,
       "tAtmVplStatisticsEntry": tAtmVplStatisticsEntry,
       "tAtmVplStatsTotalCellsRxd": tAtmVplStatsTotalCellsRxd,
       "tAtmVplStatsTotalClp0CellsRxd": tAtmVplStatsTotalClp0CellsRxd,
       "tAtmVplStatsTotalCellsTxd": tAtmVplStatsTotalCellsTxd,
       "tAtmVplStatsTotalClp0CellsTxd": tAtmVplStatsTotalClp0CellsTxd,
       "tAtmVplStatsTotalBytesRxd": tAtmVplStatsTotalBytesRxd,
       "tAtmVplStatsTotalBytesTxd": tAtmVplStatsTotalBytesTxd,
       "tAtmVplStatsDrpCellsRxd": tAtmVplStatsDrpCellsRxd,
       "tAtmVplStatsDrpClp0CellsRxd": tAtmVplStatsDrpClp0CellsRxd,
       "tAtmVplStatsDrpClp0CellsTxd": tAtmVplStatsDrpClp0CellsTxd,
       "tAtmVplStatsTagCells": tAtmVplStatsTagCells,
       "tAtmOamVplStatisticsTable": tAtmOamVplStatisticsTable,
       "tAtmOamVplStatisticsEntry": tAtmOamVplStatisticsEntry,
       "tAtmOamVplStatsAISCellsTxd": tAtmOamVplStatsAISCellsTxd,
       "tAtmOamVplStatsRDICellsTxd": tAtmOamVplStatsRDICellsTxd,
       "tAtmOamVplStatsLoopbackCellsTxd": tAtmOamVplStatsLoopbackCellsTxd,
       "tAtmOamVplStatsAISCellsRxd": tAtmOamVplStatsAISCellsRxd,
       "tAtmOamVplStatsRDICellsRxd": tAtmOamVplStatsRDICellsRxd,
       "tAtmOamVplStatsLoopbackCellsRxd": tAtmOamVplStatsLoopbackCellsRxd,
       "tAtmOamVplStatsCrc10Errors": tAtmOamVplStatsCrc10Errors,
       "tAtmOamVplStatsOtherCellsRxd": tAtmOamVplStatsOtherCellsRxd,
       "tAtmVtlObjs": tAtmVtlObjs,
       "tAtmVtlInfoTable": tAtmVtlInfoTable,
       "tAtmVtlInfoEntry": tAtmVtlInfoEntry,
       "tAtmVtlStartVpi": tAtmVtlStartVpi,
       "tAtmVtlEndVpi": tAtmVtlEndVpi,
       "tAtmVtlAdminStatus": tAtmVtlAdminStatus,
       "tAtmVtlOperStatus": tAtmVtlOperStatus,
       "tAtmVtlLastChange": tAtmVtlLastChange,
       "tAtmVtlReceiveTrafficDescrIndex": tAtmVtlReceiveTrafficDescrIndex,
       "tAtmVtlTransmitTrafficDescrIndex": tAtmVtlTransmitTrafficDescrIndex,
       "tAtmVtlRowStatus": tAtmVtlRowStatus,
       "tAtmVtlCastType": tAtmVtlCastType,
       "tAtmVtlConnKind": tAtmVtlConnKind,
       "tAtmVtlInfoOwner": tAtmVtlInfoOwner,
       "tAtmVtlStatisticsTable": tAtmVtlStatisticsTable,
       "tAtmVtlStatisticsEntry": tAtmVtlStatisticsEntry,
       "tAtmVtlStatsTotalCellsRxd": tAtmVtlStatsTotalCellsRxd,
       "tAtmVtlStatsTotalClp0CellsRxd": tAtmVtlStatsTotalClp0CellsRxd,
       "tAtmVtlStatsTotalCellsTxd": tAtmVtlStatsTotalCellsTxd,
       "tAtmVtlStatsTotalClp0CellsTxd": tAtmVtlStatsTotalClp0CellsTxd,
       "tAtmVtlStatsTotalBytesRxd": tAtmVtlStatsTotalBytesRxd,
       "tAtmVtlStatsTotalBytesTxd": tAtmVtlStatsTotalBytesTxd,
       "tAtmVtlStatsDrpCellsRxd": tAtmVtlStatsDrpCellsRxd,
       "tAtmVtlStatsDrpClp0CellsRxd": tAtmVtlStatsDrpClp0CellsRxd,
       "tAtmVtlStatsDrpClp0CellsTxd": tAtmVtlStatsDrpClp0CellsTxd,
       "tAtmVtlStatsTagCells": tAtmVtlStatsTagCells,
       "tAtmCellVclObjs": tAtmCellVclObjs,
       "tAtmCellVclStatisticsTable": tAtmCellVclStatisticsTable,
       "tAtmCellVclStatisticsEntry": tAtmCellVclStatisticsEntry,
       "tAtmCellVclStatsClp0CellsRxd": tAtmCellVclStatsClp0CellsRxd,
       "tAtmCellVclStatsClp0CellsTxd": tAtmCellVclStatsClp0CellsTxd,
       "tAtmCellVclStatsDrpCellsRxd": tAtmCellVclStatsDrpCellsRxd,
       "tAtmCellVclStatsDrpClp0CellsRxd": tAtmCellVclStatsDrpClp0CellsRxd,
       "tAtmCellVclStatsDrpClp0CellsTxd": tAtmCellVclStatsDrpClp0CellsTxd,
       "tAtmCellVclStatsTagCells": tAtmCellVclStatsTagCells,
       "tAtmSystemObjs": tAtmSystemObjs,
       "tAtmSysLlid": tAtmSysLlid,
       "tAtmSysOamRetryUp": tAtmSysOamRetryUp,
       "tAtmSysOamRetryDown": tAtmSysOamRetryDown,
       "tAtmSysOamLoopbackPeriod": tAtmSysOamLoopbackPeriod,
       "tAtmIlmiLinkObjs": tAtmIlmiLinkObjs,
       "tAtmIlmiLinkTable": tAtmIlmiLinkTable,
       "tAtmIlmiLinkEntry": tAtmIlmiLinkEntry,
       "tAtmIlmiLinkRowStatus": tAtmIlmiLinkRowStatus,
       "tAtmIlmiLinkLastChanged": tAtmIlmiLinkLastChanged,
       "tAtmIlmiLinkAdminStatus": tAtmIlmiLinkAdminStatus,
       "tAtmIlmiLinkOperStatus": tAtmIlmiLinkOperStatus,
       "tAtmIlmiLinkVpi": tAtmIlmiLinkVpi,
       "tAtmIlmiLinkVci": tAtmIlmiLinkVci,
       "tAtmIlmiLinkFsmState": tAtmIlmiLinkFsmState,
       "tAtmIlmiLinkReceiveTrafficDescrIndex": tAtmIlmiLinkReceiveTrafficDescrIndex,
       "tAtmIlmiLinkTransmitTrafficDescrIndex": tAtmIlmiLinkTransmitTrafficDescrIndex,
       "tAtmIlmiLinkEstablishConPollIntvl": tAtmIlmiLinkEstablishConPollIntvl,
       "tAtmIlmiLinkCheckConPollIntvl": tAtmIlmiLinkCheckConPollIntvl,
       "tAtmIlmiLinkConPollInactFactor": tAtmIlmiLinkConPollInactFactor,
       "tAtmIlmiLinkUniType": tAtmIlmiLinkUniType,
       "tAtmIlmiLinkDeviceType": tAtmIlmiLinkDeviceType,
       "tAtmIlmiLinkVersion": tAtmIlmiLinkVersion,
       "tAtmIlmiLinkImeType": tAtmIlmiLinkImeType,
       "tAtmIlmiLinkNegotiatedVersion": tAtmIlmiLinkNegotiatedVersion,
       "tAtmIlmiLinkNegotiatedImeType": tAtmIlmiLinkNegotiatedImeType,
       "tAtmIlmiLinkNeighborIfIdentifier": tAtmIlmiLinkNeighborIfIdentifier,
       "tAtmIlmiLinkNeighborSystemIdentifier": tAtmIlmiLinkNeighborSystemIdentifier,
       "tAtmIlmiLinkNeighborUniType": tAtmIlmiLinkNeighborUniType,
       "tAtmIlmiLinkNeighborDeviceType": tAtmIlmiLinkNeighborDeviceType,
       "tAtmIlmiLinkNeighborVersion": tAtmIlmiLinkNeighborVersion,
       "tAtmIlmiLinkNeighborMaxVpcs": tAtmIlmiLinkNeighborMaxVpcs,
       "tAtmIlmiLinkNeighborMaxVccs": tAtmIlmiLinkNeighborMaxVccs,
       "tAtmIlmiLinkNeighborMaxVpiBits": tAtmIlmiLinkNeighborMaxVpiBits,
       "tAtmIlmiLinkNeighborMaxVciBits": tAtmIlmiLinkNeighborMaxVciBits,
       "tAtmIlmiLinkStatisticsTable": tAtmIlmiLinkStatisticsTable,
       "tAtmIlmiLinkStatisticsEntry": tAtmIlmiLinkStatisticsEntry,
       "tAtmIlmiLinkOutPdus": tAtmIlmiLinkOutPdus,
       "tAtmIlmiLinkOutGetRequestPdus": tAtmIlmiLinkOutGetRequestPdus,
       "tAtmIlmiLinkOutGetNextRequestPdus": tAtmIlmiLinkOutGetNextRequestPdus,
       "tAtmIlmiLinkOutSetRequestPdus": tAtmIlmiLinkOutSetRequestPdus,
       "tAtmIlmiLinkOutGetResponsePdus": tAtmIlmiLinkOutGetResponsePdus,
       "tAtmIlmiLinkOutTrapPdus": tAtmIlmiLinkOutTrapPdus,
       "tAtmIlmiLinkOutTooBigErrors": tAtmIlmiLinkOutTooBigErrors,
       "tAtmIlmiLinkOutNoSuchNameErrors": tAtmIlmiLinkOutNoSuchNameErrors,
       "tAtmIlmiLinkOutBadValueErrors": tAtmIlmiLinkOutBadValueErrors,
       "tAtmIlmiLinkOutReadOnlyErrors": tAtmIlmiLinkOutReadOnlyErrors,
       "tAtmIlmiLinkOutGeneralErrors": tAtmIlmiLinkOutGeneralErrors,
       "tAtmIlmiLinkInPdus": tAtmIlmiLinkInPdus,
       "tAtmIlmiLinkInGetRequestPdus": tAtmIlmiLinkInGetRequestPdus,
       "tAtmIlmiLinkInGetNextRequestPdus": tAtmIlmiLinkInGetNextRequestPdus,
       "tAtmIlmiLinkInSetRequestPdus": tAtmIlmiLinkInSetRequestPdus,
       "tAtmIlmiLinkInGetResponsePdus": tAtmIlmiLinkInGetResponsePdus,
       "tAtmIlmiLinkInTrapPdus": tAtmIlmiLinkInTrapPdus,
       "tAtmIlmiLinkInTooBigErrors": tAtmIlmiLinkInTooBigErrors,
       "tAtmIlmiLinkInNoSuchNameErrors": tAtmIlmiLinkInNoSuchNameErrors,
       "tAtmIlmiLinkInBadValueErrors": tAtmIlmiLinkInBadValueErrors,
       "tAtmIlmiLinkInReadOnlyErrors": tAtmIlmiLinkInReadOnlyErrors,
       "tAtmIlmiLinkInGeneralErrors": tAtmIlmiLinkInGeneralErrors,
       "tAtmIlmiLinkInInvalidSnmpVersionPdus": tAtmIlmiLinkInInvalidSnmpVersionPdus,
       "tAtmIlmiLinkInInvalidSnmpCommunityStringPdus": tAtmIlmiLinkInInvalidSnmpCommunityStringPdus,
       "tAtmIlmiLinkInInvalidSnmpFormatPdus": tAtmIlmiLinkInInvalidSnmpFormatPdus,
       "tAtmTCSublayerObjs": tAtmTCSublayerObjs,
       "tAtmTCSublayerTable": tAtmTCSublayerTable,
       "tAtmTCSublayerEntry": tAtmTCSublayerEntry,
       "tAtmTCSublayerHecErrors": tAtmTCSublayerHecErrors,
       "tAtmTCSublayerHecErrorsFixed": tAtmTCSublayerHecErrorsFixed,
       "tAtmCpObjs": tAtmCpObjs,
       "tAtmCpStatisticsTable": tAtmCpStatisticsTable,
       "tAtmCpStatisticsEntry": tAtmCpStatisticsEntry,
       "tAtmCpStatsTotalCellsRxd": tAtmCpStatsTotalCellsRxd,
       "tAtmCpStatsTotalCellsRxdLo": tAtmCpStatsTotalCellsRxdLo,
       "tAtmCpStatsTotalCellsRxdHi": tAtmCpStatsTotalCellsRxdHi,
       "tAtmCpStatsTotalCellsTxd": tAtmCpStatsTotalCellsTxd,
       "tAtmCpStatsTotalCellsTxdLo": tAtmCpStatsTotalCellsTxdLo,
       "tAtmCpStatsTotalCellsTxdHi": tAtmCpStatsTotalCellsTxdHi,
       "tAtmCpStatsClp0CellsRxd": tAtmCpStatsClp0CellsRxd,
       "tAtmCpStatsClp0CellsRxdLo": tAtmCpStatsClp0CellsRxdLo,
       "tAtmCpStatsClp0CellsRxdHi": tAtmCpStatsClp0CellsRxdHi,
       "tAtmCpStatsClp0CellsTxd": tAtmCpStatsClp0CellsTxd,
       "tAtmCpStatsClp0CellsTxdLo": tAtmCpStatsClp0CellsTxdLo,
       "tAtmCpStatsClp0CellsTxdHi": tAtmCpStatsClp0CellsTxdHi,
       "tAtmCpStatsDrpCellsRxd": tAtmCpStatsDrpCellsRxd,
       "tAtmCpStatsDrpClp0CellsRxd": tAtmCpStatsDrpClp0CellsRxd,
       "tAtmCpStatsDrpClp0CellsTxd": tAtmCpStatsDrpClp0CellsTxd,
       "tAtmCpStatsTagCells": tAtmCpStatsTagCells,
       "tmnxAtmNotifyPrefix": tmnxAtmNotifyPrefix,
       "tAtmNotifications": tAtmNotifications,
       "tAtmTcSubLayerDown": tAtmTcSubLayerDown,
       "tAtmTcSubLayerClear": tAtmTcSubLayerClear,
       "tAtmPlcpSubLayerDown": tAtmPlcpSubLayerDown,
       "tAtmPlcpSubLayerClear": tAtmPlcpSubLayerClear,
       "tAtmEpOutOfPeerVpiOrVciRange": tAtmEpOutOfPeerVpiOrVciRange,
       "tAtmMaxPeerVccsExceeded": tAtmMaxPeerVccsExceeded,
       "tAtmMaxPeerVpcsExceeded": tAtmMaxPeerVpcsExceeded,
       "tAtmIlmiLinkStatusChange": tAtmIlmiLinkStatusChange}
)
