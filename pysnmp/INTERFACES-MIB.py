# SNMP MIB module (INTERFACES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTERFACES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:25 2024
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

_Txport_ObjectIdentity = ObjectIdentity
txport = _Txport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425)
)
_Companyinfo_ObjectIdentity = ObjectIdentity
companyinfo = _Companyinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 1)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 2)
)
_Temporary_ObjectIdentity = ObjectIdentity
temporary = _Temporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 3)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 4)
)
_Revision_ObjectIdentity = ObjectIdentity
revision = _Revision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 5)
)
_Pdc_ObjectIdentity = ObjectIdentity
pdc = _Pdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 6)
)
_Utilities_ObjectIdentity = ObjectIdentity
utilities = _Utilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 7)
)
_Tinterfaces_ObjectIdentity = ObjectIdentity
tinterfaces = _Tinterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 8)
)
_MgmtPorts_ObjectIdentity = ObjectIdentity
mgmtPorts = _MgmtPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 8, 1)
)
_MgmtPortsTable_Object = MibTable
mgmtPortsTable = _MgmtPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 1, 1)
)
if mibBuilder.loadTexts:
    mgmtPortsTable.setStatus("optional")
_MgmtPortsTableEntry_Object = MibTableRow
mgmtPortsTableEntry = _MgmtPortsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 1, 1, 1)
)
mgmtPortsTableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "mgmtPortsTableIndex"),
)
if mibBuilder.loadTexts:
    mgmtPortsTableEntry.setStatus("mandatory")
_MgmtPortsTableIndex_Type = Integer32
_MgmtPortsTableIndex_Object = MibTableColumn
mgmtPortsTableIndex = _MgmtPortsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 1, 1, 1, 1),
    _MgmtPortsTableIndex_Type()
)
mgmtPortsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtPortsTableIndex.setStatus("mandatory")


class _MgmtPortsDescription_Type(DisplayString):
    """Custom type mgmtPortsDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MgmtPortsDescription_Type.__name__ = "DisplayString"
_MgmtPortsDescription_Object = MibTableColumn
mgmtPortsDescription = _MgmtPortsDescription_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 1, 1, 1, 2),
    _MgmtPortsDescription_Type()
)
mgmtPortsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtPortsDescription.setStatus("mandatory")


class _MgmtPortsElementID_Type(DisplayString):
    """Custom type mgmtPortsElementID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_MgmtPortsElementID_Type.__name__ = "DisplayString"
_MgmtPortsElementID_Object = MibTableColumn
mgmtPortsElementID = _MgmtPortsElementID_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 1, 1, 1, 3),
    _MgmtPortsElementID_Type()
)
mgmtPortsElementID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtPortsElementID.setStatus("mandatory")


class _MgmtPortsMode_Type(Integer32):
    """Custom type mgmtPortsMode based on Integer32"""
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
        *(("coadial", 3),
          ("coadirect", 4),
          ("disabled", 2),
          ("extAlarmOnClosed", 6),
          ("extAlarmOnOpen", 5),
          ("other", 1),
          ("slipdial", 7),
          ("slipdirect", 8))
    )


_MgmtPortsMode_Type.__name__ = "Integer32"
_MgmtPortsMode_Object = MibTableColumn
mgmtPortsMode = _MgmtPortsMode_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 1, 1, 1, 4),
    _MgmtPortsMode_Type()
)
mgmtPortsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtPortsMode.setStatus("mandatory")


class _MgmtPortsDialPrefix_Type(DisplayString):
    """Custom type mgmtPortsDialPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_MgmtPortsDialPrefix_Type.__name__ = "DisplayString"
_MgmtPortsDialPrefix_Object = MibTableColumn
mgmtPortsDialPrefix = _MgmtPortsDialPrefix_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 1, 1, 1, 5),
    _MgmtPortsDialPrefix_Type()
)
mgmtPortsDialPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtPortsDialPrefix.setStatus("mandatory")


class _MgmtPortsPrimaryDialString_Type(DisplayString):
    """Custom type mgmtPortsPrimaryDialString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_MgmtPortsPrimaryDialString_Type.__name__ = "DisplayString"
_MgmtPortsPrimaryDialString_Object = MibTableColumn
mgmtPortsPrimaryDialString = _MgmtPortsPrimaryDialString_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 1, 1, 1, 6),
    _MgmtPortsPrimaryDialString_Type()
)
mgmtPortsPrimaryDialString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtPortsPrimaryDialString.setStatus("mandatory")


class _MgmtPortsSecondaryDialString_Type(DisplayString):
    """Custom type mgmtPortsSecondaryDialString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_MgmtPortsSecondaryDialString_Type.__name__ = "DisplayString"
_MgmtPortsSecondaryDialString_Object = MibTableColumn
mgmtPortsSecondaryDialString = _MgmtPortsSecondaryDialString_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 1, 1, 1, 7),
    _MgmtPortsSecondaryDialString_Type()
)
mgmtPortsSecondaryDialString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtPortsSecondaryDialString.setStatus("mandatory")


class _MgmtPortsExtInitString_Type(DisplayString):
    """Custom type mgmtPortsExtInitString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_MgmtPortsExtInitString_Type.__name__ = "DisplayString"
_MgmtPortsExtInitString_Object = MibTableColumn
mgmtPortsExtInitString = _MgmtPortsExtInitString_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 1, 1, 1, 8),
    _MgmtPortsExtInitString_Type()
)
mgmtPortsExtInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtPortsExtInitString.setStatus("mandatory")


class _MgmtPortsCompressedSlip_Type(Integer32):
    """Custom type mgmtPortsCompressedSlip based on Integer32"""
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
        *(("auto", 4),
          ("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_MgmtPortsCompressedSlip_Type.__name__ = "Integer32"
_MgmtPortsCompressedSlip_Object = MibTableColumn
mgmtPortsCompressedSlip = _MgmtPortsCompressedSlip_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 1, 1, 1, 9),
    _MgmtPortsCompressedSlip_Type()
)
mgmtPortsCompressedSlip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtPortsCompressedSlip.setStatus("mandatory")


class _MgmtPortsInternalModem_Type(Integer32):
    """Custom type mgmtPortsInternalModem based on Integer32"""
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
        *(("disabled", 4),
          ("enabled", 3),
          ("notPresent", 2),
          ("other", 1))
    )


_MgmtPortsInternalModem_Type.__name__ = "Integer32"
_MgmtPortsInternalModem_Object = MibTableColumn
mgmtPortsInternalModem = _MgmtPortsInternalModem_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 1, 1, 1, 10),
    _MgmtPortsInternalModem_Type()
)
mgmtPortsInternalModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtPortsInternalModem.setStatus("mandatory")
_Dbu_ObjectIdentity = ObjectIdentity
dbu = _Dbu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 8, 2)
)
_DbuConfigTable_Object = MibTable
dbuConfigTable = _DbuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1)
)
if mibBuilder.loadTexts:
    dbuConfigTable.setStatus("optional")
_DbuConfigTableEntry_Object = MibTableRow
dbuConfigTableEntry = _DbuConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1)
)
dbuConfigTableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "dbuNearIndex"),
    (0, "INTERFACES-MIB", "dbuFarIndex"),
    (0, "INTERFACES-MIB", "dbuConfigTableIndex"),
)
if mibBuilder.loadTexts:
    dbuConfigTableEntry.setStatus("mandatory")
_DbuNearIndex_Type = Integer32
_DbuNearIndex_Object = MibTableColumn
dbuNearIndex = _DbuNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 1),
    _DbuNearIndex_Type()
)
dbuNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbuNearIndex.setStatus("mandatory")
_DbuFarIndex_Type = Integer32
_DbuFarIndex_Object = MibTableColumn
dbuFarIndex = _DbuFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 2),
    _DbuFarIndex_Type()
)
dbuFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbuFarIndex.setStatus("mandatory")
_DbuConfigTableIndex_Type = Integer32
_DbuConfigTableIndex_Object = MibTableColumn
dbuConfigTableIndex = _DbuConfigTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 3),
    _DbuConfigTableIndex_Type()
)
dbuConfigTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbuConfigTableIndex.setStatus("mandatory")


class _DbuDescription_Type(DisplayString):
    """Custom type dbuDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DbuDescription_Type.__name__ = "DisplayString"
_DbuDescription_Object = MibTableColumn
dbuDescription = _DbuDescription_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 4),
    _DbuDescription_Type()
)
dbuDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbuDescription.setStatus("mandatory")


class _DbuRate_Type(Integer32):
    """Custom type dbuRate based on Integer32"""
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
        *(("dbuRate19200", 5),
          ("dbuRate2400", 2),
          ("dbuRate38400", 6),
          ("dbuRate4800", 3),
          ("dbuRate56000", 7),
          ("dbuRate57600", 8),
          ("dbuRate64000", 9),
          ("dbuRate9600", 4),
          ("dbuRateOther", 1))
    )


_DbuRate_Type.__name__ = "Integer32"
_DbuRate_Object = MibTableColumn
dbuRate = _DbuRate_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 5),
    _DbuRate_Type()
)
dbuRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuRate.setStatus("mandatory")


class _DbuMode_Type(Integer32):
    """Custom type dbuMode based on Integer32"""
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
        *(("dbuModeAnsw", 3),
          ("dbuModeCallbackAnsw", 6),
          ("dbuModeCallbackOrig", 5),
          ("dbuModeMaster", 7),
          ("dbuModeNotAvail", 4),
          ("dbuModeOrig", 2),
          ("dbuModeOther", 1),
          ("dbuModeSlave", 8))
    )


_DbuMode_Type.__name__ = "Integer32"
_DbuMode_Object = MibTableColumn
dbuMode = _DbuMode_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 6),
    _DbuMode_Type()
)
dbuMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuMode.setStatus("mandatory")


class _DbuFormat_Type(Integer32):
    """Custom type dbuFormat based on Integer32"""
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
        *(("dbuFormatAsync", 3),
          ("dbuFormatNotAvail", 4),
          ("dbuFormatOther", 1),
          ("dbuFormatSync", 2))
    )


_DbuFormat_Type.__name__ = "Integer32"
_DbuFormat_Object = MibTableColumn
dbuFormat = _DbuFormat_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 7),
    _DbuFormat_Type()
)
dbuFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuFormat.setStatus("mandatory")


class _DbuNumber_Type(DisplayString):
    """Custom type dbuNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_DbuNumber_Type.__name__ = "DisplayString"
_DbuNumber_Object = MibTableColumn
dbuNumber = _DbuNumber_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 8),
    _DbuNumber_Type()
)
dbuNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuNumber.setStatus("mandatory")


class _DbuStatus_Type(Integer32):
    """Custom type dbuStatus based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("dbuStatusActive", 4),
          ("dbuStatusAwaitingCall", 8),
          ("dbuStatusConnecting", 6),
          ("dbuStatusDialing", 9),
          ("dbuStatusDisabled", 2),
          ("dbuStatusDisallowed", 7),
          ("dbuStatusDisconnecting", 10),
          ("dbuStatusEnabled", 3),
          ("dbuStatusLocked", 5),
          ("dbuStatusOther", 1),
          ("dbuStatusTestFailed", 13),
          ("dbuStatusTestPassed", 12),
          ("dbuStatusTesting", 11))
    )


_DbuStatus_Type.__name__ = "Integer32"
_DbuStatus_Object = MibTableColumn
dbuStatus = _DbuStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 9),
    _DbuStatus_Type()
)
dbuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbuStatus.setStatus("mandatory")


class _DbuCommand_Type(Integer32):
    """Custom type dbuCommand based on Integer32"""
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
        *(("dbuCommandActivate", 4),
          ("dbuCommandDisable", 2),
          ("dbuCommandEnable", 3),
          ("dbuCommandEnableDaily", 6),
          ("dbuCommandLock", 5),
          ("dbuCommandOther", 1),
          ("dbuCommandTest", 7))
    )


_DbuCommand_Type.__name__ = "Integer32"
_DbuCommand_Object = MibTableColumn
dbuCommand = _DbuCommand_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 10),
    _DbuCommand_Type()
)
dbuCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuCommand.setStatus("mandatory")


class _DbuActivator1_Type(Integer32):
    """Custom type dbuActivator1 based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("dbuActivatorAIS", 11),
          ("dbuActivatorAny", 5),
          ("dbuActivatorBPV", 12),
          ("dbuActivatorES", 6),
          ("dbuActivatorLOF", 9),
          ("dbuActivatorLOS", 2),
          ("dbuActivatorOOF", 4),
          ("dbuActivatorOOS", 3),
          ("dbuActivatorOther", 1),
          ("dbuActivatorRAS", 10),
          ("dbuActivatorSES", 7),
          ("dbuActivatorUAS", 8))
    )


_DbuActivator1_Type.__name__ = "Integer32"
_DbuActivator1_Object = MibTableColumn
dbuActivator1 = _DbuActivator1_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 11),
    _DbuActivator1_Type()
)
dbuActivator1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuActivator1.setStatus("mandatory")


class _DbuActivator2_Type(Integer32):
    """Custom type dbuActivator2 based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("dbuActivatorAIS", 11),
          ("dbuActivatorAny", 5),
          ("dbuActivatorBPV", 12),
          ("dbuActivatorES", 6),
          ("dbuActivatorLOF", 9),
          ("dbuActivatorLOS", 2),
          ("dbuActivatorOOF", 4),
          ("dbuActivatorOOS", 3),
          ("dbuActivatorOther", 1),
          ("dbuActivatorRAS", 10),
          ("dbuActivatorSES", 7),
          ("dbuActivatorUAS", 8))
    )


_DbuActivator2_Type.__name__ = "Integer32"
_DbuActivator2_Object = MibTableColumn
dbuActivator2 = _DbuActivator2_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 12),
    _DbuActivator2_Type()
)
dbuActivator2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuActivator2.setStatus("mandatory")


class _DbuDialStr_Type(DisplayString):
    """Custom type dbuDialStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DbuDialStr_Type.__name__ = "DisplayString"
_DbuDialStr_Object = MibTableColumn
dbuDialStr = _DbuDialStr_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 13),
    _DbuDialStr_Type()
)
dbuDialStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuDialStr.setStatus("mandatory")


class _DbuInitStr_Type(DisplayString):
    """Custom type dbuInitStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DbuInitStr_Type.__name__ = "DisplayString"
_DbuInitStr_Object = MibTableColumn
dbuInitStr = _DbuInitStr_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 14),
    _DbuInitStr_Type()
)
dbuInitStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuInitStr.setStatus("mandatory")


class _DbuHangupStr_Type(DisplayString):
    """Custom type dbuHangupStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DbuHangupStr_Type.__name__ = "DisplayString"
_DbuHangupStr_Object = MibTableColumn
dbuHangupStr = _DbuHangupStr_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 15),
    _DbuHangupStr_Type()
)
dbuHangupStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuHangupStr.setStatus("mandatory")


class _DbuPasswordStr_Type(DisplayString):
    """Custom type dbuPasswordStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DbuPasswordStr_Type.__name__ = "DisplayString"
_DbuPasswordStr_Object = MibTableColumn
dbuPasswordStr = _DbuPasswordStr_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 16),
    _DbuPasswordStr_Type()
)
dbuPasswordStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuPasswordStr.setStatus("mandatory")


class _DbuSecurity_Type(Integer32):
    """Custom type dbuSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dbuSecurityDisable", 2),
          ("dbuSecurityEnable", 3),
          ("dbuSecurityOther", 1))
    )


_DbuSecurity_Type.__name__ = "Integer32"
_DbuSecurity_Object = MibTableColumn
dbuSecurity = _DbuSecurity_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 17),
    _DbuSecurity_Type()
)
dbuSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuSecurity.setStatus("mandatory")


class _DbuDtrDial_Type(Integer32):
    """Custom type dbuDtrDial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dbuDtrDialDisable", 2),
          ("dbuDtrDialEnable", 3),
          ("dbuDtrDialOther", 1))
    )


_DbuDtrDial_Type.__name__ = "Integer32"
_DbuDtrDial_Object = MibTableColumn
dbuDtrDial = _DbuDtrDial_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 18),
    _DbuDtrDial_Type()
)
dbuDtrDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuDtrDial.setStatus("mandatory")
_DbuISDNSwitchType_Type = Integer32
_DbuISDNSwitchType_Object = MibTableColumn
dbuISDNSwitchType = _DbuISDNSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 19),
    _DbuISDNSwitchType_Type()
)
dbuISDNSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuISDNSwitchType.setStatus("mandatory")


class _DbuISDNSwitchVersion_Type(Integer32):
    """Custom type dbuISDNSwitchVersion based on Integer32"""
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
        *(("dbuISDNSwitchVersionATTMP", 4),
          ("dbuISDNSwitchVersionATTP2P", 3),
          ("dbuISDNSwitchVersionDMS100PVCIC0", 5),
          ("dbuISDNSwitchVersionDMS100PVCIC1", 6),
          ("dbuISDNSwitchVersionNational1", 2),
          ("dbuISDNSwitchVersionOther", 1))
    )


_DbuISDNSwitchVersion_Type.__name__ = "Integer32"
_DbuISDNSwitchVersion_Object = MibTableColumn
dbuISDNSwitchVersion = _DbuISDNSwitchVersion_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 20),
    _DbuISDNSwitchVersion_Type()
)
dbuISDNSwitchVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuISDNSwitchVersion.setStatus("mandatory")


class _DbuISDNTEI_Type(Integer32):
    """Custom type dbuISDNTEI based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67)
        )
    )
    namedValues = NamedValues(
        *(("dbuISDNTEI0", 4),
          ("dbuISDNTEI1", 5),
          ("dbuISDNTEI10", 14),
          ("dbuISDNTEI11", 15),
          ("dbuISDNTEI12", 16),
          ("dbuISDNTEI13", 17),
          ("dbuISDNTEI14", 18),
          ("dbuISDNTEI15", 19),
          ("dbuISDNTEI16", 20),
          ("dbuISDNTEI17", 21),
          ("dbuISDNTEI18", 22),
          ("dbuISDNTEI19", 23),
          ("dbuISDNTEI2", 6),
          ("dbuISDNTEI20", 24),
          ("dbuISDNTEI21", 25),
          ("dbuISDNTEI22", 26),
          ("dbuISDNTEI23", 27),
          ("dbuISDNTEI24", 28),
          ("dbuISDNTEI25", 29),
          ("dbuISDNTEI26", 30),
          ("dbuISDNTEI27", 31),
          ("dbuISDNTEI28", 32),
          ("dbuISDNTEI29", 33),
          ("dbuISDNTEI3", 7),
          ("dbuISDNTEI30", 34),
          ("dbuISDNTEI31", 35),
          ("dbuISDNTEI32", 36),
          ("dbuISDNTEI33", 37),
          ("dbuISDNTEI34", 38),
          ("dbuISDNTEI35", 39),
          ("dbuISDNTEI36", 40),
          ("dbuISDNTEI37", 41),
          ("dbuISDNTEI38", 42),
          ("dbuISDNTEI39", 43),
          ("dbuISDNTEI4", 8),
          ("dbuISDNTEI40", 44),
          ("dbuISDNTEI41", 45),
          ("dbuISDNTEI42", 46),
          ("dbuISDNTEI43", 47),
          ("dbuISDNTEI44", 48),
          ("dbuISDNTEI45", 49),
          ("dbuISDNTEI46", 50),
          ("dbuISDNTEI47", 51),
          ("dbuISDNTEI48", 52),
          ("dbuISDNTEI49", 53),
          ("dbuISDNTEI5", 9),
          ("dbuISDNTEI50", 54),
          ("dbuISDNTEI51", 55),
          ("dbuISDNTEI52", 56),
          ("dbuISDNTEI53", 57),
          ("dbuISDNTEI54", 58),
          ("dbuISDNTEI55", 59),
          ("dbuISDNTEI56", 60),
          ("dbuISDNTEI57", 61),
          ("dbuISDNTEI58", 62),
          ("dbuISDNTEI59", 63),
          ("dbuISDNTEI6", 10),
          ("dbuISDNTEI60", 64),
          ("dbuISDNTEI61", 65),
          ("dbuISDNTEI62", 66),
          ("dbuISDNTEI63", 67),
          ("dbuISDNTEI7", 11),
          ("dbuISDNTEI8", 12),
          ("dbuISDNTEI9", 13),
          ("dbuISDNTEIAuto", 3),
          ("dbuISDNTEIDisable", 2),
          ("dbuISDNTEIOther", 1))
    )


_DbuISDNTEI_Type.__name__ = "Integer32"
_DbuISDNTEI_Object = MibTableColumn
dbuISDNTEI = _DbuISDNTEI_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 21),
    _DbuISDNTEI_Type()
)
dbuISDNTEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuISDNTEI.setStatus("mandatory")


class _DbuISDNSPID_Type(DisplayString):
    """Custom type dbuISDNSPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DbuISDNSPID_Type.__name__ = "DisplayString"
_DbuISDNSPID_Object = MibTableColumn
dbuISDNSPID = _DbuISDNSPID_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 22),
    _DbuISDNSPID_Type()
)
dbuISDNSPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuISDNSPID.setStatus("mandatory")


class _DbuISDNDDNUM_Type(DisplayString):
    """Custom type dbuISDNDDNUM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DbuISDNDDNUM_Type.__name__ = "DisplayString"
_DbuISDNDDNUM_Object = MibTableColumn
dbuISDNDDNUM = _DbuISDNDDNUM_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 1, 1, 23),
    _DbuISDNDDNUM_Type()
)
dbuISDNDDNUM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuISDNDDNUM.setStatus("mandatory")
_DbuResetStringsTable_Object = MibTable
dbuResetStringsTable = _DbuResetStringsTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 2)
)
if mibBuilder.loadTexts:
    dbuResetStringsTable.setStatus("mandatory")
_DbuResetStringsEntry_Object = MibTableRow
dbuResetStringsEntry = _DbuResetStringsEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 2, 1)
)
dbuResetStringsEntry.setIndexNames(
    (0, "INTERFACES-MIB", "dbuResetNearIndex"),
    (0, "INTERFACES-MIB", "dbuResetFarIndex"),
    (0, "INTERFACES-MIB", "dbuResetConfigEntryIndex"),
    (0, "INTERFACES-MIB", "dbuResetStringsIndex"),
)
if mibBuilder.loadTexts:
    dbuResetStringsEntry.setStatus("mandatory")
_DbuResetNearIndex_Type = Integer32
_DbuResetNearIndex_Object = MibTableColumn
dbuResetNearIndex = _DbuResetNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 2, 1, 1),
    _DbuResetNearIndex_Type()
)
dbuResetNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbuResetNearIndex.setStatus("mandatory")
_DbuResetFarIndex_Type = Integer32
_DbuResetFarIndex_Object = MibTableColumn
dbuResetFarIndex = _DbuResetFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 2, 1, 2),
    _DbuResetFarIndex_Type()
)
dbuResetFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbuResetFarIndex.setStatus("mandatory")
_DbuResetConfigEntryIndex_Type = Integer32
_DbuResetConfigEntryIndex_Object = MibTableColumn
dbuResetConfigEntryIndex = _DbuResetConfigEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 2, 1, 3),
    _DbuResetConfigEntryIndex_Type()
)
dbuResetConfigEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbuResetConfigEntryIndex.setStatus("mandatory")
_DbuResetStringsIndex_Type = Integer32
_DbuResetStringsIndex_Object = MibTableColumn
dbuResetStringsIndex = _DbuResetStringsIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 2, 1, 4),
    _DbuResetStringsIndex_Type()
)
dbuResetStringsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbuResetStringsIndex.setStatus("mandatory")


