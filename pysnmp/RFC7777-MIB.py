# SNMP MIB module (RFC7777-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC7777-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:33 2024
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
 Opaque,
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
    "Opaque",
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

_Wellfleet_ObjectIdentity = ObjectIdentity
wellfleet = _Wellfleet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18)
)
_WfOspfGeneralGroup_ObjectIdentity = ObjectIdentity
wfOspfGeneralGroup = _WfOspfGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1)
)


class _WfOspfGeneralDelete_Type(Integer32):
    """Custom type wfOspfGeneralDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOspfGeneralDelete_Type.__name__ = "Integer32"
_WfOspfGeneralDelete_Object = MibScalar
wfOspfGeneralDelete = _WfOspfGeneralDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 1),
    _WfOspfGeneralDelete_Type()
)
wfOspfGeneralDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfGeneralDelete.setStatus("mandatory")


class _WfOspfGeneralDisable_Type(Integer32):
    """Custom type wfOspfGeneralDisable based on Integer32"""
    defaultValue = 1

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


_WfOspfGeneralDisable_Type.__name__ = "Integer32"
_WfOspfGeneralDisable_Object = MibScalar
wfOspfGeneralDisable = _WfOspfGeneralDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 2),
    _WfOspfGeneralDisable_Type()
)
wfOspfGeneralDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfGeneralDisable.setStatus("mandatory")


class _WfOspfGeneralState_Type(Integer32):
    """Custom type wfOspfGeneralState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfOspfGeneralState_Type.__name__ = "Integer32"
_WfOspfGeneralState_Object = MibScalar
wfOspfGeneralState = _WfOspfGeneralState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 3),
    _WfOspfGeneralState_Type()
)
wfOspfGeneralState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfGeneralState.setStatus("mandatory")
_WfOspfRouterId_Type = IpAddress
_WfOspfRouterId_Object = MibScalar
wfOspfRouterId = _WfOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 4),
    _WfOspfRouterId_Type()
)
wfOspfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfRouterId.setStatus("mandatory")
_WfOspfVersionNumber_Type = Integer32
_WfOspfVersionNumber_Object = MibScalar
wfOspfVersionNumber = _WfOspfVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 5),
    _WfOspfVersionNumber_Type()
)
wfOspfVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVersionNumber.setStatus("mandatory")


class _WfOspfAreaBdrRtrStatus_Type(Integer32):
    """Custom type wfOspfAreaBdrRtrStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfOspfAreaBdrRtrStatus_Type.__name__ = "Integer32"
_WfOspfAreaBdrRtrStatus_Object = MibScalar
wfOspfAreaBdrRtrStatus = _WfOspfAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 6),
    _WfOspfAreaBdrRtrStatus_Type()
)
wfOspfAreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfAreaBdrRtrStatus.setStatus("mandatory")


class _WfOspfASBdrRtrStatus_Type(Integer32):
    """Custom type wfOspfASBdrRtrStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfOspfASBdrRtrStatus_Type.__name__ = "Integer32"
_WfOspfASBdrRtrStatus_Object = MibScalar
wfOspfASBdrRtrStatus = _WfOspfASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 7),
    _WfOspfASBdrRtrStatus_Type()
)
wfOspfASBdrRtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfASBdrRtrStatus.setStatus("mandatory")


class _WfOspfTOSSupport_Type(Integer32):
    """Custom type wfOspfTOSSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfOspfTOSSupport_Type.__name__ = "Integer32"
_WfOspfTOSSupport_Object = MibScalar
wfOspfTOSSupport = _WfOspfTOSSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 8),
    _WfOspfTOSSupport_Type()
)
wfOspfTOSSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfTOSSupport.setStatus("mandatory")


class _WfOspfSpfHoldDown_Type(Integer32):
    """Custom type wfOspfSpfHoldDown based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("defval", 1),
          ("maximum", 10))
    )


_WfOspfSpfHoldDown_Type.__name__ = "Integer32"
_WfOspfSpfHoldDown_Object = MibScalar
wfOspfSpfHoldDown = _WfOspfSpfHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 9),
    _WfOspfSpfHoldDown_Type()
)
wfOspfSpfHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfSpfHoldDown.setStatus("mandatory")


class _WfOspfSlotMask_Type(Integer32):
    """Custom type wfOspfSlotMask based on Integer32"""
    defaultValue = 4261150720

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4261150720
        )
    )
    namedValues = NamedValues(
        ("slotmask", 4261150720)
    )


_WfOspfSlotMask_Type.__name__ = "Integer32"
_WfOspfSlotMask_Object = MibScalar
wfOspfSlotMask = _WfOspfSlotMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 10),
    _WfOspfSlotMask_Type()
)
wfOspfSlotMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfSlotMask.setStatus("mandatory")
_WfOspfAreaTable_Object = MibTable
wfOspfAreaTable = _WfOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    wfOspfAreaTable.setStatus("mandatory")
_WfOspfAreaEntry_Object = MibTableRow
wfOspfAreaEntry = _WfOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1)
)
wfOspfAreaEntry.setIndexNames(
    (0, "RFC7777-MIB", "wfOspfAreaId"),
)
if mibBuilder.loadTexts:
    wfOspfAreaEntry.setStatus("mandatory")


class _WfOspfAreaDelete_Type(Integer32):
    """Custom type wfOspfAreaDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOspfAreaDelete_Type.__name__ = "Integer32"
_WfOspfAreaDelete_Object = MibTableColumn
wfOspfAreaDelete = _WfOspfAreaDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1, 1),
    _WfOspfAreaDelete_Type()
)
wfOspfAreaDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfAreaDelete.setStatus("mandatory")


class _WfOspfAreaDisable_Type(Integer32):
    """Custom type wfOspfAreaDisable based on Integer32"""
    defaultValue = 1

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


_WfOspfAreaDisable_Type.__name__ = "Integer32"
_WfOspfAreaDisable_Object = MibTableColumn
wfOspfAreaDisable = _WfOspfAreaDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1, 2),
    _WfOspfAreaDisable_Type()
)
wfOspfAreaDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfAreaDisable.setStatus("mandatory")


class _WfOspfAreaState_Type(Integer32):
    """Custom type wfOspfAreaState based on Integer32"""
    defaultValue = 2

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


_WfOspfAreaState_Type.__name__ = "Integer32"
_WfOspfAreaState_Object = MibTableColumn
wfOspfAreaState = _WfOspfAreaState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1, 3),
    _WfOspfAreaState_Type()
)
wfOspfAreaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfAreaState.setStatus("mandatory")
_WfOspfAreaId_Type = IpAddress
_WfOspfAreaId_Object = MibTableColumn
wfOspfAreaId = _WfOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1, 4),
    _WfOspfAreaId_Type()
)
wfOspfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfAreaId.setStatus("mandatory")


class _WfOspfAuthType_Type(Integer32):
    """Custom type wfOspfAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nopassword", 1),
          ("simplepassword", 2))
    )


_WfOspfAuthType_Type.__name__ = "Integer32"
_WfOspfAuthType_Object = MibTableColumn
wfOspfAuthType = _WfOspfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1, 5),
    _WfOspfAuthType_Type()
)
wfOspfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfAuthType.setStatus("mandatory")


