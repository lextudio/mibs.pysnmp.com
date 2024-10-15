# SNMP MIB module (Fore-frf8-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-frf8-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:22 2024
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
 atmSwitch,
 frameInternetworking) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "AtmAddress",
    "atmSwitch",
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

foreFrf8Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Frf8ConnTable_Object = MibTable
frf8ConnTable = _Frf8ConnTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1)
)
if mibBuilder.loadTexts:
    frf8ConnTable.setStatus("current")
_Frf8ConnEntry_Object = MibTableRow
frf8ConnEntry = _Frf8ConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1)
)
frf8ConnEntry.setIndexNames(
    (0, "Fore-frf8-MIB", "frf8ConnFrServiceIfIndex"),
    (0, "Fore-frf8-MIB", "frf8ConnDlci"),
)
if mibBuilder.loadTexts:
    frf8ConnEntry.setStatus("current")
_Frf8ConnFrServiceIfIndex_Type = InterfaceIndex
_Frf8ConnFrServiceIfIndex_Object = MibTableColumn
frf8ConnFrServiceIfIndex = _Frf8ConnFrServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 1),
    _Frf8ConnFrServiceIfIndex_Type()
)
frf8ConnFrServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ConnFrServiceIfIndex.setStatus("current")
_Frf8ConnDlci_Type = Integer32
_Frf8ConnDlci_Object = MibTableColumn
frf8ConnDlci = _Frf8ConnDlci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 2),
    _Frf8ConnDlci_Type()
)
frf8ConnDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ConnDlci.setStatus("current")
_Frf8ConnFabServiceIfIndex_Type = InterfaceIndex
_Frf8ConnFabServiceIfIndex_Object = MibTableColumn
frf8ConnFabServiceIfIndex = _Frf8ConnFabServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 3),
    _Frf8ConnFabServiceIfIndex_Type()
)
frf8ConnFabServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ConnFabServiceIfIndex.setStatus("current")
_Frf8ConnFabVpi_Type = Integer32
_Frf8ConnFabVpi_Object = MibTableColumn
frf8ConnFabVpi = _Frf8ConnFabVpi_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 4),
    _Frf8ConnFabVpi_Type()
)
frf8ConnFabVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ConnFabVpi.setStatus("current")
_Frf8ConnFabVci_Type = Integer32
_Frf8ConnFabVci_Object = MibTableColumn
frf8ConnFabVci = _Frf8ConnFabVci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 5),
    _Frf8ConnFabVci_Type()
)
frf8ConnFabVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ConnFabVci.setStatus("current")
_Frf8ConnRowStatus_Type = RowStatus
_Frf8ConnRowStatus_Object = MibTableColumn
frf8ConnRowStatus = _Frf8ConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 6),
    _Frf8ConnRowStatus_Type()
)
frf8ConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf8ConnRowStatus.setStatus("current")
_Frf8ConnProfileFrf8Index_Type = Integer32
_Frf8ConnProfileFrf8Index_Object = MibTableColumn
frf8ConnProfileFrf8Index = _Frf8ConnProfileFrf8Index_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 7),
    _Frf8ConnProfileFrf8Index_Type()
)
frf8ConnProfileFrf8Index.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf8ConnProfileFrf8Index.setStatus("current")
_Frf8ConnProfileEpdPpdIndex_Type = Integer32
_Frf8ConnProfileEpdPpdIndex_Object = MibTableColumn
frf8ConnProfileEpdPpdIndex = _Frf8ConnProfileEpdPpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 8),
    _Frf8ConnProfileEpdPpdIndex_Type()
)
frf8ConnProfileEpdPpdIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf8ConnProfileEpdPpdIndex.setStatus("current")


class _Frf8ConnAtmAddrType_Type(Integer32):
    """Custom type frf8ConnAtmAddrType based on Integer32"""
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


_Frf8ConnAtmAddrType_Type.__name__ = "Integer32"
_Frf8ConnAtmAddrType_Object = MibTableColumn
frf8ConnAtmAddrType = _Frf8ConnAtmAddrType_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 9),
    _Frf8ConnAtmAddrType_Type()
)
frf8ConnAtmAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf8ConnAtmAddrType.setStatus("current")
_Frf8ConnAtmAddress_Type = AtmAddress
_Frf8ConnAtmAddress_Object = MibTableColumn
frf8ConnAtmAddress = _Frf8ConnAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 10),
    _Frf8ConnAtmAddress_Type()
)
frf8ConnAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf8ConnAtmAddress.setStatus("current")


