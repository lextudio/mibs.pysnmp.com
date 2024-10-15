# SNMP MIB module (HPNSASOFTWARESUBSYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPNSASOFTWARESUBSYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:26 2024
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

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaSW_ObjectIdentity = ObjectIdentity
hpnsaSW = _HpnsaSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24)
)
_HpnsaSWMibRev_ObjectIdentity = ObjectIdentity
hpnsaSWMibRev = _HpnsaSWMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 1)
)


class _HpnsaSWMibRevMajor_Type(Integer32):
    """Custom type hpnsaSWMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaSWMibRevMajor_Type.__name__ = "Integer32"
_HpnsaSWMibRevMajor_Object = MibScalar
hpnsaSWMibRevMajor = _HpnsaSWMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 1, 1),
    _HpnsaSWMibRevMajor_Type()
)
hpnsaSWMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWMibRevMajor.setStatus("mandatory")


class _HpnsaSWMibRevMinor_Type(Integer32):
    """Custom type hpnsaSWMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaSWMibRevMinor_Type.__name__ = "Integer32"
_HpnsaSWMibRevMinor_Object = MibScalar
hpnsaSWMibRevMinor = _HpnsaSWMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 1, 2),
    _HpnsaSWMibRevMinor_Type()
)
hpnsaSWMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWMibRevMinor.setStatus("mandatory")
_HpnsaSWManageability_ObjectIdentity = ObjectIdentity
hpnsaSWManageability = _HpnsaSWManageability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2)
)
_HpnsaSWManageabilityTable_Object = MibTable
hpnsaSWManageabilityTable = _HpnsaSWManageabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1)
)
if mibBuilder.loadTexts:
    hpnsaSWManageabilityTable.setStatus("mandatory")
_HpnsaSWManageabilityEntry_Object = MibTableRow
hpnsaSWManageabilityEntry = _HpnsaSWManageabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1)
)
hpnsaSWManageabilityEntry.setIndexNames(
    (0, "HPNSASOFTWARESUBSYSTEM-MIB", "hpnsaSWManageabilityIndex"),
)
if mibBuilder.loadTexts:
    hpnsaSWManageabilityEntry.setStatus("mandatory")
_HpnsaSWManageabilityIndex_Type = Integer32
_HpnsaSWManageabilityIndex_Object = MibTableColumn
hpnsaSWManageabilityIndex = _HpnsaSWManageabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1, 1),
    _HpnsaSWManageabilityIndex_Type()
)
hpnsaSWManageabilityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWManageabilityIndex.setStatus("mandatory")


class _HpnsaSWManageabilityFileName_Type(DisplayString):
    """Custom type hpnsaSWManageabilityFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnsaSWManageabilityFileName_Type.__name__ = "DisplayString"
_HpnsaSWManageabilityFileName_Object = MibTableColumn
hpnsaSWManageabilityFileName = _HpnsaSWManageabilityFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1, 2),
    _HpnsaSWManageabilityFileName_Type()
)
hpnsaSWManageabilityFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWManageabilityFileName.setStatus("mandatory")


class _HpnsaSWManageabilityFileSize_Type(DisplayString):
    """Custom type hpnsaSWManageabilityFileSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnsaSWManageabilityFileSize_Type.__name__ = "DisplayString"
_HpnsaSWManageabilityFileSize_Object = MibTableColumn
hpnsaSWManageabilityFileSize = _HpnsaSWManageabilityFileSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1, 3),
    _HpnsaSWManageabilityFileSize_Type()
)
hpnsaSWManageabilityFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWManageabilityFileSize.setStatus("mandatory")


