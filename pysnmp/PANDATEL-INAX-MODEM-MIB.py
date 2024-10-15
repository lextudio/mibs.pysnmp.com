# SNMP MIB module (PANDATEL-INAX-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PANDATEL-INAX-MODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:54 2024
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

(device_id,
 mdmSpecifics) = mibBuilder.importSymbols(
    "PANDATEL-MODEM-MIB",
    "device-id",
    "mdmSpecifics")

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

_Inax_ObjectIdentity = ObjectIdentity
inax = _Inax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701)
)
_InaxModemTable_Object = MibTable
inaxModemTable = _InaxModemTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1)
)
if mibBuilder.loadTexts:
    inaxModemTable.setStatus("mandatory")
_InaxTableEntry_Object = MibTableRow
inaxTableEntry = _InaxTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1, 1)
)
inaxTableEntry.setIndexNames(
    (0, "PANDATEL-INAX-MODEM-MIB", "mdmRack"),
    (0, "PANDATEL-INAX-MODEM-MIB", "mdmModem"),
    (0, "PANDATEL-INAX-MODEM-MIB", "mdmPosition"),
)
if mibBuilder.loadTexts:
    inaxTableEntry.setStatus("mandatory")
_MdmRack_Type = Integer32
_MdmRack_Object = MibTableColumn
mdmRack = _MdmRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1, 1, 1),
    _MdmRack_Type()
)
mdmRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRack.setStatus("mandatory")
_MdmModem_Type = Integer32
_MdmModem_Object = MibTableColumn
mdmModem = _MdmModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1, 1, 2),
    _MdmModem_Type()
)
mdmModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmModem.setStatus("mandatory")


class _MdmPosition_Type(Integer32):
    """Custom type mdmPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_MdmPosition_Type.__name__ = "Integer32"
_MdmPosition_Object = MibTableColumn
mdmPosition = _MdmPosition_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1, 1, 3),
    _MdmPosition_Type()
)
mdmPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPosition.setStatus("mandatory")
_MdmModemName_Type = DisplayString
_MdmModemName_Object = MibTableColumn
mdmModemName = _MdmModemName_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1, 1, 5),
    _MdmModemName_Type()
)
mdmModemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmModemName.setStatus("mandatory")


class _MdmModemProperty_Type(Integer32):
    """Custom type mdmModemProperty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("other", 1),
          ("t1", 3),
          ("unknown", 99))
    )


_MdmModemProperty_Type.__name__ = "Integer32"
_MdmModemProperty_Object = MibTableColumn
mdmModemProperty = _MdmModemProperty_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1, 1, 7),
    _MdmModemProperty_Type()
)
mdmModemProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmModemProperty.setStatus("mandatory")