class _DbuResetString_Type(DisplayString):
    """Custom type dbuResetString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DbuResetString_Type.__name__ = "DisplayString"
_DbuResetString_Object = MibTableColumn
dbuResetString = _DbuResetString_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 2, 1, 5),
    _DbuResetString_Type()
)
dbuResetString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuResetString.setStatus("mandatory")
_DbuStartStopTable_Object = MibTable
dbuStartStopTable = _DbuStartStopTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 3)
)
if mibBuilder.loadTexts:
    dbuStartStopTable.setStatus("optional")
_DbuStartStopTableEntry_Object = MibTableRow
dbuStartStopTableEntry = _DbuStartStopTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 3, 1)
)
dbuStartStopTableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "dbuStartStopNearIndex"),
    (0, "INTERFACES-MIB", "dbuStartStopFarIndex"),
    (0, "INTERFACES-MIB", "dbuStartStopConfigEntryIndex"),
    (0, "INTERFACES-MIB", "dbuStartStopDayOfWeek"),
)
if mibBuilder.loadTexts:
    dbuStartStopTableEntry.setStatus("mandatory")
_DbuStartStopNearIndex_Type = Integer32
_DbuStartStopNearIndex_Object = MibTableColumn
dbuStartStopNearIndex = _DbuStartStopNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 3, 1, 1),
    _DbuStartStopNearIndex_Type()
)
dbuStartStopNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbuStartStopNearIndex.setStatus("mandatory")
_DbuStartStopFarIndex_Type = Integer32
_DbuStartStopFarIndex_Object = MibTableColumn
dbuStartStopFarIndex = _DbuStartStopFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 3, 1, 2),
    _DbuStartStopFarIndex_Type()
)
dbuStartStopFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbuStartStopFarIndex.setStatus("mandatory")
_DbuStartStopConfigEntryIndex_Type = Integer32
_DbuStartStopConfigEntryIndex_Object = MibTableColumn
dbuStartStopConfigEntryIndex = _DbuStartStopConfigEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 3, 1, 3),
    _DbuStartStopConfigEntryIndex_Type()
)
dbuStartStopConfigEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbuStartStopConfigEntryIndex.setStatus("mandatory")


class _DbuStartStopDayOfWeek_Type(Integer32):
    """Custom type dbuStartStopDayOfWeek based on Integer32"""
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
        *(("dbuStartStopFriday", 6),
          ("dbuStartStopMonday", 2),
          ("dbuStartStopSaturday", 7),
          ("dbuStartStopSunday", 1),
          ("dbuStartStopThursday", 5),
          ("dbuStartStopTuesday", 3),
          ("dbuStartStopWednesday", 4))
    )


_DbuStartStopDayOfWeek_Type.__name__ = "Integer32"
_DbuStartStopDayOfWeek_Object = MibTableColumn
dbuStartStopDayOfWeek = _DbuStartStopDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 3, 1, 4),
    _DbuStartStopDayOfWeek_Type()
)
dbuStartStopDayOfWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbuStartStopDayOfWeek.setStatus("mandatory")


class _DbuStart_Type(Integer32):
    """Custom type dbuStart based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("dbuStartHour00", 1),
          ("dbuStartHour01", 2),
          ("dbuStartHour02", 3),
          ("dbuStartHour03", 4),
          ("dbuStartHour04", 5),
          ("dbuStartHour05", 6),
          ("dbuStartHour06", 7),
          ("dbuStartHour07", 8),
          ("dbuStartHour08", 9),
          ("dbuStartHour09", 10),
          ("dbuStartHour10", 11),
          ("dbuStartHour11", 12),
          ("dbuStartHour12", 13),
          ("dbuStartHour13", 14),
          ("dbuStartHour14", 15),
          ("dbuStartHour15", 16),
          ("dbuStartHour16", 17),
          ("dbuStartHour17", 18),
          ("dbuStartHour18", 19),
          ("dbuStartHour19", 20),
          ("dbuStartHour20", 21),
          ("dbuStartHour21", 22),
          ("dbuStartHour22", 23),
          ("dbuStartHour23", 24))
    )


_DbuStart_Type.__name__ = "Integer32"
_DbuStart_Object = MibTableColumn
dbuStart = _DbuStart_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 3, 1, 5),
    _DbuStart_Type()
)
dbuStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuStart.setStatus("mandatory")


class _DbuStop_Type(Integer32):
    """Custom type dbuStop based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("dbuStopHour00", 1),
          ("dbuStopHour01", 2),
          ("dbuStopHour02", 3),
          ("dbuStopHour03", 4),
          ("dbuStopHour04", 5),
          ("dbuStopHour05", 6),
          ("dbuStopHour06", 7),
          ("dbuStopHour07", 8),
          ("dbuStopHour08", 9),
          ("dbuStopHour09", 10),
          ("dbuStopHour10", 11),
          ("dbuStopHour11", 12),
          ("dbuStopHour12", 13),
          ("dbuStopHour13", 14),
          ("dbuStopHour14", 15),
          ("dbuStopHour15", 16),
          ("dbuStopHour16", 17),
          ("dbuStopHour17", 18),
          ("dbuStopHour18", 19),
          ("dbuStopHour19", 20),
          ("dbuStopHour20", 21),
          ("dbuStopHour21", 22),
          ("dbuStopHour22", 23),
          ("dbuStopHour23", 24))
    )


_DbuStop_Type.__name__ = "Integer32"
_DbuStop_Object = MibTableColumn
dbuStop = _DbuStop_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 2, 3, 1, 6),
    _DbuStop_Type()
)
dbuStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuStop.setStatus("mandatory")
_T1e1_ObjectIdentity = ObjectIdentity
t1e1 = _T1e1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 8, 3)
)
_T1e1ConfigTable_Object = MibTable
t1e1ConfigTable = _T1e1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1)
)
if mibBuilder.loadTexts:
    t1e1ConfigTable.setStatus("optional")
_T1e1ConfigTableEntry_Object = MibTableRow
t1e1ConfigTableEntry = _T1e1ConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1)
)
t1e1ConfigTableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "t1e1ConfigNearIndex"),
    (0, "INTERFACES-MIB", "t1e1ConfigFarIndex"),
    (0, "INTERFACES-MIB", "t1e1ConfigIndex"),
)
if mibBuilder.loadTexts:
    t1e1ConfigTableEntry.setStatus("mandatory")
_T1e1ConfigNearIndex_Type = Integer32
_T1e1ConfigNearIndex_Object = MibTableColumn
t1e1ConfigNearIndex = _T1e1ConfigNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 1),
    _T1e1ConfigNearIndex_Type()
)
t1e1ConfigNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1ConfigNearIndex.setStatus("mandatory")
_T1e1ConfigFarIndex_Type = Integer32
_T1e1ConfigFarIndex_Object = MibTableColumn
t1e1ConfigFarIndex = _T1e1ConfigFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 2),
    _T1e1ConfigFarIndex_Type()
)
t1e1ConfigFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1ConfigFarIndex.setStatus("mandatory")
_T1e1ConfigIndex_Type = Integer32
_T1e1ConfigIndex_Object = MibTableColumn
t1e1ConfigIndex = _T1e1ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 3),
    _T1e1ConfigIndex_Type()
)
t1e1ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1ConfigIndex.setStatus("mandatory")


class _T1e1Description_Type(DisplayString):
    """Custom type t1e1Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_T1e1Description_Type.__name__ = "DisplayString"
_T1e1Description_Object = MibTableColumn
t1e1Description = _T1e1Description_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 4),
    _T1e1Description_Type()
)
t1e1Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1Description.setStatus("mandatory")


class _T1e1Mode_Type(Integer32):
    """Custom type t1e1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1ModeDTE", 2),
          ("t1e1ModeNetwork", 3),
          ("t1e1ModeOther", 1))
    )


_T1e1Mode_Type.__name__ = "Integer32"
_T1e1Mode_Object = MibTableColumn
t1e1Mode = _T1e1Mode_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 5),
    _T1e1Mode_Type()
)
t1e1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1Mode.setStatus("mandatory")


class _T1e1FrameType_Type(Integer32):
    """Custom type t1e1FrameType based on Integer32"""
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
        *(("t1e1FrameTypeCAS", 6),
          ("t1e1FrameTypeCASCRC", 7),
          ("t1e1FrameTypeCCS", 5),
          ("t1e1FrameTypeCCSCRC", 4),
          ("t1e1FrameTypeD4", 3),
          ("t1e1FrameTypeESF", 2),
          ("t1e1FrameTypeOther", 1),
          ("t1e1FrameTypeUnframed", 8))
    )


_T1e1FrameType_Type.__name__ = "Integer32"
_T1e1FrameType_Object = MibTableColumn
t1e1FrameType = _T1e1FrameType_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 6),
    _T1e1FrameType_Type()
)
t1e1FrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1FrameType.setStatus("mandatory")


class _T1e1LineCode_Type(Integer32):
    """Custom type t1e1LineCode based on Integer32"""
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
        *(("t1e1LineCodeAMI", 2),
          ("t1e1LineCodeB8ZS", 3),
          ("t1e1LineCodeHDB3", 4),
          ("t1e1LineCodeOther", 1))
    )


_T1e1LineCode_Type.__name__ = "Integer32"
_T1e1LineCode_Object = MibTableColumn
t1e1LineCode = _T1e1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 7),
    _T1e1LineCode_Type()
)
t1e1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1LineCode.setStatus("mandatory")


class _T1e1LineBuildOut_Type(Integer32):
    """Custom type t1e1LineBuildOut based on Integer32"""
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
        *(("t1e1LineBuildOut0db", 2),
          ("t1e1LineBuildOut15db", 4),
          ("t1e1LineBuildOut225db", 5),
          ("t1e1LineBuildOut75db", 3),
          ("t1e1LineBuildOutOther", 1))
    )


_T1e1LineBuildOut_Type.__name__ = "Integer32"
_T1e1LineBuildOut_Object = MibTableColumn
t1e1LineBuildOut = _T1e1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 8),
    _T1e1LineBuildOut_Type()
)
t1e1LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1LineBuildOut.setStatus("mandatory")


class _T1e1Timing_Type(Integer32):
    """Custom type t1e1Timing based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108)
        )
    )
    namedValues = NamedValues(
        *(("t1e1TimingInternal", 2),
          ("t1e1TimingNetwork", 3),
          ("t1e1TimingOther", 1),
          ("t1e1TimingPort1", 7),
          ("t1e1TimingPort10", 16),
          ("t1e1TimingPort11", 17),
          ("t1e1TimingPort12", 18),
          ("t1e1TimingPort13", 19),
          ("t1e1TimingPort14", 20),
          ("t1e1TimingPort15", 21),
          ("t1e1TimingPort16", 22),
          ("t1e1TimingPort17", 23),
          ("t1e1TimingPort18", 24),
          ("t1e1TimingPort19", 25),
          ("t1e1TimingPort2", 8),
          ("t1e1TimingPort20", 26),
          ("t1e1TimingPort21", 27),
          ("t1e1TimingPort22", 28),
          ("t1e1TimingPort23", 29),
          ("t1e1TimingPort24", 30),
          ("t1e1TimingPort25", 31),
          ("t1e1TimingPort26", 32),
          ("t1e1TimingPort27", 33),
          ("t1e1TimingPort28", 34),
          ("t1e1TimingPort29", 35),
          ("t1e1TimingPort3", 9),
          ("t1e1TimingPort30", 36),
          ("t1e1TimingPort31", 37),
          ("t1e1TimingPort32", 38),
          ("t1e1TimingPort4", 10),
          ("t1e1TimingPort5", 11),
          ("t1e1TimingPort6", 12),
          ("t1e1TimingPort7", 13),
          ("t1e1TimingPort8", 14),
          ("t1e1TimingPort9", 15),
          ("t1e1TimingSlot2Dsu1PortA", 49),
          ("t1e1TimingSlot2Dsu1PortB", 50),
          ("t1e1TimingSlot2Dsu2PortA", 51),
          ("t1e1TimingSlot2Dsu2PortB", 52),
          ("t1e1TimingSlot2Dsu3PortA", 53),
          ("t1e1TimingSlot2Dsu3PortB", 54),
          ("t1e1TimingSlot2Dsu4PortA", 55),
          ("t1e1TimingSlot2Dsu4PortB", 56),
          ("t1e1TimingSlot2Dsu5PortA", 57),
          ("t1e1TimingSlot2Dsu5PortB", 58),
          ("t1e1TimingSlot2Dsu6PortA", 59),
          ("t1e1TimingSlot2Dsu6PortB", 60),
          ("t1e1TimingSlot2PortA", 39),
          ("t1e1TimingSlot2PortB", 40),
          ("t1e1TimingSlot3Dsu1PortA", 61),
          ("t1e1TimingSlot3Dsu1PortB", 62),
          ("t1e1TimingSlot3Dsu2PortA", 63),
          ("t1e1TimingSlot3Dsu2PortB", 64),
          ("t1e1TimingSlot3Dsu3PortA", 65),
          ("t1e1TimingSlot3Dsu3PortB", 66),
          ("t1e1TimingSlot3Dsu4PortA", 67),
          ("t1e1TimingSlot3Dsu4PortB", 68),
          ("t1e1TimingSlot3Dsu5PortA", 69),
          ("t1e1TimingSlot3Dsu5PortB", 70),
          ("t1e1TimingSlot3Dsu6PortA", 71),
          ("t1e1TimingSlot3Dsu6PortB", 72),
          ("t1e1TimingSlot3PortA", 41),
          ("t1e1TimingSlot3PortB", 42),
          ("t1e1TimingSlot4Dsu1PortA", 73),
          ("t1e1TimingSlot4Dsu1PortB", 74),
          ("t1e1TimingSlot4Dsu2PortA", 75),
          ("t1e1TimingSlot4Dsu2PortB", 76),
          ("t1e1TimingSlot4Dsu3PortA", 77),
          ("t1e1TimingSlot4Dsu3PortB", 78),
          ("t1e1TimingSlot4Dsu4PortA", 79),
          ("t1e1TimingSlot4Dsu4PortB", 80),
          ("t1e1TimingSlot4Dsu5PortA", 81),
          ("t1e1TimingSlot4Dsu5PortB", 82),
          ("t1e1TimingSlot4Dsu6PortA", 83),
          ("t1e1TimingSlot4Dsu6PortB", 84),
          ("t1e1TimingSlot4PortA", 43),
          ("t1e1TimingSlot4PortB", 44),
          ("t1e1TimingSlot5Dsu1PortA", 85),
          ("t1e1TimingSlot5Dsu1PortB", 86),
          ("t1e1TimingSlot5Dsu2PortA", 87),
          ("t1e1TimingSlot5Dsu2PortB", 88),
          ("t1e1TimingSlot5Dsu3PortA", 89),
          ("t1e1TimingSlot5Dsu3PortB", 90),
          ("t1e1TimingSlot5Dsu4PortA", 91),
          ("t1e1TimingSlot5Dsu4PortB", 92),
          ("t1e1TimingSlot5Dsu5PortA", 93),
          ("t1e1TimingSlot5Dsu5PortB", 94),
          ("t1e1TimingSlot5Dsu6PortA", 95),
          ("t1e1TimingSlot5Dsu6PortB", 96),
          ("t1e1TimingSlot5PortA", 45),
          ("t1e1TimingSlot5PortB", 46),
          ("t1e1TimingSlot6Dsu1PortA", 97),
          ("t1e1TimingSlot6Dsu1PortB", 98),
          ("t1e1TimingSlot6Dsu2PortA", 99),
          ("t1e1TimingSlot6Dsu2PortB", 100),
          ("t1e1TimingSlot6Dsu3PortA", 101),
          ("t1e1TimingSlot6Dsu3PortB", 102),
          ("t1e1TimingSlot6Dsu4PortA", 103),
          ("t1e1TimingSlot6Dsu4PortB", 104),
          ("t1e1TimingSlot6Dsu5PortA", 105),
          ("t1e1TimingSlot6Dsu5PortB", 106),
          ("t1e1TimingSlot6Dsu6PortA", 107),
          ("t1e1TimingSlot6Dsu6PortB", 108),
          ("t1e1TimingSlot6PortA", 47),
          ("t1e1TimingSlot6PortB", 48),
          ("t1e1TimingStaClock", 6),
          ("t1e1TimingStation", 5),
          ("t1e1TimingT1DTE", 4))
    )


_T1e1Timing_Type.__name__ = "Integer32"
_T1e1Timing_Object = MibTableColumn
t1e1Timing = _T1e1Timing_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 9),
    _T1e1Timing_Type()
)
t1e1Timing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1Timing.setStatus("mandatory")


class _T1e1StationInTiming_Type(Integer32):
    """Custom type t1e1StationInTiming based on Integer32"""
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
        *(("t1e1StationInTiming1544", 4),
          ("t1e1StationInTiming2048", 5),
          ("t1e1StationInTimingNX56", 2),
          ("t1e1StationInTimingNX64", 3),
          ("t1e1StationInTimingOther", 1))
    )


_T1e1StationInTiming_Type.__name__ = "Integer32"
_T1e1StationInTiming_Object = MibTableColumn
t1e1StationInTiming = _T1e1StationInTiming_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 10),
    _T1e1StationInTiming_Type()
)
t1e1StationInTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1StationInTiming.setStatus("mandatory")
_T1e1StationTiming_Type = Integer32
_T1e1StationTiming_Object = MibTableColumn
t1e1StationTiming = _T1e1StationTiming_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 11),
    _T1e1StationTiming_Type()
)
t1e1StationTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1StationTiming.setStatus("mandatory")


class _T1e1PRM_Type(Integer32):
    """Custom type t1e1PRM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1PRMDisable", 2),
          ("t1e1PRMEnable", 3),
          ("t1e1PRMOther", 1))
    )


_T1e1PRM_Type.__name__ = "Integer32"
_T1e1PRM_Object = MibTableColumn
t1e1PRM = _T1e1PRM_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 12),
    _T1e1PRM_Type()
)
t1e1PRM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1PRM.setStatus("mandatory")


class _T1e1ZeroSuppress_Type(Integer32):
    """Custom type t1e1ZeroSuppress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1ZeroDisable", 2),
          ("t1e1ZeroEnable", 3),
          ("t1e1ZeroOther", 1))
    )


_T1e1ZeroSuppress_Type.__name__ = "Integer32"
_T1e1ZeroSuppress_Object = MibTableColumn
t1e1ZeroSuppress = _T1e1ZeroSuppress_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 13),
    _T1e1ZeroSuppress_Type()
)
t1e1ZeroSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1ZeroSuppress.setStatus("mandatory")


class _T1e1NationalBit_Type(Integer32):
    """Custom type t1e1NationalBit based on Integer32"""
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
        *(("t1e1NationalNone", 2),
          ("t1e1NationalOther", 1),
          ("t1e1NationalSA4", 3),
          ("t1e1NationalSA5", 4),
          ("t1e1NationalSA6", 5),
          ("t1e1NationalSA7", 6),
          ("t1e1NationalSA8", 7))
    )


_T1e1NationalBit_Type.__name__ = "Integer32"
_T1e1NationalBit_Object = MibTableColumn
t1e1NationalBit = _T1e1NationalBit_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 14),
    _T1e1NationalBit_Type()
)
t1e1NationalBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1NationalBit.setStatus("mandatory")


class _T1e1KeepAlive_Type(Integer32):
    """Custom type t1e1KeepAlive based on Integer32"""
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
        *(("t1e1KeepAliveFramedOnes", 3),
          ("t1e1KeepAliveLoop", 4),
          ("t1e1KeepAliveOther", 1),
          ("t1e1KeepAliveUnframedOnes", 2))
    )


_T1e1KeepAlive_Type.__name__ = "Integer32"
_T1e1KeepAlive_Object = MibTableColumn
t1e1KeepAlive = _T1e1KeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 15),
    _T1e1KeepAlive_Type()
)
t1e1KeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1KeepAlive.setStatus("mandatory")


class _T1e1CRC4Mode_Type(Integer32):
    """Custom type t1e1CRC4Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1CRC4Disabled", 2),
          ("t1e1CRC4Enabled", 3),
          ("t1e1CRC4Other", 1))
    )


_T1e1CRC4Mode_Type.__name__ = "Integer32"
_T1e1CRC4Mode_Object = MibTableColumn
t1e1CRC4Mode = _T1e1CRC4Mode_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 16),
    _T1e1CRC4Mode_Type()
)
t1e1CRC4Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1CRC4Mode.setStatus("mandatory")


class _T1e1DSXLevel_Type(Integer32):
    """Custom type t1e1DSXLevel based on Integer32"""
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
        *(("t1e1DSX0110", 2),
          ("t1e1DSX111220", 3),
          ("t1e1DSX221330", 4),
          ("t1e1DSX331440", 5),
          ("t1e1DSX441550", 6),
          ("t1e1DSX551660", 7),
          ("t1e1DSX661up", 8),
          ("t1e1DSXOther", 1))
    )


_T1e1DSXLevel_Type.__name__ = "Integer32"
_T1e1DSXLevel_Object = MibTableColumn
t1e1DSXLevel = _T1e1DSXLevel_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 17),
    _T1e1DSXLevel_Type()
)
t1e1DSXLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1DSXLevel.setStatus("mandatory")


class _T1e1CRC_Type(Integer32):
    """Custom type t1e1CRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1CRCOther", 1),
          ("t1e1CRCPass", 2),
          ("t1e1CRCRegenerate", 3))
    )


_T1e1CRC_Type.__name__ = "Integer32"
_T1e1CRC_Object = MibTableColumn
t1e1CRC = _T1e1CRC_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 18),
    _T1e1CRC_Type()
)
t1e1CRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1CRC.setStatus("mandatory")


class _T1e1FDLPassThrough_Type(Integer32):
    """Custom type t1e1FDLPassThrough based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1FDLPassThroughOther", 1),
          ("t1e1FDLPassThroughPass", 2),
          ("t1e1FDLPassThroughTerminate", 3))
    )


_T1e1FDLPassThrough_Type.__name__ = "Integer32"
_T1e1FDLPassThrough_Object = MibTableColumn
t1e1FDLPassThrough = _T1e1FDLPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 19),
    _T1e1FDLPassThrough_Type()
)
t1e1FDLPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1FDLPassThrough.setStatus("mandatory")


class _T1e1AudibleAlarm_Type(Integer32):
    """Custom type t1e1AudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1AudibleAlarmDisabled", 2),
          ("t1e1AudibleAlarmEnabled", 3),
          ("t1e1AudibleAlarmOther", 1))
    )


