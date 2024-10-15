# SNMP MIB module (INTELCORPORATIONICMBFEATURE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELCORPORATIONICMBFEATURE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:17 2024
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



class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiOctetstring(OctetString):
    """Custom type DmiOctetstring based on OctetString"""




class DmiDisplaystring(DisplayString):
    """Custom type DmiDisplaystring based on DisplayString"""




class DmiDateX(OctetString):
    """Custom type DmiDateX based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(28, 28),
    )





class DmiComponentIndex(Integer32):
    """Custom type DmiComponentIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Intel_ObjectIdentity = ObjectIdentity
intel = _Intel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2)
)
_Server_products_ObjectIdentity = ObjectIdentity
server_products = _Server_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6)
)
_Platforms_ObjectIdentity = ObjectIdentity
platforms = _Platforms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2)
)
_IcmbFeature_ObjectIdentity = ObjectIdentity
icmbFeature = _IcmbFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1)
)
_TComponentid_Object = MibTable
tComponentid = _TComponentid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid.setStatus("mandatory")
_EComponentid_Object = MibTableRow
eComponentid = _EComponentid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 1, 1)
)
eComponentid.setIndexNames(
    (0, "INTELCORPORATIONICMBFEATURE-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_A1Installation_Type = DmiDateX
_A1Installation_Object = MibTableColumn
a1Installation = _A1Installation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 1, 1, 5),
    _A1Installation_Type()
)
a1Installation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Installation.setStatus("mandatory")


class _A1Verify_Type(Integer32):
    """Custom type a1Verify based on Integer32"""
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
        *(("vAnErrorOccurredCheckStatusCode", 0),
          ("vReserved", 3),
          ("vThisComponentDoesNotExist", 1),
          ("vThisComponentExistsAndIsFunctioningCorr", 7),
          ("vThisComponentExistsAndIsNotFunctioningC", 6),
          ("vThisComponentExistsButTheFunctionality1", 5),
          ("vThisComponentExistsButTheFunctionalityI", 4),
          ("vVerificationIsNotSupported", 2))
    )


_A1Verify_Type.__name__ = "Integer32"
_A1Verify_Object = MibTableColumn
a1Verify = _A1Verify_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 1, 1, 6),
    _A1Verify_Type()
)
a1Verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Verify.setStatus("mandatory")
_TIcmbChassisTable_Object = MibTable
tIcmbChassisTable = _TIcmbChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 11)
)
if mibBuilder.loadTexts:
    tIcmbChassisTable.setStatus("mandatory")
_EIcmbChassisTable_Object = MibTableRow
eIcmbChassisTable = _EIcmbChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 11, 1)
)
eIcmbChassisTable.setIndexNames(
    (0, "INTELCORPORATIONICMBFEATURE-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONICMBFEATURE-MIB", "a11ChassisIndex"),
)
if mibBuilder.loadTexts:
    eIcmbChassisTable.setStatus("mandatory")
_A11ChassisIndex_Type = DmiInteger
_A11ChassisIndex_Object = MibTableColumn
a11ChassisIndex = _A11ChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 11, 1, 1),
    _A11ChassisIndex_Type()
)
a11ChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11ChassisIndex.setStatus("mandatory")
_A11ComponentId_Type = DmiInteger
_A11ComponentId_Object = MibTableColumn
a11ComponentId = _A11ComponentId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 11, 1, 2),
    _A11ComponentId_Type()
)
a11ComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11ComponentId.setStatus("mandatory")