class _HpnsaSWManageabilityFileDate_Type(OctetString):
    """Custom type hpnsaSWManageabilityFileDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnsaSWManageabilityFileDate_Type.__name__ = "OctetString"
_HpnsaSWManageabilityFileDate_Object = MibTableColumn
hpnsaSWManageabilityFileDate = _HpnsaSWManageabilityFileDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1, 4),
    _HpnsaSWManageabilityFileDate_Type()
)
hpnsaSWManageabilityFileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWManageabilityFileDate.setStatus("mandatory")


class _HpnsaSWManageabilityState_Type(Integer32):
    """Custom type hpnsaSWManageabilityState based on Integer32"""
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
        *(("continue-pending", 5),
          ("pause-pending", 6),
          ("paused", 7),
          ("running", 4),
          ("start-pending", 2),
          ("stop-pending", 3),
          ("stopped", 1),
          ("unknown", 0))
    )


_HpnsaSWManageabilityState_Type.__name__ = "Integer32"
_HpnsaSWManageabilityState_Object = MibTableColumn
hpnsaSWManageabilityState = _HpnsaSWManageabilityState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1, 5),
    _HpnsaSWManageabilityState_Type()
)
hpnsaSWManageabilityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWManageabilityState.setStatus("mandatory")


class _HpnsaSWManageabilityType_Type(Integer32):
    """Custom type hpnsaSWManageabilityType based on Integer32"""
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
        *(("agent", 1),
          ("driver", 3),
          ("other", 4),
          ("service", 2),
          ("unknown", 0))
    )


_HpnsaSWManageabilityType_Type.__name__ = "Integer32"
_HpnsaSWManageabilityType_Object = MibTableColumn
hpnsaSWManageabilityType = _HpnsaSWManageabilityType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1, 6),
    _HpnsaSWManageabilityType_Type()
)
hpnsaSWManageabilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWManageabilityType.setStatus("mandatory")


class _HpnsaSWManageabilityVersion_Type(DisplayString):
    """Custom type hpnsaSWManageabilityVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HpnsaSWManageabilityVersion_Type.__name__ = "DisplayString"
_HpnsaSWManageabilityVersion_Object = MibTableColumn
hpnsaSWManageabilityVersion = _HpnsaSWManageabilityVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1, 7),
    _HpnsaSWManageabilityVersion_Type()
)
hpnsaSWManageabilityVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWManageabilityVersion.setStatus("mandatory")


class _HpnsaSWManageabilityDescription_Type(DisplayString):
    """Custom type hpnsaSWManageabilityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnsaSWManageabilityDescription_Type.__name__ = "DisplayString"
_HpnsaSWManageabilityDescription_Object = MibTableColumn
hpnsaSWManageabilityDescription = _HpnsaSWManageabilityDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1, 8),
    _HpnsaSWManageabilityDescription_Type()
)
hpnsaSWManageabilityDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWManageabilityDescription.setStatus("mandatory")
_HpnsaSWDrivers_ObjectIdentity = ObjectIdentity
hpnsaSWDrivers = _HpnsaSWDrivers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3)
)
_HpnsaSWDriversTable_Object = MibTable
hpnsaSWDriversTable = _HpnsaSWDriversTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1)
)
if mibBuilder.loadTexts:
    hpnsaSWDriversTable.setStatus("mandatory")
_HpnsaSWDriversEntry_Object = MibTableRow
hpnsaSWDriversEntry = _HpnsaSWDriversEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1)
)
hpnsaSWDriversEntry.setIndexNames(
    (0, "HPNSASOFTWARESUBSYSTEM-MIB", "hpnsaSWDriversIndex"),
)
if mibBuilder.loadTexts:
    hpnsaSWDriversEntry.setStatus("mandatory")


class _HpnsaSWDriversIndex_Type(Integer32):
    """Custom type hpnsaSWDriversIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaSWDriversIndex_Type.__name__ = "Integer32"
_HpnsaSWDriversIndex_Object = MibTableColumn
hpnsaSWDriversIndex = _HpnsaSWDriversIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1, 1),
    _HpnsaSWDriversIndex_Type()
)
hpnsaSWDriversIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWDriversIndex.setStatus("mandatory")


class _HpnsaSWDriversFileName_Type(DisplayString):
    """Custom type hpnsaSWDriversFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnsaSWDriversFileName_Type.__name__ = "DisplayString"
_HpnsaSWDriversFileName_Object = MibTableColumn
hpnsaSWDriversFileName = _HpnsaSWDriversFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1, 2),
    _HpnsaSWDriversFileName_Type()
)
hpnsaSWDriversFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWDriversFileName.setStatus("mandatory")


class _HpnsaSWDriversFileSize_Type(DisplayString):
    """Custom type hpnsaSWDriversFileSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnsaSWDriversFileSize_Type.__name__ = "DisplayString"
_HpnsaSWDriversFileSize_Object = MibTableColumn
hpnsaSWDriversFileSize = _HpnsaSWDriversFileSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1, 3),
    _HpnsaSWDriversFileSize_Type()
)
hpnsaSWDriversFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWDriversFileSize.setStatus("mandatory")