_T1e1AudibleAlarm_Type.__name__ = "Integer32"
_T1e1AudibleAlarm_Object = MibTableColumn
t1e1AudibleAlarm = _T1e1AudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 1, 1, 20),
    _T1e1AudibleAlarm_Type()
)
t1e1AudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1AudibleAlarm.setStatus("mandatory")
_T1e1AlarmTable_Object = MibTable
t1e1AlarmTable = _T1e1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2)
)
if mibBuilder.loadTexts:
    t1e1AlarmTable.setStatus("optional")
_T1e1AlarmTableEntry_Object = MibTableRow
t1e1AlarmTableEntry = _T1e1AlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1)
)
t1e1AlarmTableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "t1e1AlarmNearIndex"),
    (0, "INTERFACES-MIB", "t1e1AlarmFarIndex"),
    (0, "INTERFACES-MIB", "t1e1AlarmIndex"),
)
if mibBuilder.loadTexts:
    t1e1AlarmTableEntry.setStatus("mandatory")
_T1e1AlarmNearIndex_Type = Integer32
_T1e1AlarmNearIndex_Object = MibTableColumn
t1e1AlarmNearIndex = _T1e1AlarmNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 1),
    _T1e1AlarmNearIndex_Type()
)
t1e1AlarmNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1AlarmNearIndex.setStatus("mandatory")
_T1e1AlarmFarIndex_Type = Integer32
_T1e1AlarmFarIndex_Object = MibTableColumn
t1e1AlarmFarIndex = _T1e1AlarmFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 2),
    _T1e1AlarmFarIndex_Type()
)
t1e1AlarmFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1AlarmFarIndex.setStatus("mandatory")
_T1e1AlarmIndex_Type = Integer32
_T1e1AlarmIndex_Object = MibTableColumn
t1e1AlarmIndex = _T1e1AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 3),
    _T1e1AlarmIndex_Type()
)
t1e1AlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1AlarmIndex.setStatus("mandatory")


class _T1e1StatusSummary_Type(DisplayString):
    """Custom type t1e1StatusSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_T1e1StatusSummary_Type.__name__ = "DisplayString"
_T1e1StatusSummary_Object = MibTableColumn
t1e1StatusSummary = _T1e1StatusSummary_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 4),
    _T1e1StatusSummary_Type()
)
t1e1StatusSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1StatusSummary.setStatus("mandatory")


class _T1e1AlarmSummary_Type(DisplayString):
    """Custom type t1e1AlarmSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_T1e1AlarmSummary_Type.__name__ = "DisplayString"
_T1e1AlarmSummary_Object = MibTableColumn
t1e1AlarmSummary = _T1e1AlarmSummary_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 5),
    _T1e1AlarmSummary_Type()
)
t1e1AlarmSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1AlarmSummary.setStatus("mandatory")


class _T1e1ESStatus_Type(Integer32):
    """Custom type t1e1ESStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1StatusES", 3),
          ("t1e1StatusNoES", 2),
          ("t1e1StatusOther", 1))
    )


_T1e1ESStatus_Type.__name__ = "Integer32"
_T1e1ESStatus_Object = MibTableColumn
t1e1ESStatus = _T1e1ESStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 6),
    _T1e1ESStatus_Type()
)
t1e1ESStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1ESStatus.setStatus("mandatory")
_T1e1ESCount_Type = Integer32
_T1e1ESCount_Object = MibTableColumn
t1e1ESCount = _T1e1ESCount_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 7),
    _T1e1ESCount_Type()
)
t1e1ESCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1ESCount.setStatus("mandatory")
_T1e1ESThreshold_Type = Integer32
_T1e1ESThreshold_Object = MibTableColumn
t1e1ESThreshold = _T1e1ESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 8),
    _T1e1ESThreshold_Type()
)
t1e1ESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1ESThreshold.setStatus("mandatory")


class _T1e1ESAlarm_Type(Integer32):
    """Custom type t1e1ESAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1ESAlarmNone", 2),
          ("t1e1ESAlarmOther", 1),
          ("t1e1ESAlarmThresholdExceeded", 3))
    )


_T1e1ESAlarm_Type.__name__ = "Integer32"
_T1e1ESAlarm_Object = MibTableColumn
t1e1ESAlarm = _T1e1ESAlarm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 9),
    _T1e1ESAlarm_Type()
)
t1e1ESAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1ESAlarm.setStatus("mandatory")


class _T1e1SESStatus_Type(Integer32):
    """Custom type t1e1SESStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1StatusNoSES", 2),
          ("t1e1StatusOther", 1),
          ("t1e1StatusSES", 3))
    )


_T1e1SESStatus_Type.__name__ = "Integer32"
_T1e1SESStatus_Object = MibTableColumn
t1e1SESStatus = _T1e1SESStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 10),
    _T1e1SESStatus_Type()
)
t1e1SESStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1SESStatus.setStatus("mandatory")
_T1e1SESCount_Type = Integer32
_T1e1SESCount_Object = MibTableColumn
t1e1SESCount = _T1e1SESCount_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 11),
    _T1e1SESCount_Type()
)
t1e1SESCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1SESCount.setStatus("mandatory")
_T1e1SESThreshold_Type = Integer32
_T1e1SESThreshold_Object = MibTableColumn
t1e1SESThreshold = _T1e1SESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 12),
    _T1e1SESThreshold_Type()
)
t1e1SESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1SESThreshold.setStatus("mandatory")


class _T1e1SESAlarm_Type(Integer32):
    """Custom type t1e1SESAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1SESAlarmNone", 2),
          ("t1e1SESAlarmOther", 1),
          ("t1e1SESAlarmThresholdExceeded", 3))
    )


_T1e1SESAlarm_Type.__name__ = "Integer32"
_T1e1SESAlarm_Object = MibTableColumn
t1e1SESAlarm = _T1e1SESAlarm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 13),
    _T1e1SESAlarm_Type()
)
t1e1SESAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1SESAlarm.setStatus("mandatory")


class _T1e1LOSSStatus_Type(Integer32):
    """Custom type t1e1LOSSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1StatusLOSS", 3),
          ("t1e1StatusNoLOSS", 2),
          ("t1e1StatusOther", 1))
    )


_T1e1LOSSStatus_Type.__name__ = "Integer32"
_T1e1LOSSStatus_Object = MibTableColumn
t1e1LOSSStatus = _T1e1LOSSStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 14),
    _T1e1LOSSStatus_Type()
)
t1e1LOSSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1LOSSStatus.setStatus("mandatory")
_T1e1LOSSCount_Type = Integer32
_T1e1LOSSCount_Object = MibTableColumn
t1e1LOSSCount = _T1e1LOSSCount_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 15),
    _T1e1LOSSCount_Type()
)
t1e1LOSSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1LOSSCount.setStatus("mandatory")
_T1e1LOSSThreshold_Type = Integer32
_T1e1LOSSThreshold_Object = MibTableColumn
t1e1LOSSThreshold = _T1e1LOSSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 16),
    _T1e1LOSSThreshold_Type()
)
t1e1LOSSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1LOSSThreshold.setStatus("mandatory")


class _T1e1LOSSAlarm_Type(Integer32):
    """Custom type t1e1LOSSAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1LOSSAlarmNone", 2),
          ("t1e1LOSSAlarmOther", 1),
          ("t1e1LOSSAlarmThresholdExceeded", 3))
    )


_T1e1LOSSAlarm_Type.__name__ = "Integer32"
_T1e1LOSSAlarm_Object = MibTableColumn
t1e1LOSSAlarm = _T1e1LOSSAlarm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 17),
    _T1e1LOSSAlarm_Type()
)
t1e1LOSSAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1LOSSAlarm.setStatus("mandatory")


class _T1e1UASStatus_Type(Integer32):
    """Custom type t1e1UASStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1StatusNoUAS", 2),
          ("t1e1StatusOther", 1),
          ("t1e1StatusUAS", 3))
    )


_T1e1UASStatus_Type.__name__ = "Integer32"
_T1e1UASStatus_Object = MibTableColumn
t1e1UASStatus = _T1e1UASStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 18),
    _T1e1UASStatus_Type()
)
t1e1UASStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1UASStatus.setStatus("mandatory")
_T1e1UASCount_Type = Integer32
_T1e1UASCount_Object = MibTableColumn
t1e1UASCount = _T1e1UASCount_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 19),
    _T1e1UASCount_Type()
)
t1e1UASCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1UASCount.setStatus("mandatory")
_T1e1UASThreshold_Type = Integer32
_T1e1UASThreshold_Object = MibTableColumn
t1e1UASThreshold = _T1e1UASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 20),
    _T1e1UASThreshold_Type()
)
t1e1UASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1UASThreshold.setStatus("mandatory")


class _T1e1UASAlarm_Type(Integer32):
    """Custom type t1e1UASAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1UASAlarmNone", 2),
          ("t1e1UASAlarmOther", 1),
          ("t1e1UASAlarmThresholdExceeded", 3))
    )


_T1e1UASAlarm_Type.__name__ = "Integer32"
_T1e1UASAlarm_Object = MibTableColumn
t1e1UASAlarm = _T1e1UASAlarm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 21),
    _T1e1UASAlarm_Type()
)
t1e1UASAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1UASAlarm.setStatus("mandatory")


class _T1e1CSSStatus_Type(Integer32):
    """Custom type t1e1CSSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1StatusCSS", 3),
          ("t1e1StatusNoCSS", 2),
          ("t1e1StatusOther", 1))
    )


_T1e1CSSStatus_Type.__name__ = "Integer32"
_T1e1CSSStatus_Object = MibTableColumn
t1e1CSSStatus = _T1e1CSSStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 22),
    _T1e1CSSStatus_Type()
)
t1e1CSSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1CSSStatus.setStatus("mandatory")
_T1e1CSSCount_Type = Integer32
_T1e1CSSCount_Object = MibTableColumn
t1e1CSSCount = _T1e1CSSCount_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 23),
    _T1e1CSSCount_Type()
)
t1e1CSSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1CSSCount.setStatus("mandatory")
_T1e1CSSThreshold_Type = Integer32
_T1e1CSSThreshold_Object = MibTableColumn
t1e1CSSThreshold = _T1e1CSSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 24),
    _T1e1CSSThreshold_Type()
)
t1e1CSSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1CSSThreshold.setStatus("mandatory")


class _T1e1CSSAlarm_Type(Integer32):
    """Custom type t1e1CSSAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1CSSAlarmNone", 2),
          ("t1e1CSSAlarmOther", 1),
          ("t1e1CSSAlarmThresholdExceeded", 3))
    )


_T1e1CSSAlarm_Type.__name__ = "Integer32"
_T1e1CSSAlarm_Object = MibTableColumn
t1e1CSSAlarm = _T1e1CSSAlarm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 25),
    _T1e1CSSAlarm_Type()
)
t1e1CSSAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1CSSAlarm.setStatus("mandatory")


class _T1e1BPVSStatus_Type(Integer32):
    """Custom type t1e1BPVSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1StatusBPVS", 3),
          ("t1e1StatusNoBPVS", 2),
          ("t1e1StatusOther", 1))
    )


_T1e1BPVSStatus_Type.__name__ = "Integer32"
_T1e1BPVSStatus_Object = MibTableColumn
t1e1BPVSStatus = _T1e1BPVSStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 26),
    _T1e1BPVSStatus_Type()
)
t1e1BPVSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1BPVSStatus.setStatus("mandatory")
_T1e1BPVSCount_Type = Integer32
_T1e1BPVSCount_Object = MibTableColumn
t1e1BPVSCount = _T1e1BPVSCount_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 27),
    _T1e1BPVSCount_Type()
)
t1e1BPVSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1BPVSCount.setStatus("mandatory")
_T1e1BPVSThreshold_Type = Integer32
_T1e1BPVSThreshold_Object = MibTableColumn
t1e1BPVSThreshold = _T1e1BPVSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 28),
    _T1e1BPVSThreshold_Type()
)
t1e1BPVSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1BPVSThreshold.setStatus("mandatory")


class _T1e1BPVSAlarm_Type(Integer32):
    """Custom type t1e1BPVSAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1BPVSAlarmNone", 2),
          ("t1e1BPVSAlarmOther", 1),
          ("t1e1BPVSAlarmThresholdExceeded", 3))
    )


_T1e1BPVSAlarm_Type.__name__ = "Integer32"
_T1e1BPVSAlarm_Object = MibTableColumn
t1e1BPVSAlarm = _T1e1BPVSAlarm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 29),
    _T1e1BPVSAlarm_Type()
)
t1e1BPVSAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1BPVSAlarm.setStatus("mandatory")


class _T1e1OOFSStatus_Type(Integer32):
    """Custom type t1e1OOFSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1StatusNoOOF", 2),
          ("t1e1StatusOOF", 3),
          ("t1e1StatusOther", 1))
    )


_T1e1OOFSStatus_Type.__name__ = "Integer32"
_T1e1OOFSStatus_Object = MibTableColumn
t1e1OOFSStatus = _T1e1OOFSStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 30),
    _T1e1OOFSStatus_Type()
)
t1e1OOFSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1OOFSStatus.setStatus("mandatory")
_T1e1OOFSCount_Type = Integer32
_T1e1OOFSCount_Object = MibTableColumn
t1e1OOFSCount = _T1e1OOFSCount_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 31),
    _T1e1OOFSCount_Type()
)
t1e1OOFSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1OOFSCount.setStatus("mandatory")
_T1e1OOFSThreshold_Type = Integer32
_T1e1OOFSThreshold_Object = MibTableColumn
t1e1OOFSThreshold = _T1e1OOFSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 32),
    _T1e1OOFSThreshold_Type()
)
t1e1OOFSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1OOFSThreshold.setStatus("mandatory")


class _T1e1OOFSAlarm_Type(Integer32):
    """Custom type t1e1OOFSAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1OOFSAlarmExists", 3),
          ("t1e1OOFSAlarmNone", 2),
          ("t1e1OOFSAlarmOther", 1))
    )


_T1e1OOFSAlarm_Type.__name__ = "Integer32"
_T1e1OOFSAlarm_Object = MibTableColumn
t1e1OOFSAlarm = _T1e1OOFSAlarm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 33),
    _T1e1OOFSAlarm_Type()
)
t1e1OOFSAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1OOFSAlarm.setStatus("mandatory")


class _T1e1AISStatus_Type(Integer32):
    """Custom type t1e1AISStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1StatusAIS", 3),
          ("t1e1StatusNoAIS", 2),
          ("t1e1StatusOther", 1))
    )


_T1e1AISStatus_Type.__name__ = "Integer32"
_T1e1AISStatus_Object = MibTableColumn
t1e1AISStatus = _T1e1AISStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 34),
    _T1e1AISStatus_Type()
)
t1e1AISStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1AISStatus.setStatus("mandatory")
_T1e1AISCount_Type = Integer32
_T1e1AISCount_Object = MibTableColumn
t1e1AISCount = _T1e1AISCount_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 35),
    _T1e1AISCount_Type()
)
t1e1AISCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1AISCount.setStatus("mandatory")
_T1e1AISThreshold_Type = Integer32
_T1e1AISThreshold_Object = MibTableColumn
t1e1AISThreshold = _T1e1AISThreshold_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 36),
    _T1e1AISThreshold_Type()
)
t1e1AISThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1AISThreshold.setStatus("mandatory")


class _T1e1AISAlarm_Type(Integer32):
    """Custom type t1e1AISAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1AISAlarmExists", 3),
          ("t1e1AISAlarmNone", 2),
          ("t1e1AISAlarmOther", 1))
    )


_T1e1AISAlarm_Type.__name__ = "Integer32"
_T1e1AISAlarm_Object = MibTableColumn
t1e1AISAlarm = _T1e1AISAlarm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 37),
    _T1e1AISAlarm_Type()
)
t1e1AISAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1AISAlarm.setStatus("mandatory")


class _T1e1RASStatus_Type(Integer32):
    """Custom type t1e1RASStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1RASStatusNoRAS", 2),
          ("t1e1RASStatusOther", 1),
          ("t1e1RASStatusRAS", 3))
    )


_T1e1RASStatus_Type.__name__ = "Integer32"
_T1e1RASStatus_Object = MibTableColumn
t1e1RASStatus = _T1e1RASStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 38),
    _T1e1RASStatus_Type()
)
t1e1RASStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1RASStatus.setStatus("mandatory")
_T1e1RASCount_Type = Integer32
_T1e1RASCount_Object = MibTableColumn
t1e1RASCount = _T1e1RASCount_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 39),
    _T1e1RASCount_Type()
)
t1e1RASCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1RASCount.setStatus("mandatory")
_T1e1RASThreshold_Type = Integer32
_T1e1RASThreshold_Object = MibTableColumn
t1e1RASThreshold = _T1e1RASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 40),
    _T1e1RASThreshold_Type()
)
t1e1RASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1RASThreshold.setStatus("mandatory")


class _T1e1RASAlarm_Type(Integer32):
    """Custom type t1e1RASAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1e1RASAlarmExists", 3),
          ("t1e1RASAlarmNone", 2),
          ("t1e1RASAlarmOther", 1))
    )


_T1e1RASAlarm_Type.__name__ = "Integer32"
_T1e1RASAlarm_Object = MibTableColumn
t1e1RASAlarm = _T1e1RASAlarm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 41),
    _T1e1RASAlarm_Type()
)
t1e1RASAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1RASAlarm.setStatus("mandatory")
_T1e1AlarmResetTimer_Type = Integer32
_T1e1AlarmResetTimer_Object = MibTableColumn
t1e1AlarmResetTimer = _T1e1AlarmResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 42),
    _T1e1AlarmResetTimer_Type()
)
t1e1AlarmResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1AlarmResetTimer.setStatus("mandatory")


class _T1e1AlarmReset_Type(Integer32):
    """Custom type t1e1AlarmReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t1e1AlarmResetClearAlarms", 2),
          ("t1e1AlarmResetOther", 1))
    )


_T1e1AlarmReset_Type.__name__ = "Integer32"
_T1e1AlarmReset_Object = MibTableColumn
t1e1AlarmReset = _T1e1AlarmReset_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 3, 2, 1, 43),
    _T1e1AlarmReset_Type()
)
t1e1AlarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1AlarmReset.setStatus("mandatory")
_DdsNet_ObjectIdentity = ObjectIdentity
ddsNet = _DdsNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 8, 4)
)
_DdsNetConfigTable_Object = MibTable
ddsNetConfigTable = _DdsNetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 1)
)
if mibBuilder.loadTexts:
    ddsNetConfigTable.setStatus("optional")
_DdsNetConfigTableEntry_Object = MibTableRow
ddsNetConfigTableEntry = _DdsNetConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 1, 1)
)
ddsNetConfigTableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "ddsNetConfigNearIndex"),
    (0, "INTERFACES-MIB", "ddsNetConfigFarIndex"),
    (0, "INTERFACES-MIB", "ddsNetConfigIndex"),
)
if mibBuilder.loadTexts:
    ddsNetConfigTableEntry.setStatus("mandatory")
_DdsNetConfigNearIndex_Type = Integer32
_DdsNetConfigNearIndex_Object = MibTableColumn
ddsNetConfigNearIndex = _DdsNetConfigNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 1, 1, 1),
    _DdsNetConfigNearIndex_Type()
)
ddsNetConfigNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetConfigNearIndex.setStatus("mandatory")
_DdsNetConfigFarIndex_Type = Integer32
_DdsNetConfigFarIndex_Object = MibTableColumn
ddsNetConfigFarIndex = _DdsNetConfigFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 1, 1, 2),
    _DdsNetConfigFarIndex_Type()
)
ddsNetConfigFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetConfigFarIndex.setStatus("mandatory")
_DdsNetConfigIndex_Type = Integer32
_DdsNetConfigIndex_Object = MibTableColumn
ddsNetConfigIndex = _DdsNetConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 1, 1, 3),
    _DdsNetConfigIndex_Type()
)
ddsNetConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetConfigIndex.setStatus("mandatory")


class _DdsNetDescription_Type(DisplayString):
    """Custom type ddsNetDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DdsNetDescription_Type.__name__ = "DisplayString"
_DdsNetDescription_Object = MibTableColumn
ddsNetDescription = _DdsNetDescription_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 1, 1, 4),
    _DdsNetDescription_Type()
)
ddsNetDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsNetDescription.setStatus("mandatory")


class _DdsNetRate_Type(Integer32):
    """Custom type ddsNetRate based on Integer32"""
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
        *(("ddsNetRate19200", 4),
          ("ddsNetRate2400", 1),
          ("ddsNetRate38400", 5),
          ("ddsNetRate4800", 2),
          ("ddsNetRate56000", 6),
          ("ddsNetRate64000", 7),
          ("ddsNetRate9600", 3))
    )


_DdsNetRate_Type.__name__ = "Integer32"
_DdsNetRate_Object = MibTableColumn
ddsNetRate = _DdsNetRate_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 1, 1, 5),
    _DdsNetRate_Type()
)
ddsNetRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsNetRate.setStatus("mandatory")


class _DdsNetMode_Type(Integer32):
    """Custom type ddsNetMode based on Integer32"""
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
        *(("ddsNetMode64KCCProprietaryTXPII", 4),
          ("ddsNetMode64KClearChannel", 3),
          ("ddsNetModeNormal", 1),
          ("ddsNetModeProprietaryTXPI", 2))
    )


_DdsNetMode_Type.__name__ = "Integer32"
_DdsNetMode_Object = MibTableColumn
ddsNetMode = _DdsNetMode_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 1, 1, 6),
    _DdsNetMode_Type()
)
ddsNetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsNetMode.setStatus("mandatory")


class _DdsNetTimingSource_Type(Integer32):
    """Custom type ddsNetTimingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddsNetTimingDTE", 3),
          ("ddsNetTimingInt", 2),
          ("ddsNetTimingNet", 1))
    )


_DdsNetTimingSource_Type.__name__ = "Integer32"
_DdsNetTimingSource_Object = MibTableColumn
ddsNetTimingSource = _DdsNetTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 1, 1, 7),
    _DdsNetTimingSource_Type()
)
ddsNetTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsNetTimingSource.setStatus("mandatory")


class _DdsNetRemComm_Type(Integer32):
    """Custom type ddsNetRemComm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddsNetRemCommDisabled", 2),
          ("ddsNetRemCommEnabled", 1),
          ("ddsNetRemCommNotAvailable", 3))
    )


_DdsNetRemComm_Type.__name__ = "Integer32"
_DdsNetRemComm_Object = MibTableColumn
ddsNetRemComm = _DdsNetRemComm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 1, 1, 8),
    _DdsNetRemComm_Type()
)
ddsNetRemComm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetRemComm.setStatus("mandatory")