class _A11ChassisAvailable_Type(Integer32):
    """Custom type a11ChassisAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vAvailable", 0),
          ("vInitializing", 3),
          ("vShuttingDown", 1),
          ("vUnavailable", 2))
    )


_A11ChassisAvailable_Type.__name__ = "Integer32"
_A11ChassisAvailable_Object = MibTableColumn
a11ChassisAvailable = _A11ChassisAvailable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 11, 1, 3),
    _A11ChassisAvailable_Type()
)
a11ChassisAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a11ChassisAvailable.setStatus("mandatory")
_TIcmbControl_Object = MibTable
tIcmbControl = _TIcmbControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 12)
)
if mibBuilder.loadTexts:
    tIcmbControl.setStatus("mandatory")
_EIcmbControl_Object = MibTableRow
eIcmbControl = _EIcmbControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 12, 1)
)
eIcmbControl.setIndexNames(
    (0, "INTELCORPORATIONICMBFEATURE-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eIcmbControl.setStatus("mandatory")


class _A12State_Type(Integer32):
    """Custom type a12State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A12State_Type.__name__ = "Integer32"
_A12State_Object = MibTableColumn
a12State = _A12State_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 12, 1, 1),
    _A12State_Type()
)
a12State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a12State.setStatus("mandatory")
_A12DiscoveryPeriod_Type = DmiInteger
_A12DiscoveryPeriod_Object = MibTableColumn
a12DiscoveryPeriod = _A12DiscoveryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 12, 1, 2),
    _A12DiscoveryPeriod_Type()
)
a12DiscoveryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a12DiscoveryPeriod.setStatus("mandatory")


class _A12SdrReadState_Type(Integer32):
    """Custom type a12SdrReadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A12SdrReadState_Type.__name__ = "Integer32"
_A12SdrReadState_Object = MibTableColumn
a12SdrReadState = _A12SdrReadState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 12, 1, 3),
    _A12SdrReadState_Type()
)
a12SdrReadState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a12SdrReadState.setStatus("mandatory")


class _A12AcceptIcmbCommands_Type(Integer32):
    """Custom type a12AcceptIcmbCommands based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A12AcceptIcmbCommands_Type.__name__ = "Integer32"
_A12AcceptIcmbCommands_Object = MibTableColumn
a12AcceptIcmbCommands = _A12AcceptIcmbCommands_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 12, 1, 4),
    _A12AcceptIcmbCommands_Type()
)
a12AcceptIcmbCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a12AcceptIcmbCommands.setStatus("mandatory")
_A12ReclaimResources_Type = DmiInteger
_A12ReclaimResources_Object = MibTableColumn
a12ReclaimResources = _A12ReclaimResources_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 12, 1, 5),
    _A12ReclaimResources_Type()
)
a12ReclaimResources.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a12ReclaimResources.setStatus("mandatory")
_TIcmbMifMappingTable_Object = MibTable
tIcmbMifMappingTable = _TIcmbMifMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 13)
)
if mibBuilder.loadTexts:
    tIcmbMifMappingTable.setStatus("mandatory")
_EIcmbMifMappingTable_Object = MibTableRow
eIcmbMifMappingTable = _EIcmbMifMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 13, 1)
)
eIcmbMifMappingTable.setIndexNames(
    (0, "INTELCORPORATIONICMBFEATURE-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONICMBFEATURE-MIB", "a13MapIndex"),
)
if mibBuilder.loadTexts:
    eIcmbMifMappingTable.setStatus("mandatory")
_A13MapIndex_Type = DmiInteger
_A13MapIndex_Object = MibTableColumn
a13MapIndex = _A13MapIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 13, 1, 1),
    _A13MapIndex_Type()
)
a13MapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a13MapIndex.setStatus("mandatory")
_A13Manufacturer_Type = DmiDisplaystring
_A13Manufacturer_Object = MibTableColumn
a13Manufacturer = _A13Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 13, 1, 2),
    _A13Manufacturer_Type()
)
a13Manufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a13Manufacturer.setStatus("mandatory")
_A13ProductName_Type = DmiDisplaystring
_A13ProductName_Object = MibTableColumn
a13ProductName = _A13ProductName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 13, 1, 3),
    _A13ProductName_Type()
)
a13ProductName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a13ProductName.setStatus("mandatory")
_A13ModelNumber_Type = DmiDisplaystring
_A13ModelNumber_Object = MibTableColumn
a13ModelNumber = _A13ModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 13, 1, 4),
    _A13ModelNumber_Type()
)
a13ModelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a13ModelNumber.setStatus("mandatory")
_A13MifFilename_Type = DmiDisplaystring
_A13MifFilename_Object = MibTableColumn
a13MifFilename = _A13MifFilename_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 13, 1, 5),
    _A13MifFilename_Type()
)
a13MifFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a13MifFilename.setStatus("mandatory")
_TMiftomib_Object = MibTable
tMiftomib = _TMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 1001)
)
if mibBuilder.loadTexts:
    tMiftomib.setStatus("mandatory")