class _Frf8ConnAtmSubAddrType_Type(Integer32):
    """Custom type frf8ConnAtmSubAddrType based on Integer32"""
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


_Frf8ConnAtmSubAddrType_Type.__name__ = "Integer32"
_Frf8ConnAtmSubAddrType_Object = MibTableColumn
frf8ConnAtmSubAddrType = _Frf8ConnAtmSubAddrType_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 11),
    _Frf8ConnAtmSubAddrType_Type()
)
frf8ConnAtmSubAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf8ConnAtmSubAddrType.setStatus("current")
_Frf8ConnAtmSubAddress_Type = AtmAddress
_Frf8ConnAtmSubAddress_Object = MibTableColumn
frf8ConnAtmSubAddress = _Frf8ConnAtmSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 12),
    _Frf8ConnAtmSubAddress_Type()
)
frf8ConnAtmSubAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf8ConnAtmSubAddress.setStatus("current")


class _Frf8ConnFrAddrType_Type(Integer32):
    """Custom type frf8ConnFrAddrType based on Integer32"""
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


_Frf8ConnFrAddrType_Type.__name__ = "Integer32"
_Frf8ConnFrAddrType_Object = MibTableColumn
frf8ConnFrAddrType = _Frf8ConnFrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 13),
    _Frf8ConnFrAddrType_Type()
)
frf8ConnFrAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf8ConnFrAddrType.setStatus("current")
_Frf8ConnFrAddress_Type = AtmAddress
_Frf8ConnFrAddress_Object = MibTableColumn
frf8ConnFrAddress = _Frf8ConnFrAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 14),
    _Frf8ConnFrAddress_Type()
)
frf8ConnFrAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf8ConnFrAddress.setStatus("current")


class _Frf8ConnAdminStatus_Type(Integer32):
    """Custom type frf8ConnAdminStatus based on Integer32"""
    defaultValue = 2

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


_Frf8ConnAdminStatus_Type.__name__ = "Integer32"
_Frf8ConnAdminStatus_Object = MibTableColumn
frf8ConnAdminStatus = _Frf8ConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 15),
    _Frf8ConnAdminStatus_Type()
)
frf8ConnAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frf8ConnAdminStatus.setStatus("current")


class _Frf8ConnOperStatus_Type(Integer32):
    """Custom type frf8ConnOperStatus based on Integer32"""
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


_Frf8ConnOperStatus_Type.__name__ = "Integer32"
_Frf8ConnOperStatus_Object = MibTableColumn
frf8ConnOperStatus = _Frf8ConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 16),
    _Frf8ConnOperStatus_Type()
)
frf8ConnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ConnOperStatus.setStatus("current")
_Frf8ConnCreationTime_Type = TimeTicks
_Frf8ConnCreationTime_Object = MibTableColumn
frf8ConnCreationTime = _Frf8ConnCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 17),
    _Frf8ConnCreationTime_Type()
)
frf8ConnCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ConnCreationTime.setStatus("current")
_Frf8ConnTimeChange_Type = TimeTicks
_Frf8ConnTimeChange_Object = MibTableColumn
frf8ConnTimeChange = _Frf8ConnTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 18),
    _Frf8ConnTimeChange_Type()
)
frf8ConnTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ConnTimeChange.setStatus("current")


class _Frf8ConnPVCAlarmReason_Type(Integer32):
    """Custom type frf8ConnPVCAlarmReason based on Integer32"""
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
        *(("aisAlarmed", 4),
          ("aisClear", 5),
          ("frAlarmed", 2),
          ("frClear", 3),
          ("nodefect", 1),
          ("rdiAlarmed", 6),
          ("rdiClear", 7))
    )


