# SNMP MIB module (Application-Monitoring-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Application-Monitoring-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:06 2024
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

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SniProductMibs_ObjectIdentity = ObjectIdentity
sniProductMibs = _SniProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2)
)
_SniAppMon_ObjectIdentity = ObjectIdentity
sniAppMon = _SniAppMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 23)
)
_SniAppMonSubSystems_ObjectIdentity = ObjectIdentity
sniAppMonSubSystems = _SniAppMonSubSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 1)
)
_AppMonSubsysTabNum_Type = Integer32
_AppMonSubsysTabNum_Object = MibScalar
appMonSubsysTabNum = _AppMonSubsysTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 1, 1),
    _AppMonSubsysTabNum_Type()
)
appMonSubsysTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonSubsysTabNum.setStatus("mandatory")
_AppMonSubsysTable_Object = MibTable
appMonSubsysTable = _AppMonSubsysTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 1, 2)
)
if mibBuilder.loadTexts:
    appMonSubsysTable.setStatus("mandatory")
_AppMonSubsysEntry_Object = MibTableRow
appMonSubsysEntry = _AppMonSubsysEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 1, 2, 1)
)
appMonSubsysEntry.setIndexNames(
    (0, "Application-Monitoring-MIB", "appMonSubsysIndex"),
)
if mibBuilder.loadTexts:
    appMonSubsysEntry.setStatus("mandatory")
_AppMonSubsysIndex_Type = Integer32
_AppMonSubsysIndex_Object = MibTableColumn
appMonSubsysIndex = _AppMonSubsysIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 1, 2, 1, 1),
    _AppMonSubsysIndex_Type()
)
appMonSubsysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonSubsysIndex.setStatus("mandatory")
_AppMonSubsysName_Type = DisplayString
_AppMonSubsysName_Object = MibTableColumn
appMonSubsysName = _AppMonSubsysName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 1, 2, 1, 2),
    _AppMonSubsysName_Type()
)
appMonSubsysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonSubsysName.setStatus("mandatory")
_AppMonSubsysVersion_Type = DisplayString
_AppMonSubsysVersion_Object = MibTableColumn
appMonSubsysVersion = _AppMonSubsysVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 1, 2, 1, 3),
    _AppMonSubsysVersion_Type()
)
appMonSubsysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonSubsysVersion.setStatus("mandatory")


class _AppMonSubsysState_Type(Integer32):
    """Custom type appMonSubsysState based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("in-create", 4),
          ("in-delete", 3),
          ("in-hold", 6),
          ("in-resume", 5),
          ("locked", 8),
          ("not-created", 2),
          ("not-resumed", 7),
          ("unknown", 255))
    )


_AppMonSubsysState_Type.__name__ = "Integer32"
_AppMonSubsysState_Object = MibTableColumn
appMonSubsysState = _AppMonSubsysState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 1, 2, 1, 4),
    _AppMonSubsysState_Type()
)
appMonSubsysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonSubsysState.setStatus("mandatory")
_AppMonSubsysTasks_Type = Integer32
_AppMonSubsysTasks_Object = MibTableColumn
appMonSubsysTasks = _AppMonSubsysTasks_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 1, 2, 1, 5),
    _AppMonSubsysTasks_Type()
)
appMonSubsysTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonSubsysTasks.setStatus("mandatory")
_SniAppMonBcamAppl_ObjectIdentity = ObjectIdentity
sniAppMonBcamAppl = _SniAppMonBcamAppl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 2)
)
_AppMonBcamApplTabNum_Type = Integer32
_AppMonBcamApplTabNum_Object = MibScalar
appMonBcamApplTabNum = _AppMonBcamApplTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 2, 1),
    _AppMonBcamApplTabNum_Type()
)
appMonBcamApplTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonBcamApplTabNum.setStatus("mandatory")
_AppMonBcamApplTable_Object = MibTable
appMonBcamApplTable = _AppMonBcamApplTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 2, 2)
)
if mibBuilder.loadTexts:
    appMonBcamApplTable.setStatus("mandatory")
_AppMonBcamApplEntry_Object = MibTableRow
appMonBcamApplEntry = _AppMonBcamApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 2, 2, 1)
)
appMonBcamApplEntry.setIndexNames(
    (0, "Application-Monitoring-MIB", "appMonBcamApplIndex"),
)
if mibBuilder.loadTexts:
    appMonBcamApplEntry.setStatus("mandatory")
_AppMonBcamApplIndex_Type = Integer32
_AppMonBcamApplIndex_Object = MibTableColumn
appMonBcamApplIndex = _AppMonBcamApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 2, 2, 1, 1),
    _AppMonBcamApplIndex_Type()
)
appMonBcamApplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonBcamApplIndex.setStatus("mandatory")
_AppMonBcamApplName_Type = DisplayString
_AppMonBcamApplName_Object = MibTableColumn
appMonBcamApplName = _AppMonBcamApplName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 2, 2, 1, 2),
    _AppMonBcamApplName_Type()
)
appMonBcamApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonBcamApplName.setStatus("mandatory")
_AppMonBcamApplVersion_Type = DisplayString
_AppMonBcamApplVersion_Object = MibTableColumn
appMonBcamApplVersion = _AppMonBcamApplVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 2, 2, 1, 3),
    _AppMonBcamApplVersion_Type()
)
appMonBcamApplVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonBcamApplVersion.setStatus("mandatory")


class _AppMonBcamApplState_Type(Integer32):
    """Custom type appMonBcamApplState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 3),
          ("in-hold", 5),
          ("loaded", 4),
          ("running", 1),
          ("scheduled", 6),
          ("terminated", 2),
          ("unknown", 255))
    )