class _DdsNetCircuitAssur_Type(Integer32):
    """Custom type ddsNetCircuitAssur based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddsNetCircuitAssurDisabled", 2),
          ("ddsNetCircuitAssurEnabled", 1),
          ("ddsNetCircuitAssurNotAvailable", 3))
    )


_DdsNetCircuitAssur_Type.__name__ = "Integer32"
_DdsNetCircuitAssur_Object = MibTableColumn
ddsNetCircuitAssur = _DdsNetCircuitAssur_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 1, 1, 9),
    _DdsNetCircuitAssur_Type()
)
ddsNetCircuitAssur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsNetCircuitAssur.setStatus("mandatory")


class _DdsNetAntiStrTimer_Type(Integer32):
    """Custom type ddsNetAntiStrTimer based on Integer32"""
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
        *(("ddsNetAntiStrTimer10", 2),
          ("ddsNetAntiStrTimer30", 3),
          ("ddsNetAntiStrTimer60", 4),
          ("ddsNetAntiStrTimerOff", 1))
    )


_DdsNetAntiStrTimer_Type.__name__ = "Integer32"
_DdsNetAntiStrTimer_Object = MibTableColumn
ddsNetAntiStrTimer = _DdsNetAntiStrTimer_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 1, 1, 10),
    _DdsNetAntiStrTimer_Type()
)
ddsNetAntiStrTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsNetAntiStrTimer.setStatus("mandatory")
_DdsNetAlarmTable_Object = MibTable
ddsNetAlarmTable = _DdsNetAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2)
)
if mibBuilder.loadTexts:
    ddsNetAlarmTable.setStatus("optional")
_DdsNetAlarmTableEntry_Object = MibTableRow
ddsNetAlarmTableEntry = _DdsNetAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1)
)
ddsNetAlarmTableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "ddsNetAlarmNearIndex"),
    (0, "INTERFACES-MIB", "ddsNetAlarmFarIndex"),
    (0, "INTERFACES-MIB", "ddsNetAlarmIndex"),
)
if mibBuilder.loadTexts:
    ddsNetAlarmTableEntry.setStatus("mandatory")
_DdsNetAlarmNearIndex_Type = Integer32
_DdsNetAlarmNearIndex_Object = MibTableColumn
ddsNetAlarmNearIndex = _DdsNetAlarmNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 1),
    _DdsNetAlarmNearIndex_Type()
)
ddsNetAlarmNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetAlarmNearIndex.setStatus("mandatory")
_DdsNetAlarmFarIndex_Type = Integer32
_DdsNetAlarmFarIndex_Object = MibTableColumn
ddsNetAlarmFarIndex = _DdsNetAlarmFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 2),
    _DdsNetAlarmFarIndex_Type()
)
ddsNetAlarmFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetAlarmFarIndex.setStatus("mandatory")
_DdsNetAlarmIndex_Type = Integer32
_DdsNetAlarmIndex_Object = MibTableColumn
ddsNetAlarmIndex = _DdsNetAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 3),
    _DdsNetAlarmIndex_Type()
)
ddsNetAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetAlarmIndex.setStatus("mandatory")


class _DdsNetStatusSummary_Type(DisplayString):
    """Custom type ddsNetStatusSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DdsNetStatusSummary_Type.__name__ = "DisplayString"
_DdsNetStatusSummary_Object = MibTableColumn
ddsNetStatusSummary = _DdsNetStatusSummary_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 4),
    _DdsNetStatusSummary_Type()
)
ddsNetStatusSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetStatusSummary.setStatus("mandatory")


class _DdsNetAlarmSummary_Type(DisplayString):
    """Custom type ddsNetAlarmSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DdsNetAlarmSummary_Type.__name__ = "DisplayString"
_DdsNetAlarmSummary_Object = MibTableColumn
ddsNetAlarmSummary = _DdsNetAlarmSummary_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 5),
    _DdsNetAlarmSummary_Type()
)
ddsNetAlarmSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetAlarmSummary.setStatus("mandatory")


class _DdsNetLOSStatus_Type(Integer32):
    """Custom type ddsNetLOSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddsNetStatusLOS", 3),
          ("ddsNetStatusLOSOther", 1),
          ("ddsNetStatusNoLOS", 2))
    )


_DdsNetLOSStatus_Type.__name__ = "Integer32"
_DdsNetLOSStatus_Object = MibTableColumn
ddsNetLOSStatus = _DdsNetLOSStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 6),
    _DdsNetLOSStatus_Type()
)
ddsNetLOSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetLOSStatus.setStatus("mandatory")
_DdsNetLOSCount_Type = Integer32
_DdsNetLOSCount_Object = MibTableColumn
ddsNetLOSCount = _DdsNetLOSCount_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 7),
    _DdsNetLOSCount_Type()
)
ddsNetLOSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetLOSCount.setStatus("mandatory")


class _DdsNetLOSThreshold_Type(Integer32):
    """Custom type ddsNetLOSThreshold based on Integer32"""
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
        *(("ddsNetLOSThreshold1", 3),
          ("ddsNetLOSThreshold10", 8),
          ("ddsNetLOSThreshold2", 4),
          ("ddsNetLOSThreshold20", 9),
          ("ddsNetLOSThreshold3", 5),
          ("ddsNetLOSThreshold30", 10),
          ("ddsNetLOSThreshold4", 6),
          ("ddsNetLOSThreshold5", 7),
          ("ddsNetLOSThresholdNone", 2),
          ("ddsNetLOSThresholdOther", 1))
    )


_DdsNetLOSThreshold_Type.__name__ = "Integer32"
_DdsNetLOSThreshold_Object = MibTableColumn
ddsNetLOSThreshold = _DdsNetLOSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 8),
    _DdsNetLOSThreshold_Type()
)
ddsNetLOSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsNetLOSThreshold.setStatus("mandatory")


class _DdsNetLOSAlarm_Type(Integer32):
    """Custom type ddsNetLOSAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddsNetLOSAlarmNone", 2),
          ("ddsNetLOSAlarmOther", 1),
          ("ddsNetLOSAlarmThresholdExceeded", 3))
    )


_DdsNetLOSAlarm_Type.__name__ = "Integer32"
_DdsNetLOSAlarm_Object = MibTableColumn
ddsNetLOSAlarm = _DdsNetLOSAlarm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 9),
    _DdsNetLOSAlarm_Type()
)
ddsNetLOSAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetLOSAlarm.setStatus("mandatory")


class _DdsNetOOFStatus_Type(Integer32):
    """Custom type ddsNetOOFStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddsNetStatusNoOOF", 2),
          ("ddsNetStatusOOF", 3),
          ("ddsNetStatusOOFOther", 1))
    )


_DdsNetOOFStatus_Type.__name__ = "Integer32"
_DdsNetOOFStatus_Object = MibTableColumn
ddsNetOOFStatus = _DdsNetOOFStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 10),
    _DdsNetOOFStatus_Type()
)
ddsNetOOFStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetOOFStatus.setStatus("mandatory")
_DdsNetOOFCount_Type = Integer32
_DdsNetOOFCount_Object = MibTableColumn
ddsNetOOFCount = _DdsNetOOFCount_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 11),
    _DdsNetOOFCount_Type()
)
ddsNetOOFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetOOFCount.setStatus("mandatory")


class _DdsNetOOFThreshold_Type(Integer32):
    """Custom type ddsNetOOFThreshold based on Integer32"""
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
        *(("ddsNetOOFThreshold1", 3),
          ("ddsNetOOFThreshold10", 8),
          ("ddsNetOOFThreshold2", 4),
          ("ddsNetOOFThreshold20", 9),
          ("ddsNetOOFThreshold3", 5),
          ("ddsNetOOFThreshold30", 10),
          ("ddsNetOOFThreshold4", 6),
          ("ddsNetOOFThreshold5", 7),
          ("ddsNetOOFThresholdNone", 2),
          ("ddsNetOOFThresholdOther", 1))
    )


_DdsNetOOFThreshold_Type.__name__ = "Integer32"
_DdsNetOOFThreshold_Object = MibTableColumn
ddsNetOOFThreshold = _DdsNetOOFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 12),
    _DdsNetOOFThreshold_Type()
)
ddsNetOOFThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsNetOOFThreshold.setStatus("mandatory")


class _DdsNetOOFAlarm_Type(Integer32):
    """Custom type ddsNetOOFAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddsNetOOFSAlarmNone", 2),
          ("ddsNetOOFSAlarmOther", 1),
          ("ddsNetOOFSAlarmThresholdExceeded", 3))
    )


_DdsNetOOFAlarm_Type.__name__ = "Integer32"
_DdsNetOOFAlarm_Object = MibTableColumn
ddsNetOOFAlarm = _DdsNetOOFAlarm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 13),
    _DdsNetOOFAlarm_Type()
)
ddsNetOOFAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetOOFAlarm.setStatus("mandatory")


class _DdsNetOOSStatus_Type(Integer32):
    """Custom type ddsNetOOSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddsNetStatusNoOOS", 2),
          ("ddsNetStatusOOS", 3),
          ("ddsNetStatusOOSOther", 1))
    )


_DdsNetOOSStatus_Type.__name__ = "Integer32"
_DdsNetOOSStatus_Object = MibTableColumn
ddsNetOOSStatus = _DdsNetOOSStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 14),
    _DdsNetOOSStatus_Type()
)
ddsNetOOSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetOOSStatus.setStatus("mandatory")
_DdsNetOOSCount_Type = Integer32
_DdsNetOOSCount_Object = MibTableColumn
ddsNetOOSCount = _DdsNetOOSCount_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 15),
    _DdsNetOOSCount_Type()
)
ddsNetOOSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetOOSCount.setStatus("mandatory")


class _DdsNetOOSThreshold_Type(Integer32):
    """Custom type ddsNetOOSThreshold based on Integer32"""
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
        *(("ddsNetOOSThreshold1", 3),
          ("ddsNetOOSThreshold10", 8),
          ("ddsNetOOSThreshold2", 4),
          ("ddsNetOOSThreshold20", 9),
          ("ddsNetOOSThreshold3", 5),
          ("ddsNetOOSThreshold30", 10),
          ("ddsNetOOSThreshold4", 6),
          ("ddsNetOOSThreshold5", 7),
          ("ddsNetOOSThresholdNone", 2),
          ("ddsNetOOSThresholdOther", 1))
    )


_DdsNetOOSThreshold_Type.__name__ = "Integer32"
_DdsNetOOSThreshold_Object = MibTableColumn
ddsNetOOSThreshold = _DdsNetOOSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 16),
    _DdsNetOOSThreshold_Type()
)
ddsNetOOSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsNetOOSThreshold.setStatus("mandatory")


class _DdsNetOOSAlarm_Type(Integer32):
    """Custom type ddsNetOOSAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddsNetOOSAlarmNone", 2),
          ("ddsNetOOSAlarmOther", 1),
          ("ddsNetOOSAlarmThresholdExceeded", 3))
    )


_DdsNetOOSAlarm_Type.__name__ = "Integer32"
_DdsNetOOSAlarm_Object = MibTableColumn
ddsNetOOSAlarm = _DdsNetOOSAlarm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 17),
    _DdsNetOOSAlarm_Type()
)
ddsNetOOSAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetOOSAlarm.setStatus("mandatory")


class _DdsNetFDLStatus_Type(Integer32):
    """Custom type ddsNetFDLStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddsNetStatusFDL", 3),
          ("ddsNetStatusFDLOther", 1),
          ("ddsNetStatusNoFDL", 2))
    )


_DdsNetFDLStatus_Type.__name__ = "Integer32"
_DdsNetFDLStatus_Object = MibTableColumn
ddsNetFDLStatus = _DdsNetFDLStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 18),
    _DdsNetFDLStatus_Type()
)
ddsNetFDLStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetFDLStatus.setStatus("mandatory")
_DdsNetFDLCount_Type = Integer32
_DdsNetFDLCount_Object = MibTableColumn
ddsNetFDLCount = _DdsNetFDLCount_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 19),
    _DdsNetFDLCount_Type()
)
ddsNetFDLCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetFDLCount.setStatus("mandatory")


class _DdsNetFDLThreshold_Type(Integer32):
    """Custom type ddsNetFDLThreshold based on Integer32"""
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
        *(("ddsNetFDLThreshold1", 3),
          ("ddsNetFDLThreshold10", 8),
          ("ddsNetFDLThreshold2", 4),
          ("ddsNetFDLThreshold20", 9),
          ("ddsNetFDLThreshold3", 5),
          ("ddsNetFDLThreshold30", 10),
          ("ddsNetFDLThreshold4", 6),
          ("ddsNetFDLThreshold5", 7),
          ("ddsNetFDLThresholdNone", 2),
          ("ddsNetFDLThresholdOther", 1))
    )


_DdsNetFDLThreshold_Type.__name__ = "Integer32"
_DdsNetFDLThreshold_Object = MibTableColumn
ddsNetFDLThreshold = _DdsNetFDLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 20),
    _DdsNetFDLThreshold_Type()
)
ddsNetFDLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsNetFDLThreshold.setStatus("mandatory")


class _DdsNetFDLAlarm_Type(Integer32):
    """Custom type ddsNetFDLAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddsNetFDLAlarmNone", 2),
          ("ddsNetFDLAlarmOther", 1),
          ("ddsNetFDLAlarmThresholdExceeded", 3))
    )


_DdsNetFDLAlarm_Type.__name__ = "Integer32"
_DdsNetFDLAlarm_Object = MibTableColumn
ddsNetFDLAlarm = _DdsNetFDLAlarm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 21),
    _DdsNetFDLAlarm_Type()
)
ddsNetFDLAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNetFDLAlarm.setStatus("mandatory")
_DdsNetAlarmResetTimer_Type = Integer32
_DdsNetAlarmResetTimer_Object = MibTableColumn
ddsNetAlarmResetTimer = _DdsNetAlarmResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 22),
    _DdsNetAlarmResetTimer_Type()
)
ddsNetAlarmResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsNetAlarmResetTimer.setStatus("mandatory")


class _DdsNetAlarmReset_Type(Integer32):
    """Custom type ddsNetAlarmReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ddsNetAlarmResetClearAlarms", 2),
          ("ddsNetAlarmResetOther", 1))
    )


_DdsNetAlarmReset_Type.__name__ = "Integer32"
_DdsNetAlarmReset_Object = MibTableColumn
ddsNetAlarmReset = _DdsNetAlarmReset_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 4, 2, 1, 23),
    _DdsNetAlarmReset_Type()
)
ddsNetAlarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsNetAlarmReset.setStatus("mandatory")
_SerialDte_ObjectIdentity = ObjectIdentity
serialDte = _SerialDte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 8, 5)
)
_SerialDteConfigTable_Object = MibTable
serialDteConfigTable = _SerialDteConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1)
)
if mibBuilder.loadTexts:
    serialDteConfigTable.setStatus("optional")
_SerialDteConfigTableEntry_Object = MibTableRow
serialDteConfigTableEntry = _SerialDteConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1)
)
serialDteConfigTableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "serialDteConfigNearIndex"),
    (0, "INTERFACES-MIB", "serialDteConfigFarIndex"),
    (0, "INTERFACES-MIB", "serialDteConfigIndex"),
)
if mibBuilder.loadTexts:
    serialDteConfigTableEntry.setStatus("mandatory")
_SerialDteConfigNearIndex_Type = Integer32
_SerialDteConfigNearIndex_Object = MibTableColumn
serialDteConfigNearIndex = _SerialDteConfigNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 1),
    _SerialDteConfigNearIndex_Type()
)
serialDteConfigNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteConfigNearIndex.setStatus("mandatory")
_SerialDteConfigFarIndex_Type = Integer32
_SerialDteConfigFarIndex_Object = MibTableColumn
serialDteConfigFarIndex = _SerialDteConfigFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 2),
    _SerialDteConfigFarIndex_Type()
)
serialDteConfigFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteConfigFarIndex.setStatus("mandatory")
_SerialDteConfigIndex_Type = Integer32
_SerialDteConfigIndex_Object = MibTableColumn
serialDteConfigIndex = _SerialDteConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 3),
    _SerialDteConfigIndex_Type()
)
serialDteConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteConfigIndex.setStatus("mandatory")


class _SerialDteDescription_Type(DisplayString):
    """Custom type serialDteDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SerialDteDescription_Type.__name__ = "DisplayString"
_SerialDteDescription_Object = MibTableColumn
serialDteDescription = _SerialDteDescription_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 4),
    _SerialDteDescription_Type()
)
serialDteDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteDescription.setStatus("mandatory")


class _SerialDteType_Type(Integer32):
    """Custom type serialDteType based on Integer32"""
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
        *(("serialDteTypeEIA530", 4),
          ("serialDteTypeOther", 1),
          ("serialDteTypeRS232", 3),
          ("serialDteTypeV35", 2))
    )


_SerialDteType_Type.__name__ = "Integer32"
_SerialDteType_Object = MibTableColumn
serialDteType = _SerialDteType_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 5),
    _SerialDteType_Type()
)
serialDteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteType.setStatus("mandatory")


class _SerialDteRate_Type(Integer32):
    """Custom type serialDteRate based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75)
        )
    )
    namedValues = NamedValues(
        *(("serialDteRate1008000", 40),
          ("serialDteRate1024000", 41),
          ("serialDteRate1064000", 42),
          ("serialDteRate1088000", 43),
          ("serialDteRate112000", 12),
          ("serialDteRate1120000", 44),
          ("serialDteRate115200", 75),
          ("serialDteRate1152000", 45),
          ("serialDteRate1176000", 46),
          ("serialDteRate1200", 70),
          ("serialDteRate1216000", 47),
          ("serialDteRate1232000", 48),
          ("serialDteRate128000", 13),
          ("serialDteRate1280000", 49),
          ("serialDteRate1288000", 50),
          ("serialDteRate1344000", 51),
          ("serialDteRate1400000", 52),
          ("serialDteRate1408000", 53),
          ("serialDteRate14400", 71),
          ("serialDteRate1456000", 54),
          ("serialDteRate1472000", 55),
          ("serialDteRate1512000", 56),
          ("serialDteRate1536000", 57),
          ("serialDteRate1568000", 58),
          ("serialDteRate1600000", 59),
          ("serialDteRate1624000", 60),
          ("serialDteRate1664000", 61),
          ("serialDteRate168000", 14),
          ("serialDteRate1680000", 62),
          ("serialDteRate1728000", 63),
          ("serialDteRate1736000", 64),
          ("serialDteRate1792000", 65),
          ("serialDteRate1856000", 66),
          ("serialDteRate19200", 5),
          ("serialDteRate192000", 15),
          ("serialDteRate1920000", 67),
          ("serialDteRate1984000", 68),
          ("serialDteRate2048000", 69),
          ("serialDteRate224000", 16),
          ("serialDteRate2400", 2),
          ("serialDteRate256000", 17),
          ("serialDteRate280000", 18),
          ("serialDteRate28800", 72),
          ("serialDteRate31200", 74),
          ("serialDteRate320000", 19),
          ("serialDteRate336000", 20),
          ("serialDteRate38400", 6),
          ("serialDteRate384000", 21),
          ("serialDteRate392000", 22),
          ("serialDteRate448000", 23),
          ("serialDteRate4800", 3),
          ("serialDteRate48000", 73),
          ("serialDteRate504000", 24),
          ("serialDteRate512000", 25),
          ("serialDteRate52000", 7),
          ("serialDteRate56000", 8),
          ("serialDteRate560000", 26),
          ("serialDteRate57600", 9),
          ("serialDteRate576000", 27),
          ("serialDteRate60000", 10),
          ("serialDteRate616000", 28),
          ("serialDteRate64000", 11),
          ("serialDteRate640000", 29),
          ("serialDteRate672000", 30),
          ("serialDteRate704000", 31),
          ("serialDteRate728000", 32),
          ("serialDteRate768000", 33),
          ("serialDteRate784000", 34),
          ("serialDteRate832000", 35),
          ("serialDteRate840000", 36),
          ("serialDteRate896000", 37),
          ("serialDteRate952000", 38),
          ("serialDteRate9600", 4),
          ("serialDteRate960000", 39),
          ("serialDteRateOther", 1))
    )


_SerialDteRate_Type.__name__ = "Integer32"
_SerialDteRate_Object = MibTableColumn
serialDteRate = _SerialDteRate_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 6),
    _SerialDteRate_Type()
)
serialDteRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteRate.setStatus("mandatory")


class _SerialDteInvertData_Type(Integer32):
    """Custom type serialDteInvertData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serialDteInvertDataDisabled", 2),
          ("serialDteInvertDataEnabled", 3),
          ("serialDteInvertDataOther", 1))
    )


_SerialDteInvertData_Type.__name__ = "Integer32"
_SerialDteInvertData_Object = MibTableColumn
serialDteInvertData = _SerialDteInvertData_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 7),
    _SerialDteInvertData_Type()
)
serialDteInvertData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteInvertData.setStatus("mandatory")


class _SerialDteFormat_Type(Integer32):
    """Custom type serialDteFormat based on Integer32"""
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
        *(("serialDteFormatAsync", 3),
          ("serialDteFormatNotAvail", 4),
          ("serialDteFormatOther", 1),
          ("serialDteFormatSync", 2))
    )


_SerialDteFormat_Type.__name__ = "Integer32"
_SerialDteFormat_Object = MibTableColumn
serialDteFormat = _SerialDteFormat_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 8),
    _SerialDteFormat_Type()
)
serialDteFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteFormat.setStatus("mandatory")


class _SerialDteParity_Type(Integer32):
    """Custom type serialDteParity based on Integer32"""
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
        *(("serialDteParityEven", 4),
          ("serialDteParityMark", 5),
          ("serialDteParityNone", 2),
          ("serialDteParityNotAvail", 7),
          ("serialDteParityOdd", 3),
          ("serialDteParityOther", 1),
          ("serialDteParitySpace", 6))
    )


_SerialDteParity_Type.__name__ = "Integer32"
_SerialDteParity_Object = MibTableColumn
serialDteParity = _SerialDteParity_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 9),
    _SerialDteParity_Type()
)
serialDteParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteParity.setStatus("mandatory")


class _SerialDteStopBit_Type(Integer32):
    """Custom type serialDteStopBit based on Integer32"""
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
        *(("serialDteStopBit1", 2),
          ("serialDteStopBit2", 3),
          ("serialDteStopBitNotAvail", 4),
          ("serialDteStopBitOther", 1))
    )


_SerialDteStopBit_Type.__name__ = "Integer32"
_SerialDteStopBit_Object = MibTableColumn
serialDteStopBit = _SerialDteStopBit_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 10),
    _SerialDteStopBit_Type()
)
serialDteStopBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteStopBit.setStatus("mandatory")


class _SerialDteMode_Type(Integer32):
    """Custom type serialDteMode based on Integer32"""
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
        *(("serialDteModeDDSI", 2),
          ("serialDteModeDDSII", 3),
          ("serialDteModeOther", 1),
          ("serialDteModeTxpIINormal", 6),
          ("serialDteModeTxpIITDM", 7),
          ("serialDteModeTxpINormal", 4),
          ("serialDteModeTxpITDM", 5))
    )


_SerialDteMode_Type.__name__ = "Integer32"
_SerialDteMode_Object = MibTableColumn
serialDteMode = _SerialDteMode_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 11),
    _SerialDteMode_Type()
)
serialDteMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteMode.setStatus("mandatory")


class _SerialDteDSR_Type(Integer32):
    """Custom type serialDteDSR based on Integer32"""
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
        *(("serialDteDSRForcedOff", 4),
          ("serialDteDSRForcedOn", 3),
          ("serialDteDSRInternal", 5),
          ("serialDteDSROther", 1),
          ("serialDteDSRTestOff", 2))
    )


_SerialDteDSR_Type.__name__ = "Integer32"
_SerialDteDSR_Object = MibTableColumn
serialDteDSR = _SerialDteDSR_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 12),
    _SerialDteDSR_Type()
)
serialDteDSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteDSR.setStatus("mandatory")


class _SerialDteDCD_Type(Integer32):
    """Custom type serialDteDCD based on Integer32"""
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
        *(("serialDteDCDFarRTS", 6),
          ("serialDteDCDForcedOff", 4),
          ("serialDteDCDForcedOn", 3),
          ("serialDteDCDIdleOff", 2),
          ("serialDteDCDInternal", 5),
          ("serialDteDCDOther", 1))
    )


_SerialDteDCD_Type.__name__ = "Integer32"
_SerialDteDCD_Object = MibTableColumn
serialDteDCD = _SerialDteDCD_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 13),
    _SerialDteDCD_Type()
)
serialDteDCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteDCD.setStatus("mandatory")


class _SerialDteRTS_Type(Integer32):
    """Custom type serialDteRTS based on Integer32"""
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
        *(("serialDteRTSExternal", 4),
          ("serialDteRTSForcedOn", 3),
          ("serialDteRTSNormal", 2),
          ("serialDteRTSOther", 1))
    )


_SerialDteRTS_Type.__name__ = "Integer32"
_SerialDteRTS_Object = MibTableColumn
serialDteRTS = _SerialDteRTS_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 14),
    _SerialDteRTS_Type()
)
serialDteRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteRTS.setStatus("mandatory")


class _SerialDteRTSDelay_Type(Integer32):
    """Custom type serialDteRTSDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serialDteRTSDelayLong", 3),
          ("serialDteRTSDelayNormal", 2),
          ("serialDteRTSDelayOther", 1))
    )


