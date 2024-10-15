# SNMP MIB module (LSERIES-TAPE-LIBRARY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LSERIES-TAPE-LIBRARY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:24 2024
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



class LserSnmpPort(Integer32):
    """Custom type LserSnmpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(161, 161),
        ValueRangeConstraint(1024, 65535),
    )





class LserSnmpTrapPort(Integer32):
    """Custom type LserSnmpTrapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(162, 162),
        ValueRangeConstraint(1024, 65535),
    )





class LserCmdClear(Integer32):
    """Custom type LserCmdClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noaction", 1))
    )





class LserDeviceStatus(Integer32):
    """Custom type LserDeviceStatus based on Integer32"""
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
        *(("error", 3),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 4))
    )





class LserMediaErrorType(Integer32):
    """Custom type LserMediaErrorType based on Integer32"""
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
        *(("error", 3),
          ("load", 1),
          ("unknown", 4),
          ("unload", 2))
    )





class LserDriveFibreLoopId(Integer32):
    """Custom type LserDriveFibreLoopId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 125),
    )





class LserDriveFibreSpeed(Integer32):
    """Custom type LserDriveFibreSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneGbit", 2),
          ("twoGbit", 3),
          ("unknown", 1))
    )





class LserDriveFibreAddressing(Integer32):
    """Custom type LserDriveFibreAddressing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hard", 1),
          ("soft", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Storagetek_ObjectIdentity = ObjectIdentity
storagetek = _Storagetek_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1)
)
_LseriesTapeLibrary_ObjectIdentity = ObjectIdentity
lseriesTapeLibrary = _LseriesTapeLibrary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12)
)
_LserAgent_ObjectIdentity = ObjectIdentity
lserAgent = _LserAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 1)
)


class _LserAgentRevision_Type(OctetString):
    """Custom type lserAgentRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserAgentRevision_Type.__name__ = "OctetString"
_LserAgentRevision_Object = MibScalar
lserAgentRevision = _LserAgentRevision_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 1, 1),
    _LserAgentRevision_Type()
)
lserAgentRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserAgentRevision.setStatus("mandatory")


class _LserAgentBootDate_Type(OctetString):
    """Custom type lserAgentBootDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserAgentBootDate_Type.__name__ = "OctetString"
_LserAgentBootDate_Object = MibScalar
lserAgentBootDate = _LserAgentBootDate_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 1, 3),
    _LserAgentBootDate_Type()
)
lserAgentBootDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserAgentBootDate.setStatus("mandatory")


class _LserAgentURL_Type(OctetString):
    """Custom type lserAgentURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserAgentURL_Type.__name__ = "OctetString"
_LserAgentURL_Object = MibScalar
lserAgentURL = _LserAgentURL_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 1, 4),
    _LserAgentURL_Type()
)
lserAgentURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserAgentURL.setStatus("mandatory")
_LserAgentPort_Type = LserSnmpPort
_LserAgentPort_Object = MibScalar
lserAgentPort = _LserAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 1, 6),
    _LserAgentPort_Type()
)
lserAgentPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserAgentPort.setStatus("mandatory")


class _LserAgentCommunity_Type(OctetString):
    """Custom type lserAgentCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserAgentCommunity_Type.__name__ = "OctetString"
_LserAgentCommunity_Object = MibScalar
lserAgentCommunity = _LserAgentCommunity_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 1, 7),
    _LserAgentCommunity_Type()
)
lserAgentCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserAgentCommunity.setStatus("mandatory")
_LserAgentTrapSink_ObjectIdentity = ObjectIdentity
lserAgentTrapSink = _LserAgentTrapSink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 1, 8)
)
_LserAgentTrapSinkClear_Type = LserCmdClear
_LserAgentTrapSinkClear_Object = MibScalar
lserAgentTrapSinkClear = _LserAgentTrapSinkClear_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 1, 8, 1),
    _LserAgentTrapSinkClear_Type()
)
lserAgentTrapSinkClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserAgentTrapSinkClear.setStatus("mandatory")


class _LserAgentTrapSinkNum_Type(Integer32):
    """Custom type lserAgentTrapSinkNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_LserAgentTrapSinkNum_Type.__name__ = "Integer32"
_LserAgentTrapSinkNum_Object = MibScalar
lserAgentTrapSinkNum = _LserAgentTrapSinkNum_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 1, 8, 2),
    _LserAgentTrapSinkNum_Type()
)
lserAgentTrapSinkNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserAgentTrapSinkNum.setStatus("mandatory")
_LserAgentTrapSinkTable_Object = MibTable
lserAgentTrapSinkTable = _LserAgentTrapSinkTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 1, 8, 3)
)
if mibBuilder.loadTexts:
    lserAgentTrapSinkTable.setStatus("mandatory")
_LserAgentTrapSinkEntry_Object = MibTableRow
lserAgentTrapSinkEntry = _LserAgentTrapSinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 1, 8, 3, 1)
)
lserAgentTrapSinkEntry.setIndexNames(
    (0, "LSERIES-TAPE-LIBRARY-MIB", "lserAgentTrapSinkTableIndex"),
)
if mibBuilder.loadTexts:
    lserAgentTrapSinkEntry.setStatus("mandatory")
_LserAgentTrapSinkTableIndex_Type = Integer32
_LserAgentTrapSinkTableIndex_Object = MibTableColumn
lserAgentTrapSinkTableIndex = _LserAgentTrapSinkTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 1, 8, 3, 1, 1),
    _LserAgentTrapSinkTableIndex_Type()
)
lserAgentTrapSinkTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserAgentTrapSinkTableIndex.setStatus("mandatory")


class _LserAgentTrapSinkNetName_Type(OctetString):
    """Custom type lserAgentTrapSinkNetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserAgentTrapSinkNetName_Type.__name__ = "OctetString"
_LserAgentTrapSinkNetName_Object = MibTableColumn
lserAgentTrapSinkNetName = _LserAgentTrapSinkNetName_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 1, 8, 3, 1, 2),
    _LserAgentTrapSinkNetName_Type()
)
lserAgentTrapSinkNetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserAgentTrapSinkNetName.setStatus("mandatory")
_LserAgentTrapSinkPort_Type = LserSnmpTrapPort
_LserAgentTrapSinkPort_Object = MibTableColumn
lserAgentTrapSinkPort = _LserAgentTrapSinkPort_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 1, 8, 3, 1, 3),
    _LserAgentTrapSinkPort_Type()
)
lserAgentTrapSinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserAgentTrapSinkPort.setStatus("mandatory")


class _LserAgentTrapSinkCommunity_Type(OctetString):
    """Custom type lserAgentTrapSinkCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserAgentTrapSinkCommunity_Type.__name__ = "OctetString"
_LserAgentTrapSinkCommunity_Object = MibTableColumn
lserAgentTrapSinkCommunity = _LserAgentTrapSinkCommunity_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 1, 8, 3, 1, 4),
    _LserAgentTrapSinkCommunity_Type()
)
lserAgentTrapSinkCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserAgentTrapSinkCommunity.setStatus("mandatory")


class _LserAgentTrapSinkVersion_Type(Integer32):
    """Custom type lserAgentTrapSinkVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmpV1", 1),
          ("snmpV2", 2))
    )


_LserAgentTrapSinkVersion_Type.__name__ = "Integer32"
_LserAgentTrapSinkVersion_Object = MibTableColumn
lserAgentTrapSinkVersion = _LserAgentTrapSinkVersion_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 1, 8, 3, 1, 5),
    _LserAgentTrapSinkVersion_Type()
)
lserAgentTrapSinkVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserAgentTrapSinkVersion.setStatus("mandatory")
_LserAgentTrapSinkClearEntry_Type = LserCmdClear
_LserAgentTrapSinkClearEntry_Object = MibTableColumn
lserAgentTrapSinkClearEntry = _LserAgentTrapSinkClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 1, 8, 3, 1, 6),
    _LserAgentTrapSinkClearEntry_Type()
)
lserAgentTrapSinkClearEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserAgentTrapSinkClearEntry.setStatus("mandatory")
_LserTrap_ObjectIdentity = ObjectIdentity
lserTrap = _LserTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 2)
)


class _LserTrapText_Type(OctetString):
    """Custom type lserTrapText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LserTrapText_Type.__name__ = "OctetString"
_LserTrapText_Object = MibScalar
lserTrapText = _LserTrapText_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 2, 1),
    _LserTrapText_Type()
)
lserTrapText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserTrapText.setStatus("mandatory")


class _LserTrapSeverity_Type(Integer32):
    """Custom type lserTrapSeverity based on Integer32"""
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
        *(("configuration", 4),
          ("error", 1),
          ("info", 3),
          ("warning", 2))
    )


_LserTrapSeverity_Type.__name__ = "Integer32"
_LserTrapSeverity_Object = MibScalar
lserTrapSeverity = _LserTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 2, 2),
    _LserTrapSeverity_Type()
)
lserTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserTrapSeverity.setStatus("mandatory")
_LserLibrary_ObjectIdentity = ObjectIdentity
lserLibrary = _LserLibrary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3)
)


class _LserLibStkBaseModel_Type(OctetString):
    """Custom type lserLibStkBaseModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibStkBaseModel_Type.__name__ = "OctetString"
_LserLibStkBaseModel_Object = MibScalar
lserLibStkBaseModel = _LserLibStkBaseModel_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 1),
    _LserLibStkBaseModel_Type()
)
lserLibStkBaseModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStkBaseModel.setStatus("mandatory")


class _LserLibConfigPassword_Type(OctetString):
    """Custom type lserLibConfigPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibConfigPassword_Type.__name__ = "OctetString"
_LserLibConfigPassword_Object = MibScalar
lserLibConfigPassword = _LserLibConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 2),
    _LserLibConfigPassword_Type()
)
lserLibConfigPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    lserLibConfigPassword.setStatus("mandatory")
_LserLibVersion_ObjectIdentity = ObjectIdentity
lserLibVersion = _LserLibVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 3)
)


class _LserLibVersionFirmRev_Type(OctetString):
    """Custom type lserLibVersionFirmRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibVersionFirmRev_Type.__name__ = "OctetString"
_LserLibVersionFirmRev_Object = MibScalar
lserLibVersionFirmRev = _LserLibVersionFirmRev_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 3, 1),
    _LserLibVersionFirmRev_Type()
)
lserLibVersionFirmRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibVersionFirmRev.setStatus("mandatory")


class _LserLibVersionFirmDate_Type(OctetString):
    """Custom type lserLibVersionFirmDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibVersionFirmDate_Type.__name__ = "OctetString"
_LserLibVersionFirmDate_Object = MibScalar
lserLibVersionFirmDate = _LserLibVersionFirmDate_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 3, 2),
    _LserLibVersionFirmDate_Type()
)
lserLibVersionFirmDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibVersionFirmDate.setStatus("mandatory")


class _LserLibVersionBootRev_Type(OctetString):
    """Custom type lserLibVersionBootRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibVersionBootRev_Type.__name__ = "OctetString"
_LserLibVersionBootRev_Object = MibScalar
lserLibVersionBootRev = _LserLibVersionBootRev_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 3, 3),
    _LserLibVersionBootRev_Type()
)
lserLibVersionBootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibVersionBootRev.setStatus("mandatory")


class _LserLibVersionFibre_Type(OctetString):
    """Custom type lserLibVersionFibre based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibVersionFibre_Type.__name__ = "OctetString"
_LserLibVersionFibre_Object = MibScalar
lserLibVersionFibre = _LserLibVersionFibre_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 3, 4),
    _LserLibVersionFibre_Type()
)
lserLibVersionFibre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibVersionFibre.setStatus("mandatory")


class _LserLibVersionHardware_Type(OctetString):
    """Custom type lserLibVersionHardware based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibVersionHardware_Type.__name__ = "OctetString"
_LserLibVersionHardware_Object = MibScalar
lserLibVersionHardware = _LserLibVersionHardware_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 3, 5),
    _LserLibVersionHardware_Type()
)
lserLibVersionHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibVersionHardware.setStatus("mandatory")


class _LserLibSerialNumber_Type(OctetString):
    """Custom type lserLibSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibSerialNumber_Type.__name__ = "OctetString"
_LserLibSerialNumber_Object = MibScalar
lserLibSerialNumber = _LserLibSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 4),
    _LserLibSerialNumber_Type()
)
lserLibSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibSerialNumber.setStatus("mandatory")
_LserLibHostInterface_ObjectIdentity = ObjectIdentity
lserLibHostInterface = _LserLibHostInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 5)
)


class _LserLibHostInterfaceType_Type(OctetString):
    """Custom type lserLibHostInterfaceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibHostInterfaceType_Type.__name__ = "OctetString"
_LserLibHostInterfaceType_Object = MibScalar
lserLibHostInterfaceType = _LserLibHostInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 5, 1),
    _LserLibHostInterfaceType_Type()
)
lserLibHostInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibHostInterfaceType.setStatus("mandatory")
_LserLibConfig_ObjectIdentity = ObjectIdentity
lserLibConfig = _LserLibConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6)
)
_LserLibCfgNumPanels_Type = Integer32
_LserLibCfgNumPanels_Object = MibScalar
lserLibCfgNumPanels = _LserLibCfgNumPanels_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 1),
    _LserLibCfgNumPanels_Type()
)
lserLibCfgNumPanels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgNumPanels.setStatus("mandatory")
_LserLibCfgNumHandCells_Type = Integer32
_LserLibCfgNumHandCells_Object = MibScalar
lserLibCfgNumHandCells = _LserLibCfgNumHandCells_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 2),
    _LserLibCfgNumHandCells_Type()
)
lserLibCfgNumHandCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgNumHandCells.setStatus("mandatory")
_LserLibCfgMinHandAddr_Type = Integer32
_LserLibCfgMinHandAddr_Object = MibScalar
lserLibCfgMinHandAddr = _LserLibCfgMinHandAddr_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 3),
    _LserLibCfgMinHandAddr_Type()
)
lserLibCfgMinHandAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgMinHandAddr.setStatus("mandatory")
_LserLibCfgMaxHandAddr_Type = Integer32
_LserLibCfgMaxHandAddr_Object = MibScalar
lserLibCfgMaxHandAddr = _LserLibCfgMaxHandAddr_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 4),
    _LserLibCfgMaxHandAddr_Type()
)
lserLibCfgMaxHandAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgMaxHandAddr.setStatus("mandatory")
_LserLibCfgNumPlayCells_Type = Integer32
_LserLibCfgNumPlayCells_Object = MibScalar
lserLibCfgNumPlayCells = _LserLibCfgNumPlayCells_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 5),
    _LserLibCfgNumPlayCells_Type()
)
lserLibCfgNumPlayCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgNumPlayCells.setStatus("mandatory")
_LserLibCfgMinPlayAddr_Type = Integer32
_LserLibCfgMinPlayAddr_Object = MibScalar
lserLibCfgMinPlayAddr = _LserLibCfgMinPlayAddr_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 6),
    _LserLibCfgMinPlayAddr_Type()
)
lserLibCfgMinPlayAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgMinPlayAddr.setStatus("mandatory")
_LserLibCfgMaxPlayAddr_Type = Integer32
_LserLibCfgMaxPlayAddr_Object = MibScalar
lserLibCfgMaxPlayAddr = _LserLibCfgMaxPlayAddr_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 7),
    _LserLibCfgMaxPlayAddr_Type()
)
lserLibCfgMaxPlayAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgMaxPlayAddr.setStatus("mandatory")
_LserLibCfgNumCaps_Type = Integer32
_LserLibCfgNumCaps_Object = MibScalar
lserLibCfgNumCaps = _LserLibCfgNumCaps_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 8),
    _LserLibCfgNumCaps_Type()
)
lserLibCfgNumCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgNumCaps.setStatus("mandatory")
_LserLibCfgNumCapColumns_Type = Integer32
_LserLibCfgNumCapColumns_Object = MibScalar
lserLibCfgNumCapColumns = _LserLibCfgNumCapColumns_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 9),
    _LserLibCfgNumCapColumns_Type()
)
lserLibCfgNumCapColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgNumCapColumns.setStatus("mandatory")
_LserLibCfgNumCapCells_Type = Integer32
_LserLibCfgNumCapCells_Object = MibScalar
lserLibCfgNumCapCells = _LserLibCfgNumCapCells_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 10),
    _LserLibCfgNumCapCells_Type()
)
lserLibCfgNumCapCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgNumCapCells.setStatus("mandatory")
_LserLibCfgMinCapAddr_Type = Integer32
_LserLibCfgMinCapAddr_Object = MibScalar
lserLibCfgMinCapAddr = _LserLibCfgMinCapAddr_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 11),
    _LserLibCfgMinCapAddr_Type()
)
lserLibCfgMinCapAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgMinCapAddr.setStatus("mandatory")
_LserLibCfgMaxCapAddr_Type = Integer32
_LserLibCfgMaxCapAddr_Object = MibScalar
lserLibCfgMaxCapAddr = _LserLibCfgMaxCapAddr_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 12),
    _LserLibCfgMaxCapAddr_Type()
)
lserLibCfgMaxCapAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgMaxCapAddr.setStatus("mandatory")
_LserLibCfgNumDriveColumns_Type = Integer32
_LserLibCfgNumDriveColumns_Object = MibScalar
lserLibCfgNumDriveColumns = _LserLibCfgNumDriveColumns_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 13),
    _LserLibCfgNumDriveColumns_Type()
)
lserLibCfgNumDriveColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgNumDriveColumns.setStatus("mandatory")
_LserLibCfgNumDrives_Type = Integer32
_LserLibCfgNumDrives_Object = MibScalar
lserLibCfgNumDrives = _LserLibCfgNumDrives_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 14),
    _LserLibCfgNumDrives_Type()
)
lserLibCfgNumDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgNumDrives.setStatus("mandatory")
_LserLibCfgMinDriveAddr_Type = Integer32
_LserLibCfgMinDriveAddr_Object = MibScalar
lserLibCfgMinDriveAddr = _LserLibCfgMinDriveAddr_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 15),
    _LserLibCfgMinDriveAddr_Type()
)
lserLibCfgMinDriveAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgMinDriveAddr.setStatus("mandatory")
_LserLibCfgMaxDriveAddr_Type = Integer32
_LserLibCfgMaxDriveAddr_Object = MibScalar
lserLibCfgMaxDriveAddr = _LserLibCfgMaxDriveAddr_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 16),
    _LserLibCfgMaxDriveAddr_Type()
)
lserLibCfgMaxDriveAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgMaxDriveAddr.setStatus("mandatory")
_LserLibCfgNumStorageCells_Type = Integer32
_LserLibCfgNumStorageCells_Object = MibScalar
lserLibCfgNumStorageCells = _LserLibCfgNumStorageCells_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 17),
    _LserLibCfgNumStorageCells_Type()
)
lserLibCfgNumStorageCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgNumStorageCells.setStatus("mandatory")
_LserLibCfgMinStorageAddr_Type = Integer32
_LserLibCfgMinStorageAddr_Object = MibScalar
lserLibCfgMinStorageAddr = _LserLibCfgMinStorageAddr_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 18),
    _LserLibCfgMinStorageAddr_Type()
)
lserLibCfgMinStorageAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgMinStorageAddr.setStatus("mandatory")
_LserLibCfgMaxStorageAddr_Type = Integer32
_LserLibCfgMaxStorageAddr_Object = MibScalar
lserLibCfgMaxStorageAddr = _LserLibCfgMaxStorageAddr_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 19),
    _LserLibCfgMaxStorageAddr_Type()
)
lserLibCfgMaxStorageAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgMaxStorageAddr.setStatus("mandatory")
_LserLibCfgNumPtps_Type = Integer32
_LserLibCfgNumPtps_Object = MibScalar
lserLibCfgNumPtps = _LserLibCfgNumPtps_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 20),
    _LserLibCfgNumPtps_Type()
)
lserLibCfgNumPtps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgNumPtps.setStatus("mandatory")
_LserLibCfgNumPtpColumns_Type = Integer32
_LserLibCfgNumPtpColumns_Object = MibScalar
lserLibCfgNumPtpColumns = _LserLibCfgNumPtpColumns_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 21),
    _LserLibCfgNumPtpColumns_Type()
)
lserLibCfgNumPtpColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgNumPtpColumns.setStatus("mandatory")
_LserLibCfgNumPtpCells_Type = Integer32
_LserLibCfgNumPtpCells_Object = MibScalar
lserLibCfgNumPtpCells = _LserLibCfgNumPtpCells_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 22),
    _LserLibCfgNumPtpCells_Type()
)
lserLibCfgNumPtpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgNumPtpCells.setStatus("mandatory")
_LserLibCfgMinPtpAddr_Type = Integer32
_LserLibCfgMinPtpAddr_Object = MibScalar
lserLibCfgMinPtpAddr = _LserLibCfgMinPtpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 23),
    _LserLibCfgMinPtpAddr_Type()
)
lserLibCfgMinPtpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgMinPtpAddr.setStatus("mandatory")
_LserLibCfgMaxPtpAddr_Type = Integer32
_LserLibCfgMaxPtpAddr_Object = MibScalar
lserLibCfgMaxPtpAddr = _LserLibCfgMaxPtpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 6, 24),
    _LserLibCfgMaxPtpAddr_Type()
)
lserLibCfgMaxPtpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCfgMaxPtpAddr.setStatus("mandatory")