class _WfOspfImportASExtern_Type(Integer32):
    """Custom type wfOspfImportASExtern based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfOspfImportASExtern_Type.__name__ = "Integer32"
_WfOspfImportASExtern_Object = MibTableColumn
wfOspfImportASExtern = _WfOspfImportASExtern_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1, 6),
    _WfOspfImportASExtern_Type()
)
wfOspfImportASExtern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfImportASExtern.setStatus("mandatory")


class _WfOspfStubMetric_Type(Integer32):
    """Custom type wfOspfStubMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16777215)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 16777215),
          ("minimum", 1))
    )


_WfOspfStubMetric_Type.__name__ = "Integer32"
_WfOspfStubMetric_Object = MibTableColumn
wfOspfStubMetric = _WfOspfStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1, 7),
    _WfOspfStubMetric_Type()
)
wfOspfStubMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfStubMetric.setStatus("mandatory")


class _WfOspfImportSum_Type(Integer32):
    """Custom type wfOspfImportSum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfOspfImportSum_Type.__name__ = "Integer32"
_WfOspfImportSum_Object = MibTableColumn
wfOspfImportSum = _WfOspfImportSum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1, 8),
    _WfOspfImportSum_Type()
)
wfOspfImportSum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfImportSum.setStatus("mandatory")
_WfOspfSpfCnt_Type = Counter32
_WfOspfSpfCnt_Object = MibTableColumn
wfOspfSpfCnt = _WfOspfSpfCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1, 9),
    _WfOspfSpfCnt_Type()
)
wfOspfSpfCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfSpfCnt.setStatus("mandatory")
_WfOspfLsdbTable_Object = MibTable
wfOspfLsdbTable = _WfOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3)
)
if mibBuilder.loadTexts:
    wfOspfLsdbTable.setStatus("mandatory")
_WfOspfLsdbEntry_Object = MibTableRow
wfOspfLsdbEntry = _WfOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1)
)
wfOspfLsdbEntry.setIndexNames(
    (0, "RFC7777-MIB", "wfOspfLsdbAreaId"),
    (0, "RFC7777-MIB", "wfOspfLsdbType"),
    (0, "RFC7777-MIB", "wfOspfLsdbLSID"),
    (0, "RFC7777-MIB", "wfOspfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    wfOspfLsdbEntry.setStatus("mandatory")
_WfOspfLsdbAreaId_Type = IpAddress
_WfOspfLsdbAreaId_Object = MibTableColumn
wfOspfLsdbAreaId = _WfOspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1, 1),
    _WfOspfLsdbAreaId_Type()
)
wfOspfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfLsdbAreaId.setStatus("mandatory")


class _WfOspfLsdbType_Type(Integer32):
    """Custom type wfOspfLsdbType based on Integer32"""
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
        *(("asexternallink", 5),
          ("assummarylink", 4),
          ("networklink", 2),
          ("routerlink", 1),
          ("summarylink", 3))
    )


_WfOspfLsdbType_Type.__name__ = "Integer32"
_WfOspfLsdbType_Object = MibTableColumn
wfOspfLsdbType = _WfOspfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1, 2),
    _WfOspfLsdbType_Type()
)
wfOspfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfLsdbType.setStatus("mandatory")
_WfOspfLsdbLSID_Type = IpAddress
_WfOspfLsdbLSID_Object = MibTableColumn
wfOspfLsdbLSID = _WfOspfLsdbLSID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1, 3),
    _WfOspfLsdbLSID_Type()
)
wfOspfLsdbLSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfLsdbLSID.setStatus("mandatory")
_WfOspfLsdbRouterId_Type = IpAddress
_WfOspfLsdbRouterId_Object = MibTableColumn
wfOspfLsdbRouterId = _WfOspfLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1, 4),
    _WfOspfLsdbRouterId_Type()
)
wfOspfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfLsdbRouterId.setStatus("mandatory")
_WfOspfLsdbSequence_Type = Integer32
_WfOspfLsdbSequence_Object = MibTableColumn
wfOspfLsdbSequence = _WfOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1, 5),
    _WfOspfLsdbSequence_Type()
)
wfOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfLsdbSequence.setStatus("mandatory")


class _WfOspfLsdbAge_Type(Integer32):
    """Custom type wfOspfLsdbAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3600
        )
    )
    namedValues = NamedValues(
        ("lsdbmaxage", 3600)
    )


_WfOspfLsdbAge_Type.__name__ = "Integer32"
_WfOspfLsdbAge_Object = MibTableColumn
wfOspfLsdbAge = _WfOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1, 6),
    _WfOspfLsdbAge_Type()
)
wfOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfLsdbAge.setStatus("mandatory")
_WfOspfLsdbChecksum_Type = Integer32
_WfOspfLsdbChecksum_Object = MibTableColumn
wfOspfLsdbChecksum = _WfOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1, 7),
    _WfOspfLsdbChecksum_Type()
)
wfOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfLsdbChecksum.setStatus("mandatory")
_WfOspfLsdbAdvLen_Type = Integer32
_WfOspfLsdbAdvLen_Object = MibTableColumn
wfOspfLsdbAdvLen = _WfOspfLsdbAdvLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1, 8),
    _WfOspfLsdbAdvLen_Type()
)
wfOspfLsdbAdvLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfLsdbAdvLen.setStatus("mandatory")
_WfOspfAreaRangeTable_Object = MibTable
wfOspfAreaRangeTable = _WfOspfAreaRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 4)
)
if mibBuilder.loadTexts:
    wfOspfAreaRangeTable.setStatus("mandatory")
_WfOspfAreaRangeEntry_Object = MibTableRow
wfOspfAreaRangeEntry = _WfOspfAreaRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 4, 1)
)
wfOspfAreaRangeEntry.setIndexNames(
    (0, "RFC7777-MIB", "wfOspfAreaRangeAreaID"),
    (0, "RFC7777-MIB", "wfOspfAreaRangeNet"),
)
if mibBuilder.loadTexts:
    wfOspfAreaRangeEntry.setStatus("mandatory")


class _WfOspfAreaRangeDelete_Type(Integer32):
    """Custom type wfOspfAreaRangeDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOspfAreaRangeDelete_Type.__name__ = "Integer32"
_WfOspfAreaRangeDelete_Object = MibTableColumn
wfOspfAreaRangeDelete = _WfOspfAreaRangeDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 4, 1, 1),
    _WfOspfAreaRangeDelete_Type()
)
wfOspfAreaRangeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfAreaRangeDelete.setStatus("mandatory")


class _WfOspfAreaRangeDisable_Type(Integer32):
    """Custom type wfOspfAreaRangeDisable based on Integer32"""
    defaultValue = 1

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


_WfOspfAreaRangeDisable_Type.__name__ = "Integer32"
_WfOspfAreaRangeDisable_Object = MibTableColumn
wfOspfAreaRangeDisable = _WfOspfAreaRangeDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 4, 1, 2),
    _WfOspfAreaRangeDisable_Type()
)
wfOspfAreaRangeDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfAreaRangeDisable.setStatus("mandatory")


class _WfOspfAreaRangeState_Type(Integer32):
    """Custom type wfOspfAreaRangeState based on Integer32"""
    defaultValue = 2

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


_WfOspfAreaRangeState_Type.__name__ = "Integer32"
_WfOspfAreaRangeState_Object = MibTableColumn
wfOspfAreaRangeState = _WfOspfAreaRangeState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 4, 1, 3),
    _WfOspfAreaRangeState_Type()
)
wfOspfAreaRangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfAreaRangeState.setStatus("mandatory")
_WfOspfAreaRangeAreaID_Type = IpAddress
_WfOspfAreaRangeAreaID_Object = MibTableColumn
wfOspfAreaRangeAreaID = _WfOspfAreaRangeAreaID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 4, 1, 4),
    _WfOspfAreaRangeAreaID_Type()
)
wfOspfAreaRangeAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfAreaRangeAreaID.setStatus("mandatory")
_WfOspfAreaRangeNet_Type = IpAddress
_WfOspfAreaRangeNet_Object = MibTableColumn
wfOspfAreaRangeNet = _WfOspfAreaRangeNet_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 4, 1, 5),
    _WfOspfAreaRangeNet_Type()
)
wfOspfAreaRangeNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfAreaRangeNet.setStatus("mandatory")
_WfOspfAreaRangeMask_Type = IpAddress
_WfOspfAreaRangeMask_Object = MibTableColumn
wfOspfAreaRangeMask = _WfOspfAreaRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 4, 1, 6),
    _WfOspfAreaRangeMask_Type()
)
wfOspfAreaRangeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfAreaRangeMask.setStatus("mandatory")
_WfOspfIfTable_Object = MibTable
wfOspfIfTable = _WfOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5)
)
if mibBuilder.loadTexts:
    wfOspfIfTable.setStatus("mandatory")
_WfOspfIfEntry_Object = MibTableRow
wfOspfIfEntry = _WfOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1)
)
wfOspfIfEntry.setIndexNames(
    (0, "RFC7777-MIB", "wfOspfIfIpAddress"),
    (0, "RFC7777-MIB", "wfOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    wfOspfIfEntry.setStatus("mandatory")


class _WfOspfIfDelete_Type(Integer32):
    """Custom type wfOspfIfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOspfIfDelete_Type.__name__ = "Integer32"