_AppMonBcamApplState_Type.__name__ = "Integer32"
_AppMonBcamApplState_Object = MibTableColumn
appMonBcamApplState = _AppMonBcamApplState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 2, 2, 1, 4),
    _AppMonBcamApplState_Type()
)
appMonBcamApplState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonBcamApplState.setStatus("mandatory")
_AppMonBcamApplMonJV_Type = DisplayString
_AppMonBcamApplMonJV_Object = MibTableColumn
appMonBcamApplMonJV = _AppMonBcamApplMonJV_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 2, 2, 1, 5),
    _AppMonBcamApplMonJV_Type()
)
appMonBcamApplMonJV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonBcamApplMonJV.setStatus("mandatory")
_SniAppMonUserAppl_ObjectIdentity = ObjectIdentity
sniAppMonUserAppl = _SniAppMonUserAppl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 3)
)
_AppMonUserApplTabNum_Type = Integer32
_AppMonUserApplTabNum_Object = MibScalar
appMonUserApplTabNum = _AppMonUserApplTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 3, 1),
    _AppMonUserApplTabNum_Type()
)
appMonUserApplTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonUserApplTabNum.setStatus("mandatory")
_AppMonUserApplTable_Object = MibTable
appMonUserApplTable = _AppMonUserApplTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 3, 2)
)
if mibBuilder.loadTexts:
    appMonUserApplTable.setStatus("mandatory")
_AppMonUserApplEntry_Object = MibTableRow
appMonUserApplEntry = _AppMonUserApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 3, 2, 1)
)
appMonUserApplEntry.setIndexNames(
    (0, "Application-Monitoring-MIB", "appMonUserApplIndex"),
)
if mibBuilder.loadTexts:
    appMonUserApplEntry.setStatus("mandatory")
_AppMonUserApplIndex_Type = Integer32
_AppMonUserApplIndex_Object = MibTableColumn
appMonUserApplIndex = _AppMonUserApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 3, 2, 1, 1),
    _AppMonUserApplIndex_Type()
)
appMonUserApplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonUserApplIndex.setStatus("mandatory")
_AppMonUserApplName_Type = DisplayString
_AppMonUserApplName_Object = MibTableColumn
appMonUserApplName = _AppMonUserApplName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 3, 2, 1, 2),
    _AppMonUserApplName_Type()
)
appMonUserApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonUserApplName.setStatus("mandatory")
_AppMonUserApplVersion_Type = DisplayString
_AppMonUserApplVersion_Object = MibTableColumn
appMonUserApplVersion = _AppMonUserApplVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 3, 2, 1, 3),
    _AppMonUserApplVersion_Type()
)
appMonUserApplVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonUserApplVersion.setStatus("mandatory")


