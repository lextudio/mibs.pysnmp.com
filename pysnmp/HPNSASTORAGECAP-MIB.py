# SNMP MIB module (HPNSASTORAGECAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPNSASTORAGECAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:27 2024
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
_HpnsaStorageCap_ObjectIdentity = ObjectIdentity
hpnsaStorageCap = _HpnsaStorageCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15)
)
_HpnsaSCMibRev_ObjectIdentity = ObjectIdentity
hpnsaSCMibRev = _HpnsaSCMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 1)
)


class _HpnsaSCMibRevMajor_Type(Integer32):
    """Custom type hpnsaSCMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaSCMibRevMajor_Type.__name__ = "Integer32"
_HpnsaSCMibRevMajor_Object = MibScalar
hpnsaSCMibRevMajor = _HpnsaSCMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 1, 1),
    _HpnsaSCMibRevMajor_Type()
)
hpnsaSCMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSCMibRevMajor.setStatus("mandatory")


class _HpnsaSCMibRevMinor_Type(Integer32):
    """Custom type hpnsaSCMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaSCMibRevMinor_Type.__name__ = "Integer32"
_HpnsaSCMibRevMinor_Object = MibScalar
hpnsaSCMibRevMinor = _HpnsaSCMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 1, 2),
    _HpnsaSCMibRevMinor_Type()
)
hpnsaSCMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSCMibRevMinor.setStatus("mandatory")
_HpnsaSCAgent_ObjectIdentity = ObjectIdentity
hpnsaSCAgent = _HpnsaSCAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 2)
)
_HpnsaSCAgentTable_Object = MibTable
hpnsaSCAgentTable = _HpnsaSCAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 2, 1)
)
if mibBuilder.loadTexts:
    hpnsaSCAgentTable.setStatus("mandatory")
_HpnsaSCAgentEntry_Object = MibTableRow
hpnsaSCAgentEntry = _HpnsaSCAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 2, 1, 1)
)
hpnsaSCAgentEntry.setIndexNames(
    (0, "HPNSASTORAGECAP-MIB", "hpnsaSCAgentIndex"),
)
if mibBuilder.loadTexts:
    hpnsaSCAgentEntry.setStatus("mandatory")


class _HpnsaSCAgentIndex_Type(Integer32):
    """Custom type hpnsaSCAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaSCAgentIndex_Type.__name__ = "Integer32"
_HpnsaSCAgentIndex_Object = MibTableColumn
hpnsaSCAgentIndex = _HpnsaSCAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 2, 1, 1, 1),
    _HpnsaSCAgentIndex_Type()
)
hpnsaSCAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSCAgentIndex.setStatus("mandatory")


class _HpnsaSCAgentName_Type(DisplayString):
    """Custom type hpnsaSCAgentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSCAgentName_Type.__name__ = "DisplayString"
_HpnsaSCAgentName_Object = MibTableColumn
hpnsaSCAgentName = _HpnsaSCAgentName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 2, 1, 1, 2),
    _HpnsaSCAgentName_Type()
)
hpnsaSCAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSCAgentName.setStatus("mandatory")


class _HpnsaSCAgentVersion_Type(DisplayString):
    """Custom type hpnsaSCAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HpnsaSCAgentVersion_Type.__name__ = "DisplayString"
_HpnsaSCAgentVersion_Object = MibTableColumn
hpnsaSCAgentVersion = _HpnsaSCAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 2, 1, 1, 3),
    _HpnsaSCAgentVersion_Type()
)
hpnsaSCAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSCAgentVersion.setStatus("mandatory")


class _HpnsaSCAgentDate_Type(OctetString):
    """Custom type hpnsaSCAgentDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnsaSCAgentDate_Type.__name__ = "OctetString"
