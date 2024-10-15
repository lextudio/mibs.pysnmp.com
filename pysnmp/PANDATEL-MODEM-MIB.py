# SNMP MIB module (PANDATEL-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PANDATEL-MODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:40 2024
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

_Pandatel_ObjectIdentity = ObjectIdentity
pandatel = _Pandatel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1)
)
_Wan_products_ObjectIdentity = ObjectIdentity
wan_products = _Wan_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2)
)
_Mdm_mgmt_ObjectIdentity = ObjectIdentity
mdm_mgmt = _Mdm_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1)
)
_MdmGroup_ObjectIdentity = ObjectIdentity
mdmGroup = _MdmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 1)
)
_MdmInstalledRacks_Type = Integer32
_MdmInstalledRacks_Object = MibScalar
mdmInstalledRacks = _MdmInstalledRacks_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 1, 1),
    _MdmInstalledRacks_Type()
)
mdmInstalledRacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmInstalledRacks.setStatus("mandatory")
_MdmInstalledModems_Type = Integer32
_MdmInstalledModems_Object = MibScalar
mdmInstalledModems = _MdmInstalledModems_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 1, 2),
    _MdmInstalledModems_Type()
)
mdmInstalledModems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmInstalledModems.setStatus("mandatory")


class _MdmLoopModeTraps_Type(Integer32):
    """Custom type mdmLoopModeTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_MdmLoopModeTraps_Type.__name__ = "Integer32"
_MdmLoopModeTraps_Object = MibScalar
mdmLoopModeTraps = _MdmLoopModeTraps_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 1, 3),
    _MdmLoopModeTraps_Type()
)
mdmLoopModeTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLoopModeTraps.setStatus("mandatory")
_MdmCurrentDate_Type = DisplayString
_MdmCurrentDate_Object = MibScalar
mdmCurrentDate = _MdmCurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 1, 13),
    _MdmCurrentDate_Type()
)
mdmCurrentDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCurrentDate.setStatus("mandatory")
_MdmCurrentTime_Type = DisplayString
_MdmCurrentTime_Object = MibScalar
mdmCurrentTime = _MdmCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 1, 14),
    _MdmCurrentTime_Type()
)
mdmCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCurrentTime.setStatus("mandatory")
_MdmRackTable_Object = MibTable
mdmRackTable = _MdmRackTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mdmRackTable.setStatus("mandatory")
_RackEntry_Object = MibTableRow
rackEntry = _RackEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 2, 1)
)
rackEntry.setIndexNames(
    (0, "PANDATEL-MODEM-MIB", "rackRack"),
)
if mibBuilder.loadTexts:
    rackEntry.setStatus("mandatory")
_RackRack_Type = Integer32
_RackRack_Object = MibTableColumn
rackRack = _RackRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 2, 1, 1),
    _RackRack_Type()
)
rackRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackRack.setStatus("mandatory")


class _RackType_Type(Integer32):
    """Custom type rackType based on Integer32"""
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
        *(("device-stack-15s", 6),
          ("hs-rack-10s-3hu", 9),
          ("hs-rack-3s-1c-3hu", 11),
          ("other", 1),
          ("rack-10s-2c-6hu", 8),
          ("rack-10s-3hu", 2),
          ("rack-10s-6hu", 4),
          ("rack-12s-3hu", 3),
          ("rack-1s-1c-1hu", 12),
          ("rack-3s-1c-1hu", 13),
          ("rack-6s-9s-6hu", 5),
          ("rack-8s-2c-6hu", 10),
          ("rack-8s-4hu", 7))
    )


_RackType_Type.__name__ = "Integer32"
_RackType_Object = MibTableColumn
rackType = _RackType_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 2, 1, 2),
    _RackType_Type()
)
rackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackType.setStatus("mandatory")
_RackDescription_Type = DisplayString
_RackDescription_Object = MibTableColumn
rackDescription = _RackDescription_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 2, 1, 3),
    _RackDescription_Type()
)
rackDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackDescription.setStatus("mandatory")
_RackModemSlots_Type = Integer32
_RackModemSlots_Object = MibTableColumn
rackModemSlots = _RackModemSlots_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 2, 1, 4),
    _RackModemSlots_Type()
)
rackModemSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackModemSlots.setStatus("mandatory")
_RackModems_Type = Integer32
_RackModems_Object = MibTableColumn
rackModems = _RackModems_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 2, 1, 5),
    _RackModems_Type()
)
rackModems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackModems.setStatus("mandatory")


class _RackPowerSupplySlots_Type(Integer32):
    """Custom type rackPowerSupplySlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            999
        )
    )
    namedValues = NamedValues(
        ("unknown", 999)
    )


_RackPowerSupplySlots_Type.__name__ = "Integer32"
_RackPowerSupplySlots_Object = MibTableColumn
rackPowerSupplySlots = _RackPowerSupplySlots_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 2, 1, 6),
    _RackPowerSupplySlots_Type()
)
rackPowerSupplySlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackPowerSupplySlots.setStatus("mandatory")


class _RackPowerSupplies_Type(Integer32):
    """Custom type rackPowerSupplies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            999
        )
    )
    namedValues = NamedValues(
        ("unknown", 999)
    )


_RackPowerSupplies_Type.__name__ = "Integer32"
_RackPowerSupplies_Object = MibTableColumn
rackPowerSupplies = _RackPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 2, 1, 7),
    _RackPowerSupplies_Type()
)
rackPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackPowerSupplies.setStatus("mandatory")
_MdmModemTable_Object = MibTable
mdmModemTable = _MdmModemTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    mdmModemTable.setStatus("mandatory")
_ModemEntry_Object = MibTableRow
modemEntry = _ModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 3, 1)
)
modemEntry.setIndexNames(
    (0, "PANDATEL-MODEM-MIB", "mdmRack"),
    (0, "PANDATEL-MODEM-MIB", "mdmModem"),
)
if mibBuilder.loadTexts:
    modemEntry.setStatus("mandatory")
_MdmRack_Type = Integer32
_MdmRack_Object = MibTableColumn
mdmRack = _MdmRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 3, 1, 1),
    _MdmRack_Type()
)
mdmRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRack.setStatus("mandatory")
_MdmModem_Type = Integer32
_MdmModem_Object = MibTableColumn
mdmModem = _MdmModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 3, 1, 2),
    _MdmModem_Type()
)
mdmModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmModem.setStatus("mandatory")
_MdmDescription_Type = DisplayString
_MdmDescription_Object = MibTableColumn
mdmDescription = _MdmDescription_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 3, 1, 3),
    _MdmDescription_Type()
)
mdmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDescription.setStatus("mandatory")
_MdmUserName_Type = DisplayString
_MdmUserName_Object = MibTableColumn
mdmUserName = _MdmUserName_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 3, 1, 4),
    _MdmUserName_Type()
)
mdmUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmUserName.setStatus("mandatory")


class _MdmSelfTest_Type(Integer32):
    """Custom type mdmSelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("start", 1))
    )


_MdmSelfTest_Type.__name__ = "Integer32"
_MdmSelfTest_Object = MibTableColumn
mdmSelfTest = _MdmSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 3, 1, 5),
    _MdmSelfTest_Type()
)
mdmSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmSelfTest.setStatus("mandatory")


class _MdmSelfTestResult_Type(Integer32):
    """Custom type mdmSelfTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("cancelled", 99),
          ("eeprom-error", 7),
          ("line-if-error", 8),
          ("never-started", 98),
          ("ok", 100),
          ("other-error", 97),
          ("ram-error", 5),
          ("rom-error", 6),
          ("running", 4),
          ("started", 3))
    )


_MdmSelfTestResult_Type.__name__ = "Integer32"
_MdmSelfTestResult_Object = MibTableColumn
mdmSelfTestResult = _MdmSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 3, 1, 6),
    _MdmSelfTestResult_Type()
)
mdmSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmSelfTestResult.setStatus("mandatory")


class _MdmRemoteAccessStatus_Type(Integer32):
    """Custom type mdmRemoteAccessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("no-access", 3))
    )


_MdmRemoteAccessStatus_Type.__name__ = "Integer32"
_MdmRemoteAccessStatus_Object = MibTableColumn
mdmRemoteAccessStatus = _MdmRemoteAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 3, 1, 7),
    _MdmRemoteAccessStatus_Type()
)
mdmRemoteAccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRemoteAccessStatus.setStatus("mandatory")
_MdmInterfacePorts_Type = Integer32
_MdmInterfacePorts_Object = MibTableColumn
mdmInterfacePorts = _MdmInterfacePorts_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 3, 1, 8),
    _MdmInterfacePorts_Type()
)
mdmInterfacePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmInterfacePorts.setStatus("mandatory")
_MdmLinePorts_Type = Integer32
_MdmLinePorts_Object = MibTableColumn
mdmLinePorts = _MdmLinePorts_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 3, 1, 9),
    _MdmLinePorts_Type()
)
mdmLinePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmLinePorts.setStatus("mandatory")
_MdmVerInfoTable_Object = MibTable
mdmVerInfoTable = _MdmVerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    mdmVerInfoTable.setStatus("mandatory")
_VerInfoEntry_Object = MibTableRow
verInfoEntry = _VerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 4, 1)
)
verInfoEntry.setIndexNames(
    (0, "PANDATEL-MODEM-MIB", "viRack"),
    (0, "PANDATEL-MODEM-MIB", "viModem"),
)
if mibBuilder.loadTexts:
    verInfoEntry.setStatus("mandatory")