class _LserLibState_Type(OctetString):
    """Custom type lserLibState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibState_Type.__name__ = "OctetString"
_LserLibState_Object = MibScalar
lserLibState = _LserLibState_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 7),
    _LserLibState_Type()
)
lserLibState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibState.setStatus("mandatory")
_LserLibStatusEnum_Type = LserDeviceStatus
_LserLibStatusEnum_Object = MibScalar
lserLibStatusEnum = _LserLibStatusEnum_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 8),
    _LserLibStatusEnum_Type()
)
lserLibStatusEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStatusEnum.setStatus("mandatory")
_LserLibLog_ObjectIdentity = ObjectIdentity
lserLibLog = _LserLibLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 9)
)
_LserLibLogClear_Type = LserCmdClear
_LserLibLogClear_Object = MibScalar
lserLibLogClear = _LserLibLogClear_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 9, 1),
    _LserLibLogClear_Type()
)
lserLibLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibLogClear.setStatus("mandatory")
_LserLibLogNumFscs_Type = Integer32
_LserLibLogNumFscs_Object = MibScalar
lserLibLogNumFscs = _LserLibLogNumFscs_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 9, 2),
    _LserLibLogNumFscs_Type()
)
lserLibLogNumFscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibLogNumFscs.setStatus("mandatory")
_LserLibLogTable_Object = MibTable
lserLibLogTable = _LserLibLogTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 9, 3)
)
if mibBuilder.loadTexts:
    lserLibLogTable.setStatus("mandatory")
_LserLibLogEntry_Object = MibTableRow
lserLibLogEntry = _LserLibLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 9, 3, 1)
)
lserLibLogEntry.setIndexNames(
    (0, "LSERIES-TAPE-LIBRARY-MIB", "lserLibLogTableIndex"),
)
if mibBuilder.loadTexts:
    lserLibLogEntry.setStatus("mandatory")
_LserLibLogTableIndex_Type = Integer32
_LserLibLogTableIndex_Object = MibTableColumn
lserLibLogTableIndex = _LserLibLogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 9, 3, 1, 1),
    _LserLibLogTableIndex_Type()
)
lserLibLogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibLogTableIndex.setStatus("mandatory")
_LserLibLogFscNumber_Type = Integer32
_LserLibLogFscNumber_Object = MibTableColumn
lserLibLogFscNumber = _LserLibLogFscNumber_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 9, 3, 1, 2),
    _LserLibLogFscNumber_Type()
)
lserLibLogFscNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibLogFscNumber.setStatus("mandatory")


class _LserLibLogMechanism_Type(OctetString):
    """Custom type lserLibLogMechanism based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibLogMechanism_Type.__name__ = "OctetString"
_LserLibLogMechanism_Object = MibTableColumn
lserLibLogMechanism = _LserLibLogMechanism_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 9, 3, 1, 3),
    _LserLibLogMechanism_Type()
)
lserLibLogMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibLogMechanism.setStatus("mandatory")
_LserLibLogFscCount_Type = Integer32
_LserLibLogFscCount_Object = MibTableColumn
lserLibLogFscCount = _LserLibLogFscCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 9, 3, 1, 4),
    _LserLibLogFscCount_Type()
)
lserLibLogFscCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibLogFscCount.setStatus("mandatory")


class _LserLibLogDateTime_Type(OctetString):
    """Custom type lserLibLogDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibLogDateTime_Type.__name__ = "OctetString"
_LserLibLogDateTime_Object = MibTableColumn
lserLibLogDateTime = _LserLibLogDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 9, 3, 1, 5),
    _LserLibLogDateTime_Type()
)
lserLibLogDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibLogDateTime.setStatus("mandatory")


class _LserLibLogSummary_Type(OctetString):
    """Custom type lserLibLogSummary based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LserLibLogSummary_Type.__name__ = "OctetString"
_LserLibLogSummary_Object = MibTableColumn
lserLibLogSummary = _LserLibLogSummary_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 9, 3, 1, 6),
    _LserLibLogSummary_Type()
)
lserLibLogSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibLogSummary.setStatus("mandatory")


class _LserLibLogText_Type(OctetString):
    """Custom type lserLibLogText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_LserLibLogText_Type.__name__ = "OctetString"
_LserLibLogText_Object = MibTableColumn
lserLibLogText = _LserLibLogText_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 9, 3, 1, 7),
    _LserLibLogText_Type()
)
lserLibLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibLogText.setStatus("mandatory")
_LserLibLogClearEntry_Type = LserCmdClear
_LserLibLogClearEntry_Object = MibTableColumn
lserLibLogClearEntry = _LserLibLogClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 9, 3, 1, 8),
    _LserLibLogClearEntry_Type()
)
lserLibLogClearEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibLogClearEntry.setStatus("mandatory")


class _LserLibLogSeverity_Type(Integer32):
    """Custom type lserLibLogSeverity based on Integer32"""
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
        *(("error", 2),
          ("info", 4),
          ("silent", 1),
          ("warning", 3))
    )


_LserLibLogSeverity_Type.__name__ = "Integer32"
_LserLibLogSeverity_Object = MibTableColumn
lserLibLogSeverity = _LserLibLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 9, 3, 1, 9),
    _LserLibLogSeverity_Type()
)
lserLibLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibLogSeverity.setStatus("mandatory")
_LserLibDeviceID_Type = Integer32
_LserLibDeviceID_Object = MibScalar
lserLibDeviceID = _LserLibDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 10),
    _LserLibDeviceID_Type()
)
lserLibDeviceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibDeviceID.setStatus("mandatory")


class _LserLibFastLoad_Type(Integer32):
    """Custom type lserLibFastLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LserLibFastLoad_Type.__name__ = "Integer32"
_LserLibFastLoad_Object = MibScalar
lserLibFastLoad = _LserLibFastLoad_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 11),
    _LserLibFastLoad_Type()
)
lserLibFastLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibFastLoad.setStatus("mandatory")
_LserLibLocation_ObjectIdentity = ObjectIdentity
lserLibLocation = _LserLibLocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 12)
)


class _LserLibLocatContact_Type(OctetString):
    """Custom type lserLibLocatContact based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibLocatContact_Type.__name__ = "OctetString"
_LserLibLocatContact_Object = MibScalar
lserLibLocatContact = _LserLibLocatContact_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 12, 1),
    _LserLibLocatContact_Type()
)
lserLibLocatContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibLocatContact.setStatus("mandatory")


class _LserLibLocatStreet_Type(OctetString):
    """Custom type lserLibLocatStreet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibLocatStreet_Type.__name__ = "OctetString"
_LserLibLocatStreet_Object = MibScalar
lserLibLocatStreet = _LserLibLocatStreet_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 12, 2),
    _LserLibLocatStreet_Type()
)
lserLibLocatStreet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibLocatStreet.setStatus("mandatory")


class _LserLibLocatState_Type(OctetString):
    """Custom type lserLibLocatState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibLocatState_Type.__name__ = "OctetString"
_LserLibLocatState_Object = MibScalar
lserLibLocatState = _LserLibLocatState_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 12, 3),
    _LserLibLocatState_Type()
)
lserLibLocatState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibLocatState.setStatus("mandatory")


class _LserLibLocatZip_Type(OctetString):
    """Custom type lserLibLocatZip based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibLocatZip_Type.__name__ = "OctetString"
_LserLibLocatZip_Object = MibScalar
lserLibLocatZip = _LserLibLocatZip_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 12, 4),
    _LserLibLocatZip_Type()
)
lserLibLocatZip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibLocatZip.setStatus("mandatory")


class _LserLibLocatCountry_Type(OctetString):
    """Custom type lserLibLocatCountry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibLocatCountry_Type.__name__ = "OctetString"
_LserLibLocatCountry_Object = MibScalar
lserLibLocatCountry = _LserLibLocatCountry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 12, 5),
    _LserLibLocatCountry_Type()
)
lserLibLocatCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibLocatCountry.setStatus("mandatory")


class _LserLibLocatDescr_Type(OctetString):
    """Custom type lserLibLocatDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibLocatDescr_Type.__name__ = "OctetString"
_LserLibLocatDescr_Object = MibScalar
lserLibLocatDescr = _LserLibLocatDescr_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 12, 6),
    _LserLibLocatDescr_Type()
)
lserLibLocatDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibLocatDescr.setStatus("mandatory")


class _LserLibLocatCity_Type(OctetString):
    """Custom type lserLibLocatCity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibLocatCity_Type.__name__ = "OctetString"
_LserLibLocatCity_Object = MibScalar
lserLibLocatCity = _LserLibLocatCity_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 12, 7),
    _LserLibLocatCity_Type()
)
lserLibLocatCity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibLocatCity.setStatus("mandatory")
_LserLibNetwork_ObjectIdentity = ObjectIdentity
lserLibNetwork = _LserLibNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 13)
)


class _LserLibNetworkIpAddr_Type(OctetString):
    """Custom type lserLibNetworkIpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LserLibNetworkIpAddr_Type.__name__ = "OctetString"
_LserLibNetworkIpAddr_Object = MibScalar
lserLibNetworkIpAddr = _LserLibNetworkIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 13, 1),
    _LserLibNetworkIpAddr_Type()
)
lserLibNetworkIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibNetworkIpAddr.setStatus("mandatory")


class _LserLibNetworkGateway_Type(OctetString):
    """Custom type lserLibNetworkGateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LserLibNetworkGateway_Type.__name__ = "OctetString"
_LserLibNetworkGateway_Object = MibScalar
lserLibNetworkGateway = _LserLibNetworkGateway_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 13, 2),
    _LserLibNetworkGateway_Type()
)
lserLibNetworkGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibNetworkGateway.setStatus("mandatory")


class _LserLibNetworkEthAddr_Type(OctetString):
    """Custom type lserLibNetworkEthAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibNetworkEthAddr_Type.__name__ = "OctetString"
_LserLibNetworkEthAddr_Object = MibScalar
lserLibNetworkEthAddr = _LserLibNetworkEthAddr_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 13, 3),
    _LserLibNetworkEthAddr_Type()
)
lserLibNetworkEthAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibNetworkEthAddr.setStatus("mandatory")


class _LserLibNetworkName_Type(OctetString):
    """Custom type lserLibNetworkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LserLibNetworkName_Type.__name__ = "OctetString"
_LserLibNetworkName_Object = MibScalar
lserLibNetworkName = _LserLibNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 13, 4),
    _LserLibNetworkName_Type()
)
lserLibNetworkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibNetworkName.setStatus("mandatory")


class _LserLibNetworkNetmask_Type(OctetString):
    """Custom type lserLibNetworkNetmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LserLibNetworkNetmask_Type.__name__ = "OctetString"
_LserLibNetworkNetmask_Object = MibScalar
lserLibNetworkNetmask = _LserLibNetworkNetmask_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 13, 5),
    _LserLibNetworkNetmask_Type()
)
lserLibNetworkNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibNetworkNetmask.setStatus("mandatory")


class _LserLibNetworkFibrePresent_Type(Integer32):
    """Custom type lserLibNetworkFibrePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 1),
          ("present", 2))
    )


_LserLibNetworkFibrePresent_Type.__name__ = "Integer32"
_LserLibNetworkFibrePresent_Object = MibScalar
lserLibNetworkFibrePresent = _LserLibNetworkFibrePresent_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 13, 6),
    _LserLibNetworkFibrePresent_Type()
)
lserLibNetworkFibrePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibNetworkFibrePresent.setStatus("mandatory")


class _LserLibNetworkFibreID_Type(OctetString):
    """Custom type lserLibNetworkFibreID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibNetworkFibreID_Type.__name__ = "OctetString"
_LserLibNetworkFibreID_Object = MibScalar
lserLibNetworkFibreID = _LserLibNetworkFibreID_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 13, 7),
    _LserLibNetworkFibreID_Type()
)
lserLibNetworkFibreID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibNetworkFibreID.setStatus("mandatory")
_LserLibNetworkFibreNumPorts_Type = Integer32
_LserLibNetworkFibreNumPorts_Object = MibScalar
lserLibNetworkFibreNumPorts = _LserLibNetworkFibreNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 13, 8),
    _LserLibNetworkFibreNumPorts_Type()
)
lserLibNetworkFibreNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibNetworkFibreNumPorts.setStatus("mandatory")


class _LserLibNetworkDhcpEnabled_Type(Integer32):
    """Custom type lserLibNetworkDhcpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LserLibNetworkDhcpEnabled_Type.__name__ = "Integer32"
_LserLibNetworkDhcpEnabled_Object = MibScalar
lserLibNetworkDhcpEnabled = _LserLibNetworkDhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 13, 9),
    _LserLibNetworkDhcpEnabled_Type()
)
lserLibNetworkDhcpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibNetworkDhcpEnabled.setStatus("mandatory")


class _LserLibNetworkDomainName_Type(OctetString):
    """Custom type lserLibNetworkDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LserLibNetworkDomainName_Type.__name__ = "OctetString"
_LserLibNetworkDomainName_Object = MibScalar
lserLibNetworkDomainName = _LserLibNetworkDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 13, 10),
    _LserLibNetworkDomainName_Type()
)
lserLibNetworkDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibNetworkDomainName.setStatus("mandatory")


class _LserLibNetworkPrimaryDNS_Type(OctetString):
    """Custom type lserLibNetworkPrimaryDNS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LserLibNetworkPrimaryDNS_Type.__name__ = "OctetString"
_LserLibNetworkPrimaryDNS_Object = MibScalar
lserLibNetworkPrimaryDNS = _LserLibNetworkPrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 13, 11),
    _LserLibNetworkPrimaryDNS_Type()
)
lserLibNetworkPrimaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibNetworkPrimaryDNS.setStatus("mandatory")


class _LserLibNetworkSecondaryDNS_Type(OctetString):
    """Custom type lserLibNetworkSecondaryDNS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LserLibNetworkSecondaryDNS_Type.__name__ = "OctetString"
