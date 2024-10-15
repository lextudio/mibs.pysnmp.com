# SNMP MIB module (PANDATEL-FME-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PANDATEL-FME-MODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:46 2024
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

_Fme_ObjectIdentity = ObjectIdentity
fme = _Fme_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601)
)
_FmeModemTable_Object = MibTable
fmeModemTable = _FmeModemTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1)
)
if mibBuilder.loadTexts:
    fmeModemTable.setStatus("mandatory")
_FmeTableEntry_Object = MibTableRow
fmeTableEntry = _FmeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1, 1)
)
fmeTableEntry.setIndexNames(
    (0, "PANDATEL-FME-MODEM-MIB", "mdmRack"),
    (0, "PANDATEL-FME-MODEM-MIB", "mdmModem"),
    (0, "PANDATEL-FME-MODEM-MIB", "mdmPosition"),
)
if mibBuilder.loadTexts:
    fmeTableEntry.setStatus("mandatory")
_MdmRack_Type = Integer32
_MdmRack_Object = MibTableColumn
mdmRack = _MdmRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1, 1, 1),
    _MdmRack_Type()
)
mdmRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRack.setStatus("mandatory")
_MdmModem_Type = Integer32
_MdmModem_Object = MibTableColumn
mdmModem = _MdmModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1, 1, 3),
    _MdmPosition_Type()
)
mdmPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPosition.setStatus("mandatory")
_MdmModemName_Type = DisplayString
_MdmModemName_Object = MibTableColumn
mdmModemName = _MdmModemName_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1, 1, 5),
    _MdmModemName_Type()
)
mdmModemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmModemName.setStatus("mandatory")


class _MdmActiveLink_Type(Integer32):
    """Custom type mdmActiveLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              90)
        )
    )
    namedValues = NamedValues(
        *(("disable", 90),
          ("line-port-7", 7),
          ("line-port-8", 8))
    )


_MdmActiveLink_Type.__name__ = "Integer32"
_MdmActiveLink_Object = MibTableColumn
mdmActiveLink = _MdmActiveLink_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1, 1, 12),
    _MdmActiveLink_Type()
)
mdmActiveLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmActiveLink.setStatus("mandatory")


class _MdmAlarmConditionPort7_Type(Integer32):
    """Custom type mdmAlarmConditionPort7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("laser-fail", 4),
          ("no-link-signal", 3),
          ("no-link-signal-or-laser-fail", 5),
          ("not-available", 100),
          ("other", 1))
    )


_MdmAlarmConditionPort7_Type.__name__ = "Integer32"
_MdmAlarmConditionPort7_Object = MibTableColumn
mdmAlarmConditionPort7 = _MdmAlarmConditionPort7_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1, 1, 116),
    _MdmAlarmConditionPort7_Type()
)
mdmAlarmConditionPort7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmAlarmConditionPort7.setStatus("mandatory")


class _MdmAlarmConditionPort8_Type(Integer32):
    """Custom type mdmAlarmConditionPort8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("laser-fail", 4),
          ("no-link-signal", 3),
          ("no-link-signal-or-laser-fail", 5),
          ("not-available", 100),
          ("other", 1))
    )


_MdmAlarmConditionPort8_Type.__name__ = "Integer32"
_MdmAlarmConditionPort8_Object = MibTableColumn
mdmAlarmConditionPort8 = _MdmAlarmConditionPort8_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1, 1, 117),
    _MdmAlarmConditionPort8_Type()
)
mdmAlarmConditionPort8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmAlarmConditionPort8.setStatus("mandatory")
_FmePortTable_Object = MibTable
fmePortTable = _FmePortTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2)
)
if mibBuilder.loadTexts:
    fmePortTable.setStatus("mandatory")
_FmePortEntry_Object = MibTableRow
fmePortEntry = _FmePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1)
)
fmePortEntry.setIndexNames(
    (0, "PANDATEL-FME-MODEM-MIB", "portRack"),
    (0, "PANDATEL-FME-MODEM-MIB", "portModem"),
    (0, "PANDATEL-FME-MODEM-MIB", "portPosition"),
    (0, "PANDATEL-FME-MODEM-MIB", "portPort"),
)
if mibBuilder.loadTexts:
    fmePortEntry.setStatus("mandatory")
_PortRack_Type = Integer32
_PortRack_Object = MibTableColumn
portRack = _PortRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 1),
    _PortRack_Type()
)
portRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRack.setStatus("mandatory")
_PortModem_Type = Integer32
_PortModem_Object = MibTableColumn
portModem = _PortModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 2),
    _PortModem_Type()
)
portModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModem.setStatus("mandatory")


class _PortPosition_Type(Integer32):
    """Custom type portPosition based on Integer32"""
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


_PortPosition_Type.__name__ = "Integer32"
_PortPosition_Object = MibTableColumn
portPosition = _PortPosition_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 3),
    _PortPosition_Type()
)
portPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPosition.setStatus("mandatory")
_PortPort_Type = Integer32
_PortPort_Object = MibTableColumn
portPort = _PortPort_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 4),
    _PortPort_Type()
)
portPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPort.setStatus("mandatory")


class _PortInterfaceEmulationMode_Type(Integer32):
    """Custom type portInterfaceEmulationMode based on Integer32"""
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


_PortInterfaceEmulationMode_Type.__name__ = "Integer32"
_PortInterfaceEmulationMode_Object = MibTableColumn
portInterfaceEmulationMode = _PortInterfaceEmulationMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 6),
    _PortInterfaceEmulationMode_Type()
)
portInterfaceEmulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInterfaceEmulationMode.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 7),
    _MdmModemProperty_Type()
)
mdmModemProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmModemProperty.setStatus("mandatory")


class _PortClockSystem_Type(Integer32):
    """Custom type portClockSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dual", 2),
          ("other", 1),
          ("single", 3))
    )