_WfOspfIfDelete_Object = MibTableColumn
wfOspfIfDelete = _WfOspfIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 1),
    _WfOspfIfDelete_Type()
)
wfOspfIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfDelete.setStatus("mandatory")


class _WfOspfIfDisable_Type(Integer32):
    """Custom type wfOspfIfDisable based on Integer32"""
    defaultValue = 1

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


_WfOspfIfDisable_Type.__name__ = "Integer32"
_WfOspfIfDisable_Object = MibTableColumn
wfOspfIfDisable = _WfOspfIfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 2),
    _WfOspfIfDisable_Type()
)
wfOspfIfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfDisable.setStatus("mandatory")


class _WfOspfIfState_Type(Integer32):
    """Custom type wfOspfIfState based on Integer32"""
    defaultValue = 1

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
        *(("backupdesignatedrouter", 6),
          ("designatedrouter", 5),
          ("down", 1),
          ("loopback", 2),
          ("otherdesignatedrouter", 7),
          ("pointtopoint", 4),
          ("waiting", 3))
    )


_WfOspfIfState_Type.__name__ = "Integer32"
_WfOspfIfState_Object = MibTableColumn
wfOspfIfState = _WfOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 3),
    _WfOspfIfState_Type()
)
wfOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfState.setStatus("mandatory")
_WfOspfIfIpAddress_Type = IpAddress
_WfOspfIfIpAddress_Object = MibTableColumn
wfOspfIfIpAddress = _WfOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 4),
    _WfOspfIfIpAddress_Type()
)
wfOspfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfIpAddress.setStatus("mandatory")
_WfOspfAddressLessIf_Type = Integer32
_WfOspfAddressLessIf_Object = MibTableColumn
wfOspfAddressLessIf = _WfOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 5),
    _WfOspfAddressLessIf_Type()
)
wfOspfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfAddressLessIf.setStatus("mandatory")
_WfOspfIfAreaId_Type = IpAddress
_WfOspfIfAreaId_Object = MibTableColumn
wfOspfIfAreaId = _WfOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 6),
    _WfOspfIfAreaId_Type()
)
wfOspfIfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfAreaId.setStatus("mandatory")


class _WfOspfIfType_Type(Integer32):
    """Custom type wfOspfIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nbma", 2),
          ("pointtopoint", 3))
    )


_WfOspfIfType_Type.__name__ = "Integer32"
_WfOspfIfType_Object = MibTableColumn
wfOspfIfType = _WfOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 7),
    _WfOspfIfType_Type()
)
wfOspfIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfType.setStatus("mandatory")


class _WfOspfIfRtrPriority_Type(Integer32):
    """Custom type wfOspfIfRtrPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("defval", 1),
          ("maximum", 255))
    )


_WfOspfIfRtrPriority_Type.__name__ = "Integer32"
_WfOspfIfRtrPriority_Object = MibTableColumn
wfOspfIfRtrPriority = _WfOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 8),
    _WfOspfIfRtrPriority_Type()
)
wfOspfIfRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfRtrPriority.setStatus("mandatory")


class _WfOspfIfTransitDelay_Type(Integer32):
    """Custom type wfOspfIfTransitDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3600)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 3600),
          ("minimum", 1))
    )


_WfOspfIfTransitDelay_Type.__name__ = "Integer32"
_WfOspfIfTransitDelay_Object = MibTableColumn
wfOspfIfTransitDelay = _WfOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 9),
    _WfOspfIfTransitDelay_Type()
)
wfOspfIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfTransitDelay.setStatus("mandatory")


class _WfOspfIfRetransInterval_Type(Integer32):
    """Custom type wfOspfIfRetransInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              3600)
        )
    )
    namedValues = NamedValues(
        *(("defval", 5),
          ("maximum", 3600),
          ("minimum", 1))
    )


_WfOspfIfRetransInterval_Type.__name__ = "Integer32"
_WfOspfIfRetransInterval_Object = MibTableColumn
wfOspfIfRetransInterval = _WfOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 10),
    _WfOspfIfRetransInterval_Type()
)
wfOspfIfRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfRetransInterval.setStatus("mandatory")


class _WfOspfIfHelloInterval_Type(Integer32):
    """Custom type wfOspfIfHelloInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("defval", 10),
          ("maximum", 65535),
          ("minimum", 1))
    )


_WfOspfIfHelloInterval_Type.__name__ = "Integer32"
_WfOspfIfHelloInterval_Object = MibTableColumn
wfOspfIfHelloInterval = _WfOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 11),
    _WfOspfIfHelloInterval_Type()
)
wfOspfIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfHelloInterval.setStatus("mandatory")


class _WfOspfIfRtrDeadInterval_Type(Integer32):
    """Custom type wfOspfIfRtrDeadInterval based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              40,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("defval", 40),
          ("maximum", 2147483647),
          ("minimum", 1))
    )


_WfOspfIfRtrDeadInterval_Type.__name__ = "Integer32"
_WfOspfIfRtrDeadInterval_Object = MibTableColumn
wfOspfIfRtrDeadInterval = _WfOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 12),
    _WfOspfIfRtrDeadInterval_Type()
)
wfOspfIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfRtrDeadInterval.setStatus("mandatory")


class _WfOspfIfPollInterval_Type(Integer32):
    """Custom type wfOspfIfPollInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              120,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("defval", 120),
          ("maximum", 2147483647),
          ("minimum", 1))
    )


_WfOspfIfPollInterval_Type.__name__ = "Integer32"
_WfOspfIfPollInterval_Object = MibTableColumn
wfOspfIfPollInterval = _WfOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 13),
    _WfOspfIfPollInterval_Type()
)
wfOspfIfPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfPollInterval.setStatus("mandatory")
_WfOspfIfDesignatedRouter_Type = IpAddress
_WfOspfIfDesignatedRouter_Object = MibTableColumn
wfOspfIfDesignatedRouter = _WfOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 14),
    _WfOspfIfDesignatedRouter_Type()
)
wfOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfDesignatedRouter.setStatus("mandatory")
_WfOspfIfBackupDesignatedRouter_Type = IpAddress
_WfOspfIfBackupDesignatedRouter_Object = MibTableColumn
wfOspfIfBackupDesignatedRouter = _WfOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 15),
    _WfOspfIfBackupDesignatedRouter_Type()
)
wfOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfBackupDesignatedRouter.setStatus("mandatory")


class _WfOspfIfMetricCost_Type(Integer32):
    """Custom type wfOspfIfMetricCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 65535),
          ("minimum", 1))
    )