_HpnsaSCAgentDate_Object = MibTableColumn
hpnsaSCAgentDate = _HpnsaSCAgentDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 2, 1, 1, 4),
    _HpnsaSCAgentDate_Type()
)
hpnsaSCAgentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSCAgentDate.setStatus("mandatory")
_HpnsaSCDrv_ObjectIdentity = ObjectIdentity
hpnsaSCDrv = _HpnsaSCDrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3)
)
_HpnsaSCDrvNumOfDrives_Type = Integer32
_HpnsaSCDrvNumOfDrives_Object = MibScalar
hpnsaSCDrvNumOfDrives = _HpnsaSCDrvNumOfDrives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3, 1),
    _HpnsaSCDrvNumOfDrives_Type()
)
hpnsaSCDrvNumOfDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSCDrvNumOfDrives.setStatus("mandatory")
_HpnsaSCDrvTable_Object = MibTable
hpnsaSCDrvTable = _HpnsaSCDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3, 2)
)
if mibBuilder.loadTexts:
    hpnsaSCDrvTable.setStatus("mandatory")
_HpnsaSCDrvEntry_Object = MibTableRow
hpnsaSCDrvEntry = _HpnsaSCDrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3, 2, 1)
)
hpnsaSCDrvEntry.setIndexNames(
    (0, "HPNSASTORAGECAP-MIB", "hpnsaSCDrvIndex"),
)
if mibBuilder.loadTexts:
    hpnsaSCDrvEntry.setStatus("mandatory")
_HpnsaSCDrvIndex_Type = Integer32
_HpnsaSCDrvIndex_Object = MibTableColumn
hpnsaSCDrvIndex = _HpnsaSCDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3, 2, 1, 1),
    _HpnsaSCDrvIndex_Type()
)
hpnsaSCDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSCDrvIndex.setStatus("mandatory")
_HpnsaSCDrvName_Type = DisplayString
_HpnsaSCDrvName_Object = MibTableColumn
hpnsaSCDrvName = _HpnsaSCDrvName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3, 2, 1, 2),
    _HpnsaSCDrvName_Type()
)
hpnsaSCDrvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSCDrvName.setStatus("mandatory")