_ViRack_Type = Integer32
_ViRack_Object = MibTableColumn
viRack = _ViRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 4, 1, 1),
    _ViRack_Type()
)
viRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viRack.setStatus("mandatory")
_ViModem_Type = Integer32
_ViModem_Object = MibTableColumn
viModem = _ViModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 4, 1, 2),
    _ViModem_Type()
)
viModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viModem.setStatus("mandatory")


class _ViType_Type(Integer32):
    """Custom type viType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              101,
              102,
              103,
              201,
              202,
              203,
              204,
              205,
              206,
              301,
              302,
              401,
              501,
              502,
              503,
              504,
              505,
              506,
              507,
              601,
              701,
              801,
              802,
              901)
        )
    )
    namedValues = NamedValues(
        *(("bm-p", 301),
          ("bm-z", 302),
          ("cmx-ie", 802),
          ("emx", 801),
          ("etc", 901),
          ("fhfl", 101),
          ("fhfl-f", 102),
          ("fhfl-s", 103),
          ("fme", 601),
          ("fobus", 501),
          ("fx", 502),
          ("fx-g", 506),
          ("fx-i", 503),
          ("fx-ig", 504),
          ("fx-ih", 507),
          ("gm-d", 203),
          ("gm-d-f", 206),
          ("gm-f", 202),
          ("gm-h", 201),
          ("gm-s", 204),
          ("gm-s-f", 205),
          ("gx", 401),
          ("inax", 701),
          ("not-present", 0),
          ("os", 505),
          ("other", 1))
    )


_ViType_Type.__name__ = "Integer32"
_ViType_Object = MibTableColumn
viType = _ViType_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 4, 1, 3),
    _ViType_Type()
)
viType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viType.setStatus("mandatory")
_ViFirmwVer_Type = DisplayString
_ViFirmwVer_Object = MibTableColumn
viFirmwVer = _ViFirmwVer_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 4, 1, 4),
    _ViFirmwVer_Type()
)
viFirmwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viFirmwVer.setStatus("mandatory")
_ViUnitRel_Type = DisplayString
_ViUnitRel_Object = MibTableColumn
viUnitRel = _ViUnitRel_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 4, 1, 5),
    _ViUnitRel_Type()
)
viUnitRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viUnitRel.setStatus("mandatory")
_ViArtNo_Type = DisplayString
_ViArtNo_Object = MibTableColumn
viArtNo = _ViArtNo_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 4, 1, 6),
    _ViArtNo_Type()
)
viArtNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viArtNo.setStatus("mandatory")


class _ViFrontVer_Type(Integer32):
    """Custom type viFrontVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("other", 1)
    )


_ViFrontVer_Type.__name__ = "Integer32"
_ViFrontVer_Object = MibTableColumn
viFrontVer = _ViFrontVer_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 4, 1, 7),
    _ViFrontVer_Type()
)
viFrontVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viFrontVer.setStatus("mandatory")
_ViSerialNumber_Type = DisplayString
_ViSerialNumber_Object = MibTableColumn
viSerialNumber = _ViSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 4, 1, 8),
    _ViSerialNumber_Type()
)
viSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viSerialNumber.setStatus("mandatory")
_MdmPortTable_Object = MibTable
mdmPortTable = _MdmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    mdmPortTable.setStatus("mandatory")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 5, 1)
)
portEntry.setIndexNames(
    (0, "PANDATEL-MODEM-MIB", "portRack"),
    (0, "PANDATEL-MODEM-MIB", "portModem"),
    (0, "PANDATEL-MODEM-MIB", "portPort"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")
_PortRack_Type = Integer32
_PortRack_Object = MibTableColumn
portRack = _PortRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 5, 1, 1),
    _PortRack_Type()
)
portRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRack.setStatus("mandatory")
_PortModem_Type = Integer32
_PortModem_Object = MibTableColumn
portModem = _PortModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 5, 1, 2),
    _PortModem_Type()
)
portModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModem.setStatus("mandatory")
_PortPort_Type = Integer32
_PortPort_Object = MibTableColumn
portPort = _PortPort_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 5, 1, 3),
    _PortPort_Type()
)
portPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPort.setStatus("mandatory")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
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
        *(("backup-port", 6),
          ("interface-port", 2),
          ("line-port", 3),
          ("other", 1),
          ("outband-mgmt-port", 5),
          ("vt100-mgmt-port", 4))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 5, 1, 4),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("mandatory")


class _PortInterfaceType_Type(Integer32):
    """Custom type portInterfaceType based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              34,
              39,
              40,
              48,
              55,
              56,
              66,
              67,
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
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              999)
        )
    )
    namedValues = NamedValues(
        *(("atm-26mb", 18),
          ("bm", 34),
          ("eth-bridge", 48),
          ("fo-e1t1", 13),
          ("g703-64k", 9),
          ("g703-e1", 55),
          ("g703-e1t1", 7),
          ("g703-e2", 56),
          ("g703-e2t2", 8),
          ("g703-e3", 19),
          ("g703-t1", 39),
          ("g703-t2", 40),
          ("g703-t3", 20),
          ("hdsl", 15),
          ("hssi", 22),
          ("i430", 10),
          ("intercom", 12),
          ("missing", 999),
          ("mm-1300-820nm", 184),
          ("mm-820-1300nm", 183),
          ("mm-fiber-1300nm", 134),
          ("mm-fiber-1550nm", 135),
          ("mm-fiber-820nm", 133),
          ("no-module", 17),
          ("other", 1),
          ("rs485", 6),
          ("s0", 14),
          ("sm-1300-1550nm", 181),
          ("sm-1550-1300nm", 182),
          ("sm-fiber-1300nm", 131),
          ("sm-fiber-1480nm", 185),
          ("sm-fiber-1510nm", 186),
          ("sm-fiber-1530-33nm", 136),
          ("sm-fiber-1531-12nm", 137),
          ("sm-fiber-1531-90nm", 138),
          ("sm-fiber-1532-68nm", 139),
          ("sm-fiber-1533-47nm", 140),
          ("sm-fiber-1534-25nm", 141),
          ("sm-fiber-1535-04nm", 142),
          ("sm-fiber-1535-82nm", 143),
          ("sm-fiber-1536-61nm", 144),
          ("sm-fiber-1537-40nm", 145),
          ("sm-fiber-1538-19nm", 146),
          ("sm-fiber-1538-98nm", 147),
          ("sm-fiber-1538nm", 187),
          ("sm-fiber-1539-77nm", 148),
          ("sm-fiber-1540-56nm", 149),
          ("sm-fiber-1541-35nm", 150),
          ("sm-fiber-1542-14nm", 151),
          ("sm-fiber-1542-94nm", 152),
          ("sm-fiber-1543-73nm", 153),
          ("sm-fiber-1544-53nm", 154),
          ("sm-fiber-1545-32nm", 155),
          ("sm-fiber-1546-12nm", 156),
          ("sm-fiber-1546-92nm", 157),
          ("sm-fiber-1547-72nm", 158),
          ("sm-fiber-1548-51nm", 159),
          ("sm-fiber-1549-32nm", 160),
          ("sm-fiber-1550-12nm", 161),
          ("sm-fiber-1550-92nm", 162),
          ("sm-fiber-1550nm", 132),
          ("sm-fiber-1551-72nm", 163),
          ("sm-fiber-1552-52nm", 164),
          ("sm-fiber-1553-33nm", 165),
          ("sm-fiber-1553nm", 188),
          ("sm-fiber-1554-13nm", 166),
          ("sm-fiber-1554-94nm", 167),
          ("sm-fiber-1555-75nm", 168),
          ("sm-fiber-1556-55nm", 169),
          ("sm-fiber-1557-36nm", 170),
          ("sm-fiber-1558-17nm", 171),
          ("sm-fiber-1558-98nm", 172),
          ("sm-fiber-1559-79nm", 173),
          ("sm-fiber-1560-61nm", 174),
          ("sm-fiber-1561-42nm", 175),
          ("sm-fiber-1562-23nm", 176),
          ("sm-fiber-1563-05nm", 177),
          ("sm-fiber-1563-86nm", 178),
          ("sm-fiber-1564-68nm", 179),
          ("sm-fiber-1565-50nm", 180),
          ("sm-fiber-820nm", 130),
          ("sm-mm-fiber-1310nm", 189),
          ("stm-1", 67),
          ("store-loop", 11),
          ("sts-1", 21),
          ("sts-3", 66),
          ("v24", 2),
          ("v35", 3),
          ("v36", 4),
          ("x21", 5))
    )


_PortInterfaceType_Type.__name__ = "Integer32"
_PortInterfaceType_Object = MibTableColumn
portInterfaceType = _PortInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 5, 1, 5),
    _PortInterfaceType_Type()
)
portInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInterfaceType.setStatus("mandatory")


class _PortConnector_Type(Integer32):
    """Custom type portConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
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
              997,
              998,
              999)
        )
    )
    namedValues = NamedValues(
        *(("bnc", 4),
          ("db-15-f", 12),
          ("db-15-m", 13),
          ("db-25-f", 14),
          ("db-25-m", 15),
          ("db-37-f", 16),
          ("db-37-m", 17),
          ("db-9-f", 10),
          ("db-9-m", 11),
          ("dpc", 5),
          ("dual-fc", 28),
          ("dual-fc-apc", 33),
          ("dual-fiber", 3),
          ("dual-lc", 36),
          ("dual-lc-apc", 37),
          ("dual-sc", 27),
          ("dual-sc-45", 40),
          ("dual-sc-apc", 32),
          ("dual-st", 29),
          ("e2000", 23),
          ("escon", 22),
          ("ics", 8),
          ("mic", 9),
          ("mini-c", 20),
          ("minimicro", 21),
          ("mt-rj", 38),
          ("not-installed", 999),
          ("other", 1),
          ("rj45", 7),
          ("single-fc", 25),
          ("single-fc-apc", 31),
          ("single-fiber", 2),
          ("single-lc", 34),
          ("single-lc-apc", 35),
          ("single-sc", 24),
          ("single-sc-45", 39),
          ("single-sc-apc", 30),
          ("single-st", 26),
          ("unknown", 997),
          ("virtual", 998),
          ("winch-f", 18),
          ("winch-m", 19))
    )


