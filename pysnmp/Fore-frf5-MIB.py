# SNMP MIB module (Fore-frf5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-frf5-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:21 2024
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

(AtmAddress,
 frameInternetworking) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "AtmAddress",
    "frameInternetworking")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

frf5 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Frf5ConnTable_Object = MibTable
frf5ConnTable = _Frf5ConnTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1)
)
if mibBuilder.loadTexts:
    frf5ConnTable.setStatus("current")
_Frf5ConnEntry_Object = MibTableRow
frf5ConnEntry = _Frf5ConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1)
)
frf5ConnEntry.setIndexNames(
    (0, "Fore-frf5-MIB", "frf5ConnFrServiceIfIndex"),
    (0, "Fore-frf5-MIB", "frf5ConnDlci"),
)
if mibBuilder.loadTexts:
    frf5ConnEntry.setStatus("current")
_Frf5ConnFrServiceIfIndex_Type = InterfaceIndex
_Frf5ConnFrServiceIfIndex_Object = MibTableColumn
frf5ConnFrServiceIfIndex = _Frf5ConnFrServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 1),
    _Frf5ConnFrServiceIfIndex_Type()
)
frf5ConnFrServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5ConnFrServiceIfIndex.setStatus("current")
_Frf5ConnDlci_Type = Integer32
_Frf5ConnDlci_Object = MibTableColumn
frf5ConnDlci = _Frf5ConnDlci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 2),
    _Frf5ConnDlci_Type()
)
frf5ConnDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5ConnDlci.setStatus("current")


class _Frf5ConnFrsscsDlci_Type(Integer32):
    """Custom type frf5ConnFrsscsDlci based on Integer32"""
    defaultValue = 1022


_Frf5ConnFrsscsDlci_Object = MibTableColumn
frf5ConnFrsscsDlci = _Frf5ConnFrsscsDlci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 3),
    _Frf5ConnFrsscsDlci_Type()
)
frf5ConnFrsscsDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf5ConnFrsscsDlci.setStatus("current")
_Frf5ConnFabServiceIfIndex_Type = Integer32
_Frf5ConnFabServiceIfIndex_Object = MibTableColumn
frf5ConnFabServiceIfIndex = _Frf5ConnFabServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 4),
    _Frf5ConnFabServiceIfIndex_Type()
)
frf5ConnFabServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5ConnFabServiceIfIndex.setStatus("current")
_Frf5ConnFabAtmIf_Type = Integer32
_Frf5ConnFabAtmIf_Object = MibTableColumn
frf5ConnFabAtmIf = _Frf5ConnFabAtmIf_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 5),
    _Frf5ConnFabAtmIf_Type()
)
frf5ConnFabAtmIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf5ConnFabAtmIf.setStatus("current")
_Frf5ConnFabVpi_Type = Integer32
_Frf5ConnFabVpi_Object = MibTableColumn
frf5ConnFabVpi = _Frf5ConnFabVpi_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 6),
    _Frf5ConnFabVpi_Type()
)
frf5ConnFabVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf5ConnFabVpi.setStatus("current")
_Frf5ConnFabVci_Type = Integer32
_Frf5ConnFabVci_Object = MibTableColumn
frf5ConnFabVci = _Frf5ConnFabVci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 7),
    _Frf5ConnFabVci_Type()
)
frf5ConnFabVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf5ConnFabVci.setStatus("current")
_Frf5ConnRowStatus_Type = RowStatus
_Frf5ConnRowStatus_Object = MibTableColumn
frf5ConnRowStatus = _Frf5ConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 8),
    _Frf5ConnRowStatus_Type()
)
frf5ConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf5ConnRowStatus.setStatus("current")


class _Frf5ConnProfileEpdPpdIndex_Type(Integer32):
    """Custom type frf5ConnProfileEpdPpdIndex based on Integer32"""
    defaultValue = 0


_Frf5ConnProfileEpdPpdIndex_Object = MibTableColumn
frf5ConnProfileEpdPpdIndex = _Frf5ConnProfileEpdPpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 9),
    _Frf5ConnProfileEpdPpdIndex_Type()
)
frf5ConnProfileEpdPpdIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf5ConnProfileEpdPpdIndex.setStatus("current")