_LserLibNetworkSecondaryDNS_Object = MibScalar
lserLibNetworkSecondaryDNS = _LserLibNetworkSecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 13, 12),
    _LserLibNetworkSecondaryDNS_Type()
)
lserLibNetworkSecondaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibNetworkSecondaryDNS.setStatus("mandatory")
_LserLibStatistics_ObjectIdentity = ObjectIdentity
lserLibStatistics = _LserLibStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14)
)
_LserLibStatsNumIPL_Type = Integer32
_LserLibStatsNumIPL_Object = MibScalar
lserLibStatsNumIPL = _LserLibStatsNumIPL_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 1),
    _LserLibStatsNumIPL_Type()
)
lserLibStatsNumIPL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStatsNumIPL.setStatus("mandatory")
_LserLibStatsNumDoorOpens_Type = Integer32
_LserLibStatsNumDoorOpens_Object = MibScalar
lserLibStatsNumDoorOpens = _LserLibStatsNumDoorOpens_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 2),
    _LserLibStatsNumDoorOpens_Type()
)
lserLibStatsNumDoorOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStatsNumDoorOpens.setStatus("mandatory")
_LserLibStatsNumGetRetries_Type = Integer32
_LserLibStatsNumGetRetries_Object = MibScalar
lserLibStatsNumGetRetries = _LserLibStatsNumGetRetries_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 3),
    _LserLibStatsNumGetRetries_Type()
)
lserLibStatsNumGetRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStatsNumGetRetries.setStatus("mandatory")
_LserLibStatsNumGetFails_Type = Integer32
_LserLibStatsNumGetFails_Object = MibScalar
lserLibStatsNumGetFails = _LserLibStatsNumGetFails_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 4),
    _LserLibStatsNumGetFails_Type()
)
lserLibStatsNumGetFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStatsNumGetFails.setStatus("mandatory")
_LserLibStatsNumPutRetries_Type = Integer32
_LserLibStatsNumPutRetries_Object = MibScalar
lserLibStatsNumPutRetries = _LserLibStatsNumPutRetries_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 5),
    _LserLibStatsNumPutRetries_Type()
)
lserLibStatsNumPutRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStatsNumPutRetries.setStatus("mandatory")
_LserLibStatsNumPutFails_Type = Integer32
_LserLibStatsNumPutFails_Object = MibScalar
lserLibStatsNumPutFails = _LserLibStatsNumPutFails_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 6),
    _LserLibStatsNumPutFails_Type()
)
lserLibStatsNumPutFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStatsNumPutFails.setStatus("mandatory")
_LserLibStatsNumLabelRetries_Type = Integer32
_LserLibStatsNumLabelRetries_Object = MibScalar
lserLibStatsNumLabelRetries = _LserLibStatsNumLabelRetries_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 7),
    _LserLibStatsNumLabelRetries_Type()
)
lserLibStatsNumLabelRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStatsNumLabelRetries.setStatus("mandatory")
_LserLibStatsNumLabelFails_Type = Integer32
_LserLibStatsNumLabelFails_Object = MibScalar
lserLibStatsNumLabelFails = _LserLibStatsNumLabelFails_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 8),
    _LserLibStatsNumLabelFails_Type()
)
lserLibStatsNumLabelFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStatsNumLabelFails.setStatus("mandatory")
_LserLibStatsNumTargetRetries_Type = Integer32
_LserLibStatsNumTargetRetries_Object = MibScalar
lserLibStatsNumTargetRetries = _LserLibStatsNumTargetRetries_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 9),
    _LserLibStatsNumTargetRetries_Type()
)
lserLibStatsNumTargetRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStatsNumTargetRetries.setStatus("mandatory")
_LserLibStatsNumTargetFails_Type = Integer32
_LserLibStatsNumTargetFails_Object = MibScalar
lserLibStatsNumTargetFails = _LserLibStatsNumTargetFails_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 10),
    _LserLibStatsNumTargetFails_Type()
)
lserLibStatsNumTargetFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStatsNumTargetFails.setStatus("mandatory")
_LserLibStatsNumMoves_Type = Integer32
_LserLibStatsNumMoves_Object = MibScalar
lserLibStatsNumMoves = _LserLibStatsNumMoves_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 11),
    _LserLibStatsNumMoves_Type()
)
lserLibStatsNumMoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStatsNumMoves.setStatus("mandatory")
_LserLibStatsNumMounts_Type = Integer32
_LserLibStatsNumMounts_Object = MibScalar
lserLibStatsNumMounts = _LserLibStatsNumMounts_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 12),
    _LserLibStatsNumMounts_Type()
)
lserLibStatsNumMounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStatsNumMounts.setStatus("mandatory")
_LserLibStatsNumTargetReads_Type = Integer32
_LserLibStatsNumTargetReads_Object = MibScalar
lserLibStatsNumTargetReads = _LserLibStatsNumTargetReads_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 13),
    _LserLibStatsNumTargetReads_Type()
)
lserLibStatsNumTargetReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStatsNumTargetReads.setStatus("mandatory")
_LserLibStatsNumEmptyReads_Type = Integer32
_LserLibStatsNumEmptyReads_Object = MibScalar
lserLibStatsNumEmptyReads = _LserLibStatsNumEmptyReads_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 14),
    _LserLibStatsNumEmptyReads_Type()
)
lserLibStatsNumEmptyReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStatsNumEmptyReads.setStatus("mandatory")
_LserLibStatsNumLabelReads_Type = Integer32
_LserLibStatsNumLabelReads_Object = MibScalar
lserLibStatsNumLabelReads = _LserLibStatsNumLabelReads_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 15),
    _LserLibStatsNumLabelReads_Type()
)
lserLibStatsNumLabelReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStatsNumLabelReads.setStatus("mandatory")
_LserLibStats5minuteSample_ObjectIdentity = ObjectIdentity
lserLibStats5minuteSample = _LserLibStats5minuteSample_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16)
)
_LserLibStats5minSampleCount_Type = Integer32
_LserLibStats5minSampleCount_Object = MibScalar
lserLibStats5minSampleCount = _LserLibStats5minSampleCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 1),
    _LserLibStats5minSampleCount_Type()
)
lserLibStats5minSampleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5minSampleCount.setStatus("mandatory")
_LserLibStats5minIdle_Type = Integer32
_LserLibStats5minIdle_Object = MibScalar
lserLibStats5minIdle = _LserLibStats5minIdle_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 2),
    _LserLibStats5minIdle_Type()
)
lserLibStats5minIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5minIdle.setStatus("mandatory")
_LserLibStats5min1to25_Type = Integer32
_LserLibStats5min1to25_Object = MibScalar
lserLibStats5min1to25 = _LserLibStats5min1to25_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 3),
    _LserLibStats5min1to25_Type()
)
lserLibStats5min1to25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min1to25.setStatus("mandatory")
_LserLibStats5min26to50_Type = Integer32
_LserLibStats5min26to50_Object = MibScalar
lserLibStats5min26to50 = _LserLibStats5min26to50_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 4),
    _LserLibStats5min26to50_Type()
)
lserLibStats5min26to50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min26to50.setStatus("mandatory")
_LserLibStats5min51to75_Type = Integer32
_LserLibStats5min51to75_Object = MibScalar
lserLibStats5min51to75 = _LserLibStats5min51to75_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 5),
    _LserLibStats5min51to75_Type()
)
lserLibStats5min51to75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min51to75.setStatus("mandatory")
_LserLibStats5min76to100_Type = Integer32
_LserLibStats5min76to100_Object = MibScalar
lserLibStats5min76to100 = _LserLibStats5min76to100_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 6),
    _LserLibStats5min76to100_Type()
)
lserLibStats5min76to100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min76to100.setStatus("mandatory")
_LserLibStats5min101to125_Type = Integer32
_LserLibStats5min101to125_Object = MibScalar
lserLibStats5min101to125 = _LserLibStats5min101to125_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 7),
    _LserLibStats5min101to125_Type()
)
lserLibStats5min101to125.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min101to125.setStatus("mandatory")
_LserLibStats5min126to150_Type = Integer32
_LserLibStats5min126to150_Object = MibScalar
lserLibStats5min126to150 = _LserLibStats5min126to150_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 8),
    _LserLibStats5min126to150_Type()
)
lserLibStats5min126to150.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min126to150.setStatus("mandatory")
_LserLibStats5min151to175_Type = Integer32
_LserLibStats5min151to175_Object = MibScalar
lserLibStats5min151to175 = _LserLibStats5min151to175_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 9),
    _LserLibStats5min151to175_Type()
)
lserLibStats5min151to175.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min151to175.setStatus("mandatory")
_LserLibStats5min176to200_Type = Integer32
_LserLibStats5min176to200_Object = MibScalar
lserLibStats5min176to200 = _LserLibStats5min176to200_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 10),
    _LserLibStats5min176to200_Type()
)
lserLibStats5min176to200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min176to200.setStatus("mandatory")
_LserLibStats5min201to225_Type = Integer32
_LserLibStats5min201to225_Object = MibScalar
lserLibStats5min201to225 = _LserLibStats5min201to225_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 11),
    _LserLibStats5min201to225_Type()
)
lserLibStats5min201to225.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min201to225.setStatus("mandatory")
_LserLibStats5min226to250_Type = Integer32
_LserLibStats5min226to250_Object = MibScalar
lserLibStats5min226to250 = _LserLibStats5min226to250_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 12),
    _LserLibStats5min226to250_Type()
)
lserLibStats5min226to250.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min226to250.setStatus("mandatory")
_LserLibStats5min251to300_Type = Integer32
_LserLibStats5min251to300_Object = MibScalar
lserLibStats5min251to300 = _LserLibStats5min251to300_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 13),
    _LserLibStats5min251to300_Type()
)
lserLibStats5min251to300.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min251to300.setStatus("mandatory")
_LserLibStats5min301to350_Type = Integer32
_LserLibStats5min301to350_Object = MibScalar
lserLibStats5min301to350 = _LserLibStats5min301to350_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 14),
    _LserLibStats5min301to350_Type()
)
lserLibStats5min301to350.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min301to350.setStatus("mandatory")
_LserLibStats5min351to400_Type = Integer32
_LserLibStats5min351to400_Object = MibScalar
lserLibStats5min351to400 = _LserLibStats5min351to400_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 15),
    _LserLibStats5min351to400_Type()
)
lserLibStats5min351to400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min351to400.setStatus("mandatory")
_LserLibStats5min401to450_Type = Integer32
_LserLibStats5min401to450_Object = MibScalar
lserLibStats5min401to450 = _LserLibStats5min401to450_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 16),
    _LserLibStats5min401to450_Type()
)
lserLibStats5min401to450.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min401to450.setStatus("mandatory")
_LserLibStats5min451to500_Type = Integer32
_LserLibStats5min451to500_Object = MibScalar
lserLibStats5min451to500 = _LserLibStats5min451to500_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 17),
    _LserLibStats5min451to500_Type()
)
lserLibStats5min451to500.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min451to500.setStatus("mandatory")
_LserLibStats5min501to550_Type = Integer32
_LserLibStats5min501to550_Object = MibScalar
lserLibStats5min501to550 = _LserLibStats5min501to550_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 18),
    _LserLibStats5min501to550_Type()
)
lserLibStats5min501to550.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min501to550.setStatus("mandatory")
_LserLibStats5min551to600_Type = Integer32
_LserLibStats5min551to600_Object = MibScalar
lserLibStats5min551to600 = _LserLibStats5min551to600_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 19),
    _LserLibStats5min551to600_Type()
)
lserLibStats5min551to600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min551to600.setStatus("mandatory")
_LserLibStats5min601to650_Type = Integer32
_LserLibStats5min601to650_Object = MibScalar
lserLibStats5min601to650 = _LserLibStats5min601to650_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 20),
    _LserLibStats5min601to650_Type()
)
lserLibStats5min601to650.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min601to650.setStatus("mandatory")
_LserLibStats5min651to700_Type = Integer32
_LserLibStats5min651to700_Object = MibScalar
lserLibStats5min651to700 = _LserLibStats5min651to700_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 21),
    _LserLibStats5min651to700_Type()
)
lserLibStats5min651to700.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5min651to700.setStatus("mandatory")
_LserLibStats5minOver700_Type = Integer32
_LserLibStats5minOver700_Object = MibScalar
lserLibStats5minOver700 = _LserLibStats5minOver700_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 16, 22),
    _LserLibStats5minOver700_Type()
)
lserLibStats5minOver700.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats5minOver700.setStatus("mandatory")
_LserLibStats15minuteSample_ObjectIdentity = ObjectIdentity
lserLibStats15minuteSample = _LserLibStats15minuteSample_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17)
)
_LserLibStats15minSampleCount_Type = Integer32
_LserLibStats15minSampleCount_Object = MibScalar
lserLibStats15minSampleCount = _LserLibStats15minSampleCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 1),
    _LserLibStats15minSampleCount_Type()
)
lserLibStats15minSampleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15minSampleCount.setStatus("mandatory")
_LserLibStats15minIdle_Type = Integer32
_LserLibStats15minIdle_Object = MibScalar
lserLibStats15minIdle = _LserLibStats15minIdle_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 2),
    _LserLibStats15minIdle_Type()
)
lserLibStats15minIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15minIdle.setStatus("mandatory")
_LserLibStats15min1to25_Type = Integer32
_LserLibStats15min1to25_Object = MibScalar
lserLibStats15min1to25 = _LserLibStats15min1to25_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 3),
    _LserLibStats15min1to25_Type()
)
lserLibStats15min1to25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min1to25.setStatus("mandatory")
_LserLibStats15min26to50_Type = Integer32
_LserLibStats15min26to50_Object = MibScalar
lserLibStats15min26to50 = _LserLibStats15min26to50_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 4),
    _LserLibStats15min26to50_Type()
)
lserLibStats15min26to50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min26to50.setStatus("mandatory")
_LserLibStats15min51to75_Type = Integer32
_LserLibStats15min51to75_Object = MibScalar
lserLibStats15min51to75 = _LserLibStats15min51to75_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 5),
    _LserLibStats15min51to75_Type()
)
lserLibStats15min51to75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min51to75.setStatus("mandatory")
_LserLibStats15min76to100_Type = Integer32
_LserLibStats15min76to100_Object = MibScalar
lserLibStats15min76to100 = _LserLibStats15min76to100_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 6),
    _LserLibStats15min76to100_Type()
)
lserLibStats15min76to100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min76to100.setStatus("mandatory")
_LserLibStats15min101to125_Type = Integer32
_LserLibStats15min101to125_Object = MibScalar
lserLibStats15min101to125 = _LserLibStats15min101to125_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 7),
    _LserLibStats15min101to125_Type()
)
lserLibStats15min101to125.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min101to125.setStatus("mandatory")
_LserLibStats15min126to150_Type = Integer32
_LserLibStats15min126to150_Object = MibScalar
lserLibStats15min126to150 = _LserLibStats15min126to150_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 8),
    _LserLibStats15min126to150_Type()
)
lserLibStats15min126to150.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min126to150.setStatus("mandatory")
_LserLibStats15min151to175_Type = Integer32
_LserLibStats15min151to175_Object = MibScalar
lserLibStats15min151to175 = _LserLibStats15min151to175_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 9),
    _LserLibStats15min151to175_Type()
)
lserLibStats15min151to175.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min151to175.setStatus("mandatory")
_LserLibStats15min176to200_Type = Integer32
_LserLibStats15min176to200_Object = MibScalar
lserLibStats15min176to200 = _LserLibStats15min176to200_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 10),
    _LserLibStats15min176to200_Type()
)
lserLibStats15min176to200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min176to200.setStatus("mandatory")
_LserLibStats15min201to225_Type = Integer32
_LserLibStats15min201to225_Object = MibScalar
lserLibStats15min201to225 = _LserLibStats15min201to225_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 11),
    _LserLibStats15min201to225_Type()
)
lserLibStats15min201to225.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min201to225.setStatus("mandatory")
_LserLibStats15min226to250_Type = Integer32
_LserLibStats15min226to250_Object = MibScalar
lserLibStats15min226to250 = _LserLibStats15min226to250_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 12),
    _LserLibStats15min226to250_Type()
)
lserLibStats15min226to250.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min226to250.setStatus("mandatory")
_LserLibStats15min251to300_Type = Integer32
_LserLibStats15min251to300_Object = MibScalar
lserLibStats15min251to300 = _LserLibStats15min251to300_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 13),
    _LserLibStats15min251to300_Type()
)
lserLibStats15min251to300.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min251to300.setStatus("mandatory")
_LserLibStats15min301to350_Type = Integer32
_LserLibStats15min301to350_Object = MibScalar
lserLibStats15min301to350 = _LserLibStats15min301to350_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 14),
    _LserLibStats15min301to350_Type()
)
lserLibStats15min301to350.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min301to350.setStatus("mandatory")
_LserLibStats15min351to400_Type = Integer32
_LserLibStats15min351to400_Object = MibScalar
lserLibStats15min351to400 = _LserLibStats15min351to400_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 15),
    _LserLibStats15min351to400_Type()
)
lserLibStats15min351to400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min351to400.setStatus("mandatory")
_LserLibStats15min401to450_Type = Integer32
_LserLibStats15min401to450_Object = MibScalar
lserLibStats15min401to450 = _LserLibStats15min401to450_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 16),
    _LserLibStats15min401to450_Type()
)
lserLibStats15min401to450.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min401to450.setStatus("mandatory")
_LserLibStats15min451to500_Type = Integer32
_LserLibStats15min451to500_Object = MibScalar
lserLibStats15min451to500 = _LserLibStats15min451to500_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 17),
    _LserLibStats15min451to500_Type()
)
lserLibStats15min451to500.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min451to500.setStatus("mandatory")
_LserLibStats15min501to550_Type = Integer32
_LserLibStats15min501to550_Object = MibScalar
lserLibStats15min501to550 = _LserLibStats15min501to550_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 18),
    _LserLibStats15min501to550_Type()
)
lserLibStats15min501to550.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min501to550.setStatus("mandatory")
_LserLibStats15min551to600_Type = Integer32
_LserLibStats15min551to600_Object = MibScalar
lserLibStats15min551to600 = _LserLibStats15min551to600_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 19),
    _LserLibStats15min551to600_Type()
)
lserLibStats15min551to600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min551to600.setStatus("mandatory")
_LserLibStats15min601to650_Type = Integer32
_LserLibStats15min601to650_Object = MibScalar
lserLibStats15min601to650 = _LserLibStats15min601to650_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 20),
    _LserLibStats15min601to650_Type()
)
lserLibStats15min601to650.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min601to650.setStatus("mandatory")
_LserLibStats15min651to700_Type = Integer32
_LserLibStats15min651to700_Object = MibScalar
lserLibStats15min651to700 = _LserLibStats15min651to700_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 21),
    _LserLibStats15min651to700_Type()
)
lserLibStats15min651to700.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15min651to700.setStatus("mandatory")
_LserLibStats15minOver700_Type = Integer32
_LserLibStats15minOver700_Object = MibScalar
lserLibStats15minOver700 = _LserLibStats15minOver700_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 17, 22),
    _LserLibStats15minOver700_Type()
)
lserLibStats15minOver700.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibStats15minOver700.setStatus("mandatory")
_LserLibStatsGlobalClear_Type = LserCmdClear
_LserLibStatsGlobalClear_Object = MibScalar
lserLibStatsGlobalClear = _LserLibStatsGlobalClear_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 18),
    _LserLibStatsGlobalClear_Type()
)
lserLibStatsGlobalClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibStatsGlobalClear.setStatus("mandatory")
_LserLibMediaErrors_ObjectIdentity = ObjectIdentity
lserLibMediaErrors = _LserLibMediaErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 19)
)
_LserMediaErrorCount_Type = Integer32
_LserMediaErrorCount_Object = MibScalar
lserMediaErrorCount = _LserMediaErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 19, 1),
    _LserMediaErrorCount_Type()
)
lserMediaErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserMediaErrorCount.setStatus("mandatory")
_LserLibMediaErrorTable_Object = MibTable
lserLibMediaErrorTable = _LserLibMediaErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 19, 2)
)
if mibBuilder.loadTexts:
    lserLibMediaErrorTable.setStatus("mandatory")
_LserLibMediaErrorEntry_Object = MibTableRow
lserLibMediaErrorEntry = _LserLibMediaErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 19, 2, 1)
)
lserLibMediaErrorEntry.setIndexNames(
    (0, "LSERIES-TAPE-LIBRARY-MIB", "lserMediaErrorIndex"),
)
if mibBuilder.loadTexts:
    lserLibMediaErrorEntry.setStatus("mandatory")
_LserMediaErrorIndex_Type = Integer32
_LserMediaErrorIndex_Object = MibTableColumn
lserMediaErrorIndex = _LserMediaErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 19, 2, 1, 1),
    _LserMediaErrorIndex_Type()
)
lserMediaErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserMediaErrorIndex.setStatus("mandatory")


class _LserMediaErrorTapeLabel_Type(OctetString):
    """Custom type lserMediaErrorTapeLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserMediaErrorTapeLabel_Type.__name__ = "OctetString"
_LserMediaErrorTapeLabel_Object = MibTableColumn
lserMediaErrorTapeLabel = _LserMediaErrorTapeLabel_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 19, 2, 1, 2),
    _LserMediaErrorTapeLabel_Type()
)
lserMediaErrorTapeLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserMediaErrorTapeLabel.setStatus("mandatory")


class _LserMediaErrorDriveSerialNum_Type(OctetString):
    """Custom type lserMediaErrorDriveSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserMediaErrorDriveSerialNum_Type.__name__ = "OctetString"
_LserMediaErrorDriveSerialNum_Object = MibTableColumn
lserMediaErrorDriveSerialNum = _LserMediaErrorDriveSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 19, 2, 1, 3),
    _LserMediaErrorDriveSerialNum_Type()
)
lserMediaErrorDriveSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserMediaErrorDriveSerialNum.setStatus("mandatory")