_PortClockSystem_Type.__name__ = "Integer32"
_PortClockSystem_Object = MibTableColumn
portClockSystem = _PortClockSystem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 23),
    _PortClockSystem_Type()
)
portClockSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portClockSystem.setStatus("mandatory")


class _PortClockSource_Type(Integer32):
    """Custom type portClockSource based on Integer32"""
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
        *(("external", 4),
          ("internal", 2),
          ("other", 1),
          ("remote", 3))
    )


_PortClockSource_Type.__name__ = "Integer32"
_PortClockSource_Object = MibTableColumn
portClockSource = _PortClockSource_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 24),
    _PortClockSource_Type()
)
portClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portClockSource.setStatus("mandatory")


class _PortDataRate_Type(Integer32):
    """Custom type portDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("other", 1)
    )


_PortDataRate_Type.__name__ = "Integer32"
_PortDataRate_Object = MibTableColumn
portDataRate = _PortDataRate_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 25),
    _PortDataRate_Type()
)
portDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDataRate.setStatus("mandatory")


class _PortLocalCarrierDetect_Type(Integer32):
    """Custom type portLocalCarrierDetect based on Integer32"""
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
        *(("fo-link", 3),
          ("fo-link-and-remote-handshake", 2),
          ("not-available", 100),
          ("other", 1))
    )


_PortLocalCarrierDetect_Type.__name__ = "Integer32"
_PortLocalCarrierDetect_Object = MibTableColumn
portLocalCarrierDetect = _PortLocalCarrierDetect_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 60),
    _PortLocalCarrierDetect_Type()
)
portLocalCarrierDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLocalCarrierDetect.setStatus("mandatory")


class _PortTDPhaseLocking_Type(Integer32):
    """Custom type portTDPhaseLocking based on Integer32"""
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
        *(("negative-clock-slope", 3),
          ("other", 1),
          ("positive-clock-slope", 2),
          ("unknown", 99))
    )


_PortTDPhaseLocking_Type.__name__ = "Integer32"
_PortTDPhaseLocking_Object = MibTableColumn
portTDPhaseLocking = _PortTDPhaseLocking_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 67),
    _PortTDPhaseLocking_Type()
)
portTDPhaseLocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTDPhaseLocking.setStatus("mandatory")


class _PortLineBuiltOut_Type(Integer32):
    """Custom type portLineBuiltOut based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("dsx-1-0to133-ft", 3),
          ("dsx-1-133to266-ft", 4),
          ("dsx-1-266to399-ft", 5),
          ("dsx-1-399to533-ft", 6),
          ("dsx-1-533to655-ft", 7),
          ("itu-rec-g703", 2),
          ("not-available", 100),
          ("other", 1))
    )


_PortLineBuiltOut_Type.__name__ = "Integer32"
_PortLineBuiltOut_Object = MibTableColumn
portLineBuiltOut = _PortLineBuiltOut_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 68),
    _PortLineBuiltOut_Type()
)
portLineBuiltOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLineBuiltOut.setStatus("mandatory")
_Fme_modem_ObjectIdentity = ObjectIdentity
fme_modem = _Fme_modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 601)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANDATEL-FME-MODEM-MIB",
    **{"fme": fme,
       "fmeModemTable": fmeModemTable,
       "fmeTableEntry": fmeTableEntry,
       "mdmRack": mdmRack,
       "mdmModem": mdmModem,
       "mdmPosition": mdmPosition,
       "mdmModemName": mdmModemName,
       "mdmActiveLink": mdmActiveLink,
       "mdmAlarmConditionPort7": mdmAlarmConditionPort7,
       "mdmAlarmConditionPort8": mdmAlarmConditionPort8,
       "fmePortTable": fmePortTable,
       "fmePortEntry": fmePortEntry,
       "portRack": portRack,
       "portModem": portModem,
       "portPosition": portPosition,
       "portPort": portPort,
       "portInterfaceEmulationMode": portInterfaceEmulationMode,
       "mdmModemProperty": mdmModemProperty,
       "portClockSystem": portClockSystem,
       "portClockSource": portClockSource,
       "portDataRate": portDataRate,
       "portLocalCarrierDetect": portLocalCarrierDetect,
       "portTDPhaseLocking": portTDPhaseLocking,
       "portLineBuiltOut": portLineBuiltOut,
       "fme-modem": fme_modem}
)