class _Frf5ConnAtmAddrType_Type(Integer32):
    """Custom type frf5ConnAtmAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e164", 2),
          ("nsap", 3),
          ("null", 1))
    )


_Frf5ConnAtmAddrType_Type.__name__ = "Integer32"
_Frf5ConnAtmAddrType_Object = MibTableColumn
frf5ConnAtmAddrType = _Frf5ConnAtmAddrType_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 10),
    _Frf5ConnAtmAddrType_Type()
)
frf5ConnAtmAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf5ConnAtmAddrType.setStatus("current")
_Frf5ConnAtmAddress_Type = AtmAddress
_Frf5ConnAtmAddress_Object = MibTableColumn
frf5ConnAtmAddress = _Frf5ConnAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 11),
    _Frf5ConnAtmAddress_Type()
)
frf5ConnAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf5ConnAtmAddress.setStatus("current")


class _Frf5ConnAtmSubAddrType_Type(Integer32):
    """Custom type frf5ConnAtmSubAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e164", 2),
          ("nsap", 3),
          ("null", 1))
    )


_Frf5ConnAtmSubAddrType_Type.__name__ = "Integer32"
_Frf5ConnAtmSubAddrType_Object = MibTableColumn
frf5ConnAtmSubAddrType = _Frf5ConnAtmSubAddrType_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 12),
    _Frf5ConnAtmSubAddrType_Type()
)
frf5ConnAtmSubAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf5ConnAtmSubAddrType.setStatus("current")
_Frf5ConnAtmSubAddress_Type = AtmAddress
_Frf5ConnAtmSubAddress_Object = MibTableColumn
frf5ConnAtmSubAddress = _Frf5ConnAtmSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 13),
    _Frf5ConnAtmSubAddress_Type()
)
frf5ConnAtmSubAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf5ConnAtmSubAddress.setStatus("current")


class _Frf5ConnFrAddrType_Type(Integer32):
    """Custom type frf5ConnFrAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e164", 2),
          ("null", 1))
    )


_Frf5ConnFrAddrType_Type.__name__ = "Integer32"
_Frf5ConnFrAddrType_Object = MibTableColumn
frf5ConnFrAddrType = _Frf5ConnFrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 14),
    _Frf5ConnFrAddrType_Type()
)
frf5ConnFrAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf5ConnFrAddrType.setStatus("current")
_Frf5ConnFrAddress_Type = AtmAddress
_Frf5ConnFrAddress_Object = MibTableColumn
frf5ConnFrAddress = _Frf5ConnFrAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 15),
    _Frf5ConnFrAddress_Type()
)
frf5ConnFrAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf5ConnFrAddress.setStatus("current")


class _Frf5ConnAdminStatus_Type(Integer32):
    """Custom type frf5ConnAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_Frf5ConnAdminStatus_Type.__name__ = "Integer32"
_Frf5ConnAdminStatus_Object = MibTableColumn
frf5ConnAdminStatus = _Frf5ConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 16),
    _Frf5ConnAdminStatus_Type()
)
frf5ConnAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf5ConnAdminStatus.setStatus("current")


class _Frf5ConnOperStatus_Type(Integer32):
    """Custom type frf5ConnOperStatus based on Integer32"""
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


_Frf5ConnOperStatus_Type.__name__ = "Integer32"
_Frf5ConnOperStatus_Object = MibTableColumn
frf5ConnOperStatus = _Frf5ConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 17),
    _Frf5ConnOperStatus_Type()
)
frf5ConnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5ConnOperStatus.setStatus("current")
_Frf5ConnCreationTime_Type = TimeTicks
_Frf5ConnCreationTime_Object = MibTableColumn
frf5ConnCreationTime = _Frf5ConnCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 18),
    _Frf5ConnCreationTime_Type()
)
frf5ConnCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5ConnCreationTime.setStatus("current")
_Frf5ConnTimeChange_Type = TimeTicks
_Frf5ConnTimeChange_Object = MibTableColumn
frf5ConnTimeChange = _Frf5ConnTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 1, 1, 19),
    _Frf5ConnTimeChange_Type()
)
frf5ConnTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5ConnTimeChange.setStatus("current")
_Frf5extDlcmiTable_Object = MibTable
frf5extDlcmiTable = _Frf5extDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2)
)
if mibBuilder.loadTexts:
    frf5extDlcmiTable.setStatus("current")
_Frf5extDlcmiEntry_Object = MibTableRow
frf5extDlcmiEntry = _Frf5extDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1)
)
frf5extDlcmiEntry.setIndexNames(
    (0, "Fore-frf5-MIB", "frf5extDlmciAtmIf"),
    (0, "Fore-frf5-MIB", "frf5extDlcmiAtmVpi"),
    (0, "Fore-frf5-MIB", "frf5extDlcmiAtmVci"),
)
if mibBuilder.loadTexts:
    frf5extDlcmiEntry.setStatus("current")