class _MdmActiveLink_Type(Integer32):
    """Custom type mdmActiveLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              11,
              90)
        )
    )
    namedValues = NamedValues(
        *(("disable", 90),
          ("line-port-4", 4),
          ("line-port-4-and-5", 11),
          ("line-port-5", 5))
    )


_MdmActiveLink_Type.__name__ = "Integer32"
_MdmActiveLink_Object = MibTableColumn
mdmActiveLink = _MdmActiveLink_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1, 1, 12),
    _MdmActiveLink_Type()
)
mdmActiveLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmActiveLink.setStatus("mandatory")


class _MdmRemoteAccessMode_Type(Integer32):
    """Custom type mdmRemoteAccessMode based on Integer32"""
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
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("disable", 98),
          ("other", 99),
          ("via-timeslot-1", 1),
          ("via-timeslot-10", 10),
          ("via-timeslot-11", 11),
          ("via-timeslot-12", 12),
          ("via-timeslot-13", 13),
          ("via-timeslot-14", 14),
          ("via-timeslot-15", 15),
          ("via-timeslot-16", 16),
          ("via-timeslot-17", 17),
          ("via-timeslot-18", 18),
          ("via-timeslot-19", 19),
          ("via-timeslot-2", 2),
          ("via-timeslot-20", 20),
          ("via-timeslot-21", 21),
          ("via-timeslot-22", 22),
          ("via-timeslot-23", 23),
          ("via-timeslot-24", 24),
          ("via-timeslot-25", 25),
          ("via-timeslot-26", 26),
          ("via-timeslot-27", 27),
          ("via-timeslot-28", 28),
          ("via-timeslot-29", 29),
          ("via-timeslot-3", 3),
          ("via-timeslot-30", 30),
          ("via-timeslot-31", 31),
          ("via-timeslot-4", 4),
          ("via-timeslot-5", 5),
          ("via-timeslot-6", 6),
          ("via-timeslot-7", 7),
          ("via-timeslot-8", 8),
          ("via-timeslot-9", 9))
    )


_MdmRemoteAccessMode_Type.__name__ = "Integer32"
_MdmRemoteAccessMode_Object = MibTableColumn
mdmRemoteAccessMode = _MdmRemoteAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1, 1, 64),
    _MdmRemoteAccessMode_Type()
)
mdmRemoteAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmRemoteAccessMode.setStatus("mandatory")
_InaxIFPortTable_Object = MibTable
inaxIFPortTable = _InaxIFPortTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2)
)
if mibBuilder.loadTexts:
    inaxIFPortTable.setStatus("mandatory")
_InaxIFPortEntry_Object = MibTableRow
inaxIFPortEntry = _InaxIFPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2, 1)
)
inaxIFPortEntry.setIndexNames(
    (0, "PANDATEL-INAX-MODEM-MIB", "iportRack"),
    (0, "PANDATEL-INAX-MODEM-MIB", "iportModem"),
    (0, "PANDATEL-INAX-MODEM-MIB", "iportPosition"),
    (0, "PANDATEL-INAX-MODEM-MIB", "iportPort"),
)
if mibBuilder.loadTexts:
    inaxIFPortEntry.setStatus("mandatory")
_IportRack_Type = Integer32
_IportRack_Object = MibTableColumn
iportRack = _IportRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2, 1, 1),
    _IportRack_Type()
)
iportRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iportRack.setStatus("mandatory")
_IportModem_Type = Integer32
_IportModem_Object = MibTableColumn
iportModem = _IportModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2, 1, 2),
    _IportModem_Type()
)
iportModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iportModem.setStatus("mandatory")


class _IportPosition_Type(Integer32):
    """Custom type iportPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_IportPosition_Type.__name__ = "Integer32"
_IportPosition_Object = MibTableColumn
iportPosition = _IportPosition_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2, 1, 3),
    _IportPosition_Type()
)
iportPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iportPosition.setStatus("mandatory")
_IportPort_Type = Integer32
_IportPort_Object = MibTableColumn
iportPort = _IportPort_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2, 1, 4),
    _IportPort_Type()
)
iportPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iportPort.setStatus("mandatory")


class _IportDataEmulationMode_Type(Integer32):
    """Custom type iportDataEmulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("dce", 3),
          ("dte", 2),
          ("nt", 5),
          ("other", 1),
          ("te", 4),
          ("unknown", 99))
    )


_IportDataEmulationMode_Type.__name__ = "Integer32"
_IportDataEmulationMode_Object = MibTableColumn
iportDataEmulationMode = _IportDataEmulationMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2, 1, 6),
    _IportDataEmulationMode_Type()
)
iportDataEmulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iportDataEmulationMode.setStatus("mandatory")


class _IportDataRate_Type(Integer32):
    """Custom type iportDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("off", 1)
    )


_IportDataRate_Type.__name__ = "Integer32"
_IportDataRate_Object = MibTableColumn
iportDataRate = _IportDataRate_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2, 1, 25),
    _IportDataRate_Type()
)
iportDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iportDataRate.setStatus("mandatory")