_SerialDteRTSDelay_Type.__name__ = "Integer32"
_SerialDteRTSDelay_Object = MibTableColumn
serialDteRTSDelay = _SerialDteRTSDelay_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 15),
    _SerialDteRTSDelay_Type()
)
serialDteRTSDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteRTSDelay.setStatus("mandatory")


class _SerialDteDTR_Type(Integer32):
    """Custom type serialDteDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serialDteDTRFalse", 2),
          ("serialDteDTROther", 1),
          ("serialDteDTRTrue", 3))
    )


_SerialDteDTR_Type.__name__ = "Integer32"
_SerialDteDTR_Object = MibTableColumn
serialDteDTR = _SerialDteDTR_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 16),
    _SerialDteDTR_Type()
)
serialDteDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteDTR.setStatus("mandatory")


class _SerialDteCTS_Type(Integer32):
    """Custom type serialDteCTS based on Integer32"""
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
        *(("serialDteCTSForceFalse", 3),
          ("serialDteCTSForceTrue", 2),
          ("serialDteCTSInternal", 4),
          ("serialDteCTSOther", 1))
    )


_SerialDteCTS_Type.__name__ = "Integer32"
_SerialDteCTS_Object = MibTableColumn
serialDteCTS = _SerialDteCTS_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 17),
    _SerialDteCTS_Type()
)
serialDteCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteCTS.setStatus("mandatory")


class _SerialDteV54_Type(Integer32):
    """Custom type serialDteV54 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serialDteV54Disable", 2),
          ("serialDteV54Enable", 3),
          ("serialDteV54Other", 1))
    )


_SerialDteV54_Type.__name__ = "Integer32"
_SerialDteV54_Object = MibTableColumn
serialDteV54 = _SerialDteV54_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 18),
    _SerialDteV54_Type()
)
serialDteV54.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteV54.setStatus("mandatory")


class _SerialDteLL_Type(Integer32):
    """Custom type serialDteLL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serialDteLLDisable", 2),
          ("serialDteLLEnable", 3),
          ("serialDteLLOther", 1))
    )


_SerialDteLL_Type.__name__ = "Integer32"
_SerialDteLL_Object = MibTableColumn
serialDteLL = _SerialDteLL_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 19),
    _SerialDteLL_Type()
)
serialDteLL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteLL.setStatus("mandatory")


class _SerialDteRL_Type(Integer32):
    """Custom type serialDteRL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serialDteRLDisable", 2),
          ("serialDteRLEnable", 3),
          ("serialDteRLOther", 1))
    )


_SerialDteRL_Type.__name__ = "Integer32"
_SerialDteRL_Object = MibTableColumn
serialDteRL = _SerialDteRL_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 20),
    _SerialDteRL_Type()
)
serialDteRL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteRL.setStatus("mandatory")
_SerialDteStartChannel_Type = Integer32
_SerialDteStartChannel_Object = MibTableColumn
serialDteStartChannel = _SerialDteStartChannel_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 21),
    _SerialDteStartChannel_Type()
)
serialDteStartChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteStartChannel.setStatus("mandatory")
_SerialDteNumberOfChannels_Type = Integer32
_SerialDteNumberOfChannels_Object = MibTableColumn
serialDteNumberOfChannels = _SerialDteNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 22),
    _SerialDteNumberOfChannels_Type()
)
serialDteNumberOfChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteNumberOfChannels.setStatus("mandatory")


class _SerialDteTxClock_Type(Integer32):
    """Custom type serialDteTxClock based on Integer32"""
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
        *(("serialDteTxClockExternal", 3),
          ("serialDteTxClockInternal", 2),
          ("serialDteTxClockOther", 1),
          ("serialDteTxClockOversample", 4))
    )


_SerialDteTxClock_Type.__name__ = "Integer32"
_SerialDteTxClock_Object = MibTableColumn
serialDteTxClock = _SerialDteTxClock_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 23),
    _SerialDteTxClock_Type()
)
serialDteTxClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteTxClock.setStatus("mandatory")


class _SerialDteBundle_Type(Integer32):
    """Custom type serialDteBundle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 3),
          ("contiguous", 2),
          ("other", 1))
    )


_SerialDteBundle_Type.__name__ = "Integer32"
_SerialDteBundle_Object = MibTableColumn
serialDteBundle = _SerialDteBundle_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 24),
    _SerialDteBundle_Type()
)
serialDteBundle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteBundle.setStatus("mandatory")


class _SerialDteChannelRate_Type(Integer32):
    """Custom type serialDteChannelRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nx56k", 2),
          ("nx64k", 3),
          ("other", 1))
    )


_SerialDteChannelRate_Type.__name__ = "Integer32"
_SerialDteChannelRate_Object = MibTableColumn
serialDteChannelRate = _SerialDteChannelRate_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 25),
    _SerialDteChannelRate_Type()
)
serialDteChannelRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteChannelRate.setStatus("mandatory")


class _SerialDteInvertClock_Type(Integer32):
    """Custom type serialDteInvertClock based on Integer32"""
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


_SerialDteInvertClock_Type.__name__ = "Integer32"
_SerialDteInvertClock_Object = MibTableColumn
serialDteInvertClock = _SerialDteInvertClock_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 1, 1, 26),
    _SerialDteInvertClock_Type()
)
serialDteInvertClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteInvertClock.setStatus("mandatory")
_SerialDteAlarmTable_Object = MibTable
serialDteAlarmTable = _SerialDteAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2)
)
if mibBuilder.loadTexts:
    serialDteAlarmTable.setStatus("optional")
_SerialDteAlarmTableEntry_Object = MibTableRow
serialDteAlarmTableEntry = _SerialDteAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1)
)
serialDteAlarmTableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "serialDteAlarmNearIndex"),
    (0, "INTERFACES-MIB", "serialDteAlarmFarIndex"),
    (0, "INTERFACES-MIB", "serialDteAlarmIndex"),
)
if mibBuilder.loadTexts:
    serialDteAlarmTableEntry.setStatus("mandatory")
_SerialDteAlarmNearIndex_Type = Integer32
_SerialDteAlarmNearIndex_Object = MibTableColumn
serialDteAlarmNearIndex = _SerialDteAlarmNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 1),
    _SerialDteAlarmNearIndex_Type()
)
serialDteAlarmNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteAlarmNearIndex.setStatus("mandatory")
_SerialDteAlarmFarIndex_Type = Integer32
_SerialDteAlarmFarIndex_Object = MibTableColumn
serialDteAlarmFarIndex = _SerialDteAlarmFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 2),
    _SerialDteAlarmFarIndex_Type()
)
serialDteAlarmFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteAlarmFarIndex.setStatus("mandatory")
_SerialDteAlarmIndex_Type = Integer32
_SerialDteAlarmIndex_Object = MibTableColumn
serialDteAlarmIndex = _SerialDteAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 3),
    _SerialDteAlarmIndex_Type()
)
serialDteAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteAlarmIndex.setStatus("mandatory")


class _SerialDteDTRAlarmControl_Type(Integer32):
    """Custom type serialDteDTRAlarmControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serialDteDTRAlarmDisable", 2),
          ("serialDteDTRAlarmEnable", 3),
          ("serialDteDTRAlarmOther", 1))
    )


_SerialDteDTRAlarmControl_Type.__name__ = "Integer32"
_SerialDteDTRAlarmControl_Object = MibTableColumn
serialDteDTRAlarmControl = _SerialDteDTRAlarmControl_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 4),
    _SerialDteDTRAlarmControl_Type()
)
serialDteDTRAlarmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteDTRAlarmControl.setStatus("mandatory")


class _SerialDteDTRAlarmStatus_Type(Integer32):
    """Custom type serialDteDTRAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serialDteDTRAlarmActive", 3),
          ("serialDteDTRAlarmNone", 2),
          ("serialDteDTRAlarmOther", 1))
    )


_SerialDteDTRAlarmStatus_Type.__name__ = "Integer32"
_SerialDteDTRAlarmStatus_Object = MibTableColumn
serialDteDTRAlarmStatus = _SerialDteDTRAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 5),
    _SerialDteDTRAlarmStatus_Type()
)
serialDteDTRAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteDTRAlarmStatus.setStatus("mandatory")


class _SerialDteStatusSummary_Type(DisplayString):
    """Custom type serialDteStatusSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialDteStatusSummary_Type.__name__ = "DisplayString"
_SerialDteStatusSummary_Object = MibTableColumn
serialDteStatusSummary = _SerialDteStatusSummary_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 6),
    _SerialDteStatusSummary_Type()
)
serialDteStatusSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteStatusSummary.setStatus("mandatory")


class _SerialDteAlarmSummary_Type(DisplayString):
    """Custom type serialDteAlarmSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialDteAlarmSummary_Type.__name__ = "DisplayString"
_SerialDteAlarmSummary_Object = MibTableColumn
serialDteAlarmSummary = _SerialDteAlarmSummary_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 7),
    _SerialDteAlarmSummary_Type()
)
serialDteAlarmSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteAlarmSummary.setStatus("mandatory")


class _SerialDteASCStatus_Type(Integer32):
    """Custom type serialDteASCStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serialDteStatusASC", 3),
          ("serialDteStatusASCOther", 1),
          ("serialDteStatusNoASC", 2))
    )


_SerialDteASCStatus_Type.__name__ = "Integer32"
_SerialDteASCStatus_Object = MibTableColumn
serialDteASCStatus = _SerialDteASCStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 8),
    _SerialDteASCStatus_Type()
)
serialDteASCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteASCStatus.setStatus("mandatory")
_SerialDteASCCount_Type = Integer32
_SerialDteASCCount_Object = MibTableColumn
serialDteASCCount = _SerialDteASCCount_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 9),
    _SerialDteASCCount_Type()
)
serialDteASCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteASCCount.setStatus("mandatory")
_SerialDteASCThreshold_Type = Integer32
_SerialDteASCThreshold_Object = MibTableColumn
serialDteASCThreshold = _SerialDteASCThreshold_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 10),
    _SerialDteASCThreshold_Type()
)
serialDteASCThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteASCThreshold.setStatus("mandatory")


class _SerialDteASCAlarm_Type(Integer32):
    """Custom type serialDteASCAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serialDteASCAlarmNone", 2),
          ("serialDteASCAlarmOther", 1),
          ("serialDteASCAlarmThresholdExceeded", 3))
    )


_SerialDteASCAlarm_Type.__name__ = "Integer32"
_SerialDteASCAlarm_Object = MibTableColumn
serialDteASCAlarm = _SerialDteASCAlarm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 11),
    _SerialDteASCAlarm_Type()
)
serialDteASCAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteASCAlarm.setStatus("mandatory")


class _SerialDteFDLStatus_Type(Integer32):
    """Custom type serialDteFDLStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serialDteStatusFDL", 3),
          ("serialDteStatusFDLOther", 1),
          ("serialDteStatusNoFDL", 2))
    )


_SerialDteFDLStatus_Type.__name__ = "Integer32"
_SerialDteFDLStatus_Object = MibTableColumn
serialDteFDLStatus = _SerialDteFDLStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 12),
    _SerialDteFDLStatus_Type()
)
serialDteFDLStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteFDLStatus.setStatus("mandatory")
_SerialDteFDLCount_Type = Integer32
_SerialDteFDLCount_Object = MibTableColumn
serialDteFDLCount = _SerialDteFDLCount_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 13),
    _SerialDteFDLCount_Type()
)
serialDteFDLCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteFDLCount.setStatus("mandatory")
_SerialDteFDLThreshold_Type = Integer32
_SerialDteFDLThreshold_Object = MibTableColumn
serialDteFDLThreshold = _SerialDteFDLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 14),
    _SerialDteFDLThreshold_Type()
)
serialDteFDLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteFDLThreshold.setStatus("mandatory")


class _SerialDteFDLAlarm_Type(Integer32):
    """Custom type serialDteFDLAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serialDteFDLAlarmNone", 2),
          ("serialDteFDLAlarmOther", 1),
          ("serialDteFDLAlarmThresholdExceeded", 3))
    )


_SerialDteFDLAlarm_Type.__name__ = "Integer32"
_SerialDteFDLAlarm_Object = MibTableColumn
serialDteFDLAlarm = _SerialDteFDLAlarm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 15),
    _SerialDteFDLAlarm_Type()
)
serialDteFDLAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteFDLAlarm.setStatus("mandatory")


class _SerialDteLOSStatus_Type(Integer32):
    """Custom type serialDteLOSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serialDteStatusLOS", 3),
          ("serialDteStatusLOSOther", 1),
          ("serialDteStatusNoLOS", 2))
    )


_SerialDteLOSStatus_Type.__name__ = "Integer32"
_SerialDteLOSStatus_Object = MibTableColumn
serialDteLOSStatus = _SerialDteLOSStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 16),
    _SerialDteLOSStatus_Type()
)
serialDteLOSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteLOSStatus.setStatus("mandatory")
_SerialDteLOSCount_Type = Integer32
_SerialDteLOSCount_Object = MibTableColumn
serialDteLOSCount = _SerialDteLOSCount_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 17),
    _SerialDteLOSCount_Type()
)
serialDteLOSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteLOSCount.setStatus("mandatory")
_SerialDteLOSThreshold_Type = Integer32
_SerialDteLOSThreshold_Object = MibTableColumn
serialDteLOSThreshold = _SerialDteLOSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 18),
    _SerialDteLOSThreshold_Type()
)
serialDteLOSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDteLOSThreshold.setStatus("mandatory")


class _SerialDteLOSAlarm_Type(Integer32):
    """Custom type serialDteLOSAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serialDteLOSAlarmNone", 2),
          ("serialDteLOSAlarmOther", 1),
          ("serialDteLOSAlarmThresholdExceeded", 3))
    )


_SerialDteLOSAlarm_Type.__name__ = "Integer32"
_SerialDteLOSAlarm_Object = MibTableColumn
serialDteLOSAlarm = _SerialDteLOSAlarm_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 5, 2, 1, 19),
    _SerialDteLOSAlarm_Type()
)
serialDteLOSAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDteLOSAlarm.setStatus("mandatory")
_AnalogDte_ObjectIdentity = ObjectIdentity
analogDte = _AnalogDte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 8, 6)
)
_AnalogDteTable_Object = MibTable
analogDteTable = _AnalogDteTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 6, 1)
)
if mibBuilder.loadTexts:
    analogDteTable.setStatus("optional")
_AnalogDteTableEntry_Object = MibTableRow
analogDteTableEntry = _AnalogDteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 6, 1, 1)
)
analogDteTableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "analogDteNearIndex"),
    (0, "INTERFACES-MIB", "analogDteFarIndex"),
    (0, "INTERFACES-MIB", "analogDteIndex"),
)
if mibBuilder.loadTexts:
    analogDteTableEntry.setStatus("mandatory")
_AnalogDteNearIndex_Type = Integer32
_AnalogDteNearIndex_Object = MibTableColumn
analogDteNearIndex = _AnalogDteNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 6, 1, 1, 1),
    _AnalogDteNearIndex_Type()
)
analogDteNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogDteNearIndex.setStatus("mandatory")
_AnalogDteFarIndex_Type = Integer32
_AnalogDteFarIndex_Object = MibTableColumn
analogDteFarIndex = _AnalogDteFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 6, 1, 1, 2),
    _AnalogDteFarIndex_Type()
)
analogDteFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogDteFarIndex.setStatus("mandatory")
_AnalogDteIndex_Type = Integer32
_AnalogDteIndex_Object = MibTableColumn
analogDteIndex = _AnalogDteIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 6, 1, 1, 3),
    _AnalogDteIndex_Type()
)
analogDteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogDteIndex.setStatus("mandatory")


class _AnalogDteDescription_Type(DisplayString):
    """Custom type analogDteDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AnalogDteDescription_Type.__name__ = "DisplayString"
_AnalogDteDescription_Object = MibTableColumn
analogDteDescription = _AnalogDteDescription_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 6, 1, 1, 4),
    _AnalogDteDescription_Type()
)
analogDteDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogDteDescription.setStatus("mandatory")


class _AnalogDteCardType_Type(Integer32):
    """Custom type analogDteCardType based on Integer32"""
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
        *(("analogDteCardType4WEM", 4),
          ("analogDteCardTypeFXO", 3),
          ("analogDteCardTypeFXS", 2),
          ("analogDteCardTypeOther", 1))
    )


_AnalogDteCardType_Type.__name__ = "Integer32"
_AnalogDteCardType_Object = MibTableColumn
analogDteCardType = _AnalogDteCardType_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 6, 1, 1, 5),
    _AnalogDteCardType_Type()
)
analogDteCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogDteCardType.setStatus("mandatory")


class _AnalogDteMode_Type(Integer32):
    """Custom type analogDteMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analogDteModeActive", 3),
          ("analogDteModeOther", 1),
          ("analogDteModeSpare", 2))
    )


_AnalogDteMode_Type.__name__ = "Integer32"
_AnalogDteMode_Object = MibTableColumn
analogDteMode = _AnalogDteMode_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 6, 1, 1, 6),
    _AnalogDteMode_Type()
)
analogDteMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogDteMode.setStatus("mandatory")


class _AnalogDteState_Type(Integer32):
    """Custom type analogDteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analogDteStateBusy", 3),
          ("analogDteStateIdle", 2),
          ("analogDteStateOther", 1))
    )


_AnalogDteState_Type.__name__ = "Integer32"
_AnalogDteState_Object = MibTableColumn
analogDteState = _AnalogDteState_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 6, 1, 1, 7),
    _AnalogDteState_Type()
)
analogDteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogDteState.setStatus("mandatory")


class _AnalogDteElementID_Type(DisplayString):
    """Custom type analogDteElementID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AnalogDteElementID_Type.__name__ = "DisplayString"
_AnalogDteElementID_Object = MibTableColumn
analogDteElementID = _AnalogDteElementID_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 6, 1, 1, 8),
    _AnalogDteElementID_Type()
)
analogDteElementID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogDteElementID.setStatus("mandatory")


class _AnalogDteSignalling_Type(Integer32):
    """Custom type analogDteSignalling based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("analogDteSignalling4WEMTO", 29),
          ("analogDteSignalling4WEMTYPE1", 24),
          ("analogDteSignalling4WEMTYPE2", 25),
          ("analogDteSignalling4WEMTYPE3", 26),
          ("analogDteSignalling4WEMTYPE4", 27),
          ("analogDteSignalling4WEMTYPE5", 28),
          ("analogDteSignallingDIDDNIS", 11),
          ("analogDteSignallingDNISDGS", 17),
          ("analogDteSignallingDNISDLS", 13),
          ("analogDteSignallingDNISDRGS", 19),
          ("analogDteSignallingDNISDRLS", 15),
          ("analogDteSignallingDNISWGS", 16),
          ("analogDteSignallingDNISWLS", 12),
          ("analogDteSignallingDNISWRGS", 18),
          ("analogDteSignallingDNISWRLS", 14),
          ("analogDteSignallingFXOGS", 21),
          ("analogDteSignallingFXOLS", 20),
          ("analogDteSignallingFXOUVG", 22),
          ("analogDteSignallingFXOUVGR", 23),
          ("analogDteSignallingFXSGS", 3),
          ("analogDteSignallingFXSLS", 2),
          ("analogDteSignallingMEGGS", 6),
          ("analogDteSignallingMEGLS", 5),
          ("analogDteSignallingMEGRGS", 8),
          ("analogDteSignallingMEGRLS", 7),
          ("analogDteSignallingOther", 1),
          ("analogDteSignallingPLAR", 9),
          ("analogDteSignallingSLC96", 10),
          ("analogDteSignallingUVG", 4))
    )


_AnalogDteSignalling_Type.__name__ = "Integer32"
_AnalogDteSignalling_Object = MibTableColumn
analogDteSignalling = _AnalogDteSignalling_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 6, 1, 1, 9),
    _AnalogDteSignalling_Type()
)
analogDteSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogDteSignalling.setStatus("mandatory")


class _AnalogDteDNISDelay_Type(Integer32):
    """Custom type analogDteDNISDelay based on Integer32"""
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
        *(("analogDteDNISDelay1Second", 2),
          ("analogDteDNISDelay2Seconds", 3),
          ("analogDteDNISDelay3Seconds", 4),
          ("analogDteDNISDelay4Seconds", 5),
          ("analogDteDNISDelay5Seconds", 6),
          ("analogDteDNISDelayOther", 1))
    )


_AnalogDteDNISDelay_Type.__name__ = "Integer32"
_AnalogDteDNISDelay_Object = MibTableColumn
analogDteDNISDelay = _AnalogDteDNISDelay_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 6, 1, 1, 10),
    _AnalogDteDNISDelay_Type()
)
analogDteDNISDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogDteDNISDelay.setStatus("mandatory")


class _AnalogDteTxGain_Type(Integer32):
    """Custom type analogDteTxGain based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("analogDteTxGain0DB", 5),
          ("analogDteTxGain1DB", 4),
          ("analogDteTxGain2DB", 3),
          ("analogDteTxGain3DB", 2),
          ("analogDteTxGainOther", 1),
          ("analogDteTxGainm10DB", 15),
          ("analogDteTxGainm1DB", 6),
          ("analogDteTxGainm2DB", 7),
          ("analogDteTxGainm3DB", 8),
          ("analogDteTxGainm4DB", 9),
          ("analogDteTxGainm5DB", 10),
          ("analogDteTxGainm6DB", 11),
          ("analogDteTxGainm7DB", 12),
          ("analogDteTxGainm8DB", 13),
          ("analogDteTxGainm9DB", 14))
    )