_PortConnector_Type.__name__ = "Integer32"
_PortConnector_Object = MibTableColumn
portConnector = _PortConnector_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 5, 1, 6),
    _PortConnector_Type()
)
portConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConnector.setStatus("mandatory")


class _PortLoopMode_Type(Integer32):
    """Custom type portLoopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("digital", 3),
          ("line", 4),
          ("off", 99),
          ("other", 1),
          ("remote", 2))
    )


_PortLoopMode_Type.__name__ = "Integer32"
_PortLoopMode_Object = MibTableColumn
portLoopMode = _PortLoopMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 5, 1, 7),
    _PortLoopMode_Type()
)
portLoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLoopMode.setStatus("mandatory")
_MdmPortSignalTable_Object = MibTable
mdmPortSignalTable = _MdmPortSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    mdmPortSignalTable.setStatus("mandatory")
_PortSignalEntry_Object = MibTableRow
portSignalEntry = _PortSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 6, 1)
)
portSignalEntry.setIndexNames(
    (0, "PANDATEL-MODEM-MIB", "psignalRack"),
    (0, "PANDATEL-MODEM-MIB", "psignalModem"),
    (0, "PANDATEL-MODEM-MIB", "psignalPort"),
    (0, "PANDATEL-MODEM-MIB", "psignalType"),
)
if mibBuilder.loadTexts:
    portSignalEntry.setStatus("mandatory")
_PsignalRack_Type = Integer32
_PsignalRack_Object = MibTableColumn
psignalRack = _PsignalRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 6, 1, 1),
    _PsignalRack_Type()
)
psignalRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psignalRack.setStatus("mandatory")
_PsignalModem_Type = Integer32
_PsignalModem_Object = MibTableColumn
psignalModem = _PsignalModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 6, 1, 2),
    _PsignalModem_Type()
)
psignalModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psignalModem.setStatus("mandatory")
_PsignalPort_Type = Integer32
_PsignalPort_Object = MibTableColumn
psignalPort = _PsignalPort_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 6, 1, 3),
    _PsignalPort_Type()
)
psignalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psignalPort.setStatus("mandatory")


class _PsignalType_Type(Integer32):
    """Custom type psignalType based on Integer32"""
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
              20,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("ais", 10),
          ("bond", 12),
          ("c", 7),
          ("ca", 15),
          ("cr", 20),
          ("dcd", 4),
          ("dsr", 6),
          ("dtr", 5),
          ("eclk", 16),
          ("fsync", 9),
          ("i", 8),
          ("laser-status", 13),
          ("laser-temp", 18),
          ("laser-tx", 17),
          ("lay1", 11),
          ("link", 2),
          ("other", 1),
          ("rd", 26),
          ("rts", 3),
          ("ta", 14),
          ("td", 27))
    )


_PsignalType_Type.__name__ = "Integer32"
_PsignalType_Object = MibTableColumn
psignalType = _PsignalType_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 6, 1, 4),
    _PsignalType_Type()
)
psignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psignalType.setStatus("mandatory")


class _PsignalStatus_Type(Integer32):
    """Custom type psignalStatus based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("active", 10),
          ("down", 3),
          ("fail", 9),
          ("high", 14),
          ("low", 15),
          ("mark", 13),
          ("no", 7),
          ("off", 5),
          ("ok", 8),
          ("on", 4),
          ("other", 1),
          ("space", 12),
          ("sync", 16),
          ("traffic", 11),
          ("up", 2),
          ("yes", 6))
    )


_PsignalStatus_Type.__name__ = "Integer32"
_PsignalStatus_Object = MibTableColumn
psignalStatus = _PsignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 6, 1, 5),
    _PsignalStatus_Type()
)
psignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psignalStatus.setStatus("mandatory")


class _PsignalTrap_Type(Integer32):
    """Custom type psignalTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_PsignalTrap_Type.__name__ = "Integer32"
_PsignalTrap_Object = MibTableColumn
psignalTrap = _PsignalTrap_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 6, 1, 6),
    _PsignalTrap_Type()
)
psignalTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psignalTrap.setStatus("mandatory")
_MdmBERTTable_Object = MibTable
mdmBERTTable = _MdmBERTTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    mdmBERTTable.setStatus("mandatory")
_BertEntry_Object = MibTableRow
bertEntry = _BertEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 7, 1)
)
bertEntry.setIndexNames(
    (0, "PANDATEL-MODEM-MIB", "bertRack"),
    (0, "PANDATEL-MODEM-MIB", "bertModem"),
)
if mibBuilder.loadTexts:
    bertEntry.setStatus("mandatory")
_BertRack_Type = Integer32
_BertRack_Object = MibTableColumn
bertRack = _BertRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 7, 1, 1),
    _BertRack_Type()
)
bertRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertRack.setStatus("mandatory")
_BertModem_Type = Integer32
_BertModem_Object = MibTableColumn
bertModem = _BertModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 7, 1, 2),
    _BertModem_Type()
)
bertModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertModem.setStatus("mandatory")
_BertPort_Type = Integer32
_BertPort_Object = MibTableColumn
bertPort = _BertPort_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 7, 1, 3),
    _BertPort_Type()
)
bertPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertPort.setStatus("mandatory")


class _BertBERTest_Type(Integer32):
    """Custom type bertBERTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("start", 3),
          ("stop", 5))
    )


_BertBERTest_Type.__name__ = "Integer32"
_BertBERTest_Object = MibTableColumn
bertBERTest = _BertBERTest_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 7, 1, 4),
    _BertBERTest_Type()
)
bertBERTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertBERTest.setStatus("mandatory")


class _BertStatus_Type(Integer32):
    """Custom type bertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("never-started", 2),
          ("other", 1),
          ("running", 4),
          ("start", 3),
          ("start-failed", 7),
          ("stopped", 6))
    )


_BertStatus_Type.__name__ = "Integer32"
_BertStatus_Object = MibTableColumn
bertStatus = _BertStatus_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 7, 1, 5),
    _BertStatus_Type()
)
bertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertStatus.setStatus("mandatory")
_BertRunTime_Type = Counter32
_BertRunTime_Object = MibTableColumn
bertRunTime = _BertRunTime_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 7, 1, 6),
    _BertRunTime_Type()
)
bertRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertRunTime.setStatus("mandatory")
_BertInErrorTime_Type = Counter32
_BertInErrorTime_Object = MibTableColumn
bertInErrorTime = _BertInErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 7, 1, 7),
    _BertInErrorTime_Type()
)
bertInErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertInErrorTime.setStatus("mandatory")
_BertErrorFreeTime_Type = Counter32
_BertErrorFreeTime_Object = MibTableColumn
bertErrorFreeTime = _BertErrorFreeTime_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 7, 1, 8),
    _BertErrorFreeTime_Type()
)
bertErrorFreeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertErrorFreeTime.setStatus("mandatory")
_BertKbitsRecWrapped_Type = Counter32
_BertKbitsRecWrapped_Object = MibTableColumn
bertKbitsRecWrapped = _BertKbitsRecWrapped_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 7, 1, 9),
    _BertKbitsRecWrapped_Type()
)
bertKbitsRecWrapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertKbitsRecWrapped.setStatus("mandatory")
_BertKbitsReceived_Type = Counter32
_BertKbitsReceived_Object = MibTableColumn
bertKbitsReceived = _BertKbitsReceived_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 7, 1, 10),
    _BertKbitsReceived_Type()
)
bertKbitsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertKbitsReceived.setStatus("mandatory")
_BertErrors_Type = Counter32
_BertErrors_Object = MibTableColumn
bertErrors = _BertErrors_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 7, 1, 11),
    _BertErrors_Type()
)
bertErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertErrors.setStatus("mandatory")
_BertSyncLosts_Type = Counter32
_BertSyncLosts_Object = MibTableColumn
bertSyncLosts = _BertSyncLosts_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 7, 1, 12),
    _BertSyncLosts_Type()
)
bertSyncLosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertSyncLosts.setStatus("mandatory")


class _BertSyncStatus_Type(Integer32):
    """Custom type bertSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in-sync", 2),
          ("no-sync", 3),
          ("other", 1))
    )