class _HpnsaSCDrvTrapsEnabled_Type(Integer32):
    """Custom type hpnsaSCDrvTrapsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HpnsaSCDrvTrapsEnabled_Type.__name__ = "Integer32"
_HpnsaSCDrvTrapsEnabled_Object = MibTableColumn
hpnsaSCDrvTrapsEnabled = _HpnsaSCDrvTrapsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3, 2, 1, 3),
    _HpnsaSCDrvTrapsEnabled_Type()
)
hpnsaSCDrvTrapsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaSCDrvTrapsEnabled.setStatus("mandatory")
_HpnsaSCDrvTrapsPollTime_Type = Integer32
_HpnsaSCDrvTrapsPollTime_Object = MibTableColumn
hpnsaSCDrvTrapsPollTime = _HpnsaSCDrvTrapsPollTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3, 2, 1, 4),
    _HpnsaSCDrvTrapsPollTime_Type()
)
hpnsaSCDrvTrapsPollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaSCDrvTrapsPollTime.setStatus("mandatory")
_HpnsaSCDrvHistSampleTime_Type = Integer32
_HpnsaSCDrvHistSampleTime_Object = MibTableColumn
hpnsaSCDrvHistSampleTime = _HpnsaSCDrvHistSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3, 2, 1, 5),
    _HpnsaSCDrvHistSampleTime_Type()
)
hpnsaSCDrvHistSampleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaSCDrvHistSampleTime.setStatus("mandatory")
_HpnsaSCDrvLoThreshold_Type = Integer32
_HpnsaSCDrvLoThreshold_Object = MibTableColumn
hpnsaSCDrvLoThreshold = _HpnsaSCDrvLoThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3, 2, 1, 6),
    _HpnsaSCDrvLoThreshold_Type()
)
hpnsaSCDrvLoThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaSCDrvLoThreshold.setStatus("mandatory")
_HpnsaSCDrvWarnThreshold_Type = Integer32
_HpnsaSCDrvWarnThreshold_Object = MibTableColumn
hpnsaSCDrvWarnThreshold = _HpnsaSCDrvWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3, 2, 1, 7),
    _HpnsaSCDrvWarnThreshold_Type()
)
hpnsaSCDrvWarnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaSCDrvWarnThreshold.setStatus("mandatory")
_HpnsaSCDrvCritThreshold_Type = Integer32
_HpnsaSCDrvCritThreshold_Object = MibTableColumn
hpnsaSCDrvCritThreshold = _HpnsaSCDrvCritThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3, 2, 1, 8),
    _HpnsaSCDrvCritThreshold_Type()
)
hpnsaSCDrvCritThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaSCDrvCritThreshold.setStatus("mandatory")
_HpnsaSCDrvTotalNumDirEntries_Type = Integer32
_HpnsaSCDrvTotalNumDirEntries_Object = MibTableColumn
hpnsaSCDrvTotalNumDirEntries = _HpnsaSCDrvTotalNumDirEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3, 2, 1, 9),
    _HpnsaSCDrvTotalNumDirEntries_Type()
)
hpnsaSCDrvTotalNumDirEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSCDrvTotalNumDirEntries.setStatus("optional")
_HpnsaSCDrvTotalNumDirEntriesUsed_Type = Integer32
_HpnsaSCDrvTotalNumDirEntriesUsed_Object = MibTableColumn
hpnsaSCDrvTotalNumDirEntriesUsed = _HpnsaSCDrvTotalNumDirEntriesUsed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3, 2, 1, 10),
    _HpnsaSCDrvTotalNumDirEntriesUsed_Type()
)
hpnsaSCDrvTotalNumDirEntriesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSCDrvTotalNumDirEntriesUsed.setStatus("optional")
_HpnsaSCDrvCurrentTotal_Type = Integer32
_HpnsaSCDrvCurrentTotal_Object = MibTableColumn
hpnsaSCDrvCurrentTotal = _HpnsaSCDrvCurrentTotal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3, 2, 1, 11),
    _HpnsaSCDrvCurrentTotal_Type()
)
hpnsaSCDrvCurrentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSCDrvCurrentTotal.setStatus("mandatory")
_HpnsaSCDrvCurrentAvailable_Type = Integer32
_HpnsaSCDrvCurrentAvailable_Object = MibTableColumn
hpnsaSCDrvCurrentAvailable = _HpnsaSCDrvCurrentAvailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3, 2, 1, 12),
    _HpnsaSCDrvCurrentAvailable_Type()
)
hpnsaSCDrvCurrentAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSCDrvCurrentAvailable.setStatus("mandatory")
_HpnsaSCDrvNumOfSamples_Type = Integer32
_HpnsaSCDrvNumOfSamples_Object = MibTableColumn
hpnsaSCDrvNumOfSamples = _HpnsaSCDrvNumOfSamples_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3, 2, 1, 13),
    _HpnsaSCDrvNumOfSamples_Type()
)
hpnsaSCDrvNumOfSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSCDrvNumOfSamples.setStatus("mandatory")
_HpnsaSCDrvClearHist_Type = Integer32
_HpnsaSCDrvClearHist_Object = MibTableColumn
hpnsaSCDrvClearHist = _HpnsaSCDrvClearHist_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 3, 2, 1, 14),
    _HpnsaSCDrvClearHist_Type()
)
hpnsaSCDrvClearHist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaSCDrvClearHist.setStatus("mandatory")
_HpnsaSCHist_ObjectIdentity = ObjectIdentity
hpnsaSCHist = _HpnsaSCHist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 4)
)
_HpnsaSCHistTable_Object = MibTable
hpnsaSCHistTable = _HpnsaSCHistTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 4, 1)
)
if mibBuilder.loadTexts:
    hpnsaSCHistTable.setStatus("mandatory")
_HpnsaSCHistEntry_Object = MibTableRow
hpnsaSCHistEntry = _HpnsaSCHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 4, 1, 1)
)
hpnsaSCHistEntry.setIndexNames(
    (0, "HPNSASTORAGECAP-MIB", "hpnsaSCHistDriveIndex"),
    (0, "HPNSASTORAGECAP-MIB", "hpnsaSCHistIndex"),
)
if mibBuilder.loadTexts:
    hpnsaSCHistEntry.setStatus("mandatory")


class _HpnsaSCHistDriveIndex_Type(Integer32):
    """Custom type hpnsaSCHistDriveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaSCHistDriveIndex_Type.__name__ = "Integer32"