class _HpnsaSWDriversFileDate_Type(OctetString):
    """Custom type hpnsaSWDriversFileDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnsaSWDriversFileDate_Type.__name__ = "OctetString"
_HpnsaSWDriversFileDate_Object = MibTableColumn
hpnsaSWDriversFileDate = _HpnsaSWDriversFileDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1, 4),
    _HpnsaSWDriversFileDate_Type()
)
hpnsaSWDriversFileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWDriversFileDate.setStatus("mandatory")


class _HpnsaSWDriversState_Type(Integer32):
    """Custom type hpnsaSWDriversState based on Integer32"""
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
        *(("continue-pending", 5),
          ("pause-pending", 6),
          ("paused", 7),
          ("running", 4),
          ("start-pending", 2),
          ("stop-pending", 3),
          ("stopped", 1),
          ("unknown", 0))
    )


_HpnsaSWDriversState_Type.__name__ = "Integer32"
_HpnsaSWDriversState_Object = MibTableColumn
hpnsaSWDriversState = _HpnsaSWDriversState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1, 5),
    _HpnsaSWDriversState_Type()
)
hpnsaSWDriversState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWDriversState.setStatus("mandatory")


class _HpnsaSWDriversType_Type(Integer32):
    """Custom type hpnsaSWDriversType based on Integer32"""
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
        *(("diskarraycontroller", 3),
          ("networkinterfacecard", 1),
          ("scsi", 2),
          ("system", 4),
          ("unknown", 0))
    )


_HpnsaSWDriversType_Type.__name__ = "Integer32"
_HpnsaSWDriversType_Object = MibTableColumn
hpnsaSWDriversType = _HpnsaSWDriversType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1, 6),
    _HpnsaSWDriversType_Type()
)
hpnsaSWDriversType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWDriversType.setStatus("mandatory")


class _HpnsaSWDriversVersion_Type(DisplayString):
    """Custom type hpnsaSWDriversVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HpnsaSWDriversVersion_Type.__name__ = "DisplayString"
_HpnsaSWDriversVersion_Object = MibTableColumn
hpnsaSWDriversVersion = _HpnsaSWDriversVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1, 7),
    _HpnsaSWDriversVersion_Type()
)
hpnsaSWDriversVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWDriversVersion.setStatus("mandatory")


class _HpnsaSWDriversDescription_Type(DisplayString):
    """Custom type hpnsaSWDriversDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnsaSWDriversDescription_Type.__name__ = "DisplayString"
_HpnsaSWDriversDescription_Object = MibTableColumn
hpnsaSWDriversDescription = _HpnsaSWDriversDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1, 8),
    _HpnsaSWDriversDescription_Type()
)
hpnsaSWDriversDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWDriversDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSASOFTWARESUBSYSTEM-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaSW": hpnsaSW,
       "hpnsaSWMibRev": hpnsaSWMibRev,
       "hpnsaSWMibRevMajor": hpnsaSWMibRevMajor,
       "hpnsaSWMibRevMinor": hpnsaSWMibRevMinor,
       "hpnsaSWManageability": hpnsaSWManageability,
       "hpnsaSWManageabilityTable": hpnsaSWManageabilityTable,
       "hpnsaSWManageabilityEntry": hpnsaSWManageabilityEntry,
       "hpnsaSWManageabilityIndex": hpnsaSWManageabilityIndex,
       "hpnsaSWManageabilityFileName": hpnsaSWManageabilityFileName,
       "hpnsaSWManageabilityFileSize": hpnsaSWManageabilityFileSize,
       "hpnsaSWManageabilityFileDate": hpnsaSWManageabilityFileDate,
       "hpnsaSWManageabilityState": hpnsaSWManageabilityState,
       "hpnsaSWManageabilityType": hpnsaSWManageabilityType,
       "hpnsaSWManageabilityVersion": hpnsaSWManageabilityVersion,
       "hpnsaSWManageabilityDescription": hpnsaSWManageabilityDescription,
       "hpnsaSWDrivers": hpnsaSWDrivers,
       "hpnsaSWDriversTable": hpnsaSWDriversTable,
       "hpnsaSWDriversEntry": hpnsaSWDriversEntry,
       "hpnsaSWDriversIndex": hpnsaSWDriversIndex,
       "hpnsaSWDriversFileName": hpnsaSWDriversFileName,
       "hpnsaSWDriversFileSize": hpnsaSWDriversFileSize,
       "hpnsaSWDriversFileDate": hpnsaSWDriversFileDate,
       "hpnsaSWDriversState": hpnsaSWDriversState,
       "hpnsaSWDriversType": hpnsaSWDriversType,
       "hpnsaSWDriversVersion": hpnsaSWDriversVersion,
       "hpnsaSWDriversDescription": hpnsaSWDriversDescription}
)