class _IportTimeslotSize_Type(Integer32):
    """Custom type iportTimeslotSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("nx56k", 3),
          ("nx64k", 2),
          ("other", 1))
    )


_IportTimeslotSize_Type.__name__ = "Integer32"
_IportTimeslotSize_Object = MibTableColumn
iportTimeslotSize = _IportTimeslotSize_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2, 1, 27),
    _IportTimeslotSize_Type()
)
iportTimeslotSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iportTimeslotSize.setStatus("mandatory")
_InaxLinePortTable_Object = MibTable
inaxLinePortTable = _InaxLinePortTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3)
)
if mibBuilder.loadTexts:
    inaxLinePortTable.setStatus("mandatory")
_InaxLinePortEntry_Object = MibTableRow
inaxLinePortEntry = _InaxLinePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1)
)
inaxLinePortEntry.setIndexNames(
    (0, "PANDATEL-INAX-MODEM-MIB", "lportRack"),
    (0, "PANDATEL-INAX-MODEM-MIB", "lportModem"),
    (0, "PANDATEL-INAX-MODEM-MIB", "lportPosition"),
    (0, "PANDATEL-INAX-MODEM-MIB", "lportPort"),
)
if mibBuilder.loadTexts:
    inaxLinePortEntry.setStatus("mandatory")
_LportRack_Type = Integer32
_LportRack_Object = MibTableColumn
lportRack = _LportRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 1),
    _LportRack_Type()
)
lportRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportRack.setStatus("mandatory")
_LportModem_Type = Integer32
_LportModem_Object = MibTableColumn
lportModem = _LportModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 2),
    _LportModem_Type()
)
lportModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportModem.setStatus("mandatory")


class _LportPosition_Type(Integer32):
    """Custom type lportPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_LportPosition_Type.__name__ = "Integer32"
_LportPosition_Object = MibTableColumn
lportPosition = _LportPosition_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 3),
    _LportPosition_Type()
)
lportPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportPosition.setStatus("mandatory")
_LportPort_Type = Integer32
_LportPort_Object = MibTableColumn
lportPort = _LportPort_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 4),
    _LportPort_Type()
)
lportPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportPort.setStatus("mandatory")


class _LportDataEmulationMode_Type(Integer32):
    """Custom type lportDataEmulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("dce", 3),
          ("dte", 2),
          ("nt", 5),
          ("other", 1),
          ("te", 4),
          ("unknown", 99))
    )


_LportDataEmulationMode_Type.__name__ = "Integer32"
_LportDataEmulationMode_Object = MibTableColumn
lportDataEmulationMode = _LportDataEmulationMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 6),
    _LportDataEmulationMode_Type()
)
lportDataEmulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDataEmulationMode.setStatus("mandatory")


class _LportClockSource_Type(Integer32):
    """Custom type lportClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("other", 1),
          ("remote", 3))
    )


_LportClockSource_Type.__name__ = "Integer32"
_LportClockSource_Object = MibTableColumn
lportClockSource = _LportClockSource_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 24),
    _LportClockSource_Type()
)
lportClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportClockSource.setStatus("mandatory")


class _LportDataRate_Type(Integer32):
    """Custom type lportDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("off", 1)
    )


_LportDataRate_Type.__name__ = "Integer32"
_LportDataRate_Object = MibTableColumn
lportDataRate = _LportDataRate_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 25),
    _LportDataRate_Type()
)
lportDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportDataRate.setStatus("mandatory")


class _LportCRC4Generation_Type(Integer32):
    """Custom type lportCRC4Generation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("not-available", 100),
          ("other", 1))
    )


_LportCRC4Generation_Type.__name__ = "Integer32"
_LportCRC4Generation_Object = MibTableColumn
lportCRC4Generation = _LportCRC4Generation_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 41),
    _LportCRC4Generation_Type()
)
lportCRC4Generation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportCRC4Generation.setStatus("mandatory")