class _LserMediaErrorDateTime_Type(OctetString):
    """Custom type lserMediaErrorDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserMediaErrorDateTime_Type.__name__ = "OctetString"
_LserMediaErrorDateTime_Object = MibTableColumn
lserMediaErrorDateTime = _LserMediaErrorDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 19, 2, 1, 4),
    _LserMediaErrorDateTime_Type()
)
lserMediaErrorDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserMediaErrorDateTime.setStatus("mandatory")
_LserLibMediaErrorEnum_Type = LserMediaErrorType
_LserLibMediaErrorEnum_Object = MibTableColumn
lserLibMediaErrorEnum = _LserLibMediaErrorEnum_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 19, 2, 1, 5),
    _LserLibMediaErrorEnum_Type()
)
lserLibMediaErrorEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibMediaErrorEnum.setStatus("mandatory")
_LserMediaErrorOccurrenceCount_Type = Integer32
_LserMediaErrorOccurrenceCount_Object = MibTableColumn
lserMediaErrorOccurrenceCount = _LserMediaErrorOccurrenceCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 14, 19, 2, 1, 6),
    _LserMediaErrorOccurrenceCount_Type()
)
lserMediaErrorOccurrenceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserMediaErrorOccurrenceCount.setStatus("mandatory")
_LserLibDate_ObjectIdentity = ObjectIdentity
lserLibDate = _LserLibDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 15)
)
_LserLibDateMonth_Type = Integer32
_LserLibDateMonth_Object = MibScalar
lserLibDateMonth = _LserLibDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 15, 1),
    _LserLibDateMonth_Type()
)
lserLibDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibDateMonth.setStatus("mandatory")
_LserLibDateDay_Type = Integer32
_LserLibDateDay_Object = MibScalar
lserLibDateDay = _LserLibDateDay_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 15, 2),
    _LserLibDateDay_Type()
)
lserLibDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibDateDay.setStatus("mandatory")
_LserLibDateYear_Type = Integer32
_LserLibDateYear_Object = MibScalar
lserLibDateYear = _LserLibDateYear_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 15, 3),
    _LserLibDateYear_Type()
)
lserLibDateYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibDateYear.setStatus("mandatory")
_LserLibDateHour_Type = Integer32
_LserLibDateHour_Object = MibScalar
lserLibDateHour = _LserLibDateHour_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 15, 4),
    _LserLibDateHour_Type()
)
lserLibDateHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibDateHour.setStatus("mandatory")
_LserLibDateMinute_Type = Integer32
_LserLibDateMinute_Object = MibScalar
lserLibDateMinute = _LserLibDateMinute_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 15, 5),
    _LserLibDateMinute_Type()
)
lserLibDateMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibDateMinute.setStatus("mandatory")
_LserLibDateSecond_Type = Integer32
_LserLibDateSecond_Object = MibScalar
lserLibDateSecond = _LserLibDateSecond_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 15, 6),
    _LserLibDateSecond_Type()
)
lserLibDateSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibDateSecond.setStatus("mandatory")


class _LserLibDateString_Type(OctetString):
    """Custom type lserLibDateString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibDateString_Type.__name__ = "OctetString"
_LserLibDateString_Object = MibScalar
lserLibDateString = _LserLibDateString_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 15, 7),
    _LserLibDateString_Type()
)
lserLibDateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibDateString.setStatus("mandatory")
_LserLibPersonality_ObjectIdentity = ObjectIdentity
lserLibPersonality = _LserLibPersonality_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 16)
)


class _LserLibPersonVendor_Type(OctetString):
    """Custom type lserLibPersonVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibPersonVendor_Type.__name__ = "OctetString"
_LserLibPersonVendor_Object = MibScalar
lserLibPersonVendor = _LserLibPersonVendor_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 16, 1),
    _LserLibPersonVendor_Type()
)
lserLibPersonVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibPersonVendor.setStatus("mandatory")


class _LserLibPersonModel_Type(OctetString):
    """Custom type lserLibPersonModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibPersonModel_Type.__name__ = "OctetString"
_LserLibPersonModel_Object = MibScalar
lserLibPersonModel = _LserLibPersonModel_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 16, 2),
    _LserLibPersonModel_Type()
)
lserLibPersonModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibPersonModel.setStatus("mandatory")


class _LserLibPersonWebEnabled_Type(Integer32):
    """Custom type lserLibPersonWebEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LserLibPersonWebEnabled_Type.__name__ = "Integer32"
_LserLibPersonWebEnabled_Object = MibScalar
lserLibPersonWebEnabled = _LserLibPersonWebEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 16, 3),
    _LserLibPersonWebEnabled_Type()
)
lserLibPersonWebEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibPersonWebEnabled.setStatus("mandatory")


class _LserLibPersonLibSize_Type(OctetString):
    """Custom type lserLibPersonLibSize based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibPersonLibSize_Type.__name__ = "OctetString"
_LserLibPersonLibSize_Object = MibScalar
lserLibPersonLibSize = _LserLibPersonLibSize_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 16, 4),
    _LserLibPersonLibSize_Type()
)
lserLibPersonLibSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibPersonLibSize.setStatus("mandatory")
_LserLibCleaning_ObjectIdentity = ObjectIdentity
lserLibCleaning = _LserLibCleaning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 17)
)


class _LserLibCleanEnabled_Type(Integer32):
    """Custom type lserLibCleanEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LserLibCleanEnabled_Type.__name__ = "Integer32"
_LserLibCleanEnabled_Object = MibScalar
lserLibCleanEnabled = _LserLibCleanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 17, 1),
    _LserLibCleanEnabled_Type()
)
lserLibCleanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibCleanEnabled.setStatus("mandatory")
_LserLibCleanNumCartTypes_Type = Integer32
_LserLibCleanNumCartTypes_Object = MibScalar
lserLibCleanNumCartTypes = _LserLibCleanNumCartTypes_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 17, 2),
    _LserLibCleanNumCartTypes_Type()
)
lserLibCleanNumCartTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCleanNumCartTypes.setStatus("mandatory")
_LserLibCleanWarnTable_Object = MibTable
lserLibCleanWarnTable = _LserLibCleanWarnTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 17, 3)
)
if mibBuilder.loadTexts:
    lserLibCleanWarnTable.setStatus("mandatory")
_LserLibCleanWarnEntry_Object = MibTableRow
lserLibCleanWarnEntry = _LserLibCleanWarnEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 17, 3, 1)
)
lserLibCleanWarnEntry.setIndexNames(
    (0, "LSERIES-TAPE-LIBRARY-MIB", "lserLibCleanWarnIndex"),
)
if mibBuilder.loadTexts:
    lserLibCleanWarnEntry.setStatus("mandatory")
_LserLibCleanWarnIndex_Type = Integer32
_LserLibCleanWarnIndex_Object = MibTableColumn
lserLibCleanWarnIndex = _LserLibCleanWarnIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 17, 3, 1, 1),
    _LserLibCleanWarnIndex_Type()
)
lserLibCleanWarnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCleanWarnIndex.setStatus("mandatory")


class _LserLibCleanCartType_Type(OctetString):
    """Custom type lserLibCleanCartType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserLibCleanCartType_Type.__name__ = "OctetString"
_LserLibCleanCartType_Object = MibTableColumn
lserLibCleanCartType = _LserLibCleanCartType_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 17, 3, 1, 2),
    _LserLibCleanCartType_Type()
)
lserLibCleanCartType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCleanCartType.setStatus("mandatory")
_LserLibCleanWarnCount_Type = Integer32
_LserLibCleanWarnCount_Object = MibTableColumn
lserLibCleanWarnCount = _LserLibCleanWarnCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 17, 3, 1, 3),
    _LserLibCleanWarnCount_Type()
)
lserLibCleanWarnCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserLibCleanWarnCount.setStatus("mandatory")
_LserLibCleanNumCarts_Type = Integer32
_LserLibCleanNumCarts_Object = MibScalar
lserLibCleanNumCarts = _LserLibCleanNumCarts_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 17, 4),
    _LserLibCleanNumCarts_Type()
)
lserLibCleanNumCarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserLibCleanNumCarts.setStatus("mandatory")
_LserLibCleanCartTable_Object = MibTable
lserLibCleanCartTable = _LserLibCleanCartTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 17, 5)
)
if mibBuilder.loadTexts:
    lserLibCleanCartTable.setStatus("mandatory")
_LserLibCleanCartEntry_Object = MibTableRow
lserLibCleanCartEntry = _LserLibCleanCartEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 17, 5, 1)
)
lserLibCleanCartEntry.setIndexNames(
    (0, "LSERIES-TAPE-LIBRARY-MIB", "lserCleanCartIndex"),
)
if mibBuilder.loadTexts:
    lserLibCleanCartEntry.setStatus("mandatory")
_LserCleanCartIndex_Type = Integer32
_LserCleanCartIndex_Object = MibTableColumn
lserCleanCartIndex = _LserCleanCartIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 17, 5, 1, 1),
    _LserCleanCartIndex_Type()
)
lserCleanCartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCleanCartIndex.setStatus("mandatory")


class _LserCleanCartLabel_Type(OctetString):
    """Custom type lserCleanCartLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserCleanCartLabel_Type.__name__ = "OctetString"
_LserCleanCartLabel_Object = MibTableColumn
lserCleanCartLabel = _LserCleanCartLabel_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 17, 5, 1, 2),
    _LserCleanCartLabel_Type()
)
lserCleanCartLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCleanCartLabel.setStatus("mandatory")


class _LserCleanCartType_Type(OctetString):
    """Custom type lserCleanCartType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserCleanCartType_Type.__name__ = "OctetString"
_LserCleanCartType_Object = MibTableColumn
lserCleanCartType = _LserCleanCartType_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 17, 5, 1, 3),
    _LserCleanCartType_Type()
)
lserCleanCartType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCleanCartType.setStatus("mandatory")
_LserCleanCartLocationElementID_Type = Integer32
_LserCleanCartLocationElementID_Object = MibTableColumn
lserCleanCartLocationElementID = _LserCleanCartLocationElementID_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 17, 5, 1, 4),
    _LserCleanCartLocationElementID_Type()
)
lserCleanCartLocationElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCleanCartLocationElementID.setStatus("mandatory")


class _LserCleanCartHostAccessible_Type(Integer32):
    """Custom type lserCleanCartHostAccessible based on Integer32"""
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


_LserCleanCartHostAccessible_Type.__name__ = "Integer32"
_LserCleanCartHostAccessible_Object = MibTableColumn
lserCleanCartHostAccessible = _LserCleanCartHostAccessible_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 17, 5, 1, 5),
    _LserCleanCartHostAccessible_Type()
)
lserCleanCartHostAccessible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCleanCartHostAccessible.setStatus("mandatory")
_LserCleanCartUsageCount_Type = Integer32
_LserCleanCartUsageCount_Object = MibTableColumn
lserCleanCartUsageCount = _LserCleanCartUsageCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 3, 17, 5, 1, 6),
    _LserCleanCartUsageCount_Type()
)
lserCleanCartUsageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCleanCartUsageCount.setStatus("mandatory")
_LserDrives_ObjectIdentity = ObjectIdentity
lserDrives = _LserDrives_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4)
)
_LserDriveCount_Type = Integer32
_LserDriveCount_Object = MibScalar
lserDriveCount = _LserDriveCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 1),
    _LserDriveCount_Type()
)
lserDriveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveCount.setStatus("mandatory")
_LserDriveTable_Object = MibTable
lserDriveTable = _LserDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2)
)
if mibBuilder.loadTexts:
    lserDriveTable.setStatus("mandatory")
_LserDriveEntry_Object = MibTableRow
lserDriveEntry = _LserDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1)
)
lserDriveEntry.setIndexNames(
    (0, "LSERIES-TAPE-LIBRARY-MIB", "lserDriveIndex"),
)
if mibBuilder.loadTexts:
    lserDriveEntry.setStatus("mandatory")
_LserDriveIndex_Type = Integer32
_LserDriveIndex_Object = MibTableColumn
lserDriveIndex = _LserDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 1),
    _LserDriveIndex_Type()
)
lserDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveIndex.setStatus("mandatory")
_LserDriveElementID_Type = Integer32
_LserDriveElementID_Object = MibTableColumn
lserDriveElementID = _LserDriveElementID_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 2),
    _LserDriveElementID_Type()
)
lserDriveElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveElementID.setStatus("mandatory")
_LserDriveRowInLib_Type = Integer32
_LserDriveRowInLib_Object = MibTableColumn
lserDriveRowInLib = _LserDriveRowInLib_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 3),
    _LserDriveRowInLib_Type()
)
lserDriveRowInLib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveRowInLib.setStatus("mandatory")
_LserDriveColInLib_Type = Integer32
_LserDriveColInLib_Object = MibTableColumn
lserDriveColInLib = _LserDriveColInLib_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 4),
    _LserDriveColInLib_Type()
)
lserDriveColInLib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveColInLib.setStatus("mandatory")


class _LserDriveType_Type(OctetString):
    """Custom type lserDriveType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserDriveType_Type.__name__ = "OctetString"
_LserDriveType_Object = MibTableColumn
lserDriveType = _LserDriveType_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 5),
    _LserDriveType_Type()
)
lserDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveType.setStatus("mandatory")


class _LserDriveVendor_Type(OctetString):
    """Custom type lserDriveVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserDriveVendor_Type.__name__ = "OctetString"
_LserDriveVendor_Object = MibTableColumn
lserDriveVendor = _LserDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 6),
    _LserDriveVendor_Type()
)
lserDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveVendor.setStatus("mandatory")


class _LserDriveSerialNum_Type(OctetString):
    """Custom type lserDriveSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserDriveSerialNum_Type.__name__ = "OctetString"
_LserDriveSerialNum_Object = MibTableColumn
lserDriveSerialNum = _LserDriveSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 7),
    _LserDriveSerialNum_Type()
)
lserDriveSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveSerialNum.setStatus("mandatory")


class _LserDriveInterfaceType_Type(Integer32):
    """Custom type lserDriveInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fibre", 3),
          ("scsi", 2),
          ("unknown", 1))
    )


_LserDriveInterfaceType_Type.__name__ = "Integer32"
_LserDriveInterfaceType_Object = MibTableColumn
lserDriveInterfaceType = _LserDriveInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 8),
    _LserDriveInterfaceType_Type()
)
lserDriveInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveInterfaceType.setStatus("mandatory")
_LserDriveID_Type = Integer32
_LserDriveID_Object = MibTableColumn
lserDriveID = _LserDriveID_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 9),
    _LserDriveID_Type()
)
lserDriveID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserDriveID.setStatus("mandatory")


class _LserDriveState_Type(OctetString):
    """Custom type lserDriveState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserDriveState_Type.__name__ = "OctetString"
_LserDriveState_Object = MibTableColumn
lserDriveState = _LserDriveState_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 10),
    _LserDriveState_Type()
)
lserDriveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveState.setStatus("mandatory")
_LserDriveStatusEnum_Type = LserDeviceStatus
_LserDriveStatusEnum_Object = MibTableColumn
lserDriveStatusEnum = _LserDriveStatusEnum_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 11),
    _LserDriveStatusEnum_Type()
)
lserDriveStatusEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveStatusEnum.setStatus("mandatory")


class _LserDriveCodeVer_Type(OctetString):
    """Custom type lserDriveCodeVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserDriveCodeVer_Type.__name__ = "OctetString"
_LserDriveCodeVer_Object = MibTableColumn
lserDriveCodeVer = _LserDriveCodeVer_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 12),
    _LserDriveCodeVer_Type()
)
lserDriveCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveCodeVer.setStatus("mandatory")


class _LserDriveVersion_Type(OctetString):
    """Custom type lserDriveVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserDriveVersion_Type.__name__ = "OctetString"
_LserDriveVersion_Object = MibTableColumn
lserDriveVersion = _LserDriveVersion_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 13),
    _LserDriveVersion_Type()
)
lserDriveVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveVersion.setStatus("mandatory")


class _LserDriveFirmwareVer_Type(OctetString):
    """Custom type lserDriveFirmwareVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserDriveFirmwareVer_Type.__name__ = "OctetString"
_LserDriveFirmwareVer_Object = MibTableColumn
lserDriveFirmwareVer = _LserDriveFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 14),
    _LserDriveFirmwareVer_Type()
)
lserDriveFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveFirmwareVer.setStatus("mandatory")
_LserDriveGetRetries_Type = Integer32
_LserDriveGetRetries_Object = MibTableColumn
lserDriveGetRetries = _LserDriveGetRetries_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 15),
    _LserDriveGetRetries_Type()
)
lserDriveGetRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveGetRetries.setStatus("mandatory")
_LserDrivePutRetries_Type = Integer32
_LserDrivePutRetries_Object = MibTableColumn
lserDrivePutRetries = _LserDrivePutRetries_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 16),
    _LserDrivePutRetries_Type()
)
lserDrivePutRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDrivePutRetries.setStatus("mandatory")


class _LserDriveCommandClean_Type(Integer32):
    """Custom type lserDriveCommandClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("enable", 1))
    )


_LserDriveCommandClean_Type.__name__ = "Integer32"
_LserDriveCommandClean_Object = MibTableColumn
lserDriveCommandClean = _LserDriveCommandClean_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 17),
    _LserDriveCommandClean_Type()
)
lserDriveCommandClean.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserDriveCommandClean.setStatus("mandatory")


class _LserDriveCellStatusEnum_Type(Integer32):
    """Custom type lserDriveCellStatusEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("empty", 2),
          ("full", 3),
          ("unknown", 1))
    )


_LserDriveCellStatusEnum_Type.__name__ = "Integer32"
_LserDriveCellStatusEnum_Object = MibTableColumn
lserDriveCellStatusEnum = _LserDriveCellStatusEnum_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 18),
    _LserDriveCellStatusEnum_Type()
)
lserDriveCellStatusEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveCellStatusEnum.setStatus("mandatory")


class _LserDriveCellStatusText_Type(OctetString):
    """Custom type lserDriveCellStatusText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserDriveCellStatusText_Type.__name__ = "OctetString"
_LserDriveCellStatusText_Object = MibTableColumn
lserDriveCellStatusText = _LserDriveCellStatusText_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 19),
    _LserDriveCellStatusText_Type()
)
lserDriveCellStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveCellStatusText.setStatus("mandatory")


class _LserDriveCellContentLabel_Type(OctetString):
    """Custom type lserDriveCellContentLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserDriveCellContentLabel_Type.__name__ = "OctetString"
_LserDriveCellContentLabel_Object = MibTableColumn
lserDriveCellContentLabel = _LserDriveCellContentLabel_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 20),
    _LserDriveCellContentLabel_Type()
)
lserDriveCellContentLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveCellContentLabel.setStatus("mandatory")