_Frf8ConnPVCAlarmReason_Type.__name__ = "Integer32"
_Frf8ConnPVCAlarmReason_Object = MibTableColumn
frf8ConnPVCAlarmReason = _Frf8ConnPVCAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 19),
    _Frf8ConnPVCAlarmReason_Type()
)
frf8ConnPVCAlarmReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ConnPVCAlarmReason.setStatus("current")
_Frf8ConnAtmToFrPDUDiscards_Type = Counter32
_Frf8ConnAtmToFrPDUDiscards_Object = MibTableColumn
frf8ConnAtmToFrPDUDiscards = _Frf8ConnAtmToFrPDUDiscards_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 20),
    _Frf8ConnAtmToFrPDUDiscards_Type()
)
frf8ConnAtmToFrPDUDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ConnAtmToFrPDUDiscards.setStatus("current")
_Frf8ConnFrToAtmPDUDiscards_Type = Counter32
_Frf8ConnFrToAtmPDUDiscards_Object = MibTableColumn
frf8ConnFrToAtmPDUDiscards = _Frf8ConnFrToAtmPDUDiscards_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 21),
    _Frf8ConnFrToAtmPDUDiscards_Type()
)
frf8ConnFrToAtmPDUDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ConnFrToAtmPDUDiscards.setStatus("current")
_Frf8ConnAtmToFrUnkProts_Type = Counter32
_Frf8ConnAtmToFrUnkProts_Object = MibTableColumn
frf8ConnAtmToFrUnkProts = _Frf8ConnAtmToFrUnkProts_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 22),
    _Frf8ConnAtmToFrUnkProts_Type()
)
frf8ConnAtmToFrUnkProts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ConnAtmToFrUnkProts.setStatus("current")
_Frf8ConnFrToAtmUnkProts_Type = Counter32
_Frf8ConnFrToAtmUnkProts_Object = MibTableColumn
frf8ConnFrToAtmUnkProts = _Frf8ConnFrToAtmUnkProts_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 23),
    _Frf8ConnFrToAtmUnkProts_Type()
)
frf8ConnFrToAtmUnkProts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ConnFrToAtmUnkProts.setStatus("current")
_Frf8ConnAtmToFrArpNakDiscards_Type = Counter32
_Frf8ConnAtmToFrArpNakDiscards_Object = MibTableColumn
frf8ConnAtmToFrArpNakDiscards = _Frf8ConnAtmToFrArpNakDiscards_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 1, 1, 24),
    _Frf8ConnAtmToFrArpNakDiscards_Type()
)
frf8ConnAtmToFrArpNakDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ConnAtmToFrArpNakDiscards.setStatus("current")
_Frf8ProtTable_Object = MibTable
frf8ProtTable = _Frf8ProtTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 2)
)
if mibBuilder.loadTexts:
    frf8ProtTable.setStatus("current")
_Frf8ProtEntry_Object = MibTableRow
frf8ProtEntry = _Frf8ProtEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 2, 1)
)
frf8ProtEntry.setIndexNames(
    (0, "Fore-frf8-MIB", "frf8ProtServiceIfIndex"),
    (0, "Fore-frf8-MIB", "frf8ProtDlci"),
    (0, "Fore-frf8-MIB", "frf8ProtProtocol"),
)
if mibBuilder.loadTexts:
    frf8ProtEntry.setStatus("current")
_Frf8ProtServiceIfIndex_Type = InterfaceIndex
_Frf8ProtServiceIfIndex_Object = MibTableColumn
frf8ProtServiceIfIndex = _Frf8ProtServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 2, 1, 1),
    _Frf8ProtServiceIfIndex_Type()
)
frf8ProtServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ProtServiceIfIndex.setStatus("current")
_Frf8ProtDlci_Type = Integer32
_Frf8ProtDlci_Object = MibTableColumn
frf8ProtDlci = _Frf8ProtDlci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 2, 1, 2),
    _Frf8ProtDlci_Type()
)
frf8ProtDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ProtDlci.setStatus("current")


class _Frf8ProtProtocol_Type(Integer32):
    """Custom type frf8ProtProtocol based on Integer32"""
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
        *(("arp", 6),
          ("fddi", 9),
          ("fddiwithfcs", 10),
          ("ip", 5),
          ("ipx", 7),
          ("prot8023", 2),
          ("prot8023withfcs", 1),
          ("prot8025", 4),
          ("prot8025withfcs", 3),
          ("prot8026", 12),
          ("routediso", 13),
          ("sna", 8),
          ("x25x75", 11))
    )