_Frf5extDlmciAtmIf_Type = Integer32
_Frf5extDlmciAtmIf_Object = MibTableColumn
frf5extDlmciAtmIf = _Frf5extDlmciAtmIf_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 1),
    _Frf5extDlmciAtmIf_Type()
)
frf5extDlmciAtmIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlmciAtmIf.setStatus("current")
_Frf5extDlcmiAtmVpi_Type = Integer32
_Frf5extDlcmiAtmVpi_Object = MibTableColumn
frf5extDlcmiAtmVpi = _Frf5extDlcmiAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 2),
    _Frf5extDlcmiAtmVpi_Type()
)
frf5extDlcmiAtmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiAtmVpi.setStatus("current")
_Frf5extDlcmiAtmVci_Type = Integer32
_Frf5extDlcmiAtmVci_Object = MibTableColumn
frf5extDlcmiAtmVci = _Frf5extDlcmiAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 3),
    _Frf5extDlcmiAtmVci_Type()
)
frf5extDlcmiAtmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiAtmVci.setStatus("current")


class _Frf5extDlcmiProfileLmiIndex_Type(Integer32):
    """Custom type frf5extDlcmiProfileLmiIndex based on Integer32"""
    defaultValue = 0


_Frf5extDlcmiProfileLmiIndex_Object = MibTableColumn
frf5extDlcmiProfileLmiIndex = _Frf5extDlcmiProfileLmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 4),
    _Frf5extDlcmiProfileLmiIndex_Type()
)
frf5extDlcmiProfileLmiIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frf5extDlcmiProfileLmiIndex.setStatus("current")


class _Frf5extDlcmiProfileFrf5Index_Type(Integer32):
    """Custom type frf5extDlcmiProfileFrf5Index based on Integer32"""
    defaultValue = 0


_Frf5extDlcmiProfileFrf5Index_Object = MibTableColumn
frf5extDlcmiProfileFrf5Index = _Frf5extDlcmiProfileFrf5Index_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 5),
    _Frf5extDlcmiProfileFrf5Index_Type()
)
frf5extDlcmiProfileFrf5Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frf5extDlcmiProfileFrf5Index.setStatus("current")


class _Frf5extDlcmiStatsMonitor_Type(Integer32):
    """Custom type frf5extDlcmiStatsMonitor based on Integer32"""
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


_Frf5extDlcmiStatsMonitor_Type.__name__ = "Integer32"
_Frf5extDlcmiStatsMonitor_Object = MibTableColumn
frf5extDlcmiStatsMonitor = _Frf5extDlcmiStatsMonitor_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 6),
    _Frf5extDlcmiStatsMonitor_Type()
)
frf5extDlcmiStatsMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frf5extDlcmiStatsMonitor.setStatus("current")
_Frf5extDlcmiStatsEnabledTimeStamp_Type = TimeTicks
_Frf5extDlcmiStatsEnabledTimeStamp_Object = MibTableColumn
frf5extDlcmiStatsEnabledTimeStamp = _Frf5extDlcmiStatsEnabledTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 7),
    _Frf5extDlcmiStatsEnabledTimeStamp_Type()
)
frf5extDlcmiStatsEnabledTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiStatsEnabledTimeStamp.setStatus("current")