_WfOspfIfMetricCost_Type.__name__ = "Integer32"
_WfOspfIfMetricCost_Object = MibTableColumn
wfOspfIfMetricCost = _WfOspfIfMetricCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 16),
    _WfOspfIfMetricCost_Type()
)
wfOspfIfMetricCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfMetricCost.setStatus("mandatory")
_WfOspfIfAuthKey_Type = OctetString
_WfOspfIfAuthKey_Object = MibTableColumn
wfOspfIfAuthKey = _WfOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 17),
    _WfOspfIfAuthKey_Type()
)
wfOspfIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfAuthKey.setStatus("mandatory")
_WfOspfIfTxHellos_Type = Counter32
_WfOspfIfTxHellos_Object = MibTableColumn
wfOspfIfTxHellos = _WfOspfIfTxHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 18),
    _WfOspfIfTxHellos_Type()
)
wfOspfIfTxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfTxHellos.setStatus("mandatory")
_WfOspfIfTxDBDescripts_Type = Counter32
_WfOspfIfTxDBDescripts_Object = MibTableColumn
wfOspfIfTxDBDescripts = _WfOspfIfTxDBDescripts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 19),
    _WfOspfIfTxDBDescripts_Type()
)
wfOspfIfTxDBDescripts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfTxDBDescripts.setStatus("mandatory")
_WfOspfIfTxLinkStateReqs_Type = Counter32
_WfOspfIfTxLinkStateReqs_Object = MibTableColumn
wfOspfIfTxLinkStateReqs = _WfOspfIfTxLinkStateReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 20),
    _WfOspfIfTxLinkStateReqs_Type()
)
wfOspfIfTxLinkStateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfTxLinkStateReqs.setStatus("mandatory")
_WfOspfIfTxLinkStateUpds_Type = Counter32
_WfOspfIfTxLinkStateUpds_Object = MibTableColumn
wfOspfIfTxLinkStateUpds = _WfOspfIfTxLinkStateUpds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 21),
    _WfOspfIfTxLinkStateUpds_Type()
)
wfOspfIfTxLinkStateUpds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfTxLinkStateUpds.setStatus("mandatory")
_WfOspfIfTxLinkStateAcks_Type = Counter32
_WfOspfIfTxLinkStateAcks_Object = MibTableColumn
wfOspfIfTxLinkStateAcks = _WfOspfIfTxLinkStateAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 22),
    _WfOspfIfTxLinkStateAcks_Type()
)
wfOspfIfTxLinkStateAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfTxLinkStateAcks.setStatus("mandatory")
_WfOspfIfRxHellos_Type = Counter32
_WfOspfIfRxHellos_Object = MibTableColumn
wfOspfIfRxHellos = _WfOspfIfRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 23),
    _WfOspfIfRxHellos_Type()
)
wfOspfIfRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfRxHellos.setStatus("mandatory")
_WfOspfIfRxDBDescripts_Type = Counter32
_WfOspfIfRxDBDescripts_Object = MibTableColumn
wfOspfIfRxDBDescripts = _WfOspfIfRxDBDescripts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 24),
    _WfOspfIfRxDBDescripts_Type()
)
wfOspfIfRxDBDescripts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfRxDBDescripts.setStatus("mandatory")
_WfOspfIfRxLinkStateReqs_Type = Counter32
_WfOspfIfRxLinkStateReqs_Object = MibTableColumn
wfOspfIfRxLinkStateReqs = _WfOspfIfRxLinkStateReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 25),
    _WfOspfIfRxLinkStateReqs_Type()
)
wfOspfIfRxLinkStateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfRxLinkStateReqs.setStatus("mandatory")
_WfOspfIfRxLinkStateUpds_Type = Counter32
_WfOspfIfRxLinkStateUpds_Object = MibTableColumn
wfOspfIfRxLinkStateUpds = _WfOspfIfRxLinkStateUpds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 26),
    _WfOspfIfRxLinkStateUpds_Type()
)
wfOspfIfRxLinkStateUpds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfRxLinkStateUpds.setStatus("mandatory")
_WfOspfIfRxLinkStateAcks_Type = Counter32
_WfOspfIfRxLinkStateAcks_Object = MibTableColumn
wfOspfIfRxLinkStateAcks = _WfOspfIfRxLinkStateAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 27),
    _WfOspfIfRxLinkStateAcks_Type()
)
wfOspfIfRxLinkStateAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfRxLinkStateAcks.setStatus("mandatory")
_WfOspfIfDrops_Type = Counter32
_WfOspfIfDrops_Object = MibTableColumn
wfOspfIfDrops = _WfOspfIfDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 28),
    _WfOspfIfDrops_Type()
)
wfOspfIfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfDrops.setStatus("mandatory")


class _WfOspfMtuSize_Type(Integer32):
    """Custom type wfOspfMtuSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10000)
        )
    )
    namedValues = NamedValues(
        *(("defval", 1),
          ("maximum", 10000),
          ("min", 2))
    )


_WfOspfMtuSize_Type.__name__ = "Integer32"
_WfOspfMtuSize_Object = MibTableColumn
wfOspfMtuSize = _WfOspfMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 29),
    _WfOspfMtuSize_Type()
)
wfOspfMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfMtuSize.setStatus("mandatory")
_WfOspfVirtIfTable_Object = MibTable
wfOspfVirtIfTable = _WfOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6)
)
if mibBuilder.loadTexts:
    wfOspfVirtIfTable.setStatus("mandatory")
_WfOspfVirtIfEntry_Object = MibTableRow
wfOspfVirtIfEntry = _WfOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1)
)
wfOspfVirtIfEntry.setIndexNames(
    (0, "RFC7777-MIB", "wfOspfVirtIfAreaID"),
    (0, "RFC7777-MIB", "wfOspfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    wfOspfVirtIfEntry.setStatus("mandatory")


class _WfOspfVirtIfDelete_Type(Integer32):
    """Custom type wfOspfVirtIfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOspfVirtIfDelete_Type.__name__ = "Integer32"
_WfOspfVirtIfDelete_Object = MibTableColumn
wfOspfVirtIfDelete = _WfOspfVirtIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 1),
    _WfOspfVirtIfDelete_Type()
)
wfOspfVirtIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfVirtIfDelete.setStatus("mandatory")


class _WfOspfVirtIfDisable_Type(Integer32):
    """Custom type wfOspfVirtIfDisable based on Integer32"""
    defaultValue = 1

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


_WfOspfVirtIfDisable_Type.__name__ = "Integer32"
_WfOspfVirtIfDisable_Object = MibTableColumn
wfOspfVirtIfDisable = _WfOspfVirtIfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 2),
    _WfOspfVirtIfDisable_Type()
)
wfOspfVirtIfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfVirtIfDisable.setStatus("mandatory")