_AnalogDteTxGain_Type.__name__ = "Integer32"
_AnalogDteTxGain_Object = MibTableColumn
analogDteTxGain = _AnalogDteTxGain_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 6, 1, 1, 11),
    _AnalogDteTxGain_Type()
)
analogDteTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogDteTxGain.setStatus("mandatory")


class _AnalogDteRxGain_Type(Integer32):
    """Custom type analogDteRxGain based on Integer32"""
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
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("analogDteRxGain0DB", 4),
          ("analogDteRxGain1DB", 3),
          ("analogDteRxGain2DB", 2),
          ("analogDteRxGainOther", 1),
          ("analogDteRxGainm10DB", 14),
          ("analogDteRxGainm11DB", 15),
          ("analogDteRxGainm12DB", 16),
          ("analogDteRxGainm13DB", 17),
          ("analogDteRxGainm14DB", 18),
          ("analogDteRxGainm15DB", 19),
          ("analogDteRxGainm16DB", 20),
          ("analogDteRxGainm1DB", 5),
          ("analogDteRxGainm2DB", 6),
          ("analogDteRxGainm3DB", 7),
          ("analogDteRxGainm4DB", 8),
          ("analogDteRxGainm5DB", 9),
          ("analogDteRxGainm6DB", 10),
          ("analogDteRxGainm7DB", 11),
          ("analogDteRxGainm8DB", 12),
          ("analogDteRxGainm9DB", 13))
    )


_AnalogDteRxGain_Type.__name__ = "Integer32"
_AnalogDteRxGain_Object = MibTableColumn
analogDteRxGain = _AnalogDteRxGain_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 6, 1, 1, 12),
    _AnalogDteRxGain_Type()
)
analogDteRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogDteRxGain.setStatus("mandatory")
_Connection_ObjectIdentity = ObjectIdentity
connection = _Connection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 8, 7)
)
_ConnectionTable_Object = MibTable
connectionTable = _ConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 7, 1)
)
if mibBuilder.loadTexts:
    connectionTable.setStatus("optional")
_ConnectionTableEntry_Object = MibTableRow
connectionTableEntry = _ConnectionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 7, 1, 1)
)
connectionTableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "connectionNearIndex"),
    (0, "INTERFACES-MIB", "connectionFarIndex"),
    (0, "INTERFACES-MIB", "connectionTableIndex"),
)
if mibBuilder.loadTexts:
    connectionTableEntry.setStatus("mandatory")
_ConnectionNearIndex_Type = Integer32
_ConnectionNearIndex_Object = MibTableColumn
connectionNearIndex = _ConnectionNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 7, 1, 1, 1),
    _ConnectionNearIndex_Type()
)
connectionNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionNearIndex.setStatus("mandatory")
_ConnectionFarIndex_Type = Integer32
_ConnectionFarIndex_Object = MibTableColumn
connectionFarIndex = _ConnectionFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 7, 1, 1, 2),
    _ConnectionFarIndex_Type()
)
connectionFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionFarIndex.setStatus("mandatory")
_ConnectionTableIndex_Type = Integer32
_ConnectionTableIndex_Object = MibTableColumn
connectionTableIndex = _ConnectionTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 7, 1, 1, 3),
    _ConnectionTableIndex_Type()
)
connectionTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionTableIndex.setStatus("mandatory")


class _ConnectionTableDescription_Type(DisplayString):
    """Custom type connectionTableDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_ConnectionTableDescription_Type.__name__ = "DisplayString"
_ConnectionTableDescription_Object = MibTableColumn
connectionTableDescription = _ConnectionTableDescription_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 7, 1, 1, 4),
    _ConnectionTableDescription_Type()
)
connectionTableDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionTableDescription.setStatus("mandatory")
_ConnectionChannelTable_Object = MibTable
connectionChannelTable = _ConnectionChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 7, 2)
)
if mibBuilder.loadTexts:
    connectionChannelTable.setStatus("mandatory")
_ConnectionChannelEntry_Object = MibTableRow
connectionChannelEntry = _ConnectionChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 7, 2, 1)
)
connectionChannelEntry.setIndexNames(
    (0, "INTERFACES-MIB", "connectionChannelNearIndex"),
    (0, "INTERFACES-MIB", "connectionChannelFarIndex"),
    (0, "INTERFACES-MIB", "connectionChannelLineIndex"),
    (0, "INTERFACES-MIB", "connectionChannelIndex"),
)
if mibBuilder.loadTexts:
    connectionChannelEntry.setStatus("mandatory")
_ConnectionChannelNearIndex_Type = Integer32
_ConnectionChannelNearIndex_Object = MibTableColumn
connectionChannelNearIndex = _ConnectionChannelNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 7, 2, 1, 1),
    _ConnectionChannelNearIndex_Type()
)
connectionChannelNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionChannelNearIndex.setStatus("mandatory")
_ConnectionChannelFarIndex_Type = Integer32
_ConnectionChannelFarIndex_Object = MibTableColumn
connectionChannelFarIndex = _ConnectionChannelFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 7, 2, 1, 2),
    _ConnectionChannelFarIndex_Type()
)
connectionChannelFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionChannelFarIndex.setStatus("mandatory")
_ConnectionChannelLineIndex_Type = Integer32
_ConnectionChannelLineIndex_Object = MibTableColumn
connectionChannelLineIndex = _ConnectionChannelLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 7, 2, 1, 3),
    _ConnectionChannelLineIndex_Type()
)
connectionChannelLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionChannelLineIndex.setStatus("mandatory")
_ConnectionChannelIndex_Type = Integer32
_ConnectionChannelIndex_Object = MibTableColumn
connectionChannelIndex = _ConnectionChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 7, 2, 1, 4),
    _ConnectionChannelIndex_Type()
)
connectionChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionChannelIndex.setStatus("mandatory")


class _ChannelInterfaceAssignment_Type(Integer32):
    """Custom type channelInterfaceAssignment based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106)
        )
    )
    namedValues = NamedValues(
        *(("dTE", 3),
          ("other", 1),
          ("port1", 5),
          ("port10", 14),
          ("port11", 15),
          ("port12", 16),
          ("port13", 17),
          ("port14", 18),
          ("port15", 19),
          ("port16", 20),
          ("port17", 21),
          ("port18", 22),
          ("port19", 23),
          ("port2", 6),
          ("port20", 24),
          ("port21", 25),
          ("port22", 26),
          ("port23", 27),
          ("port24", 28),
          ("port25", 29),
          ("port26", 30),
          ("port27", 31),
          ("port28", 32),
          ("port29", 33),
          ("port3", 7),
          ("port30", 34),
          ("port31", 35),
          ("port32", 36),
          ("port4", 8),
          ("port5", 9),
          ("port6", 10),
          ("port7", 11),
          ("port8", 12),
          ("port9", 13),
          ("remComm", 4),
          ("slot2Dsu1PortA", 47),
          ("slot2Dsu1PortB", 48),
          ("slot2Dsu2PortA", 49),
          ("slot2Dsu2PortB", 50),
          ("slot2Dsu3PortA", 51),
          ("slot2Dsu3PortB", 52),
          ("slot2Dsu4PortA", 53),
          ("slot2Dsu4PortB", 54),
          ("slot2Dsu5PortA", 55),
          ("slot2Dsu5PortB", 56),
          ("slot2Dsu6PortA", 57),
          ("slot2Dsu6PortB", 58),
          ("slot2PortA", 37),
          ("slot2PortB", 38),
          ("slot3Dsu1PortA", 59),
          ("slot3Dsu1PortB", 60),
          ("slot3Dsu2PortA", 61),
          ("slot3Dsu2PortB", 62),
          ("slot3Dsu3PortA", 63),
          ("slot3Dsu3PortB", 64),
          ("slot3Dsu4PortA", 65),
          ("slot3Dsu4PortB", 66),
          ("slot3Dsu5PortA", 67),
          ("slot3Dsu5PortB", 68),
          ("slot3Dsu6PortA", 69),
          ("slot3Dsu6PortB", 70),
          ("slot3PortA", 39),
          ("slot3PortB", 40),
          ("slot4Dsu1PortA", 71),
          ("slot4Dsu1PortB", 72),
          ("slot4Dsu2PortA", 73),
          ("slot4Dsu2PortB", 74),
          ("slot4Dsu3PortA", 75),
          ("slot4Dsu3PortB", 76),
          ("slot4Dsu4PortA", 77),
          ("slot4Dsu4PortB", 78),
          ("slot4Dsu5PortA", 79),
          ("slot4Dsu5PortB", 80),
          ("slot4Dsu6PortA", 81),
          ("slot4Dsu6PortB", 82),
          ("slot4PortA", 41),
          ("slot4PortB", 42),
          ("slot5Dsu1PortA", 83),
          ("slot5Dsu1PortB", 84),
          ("slot5Dsu2PortA", 85),
          ("slot5Dsu2PortB", 86),
          ("slot5Dsu3PortA", 87),
          ("slot5Dsu3PortB", 88),
          ("slot5Dsu4PortA", 89),
          ("slot5Dsu4PortB", 90),
          ("slot5Dsu5PortA", 91),
          ("slot5Dsu5PortB", 92),
          ("slot5Dsu6PortA", 93),
          ("slot5Dsu6PortB", 94),
          ("slot5PortA", 43),
          ("slot5PortB", 44),
          ("slot6Dsu1PortA", 95),
          ("slot6Dsu1PortB", 96),
          ("slot6Dsu2PortA", 97),
          ("slot6Dsu2PortB", 98),
          ("slot6Dsu3PortA", 99),
          ("slot6Dsu3PortB", 100),
          ("slot6Dsu4PortA", 101),
          ("slot6Dsu4PortB", 102),
          ("slot6Dsu5PortA", 103),
          ("slot6Dsu5PortB", 104),
          ("slot6Dsu6PortA", 105),
          ("slot6Dsu6PortB", 106),
          ("slot6PortA", 45),
          ("slot6PortB", 46),
          ("unassigned", 2))
    )


_ChannelInterfaceAssignment_Type.__name__ = "Integer32"
_ChannelInterfaceAssignment_Object = MibTableColumn
channelInterfaceAssignment = _ChannelInterfaceAssignment_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 7, 2, 1, 5),
    _ChannelInterfaceAssignment_Type()
)
channelInterfaceAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelInterfaceAssignment.setStatus("mandatory")


class _ChannelInterfaceDescription_Type(DisplayString):
    """Custom type channelInterfaceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ChannelInterfaceDescription_Type.__name__ = "DisplayString"
_ChannelInterfaceDescription_Object = MibTableColumn
channelInterfaceDescription = _ChannelInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 7, 2, 1, 6),
    _ChannelInterfaceDescription_Type()
)
channelInterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInterfaceDescription.setStatus("mandatory")
_ChannelInterfaceChannel_Type = Integer32
_ChannelInterfaceChannel_Object = MibTableColumn
channelInterfaceChannel = _ChannelInterfaceChannel_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 7, 2, 1, 7),
    _ChannelInterfaceChannel_Type()
)
channelInterfaceChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelInterfaceChannel.setStatus("mandatory")


class _ChannelSignalling_Type(Integer32):
    """Custom type channelSignalling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearChannel", 2),
          ("other", 1),
          ("robbedBit", 3))
    )


_ChannelSignalling_Type.__name__ = "Integer32"
_ChannelSignalling_Object = MibTableColumn
channelSignalling = _ChannelSignalling_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 7, 2, 1, 8),
    _ChannelSignalling_Type()
)
channelSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelSignalling.setStatus("mandatory")
_Maintenance_ObjectIdentity = ObjectIdentity
maintenance = _Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 8, 8)
)
_BertTable_Object = MibTable
bertTable = _BertTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 1)
)
if mibBuilder.loadTexts:
    bertTable.setStatus("optional")
_BertTableEntry_Object = MibTableRow
bertTableEntry = _BertTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 1, 1)
)
bertTableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "bertNearIndex"),
    (0, "INTERFACES-MIB", "bertFarIndex"),
    (0, "INTERFACES-MIB", "bertIndex"),
)
if mibBuilder.loadTexts:
    bertTableEntry.setStatus("mandatory")
_BertNearIndex_Type = Integer32
_BertNearIndex_Object = MibTableColumn
bertNearIndex = _BertNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 1, 1, 1),
    _BertNearIndex_Type()
)
bertNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertNearIndex.setStatus("mandatory")
_BertFarIndex_Type = Integer32
_BertFarIndex_Object = MibTableColumn
bertFarIndex = _BertFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 1, 1, 2),
    _BertFarIndex_Type()
)
bertFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertFarIndex.setStatus("mandatory")
_BertIndex_Type = Integer32
_BertIndex_Object = MibTableColumn
bertIndex = _BertIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 1, 1, 3),
    _BertIndex_Type()
)
bertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertIndex.setStatus("mandatory")


class _BertPattern_Type(Integer32):
    """Custom type bertPattern based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("bertPattern1in8", 9),
          ("bertPattern2047", 5),
          ("bertPattern215", 6),
          ("bertPattern220", 7),
          ("bertPattern223", 8),
          ("bertPattern3in24", 10),
          ("bertPattern511", 4),
          ("bertPattern63", 3),
          ("bertPatternALT", 11),
          ("bertPatternCLEAR", 12),
          ("bertPatternOther", 1),
          ("bertPatternQRSS", 2))
    )


_BertPattern_Type.__name__ = "Integer32"
_BertPattern_Object = MibTableColumn
bertPattern = _BertPattern_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 1, 1, 4),
    _BertPattern_Type()
)
bertPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertPattern.setStatus("mandatory")


class _BertLength_Type(Integer32):
    """Custom type bertLength based on Integer32"""
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
        *(("bertLength15minutes", 2),
          ("bertLength24hours", 5),
          ("bertLength30minutes", 3),
          ("bertLength60minutes", 4),
          ("bertLengthContinuous", 6),
          ("bertLengthOther", 1))
    )


_BertLength_Type.__name__ = "Integer32"
_BertLength_Object = MibTableColumn
bertLength = _BertLength_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 1, 1, 5),
    _BertLength_Type()
)
bertLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertLength.setStatus("mandatory")


class _BertPatternSync_Type(Integer32):
    """Custom type bertPatternSync based on Integer32"""
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
        *(("bertPatternSyncInsync", 4),
          ("bertPatternSyncNoSync", 3),
          ("bertPatternSyncNoTest", 2),
          ("bertPatternSyncOther", 1))
    )


_BertPatternSync_Type.__name__ = "Integer32"
_BertPatternSync_Object = MibTableColumn
bertPatternSync = _BertPatternSync_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 1, 1, 6),
    _BertPatternSync_Type()
)
bertPatternSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertPatternSync.setStatus("mandatory")
_BertElapsedTime_Type = Integer32
_BertElapsedTime_Object = MibTableColumn
bertElapsedTime = _BertElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 1, 1, 7),
    _BertElapsedTime_Type()
)
bertElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertElapsedTime.setStatus("mandatory")
_BertBitErrors_Type = Integer32
_BertBitErrors_Object = MibTableColumn
bertBitErrors = _BertBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 1, 1, 8),
    _BertBitErrors_Type()
)
bertBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertBitErrors.setStatus("mandatory")
_BertErroredSeconds_Type = Integer32
_BertErroredSeconds_Object = MibTableColumn
bertErroredSeconds = _BertErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 1, 1, 9),
    _BertErroredSeconds_Type()
)
bertErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertErroredSeconds.setStatus("mandatory")
_BertPercentEFS_Type = Integer32
_BertPercentEFS_Object = MibTableColumn
bertPercentEFS = _BertPercentEFS_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 1, 1, 10),
    _BertPercentEFS_Type()
)
bertPercentEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertPercentEFS.setStatus("mandatory")


class _BertCommand_Type(Integer32):
    """Custom type bertCommand based on Integer32"""
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
        *(("bertCommandInjectError", 5),
          ("bertCommandOther", 1),
          ("bertCommandResetErrors", 4),
          ("bertCommandStart", 2),
          ("bertCommandStop", 3))
    )


_BertCommand_Type.__name__ = "Integer32"
_BertCommand_Object = MibTableColumn
bertCommand = _BertCommand_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 1, 1, 11),
    _BertCommand_Type()
)
bertCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertCommand.setStatus("mandatory")
_BertInterfaceTable_Object = MibTable
bertInterfaceTable = _BertInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 2)
)
if mibBuilder.loadTexts:
    bertInterfaceTable.setStatus("mandatory")
_BertInterfaceTableEntry_Object = MibTableRow
bertInterfaceTableEntry = _BertInterfaceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 2, 1)
)
bertInterfaceTableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "bertInterfaceNearIndex"),
    (0, "INTERFACES-MIB", "bertInterfaceFarIndex"),
    (0, "INTERFACES-MIB", "bertChipIndex"),
    (0, "INTERFACES-MIB", "bertInterfaceIndex"),
)
if mibBuilder.loadTexts:
    bertInterfaceTableEntry.setStatus("mandatory")
_BertInterfaceNearIndex_Type = Integer32
_BertInterfaceNearIndex_Object = MibTableColumn
bertInterfaceNearIndex = _BertInterfaceNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 2, 1, 1),
    _BertInterfaceNearIndex_Type()
)
bertInterfaceNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertInterfaceNearIndex.setStatus("mandatory")
_BertInterfaceFarIndex_Type = Integer32
_BertInterfaceFarIndex_Object = MibTableColumn
bertInterfaceFarIndex = _BertInterfaceFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 2, 1, 2),
    _BertInterfaceFarIndex_Type()
)
bertInterfaceFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertInterfaceFarIndex.setStatus("mandatory")
_BertChipIndex_Type = Integer32
_BertChipIndex_Object = MibTableColumn
bertChipIndex = _BertChipIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 2, 1, 3),
    _BertChipIndex_Type()
)
bertChipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertChipIndex.setStatus("mandatory")
_BertInterfaceIndex_Type = Integer32
_BertInterfaceIndex_Object = MibTableColumn
bertInterfaceIndex = _BertInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 2, 1, 4),
    _BertInterfaceIndex_Type()
)
bertInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertInterfaceIndex.setStatus("mandatory")


class _BertInterfaceSetting_Type(Integer32):
    """Custom type bertInterfaceSetting based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("bertInterfaceSettingChannel1", 3),
          ("bertInterfaceSettingChannel10", 12),
          ("bertInterfaceSettingChannel11", 13),
          ("bertInterfaceSettingChannel12", 14),
          ("bertInterfaceSettingChannel13", 15),
          ("bertInterfaceSettingChannel14", 16),
          ("bertInterfaceSettingChannel15", 17),
          ("bertInterfaceSettingChannel16", 18),
          ("bertInterfaceSettingChannel17", 19),
          ("bertInterfaceSettingChannel18", 20),
          ("bertInterfaceSettingChannel19", 21),
          ("bertInterfaceSettingChannel2", 4),
          ("bertInterfaceSettingChannel20", 22),
          ("bertInterfaceSettingChannel21", 23),
          ("bertInterfaceSettingChannel22", 24),
          ("bertInterfaceSettingChannel23", 25),
          ("bertInterfaceSettingChannel24", 26),
          ("bertInterfaceSettingChannel25", 27),
          ("bertInterfaceSettingChannel26", 28),
          ("bertInterfaceSettingChannel27", 29),
          ("bertInterfaceSettingChannel28", 30),
          ("bertInterfaceSettingChannel29", 31),
          ("bertInterfaceSettingChannel3", 5),
          ("bertInterfaceSettingChannel30", 32),
          ("bertInterfaceSettingChannel31", 33),
          ("bertInterfaceSettingChannel32", 34),
          ("bertInterfaceSettingChannel4", 6),
          ("bertInterfaceSettingChannel5", 7),
          ("bertInterfaceSettingChannel6", 8),
          ("bertInterfaceSettingChannel7", 9),
          ("bertInterfaceSettingChannel8", 10),
          ("bertInterfaceSettingChannel9", 11),
          ("bertInterfaceSettingDTE", 36),
          ("bertInterfaceSettingIdle", 2),
          ("bertInterfaceSettingNet", 35),
          ("bertInterfaceSettingNotEnabled", 37),
          ("bertInterfaceSettingOther", 1))
    )


_BertInterfaceSetting_Type.__name__ = "Integer32"
_BertInterfaceSetting_Object = MibTableColumn
bertInterfaceSetting = _BertInterfaceSetting_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 2, 1, 5),
    _BertInterfaceSetting_Type()
)
bertInterfaceSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertInterfaceSetting.setStatus("mandatory")
_TestTable_Object = MibTable
testTable = _TestTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 3)
)
if mibBuilder.loadTexts:
    testTable.setStatus("optional")
_TestTableEntry_Object = MibTableRow
testTableEntry = _TestTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 3, 1)
)
testTableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "testNearIndex"),
    (0, "INTERFACES-MIB", "testFarIndex"),
    (0, "INTERFACES-MIB", "testTableIndex"),
)
if mibBuilder.loadTexts:
    testTableEntry.setStatus("mandatory")
_TestNearIndex_Type = Integer32
_TestNearIndex_Object = MibTableColumn
testNearIndex = _TestNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 3, 1, 1),
    _TestNearIndex_Type()
)
testNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testNearIndex.setStatus("mandatory")
_TestFarIndex_Type = Integer32
_TestFarIndex_Object = MibTableColumn
testFarIndex = _TestFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 3, 1, 2),
    _TestFarIndex_Type()
)
testFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testFarIndex.setStatus("mandatory")
_TestTableIndex_Type = Integer32
_TestTableIndex_Object = MibTableColumn
testTableIndex = _TestTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 3, 1, 3),
    _TestTableIndex_Type()
)
testTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testTableIndex.setStatus("mandatory")


class _TestType_Type(Integer32):
    """Custom type testType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("testTypeFarLLB", 7),
          ("testTypeFarMLB", 8),
          ("testTypeFarPLB", 6),
          ("testTypeFarV54Loop", 11),
          ("testTypeLLB", 4),
          ("testTypeNoTest", 2),
          ("testTypeOther", 1),
          ("testTypePLB", 3),
          ("testTypePortLoop", 9),
          ("testTypeV54Loop", 10),
          ("testtypeMLB", 5))
    )


_TestType_Type.__name__ = "Integer32"
_TestType_Object = MibTableColumn
testType = _TestType_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 3, 1, 4),
    _TestType_Type()
)
testType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    testType.setStatus("mandatory")


class _TestLoopDirection_Type(Integer32):
    """Custom type testLoopDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("testLoopBidirectional", 3),
          ("testLoopOther", 1),
          ("testLoopUnidirectional", 2))
    )


_TestLoopDirection_Type.__name__ = "Integer32"
_TestLoopDirection_Object = MibTableColumn
testLoopDirection = _TestLoopDirection_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 3, 1, 5),
    _TestLoopDirection_Type()
)
testLoopDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    testLoopDirection.setStatus("mandatory")