class _LserDriveCellContentType_Type(OctetString):
    """Custom type lserDriveCellContentType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserDriveCellContentType_Type.__name__ = "OctetString"
_LserDriveCellContentType_Object = MibTableColumn
lserDriveCellContentType = _LserDriveCellContentType_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 21),
    _LserDriveCellContentType_Type()
)
lserDriveCellContentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveCellContentType.setStatus("mandatory")
_LserDriveIdleSeconds_Type = Integer32
_LserDriveIdleSeconds_Object = MibTableColumn
lserDriveIdleSeconds = _LserDriveIdleSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 24),
    _LserDriveIdleSeconds_Type()
)
lserDriveIdleSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveIdleSeconds.setStatus("mandatory")
_LserDriveNumMounts_Type = Integer32
_LserDriveNumMounts_Object = MibTableColumn
lserDriveNumMounts = _LserDriveNumMounts_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 25),
    _LserDriveNumMounts_Type()
)
lserDriveNumMounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveNumMounts.setStatus("mandatory")
_LserDriveUsageSampleCount_Type = Integer32
_LserDriveUsageSampleCount_Object = MibTableColumn
lserDriveUsageSampleCount = _LserDriveUsageSampleCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 26),
    _LserDriveUsageSampleCount_Type()
)
lserDriveUsageSampleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveUsageSampleCount.setStatus("mandatory")
_LserDriveUsageMinimum_Type = Integer32
_LserDriveUsageMinimum_Object = MibTableColumn
lserDriveUsageMinimum = _LserDriveUsageMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 27),
    _LserDriveUsageMinimum_Type()
)
lserDriveUsageMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveUsageMinimum.setStatus("mandatory")
_LserDriveUsage5min_Type = Integer32
_LserDriveUsage5min_Object = MibTableColumn
lserDriveUsage5min = _LserDriveUsage5min_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 28),
    _LserDriveUsage5min_Type()
)
lserDriveUsage5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveUsage5min.setStatus("mandatory")
_LserDriveUsage5to10_Type = Integer32
_LserDriveUsage5to10_Object = MibTableColumn
lserDriveUsage5to10 = _LserDriveUsage5to10_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 29),
    _LserDriveUsage5to10_Type()
)
lserDriveUsage5to10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveUsage5to10.setStatus("mandatory")
_LserDriveUsage10to30_Type = Integer32
_LserDriveUsage10to30_Object = MibTableColumn
lserDriveUsage10to30 = _LserDriveUsage10to30_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 30),
    _LserDriveUsage10to30_Type()
)
lserDriveUsage10to30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveUsage10to30.setStatus("mandatory")
_LserDriveUsage30to60_Type = Integer32
_LserDriveUsage30to60_Object = MibTableColumn
lserDriveUsage30to60 = _LserDriveUsage30to60_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 31),
    _LserDriveUsage30to60_Type()
)
lserDriveUsage30to60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveUsage30to60.setStatus("mandatory")
_LserDriveUsageMaximum_Type = Integer32
_LserDriveUsageMaximum_Object = MibTableColumn
lserDriveUsageMaximum = _LserDriveUsageMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 2, 1, 32),
    _LserDriveUsageMaximum_Type()
)
lserDriveUsageMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveUsageMaximum.setStatus("mandatory")
_LserDriveFibreCount_Type = Integer32
_LserDriveFibreCount_Object = MibScalar
lserDriveFibreCount = _LserDriveFibreCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 3),
    _LserDriveFibreCount_Type()
)
lserDriveFibreCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveFibreCount.setStatus("mandatory")
_LserDriveFibreTable_Object = MibTable
lserDriveFibreTable = _LserDriveFibreTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 4)
)
if mibBuilder.loadTexts:
    lserDriveFibreTable.setStatus("mandatory")
_LserDriveFibreEntry_Object = MibTableRow
lserDriveFibreEntry = _LserDriveFibreEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 4, 1)
)
lserDriveFibreEntry.setIndexNames(
    (0, "LSERIES-TAPE-LIBRARY-MIB", "lserDriveFibreIndex"),
)
if mibBuilder.loadTexts:
    lserDriveFibreEntry.setStatus("mandatory")
_LserDriveFibreIndex_Type = Integer32
_LserDriveFibreIndex_Object = MibTableColumn
lserDriveFibreIndex = _LserDriveFibreIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 4, 1, 1),
    _LserDriveFibreIndex_Type()
)
lserDriveFibreIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveFibreIndex.setStatus("mandatory")


class _LserDriveFibreSerialNum_Type(OctetString):
    """Custom type lserDriveFibreSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserDriveFibreSerialNum_Type.__name__ = "OctetString"
_LserDriveFibreSerialNum_Object = MibTableColumn
lserDriveFibreSerialNum = _LserDriveFibreSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 4, 1, 2),
    _LserDriveFibreSerialNum_Type()
)
lserDriveFibreSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveFibreSerialNum.setStatus("mandatory")


class _LserDriveFibreNodeName_Type(OctetString):
    """Custom type lserDriveFibreNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserDriveFibreNodeName_Type.__name__ = "OctetString"
_LserDriveFibreNodeName_Object = MibTableColumn
lserDriveFibreNodeName = _LserDriveFibreNodeName_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 4, 1, 3),
    _LserDriveFibreNodeName_Type()
)
lserDriveFibreNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveFibreNodeName.setStatus("mandatory")


class _LserDriveFibrePortCount_Type(Integer32):
    """Custom type lserDriveFibrePortCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dual", 2),
          ("single", 1))
    )


_LserDriveFibrePortCount_Type.__name__ = "Integer32"
_LserDriveFibrePortCount_Object = MibTableColumn
lserDriveFibrePortCount = _LserDriveFibrePortCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 4, 1, 4),
    _LserDriveFibrePortCount_Type()
)
lserDriveFibrePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveFibrePortCount.setStatus("mandatory")


class _LserDriveFibrePortAWWN_Type(OctetString):
    """Custom type lserDriveFibrePortAWWN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserDriveFibrePortAWWN_Type.__name__ = "OctetString"
_LserDriveFibrePortAWWN_Object = MibTableColumn
lserDriveFibrePortAWWN = _LserDriveFibrePortAWWN_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 4, 1, 5),
    _LserDriveFibrePortAWWN_Type()
)
lserDriveFibrePortAWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveFibrePortAWWN.setStatus("mandatory")
_LserDriveFibrePortAAddressingMode_Type = LserDriveFibreAddressing
_LserDriveFibrePortAAddressingMode_Object = MibTableColumn
lserDriveFibrePortAAddressingMode = _LserDriveFibrePortAAddressingMode_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 4, 1, 6),
    _LserDriveFibrePortAAddressingMode_Type()
)
lserDriveFibrePortAAddressingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveFibrePortAAddressingMode.setStatus("mandatory")


class _LserDriveFibrePortAPortEnabled_Type(Integer32):
    """Custom type lserDriveFibrePortAPortEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LserDriveFibrePortAPortEnabled_Type.__name__ = "Integer32"
_LserDriveFibrePortAPortEnabled_Object = MibTableColumn
lserDriveFibrePortAPortEnabled = _LserDriveFibrePortAPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 4, 1, 7),
    _LserDriveFibrePortAPortEnabled_Type()
)
lserDriveFibrePortAPortEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveFibrePortAPortEnabled.setStatus("mandatory")
_LserDriveFibrePortALoopId_Type = LserDriveFibreLoopId
_LserDriveFibrePortALoopId_Object = MibTableColumn
lserDriveFibrePortALoopId = _LserDriveFibrePortALoopId_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 4, 1, 8),
    _LserDriveFibrePortALoopId_Type()
)
lserDriveFibrePortALoopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveFibrePortALoopId.setStatus("mandatory")
_LserDriveFibrePortAPortSpeed_Type = LserDriveFibreSpeed
_LserDriveFibrePortAPortSpeed_Object = MibTableColumn
lserDriveFibrePortAPortSpeed = _LserDriveFibrePortAPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 4, 1, 9),
    _LserDriveFibrePortAPortSpeed_Type()
)
lserDriveFibrePortAPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveFibrePortAPortSpeed.setStatus("mandatory")


class _LserDriveFibrePortBWWN_Type(OctetString):
    """Custom type lserDriveFibrePortBWWN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserDriveFibrePortBWWN_Type.__name__ = "OctetString"
_LserDriveFibrePortBWWN_Object = MibTableColumn
lserDriveFibrePortBWWN = _LserDriveFibrePortBWWN_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 4, 1, 10),
    _LserDriveFibrePortBWWN_Type()
)
lserDriveFibrePortBWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveFibrePortBWWN.setStatus("mandatory")
_LserDriveFibrePortBAddressingMode_Type = LserDriveFibreAddressing
_LserDriveFibrePortBAddressingMode_Object = MibTableColumn
lserDriveFibrePortBAddressingMode = _LserDriveFibrePortBAddressingMode_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 4, 1, 11),
    _LserDriveFibrePortBAddressingMode_Type()
)
lserDriveFibrePortBAddressingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveFibrePortBAddressingMode.setStatus("mandatory")


class _LserDriveFibrePortBPortEnabled_Type(Integer32):
    """Custom type lserDriveFibrePortBPortEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LserDriveFibrePortBPortEnabled_Type.__name__ = "Integer32"
_LserDriveFibrePortBPortEnabled_Object = MibTableColumn
lserDriveFibrePortBPortEnabled = _LserDriveFibrePortBPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 4, 1, 12),
    _LserDriveFibrePortBPortEnabled_Type()
)
lserDriveFibrePortBPortEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveFibrePortBPortEnabled.setStatus("mandatory")
_LserDriveFibrePortBLoopId_Type = LserDriveFibreLoopId
_LserDriveFibrePortBLoopId_Object = MibTableColumn
lserDriveFibrePortBLoopId = _LserDriveFibrePortBLoopId_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 4, 1, 13),
    _LserDriveFibrePortBLoopId_Type()
)
lserDriveFibrePortBLoopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveFibrePortBLoopId.setStatus("mandatory")
_LserDriveFibrePortBPortSpeed_Type = LserDriveFibreSpeed
_LserDriveFibrePortBPortSpeed_Object = MibTableColumn
lserDriveFibrePortBPortSpeed = _LserDriveFibrePortBPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 4, 1, 14),
    _LserDriveFibrePortBPortSpeed_Type()
)
lserDriveFibrePortBPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveFibrePortBPortSpeed.setStatus("mandatory")


class _LserDriveWWNEnabled_Type(Integer32):
    """Custom type lserDriveWWNEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LserDriveWWNEnabled_Type.__name__ = "Integer32"
_LserDriveWWNEnabled_Object = MibScalar
lserDriveWWNEnabled = _LserDriveWWNEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 4, 5),
    _LserDriveWWNEnabled_Type()
)
lserDriveWWNEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserDriveWWNEnabled.setStatus("mandatory")
_LserCaps_ObjectIdentity = ObjectIdentity
lserCaps = _LserCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5)
)
_LserCapCount_Type = Integer32
_LserCapCount_Object = MibScalar
lserCapCount = _LserCapCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 1),
    _LserCapCount_Type()
)
lserCapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapCount.setStatus("mandatory")
_LserCapTable_Object = MibTable
lserCapTable = _LserCapTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2)
)
if mibBuilder.loadTexts:
    lserCapTable.setStatus("mandatory")
_LserCapEntry_Object = MibTableRow
lserCapEntry = _LserCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1)
)
lserCapEntry.setIndexNames(
    (0, "LSERIES-TAPE-LIBRARY-MIB", "lserCapIndex"),
)
if mibBuilder.loadTexts:
    lserCapEntry.setStatus("mandatory")
_LserCapIndex_Type = Integer32
_LserCapIndex_Object = MibTableColumn
lserCapIndex = _LserCapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 1),
    _LserCapIndex_Type()
)
lserCapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapIndex.setStatus("mandatory")


class _LserCapAccessibility_Type(OctetString):
    """Custom type lserCapAccessibility based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserCapAccessibility_Type.__name__ = "OctetString"
_LserCapAccessibility_Object = MibTableColumn
lserCapAccessibility = _LserCapAccessibility_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 2),
    _LserCapAccessibility_Type()
)
lserCapAccessibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapAccessibility.setStatus("mandatory")


class _LserCapAccessStateEnum_Type(Integer32):
    """Custom type lserCapAccessStateEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("close", 3),
          ("open", 2),
          ("unknown", 1))
    )


_LserCapAccessStateEnum_Type.__name__ = "Integer32"
_LserCapAccessStateEnum_Object = MibTableColumn
lserCapAccessStateEnum = _LserCapAccessStateEnum_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 3),
    _LserCapAccessStateEnum_Type()
)
lserCapAccessStateEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapAccessStateEnum.setStatus("mandatory")


class _LserCapState_Type(OctetString):
    """Custom type lserCapState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserCapState_Type.__name__ = "OctetString"
_LserCapState_Object = MibTableColumn
lserCapState = _LserCapState_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 4),
    _LserCapState_Type()
)
lserCapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapState.setStatus("mandatory")
_LserCapStatusEnum_Type = LserDeviceStatus
_LserCapStatusEnum_Object = MibTableColumn
lserCapStatusEnum = _LserCapStatusEnum_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 5),
    _LserCapStatusEnum_Type()
)
lserCapStatusEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapStatusEnum.setStatus("mandatory")
_LserCapUsageGetSampleCount_Type = Integer32
_LserCapUsageGetSampleCount_Object = MibTableColumn
lserCapUsageGetSampleCount = _LserCapUsageGetSampleCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 8),
    _LserCapUsageGetSampleCount_Type()
)
lserCapUsageGetSampleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsageGetSampleCount.setStatus("mandatory")
_LserCapUsageGetIdle_Type = Integer32
_LserCapUsageGetIdle_Object = MibTableColumn
lserCapUsageGetIdle = _LserCapUsageGetIdle_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 9),
    _LserCapUsageGetIdle_Type()
)
lserCapUsageGetIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsageGetIdle.setStatus("mandatory")
_LserCapUsageGet1_Type = Integer32
_LserCapUsageGet1_Object = MibTableColumn
lserCapUsageGet1 = _LserCapUsageGet1_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 10),
    _LserCapUsageGet1_Type()
)
lserCapUsageGet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsageGet1.setStatus("mandatory")
_LserCapUsageGet2_Type = Integer32
_LserCapUsageGet2_Object = MibTableColumn
lserCapUsageGet2 = _LserCapUsageGet2_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 11),
    _LserCapUsageGet2_Type()
)
lserCapUsageGet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsageGet2.setStatus("mandatory")
_LserCapUsageGet3_Type = Integer32
_LserCapUsageGet3_Object = MibTableColumn
lserCapUsageGet3 = _LserCapUsageGet3_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 12),
    _LserCapUsageGet3_Type()
)
lserCapUsageGet3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsageGet3.setStatus("mandatory")
_LserCapUsageGet4_Type = Integer32
_LserCapUsageGet4_Object = MibTableColumn
lserCapUsageGet4 = _LserCapUsageGet4_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 13),
    _LserCapUsageGet4_Type()
)
lserCapUsageGet4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsageGet4.setStatus("mandatory")
_LserCapUsageGet5_Type = Integer32
_LserCapUsageGet5_Object = MibTableColumn
lserCapUsageGet5 = _LserCapUsageGet5_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 14),
    _LserCapUsageGet5_Type()
)
lserCapUsageGet5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsageGet5.setStatus("mandatory")
_LserCapUsageGet6to10_Type = Integer32
_LserCapUsageGet6to10_Object = MibTableColumn
lserCapUsageGet6to10 = _LserCapUsageGet6to10_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 15),
    _LserCapUsageGet6to10_Type()
)
lserCapUsageGet6to10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsageGet6to10.setStatus("mandatory")
_LserCapUsageGet11to15_Type = Integer32
_LserCapUsageGet11to15_Object = MibTableColumn
lserCapUsageGet11to15 = _LserCapUsageGet11to15_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 16),
    _LserCapUsageGet11to15_Type()
)
lserCapUsageGet11to15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsageGet11to15.setStatus("mandatory")
_LserCapUsageGet16to20_Type = Integer32
_LserCapUsageGet16to20_Object = MibTableColumn
lserCapUsageGet16to20 = _LserCapUsageGet16to20_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 17),
    _LserCapUsageGet16to20_Type()
)
lserCapUsageGet16to20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsageGet16to20.setStatus("mandatory")
_LserCapUsageGet21toMax_Type = Integer32
_LserCapUsageGet21toMax_Object = MibTableColumn
lserCapUsageGet21toMax = _LserCapUsageGet21toMax_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 18),
    _LserCapUsageGet21toMax_Type()
)
lserCapUsageGet21toMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsageGet21toMax.setStatus("mandatory")
_LserCapUsagePutSampleCount_Type = Integer32
_LserCapUsagePutSampleCount_Object = MibTableColumn
lserCapUsagePutSampleCount = _LserCapUsagePutSampleCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 19),
    _LserCapUsagePutSampleCount_Type()
)
lserCapUsagePutSampleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsagePutSampleCount.setStatus("mandatory")
_LserCapUsagePutIdle_Type = Integer32
_LserCapUsagePutIdle_Object = MibTableColumn
lserCapUsagePutIdle = _LserCapUsagePutIdle_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 20),
    _LserCapUsagePutIdle_Type()
)
lserCapUsagePutIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsagePutIdle.setStatus("mandatory")
_LserCapUsagePut1_Type = Integer32
_LserCapUsagePut1_Object = MibTableColumn
lserCapUsagePut1 = _LserCapUsagePut1_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 21),
    _LserCapUsagePut1_Type()
)
lserCapUsagePut1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsagePut1.setStatus("mandatory")
_LserCapUsagePut2_Type = Integer32
_LserCapUsagePut2_Object = MibTableColumn
lserCapUsagePut2 = _LserCapUsagePut2_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 22),
    _LserCapUsagePut2_Type()
)
lserCapUsagePut2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsagePut2.setStatus("mandatory")
_LserCapUsagePut3_Type = Integer32
_LserCapUsagePut3_Object = MibTableColumn
lserCapUsagePut3 = _LserCapUsagePut3_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 23),
    _LserCapUsagePut3_Type()
)
lserCapUsagePut3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsagePut3.setStatus("mandatory")
_LserCapUsagePut4_Type = Integer32
_LserCapUsagePut4_Object = MibTableColumn
lserCapUsagePut4 = _LserCapUsagePut4_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 24),
    _LserCapUsagePut4_Type()
)
lserCapUsagePut4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsagePut4.setStatus("mandatory")
_LserCapUsagePut5_Type = Integer32
_LserCapUsagePut5_Object = MibTableColumn
lserCapUsagePut5 = _LserCapUsagePut5_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 25),
    _LserCapUsagePut5_Type()
)
lserCapUsagePut5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsagePut5.setStatus("mandatory")
_LserCapUsagePut6to10_Type = Integer32
_LserCapUsagePut6to10_Object = MibTableColumn
lserCapUsagePut6to10 = _LserCapUsagePut6to10_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 26),
    _LserCapUsagePut6to10_Type()
)
lserCapUsagePut6to10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsagePut6to10.setStatus("mandatory")
_LserCapUsagePut11to15_Type = Integer32
_LserCapUsagePut11to15_Object = MibTableColumn
lserCapUsagePut11to15 = _LserCapUsagePut11to15_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 27),
    _LserCapUsagePut11to15_Type()
)
lserCapUsagePut11to15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsagePut11to15.setStatus("mandatory")
_LserCapUsagePut16to20_Type = Integer32
_LserCapUsagePut16to20_Object = MibTableColumn
lserCapUsagePut16to20 = _LserCapUsagePut16to20_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 28),
    _LserCapUsagePut16to20_Type()
)
lserCapUsagePut16to20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsagePut16to20.setStatus("mandatory")
_LserCapUsagePut21toMax_Type = Integer32
_LserCapUsagePut21toMax_Object = MibTableColumn
lserCapUsagePut21toMax = _LserCapUsagePut21toMax_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 29),
    _LserCapUsagePut21toMax_Type()
)
lserCapUsagePut21toMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapUsagePut21toMax.setStatus("mandatory")


class _LserCapName_Type(OctetString):
    """Custom type lserCapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserCapName_Type.__name__ = "OctetString"
_LserCapName_Object = MibTableColumn
lserCapName = _LserCapName_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 5, 2, 1, 30),
    _LserCapName_Type()
)
lserCapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCapName.setStatus("mandatory")
_LserPassThru_ObjectIdentity = ObjectIdentity
lserPassThru = _LserPassThru_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6)
)
_LserPtpCount_Type = Integer32
_LserPtpCount_Object = MibScalar
lserPtpCount = _LserPtpCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 1),
    _LserPtpCount_Type()
)
lserPtpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpCount.setStatus("mandatory")
_LserPtpTable_Object = MibTable
lserPtpTable = _LserPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2)
)
if mibBuilder.loadTexts:
    lserPtpTable.setStatus("mandatory")
_LserPtpEntry_Object = MibTableRow
lserPtpEntry = _LserPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1)
)
lserPtpEntry.setIndexNames(
    (0, "LSERIES-TAPE-LIBRARY-MIB", "lserPtpIndex"),
)
if mibBuilder.loadTexts:
    lserPtpEntry.setStatus("mandatory")
_LserPtpIndex_Type = Integer32
_LserPtpIndex_Object = MibTableColumn
lserPtpIndex = _LserPtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 1),
    _LserPtpIndex_Type()
)
lserPtpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpIndex.setStatus("mandatory")


class _LserPtpState_Type(OctetString):
    """Custom type lserPtpState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserPtpState_Type.__name__ = "OctetString"