class _WfOspfVirtIfState_Type(Integer32):
    """Custom type wfOspfVirtIfState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pointtopoint", 4))
    )


_WfOspfVirtIfState_Type.__name__ = "Integer32"
_WfOspfVirtIfState_Object = MibTableColumn
wfOspfVirtIfState = _WfOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 3),
    _WfOspfVirtIfState_Type()
)
wfOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfState.setStatus("mandatory")
_WfOspfVirtIfAreaID_Type = IpAddress
_WfOspfVirtIfAreaID_Object = MibTableColumn
wfOspfVirtIfAreaID = _WfOspfVirtIfAreaID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 4),
    _WfOspfVirtIfAreaID_Type()
)
wfOspfVirtIfAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfAreaID.setStatus("mandatory")
_WfOspfVirtIfNeighbor_Type = IpAddress
_WfOspfVirtIfNeighbor_Object = MibTableColumn
wfOspfVirtIfNeighbor = _WfOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 5),
    _WfOspfVirtIfNeighbor_Type()
)
wfOspfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfNeighbor.setStatus("mandatory")


class _WfOspfVirtIfTransitDelay_Type(Integer32):
    """Custom type wfOspfVirtIfTransitDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3600)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 3600),
          ("minimum", 1))
    )


_WfOspfVirtIfTransitDelay_Type.__name__ = "Integer32"
_WfOspfVirtIfTransitDelay_Object = MibTableColumn
wfOspfVirtIfTransitDelay = _WfOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 6),
    _WfOspfVirtIfTransitDelay_Type()
)
wfOspfVirtIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfVirtIfTransitDelay.setStatus("mandatory")


class _WfOspfVirtIfRetransInterval_Type(Integer32):
    """Custom type wfOspfVirtIfRetransInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              3600)
        )
    )
    namedValues = NamedValues(
        *(("defval", 5),
          ("maximum", 3600),
          ("minimum", 1))
    )


_WfOspfVirtIfRetransInterval_Type.__name__ = "Integer32"
_WfOspfVirtIfRetransInterval_Object = MibTableColumn
wfOspfVirtIfRetransInterval = _WfOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 7),
    _WfOspfVirtIfRetransInterval_Type()
)
wfOspfVirtIfRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfVirtIfRetransInterval.setStatus("mandatory")


class _WfOspfVirtIfHelloInterval_Type(Integer32):
    """Custom type wfOspfVirtIfHelloInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              15,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("defval", 15),
          ("maximum", 65535),
          ("minimum", 1))
    )


_WfOspfVirtIfHelloInterval_Type.__name__ = "Integer32"
_WfOspfVirtIfHelloInterval_Object = MibTableColumn
wfOspfVirtIfHelloInterval = _WfOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 8),
    _WfOspfVirtIfHelloInterval_Type()
)
wfOspfVirtIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfVirtIfHelloInterval.setStatus("mandatory")


class _WfOspfVirtIfRtrDeadInterval_Type(Integer32):
    """Custom type wfOspfVirtIfRtrDeadInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              60,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("defval", 60),
          ("maximum", 2147483647),
          ("minimum", 1))
    )


_WfOspfVirtIfRtrDeadInterval_Type.__name__ = "Integer32"
_WfOspfVirtIfRtrDeadInterval_Object = MibTableColumn
wfOspfVirtIfRtrDeadInterval = _WfOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 9),
    _WfOspfVirtIfRtrDeadInterval_Type()
)
wfOspfVirtIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfVirtIfRtrDeadInterval.setStatus("mandatory")
_WfOspfVirtIfAuthKey_Type = OctetString
_WfOspfVirtIfAuthKey_Object = MibTableColumn
wfOspfVirtIfAuthKey = _WfOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 10),
    _WfOspfVirtIfAuthKey_Type()
)
wfOspfVirtIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfVirtIfAuthKey.setStatus("mandatory")
_WfOspfVirtIfTxHellos_Type = Counter32
_WfOspfVirtIfTxHellos_Object = MibTableColumn
wfOspfVirtIfTxHellos = _WfOspfVirtIfTxHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 11),
    _WfOspfVirtIfTxHellos_Type()
)
wfOspfVirtIfTxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfTxHellos.setStatus("mandatory")
_WfOspfVirtIfTxDBDescripts_Type = Counter32
_WfOspfVirtIfTxDBDescripts_Object = MibTableColumn
wfOspfVirtIfTxDBDescripts = _WfOspfVirtIfTxDBDescripts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 12),
    _WfOspfVirtIfTxDBDescripts_Type()
)
wfOspfVirtIfTxDBDescripts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfTxDBDescripts.setStatus("mandatory")
_WfOspfVirtIfTxLinkStateReqs_Type = Counter32
_WfOspfVirtIfTxLinkStateReqs_Object = MibTableColumn
wfOspfVirtIfTxLinkStateReqs = _WfOspfVirtIfTxLinkStateReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 13),
    _WfOspfVirtIfTxLinkStateReqs_Type()
)
wfOspfVirtIfTxLinkStateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfTxLinkStateReqs.setStatus("mandatory")
_WfOspfVirtIfTxLinkStateUpds_Type = Counter32
_WfOspfVirtIfTxLinkStateUpds_Object = MibTableColumn
wfOspfVirtIfTxLinkStateUpds = _WfOspfVirtIfTxLinkStateUpds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 14),
    _WfOspfVirtIfTxLinkStateUpds_Type()
)
wfOspfVirtIfTxLinkStateUpds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfTxLinkStateUpds.setStatus("mandatory")
_WfOspfVirtIfTxLinkStateAcks_Type = Counter32
_WfOspfVirtIfTxLinkStateAcks_Object = MibTableColumn
wfOspfVirtIfTxLinkStateAcks = _WfOspfVirtIfTxLinkStateAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 15),
    _WfOspfVirtIfTxLinkStateAcks_Type()
)
wfOspfVirtIfTxLinkStateAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfTxLinkStateAcks.setStatus("mandatory")
_WfOspfVirtIfRxHellos_Type = Counter32
_WfOspfVirtIfRxHellos_Object = MibTableColumn
wfOspfVirtIfRxHellos = _WfOspfVirtIfRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 16),
    _WfOspfVirtIfRxHellos_Type()
)
wfOspfVirtIfRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfRxHellos.setStatus("mandatory")
_WfOspfVirtIfRxDBDescripts_Type = Counter32
_WfOspfVirtIfRxDBDescripts_Object = MibTableColumn
wfOspfVirtIfRxDBDescripts = _WfOspfVirtIfRxDBDescripts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 17),
    _WfOspfVirtIfRxDBDescripts_Type()
)
wfOspfVirtIfRxDBDescripts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfRxDBDescripts.setStatus("mandatory")
_WfOspfVirtIfRxLinkStateReqs_Type = Counter32
_WfOspfVirtIfRxLinkStateReqs_Object = MibTableColumn
wfOspfVirtIfRxLinkStateReqs = _WfOspfVirtIfRxLinkStateReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 18),
    _WfOspfVirtIfRxLinkStateReqs_Type()
)
wfOspfVirtIfRxLinkStateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfRxLinkStateReqs.setStatus("mandatory")
_WfOspfVirtIfRxLinkStateUpds_Type = Counter32
_WfOspfVirtIfRxLinkStateUpds_Object = MibTableColumn
wfOspfVirtIfRxLinkStateUpds = _WfOspfVirtIfRxLinkStateUpds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 19),
    _WfOspfVirtIfRxLinkStateUpds_Type()
)
wfOspfVirtIfRxLinkStateUpds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfRxLinkStateUpds.setStatus("mandatory")
_WfOspfVirtIfRxLinkStateAcks_Type = Counter32
_WfOspfVirtIfRxLinkStateAcks_Object = MibTableColumn
wfOspfVirtIfRxLinkStateAcks = _WfOspfVirtIfRxLinkStateAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 20),
    _WfOspfVirtIfRxLinkStateAcks_Type()
)
wfOspfVirtIfRxLinkStateAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfRxLinkStateAcks.setStatus("mandatory")
_WfOspfVirtIfDrops_Type = Counter32
_WfOspfVirtIfDrops_Object = MibTableColumn
wfOspfVirtIfDrops = _WfOspfVirtIfDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 21),
    _WfOspfVirtIfDrops_Type()
)
wfOspfVirtIfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfDrops.setStatus("mandatory")
_WfOspfNbrTable_Object = MibTable
wfOspfNbrTable = _WfOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7)
)
if mibBuilder.loadTexts:
    wfOspfNbrTable.setStatus("mandatory")
_WfOspfNbrEntry_Object = MibTableRow
wfOspfNbrEntry = _WfOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1)
)
wfOspfNbrEntry.setIndexNames(
    (0, "RFC7777-MIB", "wfOspfNbrIpAddr"),
    (0, "RFC7777-MIB", "wfOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    wfOspfNbrEntry.setStatus("mandatory")


class _WfOspfNbrDelete_Type(Integer32):
    """Custom type wfOspfNbrDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOspfNbrDelete_Type.__name__ = "Integer32"