_BertSyncStatus_Type.__name__ = "Integer32"
_BertSyncStatus_Object = MibTableColumn
bertSyncStatus = _BertSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 7, 1, 13),
    _BertSyncStatus_Type()
)
bertSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertSyncStatus.setStatus("mandatory")
_BertBitErrorRate_Type = DisplayString
_BertBitErrorRate_Object = MibTableColumn
bertBitErrorRate = _BertBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 7, 1, 14),
    _BertBitErrorRate_Type()
)
bertBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertBitErrorRate.setStatus("mandatory")
_MdmRemoteAccess_ObjectIdentity = ObjectIdentity
mdmRemoteAccess = _MdmRemoteAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9)
)
_RemModemTable_Object = MibTable
remModemTable = _RemModemTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 3)
)
if mibBuilder.loadTexts:
    remModemTable.setStatus("mandatory")
_RmodemEntry_Object = MibTableRow
rmodemEntry = _RmodemEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 3, 1)
)
rmodemEntry.setIndexNames(
    (0, "PANDATEL-MODEM-MIB", "rmdmRack"),
    (0, "PANDATEL-MODEM-MIB", "rmdmModem"),
)
if mibBuilder.loadTexts:
    rmodemEntry.setStatus("mandatory")
_RmdmRack_Type = Integer32
_RmdmRack_Object = MibTableColumn
rmdmRack = _RmdmRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 3, 1, 1),
    _RmdmRack_Type()
)
rmdmRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmdmRack.setStatus("mandatory")
_RmdmModem_Type = Integer32
_RmdmModem_Object = MibTableColumn
rmdmModem = _RmdmModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 3, 1, 2),
    _RmdmModem_Type()
)
rmdmModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmdmModem.setStatus("mandatory")
_RmdmDescription_Type = DisplayString
_RmdmDescription_Object = MibTableColumn
rmdmDescription = _RmdmDescription_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 3, 1, 3),
    _RmdmDescription_Type()
)
rmdmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmdmDescription.setStatus("mandatory")
_RmdmUserName_Type = DisplayString
_RmdmUserName_Object = MibTableColumn
rmdmUserName = _RmdmUserName_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 3, 1, 4),
    _RmdmUserName_Type()
)
rmdmUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmdmUserName.setStatus("mandatory")


class _RmdmSelfTest_Type(Integer32):
    """Custom type rmdmSelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("start", 1))
    )


_RmdmSelfTest_Type.__name__ = "Integer32"
_RmdmSelfTest_Object = MibTableColumn
rmdmSelfTest = _RmdmSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 3, 1, 5),
    _RmdmSelfTest_Type()
)
rmdmSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmdmSelfTest.setStatus("mandatory")


class _RmdmSelfTestResult_Type(Integer32):
    """Custom type rmdmSelfTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("cancelled", 99),
          ("eeprom-error", 7),
          ("line-if-error", 8),
          ("never-started", 98),
          ("ok", 100),
          ("other-error", 97),
          ("ram-error", 5),
          ("rom-error", 6),
          ("running", 4),
          ("started", 3))
    )


_RmdmSelfTestResult_Type.__name__ = "Integer32"
_RmdmSelfTestResult_Object = MibTableColumn
rmdmSelfTestResult = _RmdmSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 3, 1, 6),
    _RmdmSelfTestResult_Type()
)
rmdmSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmdmSelfTestResult.setStatus("mandatory")


class _RmdmRemoteAccessStatus_Type(Integer32):
    """Custom type rmdmRemoteAccessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("no-access", 3))
    )


_RmdmRemoteAccessStatus_Type.__name__ = "Integer32"
_RmdmRemoteAccessStatus_Object = MibTableColumn
rmdmRemoteAccessStatus = _RmdmRemoteAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 3, 1, 7),
    _RmdmRemoteAccessStatus_Type()
)
rmdmRemoteAccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmdmRemoteAccessStatus.setStatus("mandatory")
_RmdmInterfacePorts_Type = Integer32
_RmdmInterfacePorts_Object = MibTableColumn
rmdmInterfacePorts = _RmdmInterfacePorts_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 3, 1, 8),
    _RmdmInterfacePorts_Type()
)
rmdmInterfacePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmdmInterfacePorts.setStatus("mandatory")
_RmdmLinePorts_Type = Integer32
_RmdmLinePorts_Object = MibTableColumn
rmdmLinePorts = _RmdmLinePorts_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 3, 1, 9),
    _RmdmLinePorts_Type()
)
rmdmLinePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmdmLinePorts.setStatus("mandatory")
_RemVerInfoTable_Object = MibTable
remVerInfoTable = _RemVerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 4)
)
if mibBuilder.loadTexts:
    remVerInfoTable.setStatus("mandatory")
_RemVerInfoEntry_Object = MibTableRow
remVerInfoEntry = _RemVerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 4, 1)
)
remVerInfoEntry.setIndexNames(
    (0, "PANDATEL-MODEM-MIB", "rviRack"),
    (0, "PANDATEL-MODEM-MIB", "rviModem"),
)
if mibBuilder.loadTexts:
    remVerInfoEntry.setStatus("mandatory")
_RviRack_Type = Integer32
_RviRack_Object = MibTableColumn
rviRack = _RviRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 4, 1, 1),
    _RviRack_Type()
)
rviRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rviRack.setStatus("mandatory")
_RviModem_Type = Integer32
_RviModem_Object = MibTableColumn
rviModem = _RviModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 4, 1, 2),
    _RviModem_Type()
)
rviModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rviModem.setStatus("mandatory")


class _RviType_Type(Integer32):
    """Custom type rviType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              101,
              102,
              103,
              201,
              202,
              203,
              204,
              205,
              206,
              301,
              302,
              401,
              501,
              502,
              503,
              504,
              506,
              507,
              601,
              701,
              801,
              802,
              901)
        )
    )
    namedValues = NamedValues(
        *(("bm-p", 301),
          ("bm-z", 302),
          ("cmx-ie", 802),
          ("emx", 801),
          ("etc", 901),
          ("fhfl", 101),
          ("fhfl-f", 102),
          ("fhfl-s", 103),
          ("fme", 601),
          ("fobus", 501),
          ("fx", 502),
          ("fx-g", 506),
          ("fx-i", 503),
          ("fx-ig", 504),
          ("fx-ih", 507),
          ("gm-d", 203),
          ("gm-d-f", 206),
          ("gm-f", 202),
          ("gm-h", 201),
          ("gm-s", 204),
          ("gm-s-f", 205),
          ("gx", 401),
          ("inax", 701),
          ("not-present", 0),
          ("other", 1))
    )


_RviType_Type.__name__ = "Integer32"
_RviType_Object = MibTableColumn
rviType = _RviType_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 4, 1, 3),
    _RviType_Type()
)
rviType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rviType.setStatus("mandatory")
_RviFirmwVer_Type = DisplayString
_RviFirmwVer_Object = MibTableColumn
rviFirmwVer = _RviFirmwVer_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 4, 1, 4),
    _RviFirmwVer_Type()
)
rviFirmwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rviFirmwVer.setStatus("mandatory")
_RviUnitRel_Type = DisplayString
_RviUnitRel_Object = MibTableColumn
rviUnitRel = _RviUnitRel_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 4, 1, 5),
    _RviUnitRel_Type()
)
rviUnitRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rviUnitRel.setStatus("mandatory")
_RviArtNo_Type = DisplayString
_RviArtNo_Object = MibTableColumn
rviArtNo = _RviArtNo_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 4, 1, 6),
    _RviArtNo_Type()
)
rviArtNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rviArtNo.setStatus("mandatory")