class _AppMonUserApplState_Type(Integer32):
    """Custom type appMonUserApplState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 3),
          ("in-hold", 5),
          ("loaded", 4),
          ("running", 1),
          ("scheduled", 6),
          ("terminated", 2),
          ("unknown", 255))
    )


_AppMonUserApplState_Type.__name__ = "Integer32"
_AppMonUserApplState_Object = MibTableColumn
appMonUserApplState = _AppMonUserApplState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 3, 2, 1, 4),
    _AppMonUserApplState_Type()
)
appMonUserApplState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonUserApplState.setStatus("mandatory")
_AppMonUserApplMonJV_Type = DisplayString
_AppMonUserApplMonJV_Object = MibTableColumn
appMonUserApplMonJV = _AppMonUserApplMonJV_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 3, 2, 1, 5),
    _AppMonUserApplMonJV_Type()
)
appMonUserApplMonJV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonUserApplMonJV.setStatus("mandatory")
_SniAppMonGlobalData_ObjectIdentity = ObjectIdentity
sniAppMonGlobalData = _SniAppMonGlobalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 5)
)
_AppMonVersion_Type = DisplayString
_AppMonVersion_Object = MibScalar
appMonVersion = _AppMonVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 5, 1),
    _AppMonVersion_Type()
)
appMonVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonVersion.setStatus("mandatory")
_AppMonConfFile_Type = DisplayString
_AppMonConfFile_Object = MibScalar
appMonConfFile = _AppMonConfFile_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 5, 2),
    _AppMonConfFile_Type()
)
appMonConfFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appMonConfFile.setStatus("mandatory")


class _AppMonTrapFormat_Type(Integer32):
    """Custom type appMonTrapFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("generic", 1),
          ("tv-cc", 2))
    )


_AppMonTrapFormat_Type.__name__ = "Integer32"
_AppMonTrapFormat_Object = MibScalar
appMonTrapFormat = _AppMonTrapFormat_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 5, 3),
    _AppMonTrapFormat_Type()
)
appMonTrapFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appMonTrapFormat.setStatus("mandatory")
_SniAppMonDcamAppl_ObjectIdentity = ObjectIdentity
sniAppMonDcamAppl = _SniAppMonDcamAppl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 6)
)
_AppMonDcamApplTabNum_Type = Integer32
_AppMonDcamApplTabNum_Object = MibScalar
appMonDcamApplTabNum = _AppMonDcamApplTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 6, 1),
    _AppMonDcamApplTabNum_Type()
)
appMonDcamApplTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonDcamApplTabNum.setStatus("mandatory")
_AppMonDcamApplTable_Object = MibTable
appMonDcamApplTable = _AppMonDcamApplTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 6, 2)
)
if mibBuilder.loadTexts:
    appMonDcamApplTable.setStatus("mandatory")
_AppMonDcamApplEntry_Object = MibTableRow
appMonDcamApplEntry = _AppMonDcamApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 6, 2, 1)
)
appMonDcamApplEntry.setIndexNames(
    (0, "Application-Monitoring-MIB", "appMonDcamApplIndex"),
)
if mibBuilder.loadTexts:
    appMonDcamApplEntry.setStatus("mandatory")
_AppMonDcamApplIndex_Type = Integer32
_AppMonDcamApplIndex_Object = MibTableColumn
appMonDcamApplIndex = _AppMonDcamApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 6, 2, 1, 1),
    _AppMonDcamApplIndex_Type()
)
appMonDcamApplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonDcamApplIndex.setStatus("mandatory")
_AppMonDcamApplName_Type = DisplayString
_AppMonDcamApplName_Object = MibTableColumn
appMonDcamApplName = _AppMonDcamApplName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 6, 2, 1, 2),
    _AppMonDcamApplName_Type()
)
appMonDcamApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonDcamApplName.setStatus("mandatory")
_AppMonDcamApplHost_Type = DisplayString
_AppMonDcamApplHost_Object = MibTableColumn
appMonDcamApplHost = _AppMonDcamApplHost_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 6, 2, 1, 3),
    _AppMonDcamApplHost_Type()
)
appMonDcamApplHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonDcamApplHost.setStatus("mandatory")