_WfOspfNbrDelete_Object = MibTableColumn
wfOspfNbrDelete = _WfOspfNbrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 1),
    _WfOspfNbrDelete_Type()
)
wfOspfNbrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfNbrDelete.setStatus("mandatory")


class _WfOspfNbrDisable_Type(Integer32):
    """Custom type wfOspfNbrDisable based on Integer32"""
    defaultValue = 1

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


_WfOspfNbrDisable_Type.__name__ = "Integer32"
_WfOspfNbrDisable_Object = MibTableColumn
wfOspfNbrDisable = _WfOspfNbrDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 2),
    _WfOspfNbrDisable_Type()
)
wfOspfNbrDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfNbrDisable.setStatus("mandatory")


class _WfOspfNbrState_Type(Integer32):
    """Custom type wfOspfNbrState based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("attempt", 2),
          ("down", 1),
          ("exchange", 6),
          ("exchangstart", 5),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("twoway", 4))
    )


_WfOspfNbrState_Type.__name__ = "Integer32"
_WfOspfNbrState_Object = MibTableColumn
wfOspfNbrState = _WfOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 3),
    _WfOspfNbrState_Type()
)
wfOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfNbrState.setStatus("mandatory")
_WfOspfNbrIpAddr_Type = IpAddress
_WfOspfNbrIpAddr_Object = MibTableColumn
wfOspfNbrIpAddr = _WfOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 4),
    _WfOspfNbrIpAddr_Type()
)
wfOspfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfNbrIpAddr.setStatus("mandatory")
_WfOspfNbrIfAddr_Type = IpAddress
_WfOspfNbrIfAddr_Object = MibTableColumn
wfOspfNbrIfAddr = _WfOspfNbrIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 5),
    _WfOspfNbrIfAddr_Type()
)
wfOspfNbrIfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfNbrIfAddr.setStatus("mandatory")
_WfOspfNbrAddressLessIndex_Type = Integer32
_WfOspfNbrAddressLessIndex_Object = MibTableColumn
wfOspfNbrAddressLessIndex = _WfOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 6),
    _WfOspfNbrAddressLessIndex_Type()
)
wfOspfNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfNbrAddressLessIndex.setStatus("mandatory")
_WfOspfNbrRtrId_Type = IpAddress
_WfOspfNbrRtrId_Object = MibTableColumn
wfOspfNbrRtrId = _WfOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 7),
    _WfOspfNbrRtrId_Type()
)
wfOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfNbrRtrId.setStatus("mandatory")
_WfOspfNbrOptions_Type = Integer32
_WfOspfNbrOptions_Object = MibTableColumn
wfOspfNbrOptions = _WfOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 8),
    _WfOspfNbrOptions_Type()
)
wfOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfNbrOptions.setStatus("mandatory")


class _WfOspfNbrPriority_Type(Integer32):
    """Custom type wfOspfNbrPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("defval", 1),
          ("maximum", 255))
    )


_WfOspfNbrPriority_Type.__name__ = "Integer32"
_WfOspfNbrPriority_Object = MibTableColumn
wfOspfNbrPriority = _WfOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 9),
    _WfOspfNbrPriority_Type()
)
wfOspfNbrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfNbrPriority.setStatus("mandatory")
_WfOspfNbrEvents_Type = Counter32
_WfOspfNbrEvents_Object = MibTableColumn
wfOspfNbrEvents = _WfOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 10),
    _WfOspfNbrEvents_Type()
)
wfOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfNbrEvents.setStatus("mandatory")
_WfOspfNbrLSRetransQLen_Type = Gauge32
_WfOspfNbrLSRetransQLen_Object = MibTableColumn
wfOspfNbrLSRetransQLen = _WfOspfNbrLSRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 11),
    _WfOspfNbrLSRetransQLen_Type()
)
wfOspfNbrLSRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfNbrLSRetransQLen.setStatus("mandatory")
_WfOspfVirtNbrTable_Object = MibTable
wfOspfVirtNbrTable = _WfOspfVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8)
)
if mibBuilder.loadTexts:
    wfOspfVirtNbrTable.setStatus("mandatory")
_WfOspfVirtNbrEntry_Object = MibTableRow
wfOspfVirtNbrEntry = _WfOspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8, 1)
)
wfOspfVirtNbrEntry.setIndexNames(
    (0, "RFC7777-MIB", "wfOspfVirtNbrArea"),
    (0, "RFC7777-MIB", "wfOspfVirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    wfOspfVirtNbrEntry.setStatus("mandatory")
_WfOspfVirtNbrArea_Type = IpAddress
_WfOspfVirtNbrArea_Object = MibTableColumn
wfOspfVirtNbrArea = _WfOspfVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8, 1, 1),
    _WfOspfVirtNbrArea_Type()
)
wfOspfVirtNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtNbrArea.setStatus("mandatory")
_WfOspfVirtNbrRtrId_Type = IpAddress
_WfOspfVirtNbrRtrId_Object = MibTableColumn
wfOspfVirtNbrRtrId = _WfOspfVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8, 1, 2),
    _WfOspfVirtNbrRtrId_Type()
)
wfOspfVirtNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtNbrRtrId.setStatus("mandatory")
_WfOspfVirtNbrIpAddr_Type = IpAddress
_WfOspfVirtNbrIpAddr_Object = MibTableColumn
wfOspfVirtNbrIpAddr = _WfOspfVirtNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8, 1, 3),
    _WfOspfVirtNbrIpAddr_Type()
)
wfOspfVirtNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtNbrIpAddr.setStatus("mandatory")
_WfOspfVirtNbrOptions_Type = Integer32
_WfOspfVirtNbrOptions_Object = MibTableColumn
wfOspfVirtNbrOptions = _WfOspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8, 1, 4),
    _WfOspfVirtNbrOptions_Type()
)
wfOspfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtNbrOptions.setStatus("mandatory")