_EMiftomib_Object = MibTableRow
eMiftomib = _EMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 1001, 1)
)
eMiftomib.setIndexNames(
    (0, "INTELCORPORATIONICMBFEATURE-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMiftomib.setStatus("mandatory")
_A1001MibName_Type = DmiDisplaystring
_A1001MibName_Object = MibTableColumn
a1001MibName = _A1001MibName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 1001, 1, 1),
    _A1001MibName_Type()
)
a1001MibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1001MibName.setStatus("mandatory")
_A1001MibOid_Type = DmiDisplaystring
_A1001MibOid_Object = MibTableColumn
a1001MibOid = _A1001MibOid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 1001, 1, 2),
    _A1001MibOid_Type()
)
a1001MibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1001MibOid.setStatus("mandatory")
_A1001DisableTrap_Type = DmiInteger
_A1001DisableTrap_Object = MibTableColumn
a1001DisableTrap = _A1001DisableTrap_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 1001, 1, 3),
    _A1001DisableTrap_Type()
)
a1001DisableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1001DisableTrap.setStatus("mandatory")
_TEifControl_Object = MibTable
tEifControl = _TEifControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2000)
)
if mibBuilder.loadTexts:
    tEifControl.setStatus("mandatory")
_EEifControl_Object = MibTableRow
eEifControl = _EEifControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2000, 1)
)
eEifControl.setIndexNames(
    (0, "INTELCORPORATIONICMBFEATURE-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eEifControl.setStatus("mandatory")


class _A2000Status_Type(Integer32):
    """Custom type a2000Status based on Integer32"""
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
        *(("vConstructedOnly", 4),
          ("vCreatedOnly", 3),
          ("vFullyOperational", 5),
          ("vIdle", 6),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A2000Status_Type.__name__ = "Integer32"
_A2000Status_Object = MibTableColumn
a2000Status = _A2000Status_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2000, 1, 1),
    _A2000Status_Type()
)
a2000Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2000Status.setStatus("mandatory")
_A2000DimContext_Type = DmiOctetstring
_A2000DimContext_Object = MibTableColumn
a2000DimContext = _A2000DimContext_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2000, 1, 2),
    _A2000DimContext_Type()
)
a2000DimContext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2000DimContext.setStatus("mandatory")
_A2000PersistentDataWriteDelay_Type = DmiInteger
_A2000PersistentDataWriteDelay_Object = MibTableColumn
a2000PersistentDataWriteDelay = _A2000PersistentDataWriteDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2000, 1, 3),
    _A2000PersistentDataWriteDelay_Type()
)
a2000PersistentDataWriteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2000PersistentDataWriteDelay.setStatus("mandatory")
_A2000EifInterfaceName_Type = DmiDisplaystring
_A2000EifInterfaceName_Object = MibTableColumn
a2000EifInterfaceName = _A2000EifInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2000, 1, 4),
    _A2000EifInterfaceName_Type()
)
a2000EifInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2000EifInterfaceName.setStatus("mandatory")
_TEifExtensionList_Object = MibTable
tEifExtensionList = _TEifExtensionList_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2001)
)
if mibBuilder.loadTexts:
    tEifExtensionList.setStatus("mandatory")