class _LportFramingMode_Type(Integer32):
    """Custom type lportFramingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("d4", 2),
          ("esf", 3),
          ("not-available", 100),
          ("other", 1))
    )


_LportFramingMode_Type.__name__ = "Integer32"
_LportFramingMode_Object = MibTableColumn
lportFramingMode = _LportFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 50),
    _LportFramingMode_Type()
)
lportFramingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportFramingMode.setStatus("mandatory")


class _LportCodingMode_Type(Integer32):
    """Custom type lportCodingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("ami", 2),
          ("b8zs", 3),
          ("not-available", 100),
          ("other", 1))
    )


_LportCodingMode_Type.__name__ = "Integer32"
_LportCodingMode_Object = MibTableColumn
lportCodingMode = _LportCodingMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 51),
    _LportCodingMode_Type()
)
lportCodingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportCodingMode.setStatus("mandatory")


class _LportLineBuiltOut_Type(Integer32):
    """Custom type lportLineBuiltOut based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("csu-0db", 8),
          ("csu-15db", 10),
          ("csu-22db5", 11),
          ("csu-7db5", 9),
          ("dsx-1-0to133-ft", 3),
          ("dsx-1-133to266-ft", 4),
          ("dsx-1-266to399-ft", 5),
          ("dsx-1-399to533-ft", 6),
          ("dsx-1-533to655-ft", 7),
          ("itu-rec-g703", 2),
          ("not-available", 100),
          ("other", 1))
    )


_LportLineBuiltOut_Type.__name__ = "Integer32"
_LportLineBuiltOut_Object = MibTableColumn
lportLineBuiltOut = _LportLineBuiltOut_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 68),
    _LportLineBuiltOut_Type()
)
lportLineBuiltOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportLineBuiltOut.setStatus("mandatory")


class _LportPortMode_Type(Integer32):
    """Custom type lportPortMode based on Integer32"""
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
        *(("backup-mode", 3),
          ("if-mode", 2),
          ("link-mode", 4),
          ("other", 1))
    )


_LportPortMode_Type.__name__ = "Integer32"
_LportPortMode_Object = MibTableColumn
lportPortMode = _LportPortMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 69),
    _LportPortMode_Type()
)
lportPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportPortMode.setStatus("mandatory")


class _LportCRC6Test_Type(Integer32):
    """Custom type lportCRC6Test based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("other", 1),
          ("start", 3),
          ("stop", 4))
    )


_LportCRC6Test_Type.__name__ = "Integer32"
_LportCRC6Test_Object = MibTableColumn
lportCRC6Test = _LportCRC6Test_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 100),
    _LportCRC6Test_Type()
)
lportCRC6Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lportCRC6Test.setStatus("mandatory")


class _LportCRC6Status_Type(Integer32):
    """Custom type lportCRC6Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              7,
              100)
        )
    )
    namedValues = NamedValues(
        *(("never-started", 2),
          ("not-available", 100),
          ("other", 1),
          ("running", 5),
          ("start-failed", 7),
          ("stopped", 6))
    )


_LportCRC6Status_Type.__name__ = "Integer32"
_LportCRC6Status_Object = MibTableColumn
lportCRC6Status = _LportCRC6Status_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 101),
    _LportCRC6Status_Type()
)
lportCRC6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportCRC6Status.setStatus("mandatory")
_LportCRC6Error_Type = Gauge32
_LportCRC6Error_Object = MibTableColumn
lportCRC6Error = _LportCRC6Error_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 102),
    _LportCRC6Error_Type()
)
lportCRC6Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lportCRC6Error.setStatus("mandatory")
_InaxTimeslotTable_Object = MibTable
inaxTimeslotTable = _InaxTimeslotTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4)
)
if mibBuilder.loadTexts:
    inaxTimeslotTable.setStatus("mandatory")
_InaxTimeslotEntry_Object = MibTableRow
inaxTimeslotEntry = _InaxTimeslotEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1)
)
inaxTimeslotEntry.setIndexNames(
    (0, "PANDATEL-INAX-MODEM-MIB", "tsRack"),
    (0, "PANDATEL-INAX-MODEM-MIB", "tsModem"),
    (0, "PANDATEL-INAX-MODEM-MIB", "tsPosition"),
    (0, "PANDATEL-INAX-MODEM-MIB", "tsPort"),
)
if mibBuilder.loadTexts:
    inaxTimeslotEntry.setStatus("mandatory")
_TsRack_Type = Integer32
_TsRack_Object = MibTableColumn
tsRack = _TsRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 1),
    _TsRack_Type()
)
tsRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsRack.setStatus("mandatory")
_TsModem_Type = Integer32
_TsModem_Object = MibTableColumn
tsModem = _TsModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 2),
    _TsModem_Type()
)
tsModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsModem.setStatus("mandatory")


class _TsPosition_Type(Integer32):
    """Custom type tsPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_TsPosition_Type.__name__ = "Integer32"