class _WfOspfVirtNbrState_Type(Integer32):
    """Custom type wfOspfVirtNbrState based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("attempt", 2),
          ("down", 1),
          ("exchange", 6),
          ("exchangstart", 5),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("twoway", 4))
    )


_WfOspfVirtNbrState_Type.__name__ = "Integer32"
_WfOspfVirtNbrState_Object = MibTableColumn
wfOspfVirtNbrState = _WfOspfVirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8, 1, 5),
    _WfOspfVirtNbrState_Type()
)
wfOspfVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtNbrState.setStatus("mandatory")
_WfOspfVirtNbrEvents_Type = Counter32
_WfOspfVirtNbrEvents_Object = MibTableColumn
wfOspfVirtNbrEvents = _WfOspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8, 1, 6),
    _WfOspfVirtNbrEvents_Type()
)
wfOspfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtNbrEvents.setStatus("mandatory")
_WfOspfVirtNbrLSRetransQLen_Type = Gauge32
_WfOspfVirtNbrLSRetransQLen_Object = MibTableColumn
wfOspfVirtNbrLSRetransQLen = _WfOspfVirtNbrLSRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8, 1, 7),
    _WfOspfVirtNbrLSRetransQLen_Type()
)
wfOspfVirtNbrLSRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtNbrLSRetransQLen.setStatus("mandatory")
_WfOspfDynNbrTable_Object = MibTable
wfOspfDynNbrTable = _WfOspfDynNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9)
)
if mibBuilder.loadTexts:
    wfOspfDynNbrTable.setStatus("mandatory")
_WfOspfDynNbrEntry_Object = MibTableRow
wfOspfDynNbrEntry = _WfOspfDynNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1)
)
wfOspfDynNbrEntry.setIndexNames(
    (0, "RFC7777-MIB", "wfOspfDynNbrIpAddr"),
    (0, "RFC7777-MIB", "wfOspfDynNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    wfOspfDynNbrEntry.setStatus("mandatory")


class _WfOspfDynNbrState_Type(Integer32):
    """Custom type wfOspfDynNbrState based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("attempt", 2),
          ("down", 1),
          ("exchange", 6),
          ("exchangstart", 5),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("twoway", 4))
    )