class _TestFarLLBFraming_Type(Integer32):
    """Custom type testFarLLBFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("testFarLLBFramingFramed", 3),
          ("testFarLLBFramingOther", 1),
          ("testFarLLBFramingUnframed", 2))
    )


_TestFarLLBFraming_Type.__name__ = "Integer32"
_TestFarLLBFraming_Object = MibTableColumn
testFarLLBFraming = _TestFarLLBFraming_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 8, 3, 1, 6),
    _TestFarLLBFraming_Type()
)
testFarLLBFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    testFarLLBFraming.setStatus("mandatory")
_Performance_ObjectIdentity = ObjectIdentity
performance = _Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 8, 9)
)
_Performance24Table_Object = MibTable
performance24Table = _Performance24Table_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1)
)
if mibBuilder.loadTexts:
    performance24Table.setStatus("optional")
_Performance24TableEntry_Object = MibTableRow
performance24TableEntry = _Performance24TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1, 1)
)
performance24TableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "performance24NearIndex"),
    (0, "INTERFACES-MIB", "performance24FarIndex"),
    (0, "INTERFACES-MIB", "performance24InterfaceIndex"),
    (0, "INTERFACES-MIB", "performance24Index"),
)
if mibBuilder.loadTexts:
    performance24TableEntry.setStatus("mandatory")
_Performance24NearIndex_Type = Integer32
_Performance24NearIndex_Object = MibTableColumn
performance24NearIndex = _Performance24NearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1, 1, 1),
    _Performance24NearIndex_Type()
)
performance24NearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance24NearIndex.setStatus("mandatory")
_Performance24FarIndex_Type = Integer32
_Performance24FarIndex_Object = MibTableColumn
performance24FarIndex = _Performance24FarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1, 1, 2),
    _Performance24FarIndex_Type()
)
performance24FarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance24FarIndex.setStatus("mandatory")
_Performance24InterfaceIndex_Type = Integer32
_Performance24InterfaceIndex_Object = MibTableColumn
performance24InterfaceIndex = _Performance24InterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1, 1, 3),
    _Performance24InterfaceIndex_Type()
)
performance24InterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance24InterfaceIndex.setStatus("mandatory")


class _Performance24Index_Type(Integer32):
    """Custom type performance24Index based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98)
        )
    )
    namedValues = NamedValues(
        *(("performance24Current", 2),
          ("performance24Summary", 1),
          ("performance24period1", 3),
          ("performance24period10", 12),
          ("performance24period11", 13),
          ("performance24period12", 14),
          ("performance24period13", 15),
          ("performance24period14", 16),
          ("performance24period15", 17),
          ("performance24period16", 18),
          ("performance24period17", 19),
          ("performance24period18", 20),
          ("performance24period19", 21),
          ("performance24period2", 4),
          ("performance24period20", 22),
          ("performance24period21", 23),
          ("performance24period22", 24),
          ("performance24period23", 25),
          ("performance24period24", 26),
          ("performance24period25", 27),
          ("performance24period26", 28),
          ("performance24period27", 29),
          ("performance24period28", 30),
          ("performance24period29", 31),
          ("performance24period3", 5),
          ("performance24period30", 32),
          ("performance24period31", 33),
          ("performance24period32", 34),
          ("performance24period33", 35),
          ("performance24period34", 36),
          ("performance24period35", 37),
          ("performance24period36", 38),
          ("performance24period37", 39),
          ("performance24period38", 40),
          ("performance24period39", 41),
          ("performance24period4", 6),
          ("performance24period40", 42),
          ("performance24period41", 43),
          ("performance24period42", 44),
          ("performance24period43", 45),
          ("performance24period44", 46),
          ("performance24period45", 47),
          ("performance24period46", 48),
          ("performance24period47", 49),
          ("performance24period48", 50),
          ("performance24period49", 51),
          ("performance24period5", 7),
          ("performance24period50", 52),
          ("performance24period51", 53),
          ("performance24period52", 54),
          ("performance24period53", 55),
          ("performance24period54", 56),
          ("performance24period55", 57),
          ("performance24period56", 58),
          ("performance24period57", 59),
          ("performance24period58", 60),
          ("performance24period59", 61),
          ("performance24period6", 8),
          ("performance24period60", 62),
          ("performance24period61", 63),
          ("performance24period62", 64),
          ("performance24period63", 65),
          ("performance24period64", 66),
          ("performance24period65", 67),
          ("performance24period66", 68),
          ("performance24period67", 69),
          ("performance24period68", 70),
          ("performance24period69", 71),
          ("performance24period7", 9),
          ("performance24period70", 72),
          ("performance24period71", 73),
          ("performance24period72", 74),
          ("performance24period73", 75),
          ("performance24period74", 76),
          ("performance24period75", 77),
          ("performance24period76", 78),
          ("performance24period77", 79),
          ("performance24period78", 80),
          ("performance24period79", 81),
          ("performance24period8", 10),
          ("performance24period80", 82),
          ("performance24period81", 83),
          ("performance24period82", 84),
          ("performance24period83", 85),
          ("performance24period84", 86),
          ("performance24period85", 87),
          ("performance24period86", 88),
          ("performance24period87", 89),
          ("performance24period88", 90),
          ("performance24period89", 91),
          ("performance24period9", 11),
          ("performance24period90", 92),
          ("performance24period91", 93),
          ("performance24period92", 94),
          ("performance24period93", 95),
          ("performance24period94", 96),
          ("performance24period95", 97),
          ("performance24period96", 98))
    )


_Performance24Index_Type.__name__ = "Integer32"
_Performance24Index_Object = MibTableColumn
performance24Index = _Performance24Index_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1, 1, 4),
    _Performance24Index_Type()
)
performance24Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance24Index.setStatus("mandatory")
_Performance24ES_Type = Integer32
_Performance24ES_Object = MibTableColumn
performance24ES = _Performance24ES_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1, 1, 5),
    _Performance24ES_Type()
)
performance24ES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance24ES.setStatus("mandatory")
_Performance24BES_Type = Integer32
_Performance24BES_Object = MibTableColumn
performance24BES = _Performance24BES_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1, 1, 6),
    _Performance24BES_Type()
)
performance24BES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance24BES.setStatus("mandatory")
_Performance24SES_Type = Integer32
_Performance24SES_Object = MibTableColumn
performance24SES = _Performance24SES_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1, 1, 7),
    _Performance24SES_Type()
)
performance24SES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance24SES.setStatus("mandatory")
_Performance24UAS_Type = Integer32
_Performance24UAS_Object = MibTableColumn
performance24UAS = _Performance24UAS_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1, 1, 8),
    _Performance24UAS_Type()
)
performance24UAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance24UAS.setStatus("mandatory")
_Performance24LOFC_Type = Integer32
_Performance24LOFC_Object = MibTableColumn
performance24LOFC = _Performance24LOFC_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1, 1, 9),
    _Performance24LOFC_Type()
)
performance24LOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance24LOFC.setStatus("mandatory")
_Performance24CSS_Type = Integer32
_Performance24CSS_Object = MibTableColumn
performance24CSS = _Performance24CSS_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1, 1, 10),
    _Performance24CSS_Type()
)
performance24CSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance24CSS.setStatus("mandatory")
_Performance24CRCES_Type = Integer32
_Performance24CRCES_Object = MibTableColumn
performance24CRCES = _Performance24CRCES_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1, 1, 11),
    _Performance24CRCES_Type()
)
performance24CRCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance24CRCES.setStatus("mandatory")
_Performance24OOFS_Type = Integer32
_Performance24OOFS_Object = MibTableColumn
performance24OOFS = _Performance24OOFS_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1, 1, 12),
    _Performance24OOFS_Type()
)
performance24OOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance24OOFS.setStatus("mandatory")
_Performance24LOSS_Type = Integer32
_Performance24LOSS_Object = MibTableColumn
performance24LOSS = _Performance24LOSS_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1, 1, 13),
    _Performance24LOSS_Type()
)
performance24LOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance24LOSS.setStatus("mandatory")
_Performance24AISS_Type = Integer32
_Performance24AISS_Object = MibTableColumn
performance24AISS = _Performance24AISS_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1, 1, 14),
    _Performance24AISS_Type()
)
performance24AISS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance24AISS.setStatus("mandatory")
_Performance24RAS_Type = Integer32
_Performance24RAS_Object = MibTableColumn
performance24RAS = _Performance24RAS_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1, 1, 15),
    _Performance24RAS_Type()
)
performance24RAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance24RAS.setStatus("mandatory")
_Performance24BPVS_Type = Integer32
_Performance24BPVS_Object = MibTableColumn
performance24BPVS = _Performance24BPVS_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 1, 1, 16),
    _Performance24BPVS_Type()
)
performance24BPVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance24BPVS.setStatus("mandatory")
_Performance30Table_Object = MibTable
performance30Table = _Performance30Table_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2)
)
if mibBuilder.loadTexts:
    performance30Table.setStatus("optional")
_Performance30TableEntry_Object = MibTableRow
performance30TableEntry = _Performance30TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2, 1)
)
performance30TableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "performance30NearIndex"),
    (0, "INTERFACES-MIB", "performance30FarIndex"),
    (0, "INTERFACES-MIB", "performance30InterfaceIndex"),
    (0, "INTERFACES-MIB", "performance30Index"),
)
if mibBuilder.loadTexts:
    performance30TableEntry.setStatus("mandatory")
_Performance30NearIndex_Type = Integer32
_Performance30NearIndex_Object = MibTableColumn
performance30NearIndex = _Performance30NearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2, 1, 1),
    _Performance30NearIndex_Type()
)
performance30NearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance30NearIndex.setStatus("mandatory")
_Performance30FarIndex_Type = Integer32
_Performance30FarIndex_Object = MibTableColumn
performance30FarIndex = _Performance30FarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2, 1, 2),
    _Performance30FarIndex_Type()
)
performance30FarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance30FarIndex.setStatus("mandatory")
_Performance30InterfaceIndex_Type = Integer32
_Performance30InterfaceIndex_Object = MibTableColumn
performance30InterfaceIndex = _Performance30InterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2, 1, 3),
    _Performance30InterfaceIndex_Type()
)
performance30InterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance30InterfaceIndex.setStatus("mandatory")


class _Performance30Index_Type(Integer32):
    """Custom type performance30Index based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("performance30Summary", 1),
          ("performance30day1", 2),
          ("performance30day10", 11),
          ("performance30day11", 12),
          ("performance30day12", 13),
          ("performance30day13", 14),
          ("performance30day14", 15),
          ("performance30day15", 16),
          ("performance30day16", 17),
          ("performance30day17", 18),
          ("performance30day18", 19),
          ("performance30day19", 20),
          ("performance30day2", 3),
          ("performance30day20", 21),
          ("performance30day21", 22),
          ("performance30day22", 23),
          ("performance30day23", 24),
          ("performance30day24", 25),
          ("performance30day25", 26),
          ("performance30day26", 27),
          ("performance30day27", 28),
          ("performance30day28", 29),
          ("performance30day29", 30),
          ("performance30day3", 4),
          ("performance30day30", 31),
          ("performance30day4", 5),
          ("performance30day5", 6),
          ("performance30day6", 7),
          ("performance30day7", 8),
          ("performance30day8", 9),
          ("performance30day9", 10))
    )


_Performance30Index_Type.__name__ = "Integer32"
_Performance30Index_Object = MibTableColumn
performance30Index = _Performance30Index_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2, 1, 4),
    _Performance30Index_Type()
)
performance30Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance30Index.setStatus("mandatory")
_Performance30ES_Type = Integer32
_Performance30ES_Object = MibTableColumn
performance30ES = _Performance30ES_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2, 1, 5),
    _Performance30ES_Type()
)
performance30ES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance30ES.setStatus("mandatory")
_Performance30BES_Type = Integer32
_Performance30BES_Object = MibTableColumn
performance30BES = _Performance30BES_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2, 1, 6),
    _Performance30BES_Type()
)
performance30BES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance30BES.setStatus("mandatory")
_Performance30SES_Type = Integer32
_Performance30SES_Object = MibTableColumn
performance30SES = _Performance30SES_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2, 1, 7),
    _Performance30SES_Type()
)
performance30SES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance30SES.setStatus("mandatory")
_Performance30UAS_Type = Integer32
_Performance30UAS_Object = MibTableColumn
performance30UAS = _Performance30UAS_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2, 1, 8),
    _Performance30UAS_Type()
)
performance30UAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance30UAS.setStatus("mandatory")
_Performance30LOFC_Type = Integer32
_Performance30LOFC_Object = MibTableColumn
performance30LOFC = _Performance30LOFC_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2, 1, 9),
    _Performance30LOFC_Type()
)
performance30LOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance30LOFC.setStatus("mandatory")
_Performance30CSS_Type = Integer32
_Performance30CSS_Object = MibTableColumn
performance30CSS = _Performance30CSS_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2, 1, 10),
    _Performance30CSS_Type()
)
performance30CSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance30CSS.setStatus("mandatory")
_Performance30CRCES_Type = Integer32
_Performance30CRCES_Object = MibTableColumn
performance30CRCES = _Performance30CRCES_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2, 1, 11),
    _Performance30CRCES_Type()
)
performance30CRCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance30CRCES.setStatus("mandatory")
_Performance30OOFS_Type = Integer32
_Performance30OOFS_Object = MibTableColumn
performance30OOFS = _Performance30OOFS_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2, 1, 12),
    _Performance30OOFS_Type()
)
performance30OOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance30OOFS.setStatus("mandatory")
_Performance30LOSS_Type = Integer32
_Performance30LOSS_Object = MibTableColumn
performance30LOSS = _Performance30LOSS_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2, 1, 13),
    _Performance30LOSS_Type()
)
performance30LOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance30LOSS.setStatus("mandatory")
_Performance30AISS_Type = Integer32
_Performance30AISS_Object = MibTableColumn
performance30AISS = _Performance30AISS_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2, 1, 14),
    _Performance30AISS_Type()
)
performance30AISS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance30AISS.setStatus("mandatory")
_Performance30RAS_Type = Integer32
_Performance30RAS_Object = MibTableColumn
performance30RAS = _Performance30RAS_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2, 1, 15),
    _Performance30RAS_Type()
)
performance30RAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance30RAS.setStatus("mandatory")
_Performance30BPVS_Type = Integer32
_Performance30BPVS_Object = MibTableColumn
performance30BPVS = _Performance30BPVS_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 9, 2, 1, 16),
    _Performance30BPVS_Type()
)
performance30BPVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performance30BPVS.setStatus("mandatory")
_Itable_ObjectIdentity = ObjectIdentity
itable = _Itable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 8, 10)
)
_ITable_Object = MibTable
iTable = _ITable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 10, 1)
)
if mibBuilder.loadTexts:
    iTable.setStatus("optional")
_ITableEntry_Object = MibTableRow
iTableEntry = _ITableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 10, 1, 1)
)
iTableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "iTableNearIndex"),
    (0, "INTERFACES-MIB", "iTableFarIndex"),
    (0, "INTERFACES-MIB", "iTableIndex"),
)
if mibBuilder.loadTexts:
    iTableEntry.setStatus("mandatory")
_ITableNearIndex_Type = Integer32
_ITableNearIndex_Object = MibTableColumn
iTableNearIndex = _ITableNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 10, 1, 1, 1),
    _ITableNearIndex_Type()
)
iTableNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iTableNearIndex.setStatus("mandatory")
_ITableFarIndex_Type = Integer32
_ITableFarIndex_Object = MibTableColumn
iTableFarIndex = _ITableFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 10, 1, 1, 2),
    _ITableFarIndex_Type()
)
iTableFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iTableFarIndex.setStatus("mandatory")
_ITableIndex_Type = Integer32
_ITableIndex_Object = MibTableColumn
iTableIndex = _ITableIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 10, 1, 1, 3),
    _ITableIndex_Type()
)
iTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iTableIndex.setStatus("mandatory")


class _IDescription_Type(DisplayString):
    """Custom type iDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IDescription_Type.__name__ = "DisplayString"
_IDescription_Object = MibTableColumn
iDescription = _IDescription_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 10, 1, 1, 4),
    _IDescription_Type()
)
iDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iDescription.setStatus("mandatory")


class _IType_Type(Integer32):
    """Custom type iType based on Integer32"""
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
              11,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              192)
        )
    )
    namedValues = NamedValues(
        *(("alt", 129),
          ("ddsdbu", 136),
          ("ddsdte", 135),
          ("ddsntw", 134),
          ("didte", 131),
          ("disabled", 0),
          ("dualddsv1", 7),
          ("dualddsv2", 11),
          ("dualt1dte", 6),
          ("e1ntw", 133),
          ("e1sig", 192),
          ("eandm", 139),
          ("eia530", 2),
          ("fxo", 138),
          ("fxs", 137),
          ("hexdds", 8),
          ("hsdata", 5),
          ("ocudp", 9),
          ("rfdl", 128),
          ("rs232", 3),
          ("t1dte", 130),
          ("t1ntw", 132),
          ("v35", 1),
          ("voice", 4),
          ("x21", 10))
    )


_IType_Type.__name__ = "Integer32"
_IType_Object = MibTableColumn
iType = _IType_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 10, 1, 1, 5),
    _IType_Type()
)
iType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iType.setStatus("mandatory")
_ISlot_Type = Integer32
_ISlot_Object = MibTableColumn
iSlot = _ISlot_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 10, 1, 1, 6),
    _ISlot_Type()
)
iSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSlot.setStatus("mandatory")
_IPort_Type = Integer32
_IPort_Object = MibTableColumn
iPort = _IPort_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 10, 1, 1, 7),
    _IPort_Type()
)
iPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPort.setStatus("mandatory")


class _IStatus_Type(Integer32):
    """Custom type iStatus based on Integer32"""
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
        *(("iStatusAlarmed", 4),
          ("iStatusErrored", 3),
          ("iStatusOK", 2),
          ("iStatusOther", 1),
          ("iStatusTesting", 5))
    )


_IStatus_Type.__name__ = "Integer32"
_IStatus_Object = MibTableColumn
iStatus = _IStatus_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 10, 1, 1, 8),
    _IStatus_Type()
)
iStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iStatus.setStatus("mandatory")
_Traplog_ObjectIdentity = ObjectIdentity
traplog = _Traplog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 8, 11)
)
_TraplogTable_Object = MibTable
traplogTable = _TraplogTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 11, 1)
)
if mibBuilder.loadTexts:
    traplogTable.setStatus("optional")
_TraplogEntry_Object = MibTableRow
traplogEntry = _TraplogEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 11, 1, 1)
)
traplogEntry.setIndexNames(
    (0, "INTERFACES-MIB", "traplogIndex"),
)
if mibBuilder.loadTexts:
    traplogEntry.setStatus("mandatory")
_TraplogIndex_Type = Integer32
_TraplogIndex_Object = MibTableColumn
traplogIndex = _TraplogIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 11, 1, 1, 1),
    _TraplogIndex_Type()
)
traplogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traplogIndex.setStatus("mandatory")
_TraplogNearIndex_Type = Integer32
_TraplogNearIndex_Object = MibTableColumn
traplogNearIndex = _TraplogNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 11, 1, 1, 2),
    _TraplogNearIndex_Type()
)
traplogNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traplogNearIndex.setStatus("mandatory")
_TraplogFarIndex_Type = Integer32
_TraplogFarIndex_Object = MibTableColumn
traplogFarIndex = _TraplogFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 11, 1, 1, 3),
    _TraplogFarIndex_Type()
)
traplogFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traplogFarIndex.setStatus("mandatory")
_TraplogInterfaceIndex_Type = Integer32
_TraplogInterfaceIndex_Object = MibTableColumn
traplogInterfaceIndex = _TraplogInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 11, 1, 1, 4),
    _TraplogInterfaceIndex_Type()
)
traplogInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traplogInterfaceIndex.setStatus("mandatory")
_TraplogTrapNum_Type = Integer32
_TraplogTrapNum_Object = MibTableColumn
traplogTrapNum = _TraplogTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 11, 1, 1, 5),
    _TraplogTrapNum_Type()
)
traplogTrapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traplogTrapNum.setStatus("mandatory")


class _TraplogTimeStamp_Type(DisplayString):
    """Custom type traplogTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TraplogTimeStamp_Type.__name__ = "DisplayString"
_TraplogTimeStamp_Object = MibTableColumn
traplogTimeStamp = _TraplogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 11, 1, 1, 6),
    _TraplogTimeStamp_Type()
)
traplogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traplogTimeStamp.setStatus("mandatory")


class _TraplogDeviceType_Type(Integer32):
    """Custom type traplogDeviceType based on Integer32"""
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
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("dds4001", 15),
          ("dds4051", 17),
          ("dds4101", 16),
          ("dds4151", 18),
          ("dds41TDM", 19),
          ("e12048", 4),
          ("e13021", 5),
          ("generic54016", 20),
          ("none", 2),
          ("other", 1),
          ("t12000", 3),
          ("t13000", 6),
          ("t13001", 7),
          ("t13002", 8),
          ("t13030", 9),
          ("t13060", 10),
          ("t13101", 11),
          ("t13102", 12),
          ("t13111", 13),
          ("t13112", 14))
    )


_TraplogDeviceType_Type.__name__ = "Integer32"
_TraplogDeviceType_Object = MibTableColumn
traplogDeviceType = _TraplogDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 11, 1, 1, 7),
    _TraplogDeviceType_Type()
)
traplogDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traplogDeviceType.setStatus("mandatory")
_TraplogDeleteEntry_Type = Integer32
_TraplogDeleteEntry_Object = MibScalar
traplogDeleteEntry = _TraplogDeleteEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 11, 2),
    _TraplogDeleteEntry_Type()
)
traplogDeleteEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traplogDeleteEntry.setStatus("mandatory")


class _TraplogSortOption_Type(Integer32):
    """Custom type traplogSortOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascendingtimestamp", 2),
          ("ascendingunit", 3),
          ("other", 1))
    )


_TraplogSortOption_Type.__name__ = "Integer32"
_TraplogSortOption_Object = MibScalar
traplogSortOption = _TraplogSortOption_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 11, 3),
    _TraplogSortOption_Type()
)
traplogSortOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traplogSortOption.setStatus("mandatory")
_TraplogLastTimeStamp_Type = TimeTicks
_TraplogLastTimeStamp_Object = MibScalar
traplogLastTimeStamp = _TraplogLastTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 11, 4),
    _TraplogLastTimeStamp_Type()
)
traplogLastTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traplogLastTimeStamp.setStatus("mandatory")
_UnitUtilities_ObjectIdentity = ObjectIdentity
unitUtilities = _UnitUtilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 425, 8, 12)
)
_UnitUtilitiesTable_Object = MibTable
unitUtilitiesTable = _UnitUtilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 12, 1)
)
if mibBuilder.loadTexts:
    unitUtilitiesTable.setStatus("optional")
_UnitUtilitiesTableEntry_Object = MibTableRow
unitUtilitiesTableEntry = _UnitUtilitiesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 12, 1, 1)
)
unitUtilitiesTableEntry.setIndexNames(
    (0, "INTERFACES-MIB", "unitUtilitiesNearIndex"),
    (0, "INTERFACES-MIB", "unitUtilitiesFarIndex"),
)
if mibBuilder.loadTexts:
    unitUtilitiesTableEntry.setStatus("mandatory")