_HpnsaSCHistDriveIndex_Object = MibTableColumn
hpnsaSCHistDriveIndex = _HpnsaSCHistDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 4, 1, 1, 1),
    _HpnsaSCHistDriveIndex_Type()
)
hpnsaSCHistDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSCHistDriveIndex.setStatus("mandatory")


class _HpnsaSCHistIndex_Type(Integer32):
    """Custom type hpnsaSCHistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )


_HpnsaSCHistIndex_Type.__name__ = "Integer32"
_HpnsaSCHistIndex_Object = MibTableColumn
hpnsaSCHistIndex = _HpnsaSCHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 4, 1, 1, 2),
    _HpnsaSCHistIndex_Type()
)
hpnsaSCHistIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSCHistIndex.setStatus("mandatory")


class _HpnsaSCHistSample_Type(OctetString):
    """Custom type hpnsaSCHistSample based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_HpnsaSCHistSample_Type.__name__ = "OctetString"
_HpnsaSCHistSample_Object = MibTableColumn
hpnsaSCHistSample = _HpnsaSCHistSample_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 15, 4, 1, 1, 3),
    _HpnsaSCHistSample_Type()
)
hpnsaSCHistSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSCHistSample.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSASTORAGECAP-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaStorageCap": hpnsaStorageCap,
       "hpnsaSCMibRev": hpnsaSCMibRev,
       "hpnsaSCMibRevMajor": hpnsaSCMibRevMajor,
       "hpnsaSCMibRevMinor": hpnsaSCMibRevMinor,
       "hpnsaSCAgent": hpnsaSCAgent,
       "hpnsaSCAgentTable": hpnsaSCAgentTable,
       "hpnsaSCAgentEntry": hpnsaSCAgentEntry,
       "hpnsaSCAgentIndex": hpnsaSCAgentIndex,
       "hpnsaSCAgentName": hpnsaSCAgentName,
       "hpnsaSCAgentVersion": hpnsaSCAgentVersion,
       "hpnsaSCAgentDate": hpnsaSCAgentDate,
       "hpnsaSCDrv": hpnsaSCDrv,
       "hpnsaSCDrvNumOfDrives": hpnsaSCDrvNumOfDrives,
       "hpnsaSCDrvTable": hpnsaSCDrvTable,
       "hpnsaSCDrvEntry": hpnsaSCDrvEntry,
       "hpnsaSCDrvIndex": hpnsaSCDrvIndex,
       "hpnsaSCDrvName": hpnsaSCDrvName,
       "hpnsaSCDrvTrapsEnabled": hpnsaSCDrvTrapsEnabled,
       "hpnsaSCDrvTrapsPollTime": hpnsaSCDrvTrapsPollTime,
       "hpnsaSCDrvHistSampleTime": hpnsaSCDrvHistSampleTime,
       "hpnsaSCDrvLoThreshold": hpnsaSCDrvLoThreshold,
       "hpnsaSCDrvWarnThreshold": hpnsaSCDrvWarnThreshold,
       "hpnsaSCDrvCritThreshold": hpnsaSCDrvCritThreshold,
       "hpnsaSCDrvTotalNumDirEntries": hpnsaSCDrvTotalNumDirEntries,
       "hpnsaSCDrvTotalNumDirEntriesUsed": hpnsaSCDrvTotalNumDirEntriesUsed,
       "hpnsaSCDrvCurrentTotal": hpnsaSCDrvCurrentTotal,
       "hpnsaSCDrvCurrentAvailable": hpnsaSCDrvCurrentAvailable,
       "hpnsaSCDrvNumOfSamples": hpnsaSCDrvNumOfSamples,
       "hpnsaSCDrvClearHist": hpnsaSCDrvClearHist,
       "hpnsaSCHist": hpnsaSCHist,
       "hpnsaSCHistTable": hpnsaSCHistTable,
       "hpnsaSCHistEntry": hpnsaSCHistEntry,
       "hpnsaSCHistDriveIndex": hpnsaSCHistDriveIndex,
       "hpnsaSCHistIndex": hpnsaSCHistIndex,
       "hpnsaSCHistSample": hpnsaSCHistSample}
)