_LserPtpState_Object = MibTableColumn
lserPtpState = _LserPtpState_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 2),
    _LserPtpState_Type()
)
lserPtpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpState.setStatus("mandatory")
_LserPtpStatusEnum_Type = LserDeviceStatus
_LserPtpStatusEnum_Object = MibTableColumn
lserPtpStatusEnum = _LserPtpStatusEnum_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 3),
    _LserPtpStatusEnum_Type()
)
lserPtpStatusEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpStatusEnum.setStatus("mandatory")


class _LserPtpSerialNumber_Type(OctetString):
    """Custom type lserPtpSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserPtpSerialNumber_Type.__name__ = "OctetString"
_LserPtpSerialNumber_Object = MibTableColumn
lserPtpSerialNumber = _LserPtpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 4),
    _LserPtpSerialNumber_Type()
)
lserPtpSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpSerialNumber.setStatus("mandatory")


class _LserPtpPartNumber_Type(OctetString):
    """Custom type lserPtpPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserPtpPartNumber_Type.__name__ = "OctetString"
_LserPtpPartNumber_Object = MibTableColumn
lserPtpPartNumber = _LserPtpPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 5),
    _LserPtpPartNumber_Type()
)
lserPtpPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpPartNumber.setStatus("mandatory")


class _LserPtpFirmwareVersion_Type(OctetString):
    """Custom type lserPtpFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserPtpFirmwareVersion_Type.__name__ = "OctetString"
_LserPtpFirmwareVersion_Object = MibTableColumn
lserPtpFirmwareVersion = _LserPtpFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 6),
    _LserPtpFirmwareVersion_Type()
)
lserPtpFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpFirmwareVersion.setStatus("mandatory")


class _LserPtpFirmwareDate_Type(OctetString):
    """Custom type lserPtpFirmwareDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserPtpFirmwareDate_Type.__name__ = "OctetString"
_LserPtpFirmwareDate_Object = MibTableColumn
lserPtpFirmwareDate = _LserPtpFirmwareDate_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 7),
    _LserPtpFirmwareDate_Type()
)
lserPtpFirmwareDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpFirmwareDate.setStatus("mandatory")
_LserPtpSoftwareResetCount_Type = Counter32
_LserPtpSoftwareResetCount_Object = MibTableColumn
lserPtpSoftwareResetCount = _LserPtpSoftwareResetCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 8),
    _LserPtpSoftwareResetCount_Type()
)
lserPtpSoftwareResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpSoftwareResetCount.setStatus("mandatory")
_LserPtpDoorOpenCount_Type = Counter32
_LserPtpDoorOpenCount_Object = MibTableColumn
lserPtpDoorOpenCount = _LserPtpDoorOpenCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 9),
    _LserPtpDoorOpenCount_Type()
)
lserPtpDoorOpenCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpDoorOpenCount.setStatus("mandatory")
_LserPtpInitializationCount_Type = Counter32
_LserPtpInitializationCount_Object = MibTableColumn
lserPtpInitializationCount = _LserPtpInitializationCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 10),
    _LserPtpInitializationCount_Type()
)
lserPtpInitializationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpInitializationCount.setStatus("mandatory")
_LserPtpInoperativeCount_Type = Counter32
_LserPtpInoperativeCount_Object = MibTableColumn
lserPtpInoperativeCount = _LserPtpInoperativeCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 11),
    _LserPtpInoperativeCount_Type()
)
lserPtpInoperativeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpInoperativeCount.setStatus("mandatory")
_LserPtpGoodCommandCount_Type = Counter32
_LserPtpGoodCommandCount_Object = MibTableColumn
lserPtpGoodCommandCount = _LserPtpGoodCommandCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 12),
    _LserPtpGoodCommandCount_Type()
)
lserPtpGoodCommandCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpGoodCommandCount.setStatus("mandatory")
_LserPtpFailCommandCount_Type = Counter32
_LserPtpFailCommandCount_Object = MibTableColumn
lserPtpFailCommandCount = _LserPtpFailCommandCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 13),
    _LserPtpFailCommandCount_Type()
)
lserPtpFailCommandCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpFailCommandCount.setStatus("mandatory")
_LserPtpGoodEmptyMotionCount_Type = Counter32
_LserPtpGoodEmptyMotionCount_Object = MibTableColumn
lserPtpGoodEmptyMotionCount = _LserPtpGoodEmptyMotionCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 14),
    _LserPtpGoodEmptyMotionCount_Type()
)
lserPtpGoodEmptyMotionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpGoodEmptyMotionCount.setStatus("mandatory")
_LserPtpFailEmptyMotionCount_Type = Counter32
_LserPtpFailEmptyMotionCount_Object = MibTableColumn
lserPtpFailEmptyMotionCount = _LserPtpFailEmptyMotionCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 15),
    _LserPtpFailEmptyMotionCount_Type()
)
lserPtpFailEmptyMotionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpFailEmptyMotionCount.setStatus("mandatory")
_LserPtpGoodPartMotionCount_Type = Counter32
_LserPtpGoodPartMotionCount_Object = MibTableColumn
lserPtpGoodPartMotionCount = _LserPtpGoodPartMotionCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 16),
    _LserPtpGoodPartMotionCount_Type()
)
lserPtpGoodPartMotionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpGoodPartMotionCount.setStatus("mandatory")
_LserPtpFailPartMotionCount_Type = Counter32
_LserPtpFailPartMotionCount_Object = MibTableColumn
lserPtpFailPartMotionCount = _LserPtpFailPartMotionCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 17),
    _LserPtpFailPartMotionCount_Type()
)
lserPtpFailPartMotionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpFailPartMotionCount.setStatus("mandatory")
_LserPtpGoodFullMotionCount_Type = Counter32
_LserPtpGoodFullMotionCount_Object = MibTableColumn
lserPtpGoodFullMotionCount = _LserPtpGoodFullMotionCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 18),
    _LserPtpGoodFullMotionCount_Type()
)
lserPtpGoodFullMotionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpGoodFullMotionCount.setStatus("mandatory")
_LserPtpFailFullMotionCount_Type = Counter32
_LserPtpFailFullMotionCount_Object = MibTableColumn
lserPtpFailFullMotionCount = _LserPtpFailFullMotionCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 19),
    _LserPtpFailFullMotionCount_Type()
)
lserPtpFailFullMotionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpFailFullMotionCount.setStatus("mandatory")


class _LserPtpCompLibNetworkIpAddr_Type(OctetString):
    """Custom type lserPtpCompLibNetworkIpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LserPtpCompLibNetworkIpAddr_Type.__name__ = "OctetString"
_LserPtpCompLibNetworkIpAddr_Object = MibTableColumn
lserPtpCompLibNetworkIpAddr = _LserPtpCompLibNetworkIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 20),
    _LserPtpCompLibNetworkIpAddr_Type()
)
lserPtpCompLibNetworkIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserPtpCompLibNetworkIpAddr.setStatus("mandatory")


class _LserPtpCompLibNetworkName_Type(OctetString):
    """Custom type lserPtpCompLibNetworkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LserPtpCompLibNetworkName_Type.__name__ = "OctetString"
_LserPtpCompLibNetworkName_Object = MibTableColumn
lserPtpCompLibNetworkName = _LserPtpCompLibNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 21),
    _LserPtpCompLibNetworkName_Type()
)
lserPtpCompLibNetworkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserPtpCompLibNetworkName.setStatus("mandatory")


class _LserPtpCompLibSerialNumber_Type(OctetString):
    """Custom type lserPtpCompLibSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserPtpCompLibSerialNumber_Type.__name__ = "OctetString"
_LserPtpCompLibSerialNumber_Object = MibTableColumn
lserPtpCompLibSerialNumber = _LserPtpCompLibSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 22),
    _LserPtpCompLibSerialNumber_Type()
)
lserPtpCompLibSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpCompLibSerialNumber.setStatus("mandatory")


class _LserPtpCompLibPartNumber_Type(OctetString):
    """Custom type lserPtpCompLibPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserPtpCompLibPartNumber_Type.__name__ = "OctetString"
_LserPtpCompLibPartNumber_Object = MibTableColumn
lserPtpCompLibPartNumber = _LserPtpCompLibPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 23),
    _LserPtpCompLibPartNumber_Type()
)
lserPtpCompLibPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpCompLibPartNumber.setStatus("mandatory")


class _LserPtpCompLibVendorName_Type(OctetString):
    """Custom type lserPtpCompLibVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserPtpCompLibVendorName_Type.__name__ = "OctetString"
_LserPtpCompLibVendorName_Object = MibTableColumn
lserPtpCompLibVendorName = _LserPtpCompLibVendorName_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 24),
    _LserPtpCompLibVendorName_Type()
)
lserPtpCompLibVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpCompLibVendorName.setStatus("mandatory")


class _LserPtpCompLibModelName_Type(OctetString):
    """Custom type lserPtpCompLibModelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserPtpCompLibModelName_Type.__name__ = "OctetString"
_LserPtpCompLibModelName_Object = MibTableColumn
lserPtpCompLibModelName = _LserPtpCompLibModelName_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 25),
    _LserPtpCompLibModelName_Type()
)
lserPtpCompLibModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpCompLibModelName.setStatus("mandatory")


class _LserPtpCompLibFirmwareVersion_Type(OctetString):
    """Custom type lserPtpCompLibFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserPtpCompLibFirmwareVersion_Type.__name__ = "OctetString"
_LserPtpCompLibFirmwareVersion_Object = MibTableColumn
lserPtpCompLibFirmwareVersion = _LserPtpCompLibFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 26),
    _LserPtpCompLibFirmwareVersion_Type()
)
lserPtpCompLibFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpCompLibFirmwareVersion.setStatus("mandatory")


class _LserPtpCompLibFirmwareDate_Type(OctetString):
    """Custom type lserPtpCompLibFirmwareDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserPtpCompLibFirmwareDate_Type.__name__ = "OctetString"
_LserPtpCompLibFirmwareDate_Object = MibTableColumn
lserPtpCompLibFirmwareDate = _LserPtpCompLibFirmwareDate_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 6, 2, 1, 27),
    _LserPtpCompLibFirmwareDate_Type()
)
lserPtpCompLibFirmwareDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPtpCompLibFirmwareDate.setStatus("mandatory")
_LserInventory_ObjectIdentity = ObjectIdentity
lserInventory = _LserInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 7)
)
_LserTapeCount_Type = Integer32
_LserTapeCount_Object = MibScalar
lserTapeCount = _LserTapeCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 7, 1),
    _LserTapeCount_Type()
)
lserTapeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserTapeCount.setStatus("mandatory")
_LserTapeTable_Object = MibTable
lserTapeTable = _LserTapeTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 7, 2)
)
if mibBuilder.loadTexts:
    lserTapeTable.setStatus("mandatory")
_LserTapeEntry_Object = MibTableRow
lserTapeEntry = _LserTapeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 7, 2, 1)
)
lserTapeEntry.setIndexNames(
    (0, "LSERIES-TAPE-LIBRARY-MIB", "lserTapeIndex"),
)
if mibBuilder.loadTexts:
    lserTapeEntry.setStatus("mandatory")
_LserTapeIndex_Type = Integer32
_LserTapeIndex_Object = MibTableColumn
lserTapeIndex = _LserTapeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 7, 2, 1, 1),
    _LserTapeIndex_Type()
)
lserTapeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserTapeIndex.setStatus("mandatory")


class _LserTapeLabel_Type(OctetString):
    """Custom type lserTapeLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserTapeLabel_Type.__name__ = "OctetString"
_LserTapeLabel_Object = MibTableColumn
lserTapeLabel = _LserTapeLabel_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 7, 2, 1, 2),
    _LserTapeLabel_Type()
)
lserTapeLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserTapeLabel.setStatus("mandatory")


class _LserTapeType_Type(OctetString):
    """Custom type lserTapeType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserTapeType_Type.__name__ = "OctetString"
_LserTapeType_Object = MibTableColumn
lserTapeType = _LserTapeType_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 7, 2, 1, 3),
    _LserTapeType_Type()
)
lserTapeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserTapeType.setStatus("mandatory")
_LserTapeLocationElementID_Type = Integer32
_LserTapeLocationElementID_Object = MibTableColumn
lserTapeLocationElementID = _LserTapeLocationElementID_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 7, 2, 1, 4),
    _LserTapeLocationElementID_Type()
)
lserTapeLocationElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserTapeLocationElementID.setStatus("mandatory")


class _LserTapeHostAccessible_Type(Integer32):
    """Custom type lserTapeHostAccessible based on Integer32"""
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


_LserTapeHostAccessible_Type.__name__ = "Integer32"
_LserTapeHostAccessible_Object = MibTableColumn
lserTapeHostAccessible = _LserTapeHostAccessible_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 7, 2, 1, 5),
    _LserTapeHostAccessible_Type()
)
lserTapeHostAccessible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserTapeHostAccessible.setStatus("mandatory")
_LserStorage_ObjectIdentity = ObjectIdentity
lserStorage = _LserStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 8)
)
_LserCellCount_Type = Integer32
_LserCellCount_Object = MibScalar
lserCellCount = _LserCellCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 8, 1),
    _LserCellCount_Type()
)
lserCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCellCount.setStatus("mandatory")
_LserCellTable_Object = MibTable
lserCellTable = _LserCellTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 8, 2)
)
if mibBuilder.loadTexts:
    lserCellTable.setStatus("mandatory")
_LserCellEntry_Object = MibTableRow
lserCellEntry = _LserCellEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 8, 2, 1)
)
lserCellEntry.setIndexNames(
    (0, "LSERIES-TAPE-LIBRARY-MIB", "lserCellIndex"),
)
if mibBuilder.loadTexts:
    lserCellEntry.setStatus("mandatory")
_LserCellIndex_Type = Integer32
_LserCellIndex_Object = MibTableColumn
lserCellIndex = _LserCellIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 8, 2, 1, 1),
    _LserCellIndex_Type()
)
lserCellIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCellIndex.setStatus("mandatory")
_LserCellElementID_Type = Integer32
_LserCellElementID_Object = MibTableColumn
lserCellElementID = _LserCellElementID_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 8, 2, 1, 2),
    _LserCellElementID_Type()
)
lserCellElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCellElementID.setStatus("mandatory")


class _LserCellHostAccessible_Type(Integer32):
    """Custom type lserCellHostAccessible based on Integer32"""
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


_LserCellHostAccessible_Type.__name__ = "Integer32"
_LserCellHostAccessible_Object = MibTableColumn
lserCellHostAccessible = _LserCellHostAccessible_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 8, 2, 1, 3),
    _LserCellHostAccessible_Type()
)
lserCellHostAccessible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCellHostAccessible.setStatus("mandatory")


class _LserCellContentStatus_Type(OctetString):
    """Custom type lserCellContentStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserCellContentStatus_Type.__name__ = "OctetString"
_LserCellContentStatus_Object = MibTableColumn
lserCellContentStatus = _LserCellContentStatus_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 8, 2, 1, 4),
    _LserCellContentStatus_Type()
)
lserCellContentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCellContentStatus.setStatus("mandatory")


class _LserCellContentLabel_Type(OctetString):
    """Custom type lserCellContentLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserCellContentLabel_Type.__name__ = "OctetString"
_LserCellContentLabel_Object = MibTableColumn
lserCellContentLabel = _LserCellContentLabel_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 8, 2, 1, 5),
    _LserCellContentLabel_Type()
)
lserCellContentLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCellContentLabel.setStatus("mandatory")


class _LserCellContentType_Type(OctetString):
    """Custom type lserCellContentType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserCellContentType_Type.__name__ = "OctetString"
_LserCellContentType_Object = MibTableColumn
lserCellContentType = _LserCellContentType_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 8, 2, 1, 6),
    _LserCellContentType_Type()
)
lserCellContentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCellContentType.setStatus("mandatory")
_LserCellGetRetryCount_Type = Integer32
_LserCellGetRetryCount_Object = MibTableColumn
lserCellGetRetryCount = _LserCellGetRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 8, 2, 1, 7),
    _LserCellGetRetryCount_Type()
)
lserCellGetRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCellGetRetryCount.setStatus("mandatory")
_LserCellPutRetryCount_Type = Integer32
_LserCellPutRetryCount_Object = MibTableColumn
lserCellPutRetryCount = _LserCellPutRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 8, 2, 1, 8),
    _LserCellPutRetryCount_Type()
)
lserCellPutRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserCellPutRetryCount.setStatus("mandatory")
_LserStorageFreeCells_Type = Integer32
_LserStorageFreeCells_Object = MibScalar
lserStorageFreeCells = _LserStorageFreeCells_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 8, 3),
    _LserStorageFreeCells_Type()
)
lserStorageFreeCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserStorageFreeCells.setStatus("mandatory")
_LserPlayground_ObjectIdentity = ObjectIdentity
lserPlayground = _LserPlayground_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 9)
)
_LserPlayCellCount_Type = Integer32
_LserPlayCellCount_Object = MibScalar
lserPlayCellCount = _LserPlayCellCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 9, 1),
    _LserPlayCellCount_Type()
)
lserPlayCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPlayCellCount.setStatus("mandatory")
_LserPlayCellTable_Object = MibTable
lserPlayCellTable = _LserPlayCellTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 9, 2)
)
if mibBuilder.loadTexts:
    lserPlayCellTable.setStatus("mandatory")
_LserPlayCellEntry_Object = MibTableRow
lserPlayCellEntry = _LserPlayCellEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 9, 2, 1)
)
lserPlayCellEntry.setIndexNames(
    (0, "LSERIES-TAPE-LIBRARY-MIB", "lserPlayCellIndex"),
)
if mibBuilder.loadTexts:
    lserPlayCellEntry.setStatus("mandatory")
_LserPlayCellIndex_Type = Integer32
_LserPlayCellIndex_Object = MibTableColumn
lserPlayCellIndex = _LserPlayCellIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 9, 2, 1, 1),
    _LserPlayCellIndex_Type()
)
lserPlayCellIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPlayCellIndex.setStatus("mandatory")
_LserPlayCellElementID_Type = Integer32
_LserPlayCellElementID_Object = MibTableColumn
lserPlayCellElementID = _LserPlayCellElementID_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 9, 2, 1, 2),
    _LserPlayCellElementID_Type()
)
lserPlayCellElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPlayCellElementID.setStatus("mandatory")


class _LserPlayCellContentStatus_Type(OctetString):
    """Custom type lserPlayCellContentStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserPlayCellContentStatus_Type.__name__ = "OctetString"
_LserPlayCellContentStatus_Object = MibTableColumn
lserPlayCellContentStatus = _LserPlayCellContentStatus_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 9, 2, 1, 3),
    _LserPlayCellContentStatus_Type()
)
lserPlayCellContentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPlayCellContentStatus.setStatus("mandatory")


class _LserPlayCellContentLabel_Type(OctetString):
    """Custom type lserPlayCellContentLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserPlayCellContentLabel_Type.__name__ = "OctetString"
_LserPlayCellContentLabel_Object = MibTableColumn
lserPlayCellContentLabel = _LserPlayCellContentLabel_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 9, 2, 1, 4),
    _LserPlayCellContentLabel_Type()
)
lserPlayCellContentLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPlayCellContentLabel.setStatus("mandatory")


class _LserPlayCellContentType_Type(OctetString):
    """Custom type lserPlayCellContentType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserPlayCellContentType_Type.__name__ = "OctetString"