_TsPosition_Object = MibTableColumn
tsPosition = _TsPosition_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 3),
    _TsPosition_Type()
)
tsPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPosition.setStatus("mandatory")
_TsPort_Type = Integer32
_TsPort_Object = MibTableColumn
tsPort = _TsPort_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 4),
    _TsPort_Type()
)
tsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPort.setStatus("mandatory")


class _TsTimeslot1_Type(Integer32):
    """Custom type tsTimeslot1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot1_Type.__name__ = "Integer32"
_TsTimeslot1_Object = MibTableColumn
tsTimeslot1 = _TsTimeslot1_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 301),
    _TsTimeslot1_Type()
)
tsTimeslot1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot1.setStatus("mandatory")


class _TsTimeslot2_Type(Integer32):
    """Custom type tsTimeslot2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot2_Type.__name__ = "Integer32"
_TsTimeslot2_Object = MibTableColumn
tsTimeslot2 = _TsTimeslot2_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 302),
    _TsTimeslot2_Type()
)
tsTimeslot2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot2.setStatus("mandatory")


class _TsTimeslot3_Type(Integer32):
    """Custom type tsTimeslot3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot3_Type.__name__ = "Integer32"
_TsTimeslot3_Object = MibTableColumn
tsTimeslot3 = _TsTimeslot3_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 303),
    _TsTimeslot3_Type()
)
tsTimeslot3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot3.setStatus("mandatory")


class _TsTimeslot4_Type(Integer32):
    """Custom type tsTimeslot4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot4_Type.__name__ = "Integer32"
_TsTimeslot4_Object = MibTableColumn
tsTimeslot4 = _TsTimeslot4_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 304),
    _TsTimeslot4_Type()
)
tsTimeslot4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot4.setStatus("mandatory")


class _TsTimeslot5_Type(Integer32):
    """Custom type tsTimeslot5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot5_Type.__name__ = "Integer32"
_TsTimeslot5_Object = MibTableColumn
tsTimeslot5 = _TsTimeslot5_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 305),
    _TsTimeslot5_Type()
)
tsTimeslot5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot5.setStatus("mandatory")


class _TsTimeslot6_Type(Integer32):
    """Custom type tsTimeslot6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot6_Type.__name__ = "Integer32"
_TsTimeslot6_Object = MibTableColumn
tsTimeslot6 = _TsTimeslot6_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 306),
    _TsTimeslot6_Type()
)
tsTimeslot6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot6.setStatus("mandatory")


class _TsTimeslot7_Type(Integer32):
    """Custom type tsTimeslot7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot7_Type.__name__ = "Integer32"
_TsTimeslot7_Object = MibTableColumn
tsTimeslot7 = _TsTimeslot7_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 307),
    _TsTimeslot7_Type()
)
tsTimeslot7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot7.setStatus("mandatory")


class _TsTimeslot8_Type(Integer32):
    """Custom type tsTimeslot8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot8_Type.__name__ = "Integer32"
_TsTimeslot8_Object = MibTableColumn
tsTimeslot8 = _TsTimeslot8_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 308),
    _TsTimeslot8_Type()
)
tsTimeslot8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot8.setStatus("mandatory")