_Frf8ProtProtocol_Type.__name__ = "Integer32"
_Frf8ProtProtocol_Object = MibTableColumn
frf8ProtProtocol = _Frf8ProtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 2, 1, 3),
    _Frf8ProtProtocol_Type()
)
frf8ProtProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ProtProtocol.setStatus("current")
_Frf8ProtAtmToFrPdus_Type = Counter32
_Frf8ProtAtmToFrPdus_Object = MibTableColumn
frf8ProtAtmToFrPdus = _Frf8ProtAtmToFrPdus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 2, 1, 4),
    _Frf8ProtAtmToFrPdus_Type()
)
frf8ProtAtmToFrPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ProtAtmToFrPdus.setStatus("current")
_Frf8ProtAtmToFrOctets_Type = Counter32
_Frf8ProtAtmToFrOctets_Object = MibTableColumn
frf8ProtAtmToFrOctets = _Frf8ProtAtmToFrOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 2, 1, 5),
    _Frf8ProtAtmToFrOctets_Type()
)
frf8ProtAtmToFrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ProtAtmToFrOctets.setStatus("current")
_Frf8ProtFrToAtmPdus_Type = Counter32
_Frf8ProtFrToAtmPdus_Object = MibTableColumn
frf8ProtFrToAtmPdus = _Frf8ProtFrToAtmPdus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 2, 1, 6),
    _Frf8ProtFrToAtmPdus_Type()
)
frf8ProtFrToAtmPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ProtFrToAtmPdus.setStatus("current")
_Frf8ProtFrToAtmOctets_Type = Counter32
_Frf8ProtFrToAtmOctets_Object = MibTableColumn
frf8ProtFrToAtmOctets = _Frf8ProtFrToAtmOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 2, 1, 7),
    _Frf8ProtFrToAtmOctets_Type()
)
frf8ProtFrToAtmOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8ProtFrToAtmOctets.setStatus("current")
_Frf8OamF5Table_Object = MibTable
frf8OamF5Table = _Frf8OamF5Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 3)
)
if mibBuilder.loadTexts:
    frf8OamF5Table.setStatus("current")
_Frf8OamF5Entry_Object = MibTableRow
frf8OamF5Entry = _Frf8OamF5Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 3, 1)
)
frf8OamF5Entry.setIndexNames(
    (0, "Fore-frf8-MIB", "frf8OamF5ServiceIfIndex"),
    (0, "Fore-frf8-MIB", "frf8OamF5VcDlci"),
)
if mibBuilder.loadTexts:
    frf8OamF5Entry.setStatus("current")
_Frf8OamF5ServiceIfIndex_Type = InterfaceIndex
_Frf8OamF5ServiceIfIndex_Object = MibTableColumn
frf8OamF5ServiceIfIndex = _Frf8OamF5ServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 3, 1, 1),
    _Frf8OamF5ServiceIfIndex_Type()
)
frf8OamF5ServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8OamF5ServiceIfIndex.setStatus("current")
_Frf8OamF5VcDlci_Type = Integer32
_Frf8OamF5VcDlci_Object = MibTableColumn
frf8OamF5VcDlci = _Frf8OamF5VcDlci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 3, 1, 2),
    _Frf8OamF5VcDlci_Type()
)
frf8OamF5VcDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8OamF5VcDlci.setStatus("current")
_Frf8OamF5AISRxCounter_Type = Counter32
_Frf8OamF5AISRxCounter_Object = MibTableColumn
frf8OamF5AISRxCounter = _Frf8OamF5AISRxCounter_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 3, 1, 3),
    _Frf8OamF5AISRxCounter_Type()
)
frf8OamF5AISRxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8OamF5AISRxCounter.setStatus("current")
_Frf8OamF5AISTxCounter_Type = Counter32
_Frf8OamF5AISTxCounter_Object = MibTableColumn
frf8OamF5AISTxCounter = _Frf8OamF5AISTxCounter_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 3, 1, 4),
    _Frf8OamF5AISTxCounter_Type()
)
frf8OamF5AISTxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8OamF5AISTxCounter.setStatus("current")
_Frf8OamF5RDIRxCounter_Type = Counter32
_Frf8OamF5RDIRxCounter_Object = MibTableColumn
frf8OamF5RDIRxCounter = _Frf8OamF5RDIRxCounter_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 3, 1, 5),
    _Frf8OamF5RDIRxCounter_Type()
)
frf8OamF5RDIRxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8OamF5RDIRxCounter.setStatus("current")
_Frf8OamF5RDITxCounter_Type = Counter32
_Frf8OamF5RDITxCounter_Object = MibTableColumn
frf8OamF5RDITxCounter = _Frf8OamF5RDITxCounter_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 2, 3, 1, 6),
    _Frf8OamF5RDITxCounter_Type()
)
frf8OamF5RDITxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frf8OamF5RDITxCounter.setStatus("current")