_UnitUtilitiesNearIndex_Type = Integer32
_UnitUtilitiesNearIndex_Object = MibTableColumn
unitUtilitiesNearIndex = _UnitUtilitiesNearIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 12, 1, 1, 1),
    _UnitUtilitiesNearIndex_Type()
)
unitUtilitiesNearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitUtilitiesNearIndex.setStatus("mandatory")
_UnitUtilitiesFarIndex_Type = Integer32
_UnitUtilitiesFarIndex_Object = MibTableColumn
unitUtilitiesFarIndex = _UnitUtilitiesFarIndex_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 12, 1, 1, 2),
    _UnitUtilitiesFarIndex_Type()
)
unitUtilitiesFarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitUtilitiesFarIndex.setStatus("mandatory")
_UnitUtilitiesLocalPassword_Type = DisplayString
_UnitUtilitiesLocalPassword_Object = MibTableColumn
unitUtilitiesLocalPassword = _UnitUtilitiesLocalPassword_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 12, 1, 1, 3),
    _UnitUtilitiesLocalPassword_Type()
)
unitUtilitiesLocalPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitUtilitiesLocalPassword.setStatus("mandatory")


class _UnitUtilitiesTime_Type(DisplayString):
    """Custom type unitUtilitiesTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_UnitUtilitiesTime_Type.__name__ = "DisplayString"
_UnitUtilitiesTime_Object = MibTableColumn
unitUtilitiesTime = _UnitUtilitiesTime_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 12, 1, 1, 4),
    _UnitUtilitiesTime_Type()
)
unitUtilitiesTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitUtilitiesTime.setStatus("mandatory")


class _UnitUtilitiesDate_Type(DisplayString):
    """Custom type unitUtilitiesDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_UnitUtilitiesDate_Type.__name__ = "DisplayString"
_UnitUtilitiesDate_Object = MibTableColumn
unitUtilitiesDate = _UnitUtilitiesDate_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 12, 1, 1, 5),
    _UnitUtilitiesDate_Type()
)
unitUtilitiesDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitUtilitiesDate.setStatus("mandatory")


class _UnitUtilitiesMaintenanceReset_Type(Integer32):
    """Custom type unitUtilitiesMaintenanceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2),
          ("restart", 3))
    )


_UnitUtilitiesMaintenanceReset_Type.__name__ = "Integer32"
_UnitUtilitiesMaintenanceReset_Object = MibTableColumn
unitUtilitiesMaintenanceReset = _UnitUtilitiesMaintenanceReset_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 12, 1, 1, 6),
    _UnitUtilitiesMaintenanceReset_Type()
)
unitUtilitiesMaintenanceReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitUtilitiesMaintenanceReset.setStatus("mandatory")
_UnitUtilitiesAlarmResetTimer_Type = Integer32
_UnitUtilitiesAlarmResetTimer_Object = MibTableColumn
unitUtilitiesAlarmResetTimer = _UnitUtilitiesAlarmResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 12, 1, 1, 7),
    _UnitUtilitiesAlarmResetTimer_Type()
)
unitUtilitiesAlarmResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitUtilitiesAlarmResetTimer.setStatus("optional")


class _UnitUtilitiesAlarmClear_Type(Integer32):
    """Custom type unitUtilitiesAlarmClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("utilitiesAlarmClearNow", 2),
          ("utilitiesAlarmClearOther", 1))
    )


_UnitUtilitiesAlarmClear_Type.__name__ = "Integer32"
_UnitUtilitiesAlarmClear_Object = MibTableColumn
unitUtilitiesAlarmClear = _UnitUtilitiesAlarmClear_Object(
    (1, 3, 6, 1, 4, 1, 425, 8, 12, 1, 1, 8),
    _UnitUtilitiesAlarmClear_Type()
)
unitUtilitiesAlarmClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitUtilitiesAlarmClear.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTERFACES-MIB",
    **{"txport": txport,
       "companyinfo": companyinfo,
       "products": products,
       "temporary": temporary,
       "traps": traps,
       "revision": revision,
       "pdc": pdc,
       "utilities": utilities,
       "tinterfaces": tinterfaces,
       "mgmtPorts": mgmtPorts,
       "mgmtPortsTable": mgmtPortsTable,
       "mgmtPortsTableEntry": mgmtPortsTableEntry,
       "mgmtPortsTableIndex": mgmtPortsTableIndex,
       "mgmtPortsDescription": mgmtPortsDescription,
       "mgmtPortsElementID": mgmtPortsElementID,
       "mgmtPortsMode": mgmtPortsMode,
       "mgmtPortsDialPrefix": mgmtPortsDialPrefix,
       "mgmtPortsPrimaryDialString": mgmtPortsPrimaryDialString,
       "mgmtPortsSecondaryDialString": mgmtPortsSecondaryDialString,
       "mgmtPortsExtInitString": mgmtPortsExtInitString,
       "mgmtPortsCompressedSlip": mgmtPortsCompressedSlip,
       "mgmtPortsInternalModem": mgmtPortsInternalModem,
       "dbu": dbu,
       "dbuConfigTable": dbuConfigTable,
       "dbuConfigTableEntry": dbuConfigTableEntry,
       "dbuNearIndex": dbuNearIndex,
       "dbuFarIndex": dbuFarIndex,
       "dbuConfigTableIndex": dbuConfigTableIndex,
       "dbuDescription": dbuDescription,
       "dbuRate": dbuRate,
       "dbuMode": dbuMode,
       "dbuFormat": dbuFormat,
       "dbuNumber": dbuNumber,
       "dbuStatus": dbuStatus,
       "dbuCommand": dbuCommand,
       "dbuActivator1": dbuActivator1,
       "dbuActivator2": dbuActivator2,
       "dbuDialStr": dbuDialStr,
       "dbuInitStr": dbuInitStr,
       "dbuHangupStr": dbuHangupStr,
       "dbuPasswordStr": dbuPasswordStr,
       "dbuSecurity": dbuSecurity,
       "dbuDtrDial": dbuDtrDial,
       "dbuISDNSwitchType": dbuISDNSwitchType,
       "dbuISDNSwitchVersion": dbuISDNSwitchVersion,
       "dbuISDNTEI": dbuISDNTEI,
       "dbuISDNSPID": dbuISDNSPID,
       "dbuISDNDDNUM": dbuISDNDDNUM,
       "dbuResetStringsTable": dbuResetStringsTable,
       "dbuResetStringsEntry": dbuResetStringsEntry,
       "dbuResetNearIndex": dbuResetNearIndex,
       "dbuResetFarIndex": dbuResetFarIndex,
       "dbuResetConfigEntryIndex": dbuResetConfigEntryIndex,
       "dbuResetStringsIndex": dbuResetStringsIndex,
       "dbuResetString": dbuResetString,
       "dbuStartStopTable": dbuStartStopTable,
       "dbuStartStopTableEntry": dbuStartStopTableEntry,
       "dbuStartStopNearIndex": dbuStartStopNearIndex,
       "dbuStartStopFarIndex": dbuStartStopFarIndex,
       "dbuStartStopConfigEntryIndex": dbuStartStopConfigEntryIndex,
       "dbuStartStopDayOfWeek": dbuStartStopDayOfWeek,
       "dbuStart": dbuStart,
       "dbuStop": dbuStop,
       "t1e1": t1e1,
       "t1e1ConfigTable": t1e1ConfigTable,
       "t1e1ConfigTableEntry": t1e1ConfigTableEntry,
       "t1e1ConfigNearIndex": t1e1ConfigNearIndex,
       "t1e1ConfigFarIndex": t1e1ConfigFarIndex,
       "t1e1ConfigIndex": t1e1ConfigIndex,
       "t1e1Description": t1e1Description,
       "t1e1Mode": t1e1Mode,
       "t1e1FrameType": t1e1FrameType,
       "t1e1LineCode": t1e1LineCode,
       "t1e1LineBuildOut": t1e1LineBuildOut,
       "t1e1Timing": t1e1Timing,
       "t1e1StationInTiming": t1e1StationInTiming,
       "t1e1StationTiming": t1e1StationTiming,
       "t1e1PRM": t1e1PRM,
       "t1e1ZeroSuppress": t1e1ZeroSuppress,
       "t1e1NationalBit": t1e1NationalBit,
       "t1e1KeepAlive": t1e1KeepAlive,
       "t1e1CRC4Mode": t1e1CRC4Mode,
       "t1e1DSXLevel": t1e1DSXLevel,
       "t1e1CRC": t1e1CRC,
       "t1e1FDLPassThrough": t1e1FDLPassThrough,
       "t1e1AudibleAlarm": t1e1AudibleAlarm,
       "t1e1AlarmTable": t1e1AlarmTable,
       "t1e1AlarmTableEntry": t1e1AlarmTableEntry,
       "t1e1AlarmNearIndex": t1e1AlarmNearIndex,
       "t1e1AlarmFarIndex": t1e1AlarmFarIndex,
       "t1e1AlarmIndex": t1e1AlarmIndex,
       "t1e1StatusSummary": t1e1StatusSummary,
       "t1e1AlarmSummary": t1e1AlarmSummary,
       "t1e1ESStatus": t1e1ESStatus,
       "t1e1ESCount": t1e1ESCount,
       "t1e1ESThreshold": t1e1ESThreshold,
       "t1e1ESAlarm": t1e1ESAlarm,
       "t1e1SESStatus": t1e1SESStatus,
       "t1e1SESCount": t1e1SESCount,
       "t1e1SESThreshold": t1e1SESThreshold,
       "t1e1SESAlarm": t1e1SESAlarm,
       "t1e1LOSSStatus": t1e1LOSSStatus,
       "t1e1LOSSCount": t1e1LOSSCount,
       "t1e1LOSSThreshold": t1e1LOSSThreshold,
       "t1e1LOSSAlarm": t1e1LOSSAlarm,
       "t1e1UASStatus": t1e1UASStatus,
       "t1e1UASCount": t1e1UASCount,
       "t1e1UASThreshold": t1e1UASThreshold,
       "t1e1UASAlarm": t1e1UASAlarm,
       "t1e1CSSStatus": t1e1CSSStatus,
       "t1e1CSSCount": t1e1CSSCount,
       "t1e1CSSThreshold": t1e1CSSThreshold,
       "t1e1CSSAlarm": t1e1CSSAlarm,
       "t1e1BPVSStatus": t1e1BPVSStatus,
       "t1e1BPVSCount": t1e1BPVSCount,
       "t1e1BPVSThreshold": t1e1BPVSThreshold,
       "t1e1BPVSAlarm": t1e1BPVSAlarm,
       "t1e1OOFSStatus": t1e1OOFSStatus,
       "t1e1OOFSCount": t1e1OOFSCount,
       "t1e1OOFSThreshold": t1e1OOFSThreshold,
       "t1e1OOFSAlarm": t1e1OOFSAlarm,
       "t1e1AISStatus": t1e1AISStatus,
       "t1e1AISCount": t1e1AISCount,
       "t1e1AISThreshold": t1e1AISThreshold,
       "t1e1AISAlarm": t1e1AISAlarm,
       "t1e1RASStatus": t1e1RASStatus,
       "t1e1RASCount": t1e1RASCount,
       "t1e1RASThreshold": t1e1RASThreshold,
       "t1e1RASAlarm": t1e1RASAlarm,
       "t1e1AlarmResetTimer": t1e1AlarmResetTimer,
       "t1e1AlarmReset": t1e1AlarmReset,
       "ddsNet": ddsNet,
       "ddsNetConfigTable": ddsNetConfigTable,
       "ddsNetConfigTableEntry": ddsNetConfigTableEntry,
       "ddsNetConfigNearIndex": ddsNetConfigNearIndex,
       "ddsNetConfigFarIndex": ddsNetConfigFarIndex,
       "ddsNetConfigIndex": ddsNetConfigIndex,
       "ddsNetDescription": ddsNetDescription,
       "ddsNetRate": ddsNetRate,
       "ddsNetMode": ddsNetMode,
       "ddsNetTimingSource": ddsNetTimingSource,
       "ddsNetRemComm": ddsNetRemComm,
       "ddsNetCircuitAssur": ddsNetCircuitAssur,
       "ddsNetAntiStrTimer": ddsNetAntiStrTimer,
       "ddsNetAlarmTable": ddsNetAlarmTable,
       "ddsNetAlarmTableEntry": ddsNetAlarmTableEntry,
       "ddsNetAlarmNearIndex": ddsNetAlarmNearIndex,
       "ddsNetAlarmFarIndex": ddsNetAlarmFarIndex,
       "ddsNetAlarmIndex": ddsNetAlarmIndex,
       "ddsNetStatusSummary": ddsNetStatusSummary,
       "ddsNetAlarmSummary": ddsNetAlarmSummary,
       "ddsNetLOSStatus": ddsNetLOSStatus,
       "ddsNetLOSCount": ddsNetLOSCount,
       "ddsNetLOSThreshold": ddsNetLOSThreshold,
       "ddsNetLOSAlarm": ddsNetLOSAlarm,
       "ddsNetOOFStatus": ddsNetOOFStatus,
       "ddsNetOOFCount": ddsNetOOFCount,
       "ddsNetOOFThreshold": ddsNetOOFThreshold,
       "ddsNetOOFAlarm": ddsNetOOFAlarm,
       "ddsNetOOSStatus": ddsNetOOSStatus,
       "ddsNetOOSCount": ddsNetOOSCount,
       "ddsNetOOSThreshold": ddsNetOOSThreshold,
       "ddsNetOOSAlarm": ddsNetOOSAlarm,
       "ddsNetFDLStatus": ddsNetFDLStatus,
       "ddsNetFDLCount": ddsNetFDLCount,
       "ddsNetFDLThreshold": ddsNetFDLThreshold,
       "ddsNetFDLAlarm": ddsNetFDLAlarm,
       "ddsNetAlarmResetTimer": ddsNetAlarmResetTimer,
       "ddsNetAlarmReset": ddsNetAlarmReset,
       "serialDte": serialDte,
       "serialDteConfigTable": serialDteConfigTable,
       "serialDteConfigTableEntry": serialDteConfigTableEntry,
       "serialDteConfigNearIndex": serialDteConfigNearIndex,
       "serialDteConfigFarIndex": serialDteConfigFarIndex,
       "serialDteConfigIndex": serialDteConfigIndex,
       "serialDteDescription": serialDteDescription,
       "serialDteType": serialDteType,
       "serialDteRate": serialDteRate,
       "serialDteInvertData": serialDteInvertData,
       "serialDteFormat": serialDteFormat,
       "serialDteParity": serialDteParity,
       "serialDteStopBit": serialDteStopBit,
       "serialDteMode": serialDteMode,
       "serialDteDSR": serialDteDSR,
       "serialDteDCD": serialDteDCD,
       "serialDteRTS": serialDteRTS,
       "serialDteRTSDelay": serialDteRTSDelay,
       "serialDteDTR": serialDteDTR,
       "serialDteCTS": serialDteCTS,
       "serialDteV54": serialDteV54,
       "serialDteLL": serialDteLL,
       "serialDteRL": serialDteRL,
       "serialDteStartChannel": serialDteStartChannel,
       "serialDteNumberOfChannels": serialDteNumberOfChannels,
       "serialDteTxClock": serialDteTxClock,
       "serialDteBundle": serialDteBundle,
       "serialDteChannelRate": serialDteChannelRate,
       "serialDteInvertClock": serialDteInvertClock,
       "serialDteAlarmTable": serialDteAlarmTable,
       "serialDteAlarmTableEntry": serialDteAlarmTableEntry,
       "serialDteAlarmNearIndex": serialDteAlarmNearIndex,
       "serialDteAlarmFarIndex": serialDteAlarmFarIndex,
       "serialDteAlarmIndex": serialDteAlarmIndex,
       "serialDteDTRAlarmControl": serialDteDTRAlarmControl,
       "serialDteDTRAlarmStatus": serialDteDTRAlarmStatus,
       "serialDteStatusSummary": serialDteStatusSummary,
       "serialDteAlarmSummary": serialDteAlarmSummary,
       "serialDteASCStatus": serialDteASCStatus,
       "serialDteASCCount": serialDteASCCount,
       "serialDteASCThreshold": serialDteASCThreshold,
       "serialDteASCAlarm": serialDteASCAlarm,
       "serialDteFDLStatus": serialDteFDLStatus,
       "serialDteFDLCount": serialDteFDLCount,
       "serialDteFDLThreshold": serialDteFDLThreshold,
       "serialDteFDLAlarm": serialDteFDLAlarm,
       "serialDteLOSStatus": serialDteLOSStatus,
       "serialDteLOSCount": serialDteLOSCount,
       "serialDteLOSThreshold": serialDteLOSThreshold,
       "serialDteLOSAlarm": serialDteLOSAlarm,
       "analogDte": analogDte,
       "analogDteTable": analogDteTable,
       "analogDteTableEntry": analogDteTableEntry,
       "analogDteNearIndex": analogDteNearIndex,
       "analogDteFarIndex": analogDteFarIndex,
       "analogDteIndex": analogDteIndex,
       "analogDteDescription": analogDteDescription,
       "analogDteCardType": analogDteCardType,
       "analogDteMode": analogDteMode,
       "analogDteState": analogDteState,
       "analogDteElementID": analogDteElementID,
       "analogDteSignalling": analogDteSignalling,
       "analogDteDNISDelay": analogDteDNISDelay,
       "analogDteTxGain": analogDteTxGain,
       "analogDteRxGain": analogDteRxGain,
       "connection": connection,
       "connectionTable": connectionTable,
       "connectionTableEntry": connectionTableEntry,
       "connectionNearIndex": connectionNearIndex,
       "connectionFarIndex": connectionFarIndex,
       "connectionTableIndex": connectionTableIndex,
       "connectionTableDescription": connectionTableDescription,
       "connectionChannelTable": connectionChannelTable,
       "connectionChannelEntry": connectionChannelEntry,
       "connectionChannelNearIndex": connectionChannelNearIndex,
       "connectionChannelFarIndex": connectionChannelFarIndex,
       "connectionChannelLineIndex": connectionChannelLineIndex,
       "connectionChannelIndex": connectionChannelIndex,
       "channelInterfaceAssignment": channelInterfaceAssignment,
       "channelInterfaceDescription": channelInterfaceDescription,
       "channelInterfaceChannel": channelInterfaceChannel,
       "channelSignalling": channelSignalling,
       "maintenance": maintenance,
       "bertTable": bertTable,
       "bertTableEntry": bertTableEntry,
       "bertNearIndex": bertNearIndex,
       "bertFarIndex": bertFarIndex,
       "bertIndex": bertIndex,
       "bertPattern": bertPattern,
       "bertLength": bertLength,
       "bertPatternSync": bertPatternSync,
       "bertElapsedTime": bertElapsedTime,
       "bertBitErrors": bertBitErrors,
       "bertErroredSeconds": bertErroredSeconds,
       "bertPercentEFS": bertPercentEFS,
       "bertCommand": bertCommand,
       "bertInterfaceTable": bertInterfaceTable,
       "bertInterfaceTableEntry": bertInterfaceTableEntry,
       "bertInterfaceNearIndex": bertInterfaceNearIndex,
       "bertInterfaceFarIndex": bertInterfaceFarIndex,
       "bertChipIndex": bertChipIndex,
       "bertInterfaceIndex": bertInterfaceIndex,
       "bertInterfaceSetting": bertInterfaceSetting,
       "testTable": testTable,
       "testTableEntry": testTableEntry,
       "testNearIndex": testNearIndex,
       "testFarIndex": testFarIndex,
       "testTableIndex": testTableIndex,
       "testType": testType,
       "testLoopDirection": testLoopDirection,
       "testFarLLBFraming": testFarLLBFraming,
       "performance": performance,
       "performance24Table": performance24Table,
       "performance24TableEntry": performance24TableEntry,
       "performance24NearIndex": performance24NearIndex,
       "performance24FarIndex": performance24FarIndex,
       "performance24InterfaceIndex": performance24InterfaceIndex,
       "performance24Index": performance24Index,
       "performance24ES": performance24ES,
       "performance24BES": performance24BES,
       "performance24SES": performance24SES,
       "performance24UAS": performance24UAS,
       "performance24LOFC": performance24LOFC,
       "performance24CSS": performance24CSS,
       "performance24CRCES": performance24CRCES,
       "performance24OOFS": performance24OOFS,
       "performance24LOSS": performance24LOSS,
       "performance24AISS": performance24AISS,
       "performance24RAS": performance24RAS,
       "performance24BPVS": performance24BPVS,
       "performance30Table": performance30Table,
       "performance30TableEntry": performance30TableEntry,
       "performance30NearIndex": performance30NearIndex,
       "performance30FarIndex": performance30FarIndex,
       "performance30InterfaceIndex": performance30InterfaceIndex,
       "performance30Index": performance30Index,
       "performance30ES": performance30ES,
       "performance30BES": performance30BES,
       "performance30SES": performance30SES,
       "performance30UAS": performance30UAS,
       "performance30LOFC": performance30LOFC,
       "performance30CSS": performance30CSS,
       "performance30CRCES": performance30CRCES,
       "performance30OOFS": performance30OOFS,
       "performance30LOSS": performance30LOSS,
       "performance30AISS": performance30AISS,
       "performance30RAS": performance30RAS,
       "performance30BPVS": performance30BPVS,
       "itable": itable,
       "iTable": iTable,
       "iTableEntry": iTableEntry,
       "iTableNearIndex": iTableNearIndex,
       "iTableFarIndex": iTableFarIndex,
       "iTableIndex": iTableIndex,
       "iDescription": iDescription,
       "iType": iType,
       "iSlot": iSlot,
       "iPort": iPort,
       "iStatus": iStatus,
       "traplog": traplog,
       "traplogTable": traplogTable,
       "traplogEntry": traplogEntry,
       "traplogIndex": traplogIndex,
       "traplogNearIndex": traplogNearIndex,
       "traplogFarIndex": traplogFarIndex,
       "traplogInterfaceIndex": traplogInterfaceIndex,
       "traplogTrapNum": traplogTrapNum,
       "traplogTimeStamp": traplogTimeStamp,
       "traplogDeviceType": traplogDeviceType,
       "traplogDeleteEntry": traplogDeleteEntry,
       "traplogSortOption": traplogSortOption,
       "traplogLastTimeStamp": traplogLastTimeStamp,
       "unitUtilities": unitUtilities,
       "unitUtilitiesTable": unitUtilitiesTable,
       "unitUtilitiesTableEntry": unitUtilitiesTableEntry,
       "unitUtilitiesNearIndex": unitUtilitiesNearIndex,
       "unitUtilitiesFarIndex": unitUtilitiesFarIndex,
       "unitUtilitiesLocalPassword": unitUtilitiesLocalPassword,
       "unitUtilitiesTime": unitUtilitiesTime,
       "unitUtilitiesDate": unitUtilitiesDate,
       "unitUtilitiesMaintenanceReset": unitUtilitiesMaintenanceReset,
       "unitUtilitiesAlarmResetTimer": unitUtilitiesAlarmResetTimer,
       "unitUtilitiesAlarmClear": unitUtilitiesAlarmClear}
)