class _TsTimeslot9_Type(Integer32):
    """Custom type tsTimeslot9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot9_Type.__name__ = "Integer32"
_TsTimeslot9_Object = MibTableColumn
tsTimeslot9 = _TsTimeslot9_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 309),
    _TsTimeslot9_Type()
)
tsTimeslot9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot9.setStatus("mandatory")


class _TsTimeslot10_Type(Integer32):
    """Custom type tsTimeslot10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot10_Type.__name__ = "Integer32"
_TsTimeslot10_Object = MibTableColumn
tsTimeslot10 = _TsTimeslot10_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 310),
    _TsTimeslot10_Type()
)
tsTimeslot10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot10.setStatus("mandatory")


class _TsTimeslot11_Type(Integer32):
    """Custom type tsTimeslot11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot11_Type.__name__ = "Integer32"
_TsTimeslot11_Object = MibTableColumn
tsTimeslot11 = _TsTimeslot11_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 311),
    _TsTimeslot11_Type()
)
tsTimeslot11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot11.setStatus("mandatory")


class _TsTimeslot12_Type(Integer32):
    """Custom type tsTimeslot12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot12_Type.__name__ = "Integer32"
_TsTimeslot12_Object = MibTableColumn
tsTimeslot12 = _TsTimeslot12_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 312),
    _TsTimeslot12_Type()
)
tsTimeslot12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot12.setStatus("mandatory")


class _TsTimeslot13_Type(Integer32):
    """Custom type tsTimeslot13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot13_Type.__name__ = "Integer32"
_TsTimeslot13_Object = MibTableColumn
tsTimeslot13 = _TsTimeslot13_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 313),
    _TsTimeslot13_Type()
)
tsTimeslot13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot13.setStatus("mandatory")


class _TsTimeslot14_Type(Integer32):
    """Custom type tsTimeslot14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot14_Type.__name__ = "Integer32"
_TsTimeslot14_Object = MibTableColumn
tsTimeslot14 = _TsTimeslot14_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 314),
    _TsTimeslot14_Type()
)
tsTimeslot14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot14.setStatus("mandatory")


class _TsTimeslot15_Type(Integer32):
    """Custom type tsTimeslot15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot15_Type.__name__ = "Integer32"
_TsTimeslot15_Object = MibTableColumn
tsTimeslot15 = _TsTimeslot15_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 315),
    _TsTimeslot15_Type()
)
tsTimeslot15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot15.setStatus("mandatory")


class _TsTimeslot16_Type(Integer32):
    """Custom type tsTimeslot16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot16_Type.__name__ = "Integer32"
_TsTimeslot16_Object = MibTableColumn
tsTimeslot16 = _TsTimeslot16_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 316),
    _TsTimeslot16_Type()
)
tsTimeslot16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot16.setStatus("mandatory")


class _TsTimeslot17_Type(Integer32):
    """Custom type tsTimeslot17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot17_Type.__name__ = "Integer32"
_TsTimeslot17_Object = MibTableColumn
tsTimeslot17 = _TsTimeslot17_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 317),
    _TsTimeslot17_Type()
)
tsTimeslot17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot17.setStatus("mandatory")


class _TsTimeslot18_Type(Integer32):
    """Custom type tsTimeslot18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot18_Type.__name__ = "Integer32"
_TsTimeslot18_Object = MibTableColumn
tsTimeslot18 = _TsTimeslot18_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 318),
    _TsTimeslot18_Type()
)
tsTimeslot18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot18.setStatus("mandatory")


class _TsTimeslot19_Type(Integer32):
    """Custom type tsTimeslot19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot19_Type.__name__ = "Integer32"
_TsTimeslot19_Object = MibTableColumn
tsTimeslot19 = _TsTimeslot19_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 319),
    _TsTimeslot19_Type()
)
tsTimeslot19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot19.setStatus("mandatory")


class _TsTimeslot20_Type(Integer32):
    """Custom type tsTimeslot20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot20_Type.__name__ = "Integer32"