_EEifExtensionList_Object = MibTableRow
eEifExtensionList = _EEifExtensionList_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2001, 1)
)
eEifExtensionList.setIndexNames(
    (0, "INTELCORPORATIONICMBFEATURE-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONICMBFEATURE-MIB", "a2001Index"),
)
if mibBuilder.loadTexts:
    eEifExtensionList.setStatus("mandatory")
_A2001Index_Type = DmiInteger
_A2001Index_Object = MibTableColumn
a2001Index = _A2001Index_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2001, 1, 1),
    _A2001Index_Type()
)
a2001Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2001Index.setStatus("mandatory")
_A2001Filename_Type = DmiDisplaystring
_A2001Filename_Object = MibTableColumn
a2001Filename = _A2001Filename_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2001, 1, 2),
    _A2001Filename_Type()
)
a2001Filename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2001Filename.setStatus("mandatory")
_TEventGenerationForEifControl_Object = MibTable
tEventGenerationForEifControl = _TEventGenerationForEifControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2002)
)
if mibBuilder.loadTexts:
    tEventGenerationForEifControl.setStatus("mandatory")
_EEventGenerationForEifControl_Object = MibTableRow
eEventGenerationForEifControl = _EEventGenerationForEifControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2002, 1)
)
eEventGenerationForEifControl.setIndexNames(
    (0, "INTELCORPORATIONICMBFEATURE-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONICMBFEATURE-MIB", "a2002AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForEifControl.setStatus("mandatory")


class _A2002EventType_Type(Integer32):
    """Custom type a2002EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vNoDimContextsCreated", 1)
    )


_A2002EventType_Type.__name__ = "Integer32"
_A2002EventType_Object = MibTableColumn
a2002EventType = _A2002EventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2002, 1, 1),
    _A2002EventType_Type()
)
a2002EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2002EventType.setStatus("mandatory")


class _A2002EventSeverity_Type(Integer32):
    """Custom type a2002EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A2002EventSeverity_Type.__name__ = "Integer32"
_A2002EventSeverity_Object = MibTableColumn
a2002EventSeverity = _A2002EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2002, 1, 2),
    _A2002EventSeverity_Type()
)
a2002EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2002EventSeverity.setStatus("mandatory")


class _A2002IsEventState_based_Type(Integer32):
    """Custom type a2002IsEventState_based based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A2002IsEventState_based_Type.__name__ = "Integer32"
_A2002IsEventState_based_Object = MibScalar
a2002IsEventState_based = _A2002IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2002, 1, 3),
    _A2002IsEventState_based_Type()
)
a2002IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2002IsEventState_based.setStatus("mandatory")
_A2002EventStateKey_Type = DmiInteger
_A2002EventStateKey_Object = MibTableColumn
a2002EventStateKey = _A2002EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2002, 1, 4),
    _A2002EventStateKey_Type()
)
a2002EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2002EventStateKey.setStatus("mandatory")
_A2002AssociatedGroup_Type = DmiDisplaystring
_A2002AssociatedGroup_Object = MibTableColumn
a2002AssociatedGroup = _A2002AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2002, 1, 5),
    _A2002AssociatedGroup_Type()
)
a2002AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2002AssociatedGroup.setStatus("mandatory")


class _A2002EventSystem_Type(Integer32):
    """Custom type a2002EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther1", 0),
          ("vUnknown1", 1))
    )


_A2002EventSystem_Type.__name__ = "Integer32"
_A2002EventSystem_Object = MibTableColumn
a2002EventSystem = _A2002EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2002, 1, 6),
    _A2002EventSystem_Type()
)
a2002EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2002EventSystem.setStatus("mandatory")