_WfOspfDynNbrState_Type.__name__ = "Integer32"
_WfOspfDynNbrState_Object = MibTableColumn
wfOspfDynNbrState = _WfOspfDynNbrState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 1),
    _WfOspfDynNbrState_Type()
)
wfOspfDynNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrState.setStatus("mandatory")
_WfOspfDynNbrIpAddr_Type = IpAddress
_WfOspfDynNbrIpAddr_Object = MibTableColumn
wfOspfDynNbrIpAddr = _WfOspfDynNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 2),
    _WfOspfDynNbrIpAddr_Type()
)
wfOspfDynNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrIpAddr.setStatus("mandatory")
_WfOspfDynNbrIfAddr_Type = IpAddress
_WfOspfDynNbrIfAddr_Object = MibTableColumn
wfOspfDynNbrIfAddr = _WfOspfDynNbrIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 3),
    _WfOspfDynNbrIfAddr_Type()
)
wfOspfDynNbrIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrIfAddr.setStatus("mandatory")
_WfOspfDynNbrAddressLessIndex_Type = Integer32
_WfOspfDynNbrAddressLessIndex_Object = MibTableColumn
wfOspfDynNbrAddressLessIndex = _WfOspfDynNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 4),
    _WfOspfDynNbrAddressLessIndex_Type()
)
wfOspfDynNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrAddressLessIndex.setStatus("mandatory")
_WfOspfDynNbrRtrId_Type = IpAddress
_WfOspfDynNbrRtrId_Object = MibTableColumn
wfOspfDynNbrRtrId = _WfOspfDynNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 5),
    _WfOspfDynNbrRtrId_Type()
)
wfOspfDynNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrRtrId.setStatus("mandatory")
_WfOspfDynNbrOptions_Type = Integer32
_WfOspfDynNbrOptions_Object = MibTableColumn
wfOspfDynNbrOptions = _WfOspfDynNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 6),
    _WfOspfDynNbrOptions_Type()
)
wfOspfDynNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrOptions.setStatus("mandatory")
_WfOspfDynNbrPriority_Type = Integer32
_WfOspfDynNbrPriority_Object = MibTableColumn
wfOspfDynNbrPriority = _WfOspfDynNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 7),
    _WfOspfDynNbrPriority_Type()
)
wfOspfDynNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrPriority.setStatus("mandatory")
_WfOspfDynNbrEvents_Type = Counter32
_WfOspfDynNbrEvents_Object = MibTableColumn
wfOspfDynNbrEvents = _WfOspfDynNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 8),
    _WfOspfDynNbrEvents_Type()
)
wfOspfDynNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrEvents.setStatus("mandatory")
_WfOspfDynNbrLSRetransQLen_Type = Gauge32
_WfOspfDynNbrLSRetransQLen_Object = MibTableColumn
wfOspfDynNbrLSRetransQLen = _WfOspfDynNbrLSRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 9),
    _WfOspfDynNbrLSRetransQLen_Type()
)
wfOspfDynNbrLSRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrLSRetransQLen.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC7777-MIB",
    **{"wellfleet": wellfleet,
       "wfOspfGeneralGroup": wfOspfGeneralGroup,
       "wfOspfGeneralDelete": wfOspfGeneralDelete,
       "wfOspfGeneralDisable": wfOspfGeneralDisable,
       "wfOspfGeneralState": wfOspfGeneralState,
       "wfOspfRouterId": wfOspfRouterId,
       "wfOspfVersionNumber": wfOspfVersionNumber,
       "wfOspfAreaBdrRtrStatus": wfOspfAreaBdrRtrStatus,
       "wfOspfASBdrRtrStatus": wfOspfASBdrRtrStatus,
       "wfOspfTOSSupport": wfOspfTOSSupport,
       "wfOspfSpfHoldDown": wfOspfSpfHoldDown,
       "wfOspfSlotMask": wfOspfSlotMask,
       "wfOspfAreaTable": wfOspfAreaTable,
       "wfOspfAreaEntry": wfOspfAreaEntry,
       "wfOspfAreaDelete": wfOspfAreaDelete,
       "wfOspfAreaDisable": wfOspfAreaDisable,
       "wfOspfAreaState": wfOspfAreaState,
       "wfOspfAreaId": wfOspfAreaId,
       "wfOspfAuthType": wfOspfAuthType,
       "wfOspfImportASExtern": wfOspfImportASExtern,
       "wfOspfStubMetric": wfOspfStubMetric,
       "wfOspfImportSum": wfOspfImportSum,
       "wfOspfSpfCnt": wfOspfSpfCnt,
       "wfOspfLsdbTable": wfOspfLsdbTable,
       "wfOspfLsdbEntry": wfOspfLsdbEntry,
       "wfOspfLsdbAreaId": wfOspfLsdbAreaId,
       "wfOspfLsdbType": wfOspfLsdbType,
       "wfOspfLsdbLSID": wfOspfLsdbLSID,
       "wfOspfLsdbRouterId": wfOspfLsdbRouterId,
       "wfOspfLsdbSequence": wfOspfLsdbSequence,
       "wfOspfLsdbAge": wfOspfLsdbAge,
       "wfOspfLsdbChecksum": wfOspfLsdbChecksum,
       "wfOspfLsdbAdvLen": wfOspfLsdbAdvLen,
       "wfOspfAreaRangeTable": wfOspfAreaRangeTable,
       "wfOspfAreaRangeEntry": wfOspfAreaRangeEntry,
       "wfOspfAreaRangeDelete": wfOspfAreaRangeDelete,
       "wfOspfAreaRangeDisable": wfOspfAreaRangeDisable,
       "wfOspfAreaRangeState": wfOspfAreaRangeState,
       "wfOspfAreaRangeAreaID": wfOspfAreaRangeAreaID,
       "wfOspfAreaRangeNet": wfOspfAreaRangeNet,
       "wfOspfAreaRangeMask": wfOspfAreaRangeMask,
       "wfOspfIfTable": wfOspfIfTable,
       "wfOspfIfEntry": wfOspfIfEntry,
       "wfOspfIfDelete": wfOspfIfDelete,
       "wfOspfIfDisable": wfOspfIfDisable,
       "wfOspfIfState": wfOspfIfState,
       "wfOspfIfIpAddress": wfOspfIfIpAddress,
       "wfOspfAddressLessIf": wfOspfAddressLessIf,
       "wfOspfIfAreaId": wfOspfIfAreaId,
       "wfOspfIfType": wfOspfIfType,
       "wfOspfIfRtrPriority": wfOspfIfRtrPriority,
       "wfOspfIfTransitDelay": wfOspfIfTransitDelay,
       "wfOspfIfRetransInterval": wfOspfIfRetransInterval,
       "wfOspfIfHelloInterval": wfOspfIfHelloInterval,
       "wfOspfIfRtrDeadInterval": wfOspfIfRtrDeadInterval,
       "wfOspfIfPollInterval": wfOspfIfPollInterval,
       "wfOspfIfDesignatedRouter": wfOspfIfDesignatedRouter,
       "wfOspfIfBackupDesignatedRouter": wfOspfIfBackupDesignatedRouter,
       "wfOspfIfMetricCost": wfOspfIfMetricCost,
       "wfOspfIfAuthKey": wfOspfIfAuthKey,
       "wfOspfIfTxHellos": wfOspfIfTxHellos,
       "wfOspfIfTxDBDescripts": wfOspfIfTxDBDescripts,
       "wfOspfIfTxLinkStateReqs": wfOspfIfTxLinkStateReqs,
       "wfOspfIfTxLinkStateUpds": wfOspfIfTxLinkStateUpds,
       "wfOspfIfTxLinkStateAcks": wfOspfIfTxLinkStateAcks,
       "wfOspfIfRxHellos": wfOspfIfRxHellos,
       "wfOspfIfRxDBDescripts": wfOspfIfRxDBDescripts,
       "wfOspfIfRxLinkStateReqs": wfOspfIfRxLinkStateReqs,
       "wfOspfIfRxLinkStateUpds": wfOspfIfRxLinkStateUpds,
       "wfOspfIfRxLinkStateAcks": wfOspfIfRxLinkStateAcks,
       "wfOspfIfDrops": wfOspfIfDrops,
       "wfOspfMtuSize": wfOspfMtuSize,
       "wfOspfVirtIfTable": wfOspfVirtIfTable,
       "wfOspfVirtIfEntry": wfOspfVirtIfEntry,
       "wfOspfVirtIfDelete": wfOspfVirtIfDelete,
       "wfOspfVirtIfDisable": wfOspfVirtIfDisable,
       "wfOspfVirtIfState": wfOspfVirtIfState,
       "wfOspfVirtIfAreaID": wfOspfVirtIfAreaID,
       "wfOspfVirtIfNeighbor": wfOspfVirtIfNeighbor,
       "wfOspfVirtIfTransitDelay": wfOspfVirtIfTransitDelay,
       "wfOspfVirtIfRetransInterval": wfOspfVirtIfRetransInterval,
       "wfOspfVirtIfHelloInterval": wfOspfVirtIfHelloInterval,
       "wfOspfVirtIfRtrDeadInterval": wfOspfVirtIfRtrDeadInterval,
       "wfOspfVirtIfAuthKey": wfOspfVirtIfAuthKey,
       "wfOspfVirtIfTxHellos": wfOspfVirtIfTxHellos,
       "wfOspfVirtIfTxDBDescripts": wfOspfVirtIfTxDBDescripts,
       "wfOspfVirtIfTxLinkStateReqs": wfOspfVirtIfTxLinkStateReqs,
       "wfOspfVirtIfTxLinkStateUpds": wfOspfVirtIfTxLinkStateUpds,
       "wfOspfVirtIfTxLinkStateAcks": wfOspfVirtIfTxLinkStateAcks,
       "wfOspfVirtIfRxHellos": wfOspfVirtIfRxHellos,
       "wfOspfVirtIfRxDBDescripts": wfOspfVirtIfRxDBDescripts,
       "wfOspfVirtIfRxLinkStateReqs": wfOspfVirtIfRxLinkStateReqs,
       "wfOspfVirtIfRxLinkStateUpds": wfOspfVirtIfRxLinkStateUpds,
       "wfOspfVirtIfRxLinkStateAcks": wfOspfVirtIfRxLinkStateAcks,
       "wfOspfVirtIfDrops": wfOspfVirtIfDrops,
       "wfOspfNbrTable": wfOspfNbrTable,
       "wfOspfNbrEntry": wfOspfNbrEntry,
       "wfOspfNbrDelete": wfOspfNbrDelete,
       "wfOspfNbrDisable": wfOspfNbrDisable,
       "wfOspfNbrState": wfOspfNbrState,
       "wfOspfNbrIpAddr": wfOspfNbrIpAddr,
       "wfOspfNbrIfAddr": wfOspfNbrIfAddr,
       "wfOspfNbrAddressLessIndex": wfOspfNbrAddressLessIndex,
       "wfOspfNbrRtrId": wfOspfNbrRtrId,
       "wfOspfNbrOptions": wfOspfNbrOptions,
       "wfOspfNbrPriority": wfOspfNbrPriority,
       "wfOspfNbrEvents": wfOspfNbrEvents,
       "wfOspfNbrLSRetransQLen": wfOspfNbrLSRetransQLen,
       "wfOspfVirtNbrTable": wfOspfVirtNbrTable,
       "wfOspfVirtNbrEntry": wfOspfVirtNbrEntry,
       "wfOspfVirtNbrArea": wfOspfVirtNbrArea,
       "wfOspfVirtNbrRtrId": wfOspfVirtNbrRtrId,
       "wfOspfVirtNbrIpAddr": wfOspfVirtNbrIpAddr,
       "wfOspfVirtNbrOptions": wfOspfVirtNbrOptions,
       "wfOspfVirtNbrState": wfOspfVirtNbrState,
       "wfOspfVirtNbrEvents": wfOspfVirtNbrEvents,
       "wfOspfVirtNbrLSRetransQLen": wfOspfVirtNbrLSRetransQLen,
       "wfOspfDynNbrTable": wfOspfDynNbrTable,
       "wfOspfDynNbrEntry": wfOspfDynNbrEntry,
       "wfOspfDynNbrState": wfOspfDynNbrState,
       "wfOspfDynNbrIpAddr": wfOspfDynNbrIpAddr,
       "wfOspfDynNbrIfAddr": wfOspfDynNbrIfAddr,
       "wfOspfDynNbrAddressLessIndex": wfOspfDynNbrAddressLessIndex,
       "wfOspfDynNbrRtrId": wfOspfDynNbrRtrId,
       "wfOspfDynNbrOptions": wfOspfDynNbrOptions,
       "wfOspfDynNbrPriority": wfOspfDynNbrPriority,
       "wfOspfDynNbrEvents": wfOspfDynNbrEvents,
       "wfOspfDynNbrLSRetransQLen": wfOspfDynNbrLSRetransQLen}
)