_TsTimeslot20_Object = MibTableColumn
tsTimeslot20 = _TsTimeslot20_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 320),
    _TsTimeslot20_Type()
)
tsTimeslot20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot20.setStatus("mandatory")


class _TsTimeslot21_Type(Integer32):
    """Custom type tsTimeslot21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot21_Type.__name__ = "Integer32"
_TsTimeslot21_Object = MibTableColumn
tsTimeslot21 = _TsTimeslot21_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 321),
    _TsTimeslot21_Type()
)
tsTimeslot21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot21.setStatus("mandatory")


class _TsTimeslot22_Type(Integer32):
    """Custom type tsTimeslot22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot22_Type.__name__ = "Integer32"
_TsTimeslot22_Object = MibTableColumn
tsTimeslot22 = _TsTimeslot22_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 322),
    _TsTimeslot22_Type()
)
tsTimeslot22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot22.setStatus("mandatory")


class _TsTimeslot23_Type(Integer32):
    """Custom type tsTimeslot23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot23_Type.__name__ = "Integer32"
_TsTimeslot23_Object = MibTableColumn
tsTimeslot23 = _TsTimeslot23_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 323),
    _TsTimeslot23_Type()
)
tsTimeslot23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot23.setStatus("mandatory")


class _TsTimeslot24_Type(Integer32):
    """Custom type tsTimeslot24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot24_Type.__name__ = "Integer32"
_TsTimeslot24_Object = MibTableColumn
tsTimeslot24 = _TsTimeslot24_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 324),
    _TsTimeslot24_Type()
)
tsTimeslot24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot24.setStatus("mandatory")


class _TsTimeslot25_Type(Integer32):
    """Custom type tsTimeslot25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot25_Type.__name__ = "Integer32"
_TsTimeslot25_Object = MibTableColumn
tsTimeslot25 = _TsTimeslot25_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 325),
    _TsTimeslot25_Type()
)
tsTimeslot25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot25.setStatus("mandatory")


class _TsTimeslot26_Type(Integer32):
    """Custom type tsTimeslot26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot26_Type.__name__ = "Integer32"
_TsTimeslot26_Object = MibTableColumn
tsTimeslot26 = _TsTimeslot26_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 326),
    _TsTimeslot26_Type()
)
tsTimeslot26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot26.setStatus("mandatory")


class _TsTimeslot27_Type(Integer32):
    """Custom type tsTimeslot27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot27_Type.__name__ = "Integer32"
_TsTimeslot27_Object = MibTableColumn
tsTimeslot27 = _TsTimeslot27_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 327),
    _TsTimeslot27_Type()
)
tsTimeslot27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot27.setStatus("mandatory")


class _TsTimeslot28_Type(Integer32):
    """Custom type tsTimeslot28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot28_Type.__name__ = "Integer32"
_TsTimeslot28_Object = MibTableColumn
tsTimeslot28 = _TsTimeslot28_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 328),
    _TsTimeslot28_Type()
)
tsTimeslot28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot28.setStatus("mandatory")


class _TsTimeslot29_Type(Integer32):
    """Custom type tsTimeslot29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot29_Type.__name__ = "Integer32"
_TsTimeslot29_Object = MibTableColumn
tsTimeslot29 = _TsTimeslot29_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 329),
    _TsTimeslot29_Type()
)
tsTimeslot29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot29.setStatus("mandatory")


class _TsTimeslot30_Type(Integer32):
    """Custom type tsTimeslot30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot30_Type.__name__ = "Integer32"
_TsTimeslot30_Object = MibTableColumn
tsTimeslot30 = _TsTimeslot30_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 330),
    _TsTimeslot30_Type()
)
tsTimeslot30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot30.setStatus("mandatory")