_LserPlayCellContentType_Object = MibTableColumn
lserPlayCellContentType = _LserPlayCellContentType_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 9, 2, 1, 5),
    _LserPlayCellContentType_Type()
)
lserPlayCellContentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserPlayCellContentType.setStatus("mandatory")
_LserHardwareMonitor_ObjectIdentity = ObjectIdentity
lserHardwareMonitor = _LserHardwareMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10)
)
_LserHdwNumTempSensors_Type = Integer32
_LserHdwNumTempSensors_Object = MibScalar
lserHdwNumTempSensors = _LserHdwNumTempSensors_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 1),
    _LserHdwNumTempSensors_Type()
)
lserHdwNumTempSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserHdwNumTempSensors.setStatus("mandatory")
_LserHdwTempSensorTable_Object = MibTable
lserHdwTempSensorTable = _LserHdwTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 2)
)
if mibBuilder.loadTexts:
    lserHdwTempSensorTable.setStatus("mandatory")
_LserHdwTempSensorEntry_Object = MibTableRow
lserHdwTempSensorEntry = _LserHdwTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 2, 1)
)
lserHdwTempSensorEntry.setIndexNames(
    (0, "LSERIES-TAPE-LIBRARY-MIB", "lserHdwTempSensorIndex"),
)
if mibBuilder.loadTexts:
    lserHdwTempSensorEntry.setStatus("mandatory")
_LserHdwTempSensorIndex_Type = Integer32
_LserHdwTempSensorIndex_Object = MibTableColumn
lserHdwTempSensorIndex = _LserHdwTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 2, 1, 1),
    _LserHdwTempSensorIndex_Type()
)
lserHdwTempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserHdwTempSensorIndex.setStatus("mandatory")


class _LserHdwTempSensorName_Type(OctetString):
    """Custom type lserHdwTempSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserHdwTempSensorName_Type.__name__ = "OctetString"
_LserHdwTempSensorName_Object = MibTableColumn
lserHdwTempSensorName = _LserHdwTempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 2, 1, 2),
    _LserHdwTempSensorName_Type()
)
lserHdwTempSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserHdwTempSensorName.setStatus("mandatory")
_LserHdwTempSensorCurrentTemp_Type = Integer32
_LserHdwTempSensorCurrentTemp_Object = MibTableColumn
lserHdwTempSensorCurrentTemp = _LserHdwTempSensorCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 2, 1, 3),
    _LserHdwTempSensorCurrentTemp_Type()
)
lserHdwTempSensorCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserHdwTempSensorCurrentTemp.setStatus("mandatory")
_LserHdwTempSensorHighTemp_Type = Integer32
_LserHdwTempSensorHighTemp_Object = MibTableColumn
lserHdwTempSensorHighTemp = _LserHdwTempSensorHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 2, 1, 4),
    _LserHdwTempSensorHighTemp_Type()
)
lserHdwTempSensorHighTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserHdwTempSensorHighTemp.setStatus("mandatory")
_LserHdwTempSensorWarnThreshold_Type = Integer32
_LserHdwTempSensorWarnThreshold_Object = MibTableColumn
lserHdwTempSensorWarnThreshold = _LserHdwTempSensorWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 2, 1, 5),
    _LserHdwTempSensorWarnThreshold_Type()
)
lserHdwTempSensorWarnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserHdwTempSensorWarnThreshold.setStatus("mandatory")
_LserHdwTempSensorFailThreshold_Type = Integer32
_LserHdwTempSensorFailThreshold_Object = MibTableColumn
lserHdwTempSensorFailThreshold = _LserHdwTempSensorFailThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 2, 1, 6),
    _LserHdwTempSensorFailThreshold_Type()
)
lserHdwTempSensorFailThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lserHdwTempSensorFailThreshold.setStatus("mandatory")
_LserHdwNumFans_Type = Integer32
_LserHdwNumFans_Object = MibScalar
lserHdwNumFans = _LserHdwNumFans_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 3),
    _LserHdwNumFans_Type()
)
lserHdwNumFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserHdwNumFans.setStatus("mandatory")
_LserHdwFanTable_Object = MibTable
lserHdwFanTable = _LserHdwFanTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 4)
)
if mibBuilder.loadTexts:
    lserHdwFanTable.setStatus("mandatory")
_LserHdwFanEntry_Object = MibTableRow
lserHdwFanEntry = _LserHdwFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 4, 1)
)
lserHdwFanEntry.setIndexNames(
    (0, "LSERIES-TAPE-LIBRARY-MIB", "lserHdwFanIndex"),
)
if mibBuilder.loadTexts:
    lserHdwFanEntry.setStatus("mandatory")
_LserHdwFanIndex_Type = Integer32
_LserHdwFanIndex_Object = MibTableColumn
lserHdwFanIndex = _LserHdwFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 4, 1, 1),
    _LserHdwFanIndex_Type()
)
lserHdwFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserHdwFanIndex.setStatus("mandatory")


class _LserHdwFanName_Type(OctetString):
    """Custom type lserHdwFanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserHdwFanName_Type.__name__ = "OctetString"
_LserHdwFanName_Object = MibTableColumn
lserHdwFanName = _LserHdwFanName_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 4, 1, 2),
    _LserHdwFanName_Type()
)
lserHdwFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserHdwFanName.setStatus("mandatory")


class _LserHdwFanOperational_Type(Integer32):
    """Custom type lserHdwFanOperational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("normal", 2))
    )


_LserHdwFanOperational_Type.__name__ = "Integer32"
_LserHdwFanOperational_Object = MibTableColumn
lserHdwFanOperational = _LserHdwFanOperational_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 4, 1, 3),
    _LserHdwFanOperational_Type()
)
lserHdwFanOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserHdwFanOperational.setStatus("mandatory")
_LserHdwNumSupplies_Type = Integer32
_LserHdwNumSupplies_Object = MibScalar
lserHdwNumSupplies = _LserHdwNumSupplies_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 5),
    _LserHdwNumSupplies_Type()
)
lserHdwNumSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserHdwNumSupplies.setStatus("mandatory")
_LserHdwSupplyTable_Object = MibTable
lserHdwSupplyTable = _LserHdwSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 6)
)
if mibBuilder.loadTexts:
    lserHdwSupplyTable.setStatus("mandatory")
_LserHdwSupplyEntry_Object = MibTableRow
lserHdwSupplyEntry = _LserHdwSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 6, 1)
)
lserHdwSupplyEntry.setIndexNames(
    (0, "LSERIES-TAPE-LIBRARY-MIB", "lserHdwSupplyIndex"),
)
if mibBuilder.loadTexts:
    lserHdwSupplyEntry.setStatus("mandatory")
_LserHdwSupplyIndex_Type = Integer32
_LserHdwSupplyIndex_Object = MibTableColumn
lserHdwSupplyIndex = _LserHdwSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 6, 1, 1),
    _LserHdwSupplyIndex_Type()
)
lserHdwSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserHdwSupplyIndex.setStatus("mandatory")


class _LserHdwSupplyName_Type(OctetString):
    """Custom type lserHdwSupplyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LserHdwSupplyName_Type.__name__ = "OctetString"
_LserHdwSupplyName_Object = MibTableColumn
lserHdwSupplyName = _LserHdwSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 6, 1, 2),
    _LserHdwSupplyName_Type()
)
lserHdwSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserHdwSupplyName.setStatus("mandatory")


class _LserHdwSupplyInstalled_Type(Integer32):
    """Custom type lserHdwSupplyInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("notinstalled", 1))
    )


_LserHdwSupplyInstalled_Type.__name__ = "Integer32"
_LserHdwSupplyInstalled_Object = MibTableColumn
lserHdwSupplyInstalled = _LserHdwSupplyInstalled_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 6, 1, 3),
    _LserHdwSupplyInstalled_Type()
)
lserHdwSupplyInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserHdwSupplyInstalled.setStatus("mandatory")


class _LserHdwSupplyOperational_Type(Integer32):
    """Custom type lserHdwSupplyOperational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("normal", 2))
    )


_LserHdwSupplyOperational_Type.__name__ = "Integer32"
_LserHdwSupplyOperational_Object = MibTableColumn
lserHdwSupplyOperational = _LserHdwSupplyOperational_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 10, 6, 1, 4),
    _LserHdwSupplyOperational_Type()
)
lserHdwSupplyOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lserHdwSupplyOperational.setStatus("mandatory")

# Managed Objects groups


# Notification objects

lserTrapError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 0, 1)
)
lserTrapError.setObjects(
      *(("LSERIES-TAPE-LIBRARY-MIB", "lserTrapText"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserTrapSeverity"))
)
if mibBuilder.loadTexts:
    lserTrapError.setStatus(
        ""
    )

lserTrapWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 0, 2)
)
lserTrapWarning.setObjects(
      *(("LSERIES-TAPE-LIBRARY-MIB", "lserTrapText"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserTrapSeverity"))
)
if mibBuilder.loadTexts:
    lserTrapWarning.setStatus(
        ""
    )

lserTrapInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 0, 3)
)
lserTrapInformation.setObjects(
      *(("LSERIES-TAPE-LIBRARY-MIB", "lserTrapText"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserTrapSeverity"))
)
if mibBuilder.loadTexts:
    lserTrapInformation.setStatus(
        ""
    )

lserTrapConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 0, 4)
)
lserTrapConfiguration.setObjects(
      *(("LSERIES-TAPE-LIBRARY-MIB", "lserTrapText"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserTrapSeverity"))
)
if mibBuilder.loadTexts:
    lserTrapConfiguration.setStatus(
        ""
    )

lserTrapAgentStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 0, 11)
)
lserTrapAgentStart.setObjects(
    ("LSERIES-TAPE-LIBRARY-MIB", "lserAgentBootDate")
)
if mibBuilder.loadTexts:
    lserTrapAgentStart.setStatus(
        ""
    )

lserTrapLibStatusGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 0, 21)
)
lserTrapLibStatusGood.setObjects(
      *(("LSERIES-TAPE-LIBRARY-MIB", "lserLibState"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserLibStkBaseModel"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserLibSerialNumber"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserLibNetworkName"))
)
if mibBuilder.loadTexts:
    lserTrapLibStatusGood.setStatus(
        ""
    )

lserTrapLibStatusCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 0, 25)
)
lserTrapLibStatusCheck.setObjects(
      *(("LSERIES-TAPE-LIBRARY-MIB", "lserLibState"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserLibStkBaseModel"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserLibSerialNumber"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserLibNetworkName"))
)
if mibBuilder.loadTexts:
    lserTrapLibStatusCheck.setStatus(
        ""
    )

lserTrapDrvStatusGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 0, 41)
)
lserTrapDrvStatusGood.setObjects(
      *(("LSERIES-TAPE-LIBRARY-MIB", "lserLibNetworkName"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserDriveState"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserDriveIndex"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserDriveSerialNum"))
)
if mibBuilder.loadTexts:
    lserTrapDrvStatusGood.setStatus(
        ""
    )

lserTrapDrvStatusCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 0, 45)
)
lserTrapDrvStatusCheck.setObjects(
      *(("LSERIES-TAPE-LIBRARY-MIB", "lserLibNetworkName"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserDriveState"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserDriveIndex"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserDriveSerialNum"))
)
if mibBuilder.loadTexts:
    lserTrapDrvStatusCheck.setStatus(
        ""
    )

lserTrapCapStatusGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 0, 61)
)
lserTrapCapStatusGood.setObjects(
      *(("LSERIES-TAPE-LIBRARY-MIB", "lserLibNetworkName"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserCapState"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserCapIndex"))
)
if mibBuilder.loadTexts:
    lserTrapCapStatusGood.setStatus(
        ""
    )

lserTrapCapStatusOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 0, 63)
)
lserTrapCapStatusOpen.setObjects(
      *(("LSERIES-TAPE-LIBRARY-MIB", "lserLibNetworkName"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserCapState"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserCapIndex"))
)
if mibBuilder.loadTexts:
    lserTrapCapStatusOpen.setStatus(
        ""
    )

lserTrapCapStatusCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 0, 65)
)
lserTrapCapStatusCheck.setObjects(
      *(("LSERIES-TAPE-LIBRARY-MIB", "lserLibNetworkName"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserCapState"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserCapIndex"))
)
if mibBuilder.loadTexts:
    lserTrapCapStatusCheck.setStatus(
        ""
    )

lserTrapPtpStatusGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 0, 81)
)
lserTrapPtpStatusGood.setObjects(
      *(("LSERIES-TAPE-LIBRARY-MIB", "lserLibNetworkName"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserPtpState"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserPtpIndex"))
)
if mibBuilder.loadTexts:
    lserTrapPtpStatusGood.setStatus(
        ""
    )

lserTrapPtpStatusCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 0, 85)
)
lserTrapPtpStatusCheck.setObjects(
      *(("LSERIES-TAPE-LIBRARY-MIB", "lserLibNetworkName"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserPtpState"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserPtpIndex"))
)
if mibBuilder.loadTexts:
    lserTrapPtpStatusCheck.setStatus(
        ""
    )