class _A2002EventSubsystem_Type(Integer32):
    """Custom type a2002EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A2002EventSubsystem_Type.__name__ = "Integer32"
_A2002EventSubsystem_Object = MibTableColumn
a2002EventSubsystem = _A2002EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2002, 1, 7),
    _A2002EventSubsystem_Type()
)
a2002EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2002EventSubsystem.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trap1ForEifControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4, 1, 2002, 1, 0, 1)
)
trap1ForEifControl.setObjects(
      *(("INTELCORPORATIONICMBFEATURE-MIB", "a2002EventType"),
        ("INTELCORPORATIONICMBFEATURE-MIB", "a2002EventSeverity"),
        ("INTELCORPORATIONICMBFEATURE-MIB", "a2002IsEventState_based"),
        ("INTELCORPORATIONICMBFEATURE-MIB", "a2002EventStateKey"),
        ("INTELCORPORATIONICMBFEATURE-MIB", "a2002AssociatedGroup"),
        ("INTELCORPORATIONICMBFEATURE-MIB", "a2002EventSystem"),
        ("INTELCORPORATIONICMBFEATURE-MIB", "a2002EventSubsystem"))
)
if mibBuilder.loadTexts:
    trap1ForEifControl.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELCORPORATIONICMBFEATURE-MIB",
    **{"DmiInteger": DmiInteger,
       "DmiOctetstring": DmiOctetstring,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDateX": DmiDateX,
       "DmiComponentIndex": DmiComponentIndex,
       "intel": intel,
       "products": products,
       "server-products": server_products,
       "platforms": platforms,
       "icmbFeature": icmbFeature,
       "dmtfGroups": dmtfGroups,
       "tComponentid": tComponentid,
       "eComponentid": eComponentid,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "a1Installation": a1Installation,
       "a1Verify": a1Verify,
       "tIcmbChassisTable": tIcmbChassisTable,
       "eIcmbChassisTable": eIcmbChassisTable,
       "a11ChassisIndex": a11ChassisIndex,
       "a11ComponentId": a11ComponentId,
       "a11ChassisAvailable": a11ChassisAvailable,
       "tIcmbControl": tIcmbControl,
       "eIcmbControl": eIcmbControl,
       "a12State": a12State,
       "a12DiscoveryPeriod": a12DiscoveryPeriod,
       "a12SdrReadState": a12SdrReadState,
       "a12AcceptIcmbCommands": a12AcceptIcmbCommands,
       "a12ReclaimResources": a12ReclaimResources,
       "tIcmbMifMappingTable": tIcmbMifMappingTable,
       "eIcmbMifMappingTable": eIcmbMifMappingTable,
       "a13MapIndex": a13MapIndex,
       "a13Manufacturer": a13Manufacturer,
       "a13ProductName": a13ProductName,
       "a13ModelNumber": a13ModelNumber,
       "a13MifFilename": a13MifFilename,
       "tMiftomib": tMiftomib,
       "eMiftomib": eMiftomib,
       "a1001MibName": a1001MibName,
       "a1001MibOid": a1001MibOid,
       "a1001DisableTrap": a1001DisableTrap,
       "tEifControl": tEifControl,
       "eEifControl": eEifControl,
       "a2000Status": a2000Status,
       "a2000DimContext": a2000DimContext,
       "a2000PersistentDataWriteDelay": a2000PersistentDataWriteDelay,
       "a2000EifInterfaceName": a2000EifInterfaceName,
       "tEifExtensionList": tEifExtensionList,
       "eEifExtensionList": eEifExtensionList,
       "a2001Index": a2001Index,
       "a2001Filename": a2001Filename,
       "tEventGenerationForEifControl": tEventGenerationForEifControl,
       "eEventGenerationForEifControl": eEventGenerationForEifControl,
       "trap1ForEifControl": trap1ForEifControl,
       "a2002EventType": a2002EventType,
       "a2002EventSeverity": a2002EventSeverity,
       "a2002IsEventState-based": a2002IsEventState_based,
       "a2002EventStateKey": a2002EventStateKey,
       "a2002AssociatedGroup": a2002AssociatedGroup,
       "a2002EventSystem": a2002EventSystem,
       "a2002EventSubsystem": a2002EventSubsystem}
)