class _TsTimeslot31_Type(Integer32):
    """Custom type tsTimeslot31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("off", 98),
          ("other", 99),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("remote-access", 97))
    )


_TsTimeslot31_Type.__name__ = "Integer32"
_TsTimeslot31_Object = MibTableColumn
tsTimeslot31 = _TsTimeslot31_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 331),
    _TsTimeslot31_Type()
)
tsTimeslot31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTimeslot31.setStatus("mandatory")
_Inax_modem_ObjectIdentity = ObjectIdentity
inax_modem = _Inax_modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 701)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANDATEL-INAX-MODEM-MIB",
    **{"inax": inax,
       "inaxModemTable": inaxModemTable,
       "inaxTableEntry": inaxTableEntry,
       "mdmRack": mdmRack,
       "mdmModem": mdmModem,
       "mdmPosition": mdmPosition,
       "mdmModemName": mdmModemName,
       "mdmModemProperty": mdmModemProperty,
       "mdmActiveLink": mdmActiveLink,
       "mdmRemoteAccessMode": mdmRemoteAccessMode,
       "inaxIFPortTable": inaxIFPortTable,
       "inaxIFPortEntry": inaxIFPortEntry,
       "iportRack": iportRack,
       "iportModem": iportModem,
       "iportPosition": iportPosition,
       "iportPort": iportPort,
       "iportDataEmulationMode": iportDataEmulationMode,
       "iportDataRate": iportDataRate,
       "iportTimeslotSize": iportTimeslotSize,
       "inaxLinePortTable": inaxLinePortTable,
       "inaxLinePortEntry": inaxLinePortEntry,
       "lportRack": lportRack,
       "lportModem": lportModem,
       "lportPosition": lportPosition,
       "lportPort": lportPort,
       "lportDataEmulationMode": lportDataEmulationMode,
       "lportClockSource": lportClockSource,
       "lportDataRate": lportDataRate,
       "lportCRC4Generation": lportCRC4Generation,
       "lportFramingMode": lportFramingMode,
       "lportCodingMode": lportCodingMode,
       "lportLineBuiltOut": lportLineBuiltOut,
       "lportPortMode": lportPortMode,
       "lportCRC6Test": lportCRC6Test,
       "lportCRC6Status": lportCRC6Status,
       "lportCRC6Error": lportCRC6Error,
       "inaxTimeslotTable": inaxTimeslotTable,
       "inaxTimeslotEntry": inaxTimeslotEntry,
       "tsRack": tsRack,
       "tsModem": tsModem,
       "tsPosition": tsPosition,
       "tsPort": tsPort,
       "tsTimeslot1": tsTimeslot1,
       "tsTimeslot2": tsTimeslot2,
       "tsTimeslot3": tsTimeslot3,
       "tsTimeslot4": tsTimeslot4,
       "tsTimeslot5": tsTimeslot5,
       "tsTimeslot6": tsTimeslot6,
       "tsTimeslot7": tsTimeslot7,
       "tsTimeslot8": tsTimeslot8,
       "tsTimeslot9": tsTimeslot9,
       "tsTimeslot10": tsTimeslot10,
       "tsTimeslot11": tsTimeslot11,
       "tsTimeslot12": tsTimeslot12,
       "tsTimeslot13": tsTimeslot13,
       "tsTimeslot14": tsTimeslot14,
       "tsTimeslot15": tsTimeslot15,
       "tsTimeslot16": tsTimeslot16,
       "tsTimeslot17": tsTimeslot17,
       "tsTimeslot18": tsTimeslot18,
       "tsTimeslot19": tsTimeslot19,
       "tsTimeslot20": tsTimeslot20,
       "tsTimeslot21": tsTimeslot21,
       "tsTimeslot22": tsTimeslot22,
       "tsTimeslot23": tsTimeslot23,
       "tsTimeslot24": tsTimeslot24,
       "tsTimeslot25": tsTimeslot25,
       "tsTimeslot26": tsTimeslot26,
       "tsTimeslot27": tsTimeslot27,
       "tsTimeslot28": tsTimeslot28,
       "tsTimeslot29": tsTimeslot29,
       "tsTimeslot30": tsTimeslot30,
       "tsTimeslot31": tsTimeslot31,
       "inax-modem": inax_modem}
)