class _Frf5extDlcmiLmiDlci_Type(Integer32):
    """Custom type frf5extDlcmiLmiDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("q933AnnexA", 0),
          ("stratacom", 1023))
    )


_Frf5extDlcmiLmiDlci_Type.__name__ = "Integer32"
_Frf5extDlcmiLmiDlci_Object = MibTableColumn
frf5extDlcmiLmiDlci = _Frf5extDlcmiLmiDlci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 8),
    _Frf5extDlcmiLmiDlci_Type()
)
frf5extDlcmiLmiDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiDlci.setStatus("current")


class _Frf5extDlcmiLmiFlowControl_Type(Integer32):
    """Custom type frf5extDlcmiLmiFlowControl based on Integer32"""
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


_Frf5extDlcmiLmiFlowControl_Type.__name__ = "Integer32"
_Frf5extDlcmiLmiFlowControl_Object = MibTableColumn
frf5extDlcmiLmiFlowControl = _Frf5extDlcmiLmiFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 9),
    _Frf5extDlcmiLmiFlowControl_Type()
)
frf5extDlcmiLmiFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiFlowControl.setStatus("current")


class _Frf5extDlcmiLmiBandwidthControl_Type(Integer32):
    """Custom type frf5extDlcmiLmiBandwidthControl based on Integer32"""
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


_Frf5extDlcmiLmiBandwidthControl_Type.__name__ = "Integer32"
_Frf5extDlcmiLmiBandwidthControl_Object = MibTableColumn
frf5extDlcmiLmiBandwidthControl = _Frf5extDlcmiLmiBandwidthControl_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 10),
    _Frf5extDlcmiLmiBandwidthControl_Type()
)
frf5extDlcmiLmiBandwidthControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiBandwidthControl.setStatus("current")
_Frf5extDlcmiRxAbortedFrames_Type = Counter32
_Frf5extDlcmiRxAbortedFrames_Object = MibTableColumn
frf5extDlcmiRxAbortedFrames = _Frf5extDlcmiRxAbortedFrames_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 11),
    _Frf5extDlcmiRxAbortedFrames_Type()
)
frf5extDlcmiRxAbortedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiRxAbortedFrames.setStatus("current")
_Frf5extDlcmiRcvCrcErrors_Type = Counter32
_Frf5extDlcmiRcvCrcErrors_Object = MibTableColumn
frf5extDlcmiRcvCrcErrors = _Frf5extDlcmiRcvCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 12),
    _Frf5extDlcmiRcvCrcErrors_Type()
)
frf5extDlcmiRcvCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiRcvCrcErrors.setStatus("current")
_Frf5extDlcmiRcvShortFrames_Type = Counter32
_Frf5extDlcmiRcvShortFrames_Object = MibTableColumn
frf5extDlcmiRcvShortFrames = _Frf5extDlcmiRcvShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 13),
    _Frf5extDlcmiRcvShortFrames_Type()
)
frf5extDlcmiRcvShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiRcvShortFrames.setStatus("current")
_Frf5extDlcmiRcvLongFrames_Type = Counter32
_Frf5extDlcmiRcvLongFrames_Object = MibTableColumn
frf5extDlcmiRcvLongFrames = _Frf5extDlcmiRcvLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 14),
    _Frf5extDlcmiRcvLongFrames_Type()
)
frf5extDlcmiRcvLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiRcvLongFrames.setStatus("current")
_Frf5extDlcmiRcvInvalidDLCI_Type = Counter32
_Frf5extDlcmiRcvInvalidDLCI_Object = MibTableColumn
frf5extDlcmiRcvInvalidDLCI = _Frf5extDlcmiRcvInvalidDLCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 15),
    _Frf5extDlcmiRcvInvalidDLCI_Type()
)
frf5extDlcmiRcvInvalidDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiRcvInvalidDLCI.setStatus("current")
_Frf5extDlcmiRcvUnknownErrs_Type = Counter32
_Frf5extDlcmiRcvUnknownErrs_Object = MibTableColumn
frf5extDlcmiRcvUnknownErrs = _Frf5extDlcmiRcvUnknownErrs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 16),
    _Frf5extDlcmiRcvUnknownErrs_Type()
)
frf5extDlcmiRcvUnknownErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiRcvUnknownErrs.setStatus("current")
_Frf5extDlcmiLmiTxStatusResponses_Type = Counter32
_Frf5extDlcmiLmiTxStatusResponses_Object = MibTableColumn
frf5extDlcmiLmiTxStatusResponses = _Frf5extDlcmiLmiTxStatusResponses_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 17),
    _Frf5extDlcmiLmiTxStatusResponses_Type()
)
frf5extDlcmiLmiTxStatusResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiTxStatusResponses.setStatus("current")
_Frf5extDlcmiLmiTxFullStatusResponses_Type = Counter32
_Frf5extDlcmiLmiTxFullStatusResponses_Object = MibTableColumn
frf5extDlcmiLmiTxFullStatusResponses = _Frf5extDlcmiLmiTxFullStatusResponses_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 18),
    _Frf5extDlcmiLmiTxFullStatusResponses_Type()
)
frf5extDlcmiLmiTxFullStatusResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiTxFullStatusResponses.setStatus("current")
_Frf5extDlcmiLmiTxStatusEnquiries_Type = Counter32
_Frf5extDlcmiLmiTxStatusEnquiries_Object = MibTableColumn
frf5extDlcmiLmiTxStatusEnquiries = _Frf5extDlcmiLmiTxStatusEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 19),
    _Frf5extDlcmiLmiTxStatusEnquiries_Type()
)
frf5extDlcmiLmiTxStatusEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiTxStatusEnquiries.setStatus("current")
_Frf5extDlcmiLmiTxFullStatusEnquiries_Type = Counter32
_Frf5extDlcmiLmiTxFullStatusEnquiries_Object = MibTableColumn
frf5extDlcmiLmiTxFullStatusEnquiries = _Frf5extDlcmiLmiTxFullStatusEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 20),
    _Frf5extDlcmiLmiTxFullStatusEnquiries_Type()
)
frf5extDlcmiLmiTxFullStatusEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiTxFullStatusEnquiries.setStatus("current")
_Frf5extDlcmiLmiRxStatusResponses_Type = Counter32
_Frf5extDlcmiLmiRxStatusResponses_Object = MibTableColumn
frf5extDlcmiLmiRxStatusResponses = _Frf5extDlcmiLmiRxStatusResponses_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 21),
    _Frf5extDlcmiLmiRxStatusResponses_Type()
)
frf5extDlcmiLmiRxStatusResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiRxStatusResponses.setStatus("current")
_Frf5extDlcmiLmiRxFullStatusResponses_Type = Counter32
_Frf5extDlcmiLmiRxFullStatusResponses_Object = MibTableColumn
frf5extDlcmiLmiRxFullStatusResponses = _Frf5extDlcmiLmiRxFullStatusResponses_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 22),
    _Frf5extDlcmiLmiRxFullStatusResponses_Type()
)
frf5extDlcmiLmiRxFullStatusResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiRxFullStatusResponses.setStatus("current")
_Frf5extDlcmiLmiRxStatusEnquiries_Type = Counter32
_Frf5extDlcmiLmiRxStatusEnquiries_Object = MibTableColumn
frf5extDlcmiLmiRxStatusEnquiries = _Frf5extDlcmiLmiRxStatusEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 23),
    _Frf5extDlcmiLmiRxStatusEnquiries_Type()
)
frf5extDlcmiLmiRxStatusEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiRxStatusEnquiries.setStatus("current")
_Frf5extDlcmiLmiRxFullStatusEnquiries_Type = Counter32
_Frf5extDlcmiLmiRxFullStatusEnquiries_Object = MibTableColumn
frf5extDlcmiLmiRxFullStatusEnquiries = _Frf5extDlcmiLmiRxFullStatusEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 24),
    _Frf5extDlcmiLmiRxFullStatusEnquiries_Type()
)
frf5extDlcmiLmiRxFullStatusEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiRxFullStatusEnquiries.setStatus("current")
_Frf5extDlcmiLmiUnknownMessagesRcvd_Type = Counter32
_Frf5extDlcmiLmiUnknownMessagesRcvd_Object = MibTableColumn
frf5extDlcmiLmiUnknownMessagesRcvd = _Frf5extDlcmiLmiUnknownMessagesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 25),
    _Frf5extDlcmiLmiUnknownMessagesRcvd_Type()
)
frf5extDlcmiLmiUnknownMessagesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiUnknownMessagesRcvd.setStatus("current")
_Frf5extDlcmiLmiStatusLostSequences_Type = Counter32
_Frf5extDlcmiLmiStatusLostSequences_Object = MibTableColumn
frf5extDlcmiLmiStatusLostSequences = _Frf5extDlcmiLmiStatusLostSequences_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 26),
    _Frf5extDlcmiLmiStatusLostSequences_Type()
)
frf5extDlcmiLmiStatusLostSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiStatusLostSequences.setStatus("current")
_Frf5extDlcmiLmiStatusEnqLostSequences_Type = Counter32
_Frf5extDlcmiLmiStatusEnqLostSequences_Object = MibTableColumn
frf5extDlcmiLmiStatusEnqLostSequences = _Frf5extDlcmiLmiStatusEnqLostSequences_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 27),
    _Frf5extDlcmiLmiStatusEnqLostSequences_Type()
)
frf5extDlcmiLmiStatusEnqLostSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiStatusEnqLostSequences.setStatus("current")
_Frf5extDlcmiLmiMissingStatEnquiries_Type = Counter32
_Frf5extDlcmiLmiMissingStatEnquiries_Object = MibTableColumn
frf5extDlcmiLmiMissingStatEnquiries = _Frf5extDlcmiLmiMissingStatEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 28),
    _Frf5extDlcmiLmiMissingStatEnquiries_Type()
)
frf5extDlcmiLmiMissingStatEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiMissingStatEnquiries.setStatus("current")
_Frf5extDlcmiLmiUnexpectedPVCStatMsg_Type = Counter32
_Frf5extDlcmiLmiUnexpectedPVCStatMsg_Object = MibTableColumn
frf5extDlcmiLmiUnexpectedPVCStatMsg = _Frf5extDlcmiLmiUnexpectedPVCStatMsg_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 29),
    _Frf5extDlcmiLmiUnexpectedPVCStatMsg_Type()
)
frf5extDlcmiLmiUnexpectedPVCStatMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiUnexpectedPVCStatMsg.setStatus("current")
_Frf5extDlcmiLmiUnexpectedDLCI_Type = Counter32
_Frf5extDlcmiLmiUnexpectedDLCI_Object = MibTableColumn
frf5extDlcmiLmiUnexpectedDLCI = _Frf5extDlcmiLmiUnexpectedDLCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 30),
    _Frf5extDlcmiLmiUnexpectedDLCI_Type()
)
frf5extDlcmiLmiUnexpectedDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiUnexpectedDLCI.setStatus("current")
_Frf5extDlcmiLmiStatEnqRatePlus_Type = Counter32
_Frf5extDlcmiLmiStatEnqRatePlus_Object = MibTableColumn
frf5extDlcmiLmiStatEnqRatePlus = _Frf5extDlcmiLmiStatEnqRatePlus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 31),
    _Frf5extDlcmiLmiStatEnqRatePlus_Type()
)
frf5extDlcmiLmiStatEnqRatePlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiStatEnqRatePlus.setStatus("current")
_Frf5extDlcmiLmiInvInfoFrame_Type = Counter32
_Frf5extDlcmiLmiInvInfoFrame_Object = MibTableColumn
frf5extDlcmiLmiInvInfoFrame = _Frf5extDlcmiLmiInvInfoFrame_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 32),
    _Frf5extDlcmiLmiInvInfoFrame_Type()
)
frf5extDlcmiLmiInvInfoFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiInvInfoFrame.setStatus("current")
_Frf5extDlcmiLmiInvFrameHdr_Type = Counter32
_Frf5extDlcmiLmiInvFrameHdr_Object = MibTableColumn
frf5extDlcmiLmiInvFrameHdr = _Frf5extDlcmiLmiInvFrameHdr_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 33),
    _Frf5extDlcmiLmiInvFrameHdr_Type()
)
frf5extDlcmiLmiInvFrameHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiInvFrameHdr.setStatus("current")
_Frf5extDlcmiLmiNoIERepType_Type = Counter32
_Frf5extDlcmiLmiNoIERepType_Object = MibTableColumn
frf5extDlcmiLmiNoIERepType = _Frf5extDlcmiLmiNoIERepType_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 34),
    _Frf5extDlcmiLmiNoIERepType_Type()
)
frf5extDlcmiLmiNoIERepType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiNoIERepType.setStatus("current")
_Frf5extDlcmiLmiNoIEKeepAlive_Type = Counter32
_Frf5extDlcmiLmiNoIEKeepAlive_Object = MibTableColumn
frf5extDlcmiLmiNoIEKeepAlive = _Frf5extDlcmiLmiNoIEKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 35),
    _Frf5extDlcmiLmiNoIEKeepAlive_Type()
)
frf5extDlcmiLmiNoIEKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiNoIEKeepAlive.setStatus("current")
_Frf5extDlcmiLmiMissingResponses_Type = Counter32
_Frf5extDlcmiLmiMissingResponses_Object = MibTableColumn
frf5extDlcmiLmiMissingResponses = _Frf5extDlcmiLmiMissingResponses_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 36),
    _Frf5extDlcmiLmiMissingResponses_Type()
)
frf5extDlcmiLmiMissingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiMissingResponses.setStatus("current")
_Frf5extDlcmiLmiUnsuppIERcvd_Type = Counter32
_Frf5extDlcmiLmiUnsuppIERcvd_Object = MibTableColumn
frf5extDlcmiLmiUnsuppIERcvd = _Frf5extDlcmiLmiUnsuppIERcvd_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 37),
    _Frf5extDlcmiLmiUnsuppIERcvd_Type()
)
frf5extDlcmiLmiUnsuppIERcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiLmiUnsuppIERcvd.setStatus("current")
_Frf5extDlcmiDlcis_Type = Counter32
_Frf5extDlcmiDlcis_Object = MibTableColumn
frf5extDlcmiDlcis = _Frf5extDlcmiDlcis_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 38),
    _Frf5extDlcmiDlcis_Type()
)
frf5extDlcmiDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiDlcis.setStatus("current")
_Frf5extDlcmiUserLinkRelErrors_Type = Counter32
_Frf5extDlcmiUserLinkRelErrors_Object = MibTableColumn
frf5extDlcmiUserLinkRelErrors = _Frf5extDlcmiUserLinkRelErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 39),
    _Frf5extDlcmiUserLinkRelErrors_Type()
)
frf5extDlcmiUserLinkRelErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiUserLinkRelErrors.setStatus("current")
_Frf5extDlcmiUserProtErrors_Type = Counter32
_Frf5extDlcmiUserProtErrors_Object = MibTableColumn
frf5extDlcmiUserProtErrors = _Frf5extDlcmiUserProtErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 40),
    _Frf5extDlcmiUserProtErrors_Type()
)
frf5extDlcmiUserProtErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiUserProtErrors.setStatus("current")
_Frf5extDlcmiUserChanInactive_Type = Counter32
_Frf5extDlcmiUserChanInactive_Object = MibTableColumn
frf5extDlcmiUserChanInactive = _Frf5extDlcmiUserChanInactive_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 41),
    _Frf5extDlcmiUserChanInactive_Type()
)
frf5extDlcmiUserChanInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiUserChanInactive.setStatus("current")
_Frf5extDlcmiNetLinkRelErrors_Type = Counter32
_Frf5extDlcmiNetLinkRelErrors_Object = MibTableColumn
frf5extDlcmiNetLinkRelErrors = _Frf5extDlcmiNetLinkRelErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 42),
    _Frf5extDlcmiNetLinkRelErrors_Type()
)
frf5extDlcmiNetLinkRelErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiNetLinkRelErrors.setStatus("current")
_Frf5extDlcmiNetProtErrors_Type = Counter32
_Frf5extDlcmiNetProtErrors_Object = MibTableColumn
frf5extDlcmiNetProtErrors = _Frf5extDlcmiNetProtErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 43),
    _Frf5extDlcmiNetProtErrors_Type()
)
frf5extDlcmiNetProtErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiNetProtErrors.setStatus("current")
_Frf5extDlcmiNetChanInactive_Type = Counter32
_Frf5extDlcmiNetChanInactive_Object = MibTableColumn
frf5extDlcmiNetChanInactive = _Frf5extDlcmiNetChanInactive_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 44),
    _Frf5extDlcmiNetChanInactive_Type()
)
frf5extDlcmiNetChanInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiNetChanInactive.setStatus("current")
_Frf5extDlcmiRootService_Type = Integer32
_Frf5extDlcmiRootService_Object = MibTableColumn
frf5extDlcmiRootService = _Frf5extDlcmiRootService_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 45),
    _Frf5extDlcmiRootService_Type()
)
frf5extDlcmiRootService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiRootService.setStatus("current")
_Frf5extDlcmiRootDlci_Type = Integer32
_Frf5extDlcmiRootDlci_Object = MibTableColumn
frf5extDlcmiRootDlci = _Frf5extDlcmiRootDlci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 7, 2, 1, 46),
    _Frf5extDlcmiRootDlci_Type()
)
frf5extDlcmiRootDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf5extDlcmiRootDlci.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-frf5-MIB",
    **{"frf5": frf5,
       "frf5ConnTable": frf5ConnTable,
       "frf5ConnEntry": frf5ConnEntry,
       "frf5ConnFrServiceIfIndex": frf5ConnFrServiceIfIndex,
       "frf5ConnDlci": frf5ConnDlci,
       "frf5ConnFrsscsDlci": frf5ConnFrsscsDlci,
       "frf5ConnFabServiceIfIndex": frf5ConnFabServiceIfIndex,
       "frf5ConnFabAtmIf": frf5ConnFabAtmIf,
       "frf5ConnFabVpi": frf5ConnFabVpi,
       "frf5ConnFabVci": frf5ConnFabVci,
       "frf5ConnRowStatus": frf5ConnRowStatus,
       "frf5ConnProfileEpdPpdIndex": frf5ConnProfileEpdPpdIndex,
       "frf5ConnAtmAddrType": frf5ConnAtmAddrType,
       "frf5ConnAtmAddress": frf5ConnAtmAddress,
       "frf5ConnAtmSubAddrType": frf5ConnAtmSubAddrType,
       "frf5ConnAtmSubAddress": frf5ConnAtmSubAddress,
       "frf5ConnFrAddrType": frf5ConnFrAddrType,
       "frf5ConnFrAddress": frf5ConnFrAddress,
       "frf5ConnAdminStatus": frf5ConnAdminStatus,
       "frf5ConnOperStatus": frf5ConnOperStatus,
       "frf5ConnCreationTime": frf5ConnCreationTime,
       "frf5ConnTimeChange": frf5ConnTimeChange,
       "frf5extDlcmiTable": frf5extDlcmiTable,
       "frf5extDlcmiEntry": frf5extDlcmiEntry,
       "frf5extDlmciAtmIf": frf5extDlmciAtmIf,
       "frf5extDlcmiAtmVpi": frf5extDlcmiAtmVpi,
       "frf5extDlcmiAtmVci": frf5extDlcmiAtmVci,
       "frf5extDlcmiProfileLmiIndex": frf5extDlcmiProfileLmiIndex,
       "frf5extDlcmiProfileFrf5Index": frf5extDlcmiProfileFrf5Index,
       "frf5extDlcmiStatsMonitor": frf5extDlcmiStatsMonitor,
       "frf5extDlcmiStatsEnabledTimeStamp": frf5extDlcmiStatsEnabledTimeStamp,
       "frf5extDlcmiLmiDlci": frf5extDlcmiLmiDlci,
       "frf5extDlcmiLmiFlowControl": frf5extDlcmiLmiFlowControl,
       "frf5extDlcmiLmiBandwidthControl": frf5extDlcmiLmiBandwidthControl,
       "frf5extDlcmiRxAbortedFrames": frf5extDlcmiRxAbortedFrames,
       "frf5extDlcmiRcvCrcErrors": frf5extDlcmiRcvCrcErrors,
       "frf5extDlcmiRcvShortFrames": frf5extDlcmiRcvShortFrames,
       "frf5extDlcmiRcvLongFrames": frf5extDlcmiRcvLongFrames,
       "frf5extDlcmiRcvInvalidDLCI": frf5extDlcmiRcvInvalidDLCI,
       "frf5extDlcmiRcvUnknownErrs": frf5extDlcmiRcvUnknownErrs,
       "frf5extDlcmiLmiTxStatusResponses": frf5extDlcmiLmiTxStatusResponses,
       "frf5extDlcmiLmiTxFullStatusResponses": frf5extDlcmiLmiTxFullStatusResponses,
       "frf5extDlcmiLmiTxStatusEnquiries": frf5extDlcmiLmiTxStatusEnquiries,
       "frf5extDlcmiLmiTxFullStatusEnquiries": frf5extDlcmiLmiTxFullStatusEnquiries,
       "frf5extDlcmiLmiRxStatusResponses": frf5extDlcmiLmiRxStatusResponses,
       "frf5extDlcmiLmiRxFullStatusResponses": frf5extDlcmiLmiRxFullStatusResponses,
       "frf5extDlcmiLmiRxStatusEnquiries": frf5extDlcmiLmiRxStatusEnquiries,
       "frf5extDlcmiLmiRxFullStatusEnquiries": frf5extDlcmiLmiRxFullStatusEnquiries,
       "frf5extDlcmiLmiUnknownMessagesRcvd": frf5extDlcmiLmiUnknownMessagesRcvd,
       "frf5extDlcmiLmiStatusLostSequences": frf5extDlcmiLmiStatusLostSequences,
       "frf5extDlcmiLmiStatusEnqLostSequences": frf5extDlcmiLmiStatusEnqLostSequences,
       "frf5extDlcmiLmiMissingStatEnquiries": frf5extDlcmiLmiMissingStatEnquiries,
       "frf5extDlcmiLmiUnexpectedPVCStatMsg": frf5extDlcmiLmiUnexpectedPVCStatMsg,
       "frf5extDlcmiLmiUnexpectedDLCI": frf5extDlcmiLmiUnexpectedDLCI,
       "frf5extDlcmiLmiStatEnqRatePlus": frf5extDlcmiLmiStatEnqRatePlus,
       "frf5extDlcmiLmiInvInfoFrame": frf5extDlcmiLmiInvInfoFrame,
       "frf5extDlcmiLmiInvFrameHdr": frf5extDlcmiLmiInvFrameHdr,
       "frf5extDlcmiLmiNoIERepType": frf5extDlcmiLmiNoIERepType,
       "frf5extDlcmiLmiNoIEKeepAlive": frf5extDlcmiLmiNoIEKeepAlive,
       "frf5extDlcmiLmiMissingResponses": frf5extDlcmiLmiMissingResponses,
       "frf5extDlcmiLmiUnsuppIERcvd": frf5extDlcmiLmiUnsuppIERcvd,
       "frf5extDlcmiDlcis": frf5extDlcmiDlcis,
       "frf5extDlcmiUserLinkRelErrors": frf5extDlcmiUserLinkRelErrors,
       "frf5extDlcmiUserProtErrors": frf5extDlcmiUserProtErrors,
       "frf5extDlcmiUserChanInactive": frf5extDlcmiUserChanInactive,
       "frf5extDlcmiNetLinkRelErrors": frf5extDlcmiNetLinkRelErrors,
       "frf5extDlcmiNetProtErrors": frf5extDlcmiNetProtErrors,
       "frf5extDlcmiNetChanInactive": frf5extDlcmiNetChanInactive,
       "frf5extDlcmiRootService": frf5extDlcmiRootService,
       "frf5extDlcmiRootDlci": frf5extDlcmiRootDlci}
)