# Managed Objects groups


# Notification objects

frf8PVCStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2000)
)
frf8PVCStatus.setObjects(
      *(("Fore-frf8-MIB", "frf8ConnFrServiceIfIndex"),
        ("Fore-frf8-MIB", "frf8ConnDlci"),
        ("Fore-frf8-MIB", "frf8ConnOperStatus"),
        ("Fore-frf8-MIB", "frf8ConnPVCAlarmReason"))
)
if mibBuilder.loadTexts:
    frf8PVCStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-frf8-MIB",
    **{"foreFrf8Module": foreFrf8Module,
       "frf8ConnTable": frf8ConnTable,
       "frf8ConnEntry": frf8ConnEntry,
       "frf8ConnFrServiceIfIndex": frf8ConnFrServiceIfIndex,
       "frf8ConnDlci": frf8ConnDlci,
       "frf8ConnFabServiceIfIndex": frf8ConnFabServiceIfIndex,
       "frf8ConnFabVpi": frf8ConnFabVpi,
       "frf8ConnFabVci": frf8ConnFabVci,
       "frf8ConnRowStatus": frf8ConnRowStatus,
       "frf8ConnProfileFrf8Index": frf8ConnProfileFrf8Index,
       "frf8ConnProfileEpdPpdIndex": frf8ConnProfileEpdPpdIndex,
       "frf8ConnAtmAddrType": frf8ConnAtmAddrType,
       "frf8ConnAtmAddress": frf8ConnAtmAddress,
       "frf8ConnAtmSubAddrType": frf8ConnAtmSubAddrType,
       "frf8ConnAtmSubAddress": frf8ConnAtmSubAddress,
       "frf8ConnFrAddrType": frf8ConnFrAddrType,
       "frf8ConnFrAddress": frf8ConnFrAddress,
       "frf8ConnAdminStatus": frf8ConnAdminStatus,
       "frf8ConnOperStatus": frf8ConnOperStatus,
       "frf8ConnCreationTime": frf8ConnCreationTime,
       "frf8ConnTimeChange": frf8ConnTimeChange,
       "frf8ConnPVCAlarmReason": frf8ConnPVCAlarmReason,
       "frf8ConnAtmToFrPDUDiscards": frf8ConnAtmToFrPDUDiscards,
       "frf8ConnFrToAtmPDUDiscards": frf8ConnFrToAtmPDUDiscards,
       "frf8ConnAtmToFrUnkProts": frf8ConnAtmToFrUnkProts,
       "frf8ConnFrToAtmUnkProts": frf8ConnFrToAtmUnkProts,
       "frf8ConnAtmToFrArpNakDiscards": frf8ConnAtmToFrArpNakDiscards,
       "frf8ProtTable": frf8ProtTable,
       "frf8ProtEntry": frf8ProtEntry,
       "frf8ProtServiceIfIndex": frf8ProtServiceIfIndex,
       "frf8ProtDlci": frf8ProtDlci,
       "frf8ProtProtocol": frf8ProtProtocol,
       "frf8ProtAtmToFrPdus": frf8ProtAtmToFrPdus,
       "frf8ProtAtmToFrOctets": frf8ProtAtmToFrOctets,
       "frf8ProtFrToAtmPdus": frf8ProtFrToAtmPdus,
       "frf8ProtFrToAtmOctets": frf8ProtFrToAtmOctets,
       "frf8OamF5Table": frf8OamF5Table,
       "frf8OamF5Entry": frf8OamF5Entry,
       "frf8OamF5ServiceIfIndex": frf8OamF5ServiceIfIndex,
       "frf8OamF5VcDlci": frf8OamF5VcDlci,
       "frf8OamF5AISRxCounter": frf8OamF5AISRxCounter,
       "frf8OamF5AISTxCounter": frf8OamF5AISTxCounter,
       "frf8OamF5RDIRxCounter": frf8OamF5RDIRxCounter,
       "frf8OamF5RDITxCounter": frf8OamF5RDITxCounter,
       "frf8PVCStatus": frf8PVCStatus}
)