class _RviFrontVer_Type(Integer32):
    """Custom type rviFrontVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("other", 1)
    )


_RviFrontVer_Type.__name__ = "Integer32"
_RviFrontVer_Object = MibTableColumn
rviFrontVer = _RviFrontVer_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 4, 1, 7),
    _RviFrontVer_Type()
)
rviFrontVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rviFrontVer.setStatus("mandatory")
_RviSerialNumber_Type = DisplayString
_RviSerialNumber_Object = MibTableColumn
rviSerialNumber = _RviSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 4, 1, 8),
    _RviSerialNumber_Type()
)
rviSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rviSerialNumber.setStatus("mandatory")
_RemPortTable_Object = MibTable
remPortTable = _RemPortTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 5)
)
if mibBuilder.loadTexts:
    remPortTable.setStatus("mandatory")
_RemPortEntry_Object = MibTableRow
remPortEntry = _RemPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 5, 1)
)
remPortEntry.setIndexNames(
    (0, "PANDATEL-MODEM-MIB", "rportRack"),
    (0, "PANDATEL-MODEM-MIB", "rportModem"),
    (0, "PANDATEL-MODEM-MIB", "rportPort"),
)
if mibBuilder.loadTexts:
    remPortEntry.setStatus("mandatory")
_RportRack_Type = Integer32
_RportRack_Object = MibTableColumn
rportRack = _RportRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 5, 1, 1),
    _RportRack_Type()
)
rportRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rportRack.setStatus("mandatory")
_RportModem_Type = Integer32
_RportModem_Object = MibTableColumn
rportModem = _RportModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 5, 1, 2),
    _RportModem_Type()
)
rportModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rportModem.setStatus("mandatory")
_RportPort_Type = Integer32
_RportPort_Object = MibTableColumn
rportPort = _RportPort_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 5, 1, 3),
    _RportPort_Type()
)
rportPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rportPort.setStatus("mandatory")


class _RportType_Type(Integer32):
    """Custom type rportType based on Integer32"""
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
        *(("backup-port", 6),
          ("interface-port", 2),
          ("line-port", 3),
          ("other", 1),
          ("outband-mgmt-port", 5),
          ("vt100-mgmt-port", 4))
    )


_RportType_Type.__name__ = "Integer32"
_RportType_Object = MibTableColumn
rportType = _RportType_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 5, 1, 4),
    _RportType_Type()
)
rportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rportType.setStatus("mandatory")


class _RportInterfaceType_Type(Integer32):
    """Custom type rportInterfaceType based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              34,
              39,
              40,
              48,
              55,
              56,
              66,
              67,
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
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              999)
        )
    )
    namedValues = NamedValues(
        *(("atm-26mb", 18),
          ("bm", 34),
          ("eth-bridge", 48),
          ("fo-e1t1", 13),
          ("g703-64k", 9),
          ("g703-e1", 55),
          ("g703-e1t1", 7),
          ("g703-e2", 56),
          ("g703-e2t2", 8),
          ("g703-e3", 19),
          ("g703-t1", 39),
          ("g703-t2", 40),
          ("g703-t3", 20),
          ("hdsl", 15),
          ("hssi", 22),
          ("i430", 10),
          ("intercom", 12),
          ("missing", 999),
          ("mm-1300-820nm", 184),
          ("mm-820-1300nm", 183),
          ("mm-fiber-1300nm", 134),
          ("mm-fiber-1550nm", 135),
          ("mm-fiber-820nm", 133),
          ("no-module", 17),
          ("other", 1),
          ("rs485", 6),
          ("s0", 14),
          ("sm-1300-1550nm", 181),
          ("sm-1550-1300nm", 182),
          ("sm-fiber-1300nm", 131),
          ("sm-fiber-1480nm", 185),
          ("sm-fiber-1510nm", 186),
          ("sm-fiber-1530-33nm", 136),
          ("sm-fiber-1531-12nm", 137),
          ("sm-fiber-1531-90nm", 138),
          ("sm-fiber-1532-68nm", 139),
          ("sm-fiber-1533-47nm", 140),
          ("sm-fiber-1534-25nm", 141),
          ("sm-fiber-1535-04nm", 142),
          ("sm-fiber-1535-82nm", 143),
          ("sm-fiber-1536-61nm", 144),
          ("sm-fiber-1537-40nm", 145),
          ("sm-fiber-1538-19nm", 146),
          ("sm-fiber-1538-98nm", 147),
          ("sm-fiber-1538nm", 187),
          ("sm-fiber-1539-77nm", 148),
          ("sm-fiber-1540-56nm", 149),
          ("sm-fiber-1541-35nm", 150),
          ("sm-fiber-1542-14nm", 151),
          ("sm-fiber-1542-94nm", 152),
          ("sm-fiber-1543-73nm", 153),
          ("sm-fiber-1544-53nm", 154),
          ("sm-fiber-1545-32nm", 155),
          ("sm-fiber-1546-12nm", 156),
          ("sm-fiber-1546-92nm", 157),
          ("sm-fiber-1547-72nm", 158),
          ("sm-fiber-1548-51nm", 159),
          ("sm-fiber-1549-32nm", 160),
          ("sm-fiber-1550-12nm", 161),
          ("sm-fiber-1550-92nm", 162),
          ("sm-fiber-1550nm", 132),
          ("sm-fiber-1551-72nm", 163),
          ("sm-fiber-1552-52nm", 164),
          ("sm-fiber-1553-33nm", 165),
          ("sm-fiber-1553nm", 188),
          ("sm-fiber-1554-13nm", 166),
          ("sm-fiber-1554-94nm", 167),
          ("sm-fiber-1555-75nm", 168),
          ("sm-fiber-1556-55nm", 169),
          ("sm-fiber-1557-36nm", 170),
          ("sm-fiber-1558-17nm", 171),
          ("sm-fiber-1558-98nm", 172),
          ("sm-fiber-1559-79nm", 173),
          ("sm-fiber-1560-61nm", 174),
          ("sm-fiber-1561-42nm", 175),
          ("sm-fiber-1562-23nm", 176),
          ("sm-fiber-1563-05nm", 177),
          ("sm-fiber-1563-86nm", 178),
          ("sm-fiber-1564-68nm", 179),
          ("sm-fiber-1565-50nm", 180),
          ("sm-fiber-820nm", 130),
          ("sm-mm-fiber-1310nm", 189),
          ("stm-1", 67),
          ("store-loop", 11),
          ("sts-1", 21),
          ("sts-3", 66),
          ("v24", 2),
          ("v35", 3),
          ("v36", 4),
          ("x21", 5))
    )


_RportInterfaceType_Type.__name__ = "Integer32"
_RportInterfaceType_Object = MibTableColumn
rportInterfaceType = _RportInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 5, 1, 5),
    _RportInterfaceType_Type()
)
rportInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rportInterfaceType.setStatus("mandatory")


class _RportConnector_Type(Integer32):
    """Custom type rportConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
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
              997,
              998,
              999)
        )
    )
    namedValues = NamedValues(
        *(("bnc", 4),
          ("db-15-f", 12),
          ("db-15-m", 13),
          ("db-25-f", 14),
          ("db-25-m", 15),
          ("db-37-f", 16),
          ("db-37-m", 17),
          ("db-9-f", 10),
          ("db-9-m", 11),
          ("dpc", 5),
          ("dual-fc", 28),
          ("dual-fc-apc", 33),
          ("dual-fiber", 3),
          ("dual-lc", 36),
          ("dual-lc-apc", 37),
          ("dual-sc", 27),
          ("dual-sc-45", 40),
          ("dual-sc-apc", 32),
          ("dual-st", 29),
          ("e2000", 23),
          ("escon", 22),
          ("ics", 8),
          ("mic", 9),
          ("mini-c", 20),
          ("minimicro", 21),
          ("mt-rj", 38),
          ("not-installed", 999),
          ("other", 1),
          ("rj45", 7),
          ("single-fc", 25),
          ("single-fc-apc", 31),
          ("single-fiber", 2),
          ("single-lc", 34),
          ("single-lc-apc", 35),
          ("single-sc", 24),
          ("single-sc-45", 39),
          ("single-sc-apc", 30),
          ("single-st", 26),
          ("unknown", 997),
          ("virtual", 998),
          ("winch-f", 18),
          ("winch-m", 19))
    )


_RportConnector_Type.__name__ = "Integer32"
_RportConnector_Object = MibTableColumn
rportConnector = _RportConnector_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 5, 1, 6),
    _RportConnector_Type()
)
rportConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rportConnector.setStatus("mandatory")


class _RportLoopMode_Type(Integer32):
    """Custom type rportLoopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("digital", 3),
          ("line", 4),
          ("off", 99),
          ("other", 1),
          ("remote", 2))
    )


_RportLoopMode_Type.__name__ = "Integer32"
_RportLoopMode_Object = MibTableColumn
rportLoopMode = _RportLoopMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 5, 1, 7),
    _RportLoopMode_Type()
)
rportLoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rportLoopMode.setStatus("mandatory")
_RemPortSignalTable_Object = MibTable
remPortSignalTable = _RemPortSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 6)
)
if mibBuilder.loadTexts:
    remPortSignalTable.setStatus("mandatory")
_RemPortSignalEntry_Object = MibTableRow
remPortSignalEntry = _RemPortSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 6, 1)
)
remPortSignalEntry.setIndexNames(
    (0, "PANDATEL-MODEM-MIB", "rpsignalRack"),
    (0, "PANDATEL-MODEM-MIB", "rpsignalModem"),
    (0, "PANDATEL-MODEM-MIB", "rpsignalPort"),
    (0, "PANDATEL-MODEM-MIB", "rpsignalType"),
)
if mibBuilder.loadTexts:
    remPortSignalEntry.setStatus("mandatory")
_RpsignalRack_Type = Integer32
_RpsignalRack_Object = MibTableColumn
rpsignalRack = _RpsignalRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 6, 1, 1),
    _RpsignalRack_Type()
)
rpsignalRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpsignalRack.setStatus("mandatory")
_RpsignalModem_Type = Integer32
_RpsignalModem_Object = MibTableColumn
rpsignalModem = _RpsignalModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 6, 1, 2),
    _RpsignalModem_Type()
)
rpsignalModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpsignalModem.setStatus("mandatory")
_RpsignalPort_Type = Integer32
_RpsignalPort_Object = MibTableColumn
rpsignalPort = _RpsignalPort_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 6, 1, 3),
    _RpsignalPort_Type()
)
rpsignalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpsignalPort.setStatus("mandatory")