class _AppMonDcamApplState_Type(Integer32):
    """Custom type appMonDcamApplState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("terminated", 2),
          ("unknown", 255))
    )


_AppMonDcamApplState_Type.__name__ = "Integer32"
_AppMonDcamApplState_Object = MibTableColumn
appMonDcamApplState = _AppMonDcamApplState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 6, 2, 1, 4),
    _AppMonDcamApplState_Type()
)
appMonDcamApplState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonDcamApplState.setStatus("mandatory")
_AppMonLogfiles_ObjectIdentity = ObjectIdentity
appMonLogfiles = _AppMonLogfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 7)
)
_AppMonLogfTabNum_Type = Integer32
_AppMonLogfTabNum_Object = MibScalar
appMonLogfTabNum = _AppMonLogfTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 7, 1),
    _AppMonLogfTabNum_Type()
)
appMonLogfTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonLogfTabNum.setStatus("mandatory")
_AppMonLogfTable_Object = MibTable
appMonLogfTable = _AppMonLogfTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 7, 2)
)
if mibBuilder.loadTexts:
    appMonLogfTable.setStatus("mandatory")
_AppMonLogfEntry_Object = MibTableRow
appMonLogfEntry = _AppMonLogfEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 7, 2, 1)
)
appMonLogfEntry.setIndexNames(
    (0, "Application-Monitoring-MIB", "appMonLogfName"),
)
if mibBuilder.loadTexts:
    appMonLogfEntry.setStatus("mandatory")
_AppMonLogfName_Type = DisplayString
_AppMonLogfName_Object = MibTableColumn
appMonLogfName = _AppMonLogfName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 7, 2, 1, 1),
    _AppMonLogfName_Type()
)
appMonLogfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonLogfName.setStatus("mandatory")
_AppMonLogfAppl_Type = DisplayString
_AppMonLogfAppl_Object = MibTableColumn
appMonLogfAppl = _AppMonLogfAppl_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 7, 2, 1, 2),
    _AppMonLogfAppl_Type()
)
appMonLogfAppl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonLogfAppl.setStatus("mandatory")


class _AppMonLogfState_Type(Integer32):
    """Custom type appMonLogfState based on Integer32"""
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
        *(("active", 2),
          ("deactive", 1),
          ("start-begin", 3),
          ("start-end", 5),
          ("start-new", 4))
    )


_AppMonLogfState_Type.__name__ = "Integer32"
_AppMonLogfState_Object = MibTableColumn
appMonLogfState = _AppMonLogfState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 7, 2, 1, 3),
    _AppMonLogfState_Type()
)
appMonLogfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appMonLogfState.setStatus("mandatory")
_AppMonLogfPattern_Type = DisplayString
_AppMonLogfPattern_Object = MibTableColumn
appMonLogfPattern = _AppMonLogfPattern_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 7, 2, 1, 4),
    _AppMonLogfPattern_Type()
)
appMonLogfPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonLogfPattern.setStatus("mandatory")
_SniAppMonJVs_ObjectIdentity = ObjectIdentity
sniAppMonJVs = _SniAppMonJVs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 8)
)
_AppMonJVTabNum_Type = Integer32
_AppMonJVTabNum_Object = MibScalar
appMonJVTabNum = _AppMonJVTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 8, 1),
    _AppMonJVTabNum_Type()
)
appMonJVTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonJVTabNum.setStatus("mandatory")
_AppMonJVTable_Object = MibTable
appMonJVTable = _AppMonJVTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 8, 2)
)
if mibBuilder.loadTexts:
    appMonJVTable.setStatus("mandatory")
_AppMonJVEntry_Object = MibTableRow
appMonJVEntry = _AppMonJVEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 8, 2, 1)
)
appMonJVEntry.setIndexNames(
    (0, "Application-Monitoring-MIB", "appMonJVName"),
)
if mibBuilder.loadTexts:
    appMonJVEntry.setStatus("mandatory")
_AppMonJVName_Type = DisplayString
_AppMonJVName_Object = MibTableColumn
appMonJVName = _AppMonJVName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 8, 2, 1, 1),
    _AppMonJVName_Type()
)
appMonJVName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonJVName.setStatus("mandatory")
_AppMonJVAppl_Type = DisplayString
_AppMonJVAppl_Object = MibTableColumn
appMonJVAppl = _AppMonJVAppl_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 8, 2, 1, 2),
    _AppMonJVAppl_Type()
)
appMonJVAppl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonJVAppl.setStatus("mandatory")
_AppMonJVValue_Type = DisplayString
_AppMonJVValue_Object = MibTableColumn
appMonJVValue = _AppMonJVValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 8, 2, 1, 3),
    _AppMonJVValue_Type()
)
appMonJVValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonJVValue.setStatus("mandatory")
_AppMonJVPattern_Type = DisplayString
_AppMonJVPattern_Object = MibTableColumn
appMonJVPattern = _AppMonJVPattern_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 8, 2, 1, 4),
    _AppMonJVPattern_Type()
)
appMonJVPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonJVPattern.setStatus("mandatory")
_SniAppMonObjects_ObjectIdentity = ObjectIdentity
sniAppMonObjects = _SniAppMonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 9)
)
_AppMonObjectsTabNum_Type = Integer32
_AppMonObjectsTabNum_Object = MibScalar
appMonObjectsTabNum = _AppMonObjectsTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 1),
    _AppMonObjectsTabNum_Type()
)
appMonObjectsTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonObjectsTabNum.setStatus("mandatory")
_AppMonObjectTable_Object = MibTable
appMonObjectTable = _AppMonObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2)
)
if mibBuilder.loadTexts:
    appMonObjectTable.setStatus("mandatory")
_AppMonObjectEntry_Object = MibTableRow
appMonObjectEntry = _AppMonObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1)
)
appMonObjectEntry.setIndexNames(
    (0, "Application-Monitoring-MIB", "appMonObjectIndex"),
)
if mibBuilder.loadTexts:
    appMonObjectEntry.setStatus("mandatory")
_AppMonObjectIndex_Type = Integer32
_AppMonObjectIndex_Object = MibTableColumn
appMonObjectIndex = _AppMonObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1, 1),
    _AppMonObjectIndex_Type()
)
appMonObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonObjectIndex.setStatus("mandatory")
_AppMonObjectName_Type = DisplayString
_AppMonObjectName_Object = MibTableColumn
appMonObjectName = _AppMonObjectName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1, 2),
    _AppMonObjectName_Type()
)
appMonObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonObjectName.setStatus("mandatory")
_AppMonObjectBcamAppl_Type = DisplayString
_AppMonObjectBcamAppl_Object = MibTableColumn
appMonObjectBcamAppl = _AppMonObjectBcamAppl_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1, 3),
    _AppMonObjectBcamAppl_Type()
)
appMonObjectBcamAppl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonObjectBcamAppl.setStatus("mandatory")
_AppMonObjectUserAppl_Type = DisplayString
_AppMonObjectUserAppl_Object = MibTableColumn
appMonObjectUserAppl = _AppMonObjectUserAppl_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1, 4),
    _AppMonObjectUserAppl_Type()
)
appMonObjectUserAppl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonObjectUserAppl.setStatus("mandatory")
_AppMonObjectDcamAppl_Type = DisplayString
_AppMonObjectDcamAppl_Object = MibTableColumn
appMonObjectDcamAppl = _AppMonObjectDcamAppl_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1, 5),
    _AppMonObjectDcamAppl_Type()
)
appMonObjectDcamAppl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonObjectDcamAppl.setStatus("mandatory")
_AppMonObjectSub_Type = DisplayString
_AppMonObjectSub_Object = MibTableColumn
appMonObjectSub = _AppMonObjectSub_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1, 6),
    _AppMonObjectSub_Type()
)
appMonObjectSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonObjectSub.setStatus("mandatory")
_AppMonObjectLogfile_Type = DisplayString
_AppMonObjectLogfile_Object = MibTableColumn
appMonObjectLogfile = _AppMonObjectLogfile_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1, 7),
    _AppMonObjectLogfile_Type()
)
appMonObjectLogfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonObjectLogfile.setStatus("mandatory")
_AppMonObjectJV_Type = DisplayString
_AppMonObjectJV_Object = MibTableColumn
appMonObjectJV = _AppMonObjectJV_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1, 8),
    _AppMonObjectJV_Type()
)
appMonObjectJV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMonObjectJV.setStatus("mandatory")
_AppMonTraps_ObjectIdentity = ObjectIdentity
appMonTraps = _AppMonTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 20)
)
_AppMonTrapData_ObjectIdentity = ObjectIdentity
appMonTrapData = _AppMonTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 1)
)
_AppMonSource_Type = DisplayString
_AppMonSource_Object = MibScalar
appMonSource = _AppMonSource_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 1, 1),
    _AppMonSource_Type()
)
appMonSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appMonSource.setStatus("mandatory")
_AppMonDevice_Type = DisplayString
_AppMonDevice_Object = MibScalar
appMonDevice = _AppMonDevice_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 1, 2),
    _AppMonDevice_Type()
)
appMonDevice.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appMonDevice.setStatus("mandatory")
_AppMonMsg_Type = DisplayString
_AppMonMsg_Object = MibScalar
appMonMsg = _AppMonMsg_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 1, 3),
    _AppMonMsg_Type()
)
appMonMsg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appMonMsg.setStatus("mandatory")
_AppMonWeight_Type = Integer32
_AppMonWeight_Object = MibScalar
appMonWeight = _AppMonWeight_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 1, 4),
    _AppMonWeight_Type()
)
appMonWeight.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appMonWeight.setStatus("mandatory")
_AppMonAckOID_Type = ObjectIdentifier
_AppMonAckOID_Object = MibScalar
appMonAckOID = _AppMonAckOID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 1, 6),
    _AppMonAckOID_Type()
)
appMonAckOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appMonAckOID.setStatus("mandatory")
_AppMonGeneric_ObjectIdentity = ObjectIdentity
appMonGeneric = _AppMonGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 2)
)
_AppMonConfirm_ObjectIdentity = ObjectIdentity
appMonConfirm = _AppMonConfirm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 3)
)

# Managed Objects groups


# Notification objects

appMonGenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 2, 0, 999)
)
appMonGenTrap.setObjects(
      *(("Application-Monitoring-MIB", "appMonSource"),
        ("Application-Monitoring-MIB", "appMonDevice"),
        ("Application-Monitoring-MIB", "appMonMsg"),
        ("Application-Monitoring-MIB", "appMonWeight"))
)
if mibBuilder.loadTexts:
    appMonGenTrap.setStatus(
        ""
    )

appMonConfirmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 3, 0, 999)
)
appMonConfirmTrap.setObjects(
      *(("Application-Monitoring-MIB", "appMonSource"),
        ("Application-Monitoring-MIB", "appMonDevice"),
        ("Application-Monitoring-MIB", "appMonMsg"),
        ("Application-Monitoring-MIB", "appMonWeight"))
)
if mibBuilder.loadTexts:
    appMonConfirmTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Application-Monitoring-MIB",
    **{"sni": sni,
       "sniProductMibs": sniProductMibs,
       "sniAppMon": sniAppMon,
       "sniAppMonSubSystems": sniAppMonSubSystems,
       "appMonSubsysTabNum": appMonSubsysTabNum,
       "appMonSubsysTable": appMonSubsysTable,
       "appMonSubsysEntry": appMonSubsysEntry,
       "appMonSubsysIndex": appMonSubsysIndex,
       "appMonSubsysName": appMonSubsysName,
       "appMonSubsysVersion": appMonSubsysVersion,
       "appMonSubsysState": appMonSubsysState,
       "appMonSubsysTasks": appMonSubsysTasks,
       "sniAppMonBcamAppl": sniAppMonBcamAppl,
       "appMonBcamApplTabNum": appMonBcamApplTabNum,
       "appMonBcamApplTable": appMonBcamApplTable,
       "appMonBcamApplEntry": appMonBcamApplEntry,
       "appMonBcamApplIndex": appMonBcamApplIndex,
       "appMonBcamApplName": appMonBcamApplName,
       "appMonBcamApplVersion": appMonBcamApplVersion,
       "appMonBcamApplState": appMonBcamApplState,
       "appMonBcamApplMonJV": appMonBcamApplMonJV,
       "sniAppMonUserAppl": sniAppMonUserAppl,
       "appMonUserApplTabNum": appMonUserApplTabNum,
       "appMonUserApplTable": appMonUserApplTable,
       "appMonUserApplEntry": appMonUserApplEntry,
       "appMonUserApplIndex": appMonUserApplIndex,
       "appMonUserApplName": appMonUserApplName,
       "appMonUserApplVersion": appMonUserApplVersion,
       "appMonUserApplState": appMonUserApplState,
       "appMonUserApplMonJV": appMonUserApplMonJV,
       "sniAppMonGlobalData": sniAppMonGlobalData,
       "appMonVersion": appMonVersion,
       "appMonConfFile": appMonConfFile,
       "appMonTrapFormat": appMonTrapFormat,
       "sniAppMonDcamAppl": sniAppMonDcamAppl,
       "appMonDcamApplTabNum": appMonDcamApplTabNum,
       "appMonDcamApplTable": appMonDcamApplTable,
       "appMonDcamApplEntry": appMonDcamApplEntry,
       "appMonDcamApplIndex": appMonDcamApplIndex,
       "appMonDcamApplName": appMonDcamApplName,
       "appMonDcamApplHost": appMonDcamApplHost,
       "appMonDcamApplState": appMonDcamApplState,
       "appMonLogfiles": appMonLogfiles,
       "appMonLogfTabNum": appMonLogfTabNum,
       "appMonLogfTable": appMonLogfTable,
       "appMonLogfEntry": appMonLogfEntry,
       "appMonLogfName": appMonLogfName,
       "appMonLogfAppl": appMonLogfAppl,
       "appMonLogfState": appMonLogfState,
       "appMonLogfPattern": appMonLogfPattern,
       "sniAppMonJVs": sniAppMonJVs,
       "appMonJVTabNum": appMonJVTabNum,
       "appMonJVTable": appMonJVTable,
       "appMonJVEntry": appMonJVEntry,
       "appMonJVName": appMonJVName,
       "appMonJVAppl": appMonJVAppl,
       "appMonJVValue": appMonJVValue,
       "appMonJVPattern": appMonJVPattern,
       "sniAppMonObjects": sniAppMonObjects,
       "appMonObjectsTabNum": appMonObjectsTabNum,
       "appMonObjectTable": appMonObjectTable,
       "appMonObjectEntry": appMonObjectEntry,
       "appMonObjectIndex": appMonObjectIndex,
       "appMonObjectName": appMonObjectName,
       "appMonObjectBcamAppl": appMonObjectBcamAppl,
       "appMonObjectUserAppl": appMonObjectUserAppl,
       "appMonObjectDcamAppl": appMonObjectDcamAppl,
       "appMonObjectSub": appMonObjectSub,
       "appMonObjectLogfile": appMonObjectLogfile,
       "appMonObjectJV": appMonObjectJV,
       "appMonTraps": appMonTraps,
       "appMonTrapData": appMonTrapData,
       "appMonSource": appMonSource,
       "appMonDevice": appMonDevice,
       "appMonMsg": appMonMsg,
       "appMonWeight": appMonWeight,
       "appMonAckOID": appMonAckOID,
       "appMonGeneric": appMonGeneric,
       "appMonGenTrap": appMonGenTrap,
       "appMonConfirm": appMonConfirm,
       "appMonConfirmTrap": appMonConfirmTrap}
)