lserTrapMediaStat = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 12, 0, 101)
)
lserTrapMediaStat.setObjects(
      *(("LSERIES-TAPE-LIBRARY-MIB", "lserMediaErrorTapeLabel"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserMediaErrorDriveSerialNum"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserMediaErrorDateTime"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserLibMediaErrorEnum"),
        ("LSERIES-TAPE-LIBRARY-MIB", "lserMediaErrorOccurrenceCount"))
)
if mibBuilder.loadTexts:
    lserTrapMediaStat.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LSERIES-TAPE-LIBRARY-MIB",
    **{"LserSnmpPort": LserSnmpPort,
       "LserSnmpTrapPort": LserSnmpTrapPort,
       "LserCmdClear": LserCmdClear,
       "LserDeviceStatus": LserDeviceStatus,
       "LserMediaErrorType": LserMediaErrorType,
       "LserDriveFibreLoopId": LserDriveFibreLoopId,
       "LserDriveFibreSpeed": LserDriveFibreSpeed,
       "LserDriveFibreAddressing": LserDriveFibreAddressing,
       "storagetek": storagetek,
       "products": products,
       "lseriesTapeLibrary": lseriesTapeLibrary,
       "lserTrapError": lserTrapError,
       "lserTrapWarning": lserTrapWarning,
       "lserTrapInformation": lserTrapInformation,
       "lserTrapConfiguration": lserTrapConfiguration,
       "lserTrapAgentStart": lserTrapAgentStart,
       "lserTrapLibStatusGood": lserTrapLibStatusGood,
       "lserTrapLibStatusCheck": lserTrapLibStatusCheck,
       "lserTrapDrvStatusGood": lserTrapDrvStatusGood,
       "lserTrapDrvStatusCheck": lserTrapDrvStatusCheck,
       "lserTrapCapStatusGood": lserTrapCapStatusGood,
       "lserTrapCapStatusOpen": lserTrapCapStatusOpen,
       "lserTrapCapStatusCheck": lserTrapCapStatusCheck,
       "lserTrapPtpStatusGood": lserTrapPtpStatusGood,
       "lserTrapPtpStatusCheck": lserTrapPtpStatusCheck,
       "lserTrapMediaStat": lserTrapMediaStat,
       "lserAgent": lserAgent,
       "lserAgentRevision": lserAgentRevision,
       "lserAgentBootDate": lserAgentBootDate,
       "lserAgentURL": lserAgentURL,
       "lserAgentPort": lserAgentPort,
       "lserAgentCommunity": lserAgentCommunity,
       "lserAgentTrapSink": lserAgentTrapSink,
       "lserAgentTrapSinkClear": lserAgentTrapSinkClear,
       "lserAgentTrapSinkNum": lserAgentTrapSinkNum,
       "lserAgentTrapSinkTable": lserAgentTrapSinkTable,
       "lserAgentTrapSinkEntry": lserAgentTrapSinkEntry,
       "lserAgentTrapSinkTableIndex": lserAgentTrapSinkTableIndex,
       "lserAgentTrapSinkNetName": lserAgentTrapSinkNetName,
       "lserAgentTrapSinkPort": lserAgentTrapSinkPort,
       "lserAgentTrapSinkCommunity": lserAgentTrapSinkCommunity,
       "lserAgentTrapSinkVersion": lserAgentTrapSinkVersion,
       "lserAgentTrapSinkClearEntry": lserAgentTrapSinkClearEntry,
       "lserTrap": lserTrap,
       "lserTrapText": lserTrapText,
       "lserTrapSeverity": lserTrapSeverity,
       "lserLibrary": lserLibrary,
       "lserLibStkBaseModel": lserLibStkBaseModel,
       "lserLibConfigPassword": lserLibConfigPassword,
       "lserLibVersion": lserLibVersion,
       "lserLibVersionFirmRev": lserLibVersionFirmRev,
       "lserLibVersionFirmDate": lserLibVersionFirmDate,
       "lserLibVersionBootRev": lserLibVersionBootRev,
       "lserLibVersionFibre": lserLibVersionFibre,
       "lserLibVersionHardware": lserLibVersionHardware,
       "lserLibSerialNumber": lserLibSerialNumber,
       "lserLibHostInterface": lserLibHostInterface,
       "lserLibHostInterfaceType": lserLibHostInterfaceType,
       "lserLibConfig": lserLibConfig,
       "lserLibCfgNumPanels": lserLibCfgNumPanels,
       "lserLibCfgNumHandCells": lserLibCfgNumHandCells,
       "lserLibCfgMinHandAddr": lserLibCfgMinHandAddr,
       "lserLibCfgMaxHandAddr": lserLibCfgMaxHandAddr,
       "lserLibCfgNumPlayCells": lserLibCfgNumPlayCells,
       "lserLibCfgMinPlayAddr": lserLibCfgMinPlayAddr,
       "lserLibCfgMaxPlayAddr": lserLibCfgMaxPlayAddr,
       "lserLibCfgNumCaps": lserLibCfgNumCaps,
       "lserLibCfgNumCapColumns": lserLibCfgNumCapColumns,
       "lserLibCfgNumCapCells": lserLibCfgNumCapCells,
       "lserLibCfgMinCapAddr": lserLibCfgMinCapAddr,
       "lserLibCfgMaxCapAddr": lserLibCfgMaxCapAddr,
       "lserLibCfgNumDriveColumns": lserLibCfgNumDriveColumns,
       "lserLibCfgNumDrives": lserLibCfgNumDrives,
       "lserLibCfgMinDriveAddr": lserLibCfgMinDriveAddr,
       "lserLibCfgMaxDriveAddr": lserLibCfgMaxDriveAddr,
       "lserLibCfgNumStorageCells": lserLibCfgNumStorageCells,
       "lserLibCfgMinStorageAddr": lserLibCfgMinStorageAddr,
       "lserLibCfgMaxStorageAddr": lserLibCfgMaxStorageAddr,
       "lserLibCfgNumPtps": lserLibCfgNumPtps,
       "lserLibCfgNumPtpColumns": lserLibCfgNumPtpColumns,
       "lserLibCfgNumPtpCells": lserLibCfgNumPtpCells,
       "lserLibCfgMinPtpAddr": lserLibCfgMinPtpAddr,
       "lserLibCfgMaxPtpAddr": lserLibCfgMaxPtpAddr,
       "lserLibState": lserLibState,
       "lserLibStatusEnum": lserLibStatusEnum,
       "lserLibLog": lserLibLog,
       "lserLibLogClear": lserLibLogClear,
       "lserLibLogNumFscs": lserLibLogNumFscs,
       "lserLibLogTable": lserLibLogTable,
       "lserLibLogEntry": lserLibLogEntry,
       "lserLibLogTableIndex": lserLibLogTableIndex,
       "lserLibLogFscNumber": lserLibLogFscNumber,
       "lserLibLogMechanism": lserLibLogMechanism,
       "lserLibLogFscCount": lserLibLogFscCount,
       "lserLibLogDateTime": lserLibLogDateTime,
       "lserLibLogSummary": lserLibLogSummary,
       "lserLibLogText": lserLibLogText,
       "lserLibLogClearEntry": lserLibLogClearEntry,
       "lserLibLogSeverity": lserLibLogSeverity,
       "lserLibDeviceID": lserLibDeviceID,
       "lserLibFastLoad": lserLibFastLoad,
       "lserLibLocation": lserLibLocation,
       "lserLibLocatContact": lserLibLocatContact,
       "lserLibLocatStreet": lserLibLocatStreet,
       "lserLibLocatState": lserLibLocatState,
       "lserLibLocatZip": lserLibLocatZip,
       "lserLibLocatCountry": lserLibLocatCountry,
       "lserLibLocatDescr": lserLibLocatDescr,
       "lserLibLocatCity": lserLibLocatCity,
       "lserLibNetwork": lserLibNetwork,
       "lserLibNetworkIpAddr": lserLibNetworkIpAddr,
       "lserLibNetworkGateway": lserLibNetworkGateway,
       "lserLibNetworkEthAddr": lserLibNetworkEthAddr,
       "lserLibNetworkName": lserLibNetworkName,
       "lserLibNetworkNetmask": lserLibNetworkNetmask,
       "lserLibNetworkFibrePresent": lserLibNetworkFibrePresent,
       "lserLibNetworkFibreID": lserLibNetworkFibreID,
       "lserLibNetworkFibreNumPorts": lserLibNetworkFibreNumPorts,
       "lserLibNetworkDhcpEnabled": lserLibNetworkDhcpEnabled,
       "lserLibNetworkDomainName": lserLibNetworkDomainName,
       "lserLibNetworkPrimaryDNS": lserLibNetworkPrimaryDNS,
       "lserLibNetworkSecondaryDNS": lserLibNetworkSecondaryDNS,
       "lserLibStatistics": lserLibStatistics,
       "lserLibStatsNumIPL": lserLibStatsNumIPL,
       "lserLibStatsNumDoorOpens": lserLibStatsNumDoorOpens,
       "lserLibStatsNumGetRetries": lserLibStatsNumGetRetries,
       "lserLibStatsNumGetFails": lserLibStatsNumGetFails,
       "lserLibStatsNumPutRetries": lserLibStatsNumPutRetries,
       "lserLibStatsNumPutFails": lserLibStatsNumPutFails,
       "lserLibStatsNumLabelRetries": lserLibStatsNumLabelRetries,
       "lserLibStatsNumLabelFails": lserLibStatsNumLabelFails,
       "lserLibStatsNumTargetRetries": lserLibStatsNumTargetRetries,
       "lserLibStatsNumTargetFails": lserLibStatsNumTargetFails,
       "lserLibStatsNumMoves": lserLibStatsNumMoves,
       "lserLibStatsNumMounts": lserLibStatsNumMounts,
       "lserLibStatsNumTargetReads": lserLibStatsNumTargetReads,
       "lserLibStatsNumEmptyReads": lserLibStatsNumEmptyReads,
       "lserLibStatsNumLabelReads": lserLibStatsNumLabelReads,
       "lserLibStats5minuteSample": lserLibStats5minuteSample,
       "lserLibStats5minSampleCount": lserLibStats5minSampleCount,
       "lserLibStats5minIdle": lserLibStats5minIdle,
       "lserLibStats5min1to25": lserLibStats5min1to25,
       "lserLibStats5min26to50": lserLibStats5min26to50,
       "lserLibStats5min51to75": lserLibStats5min51to75,
       "lserLibStats5min76to100": lserLibStats5min76to100,
       "lserLibStats5min101to125": lserLibStats5min101to125,
       "lserLibStats5min126to150": lserLibStats5min126to150,
       "lserLibStats5min151to175": lserLibStats5min151to175,
       "lserLibStats5min176to200": lserLibStats5min176to200,
       "lserLibStats5min201to225": lserLibStats5min201to225,
       "lserLibStats5min226to250": lserLibStats5min226to250,
       "lserLibStats5min251to300": lserLibStats5min251to300,
       "lserLibStats5min301to350": lserLibStats5min301to350,
       "lserLibStats5min351to400": lserLibStats5min351to400,
       "lserLibStats5min401to450": lserLibStats5min401to450,
       "lserLibStats5min451to500": lserLibStats5min451to500,
       "lserLibStats5min501to550": lserLibStats5min501to550,
       "lserLibStats5min551to600": lserLibStats5min551to600,
       "lserLibStats5min601to650": lserLibStats5min601to650,
       "lserLibStats5min651to700": lserLibStats5min651to700,
       "lserLibStats5minOver700": lserLibStats5minOver700,
       "lserLibStats15minuteSample": lserLibStats15minuteSample,
       "lserLibStats15minSampleCount": lserLibStats15minSampleCount,
       "lserLibStats15minIdle": lserLibStats15minIdle,
       "lserLibStats15min1to25": lserLibStats15min1to25,
       "lserLibStats15min26to50": lserLibStats15min26to50,
       "lserLibStats15min51to75": lserLibStats15min51to75,
       "lserLibStats15min76to100": lserLibStats15min76to100,
       "lserLibStats15min101to125": lserLibStats15min101to125,
       "lserLibStats15min126to150": lserLibStats15min126to150,
       "lserLibStats15min151to175": lserLibStats15min151to175,
       "lserLibStats15min176to200": lserLibStats15min176to200,
       "lserLibStats15min201to225": lserLibStats15min201to225,
       "lserLibStats15min226to250": lserLibStats15min226to250,
       "lserLibStats15min251to300": lserLibStats15min251to300,
       "lserLibStats15min301to350": lserLibStats15min301to350,
       "lserLibStats15min351to400": lserLibStats15min351to400,
       "lserLibStats15min401to450": lserLibStats15min401to450,
       "lserLibStats15min451to500": lserLibStats15min451to500,
       "lserLibStats15min501to550": lserLibStats15min501to550,
       "lserLibStats15min551to600": lserLibStats15min551to600,
       "lserLibStats15min601to650": lserLibStats15min601to650,
       "lserLibStats15min651to700": lserLibStats15min651to700,
       "lserLibStats15minOver700": lserLibStats15minOver700,
       "lserLibStatsGlobalClear": lserLibStatsGlobalClear,
       "lserLibMediaErrors": lserLibMediaErrors,
       "lserMediaErrorCount": lserMediaErrorCount,
       "lserLibMediaErrorTable": lserLibMediaErrorTable,
       "lserLibMediaErrorEntry": lserLibMediaErrorEntry,
       "lserMediaErrorIndex": lserMediaErrorIndex,
       "lserMediaErrorTapeLabel": lserMediaErrorTapeLabel,
       "lserMediaErrorDriveSerialNum": lserMediaErrorDriveSerialNum,
       "lserMediaErrorDateTime": lserMediaErrorDateTime,
       "lserLibMediaErrorEnum": lserLibMediaErrorEnum,
       "lserMediaErrorOccurrenceCount": lserMediaErrorOccurrenceCount,
       "lserLibDate": lserLibDate,
       "lserLibDateMonth": lserLibDateMonth,
       "lserLibDateDay": lserLibDateDay,
       "lserLibDateYear": lserLibDateYear,
       "lserLibDateHour": lserLibDateHour,
       "lserLibDateMinute": lserLibDateMinute,
       "lserLibDateSecond": lserLibDateSecond,
       "lserLibDateString": lserLibDateString,
       "lserLibPersonality": lserLibPersonality,
       "lserLibPersonVendor": lserLibPersonVendor,
       "lserLibPersonModel": lserLibPersonModel,
       "lserLibPersonWebEnabled": lserLibPersonWebEnabled,
       "lserLibPersonLibSize": lserLibPersonLibSize,
       "lserLibCleaning": lserLibCleaning,
       "lserLibCleanEnabled": lserLibCleanEnabled,
       "lserLibCleanNumCartTypes": lserLibCleanNumCartTypes,
       "lserLibCleanWarnTable": lserLibCleanWarnTable,
       "lserLibCleanWarnEntry": lserLibCleanWarnEntry,
       "lserLibCleanWarnIndex": lserLibCleanWarnIndex,
       "lserLibCleanCartType": lserLibCleanCartType,
       "lserLibCleanWarnCount": lserLibCleanWarnCount,
       "lserLibCleanNumCarts": lserLibCleanNumCarts,
       "lserLibCleanCartTable": lserLibCleanCartTable,
       "lserLibCleanCartEntry": lserLibCleanCartEntry,
       "lserCleanCartIndex": lserCleanCartIndex,
       "lserCleanCartLabel": lserCleanCartLabel,
       "lserCleanCartType": lserCleanCartType,
       "lserCleanCartLocationElementID": lserCleanCartLocationElementID,
       "lserCleanCartHostAccessible": lserCleanCartHostAccessible,
       "lserCleanCartUsageCount": lserCleanCartUsageCount,
       "lserDrives": lserDrives,
       "lserDriveCount": lserDriveCount,
       "lserDriveTable": lserDriveTable,
       "lserDriveEntry": lserDriveEntry,
       "lserDriveIndex": lserDriveIndex,
       "lserDriveElementID": lserDriveElementID,
       "lserDriveRowInLib": lserDriveRowInLib,
       "lserDriveColInLib": lserDriveColInLib,
       "lserDriveType": lserDriveType,
       "lserDriveVendor": lserDriveVendor,
       "lserDriveSerialNum": lserDriveSerialNum,
       "lserDriveInterfaceType": lserDriveInterfaceType,
       "lserDriveID": lserDriveID,
       "lserDriveState": lserDriveState,
       "lserDriveStatusEnum": lserDriveStatusEnum,
       "lserDriveCodeVer": lserDriveCodeVer,
       "lserDriveVersion": lserDriveVersion,
       "lserDriveFirmwareVer": lserDriveFirmwareVer,
       "lserDriveGetRetries": lserDriveGetRetries,
       "lserDrivePutRetries": lserDrivePutRetries,
       "lserDriveCommandClean": lserDriveCommandClean,
       "lserDriveCellStatusEnum": lserDriveCellStatusEnum,
       "lserDriveCellStatusText": lserDriveCellStatusText,
       "lserDriveCellContentLabel": lserDriveCellContentLabel,
       "lserDriveCellContentType": lserDriveCellContentType,
       "lserDriveIdleSeconds": lserDriveIdleSeconds,
       "lserDriveNumMounts": lserDriveNumMounts,
       "lserDriveUsageSampleCount": lserDriveUsageSampleCount,
       "lserDriveUsageMinimum": lserDriveUsageMinimum,
       "lserDriveUsage5min": lserDriveUsage5min,
       "lserDriveUsage5to10": lserDriveUsage5to10,
       "lserDriveUsage10to30": lserDriveUsage10to30,
       "lserDriveUsage30to60": lserDriveUsage30to60,
       "lserDriveUsageMaximum": lserDriveUsageMaximum,
       "lserDriveFibreCount": lserDriveFibreCount,
       "lserDriveFibreTable": lserDriveFibreTable,
       "lserDriveFibreEntry": lserDriveFibreEntry,
       "lserDriveFibreIndex": lserDriveFibreIndex,
       "lserDriveFibreSerialNum": lserDriveFibreSerialNum,
       "lserDriveFibreNodeName": lserDriveFibreNodeName,
       "lserDriveFibrePortCount": lserDriveFibrePortCount,
       "lserDriveFibrePortAWWN": lserDriveFibrePortAWWN,
       "lserDriveFibrePortAAddressingMode": lserDriveFibrePortAAddressingMode,
       "lserDriveFibrePortAPortEnabled": lserDriveFibrePortAPortEnabled,
       "lserDriveFibrePortALoopId": lserDriveFibrePortALoopId,
       "lserDriveFibrePortAPortSpeed": lserDriveFibrePortAPortSpeed,
       "lserDriveFibrePortBWWN": lserDriveFibrePortBWWN,
       "lserDriveFibrePortBAddressingMode": lserDriveFibrePortBAddressingMode,
       "lserDriveFibrePortBPortEnabled": lserDriveFibrePortBPortEnabled,
       "lserDriveFibrePortBLoopId": lserDriveFibrePortBLoopId,
       "lserDriveFibrePortBPortSpeed": lserDriveFibrePortBPortSpeed,
       "lserDriveWWNEnabled": lserDriveWWNEnabled,
       "lserCaps": lserCaps,
       "lserCapCount": lserCapCount,
       "lserCapTable": lserCapTable,
       "lserCapEntry": lserCapEntry,
       "lserCapIndex": lserCapIndex,
       "lserCapAccessibility": lserCapAccessibility,
       "lserCapAccessStateEnum": lserCapAccessStateEnum,
       "lserCapState": lserCapState,
       "lserCapStatusEnum": lserCapStatusEnum,
       "lserCapUsageGetSampleCount": lserCapUsageGetSampleCount,
       "lserCapUsageGetIdle": lserCapUsageGetIdle,
       "lserCapUsageGet1": lserCapUsageGet1,
       "lserCapUsageGet2": lserCapUsageGet2,
       "lserCapUsageGet3": lserCapUsageGet3,
       "lserCapUsageGet4": lserCapUsageGet4,
       "lserCapUsageGet5": lserCapUsageGet5,
       "lserCapUsageGet6to10": lserCapUsageGet6to10,
       "lserCapUsageGet11to15": lserCapUsageGet11to15,
       "lserCapUsageGet16to20": lserCapUsageGet16to20,
       "lserCapUsageGet21toMax": lserCapUsageGet21toMax,
       "lserCapUsagePutSampleCount": lserCapUsagePutSampleCount,
       "lserCapUsagePutIdle": lserCapUsagePutIdle,
       "lserCapUsagePut1": lserCapUsagePut1,
       "lserCapUsagePut2": lserCapUsagePut2,
       "lserCapUsagePut3": lserCapUsagePut3,
       "lserCapUsagePut4": lserCapUsagePut4,
       "lserCapUsagePut5": lserCapUsagePut5,
       "lserCapUsagePut6to10": lserCapUsagePut6to10,
       "lserCapUsagePut11to15": lserCapUsagePut11to15,
       "lserCapUsagePut16to20": lserCapUsagePut16to20,
       "lserCapUsagePut21toMax": lserCapUsagePut21toMax,
       "lserCapName": lserCapName,
       "lserPassThru": lserPassThru,
       "lserPtpCount": lserPtpCount,
       "lserPtpTable": lserPtpTable,
       "lserPtpEntry": lserPtpEntry,
       "lserPtpIndex": lserPtpIndex,
       "lserPtpState": lserPtpState,
       "lserPtpStatusEnum": lserPtpStatusEnum,
       "lserPtpSerialNumber": lserPtpSerialNumber,
       "lserPtpPartNumber": lserPtpPartNumber,
       "lserPtpFirmwareVersion": lserPtpFirmwareVersion,
       "lserPtpFirmwareDate": lserPtpFirmwareDate,
       "lserPtpSoftwareResetCount": lserPtpSoftwareResetCount,
       "lserPtpDoorOpenCount": lserPtpDoorOpenCount,
       "lserPtpInitializationCount": lserPtpInitializationCount,
       "lserPtpInoperativeCount": lserPtpInoperativeCount,
       "lserPtpGoodCommandCount": lserPtpGoodCommandCount,
       "lserPtpFailCommandCount": lserPtpFailCommandCount,
       "lserPtpGoodEmptyMotionCount": lserPtpGoodEmptyMotionCount,
       "lserPtpFailEmptyMotionCount": lserPtpFailEmptyMotionCount,
       "lserPtpGoodPartMotionCount": lserPtpGoodPartMotionCount,
       "lserPtpFailPartMotionCount": lserPtpFailPartMotionCount,
       "lserPtpGoodFullMotionCount": lserPtpGoodFullMotionCount,
       "lserPtpFailFullMotionCount": lserPtpFailFullMotionCount,
       "lserPtpCompLibNetworkIpAddr": lserPtpCompLibNetworkIpAddr,
       "lserPtpCompLibNetworkName": lserPtpCompLibNetworkName,
       "lserPtpCompLibSerialNumber": lserPtpCompLibSerialNumber,
       "lserPtpCompLibPartNumber": lserPtpCompLibPartNumber,
       "lserPtpCompLibVendorName": lserPtpCompLibVendorName,
       "lserPtpCompLibModelName": lserPtpCompLibModelName,
       "lserPtpCompLibFirmwareVersion": lserPtpCompLibFirmwareVersion,
       "lserPtpCompLibFirmwareDate": lserPtpCompLibFirmwareDate,
       "lserInventory": lserInventory,
       "lserTapeCount": lserTapeCount,
       "lserTapeTable": lserTapeTable,
       "lserTapeEntry": lserTapeEntry,
       "lserTapeIndex": lserTapeIndex,
       "lserTapeLabel": lserTapeLabel,
       "lserTapeType": lserTapeType,
       "lserTapeLocationElementID": lserTapeLocationElementID,
       "lserTapeHostAccessible": lserTapeHostAccessible,
       "lserStorage": lserStorage,
       "lserCellCount": lserCellCount,
       "lserCellTable": lserCellTable,
       "lserCellEntry": lserCellEntry,
       "lserCellIndex": lserCellIndex,
       "lserCellElementID": lserCellElementID,
       "lserCellHostAccessible": lserCellHostAccessible,
       "lserCellContentStatus": lserCellContentStatus,
       "lserCellContentLabel": lserCellContentLabel,
       "lserCellContentType": lserCellContentType,
       "lserCellGetRetryCount": lserCellGetRetryCount,
       "lserCellPutRetryCount": lserCellPutRetryCount,
       "lserStorageFreeCells": lserStorageFreeCells,
       "lserPlayground": lserPlayground,
       "lserPlayCellCount": lserPlayCellCount,
       "lserPlayCellTable": lserPlayCellTable,
       "lserPlayCellEntry": lserPlayCellEntry,
       "lserPlayCellIndex": lserPlayCellIndex,
       "lserPlayCellElementID": lserPlayCellElementID,
       "lserPlayCellContentStatus": lserPlayCellContentStatus,
       "lserPlayCellContentLabel": lserPlayCellContentLabel,
       "lserPlayCellContentType": lserPlayCellContentType,
       "lserHardwareMonitor": lserHardwareMonitor,
       "lserHdwNumTempSensors": lserHdwNumTempSensors,
       "lserHdwTempSensorTable": lserHdwTempSensorTable,
       "lserHdwTempSensorEntry": lserHdwTempSensorEntry,
       "lserHdwTempSensorIndex": lserHdwTempSensorIndex,
       "lserHdwTempSensorName": lserHdwTempSensorName,
       "lserHdwTempSensorCurrentTemp": lserHdwTempSensorCurrentTemp,
       "lserHdwTempSensorHighTemp": lserHdwTempSensorHighTemp,
       "lserHdwTempSensorWarnThreshold": lserHdwTempSensorWarnThreshold,
       "lserHdwTempSensorFailThreshold": lserHdwTempSensorFailThreshold,
       "lserHdwNumFans": lserHdwNumFans,
       "lserHdwFanTable": lserHdwFanTable,
       "lserHdwFanEntry": lserHdwFanEntry,
       "lserHdwFanIndex": lserHdwFanIndex,
       "lserHdwFanName": lserHdwFanName,
       "lserHdwFanOperational": lserHdwFanOperational,
       "lserHdwNumSupplies": lserHdwNumSupplies,
       "lserHdwSupplyTable": lserHdwSupplyTable,
       "lserHdwSupplyEntry": lserHdwSupplyEntry,
       "lserHdwSupplyIndex": lserHdwSupplyIndex,
       "lserHdwSupplyName": lserHdwSupplyName,
       "lserHdwSupplyInstalled": lserHdwSupplyInstalled,
       "lserHdwSupplyOperational": lserHdwSupplyOperational}
)