class _RpsignalType_Type(Integer32):
    """Custom type rpsignalType based on Integer32"""
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
              20,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("ais", 10),
          ("bond", 12),
          ("c", 7),
          ("ca", 15),
          ("cr", 20),
          ("dcd", 4),
          ("dsr", 6),
          ("dtr", 5),
          ("eclk", 16),
          ("fsync", 9),
          ("i", 8),
          ("laser-status", 13),
          ("laser-temp", 18),
          ("laser-tx", 17),
          ("lay1", 11),
          ("link", 2),
          ("other", 1),
          ("rd", 26),
          ("rts", 3),
          ("ta", 14),
          ("td", 27))
    )


_RpsignalType_Type.__name__ = "Integer32"
_RpsignalType_Object = MibTableColumn
rpsignalType = _RpsignalType_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 6, 1, 4),
    _RpsignalType_Type()
)
rpsignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpsignalType.setStatus("mandatory")


class _RpsignalStatus_Type(Integer32):
    """Custom type rpsignalStatus based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("active", 10),
          ("down", 3),
          ("fail", 9),
          ("high", 14),
          ("low", 15),
          ("mark", 13),
          ("no", 7),
          ("off", 5),
          ("ok", 8),
          ("on", 4),
          ("other", 1),
          ("space", 12),
          ("sync", 16),
          ("traffic", 11),
          ("up", 2),
          ("yes", 6))
    )


_RpsignalStatus_Type.__name__ = "Integer32"
_RpsignalStatus_Object = MibTableColumn
rpsignalStatus = _RpsignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 9, 6, 1, 5),
    _RpsignalStatus_Type()
)
rpsignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpsignalStatus.setStatus("mandatory")
_MdmSpecifics_ObjectIdentity = ObjectIdentity
mdmSpecifics = _MdmSpecifics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10)
)
_Mdm_oid_ObjectIdentity = ObjectIdentity
mdm_oid = _Mdm_oid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000)
)
_Comp_id_ObjectIdentity = ObjectIdentity
comp_id = _Comp_id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 1)
)
_Rack_other_ObjectIdentity = ObjectIdentity
rack_other = _Rack_other_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 1, 1)
)
_Rack_10s_3hu_ObjectIdentity = ObjectIdentity
rack_10s_3hu = _Rack_10s_3hu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 1, 2)
)
_Rack_12s_3hu_ObjectIdentity = ObjectIdentity
rack_12s_3hu = _Rack_12s_3hu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 1, 3)
)
_Rack_10s_6hu_ObjectIdentity = ObjectIdentity
rack_10s_6hu = _Rack_10s_6hu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 1, 4)
)
_Rack_6s_9s_6hu_ObjectIdentity = ObjectIdentity
rack_6s_9s_6hu = _Rack_6s_9s_6hu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 1, 5)
)
_Device_stack_15s_ObjectIdentity = ObjectIdentity
device_stack_15s = _Device_stack_15s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 1, 6)
)
_Rack_8s_4hu_ObjectIdentity = ObjectIdentity
rack_8s_4hu = _Rack_8s_4hu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 1, 7)
)
_Rack_10s_2c_6hu_ObjectIdentity = ObjectIdentity
rack_10s_2c_6hu = _Rack_10s_2c_6hu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 1, 8)
)
_Hs_rack_10s_3hu_ObjectIdentity = ObjectIdentity
hs_rack_10s_3hu = _Hs_rack_10s_3hu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 1, 9)
)
_Rack_8s_2c_6hu_ObjectIdentity = ObjectIdentity
rack_8s_2c_6hu = _Rack_8s_2c_6hu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 1, 10)
)
_Hs_rack_3s_1c_3hu_ObjectIdentity = ObjectIdentity
hs_rack_3s_1c_3hu = _Hs_rack_3s_1c_3hu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 1, 11)
)
_Rack_1s_1c_1hu_ObjectIdentity = ObjectIdentity
rack_1s_1c_1hu = _Rack_1s_1c_1hu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 1, 12)
)
_Rack_3s_1c_1hu_ObjectIdentity = ObjectIdentity
rack_3s_1c_1hu = _Rack_3s_1c_1hu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 1, 13)
)
_Device_id_ObjectIdentity = ObjectIdentity
device_id = _Device_id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2)
)
_OtherModem_ObjectIdentity = ObjectIdentity
otherModem = _OtherModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 1)
)
_Cms_snmp_master_ObjectIdentity = ObjectIdentity
cms_snmp_master = _Cms_snmp_master_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 10001)
)
_Cms_slave_ObjectIdentity = ObjectIdentity
cms_slave = _Cms_slave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 10002)
)
_Cms_intelligent_slave_ObjectIdentity = ObjectIdentity
cms_intelligent_slave = _Cms_intelligent_slave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 10003)
)
_Rc_control_ObjectIdentity = ObjectIdentity
rc_control = _Rc_control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 10004)
)
_Slot_id_ObjectIdentity = ObjectIdentity
slot_id = _Slot_id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 3)
)
_ModemSlot_ObjectIdentity = ObjectIdentity
modemSlot = _ModemSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 3, 1)
)
_MgmtSlot_ObjectIdentity = ObjectIdentity
mgmtSlot = _MgmtSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 3, 2)
)
_ModemAddr_ObjectIdentity = ObjectIdentity
modemAddr = _ModemAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 3, 3)
)
_MgmtAddr_ObjectIdentity = ObjectIdentity
mgmtAddr = _MgmtAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 3, 4)
)
_WdmSlot_ObjectIdentity = ObjectIdentity
wdmSlot = _WdmSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 3, 5)
)
_ControlSlot_ObjectIdentity = ObjectIdentity
controlSlot = _ControlSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 3, 6)
)
_PsupplySlot_ObjectIdentity = ObjectIdentity
psupplySlot = _PsupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 3, 10)
)
_Port_id_ObjectIdentity = ObjectIdentity
port_id = _Port_id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 4)
)
_OtherPort_ObjectIdentity = ObjectIdentity
otherPort = _OtherPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 4, 1)
)
_InterfacePort_ObjectIdentity = ObjectIdentity
interfacePort = _InterfacePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 4, 2)
)
_LinePort_ObjectIdentity = ObjectIdentity
linePort = _LinePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 4, 3)
)
_Vt100mgmtPort_ObjectIdentity = ObjectIdentity
vt100mgmtPort = _Vt100mgmtPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 4, 4)
)
_OutbandmgmtPort_ObjectIdentity = ObjectIdentity
outbandmgmtPort = _OutbandmgmtPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 4, 5)
)
_BackupPort_ObjectIdentity = ObjectIdentity
backupPort = _BackupPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 4, 6)
)
_Rs485Port_ObjectIdentity = ObjectIdentity
rs485Port = _Rs485Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 4, 7)
)
_Psupply_id_ObjectIdentity = ObjectIdentity
psupply_id = _Psupply_id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 5)
)
_Ps_other_ObjectIdentity = ObjectIdentity
ps_other = _Ps_other_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 5, 1)
)
_P_ac_x_5v_20a_ObjectIdentity = ObjectIdentity
p_ac_x_5v_20a = _P_ac_x_5v_20a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 5, 2)
)
_P_ac_x_5v_30a_ObjectIdentity = ObjectIdentity
p_ac_x_5v_30a = _P_ac_x_5v_30a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 5, 3)
)
_P_dc_48v_5v_18a_ObjectIdentity = ObjectIdentity
p_dc_48v_5v_18a = _P_dc_48v_5v_18a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 5, 4)
)
_P_dc_24v_5v_15a_ObjectIdentity = ObjectIdentity
p_dc_24v_5v_15a = _P_dc_24v_5v_15a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 5, 5)
)
_P_dc_48v_5v_30a_ObjectIdentity = ObjectIdentity
p_dc_48v_5v_30a = _P_dc_48v_5v_30a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 5, 6)
)
_B_ac_x_5v_6a_ObjectIdentity = ObjectIdentity
b_ac_x_5v_6a = _B_ac_x_5v_6a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 5, 7)
)
_B_dc_48v_5v_lc_ObjectIdentity = ObjectIdentity
b_dc_48v_5v_lc = _B_dc_48v_5v_lc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 5, 8)
)
_B_dc_48v_5v_hc_ObjectIdentity = ObjectIdentity
b_dc_48v_5v_hc = _B_dc_48v_5v_hc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 5, 9)
)
_B_dc_24v_5v_su_ObjectIdentity = ObjectIdentity
b_dc_24v_5v_su = _B_dc_24v_5v_su_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 5, 10)
)
_P_ac_x_3v_20a_ObjectIdentity = ObjectIdentity
p_ac_x_3v_20a = _P_ac_x_3v_20a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 5, 11)
)
_P_dc_48v_5v_20a_ObjectIdentity = ObjectIdentity
p_dc_48v_5v_20a = _P_dc_48v_5v_20a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 5, 12)
)
_P_dc_5v_3v_4a_ObjectIdentity = ObjectIdentity
p_dc_5v_3v_4a = _P_dc_5v_3v_4a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 5, 13)
)
_P_dc_5v_5v_5a_ObjectIdentity = ObjectIdentity
p_dc_5v_5v_5a = _P_dc_5v_5v_5a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 5, 14)
)
_Psonoff_id_ObjectIdentity = ObjectIdentity
psonoff_id = _Psonoff_id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 6)
)
_PS1_PS2_other_ObjectIdentity = ObjectIdentity
pS1_PS2_other = _PS1_PS2_other_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 6, 1)
)
_PS1_on_PS2_off_ObjectIdentity = ObjectIdentity
pS1_on_PS2_off = _PS1_on_PS2_off_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 6, 2)
)
_PS1_on_PS2_on_ObjectIdentity = ObjectIdentity
pS1_on_PS2_on = _PS1_on_PS2_on_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 6, 3)
)
_Fanonoff_id_ObjectIdentity = ObjectIdentity
fanonoff_id = _Fanonoff_id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 7)
)
_FAN1_FAN2_other_ObjectIdentity = ObjectIdentity
fAN1_FAN2_other = _FAN1_FAN2_other_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 7, 1)
)
_FAN1_off_FAN2_off_ObjectIdentity = ObjectIdentity
fAN1_off_FAN2_off = _FAN1_off_FAN2_off_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 7, 2)
)
_FAN1_on_FAN2_off_ObjectIdentity = ObjectIdentity
fAN1_on_FAN2_off = _FAN1_on_FAN2_off_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 7, 3)
)
_FAN1_off_FAN2_on_ObjectIdentity = ObjectIdentity
fAN1_off_FAN2_on = _FAN1_off_FAN2_on_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 7, 4)
)
_FAN1_on_FAN2_on_ObjectIdentity = ObjectIdentity
fAN1_on_FAN2_on = _FAN1_on_FAN2_on_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 7, 5)
)
_MdmMgmtIfGroup_ObjectIdentity = ObjectIdentity
mdmMgmtIfGroup = _MdmMgmtIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 20)
)


class _MdmIfType_Type(Integer32):
    """Custom type mdmIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              999)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 6),
          ("missing", 999),
          ("other", 1),
          ("v24", 2),
          ("v35", 4),
          ("x21", 5))
    )


_MdmIfType_Type.__name__ = "Integer32"
_MdmIfType_Object = MibScalar
mdmIfType = _MdmIfType_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 20, 1),
    _MdmIfType_Type()
)
mdmIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIfType.setStatus("mandatory")


class _MdmIfProtocol_Type(Integer32):
    """Custom type mdmIfProtocol based on Integer32"""
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
        *(("ethernetII", 5),
          ("other", 1),
          ("ppp-async", 3),
          ("ppp-sync", 4),
          ("slip", 2))
    )


_MdmIfProtocol_Type.__name__ = "Integer32"
_MdmIfProtocol_Object = MibScalar
mdmIfProtocol = _MdmIfProtocol_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 20, 2),
    _MdmIfProtocol_Type()
)
mdmIfProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIfProtocol.setStatus("mandatory")
_MdmIfDataRate_Type = Integer32
_MdmIfDataRate_Object = MibScalar
mdmIfDataRate = _MdmIfDataRate_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 20, 3),
    _MdmIfDataRate_Type()
)
mdmIfDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIfDataRate.setStatus("mandatory")


class _MdmIfDialEnable_Type(Integer32):
    """Custom type mdmIfDialEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_MdmIfDialEnable_Type.__name__ = "Integer32"
_MdmIfDialEnable_Object = MibScalar
mdmIfDialEnable = _MdmIfDialEnable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 20, 4),
    _MdmIfDialEnable_Type()
)
mdmIfDialEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmIfDialEnable.setStatus("mandatory")
_MdmIfInitString_Type = DisplayString
_MdmIfInitString_Object = MibScalar
mdmIfInitString = _MdmIfInitString_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 20, 5),
    _MdmIfInitString_Type()
)
mdmIfInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmIfInitString.setStatus("mandatory")
_MdmIfDialString_Type = DisplayString
_MdmIfDialString_Object = MibScalar
mdmIfDialString = _MdmIfDialString_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 20, 6),
    _MdmIfDialString_Type()
)
mdmIfDialString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmIfDialString.setStatus("mandatory")
_MdmIfSendTTL_Type = Integer32
_MdmIfSendTTL_Object = MibScalar
mdmIfSendTTL = _MdmIfSendTTL_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 20, 7),
    _MdmIfSendTTL_Type()
)
mdmIfSendTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmIfSendTTL.setStatus("mandatory")
_MdmIfDialTimeout_Type = Integer32
_MdmIfDialTimeout_Object = MibScalar
mdmIfDialTimeout = _MdmIfDialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 20, 8),
    _MdmIfDialTimeout_Type()
)
mdmIfDialTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmIfDialTimeout.setStatus("mandatory")
_MdmIfRedialPause_Type = Integer32
_MdmIfRedialPause_Object = MibScalar
mdmIfRedialPause = _MdmIfRedialPause_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 20, 9),
    _MdmIfRedialPause_Type()
)
mdmIfRedialPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmIfRedialPause.setStatus("mandatory")
_MdmIfIdlePeriodBeforeDisconnect_Type = Integer32
_MdmIfIdlePeriodBeforeDisconnect_Object = MibScalar
mdmIfIdlePeriodBeforeDisconnect = _MdmIfIdlePeriodBeforeDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 20, 10),
    _MdmIfIdlePeriodBeforeDisconnect_Type()
)
mdmIfIdlePeriodBeforeDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmIfIdlePeriodBeforeDisconnect.setStatus("mandatory")

# Managed Objects groups


# Notification objects

rackAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 0, 1)
)
rackAdded.setObjects(
    ("PANDATEL-MODEM-MIB", "rackType")
)
if mibBuilder.loadTexts:
    rackAdded.setStatus(
        ""
    )

rackRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 0, 2)
)
rackRemoved.setObjects(
    ("PANDATEL-MODEM-MIB", "rackType")
)
if mibBuilder.loadTexts:
    rackRemoved.setStatus(
        ""
    )

modemAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 0, 3)
)
modemAdded.setObjects(
    ("PANDATEL-MODEM-MIB", "viType")
)
if mibBuilder.loadTexts:
    modemAdded.setStatus(
        ""
    )

modemRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 0, 4)
)
modemRemoved.setObjects(
    ("PANDATEL-MODEM-MIB", "viType")
)
if mibBuilder.loadTexts:
    modemRemoved.setStatus(
        ""
    )

portLoopEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 0, 5)
)
portLoopEnabled.setObjects(
    ("PANDATEL-MODEM-MIB", "portLoopMode")
)
if mibBuilder.loadTexts:
    portLoopEnabled.setStatus(
        ""
    )

portLoopDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 0, 6)
)
portLoopDisabled.setObjects(
    ("PANDATEL-MODEM-MIB", "portLoopMode")
)
if mibBuilder.loadTexts:
    portLoopDisabled.setStatus(
        ""
    )

portSignalStatusGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 0, 7)
)
portSignalStatusGood.setObjects(
    ("PANDATEL-MODEM-MIB", "psignalType")
)
if mibBuilder.loadTexts:
    portSignalStatusGood.setStatus(
        ""
    )

portSignalStatusBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 0, 8)
)
portSignalStatusBad.setObjects(
    ("PANDATEL-MODEM-MIB", "psignalType")
)
if mibBuilder.loadTexts:
    portSignalStatusBad.setStatus(
        ""
    )

portBackupEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 0, 9)
)
portBackupEnabled.setObjects(
      *(("PANDATEL-MODEM-MIB", "portPort"),
        ("PANDATEL-MODEM-MIB", "portPort"))
)
if mibBuilder.loadTexts:
    portBackupEnabled.setStatus(
        ""
    )

portBackupDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 0, 10)
)
portBackupDisabled.setObjects(
      *(("PANDATEL-MODEM-MIB", "portPort"),
        ("PANDATEL-MODEM-MIB", "portPort"))
)
if mibBuilder.loadTexts:
    portBackupDisabled.setStatus(
        ""
    )

portBackupAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 0, 11)
)
portBackupAvailable.setObjects(
    ("PANDATEL-MODEM-MIB", "portPort")
)
if mibBuilder.loadTexts:
    portBackupAvailable.setStatus(
        ""
    )

portBackupNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 0, 12)
)
portBackupNotAvailable.setObjects(
    ("PANDATEL-MODEM-MIB", "portPort")
)
if mibBuilder.loadTexts:
    portBackupNotAvailable.setStatus(
        ""
    )

portDataPortChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 0, 13)
)
portDataPortChanged.setObjects(
      *(("PANDATEL-MODEM-MIB", "portPort"),
        ("PANDATEL-MODEM-MIB", "portPort"))
)
if mibBuilder.loadTexts:
    portDataPortChanged.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANDATEL-MODEM-MIB",
    **{"pandatel": pandatel,
       "mibs": mibs,
       "products": products,
       "wan-products": wan_products,
       "mdm-mgmt": mdm_mgmt,
       "rackAdded": rackAdded,
       "rackRemoved": rackRemoved,
       "modemAdded": modemAdded,
       "modemRemoved": modemRemoved,
       "portLoopEnabled": portLoopEnabled,
       "portLoopDisabled": portLoopDisabled,
       "portSignalStatusGood": portSignalStatusGood,
       "portSignalStatusBad": portSignalStatusBad,
       "portBackupEnabled": portBackupEnabled,
       "portBackupDisabled": portBackupDisabled,
       "portBackupAvailable": portBackupAvailable,
       "portBackupNotAvailable": portBackupNotAvailable,
       "portDataPortChanged": portDataPortChanged,
       "mdmGroup": mdmGroup,
       "mdmInstalledRacks": mdmInstalledRacks,
       "mdmInstalledModems": mdmInstalledModems,
       "mdmLoopModeTraps": mdmLoopModeTraps,
       "mdmCurrentDate": mdmCurrentDate,
       "mdmCurrentTime": mdmCurrentTime,
       "mdmRackTable": mdmRackTable,
       "rackEntry": rackEntry,
       "rackRack": rackRack,
       "rackType": rackType,
       "rackDescription": rackDescription,
       "rackModemSlots": rackModemSlots,
       "rackModems": rackModems,
       "rackPowerSupplySlots": rackPowerSupplySlots,
       "rackPowerSupplies": rackPowerSupplies,
       "mdmModemTable": mdmModemTable,
       "modemEntry": modemEntry,
       "mdmRack": mdmRack,
       "mdmModem": mdmModem,
       "mdmDescription": mdmDescription,
       "mdmUserName": mdmUserName,
       "mdmSelfTest": mdmSelfTest,
       "mdmSelfTestResult": mdmSelfTestResult,
       "mdmRemoteAccessStatus": mdmRemoteAccessStatus,
       "mdmInterfacePorts": mdmInterfacePorts,
       "mdmLinePorts": mdmLinePorts,
       "mdmVerInfoTable": mdmVerInfoTable,
       "verInfoEntry": verInfoEntry,
       "viRack": viRack,
       "viModem": viModem,
       "viType": viType,
       "viFirmwVer": viFirmwVer,
       "viUnitRel": viUnitRel,
       "viArtNo": viArtNo,
       "viFrontVer": viFrontVer,
       "viSerialNumber": viSerialNumber,
       "mdmPortTable": mdmPortTable,
       "portEntry": portEntry,
       "portRack": portRack,
       "portModem": portModem,
       "portPort": portPort,
       "portType": portType,
       "portInterfaceType": portInterfaceType,
       "portConnector": portConnector,
       "portLoopMode": portLoopMode,
       "mdmPortSignalTable": mdmPortSignalTable,
       "portSignalEntry": portSignalEntry,
       "psignalRack": psignalRack,
       "psignalModem": psignalModem,
       "psignalPort": psignalPort,
       "psignalType": psignalType,
       "psignalStatus": psignalStatus,
       "psignalTrap": psignalTrap,
       "mdmBERTTable": mdmBERTTable,
       "bertEntry": bertEntry,
       "bertRack": bertRack,
       "bertModem": bertModem,
       "bertPort": bertPort,
       "bertBERTest": bertBERTest,
       "bertStatus": bertStatus,
       "bertRunTime": bertRunTime,
       "bertInErrorTime": bertInErrorTime,
       "bertErrorFreeTime": bertErrorFreeTime,
       "bertKbitsRecWrapped": bertKbitsRecWrapped,
       "bertKbitsReceived": bertKbitsReceived,
       "bertErrors": bertErrors,
       "bertSyncLosts": bertSyncLosts,
       "bertSyncStatus": bertSyncStatus,
       "bertBitErrorRate": bertBitErrorRate,
       "mdmRemoteAccess": mdmRemoteAccess,
       "remModemTable": remModemTable,
       "rmodemEntry": rmodemEntry,
       "rmdmRack": rmdmRack,
       "rmdmModem": rmdmModem,
       "rmdmDescription": rmdmDescription,
       "rmdmUserName": rmdmUserName,
       "rmdmSelfTest": rmdmSelfTest,
       "rmdmSelfTestResult": rmdmSelfTestResult,
       "rmdmRemoteAccessStatus": rmdmRemoteAccessStatus,
       "rmdmInterfacePorts": rmdmInterfacePorts,
       "rmdmLinePorts": rmdmLinePorts,
       "remVerInfoTable": remVerInfoTable,
       "remVerInfoEntry": remVerInfoEntry,
       "rviRack": rviRack,
       "rviModem": rviModem,
       "rviType": rviType,
       "rviFirmwVer": rviFirmwVer,
       "rviUnitRel": rviUnitRel,
       "rviArtNo": rviArtNo,
       "rviFrontVer": rviFrontVer,
       "rviSerialNumber": rviSerialNumber,
       "remPortTable": remPortTable,
       "remPortEntry": remPortEntry,
       "rportRack": rportRack,
       "rportModem": rportModem,
       "rportPort": rportPort,
       "rportType": rportType,
       "rportInterfaceType": rportInterfaceType,
       "rportConnector": rportConnector,
       "rportLoopMode": rportLoopMode,
       "remPortSignalTable": remPortSignalTable,
       "remPortSignalEntry": remPortSignalEntry,
       "rpsignalRack": rpsignalRack,
       "rpsignalModem": rpsignalModem,
       "rpsignalPort": rpsignalPort,
       "rpsignalType": rpsignalType,
       "rpsignalStatus": rpsignalStatus,
       "mdmSpecifics": mdmSpecifics,
       "mdm-oid": mdm_oid,
       "comp-id": comp_id,
       "rack-other": rack_other,
       "rack-10s-3hu": rack_10s_3hu,
       "rack-12s-3hu": rack_12s_3hu,
       "rack-10s-6hu": rack_10s_6hu,
       "rack-6s-9s-6hu": rack_6s_9s_6hu,
       "device-stack-15s": device_stack_15s,
       "rack-8s-4hu": rack_8s_4hu,
       "rack-10s-2c-6hu": rack_10s_2c_6hu,
       "hs-rack-10s-3hu": hs_rack_10s_3hu,
       "rack-8s-2c-6hu": rack_8s_2c_6hu,
       "hs-rack-3s-1c-3hu": hs_rack_3s_1c_3hu,
       "rack-1s-1c-1hu": rack_1s_1c_1hu,
       "rack-3s-1c-1hu": rack_3s_1c_1hu,
       "device-id": device_id,
       "otherModem": otherModem,
       "cms-snmp-master": cms_snmp_master,
       "cms-slave": cms_slave,
       "cms-intelligent-slave": cms_intelligent_slave,
       "rc-control": rc_control,
       "slot-id": slot_id,
       "modemSlot": modemSlot,
       "mgmtSlot": mgmtSlot,
       "modemAddr": modemAddr,
       "mgmtAddr": mgmtAddr,
       "wdmSlot": wdmSlot,
       "controlSlot": controlSlot,
       "psupplySlot": psupplySlot,
       "port-id": port_id,
       "otherPort": otherPort,
       "interfacePort": interfacePort,
       "linePort": linePort,
       "vt100mgmtPort": vt100mgmtPort,
       "outbandmgmtPort": outbandmgmtPort,
       "backupPort": backupPort,
       "rs485Port": rs485Port,
       "psupply-id": psupply_id,
       "ps-other": ps_other,
       "p-ac-x-5v-20a": p_ac_x_5v_20a,
       "p-ac-x-5v-30a": p_ac_x_5v_30a,
       "p-dc-48v-5v-18a": p_dc_48v_5v_18a,
       "p-dc-24v-5v-15a": p_dc_24v_5v_15a,
       "p-dc-48v-5v-30a": p_dc_48v_5v_30a,
       "b-ac-x-5v-6a": b_ac_x_5v_6a,
       "b-dc-48v-5v-lc": b_dc_48v_5v_lc,
       "b-dc-48v-5v-hc": b_dc_48v_5v_hc,
       "b-dc-24v-5v-su": b_dc_24v_5v_su,
       "p-ac-x-3v-20a": p_ac_x_3v_20a,
       "p-dc-48v-5v-20a": p_dc_48v_5v_20a,
       "p-dc-5v-3v-4a": p_dc_5v_3v_4a,
       "p-dc-5v-5v-5a": p_dc_5v_5v_5a,
       "psonoff-id": psonoff_id,
       "pS1-PS2-other": pS1_PS2_other,
       "pS1-on-PS2-off": pS1_on_PS2_off,
       "pS1-on-PS2-on": pS1_on_PS2_on,
       "fanonoff-id": fanonoff_id,
       "fAN1-FAN2-other": fAN1_FAN2_other,
       "fAN1-off-FAN2-off": fAN1_off_FAN2_off,
       "fAN1-on-FAN2-off": fAN1_on_FAN2_off,
       "fAN1-off-FAN2-on": fAN1_off_FAN2_on,
       "fAN1-on-FAN2-on": fAN1_on_FAN2_on,
       "mdmMgmtIfGroup": mdmMgmtIfGroup,
       "mdmIfType": mdmIfType,
       "mdmIfProtocol": mdmIfProtocol,
       "mdmIfDataRate": mdmIfDataRate,
       "mdmIfDialEnable": mdmIfDialEnable,
       "mdmIfInitString": mdmIfInitString,
       "mdmIfDialString": mdmIfDialString,
       "mdmIfSendTTL": mdmIfSendTTL,
       "mdmIfDialTimeout": mdmIfDialTimeout,
       "mdmIfRedialPause": mdmIfRedialPause,
       "mdmIfIdlePeriodBeforeDisconnect": mdmIfIdlePeriodBeforeDisconnect}
)
