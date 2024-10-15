# SNMP MIB module (ATMEDIA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATMEDIA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:09 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Atmedia_ObjectIdentity = ObjectIdentity
atmedia = _Atmedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458)
)
_Atmcrypt_ObjectIdentity = ObjectIdentity
atmcrypt = _Atmcrypt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1)
)
_AcMachine_ObjectIdentity = ObjectIdentity
acMachine = _AcMachine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 1)
)
_AcProductID_Type = DisplayString
_AcProductID_Object = MibScalar
acProductID = _AcProductID_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 1, 1),
    _AcProductID_Type()
)
acProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acProductID.setStatus("current")
_AcSerialNumber_Type = DisplayString
_AcSerialNumber_Object = MibScalar
acSerialNumber = _AcSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 1, 2),
    _AcSerialNumber_Type()
)
acSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSerialNumber.setStatus("current")
_AcHostname_Type = DisplayString
_AcHostname_Object = MibScalar
acHostname = _AcHostname_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 1, 3),
    _AcHostname_Type()
)
acHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acHostname.setStatus("current")
_AcContact_Type = DisplayString
_AcContact_Object = MibScalar
acContact = _AcContact_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 1, 4),
    _AcContact_Type()
)
acContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acContact.setStatus("current")
_AcLocation_Type = DisplayString
_AcLocation_Object = MibScalar
acLocation = _AcLocation_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 1, 5),
    _AcLocation_Type()
)
acLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLocation.setStatus("current")
_AcDescr_Type = DisplayString
_AcDescr_Object = MibScalar
acDescr = _AcDescr_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 1, 6),
    _AcDescr_Type()
)
acDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDescr.setStatus("current")
_AcSoftware_ObjectIdentity = ObjectIdentity
acSoftware = _AcSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 2)
)
_AcSoftVersion_Type = DisplayString
_AcSoftVersion_Object = MibScalar
acSoftVersion = _AcSoftVersion_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 2, 1),
    _AcSoftVersion_Type()
)
acSoftVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSoftVersion.setStatus("current")
_AcSoftDescr_Type = DisplayString
_AcSoftDescr_Object = MibScalar
acSoftDescr = _AcSoftDescr_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 2, 2),
    _AcSoftDescr_Type()
)
acSoftDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSoftDescr.setStatus("current")
_AcHardware_ObjectIdentity = ObjectIdentity
acHardware = _AcHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3)
)
_AcHardVersion_Type = DisplayString
_AcHardVersion_Object = MibScalar
acHardVersion = _AcHardVersion_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 1),
    _AcHardVersion_Type()
)
acHardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acHardVersion.setStatus("current")
_AcHardDescr_Type = DisplayString
_AcHardDescr_Object = MibScalar
acHardDescr = _AcHardDescr_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 2),
    _AcHardDescr_Type()
)
acHardDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acHardDescr.setStatus("current")
_AcInterfaces_ObjectIdentity = ObjectIdentity
acInterfaces = _AcInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 3)
)
_AcIfNumber_Type = Integer32
_AcIfNumber_Object = MibScalar
acIfNumber = _AcIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 3, 1),
    _AcIfNumber_Type()
)
acIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acIfNumber.setStatus("current")
_AcIfTable_Object = MibTable
acIfTable = _AcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    acIfTable.setStatus("current")
_AcIfEntry_Object = MibTableRow
acIfEntry = _AcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 3, 2, 1)
)
acIfEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acIfIndex"),
)
if mibBuilder.loadTexts:
    acIfEntry.setStatus("current")
_AcIfIndex_Type = Integer32
_AcIfIndex_Object = MibTableColumn
acIfIndex = _AcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 3, 2, 1, 1),
    _AcIfIndex_Type()
)
acIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acIfIndex.setStatus("current")
_AcIfDescr_Type = DisplayString
_AcIfDescr_Object = MibTableColumn
acIfDescr = _AcIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 3, 2, 1, 2),
    _AcIfDescr_Type()
)
acIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acIfDescr.setStatus("current")


class _AcIfPhyType_Type(Integer32):
    """Custom type acIfPhyType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ds1", 5),
          ("ds3", 3),
          ("e1", 4),
          ("e3", 2),
          ("ethernet", 9),
          ("fibrechannel", 8),
          ("gigabit", 6),
          ("other", 0),
          ("sonet", 1),
          ("sonetlink", 7))
    )


_AcIfPhyType_Type.__name__ = "Integer32"
_AcIfPhyType_Object = MibTableColumn
acIfPhyType = _AcIfPhyType_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 3, 2, 1, 3),
    _AcIfPhyType_Type()
)
acIfPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acIfPhyType.setStatus("current")
_AcIfSpeed_Type = Gauge32
_AcIfSpeed_Object = MibTableColumn
acIfSpeed = _AcIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 3, 2, 1, 4),
    _AcIfSpeed_Type()
)
acIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acIfSpeed.setStatus("current")
_AcIfRevision_Type = DisplayString
_AcIfRevision_Object = MibTableColumn
acIfRevision = _AcIfRevision_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 3, 2, 1, 5),
    _AcIfRevision_Type()
)
acIfRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acIfRevision.setStatus("current")
_AcEncryptors_ObjectIdentity = ObjectIdentity
acEncryptors = _AcEncryptors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 4)
)
_AcEcNumber_Type = Integer32
_AcEcNumber_Object = MibScalar
acEcNumber = _AcEcNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 4, 1),
    _AcEcNumber_Type()
)
acEcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEcNumber.setStatus("current")
_AcEcTable_Object = MibTable
acEcTable = _AcEcTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    acEcTable.setStatus("current")
_AcEcEntry_Object = MibTableRow
acEcEntry = _AcEcEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 4, 2, 1)
)
acEcEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acEcIndex"),
)
if mibBuilder.loadTexts:
    acEcEntry.setStatus("current")
_AcEcIndex_Type = Integer32
_AcEcIndex_Object = MibTableColumn
acEcIndex = _AcEcIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 4, 2, 1, 1),
    _AcEcIndex_Type()
)
acEcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEcIndex.setStatus("current")
_AcEcDescr_Type = DisplayString
_AcEcDescr_Object = MibTableColumn
acEcDescr = _AcEcDescr_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 4, 2, 1, 2),
    _AcEcDescr_Type()
)
acEcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEcDescr.setStatus("current")
_AcEcRevision_Type = DisplayString
_AcEcRevision_Object = MibTableColumn
acEcRevision = _AcEcRevision_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 3, 4, 2, 1, 3),
    _AcEcRevision_Type()
)
acEcRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEcRevision.setStatus("current")
_AcStatus_ObjectIdentity = ObjectIdentity
acStatus = _AcStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4)
)
_AcInterfaceStatus_ObjectIdentity = ObjectIdentity
acInterfaceStatus = _AcInterfaceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 1)
)
_AcInterfaceStatusNumber_Type = Integer32
_AcInterfaceStatusNumber_Object = MibScalar
acInterfaceStatusNumber = _AcInterfaceStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 1, 1),
    _AcInterfaceStatusNumber_Type()
)
acInterfaceStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acInterfaceStatusNumber.setStatus("current")
_AcInterfaceStatusTable_Object = MibTable
acInterfaceStatusTable = _AcInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    acInterfaceStatusTable.setStatus("current")
_AcInterfaceStatusEntry_Object = MibTableRow
acInterfaceStatusEntry = _AcInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 1, 2, 1)
)
acInterfaceStatusEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acInterfaceStatusIndex"),
)
if mibBuilder.loadTexts:
    acInterfaceStatusEntry.setStatus("current")
_AcInterfaceStatusIndex_Type = Integer32
_AcInterfaceStatusIndex_Object = MibTableColumn
acInterfaceStatusIndex = _AcInterfaceStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 1, 2, 1, 1),
    _AcInterfaceStatusIndex_Type()
)
acInterfaceStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acInterfaceStatusIndex.setStatus("current")


class _AcInterfaceStatusState_Type(Integer32):
    """Custom type acInterfaceStatusState based on Integer32"""
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


_AcInterfaceStatusState_Type.__name__ = "Integer32"
_AcInterfaceStatusState_Object = MibTableColumn
acInterfaceStatusState = _AcInterfaceStatusState_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 1, 2, 1, 2),
    _AcInterfaceStatusState_Type()
)
acInterfaceStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acInterfaceStatusState.setStatus("current")
_AcInterfaceStatusLastChange_Type = TimeTicks
_AcInterfaceStatusLastChange_Object = MibTableColumn
acInterfaceStatusLastChange = _AcInterfaceStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 1, 2, 1, 3),
    _AcInterfaceStatusLastChange_Type()
)
acInterfaceStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acInterfaceStatusLastChange.setStatus("current")
_AcInterfaceStatusDescr_Type = DisplayString
_AcInterfaceStatusDescr_Object = MibTableColumn
acInterfaceStatusDescr = _AcInterfaceStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 1, 2, 1, 4),
    _AcInterfaceStatusDescr_Type()
)
acInterfaceStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acInterfaceStatusDescr.setStatus("current")
_AcInterfaceStatusRxCells_Type = Counter64
_AcInterfaceStatusRxCells_Object = MibTableColumn
acInterfaceStatusRxCells = _AcInterfaceStatusRxCells_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 1, 2, 1, 5),
    _AcInterfaceStatusRxCells_Type()
)
acInterfaceStatusRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acInterfaceStatusRxCells.setStatus("current")
_AcInterfaceStatusTxCells_Type = Counter64
_AcInterfaceStatusTxCells_Object = MibTableColumn
acInterfaceStatusTxCells = _AcInterfaceStatusTxCells_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 1, 2, 1, 6),
    _AcInterfaceStatusTxCells_Type()
)
acInterfaceStatusTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acInterfaceStatusTxCells.setStatus("current")
_AcInterfaceStatusRxBytes_Type = Counter64
_AcInterfaceStatusRxBytes_Object = MibTableColumn
acInterfaceStatusRxBytes = _AcInterfaceStatusRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 1, 2, 1, 7),
    _AcInterfaceStatusRxBytes_Type()
)
acInterfaceStatusRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acInterfaceStatusRxBytes.setStatus("current")
_AcInterfaceStatusTxBytes_Type = Counter64
_AcInterfaceStatusTxBytes_Object = MibTableColumn
acInterfaceStatusTxBytes = _AcInterfaceStatusTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 1, 2, 1, 8),
    _AcInterfaceStatusTxBytes_Type()
)
acInterfaceStatusTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acInterfaceStatusTxBytes.setStatus("current")
_AcInterfaceStatusRxRate_Type = Gauge32
_AcInterfaceStatusRxRate_Object = MibTableColumn
acInterfaceStatusRxRate = _AcInterfaceStatusRxRate_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 1, 2, 1, 9),
    _AcInterfaceStatusRxRate_Type()
)
acInterfaceStatusRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acInterfaceStatusRxRate.setStatus("current")
_AcInterfaceStatusTxRate_Type = Gauge32
_AcInterfaceStatusTxRate_Object = MibTableColumn
acInterfaceStatusTxRate = _AcInterfaceStatusTxRate_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 1, 2, 1, 10),
    _AcInterfaceStatusTxRate_Type()
)
acInterfaceStatusTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acInterfaceStatusTxRate.setStatus("current")
_AcEncryptorStatus_ObjectIdentity = ObjectIdentity
acEncryptorStatus = _AcEncryptorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 2)
)
_AcEncryptorStatusNumber_Type = Integer32
_AcEncryptorStatusNumber_Object = MibScalar
acEncryptorStatusNumber = _AcEncryptorStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 2, 1),
    _AcEncryptorStatusNumber_Type()
)
acEncryptorStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEncryptorStatusNumber.setStatus("current")
_AcEncryptorStatusTable_Object = MibTable
acEncryptorStatusTable = _AcEncryptorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    acEncryptorStatusTable.setStatus("current")
_AcEncryptorStatusEntry_Object = MibTableRow
acEncryptorStatusEntry = _AcEncryptorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 2, 2, 1)
)
acEncryptorStatusEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acEncryptorStatusIndex"),
)
if mibBuilder.loadTexts:
    acEncryptorStatusEntry.setStatus("current")
_AcEncryptorStatusIndex_Type = Integer32
_AcEncryptorStatusIndex_Object = MibTableColumn
acEncryptorStatusIndex = _AcEncryptorStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 2, 2, 1, 1),
    _AcEncryptorStatusIndex_Type()
)
acEncryptorStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEncryptorStatusIndex.setStatus("current")


class _AcEncryptorStatusState_Type(Integer32):
    """Custom type acEncryptorStatusState based on Integer32"""
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
          ("plain", 3),
          ("up", 1))
    )


_AcEncryptorStatusState_Type.__name__ = "Integer32"
_AcEncryptorStatusState_Object = MibTableColumn
acEncryptorStatusState = _AcEncryptorStatusState_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 2, 2, 1, 2),
    _AcEncryptorStatusState_Type()
)
acEncryptorStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEncryptorStatusState.setStatus("current")
_AcEncryptorStatusLastChange_Type = TimeTicks
_AcEncryptorStatusLastChange_Object = MibTableColumn
acEncryptorStatusLastChange = _AcEncryptorStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 2, 2, 1, 3),
    _AcEncryptorStatusLastChange_Type()
)
acEncryptorStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEncryptorStatusLastChange.setStatus("current")
_AcEncryptorStatusDescr_Type = DisplayString
_AcEncryptorStatusDescr_Object = MibTableColumn
acEncryptorStatusDescr = _AcEncryptorStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 4, 2, 2, 1, 4),
    _AcEncryptorStatusDescr_Type()
)
acEncryptorStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEncryptorStatusDescr.setStatus("current")
_AcMaintenance_ObjectIdentity = ObjectIdentity
acMaintenance = _AcMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 5)
)
_AcMaUptime_Type = TimeTicks
_AcMaUptime_Object = MibScalar
acMaUptime = _AcMaUptime_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 5, 1),
    _AcMaUptime_Type()
)
acMaUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acMaUptime.setStatus("current")
_AcMaLastBoot_Type = TimeTicks
_AcMaLastBoot_Object = MibScalar
acMaLastBoot = _AcMaLastBoot_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 5, 2),
    _AcMaLastBoot_Type()
)
acMaLastBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acMaLastBoot.setStatus("current")
_AcMaSystime_Type = DateAndTime
_AcMaSystime_Object = MibScalar
acMaSystime = _AcMaSystime_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 5, 3),
    _AcMaSystime_Type()
)
acMaSystime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acMaSystime.setStatus("current")
_AcMaTemperature_Type = Gauge32
_AcMaTemperature_Object = MibScalar
acMaTemperature = _AcMaTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 5, 4),
    _AcMaTemperature_Type()
)
acMaTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acMaTemperature.setStatus("current")
_AcMaCpuTemperature1_Type = Gauge32
_AcMaCpuTemperature1_Object = MibScalar
acMaCpuTemperature1 = _AcMaCpuTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 5, 5),
    _AcMaCpuTemperature1_Type()
)
acMaCpuTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acMaCpuTemperature1.setStatus("current")
_AcMaCpuTemperature2_Type = Gauge32
_AcMaCpuTemperature2_Object = MibScalar
acMaCpuTemperature2 = _AcMaCpuTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 5, 6),
    _AcMaCpuTemperature2_Type()
)
acMaCpuTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acMaCpuTemperature2.setStatus("current")
_AcMaFanSpeed1_Type = Gauge32
_AcMaFanSpeed1_Object = MibScalar
acMaFanSpeed1 = _AcMaFanSpeed1_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 5, 7),
    _AcMaFanSpeed1_Type()
)
acMaFanSpeed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acMaFanSpeed1.setStatus("current")
_AcMaFanSpeed2_Type = Gauge32
_AcMaFanSpeed2_Object = MibScalar
acMaFanSpeed2 = _AcMaFanSpeed2_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 5, 8),
    _AcMaFanSpeed2_Type()
)
acMaFanSpeed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acMaFanSpeed2.setStatus("current")
_AcMaFanSpeed3_Type = Gauge32
_AcMaFanSpeed3_Object = MibScalar
acMaFanSpeed3 = _AcMaFanSpeed3_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 5, 9),
    _AcMaFanSpeed3_Type()
)
acMaFanSpeed3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acMaFanSpeed3.setStatus("current")
_AcMaFanSpeed4_Type = Gauge32
_AcMaFanSpeed4_Object = MibScalar
acMaFanSpeed4 = _AcMaFanSpeed4_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 5, 10),
    _AcMaFanSpeed4_Type()
)
acMaFanSpeed4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acMaFanSpeed4.setStatus("current")


class _AcMaPowerState_Type(Integer32):
    """Custom type acMaPowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 0),
          ("up", 1))
    )


_AcMaPowerState_Type.__name__ = "Integer32"
_AcMaPowerState_Object = MibScalar
acMaPowerState = _AcMaPowerState_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 5, 11),
    _AcMaPowerState_Type()
)
acMaPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acMaPowerState.setStatus("current")
_AcMaPowerLastChange_Type = TimeTicks
_AcMaPowerLastChange_Object = MibScalar
acMaPowerLastChange = _AcMaPowerLastChange_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 5, 12),
    _AcMaPowerLastChange_Type()
)
acMaPowerLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acMaPowerLastChange.setStatus("current")
_AcTransmission_ObjectIdentity = ObjectIdentity
acTransmission = _AcTransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6)
)
_AcSonet_ObjectIdentity = ObjectIdentity
acSonet = _AcSonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1)
)
_AcSonetStatus_ObjectIdentity = ObjectIdentity
acSonetStatus = _AcSonetStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 1)
)
_AcSonetStatusNumber_Type = Integer32
_AcSonetStatusNumber_Object = MibScalar
acSonetStatusNumber = _AcSonetStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 1, 1),
    _AcSonetStatusNumber_Type()
)
acSonetStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetStatusNumber.setStatus("current")
_AcSonetStatusTable_Object = MibTable
acSonetStatusTable = _AcSonetStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    acSonetStatusTable.setStatus("current")
_AcSonetStatusEntry_Object = MibTableRow
acSonetStatusEntry = _AcSonetStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 1, 2, 1)
)
acSonetStatusEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acSonetStatusIndex"),
)
if mibBuilder.loadTexts:
    acSonetStatusEntry.setStatus("current")
_AcSonetStatusIndex_Type = Integer32
_AcSonetStatusIndex_Object = MibTableColumn
acSonetStatusIndex = _AcSonetStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 1, 2, 1, 1),
    _AcSonetStatusIndex_Type()
)
acSonetStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetStatusIndex.setStatus("current")


class _AcSonetStatusState_Type(Integer32):
    """Custom type acSonetStatusState based on Integer32"""
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
          ("failure", 3),
          ("up", 1))
    )


_AcSonetStatusState_Type.__name__ = "Integer32"
_AcSonetStatusState_Object = MibTableColumn
acSonetStatusState = _AcSonetStatusState_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 1, 2, 1, 2),
    _AcSonetStatusState_Type()
)
acSonetStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetStatusState.setStatus("current")


class _AcSonetStatusLOS_Type(Integer32):
    """Custom type acSonetStatusLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcSonetStatusLOS_Type.__name__ = "Integer32"
_AcSonetStatusLOS_Object = MibTableColumn
acSonetStatusLOS = _AcSonetStatusLOS_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 1, 2, 1, 3),
    _AcSonetStatusLOS_Type()
)
acSonetStatusLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetStatusLOS.setStatus("current")


class _AcSonetStatusOOF_Type(Integer32):
    """Custom type acSonetStatusOOF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcSonetStatusOOF_Type.__name__ = "Integer32"
_AcSonetStatusOOF_Object = MibTableColumn
acSonetStatusOOF = _AcSonetStatusOOF_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 1, 2, 1, 4),
    _AcSonetStatusOOF_Type()
)
acSonetStatusOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetStatusOOF.setStatus("current")


class _AcSonetStatusLOC_Type(Integer32):
    """Custom type acSonetStatusLOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcSonetStatusLOC_Type.__name__ = "Integer32"
_AcSonetStatusLOC_Object = MibTableColumn
acSonetStatusLOC = _AcSonetStatusLOC_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 1, 2, 1, 5),
    _AcSonetStatusLOC_Type()
)
acSonetStatusLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetStatusLOC.setStatus("current")


class _AcSonetStatusLineAIS_Type(Integer32):
    """Custom type acSonetStatusLineAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcSonetStatusLineAIS_Type.__name__ = "Integer32"
_AcSonetStatusLineAIS_Object = MibTableColumn
acSonetStatusLineAIS = _AcSonetStatusLineAIS_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 1, 2, 1, 6),
    _AcSonetStatusLineAIS_Type()
)
acSonetStatusLineAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetStatusLineAIS.setStatus("current")


class _AcSonetStatusLineRDI_Type(Integer32):
    """Custom type acSonetStatusLineRDI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcSonetStatusLineRDI_Type.__name__ = "Integer32"
_AcSonetStatusLineRDI_Object = MibTableColumn
acSonetStatusLineRDI = _AcSonetStatusLineRDI_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 1, 2, 1, 7),
    _AcSonetStatusLineRDI_Type()
)
acSonetStatusLineRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetStatusLineRDI.setStatus("current")


class _AcSonetStatusPathAIS_Type(Integer32):
    """Custom type acSonetStatusPathAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcSonetStatusPathAIS_Type.__name__ = "Integer32"
_AcSonetStatusPathAIS_Object = MibTableColumn
acSonetStatusPathAIS = _AcSonetStatusPathAIS_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 1, 2, 1, 8),
    _AcSonetStatusPathAIS_Type()
)
acSonetStatusPathAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetStatusPathAIS.setStatus("current")


class _AcSonetStatusPathYellow_Type(Integer32):
    """Custom type acSonetStatusPathYellow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcSonetStatusPathYellow_Type.__name__ = "Integer32"
_AcSonetStatusPathYellow_Object = MibTableColumn
acSonetStatusPathYellow = _AcSonetStatusPathYellow_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 1, 2, 1, 9),
    _AcSonetStatusPathYellow_Type()
)
acSonetStatusPathYellow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetStatusPathYellow.setStatus("current")
_AcSonetStatusCustom_Type = Integer32
_AcSonetStatusCustom_Object = MibTableColumn
acSonetStatusCustom = _AcSonetStatusCustom_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 1, 2, 1, 10),
    _AcSonetStatusCustom_Type()
)
acSonetStatusCustom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetStatusCustom.setStatus("current")
_AcSonetStatusDescr_Type = DisplayString
_AcSonetStatusDescr_Object = MibTableColumn
acSonetStatusDescr = _AcSonetStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 1, 2, 1, 11),
    _AcSonetStatusDescr_Type()
)
acSonetStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetStatusDescr.setStatus("current")
_AcSonetAlarms_ObjectIdentity = ObjectIdentity
acSonetAlarms = _AcSonetAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 2)
)
_AcSonetAlarmsNumber_Type = Integer32
_AcSonetAlarmsNumber_Object = MibScalar
acSonetAlarmsNumber = _AcSonetAlarmsNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 2, 1),
    _AcSonetAlarmsNumber_Type()
)
acSonetAlarmsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetAlarmsNumber.setStatus("current")
_AcSonetAlarmsTable_Object = MibTable
acSonetAlarmsTable = _AcSonetAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    acSonetAlarmsTable.setStatus("current")
_AcSonetAlarmsEntry_Object = MibTableRow
acSonetAlarmsEntry = _AcSonetAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 2, 2, 1)
)
acSonetAlarmsEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acSonetAlarmsIndex"),
)
if mibBuilder.loadTexts:
    acSonetAlarmsEntry.setStatus("current")
_AcSonetAlarmsIndex_Type = Integer32
_AcSonetAlarmsIndex_Object = MibTableColumn
acSonetAlarmsIndex = _AcSonetAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 2, 2, 1, 1),
    _AcSonetAlarmsIndex_Type()
)
acSonetAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetAlarmsIndex.setStatus("current")
_AcSonetAlarmsLOS_Type = Counter64
_AcSonetAlarmsLOS_Object = MibTableColumn
acSonetAlarmsLOS = _AcSonetAlarmsLOS_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 2, 2, 1, 2),
    _AcSonetAlarmsLOS_Type()
)
acSonetAlarmsLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetAlarmsLOS.setStatus("current")
_AcSonetAlarmsLineAIS_Type = Counter64
_AcSonetAlarmsLineAIS_Object = MibTableColumn
acSonetAlarmsLineAIS = _AcSonetAlarmsLineAIS_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 2, 2, 1, 3),
    _AcSonetAlarmsLineAIS_Type()
)
acSonetAlarmsLineAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetAlarmsLineAIS.setStatus("current")
_AcSonetAlarmsLineRDI_Type = Counter64
_AcSonetAlarmsLineRDI_Object = MibTableColumn
acSonetAlarmsLineRDI = _AcSonetAlarmsLineRDI_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 2, 2, 1, 4),
    _AcSonetAlarmsLineRDI_Type()
)
acSonetAlarmsLineRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetAlarmsLineRDI.setStatus("current")
_AcSonetAlarmsPathAIS_Type = Counter64
_AcSonetAlarmsPathAIS_Object = MibTableColumn
acSonetAlarmsPathAIS = _AcSonetAlarmsPathAIS_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 2, 2, 1, 5),
    _AcSonetAlarmsPathAIS_Type()
)
acSonetAlarmsPathAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetAlarmsPathAIS.setStatus("current")
_AcSonetAlarmsPathYellow_Type = Counter64
_AcSonetAlarmsPathYellow_Object = MibTableColumn
acSonetAlarmsPathYellow = _AcSonetAlarmsPathYellow_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 2, 2, 1, 6),
    _AcSonetAlarmsPathYellow_Type()
)
acSonetAlarmsPathYellow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetAlarmsPathYellow.setStatus("current")
_AcSonetErrCounter_ObjectIdentity = ObjectIdentity
acSonetErrCounter = _AcSonetErrCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 3)
)
_AcSonetErrCounterNumber_Type = Integer32
_AcSonetErrCounterNumber_Object = MibScalar
acSonetErrCounterNumber = _AcSonetErrCounterNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 3, 1),
    _AcSonetErrCounterNumber_Type()
)
acSonetErrCounterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetErrCounterNumber.setStatus("current")
_AcSonetErrCounterTable_Object = MibTable
acSonetErrCounterTable = _AcSonetErrCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 3, 2)
)
if mibBuilder.loadTexts:
    acSonetErrCounterTable.setStatus("current")
_AcSonetErrCounterEntry_Object = MibTableRow
acSonetErrCounterEntry = _AcSonetErrCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 3, 2, 1)
)
acSonetErrCounterEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acSonetErrCounterIndex"),
)
if mibBuilder.loadTexts:
    acSonetErrCounterEntry.setStatus("current")
_AcSonetErrCounterIndex_Type = Integer32
_AcSonetErrCounterIndex_Object = MibTableColumn
acSonetErrCounterIndex = _AcSonetErrCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 3, 2, 1, 1),
    _AcSonetErrCounterIndex_Type()
)
acSonetErrCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetErrCounterIndex.setStatus("current")
_AcSonetErrCounterOOF_Type = Counter64
_AcSonetErrCounterOOF_Object = MibTableColumn
acSonetErrCounterOOF = _AcSonetErrCounterOOF_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 3, 2, 1, 2),
    _AcSonetErrCounterOOF_Type()
)
acSonetErrCounterOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetErrCounterOOF.setStatus("current")
_AcSonetErrCounterLOC_Type = Counter64
_AcSonetErrCounterLOC_Object = MibTableColumn
acSonetErrCounterLOC = _AcSonetErrCounterLOC_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 3, 2, 1, 3),
    _AcSonetErrCounterLOC_Type()
)
acSonetErrCounterLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetErrCounterLOC.setStatus("current")
_AcSonetErrCounterB1BIP_Type = Counter64
_AcSonetErrCounterB1BIP_Object = MibTableColumn
acSonetErrCounterB1BIP = _AcSonetErrCounterB1BIP_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 3, 2, 1, 4),
    _AcSonetErrCounterB1BIP_Type()
)
acSonetErrCounterB1BIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetErrCounterB1BIP.setStatus("current")
_AcSonetErrCounterB2BIP_Type = Counter64
_AcSonetErrCounterB2BIP_Object = MibTableColumn
acSonetErrCounterB2BIP = _AcSonetErrCounterB2BIP_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 3, 2, 1, 5),
    _AcSonetErrCounterB2BIP_Type()
)
acSonetErrCounterB2BIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetErrCounterB2BIP.setStatus("current")
_AcSonetErrCounterB3BIP_Type = Counter64
_AcSonetErrCounterB3BIP_Object = MibTableColumn
acSonetErrCounterB3BIP = _AcSonetErrCounterB3BIP_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 3, 2, 1, 6),
    _AcSonetErrCounterB3BIP_Type()
)
acSonetErrCounterB3BIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetErrCounterB3BIP.setStatus("current")
_AcSonetErrCounterLineFEBE_Type = Counter64
_AcSonetErrCounterLineFEBE_Object = MibTableColumn
acSonetErrCounterLineFEBE = _AcSonetErrCounterLineFEBE_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 3, 2, 1, 7),
    _AcSonetErrCounterLineFEBE_Type()
)
acSonetErrCounterLineFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetErrCounterLineFEBE.setStatus("current")
_AcSonetErrCounterPathFEBE_Type = Counter64
_AcSonetErrCounterPathFEBE_Object = MibTableColumn
acSonetErrCounterPathFEBE = _AcSonetErrCounterPathFEBE_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 3, 2, 1, 8),
    _AcSonetErrCounterPathFEBE_Type()
)
acSonetErrCounterPathFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetErrCounterPathFEBE.setStatus("current")
_AcSonetErrCounterHEC_Type = Counter64
_AcSonetErrCounterHEC_Object = MibTableColumn
acSonetErrCounterHEC = _AcSonetErrCounterHEC_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 3, 2, 1, 9),
    _AcSonetErrCounterHEC_Type()
)
acSonetErrCounterHEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetErrCounterHEC.setStatus("current")
_AcSonetEtsCounter_ObjectIdentity = ObjectIdentity
acSonetEtsCounter = _AcSonetEtsCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 4)
)
_AcSonetEtsCounterNumber_Type = Integer32
_AcSonetEtsCounterNumber_Object = MibScalar
acSonetEtsCounterNumber = _AcSonetEtsCounterNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 4, 1),
    _AcSonetEtsCounterNumber_Type()
)
acSonetEtsCounterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetEtsCounterNumber.setStatus("current")
_AcSonetEtsCounterTable_Object = MibTable
acSonetEtsCounterTable = _AcSonetEtsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 4, 2)
)
if mibBuilder.loadTexts:
    acSonetEtsCounterTable.setStatus("current")
_AcSonetEtsCounterEntry_Object = MibTableRow
acSonetEtsCounterEntry = _AcSonetEtsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 4, 2, 1)
)
acSonetEtsCounterEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acSonetEtsCounterIndex"),
)
if mibBuilder.loadTexts:
    acSonetEtsCounterEntry.setStatus("current")
_AcSonetEtsCounterIndex_Type = Integer32
_AcSonetEtsCounterIndex_Object = MibTableColumn
acSonetEtsCounterIndex = _AcSonetEtsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 4, 2, 1, 1),
    _AcSonetEtsCounterIndex_Type()
)
acSonetEtsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetEtsCounterIndex.setStatus("current")
_AcSonetEtsCounterOOF_Type = Counter64
_AcSonetEtsCounterOOF_Object = MibTableColumn
acSonetEtsCounterOOF = _AcSonetEtsCounterOOF_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 4, 2, 1, 2),
    _AcSonetEtsCounterOOF_Type()
)
acSonetEtsCounterOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetEtsCounterOOF.setStatus("current")
_AcSonetEtsCounterLOC_Type = Counter64
_AcSonetEtsCounterLOC_Object = MibTableColumn
acSonetEtsCounterLOC = _AcSonetEtsCounterLOC_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 4, 2, 1, 3),
    _AcSonetEtsCounterLOC_Type()
)
acSonetEtsCounterLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetEtsCounterLOC.setStatus("current")
_AcSonetEtsCounterB1BIP_Type = Counter64
_AcSonetEtsCounterB1BIP_Object = MibTableColumn
acSonetEtsCounterB1BIP = _AcSonetEtsCounterB1BIP_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 4, 2, 1, 4),
    _AcSonetEtsCounterB1BIP_Type()
)
acSonetEtsCounterB1BIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetEtsCounterB1BIP.setStatus("current")
_AcSonetEtsCounterB2BIP_Type = Counter64
_AcSonetEtsCounterB2BIP_Object = MibTableColumn
acSonetEtsCounterB2BIP = _AcSonetEtsCounterB2BIP_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 4, 2, 1, 5),
    _AcSonetEtsCounterB2BIP_Type()
)
acSonetEtsCounterB2BIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetEtsCounterB2BIP.setStatus("current")
_AcSonetEtsCounterB3BIP_Type = Counter64
_AcSonetEtsCounterB3BIP_Object = MibTableColumn
acSonetEtsCounterB3BIP = _AcSonetEtsCounterB3BIP_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 4, 2, 1, 6),
    _AcSonetEtsCounterB3BIP_Type()
)
acSonetEtsCounterB3BIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetEtsCounterB3BIP.setStatus("current")
_AcSonetEtsCounterLineFEBE_Type = Counter64
_AcSonetEtsCounterLineFEBE_Object = MibTableColumn
acSonetEtsCounterLineFEBE = _AcSonetEtsCounterLineFEBE_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 4, 2, 1, 7),
    _AcSonetEtsCounterLineFEBE_Type()
)
acSonetEtsCounterLineFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetEtsCounterLineFEBE.setStatus("current")
_AcSonetEtsCounterPathFEBE_Type = Counter64
_AcSonetEtsCounterPathFEBE_Object = MibTableColumn
acSonetEtsCounterPathFEBE = _AcSonetEtsCounterPathFEBE_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 4, 2, 1, 8),
    _AcSonetEtsCounterPathFEBE_Type()
)
acSonetEtsCounterPathFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetEtsCounterPathFEBE.setStatus("current")
_AcSonetEtsCounterHEC_Type = Counter64
_AcSonetEtsCounterHEC_Object = MibTableColumn
acSonetEtsCounterHEC = _AcSonetEtsCounterHEC_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 1, 4, 2, 1, 9),
    _AcSonetEtsCounterHEC_Type()
)
acSonetEtsCounterHEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetEtsCounterHEC.setStatus("current")
_AcE3_ObjectIdentity = ObjectIdentity
acE3 = _AcE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2)
)
_AcE3Status_ObjectIdentity = ObjectIdentity
acE3Status = _AcE3Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 1)
)
_AcE3StatusNumber_Type = Integer32
_AcE3StatusNumber_Object = MibScalar
acE3StatusNumber = _AcE3StatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 1, 1),
    _AcE3StatusNumber_Type()
)
acE3StatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3StatusNumber.setStatus("current")
_AcE3StatusTable_Object = MibTable
acE3StatusTable = _AcE3StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    acE3StatusTable.setStatus("current")
_AcE3StatusEntry_Object = MibTableRow
acE3StatusEntry = _AcE3StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 1, 2, 1)
)
acE3StatusEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acE3StatusIndex"),
)
if mibBuilder.loadTexts:
    acE3StatusEntry.setStatus("current")
_AcE3StatusIndex_Type = Integer32
_AcE3StatusIndex_Object = MibTableColumn
acE3StatusIndex = _AcE3StatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 1, 2, 1, 1),
    _AcE3StatusIndex_Type()
)
acE3StatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3StatusIndex.setStatus("current")


class _AcE3StatusState_Type(Integer32):
    """Custom type acE3StatusState based on Integer32"""
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
          ("failure", 3),
          ("up", 1))
    )


_AcE3StatusState_Type.__name__ = "Integer32"
_AcE3StatusState_Object = MibTableColumn
acE3StatusState = _AcE3StatusState_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 1, 2, 1, 2),
    _AcE3StatusState_Type()
)
acE3StatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3StatusState.setStatus("current")


class _AcE3StatusLOS_Type(Integer32):
    """Custom type acE3StatusLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcE3StatusLOS_Type.__name__ = "Integer32"
_AcE3StatusLOS_Object = MibTableColumn
acE3StatusLOS = _AcE3StatusLOS_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 1, 2, 1, 3),
    _AcE3StatusLOS_Type()
)
acE3StatusLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3StatusLOS.setStatus("current")


class _AcE3StatusOOF_Type(Integer32):
    """Custom type acE3StatusOOF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcE3StatusOOF_Type.__name__ = "Integer32"
_AcE3StatusOOF_Object = MibTableColumn
acE3StatusOOF = _AcE3StatusOOF_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 1, 2, 1, 4),
    _AcE3StatusOOF_Type()
)
acE3StatusOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3StatusOOF.setStatus("current")


class _AcE3StatusLOC_Type(Integer32):
    """Custom type acE3StatusLOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcE3StatusLOC_Type.__name__ = "Integer32"
_AcE3StatusLOC_Object = MibTableColumn
acE3StatusLOC = _AcE3StatusLOC_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 1, 2, 1, 5),
    _AcE3StatusLOC_Type()
)
acE3StatusLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3StatusLOC.setStatus("current")


class _AcE3StatusAIS_Type(Integer32):
    """Custom type acE3StatusAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcE3StatusAIS_Type.__name__ = "Integer32"
_AcE3StatusAIS_Object = MibTableColumn
acE3StatusAIS = _AcE3StatusAIS_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 1, 2, 1, 6),
    _AcE3StatusAIS_Type()
)
acE3StatusAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3StatusAIS.setStatus("current")


class _AcE3StatusMAFERF_Type(Integer32):
    """Custom type acE3StatusMAFERF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcE3StatusMAFERF_Type.__name__ = "Integer32"
_AcE3StatusMAFERF_Object = MibTableColumn
acE3StatusMAFERF = _AcE3StatusMAFERF_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 1, 2, 1, 7),
    _AcE3StatusMAFERF_Type()
)
acE3StatusMAFERF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3StatusMAFERF.setStatus("current")
_AcE3StatusCustom_Type = Integer32
_AcE3StatusCustom_Object = MibTableColumn
acE3StatusCustom = _AcE3StatusCustom_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 1, 2, 1, 8),
    _AcE3StatusCustom_Type()
)
acE3StatusCustom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3StatusCustom.setStatus("current")
_AcE3StatusDescr_Type = DisplayString
_AcE3StatusDescr_Object = MibTableColumn
acE3StatusDescr = _AcE3StatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 1, 2, 1, 9),
    _AcE3StatusDescr_Type()
)
acE3StatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3StatusDescr.setStatus("current")
_AcE3Alarms_ObjectIdentity = ObjectIdentity
acE3Alarms = _AcE3Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 2)
)
_AcE3AlarmsNumber_Type = Integer32
_AcE3AlarmsNumber_Object = MibScalar
acE3AlarmsNumber = _AcE3AlarmsNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 2, 1),
    _AcE3AlarmsNumber_Type()
)
acE3AlarmsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3AlarmsNumber.setStatus("current")
_AcE3AlarmsTable_Object = MibTable
acE3AlarmsTable = _AcE3AlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 2, 2)
)
if mibBuilder.loadTexts:
    acE3AlarmsTable.setStatus("current")
_AcE3AlarmsEntry_Object = MibTableRow
acE3AlarmsEntry = _AcE3AlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 2, 2, 1)
)
acE3AlarmsEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acE3AlarmsIndex"),
)
if mibBuilder.loadTexts:
    acE3AlarmsEntry.setStatus("current")
_AcE3AlarmsIndex_Type = Integer32
_AcE3AlarmsIndex_Object = MibTableColumn
acE3AlarmsIndex = _AcE3AlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 2, 2, 1, 1),
    _AcE3AlarmsIndex_Type()
)
acE3AlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3AlarmsIndex.setStatus("current")
_AcE3AlarmsLOS_Type = Counter64
_AcE3AlarmsLOS_Object = MibTableColumn
acE3AlarmsLOS = _AcE3AlarmsLOS_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 2, 2, 1, 2),
    _AcE3AlarmsLOS_Type()
)
acE3AlarmsLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3AlarmsLOS.setStatus("current")
_AcE3AlarmsAIS_Type = Counter64
_AcE3AlarmsAIS_Object = MibTableColumn
acE3AlarmsAIS = _AcE3AlarmsAIS_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 2, 2, 1, 3),
    _AcE3AlarmsAIS_Type()
)
acE3AlarmsAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3AlarmsAIS.setStatus("current")
_AcE3AlarmsMAFERF_Type = Counter64
_AcE3AlarmsMAFERF_Object = MibTableColumn
acE3AlarmsMAFERF = _AcE3AlarmsMAFERF_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 2, 2, 1, 4),
    _AcE3AlarmsMAFERF_Type()
)
acE3AlarmsMAFERF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3AlarmsMAFERF.setStatus("current")
_AcE3ErrCounter_ObjectIdentity = ObjectIdentity
acE3ErrCounter = _AcE3ErrCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 3)
)
_AcE3ErrCounterNumber_Type = Integer32
_AcE3ErrCounterNumber_Object = MibScalar
acE3ErrCounterNumber = _AcE3ErrCounterNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 3, 1),
    _AcE3ErrCounterNumber_Type()
)
acE3ErrCounterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3ErrCounterNumber.setStatus("current")
_AcE3ErrCounterTable_Object = MibTable
acE3ErrCounterTable = _AcE3ErrCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 3, 2)
)
if mibBuilder.loadTexts:
    acE3ErrCounterTable.setStatus("current")
_AcE3ErrCounterEntry_Object = MibTableRow
acE3ErrCounterEntry = _AcE3ErrCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 3, 2, 1)
)
acE3ErrCounterEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acE3ErrCounterIndex"),
)
if mibBuilder.loadTexts:
    acE3ErrCounterEntry.setStatus("current")
_AcE3ErrCounterIndex_Type = Integer32
_AcE3ErrCounterIndex_Object = MibTableColumn
acE3ErrCounterIndex = _AcE3ErrCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 3, 2, 1, 1),
    _AcE3ErrCounterIndex_Type()
)
acE3ErrCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3ErrCounterIndex.setStatus("current")
_AcE3ErrCounterLCV_Type = Counter64
_AcE3ErrCounterLCV_Object = MibTableColumn
acE3ErrCounterLCV = _AcE3ErrCounterLCV_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 3, 2, 1, 2),
    _AcE3ErrCounterLCV_Type()
)
acE3ErrCounterLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3ErrCounterLCV.setStatus("current")
_AcE3ErrCounterOOF_Type = Counter64
_AcE3ErrCounterOOF_Object = MibTableColumn
acE3ErrCounterOOF = _AcE3ErrCounterOOF_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 3, 2, 1, 3),
    _AcE3ErrCounterOOF_Type()
)
acE3ErrCounterOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3ErrCounterOOF.setStatus("current")
_AcE3ErrCounterLOC_Type = Counter64
_AcE3ErrCounterLOC_Object = MibTableColumn
acE3ErrCounterLOC = _AcE3ErrCounterLOC_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 3, 2, 1, 4),
    _AcE3ErrCounterLOC_Type()
)
acE3ErrCounterLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3ErrCounterLOC.setStatus("current")
_AcE3ErrCounterBIP_Type = Counter64
_AcE3ErrCounterBIP_Object = MibTableColumn
acE3ErrCounterBIP = _AcE3ErrCounterBIP_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 3, 2, 1, 5),
    _AcE3ErrCounterBIP_Type()
)
acE3ErrCounterBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3ErrCounterBIP.setStatus("current")
_AcE3ErrCounterMAFEBE_Type = Counter64
_AcE3ErrCounterMAFEBE_Object = MibTableColumn
acE3ErrCounterMAFEBE = _AcE3ErrCounterMAFEBE_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 3, 2, 1, 6),
    _AcE3ErrCounterMAFEBE_Type()
)
acE3ErrCounterMAFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3ErrCounterMAFEBE.setStatus("current")
_AcE3ErrCounterHEC_Type = Counter64
_AcE3ErrCounterHEC_Object = MibTableColumn
acE3ErrCounterHEC = _AcE3ErrCounterHEC_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 3, 2, 1, 7),
    _AcE3ErrCounterHEC_Type()
)
acE3ErrCounterHEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3ErrCounterHEC.setStatus("current")
_AcE3EtsCounter_ObjectIdentity = ObjectIdentity
acE3EtsCounter = _AcE3EtsCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 4)
)
_AcE3EtsCounterNumber_Type = Integer32
_AcE3EtsCounterNumber_Object = MibScalar
acE3EtsCounterNumber = _AcE3EtsCounterNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 4, 1),
    _AcE3EtsCounterNumber_Type()
)
acE3EtsCounterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3EtsCounterNumber.setStatus("current")
_AcE3EtsCounterTable_Object = MibTable
acE3EtsCounterTable = _AcE3EtsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 4, 2)
)
if mibBuilder.loadTexts:
    acE3EtsCounterTable.setStatus("current")
_AcE3EtsCounterEntry_Object = MibTableRow
acE3EtsCounterEntry = _AcE3EtsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 4, 2, 1)
)
acE3EtsCounterEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acE3EtsCounterIndex"),
)
if mibBuilder.loadTexts:
    acE3EtsCounterEntry.setStatus("current")
_AcE3EtsCounterIndex_Type = Integer32
_AcE3EtsCounterIndex_Object = MibTableColumn
acE3EtsCounterIndex = _AcE3EtsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 4, 2, 1, 1),
    _AcE3EtsCounterIndex_Type()
)
acE3EtsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3EtsCounterIndex.setStatus("current")
_AcE3EtsCounterLCV_Type = Counter64
_AcE3EtsCounterLCV_Object = MibTableColumn
acE3EtsCounterLCV = _AcE3EtsCounterLCV_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 4, 2, 1, 2),
    _AcE3EtsCounterLCV_Type()
)
acE3EtsCounterLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3EtsCounterLCV.setStatus("current")
_AcE3EtsCounterOOF_Type = Counter64
_AcE3EtsCounterOOF_Object = MibTableColumn
acE3EtsCounterOOF = _AcE3EtsCounterOOF_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 4, 2, 1, 3),
    _AcE3EtsCounterOOF_Type()
)
acE3EtsCounterOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3EtsCounterOOF.setStatus("current")
_AcE3EtsCounterLOC_Type = Counter64
_AcE3EtsCounterLOC_Object = MibTableColumn
acE3EtsCounterLOC = _AcE3EtsCounterLOC_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 4, 2, 1, 4),
    _AcE3EtsCounterLOC_Type()
)
acE3EtsCounterLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3EtsCounterLOC.setStatus("current")
_AcE3EtsCounterBIP_Type = Counter64
_AcE3EtsCounterBIP_Object = MibTableColumn
acE3EtsCounterBIP = _AcE3EtsCounterBIP_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 4, 2, 1, 5),
    _AcE3EtsCounterBIP_Type()
)
acE3EtsCounterBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3EtsCounterBIP.setStatus("current")
_AcE3EtsCounterMAFEBE_Type = Counter64
_AcE3EtsCounterMAFEBE_Object = MibTableColumn
acE3EtsCounterMAFEBE = _AcE3EtsCounterMAFEBE_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 4, 2, 1, 6),
    _AcE3EtsCounterMAFEBE_Type()
)
acE3EtsCounterMAFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3EtsCounterMAFEBE.setStatus("current")
_AcE3EtsCounterHEC_Type = Counter64
_AcE3EtsCounterHEC_Object = MibTableColumn
acE3EtsCounterHEC = _AcE3EtsCounterHEC_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 2, 4, 2, 1, 7),
    _AcE3EtsCounterHEC_Type()
)
acE3EtsCounterHEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acE3EtsCounterHEC.setStatus("current")
_AcE1_ObjectIdentity = ObjectIdentity
acE1 = _AcE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 3)
)
_AcE1Status_ObjectIdentity = ObjectIdentity
acE1Status = _AcE1Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 3, 1)
)
_AcE1Alarms_ObjectIdentity = ObjectIdentity
acE1Alarms = _AcE1Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 3, 2)
)
_AcE1ErrCounter_ObjectIdentity = ObjectIdentity
acE1ErrCounter = _AcE1ErrCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 3, 3)
)
_AcE1EtsCounter_ObjectIdentity = ObjectIdentity
acE1EtsCounter = _AcE1EtsCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 3, 4)
)
_AcGigabit_ObjectIdentity = ObjectIdentity
acGigabit = _AcGigabit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4)
)
_AcGigabitStatus_ObjectIdentity = ObjectIdentity
acGigabitStatus = _AcGigabitStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 1)
)
_AcGigabitStatusNumber_Type = Integer32
_AcGigabitStatusNumber_Object = MibScalar
acGigabitStatusNumber = _AcGigabitStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 1, 1),
    _AcGigabitStatusNumber_Type()
)
acGigabitStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitStatusNumber.setStatus("current")
_AcGigabitStatusTable_Object = MibTable
acGigabitStatusTable = _AcGigabitStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    acGigabitStatusTable.setStatus("current")
_AcGigabitStatusEntry_Object = MibTableRow
acGigabitStatusEntry = _AcGigabitStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 1, 2, 1)
)
acGigabitStatusEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acGigabitStatusIndex"),
)
if mibBuilder.loadTexts:
    acGigabitStatusEntry.setStatus("current")
_AcGigabitStatusIndex_Type = Integer32
_AcGigabitStatusIndex_Object = MibTableColumn
acGigabitStatusIndex = _AcGigabitStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 1, 2, 1, 1),
    _AcGigabitStatusIndex_Type()
)
acGigabitStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitStatusIndex.setStatus("current")


class _AcGigabitStatusState_Type(Integer32):
    """Custom type acGigabitStatusState based on Integer32"""
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
          ("failure", 3),
          ("up", 1))
    )


_AcGigabitStatusState_Type.__name__ = "Integer32"
_AcGigabitStatusState_Object = MibTableColumn
acGigabitStatusState = _AcGigabitStatusState_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 1, 2, 1, 2),
    _AcGigabitStatusState_Type()
)
acGigabitStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitStatusState.setStatus("current")


class _AcGigabitStatusLOS_Type(Integer32):
    """Custom type acGigabitStatusLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcGigabitStatusLOS_Type.__name__ = "Integer32"
_AcGigabitStatusLOS_Object = MibTableColumn
acGigabitStatusLOS = _AcGigabitStatusLOS_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 1, 2, 1, 3),
    _AcGigabitStatusLOS_Type()
)
acGigabitStatusLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitStatusLOS.setStatus("current")


class _AcGigabitStatusLossofSync_Type(Integer32):
    """Custom type acGigabitStatusLossofSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcGigabitStatusLossofSync_Type.__name__ = "Integer32"
_AcGigabitStatusLossofSync_Object = MibTableColumn
acGigabitStatusLossofSync = _AcGigabitStatusLossofSync_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 1, 2, 1, 4),
    _AcGigabitStatusLossofSync_Type()
)
acGigabitStatusLossofSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitStatusLossofSync.setStatus("current")


class _AcGigabitStatusLinkDown_Type(Integer32):
    """Custom type acGigabitStatusLinkDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcGigabitStatusLinkDown_Type.__name__ = "Integer32"
_AcGigabitStatusLinkDown_Object = MibTableColumn
acGigabitStatusLinkDown = _AcGigabitStatusLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 1, 2, 1, 5),
    _AcGigabitStatusLinkDown_Type()
)
acGigabitStatusLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitStatusLinkDown.setStatus("current")
_AcGigabitStatusCustom_Type = Integer32
_AcGigabitStatusCustom_Object = MibTableColumn
acGigabitStatusCustom = _AcGigabitStatusCustom_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 1, 2, 1, 6),
    _AcGigabitStatusCustom_Type()
)
acGigabitStatusCustom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitStatusCustom.setStatus("current")
_AcGigabitStatusDescr_Type = DisplayString
_AcGigabitStatusDescr_Object = MibTableColumn
acGigabitStatusDescr = _AcGigabitStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 1, 2, 1, 7),
    _AcGigabitStatusDescr_Type()
)
acGigabitStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitStatusDescr.setStatus("current")
_AcGigabitAlarms_ObjectIdentity = ObjectIdentity
acGigabitAlarms = _AcGigabitAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 2)
)
_AcGigabitAlarmsNumber_Type = Integer32
_AcGigabitAlarmsNumber_Object = MibScalar
acGigabitAlarmsNumber = _AcGigabitAlarmsNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 2, 1),
    _AcGigabitAlarmsNumber_Type()
)
acGigabitAlarmsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitAlarmsNumber.setStatus("current")
_AcGigabitAlarmsTable_Object = MibTable
acGigabitAlarmsTable = _AcGigabitAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 2, 2)
)
if mibBuilder.loadTexts:
    acGigabitAlarmsTable.setStatus("current")
_AcGigabitAlarmsEntry_Object = MibTableRow
acGigabitAlarmsEntry = _AcGigabitAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 2, 2, 1)
)
acGigabitAlarmsEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acGigabitAlarmsIndex"),
)
if mibBuilder.loadTexts:
    acGigabitAlarmsEntry.setStatus("current")
_AcGigabitAlarmsIndex_Type = Integer32
_AcGigabitAlarmsIndex_Object = MibTableColumn
acGigabitAlarmsIndex = _AcGigabitAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 2, 2, 1, 1),
    _AcGigabitAlarmsIndex_Type()
)
acGigabitAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitAlarmsIndex.setStatus("current")
_AcGigabitAlarmsLOS_Type = Counter64
_AcGigabitAlarmsLOS_Object = MibTableColumn
acGigabitAlarmsLOS = _AcGigabitAlarmsLOS_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 2, 2, 1, 2),
    _AcGigabitAlarmsLOS_Type()
)
acGigabitAlarmsLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitAlarmsLOS.setStatus("current")
_AcGigabitAlarmsLinkDown_Type = Counter64
_AcGigabitAlarmsLinkDown_Object = MibTableColumn
acGigabitAlarmsLinkDown = _AcGigabitAlarmsLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 2, 2, 1, 3),
    _AcGigabitAlarmsLinkDown_Type()
)
acGigabitAlarmsLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitAlarmsLinkDown.setStatus("current")
_AcGigabitErrCounter_ObjectIdentity = ObjectIdentity
acGigabitErrCounter = _AcGigabitErrCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 3)
)
_AcGigabitErrCounterNumber_Type = Integer32
_AcGigabitErrCounterNumber_Object = MibScalar
acGigabitErrCounterNumber = _AcGigabitErrCounterNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 3, 1),
    _AcGigabitErrCounterNumber_Type()
)
acGigabitErrCounterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitErrCounterNumber.setStatus("current")
_AcGigabitErrCounterTable_Object = MibTable
acGigabitErrCounterTable = _AcGigabitErrCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 3, 2)
)
if mibBuilder.loadTexts:
    acGigabitErrCounterTable.setStatus("current")
_AcGigabitErrCounterEntry_Object = MibTableRow
acGigabitErrCounterEntry = _AcGigabitErrCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 3, 2, 1)
)
acGigabitErrCounterEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acGigabitErrCounterIndex"),
)
if mibBuilder.loadTexts:
    acGigabitErrCounterEntry.setStatus("current")
_AcGigabitErrCounterIndex_Type = Integer32
_AcGigabitErrCounterIndex_Object = MibTableColumn
acGigabitErrCounterIndex = _AcGigabitErrCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 3, 2, 1, 1),
    _AcGigabitErrCounterIndex_Type()
)
acGigabitErrCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitErrCounterIndex.setStatus("current")
_AcGigabitErrCounterTotalFrame_Type = Counter64
_AcGigabitErrCounterTotalFrame_Object = MibTableColumn
acGigabitErrCounterTotalFrame = _AcGigabitErrCounterTotalFrame_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 3, 2, 1, 2),
    _AcGigabitErrCounterTotalFrame_Type()
)
acGigabitErrCounterTotalFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitErrCounterTotalFrame.setStatus("current")
_AcGigabitErrCounterErroredFrame_Type = Counter64
_AcGigabitErrCounterErroredFrame_Object = MibTableColumn
acGigabitErrCounterErroredFrame = _AcGigabitErrCounterErroredFrame_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 3, 2, 1, 3),
    _AcGigabitErrCounterErroredFrame_Type()
)
acGigabitErrCounterErroredFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitErrCounterErroredFrame.setStatus("current")
_AcGigabitErrCounterFalseCarrier_Type = Counter64
_AcGigabitErrCounterFalseCarrier_Object = MibTableColumn
acGigabitErrCounterFalseCarrier = _AcGigabitErrCounterFalseCarrier_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 3, 2, 1, 4),
    _AcGigabitErrCounterFalseCarrier_Type()
)
acGigabitErrCounterFalseCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitErrCounterFalseCarrier.setStatus("current")
_AcGigabitErrCounterLossofSync_Type = Counter64
_AcGigabitErrCounterLossofSync_Object = MibTableColumn
acGigabitErrCounterLossofSync = _AcGigabitErrCounterLossofSync_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 3, 2, 1, 5),
    _AcGigabitErrCounterLossofSync_Type()
)
acGigabitErrCounterLossofSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitErrCounterLossofSync.setStatus("current")
_AcGigabitErrCounterLineError_Type = Counter64
_AcGigabitErrCounterLineError_Object = MibTableColumn
acGigabitErrCounterLineError = _AcGigabitErrCounterLineError_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 3, 2, 1, 6),
    _AcGigabitErrCounterLineError_Type()
)
acGigabitErrCounterLineError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitErrCounterLineError.setStatus("current")
_AcGigabitEtsCounter_ObjectIdentity = ObjectIdentity
acGigabitEtsCounter = _AcGigabitEtsCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 4)
)
_AcGigabitEtsCounterNumber_Type = Integer32
_AcGigabitEtsCounterNumber_Object = MibScalar
acGigabitEtsCounterNumber = _AcGigabitEtsCounterNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 4, 1),
    _AcGigabitEtsCounterNumber_Type()
)
acGigabitEtsCounterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitEtsCounterNumber.setStatus("current")
_AcGigabitEtsCounterTable_Object = MibTable
acGigabitEtsCounterTable = _AcGigabitEtsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 4, 2)
)
if mibBuilder.loadTexts:
    acGigabitEtsCounterTable.setStatus("current")
_AcGigabitEtsCounterEntry_Object = MibTableRow
acGigabitEtsCounterEntry = _AcGigabitEtsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 4, 2, 1)
)
acGigabitEtsCounterEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acGigabitEtsCounterIndex"),
)
if mibBuilder.loadTexts:
    acGigabitEtsCounterEntry.setStatus("current")
_AcGigabitEtsCounterIndex_Type = Integer32
_AcGigabitEtsCounterIndex_Object = MibTableColumn
acGigabitEtsCounterIndex = _AcGigabitEtsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 4, 2, 1, 1),
    _AcGigabitEtsCounterIndex_Type()
)
acGigabitEtsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitEtsCounterIndex.setStatus("current")
_AcGigabitEtsCounterTotalFrame_Type = Counter64
_AcGigabitEtsCounterTotalFrame_Object = MibTableColumn
acGigabitEtsCounterTotalFrame = _AcGigabitEtsCounterTotalFrame_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 4, 2, 1, 2),
    _AcGigabitEtsCounterTotalFrame_Type()
)
acGigabitEtsCounterTotalFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitEtsCounterTotalFrame.setStatus("current")
_AcGigabitEtsCounterErroredFrame_Type = Counter64
_AcGigabitEtsCounterErroredFrame_Object = MibTableColumn
acGigabitEtsCounterErroredFrame = _AcGigabitEtsCounterErroredFrame_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 4, 2, 1, 3),
    _AcGigabitEtsCounterErroredFrame_Type()
)
acGigabitEtsCounterErroredFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitEtsCounterErroredFrame.setStatus("current")
_AcGigabitEtsCounterFalseCarrier_Type = Counter64
_AcGigabitEtsCounterFalseCarrier_Object = MibTableColumn
acGigabitEtsCounterFalseCarrier = _AcGigabitEtsCounterFalseCarrier_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 4, 2, 1, 4),
    _AcGigabitEtsCounterFalseCarrier_Type()
)
acGigabitEtsCounterFalseCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitEtsCounterFalseCarrier.setStatus("current")
_AcGigabitEtsCounterLossofSync_Type = Counter64
_AcGigabitEtsCounterLossofSync_Object = MibTableColumn
acGigabitEtsCounterLossofSync = _AcGigabitEtsCounterLossofSync_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 4, 2, 1, 5),
    _AcGigabitEtsCounterLossofSync_Type()
)
acGigabitEtsCounterLossofSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitEtsCounterLossofSync.setStatus("current")
_AcGigabitEtsCounterLineError_Type = Counter64
_AcGigabitEtsCounterLineError_Object = MibTableColumn
acGigabitEtsCounterLineError = _AcGigabitEtsCounterLineError_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 4, 4, 2, 1, 6),
    _AcGigabitEtsCounterLineError_Type()
)
acGigabitEtsCounterLineError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGigabitEtsCounterLineError.setStatus("current")
_AcFibrechannel_ObjectIdentity = ObjectIdentity
acFibrechannel = _AcFibrechannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5)
)
_AcFibrechannelStatus_ObjectIdentity = ObjectIdentity
acFibrechannelStatus = _AcFibrechannelStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 1)
)
_AcFibrechannelStatusNumber_Type = Integer32
_AcFibrechannelStatusNumber_Object = MibScalar
acFibrechannelStatusNumber = _AcFibrechannelStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 1, 1),
    _AcFibrechannelStatusNumber_Type()
)
acFibrechannelStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelStatusNumber.setStatus("current")
_AcFibrechannelStatusTable_Object = MibTable
acFibrechannelStatusTable = _AcFibrechannelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 1, 2)
)
if mibBuilder.loadTexts:
    acFibrechannelStatusTable.setStatus("current")
_AcFibrechannelStatusEntry_Object = MibTableRow
acFibrechannelStatusEntry = _AcFibrechannelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 1, 2, 1)
)
acFibrechannelStatusEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acFibrechannelStatusIndex"),
)
if mibBuilder.loadTexts:
    acFibrechannelStatusEntry.setStatus("current")
_AcFibrechannelStatusIndex_Type = Integer32
_AcFibrechannelStatusIndex_Object = MibTableColumn
acFibrechannelStatusIndex = _AcFibrechannelStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 1, 2, 1, 1),
    _AcFibrechannelStatusIndex_Type()
)
acFibrechannelStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelStatusIndex.setStatus("current")


class _AcFibrechannelStatusState_Type(Integer32):
    """Custom type acFibrechannelStatusState based on Integer32"""
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
          ("failure", 3),
          ("up", 1))
    )


_AcFibrechannelStatusState_Type.__name__ = "Integer32"
_AcFibrechannelStatusState_Object = MibTableColumn
acFibrechannelStatusState = _AcFibrechannelStatusState_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 1, 2, 1, 2),
    _AcFibrechannelStatusState_Type()
)
acFibrechannelStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelStatusState.setStatus("current")


class _AcFibrechannelStatusLOS_Type(Integer32):
    """Custom type acFibrechannelStatusLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcFibrechannelStatusLOS_Type.__name__ = "Integer32"
_AcFibrechannelStatusLOS_Object = MibTableColumn
acFibrechannelStatusLOS = _AcFibrechannelStatusLOS_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 1, 2, 1, 3),
    _AcFibrechannelStatusLOS_Type()
)
acFibrechannelStatusLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelStatusLOS.setStatus("current")


class _AcFibrechannelStatusLossofSync_Type(Integer32):
    """Custom type acFibrechannelStatusLossofSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcFibrechannelStatusLossofSync_Type.__name__ = "Integer32"
_AcFibrechannelStatusLossofSync_Object = MibTableColumn
acFibrechannelStatusLossofSync = _AcFibrechannelStatusLossofSync_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 1, 2, 1, 4),
    _AcFibrechannelStatusLossofSync_Type()
)
acFibrechannelStatusLossofSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelStatusLossofSync.setStatus("current")


class _AcFibrechannelStatusLinkDown_Type(Integer32):
    """Custom type acFibrechannelStatusLinkDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AcFibrechannelStatusLinkDown_Type.__name__ = "Integer32"
_AcFibrechannelStatusLinkDown_Object = MibTableColumn
acFibrechannelStatusLinkDown = _AcFibrechannelStatusLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 1, 2, 1, 5),
    _AcFibrechannelStatusLinkDown_Type()
)
acFibrechannelStatusLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelStatusLinkDown.setStatus("current")
_AcFibrechannelStatusCustom_Type = Integer32
_AcFibrechannelStatusCustom_Object = MibTableColumn
acFibrechannelStatusCustom = _AcFibrechannelStatusCustom_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 1, 2, 1, 6),
    _AcFibrechannelStatusCustom_Type()
)
acFibrechannelStatusCustom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelStatusCustom.setStatus("current")
_AcFibrechannelStatusDescr_Type = DisplayString
_AcFibrechannelStatusDescr_Object = MibTableColumn
acFibrechannelStatusDescr = _AcFibrechannelStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 1, 2, 1, 7),
    _AcFibrechannelStatusDescr_Type()
)
acFibrechannelStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelStatusDescr.setStatus("current")
_AcFibrechannelAlarms_ObjectIdentity = ObjectIdentity
acFibrechannelAlarms = _AcFibrechannelAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 2)
)
_AcFibrechannelAlarmsNumber_Type = Integer32
_AcFibrechannelAlarmsNumber_Object = MibScalar
acFibrechannelAlarmsNumber = _AcFibrechannelAlarmsNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 2, 1),
    _AcFibrechannelAlarmsNumber_Type()
)
acFibrechannelAlarmsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelAlarmsNumber.setStatus("current")
_AcFibrechannelAlarmsTable_Object = MibTable
acFibrechannelAlarmsTable = _AcFibrechannelAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 2, 2)
)
if mibBuilder.loadTexts:
    acFibrechannelAlarmsTable.setStatus("current")
_AcFibrechannelAlarmsEntry_Object = MibTableRow
acFibrechannelAlarmsEntry = _AcFibrechannelAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 2, 2, 1)
)
acFibrechannelAlarmsEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acFibrechannelAlarmsIndex"),
)
if mibBuilder.loadTexts:
    acFibrechannelAlarmsEntry.setStatus("current")
_AcFibrechannelAlarmsIndex_Type = Integer32
_AcFibrechannelAlarmsIndex_Object = MibTableColumn
acFibrechannelAlarmsIndex = _AcFibrechannelAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 2, 2, 1, 1),
    _AcFibrechannelAlarmsIndex_Type()
)
acFibrechannelAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelAlarmsIndex.setStatus("current")
_AcFibrechannelAlarmsLOS_Type = Counter64
_AcFibrechannelAlarmsLOS_Object = MibTableColumn
acFibrechannelAlarmsLOS = _AcFibrechannelAlarmsLOS_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 2, 2, 1, 2),
    _AcFibrechannelAlarmsLOS_Type()
)
acFibrechannelAlarmsLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelAlarmsLOS.setStatus("current")
_AcFibrechannelAlarmsLinkDown_Type = Counter64
_AcFibrechannelAlarmsLinkDown_Object = MibTableColumn
acFibrechannelAlarmsLinkDown = _AcFibrechannelAlarmsLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 2, 2, 1, 3),
    _AcFibrechannelAlarmsLinkDown_Type()
)
acFibrechannelAlarmsLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelAlarmsLinkDown.setStatus("current")
_AcFibrechannelErrCounter_ObjectIdentity = ObjectIdentity
acFibrechannelErrCounter = _AcFibrechannelErrCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 3)
)
_AcFibrechannelErrCounterNumber_Type = Integer32
_AcFibrechannelErrCounterNumber_Object = MibScalar
acFibrechannelErrCounterNumber = _AcFibrechannelErrCounterNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 3, 1),
    _AcFibrechannelErrCounterNumber_Type()
)
acFibrechannelErrCounterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelErrCounterNumber.setStatus("current")
_AcFibrechannelErrCounterTable_Object = MibTable
acFibrechannelErrCounterTable = _AcFibrechannelErrCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 3, 2)
)
if mibBuilder.loadTexts:
    acFibrechannelErrCounterTable.setStatus("current")
_AcFibrechannelErrCounterEntry_Object = MibTableRow
acFibrechannelErrCounterEntry = _AcFibrechannelErrCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 3, 2, 1)
)
acFibrechannelErrCounterEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acFibrechannelErrCounterIndex"),
)
if mibBuilder.loadTexts:
    acFibrechannelErrCounterEntry.setStatus("current")
_AcFibrechannelErrCounterIndex_Type = Integer32
_AcFibrechannelErrCounterIndex_Object = MibTableColumn
acFibrechannelErrCounterIndex = _AcFibrechannelErrCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 3, 2, 1, 1),
    _AcFibrechannelErrCounterIndex_Type()
)
acFibrechannelErrCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelErrCounterIndex.setStatus("current")
_AcFibrechannelErrCounterTotalFrame_Type = Counter64
_AcFibrechannelErrCounterTotalFrame_Object = MibTableColumn
acFibrechannelErrCounterTotalFrame = _AcFibrechannelErrCounterTotalFrame_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 3, 2, 1, 2),
    _AcFibrechannelErrCounterTotalFrame_Type()
)
acFibrechannelErrCounterTotalFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelErrCounterTotalFrame.setStatus("current")
_AcFibrechannelErrCounterErroredFrame_Type = Counter64
_AcFibrechannelErrCounterErroredFrame_Object = MibTableColumn
acFibrechannelErrCounterErroredFrame = _AcFibrechannelErrCounterErroredFrame_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 3, 2, 1, 3),
    _AcFibrechannelErrCounterErroredFrame_Type()
)
acFibrechannelErrCounterErroredFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelErrCounterErroredFrame.setStatus("current")
_AcFibrechannelErrCounterDiscardFrame_Type = Counter64
_AcFibrechannelErrCounterDiscardFrame_Object = MibTableColumn
acFibrechannelErrCounterDiscardFrame = _AcFibrechannelErrCounterDiscardFrame_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 3, 2, 1, 4),
    _AcFibrechannelErrCounterDiscardFrame_Type()
)
acFibrechannelErrCounterDiscardFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelErrCounterDiscardFrame.setStatus("current")
_AcFibrechannelErrCounterLossofSync_Type = Counter64
_AcFibrechannelErrCounterLossofSync_Object = MibTableColumn
acFibrechannelErrCounterLossofSync = _AcFibrechannelErrCounterLossofSync_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 3, 2, 1, 5),
    _AcFibrechannelErrCounterLossofSync_Type()
)
acFibrechannelErrCounterLossofSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelErrCounterLossofSync.setStatus("current")
_AcFibrechannelErrCounterLineError_Type = Counter64
_AcFibrechannelErrCounterLineError_Object = MibTableColumn
acFibrechannelErrCounterLineError = _AcFibrechannelErrCounterLineError_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 3, 2, 1, 6),
    _AcFibrechannelErrCounterLineError_Type()
)
acFibrechannelErrCounterLineError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelErrCounterLineError.setStatus("current")
_AcFibrechannelErrCounterFCSError_Type = Counter64
_AcFibrechannelErrCounterFCSError_Object = MibTableColumn
acFibrechannelErrCounterFCSError = _AcFibrechannelErrCounterFCSError_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 3, 2, 1, 7),
    _AcFibrechannelErrCounterFCSError_Type()
)
acFibrechannelErrCounterFCSError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelErrCounterFCSError.setStatus("current")
_AcFibrechannelErrCounterCheckError_Type = Counter64
_AcFibrechannelErrCounterCheckError_Object = MibTableColumn
acFibrechannelErrCounterCheckError = _AcFibrechannelErrCounterCheckError_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 3, 2, 1, 8),
    _AcFibrechannelErrCounterCheckError_Type()
)
acFibrechannelErrCounterCheckError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelErrCounterCheckError.setStatus("current")
_AcFibrechannelEtsCounter_ObjectIdentity = ObjectIdentity
acFibrechannelEtsCounter = _AcFibrechannelEtsCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 4)
)
_AcFibrechannelEtsCounterNumber_Type = Integer32
_AcFibrechannelEtsCounterNumber_Object = MibScalar
acFibrechannelEtsCounterNumber = _AcFibrechannelEtsCounterNumber_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 4, 1),
    _AcFibrechannelEtsCounterNumber_Type()
)
acFibrechannelEtsCounterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelEtsCounterNumber.setStatus("current")
_AcFibrechannelEtsCounterTable_Object = MibTable
acFibrechannelEtsCounterTable = _AcFibrechannelEtsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 4, 2)
)
if mibBuilder.loadTexts:
    acFibrechannelEtsCounterTable.setStatus("current")
_AcFibrechannelEtsCounterEntry_Object = MibTableRow
acFibrechannelEtsCounterEntry = _AcFibrechannelEtsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 4, 2, 1)
)
acFibrechannelEtsCounterEntry.setIndexNames(
    (0, "ATMEDIA-MIB", "acFibrechannelEtsCounterIndex"),
)
if mibBuilder.loadTexts:
    acFibrechannelEtsCounterEntry.setStatus("current")
_AcFibrechannelEtsCounterIndex_Type = Integer32
_AcFibrechannelEtsCounterIndex_Object = MibTableColumn
acFibrechannelEtsCounterIndex = _AcFibrechannelEtsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 4, 2, 1, 1),
    _AcFibrechannelEtsCounterIndex_Type()
)
acFibrechannelEtsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelEtsCounterIndex.setStatus("current")
_AcFibrechannelEtsCounterTotalFrame_Type = Counter64
_AcFibrechannelEtsCounterTotalFrame_Object = MibTableColumn
acFibrechannelEtsCounterTotalFrame = _AcFibrechannelEtsCounterTotalFrame_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 4, 2, 1, 2),
    _AcFibrechannelEtsCounterTotalFrame_Type()
)
acFibrechannelEtsCounterTotalFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelEtsCounterTotalFrame.setStatus("current")
_AcFibrechannelEtsCounterErroredFrame_Type = Counter64
_AcFibrechannelEtsCounterErroredFrame_Object = MibTableColumn
acFibrechannelEtsCounterErroredFrame = _AcFibrechannelEtsCounterErroredFrame_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 4, 2, 1, 3),
    _AcFibrechannelEtsCounterErroredFrame_Type()
)
acFibrechannelEtsCounterErroredFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelEtsCounterErroredFrame.setStatus("current")
_AcFibrechannelEtsCounterDiscardFrame_Type = Counter64
_AcFibrechannelEtsCounterDiscardFrame_Object = MibTableColumn
acFibrechannelEtsCounterDiscardFrame = _AcFibrechannelEtsCounterDiscardFrame_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 4, 2, 1, 4),
    _AcFibrechannelEtsCounterDiscardFrame_Type()
)
acFibrechannelEtsCounterDiscardFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelEtsCounterDiscardFrame.setStatus("current")
_AcFibrechannelEtsCounterLossofSync_Type = Counter64
_AcFibrechannelEtsCounterLossofSync_Object = MibTableColumn
acFibrechannelEtsCounterLossofSync = _AcFibrechannelEtsCounterLossofSync_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 4, 2, 1, 5),
    _AcFibrechannelEtsCounterLossofSync_Type()
)
acFibrechannelEtsCounterLossofSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelEtsCounterLossofSync.setStatus("current")
_AcFibrechannelEtsCounterLineError_Type = Counter64
_AcFibrechannelEtsCounterLineError_Object = MibTableColumn
acFibrechannelEtsCounterLineError = _AcFibrechannelEtsCounterLineError_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 4, 2, 1, 6),
    _AcFibrechannelEtsCounterLineError_Type()
)
acFibrechannelEtsCounterLineError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelEtsCounterLineError.setStatus("current")
_AcFibrechannelEtsCounterFCSError_Type = Counter64
_AcFibrechannelEtsCounterFCSError_Object = MibTableColumn
acFibrechannelEtsCounterFCSError = _AcFibrechannelEtsCounterFCSError_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 4, 2, 1, 7),
    _AcFibrechannelEtsCounterFCSError_Type()
)
acFibrechannelEtsCounterFCSError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelEtsCounterFCSError.setStatus("current")
_AcFibrechannelEtsCounterCheckError_Type = Counter64
_AcFibrechannelEtsCounterCheckError_Object = MibTableColumn
acFibrechannelEtsCounterCheckError = _AcFibrechannelEtsCounterCheckError_Object(
    (1, 3, 6, 1, 4, 1, 13458, 1, 6, 5, 4, 2, 1, 8),
    _AcFibrechannelEtsCounterCheckError_Type()
)
acFibrechannelEtsCounterCheckError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFibrechannelEtsCounterCheckError.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATMEDIA-MIB",
    **{"DisplayString": DisplayString,
       "atmedia": atmedia,
       "atmcrypt": atmcrypt,
       "acMachine": acMachine,
       "acProductID": acProductID,
       "acSerialNumber": acSerialNumber,
       "acHostname": acHostname,
       "acContact": acContact,
       "acLocation": acLocation,
       "acDescr": acDescr,
       "acSoftware": acSoftware,
       "acSoftVersion": acSoftVersion,
       "acSoftDescr": acSoftDescr,
       "acHardware": acHardware,
       "acHardVersion": acHardVersion,
       "acHardDescr": acHardDescr,
       "acInterfaces": acInterfaces,
       "acIfNumber": acIfNumber,
       "acIfTable": acIfTable,
       "acIfEntry": acIfEntry,
       "acIfIndex": acIfIndex,
       "acIfDescr": acIfDescr,
       "acIfPhyType": acIfPhyType,
       "acIfSpeed": acIfSpeed,
       "acIfRevision": acIfRevision,
       "acEncryptors": acEncryptors,
       "acEcNumber": acEcNumber,
       "acEcTable": acEcTable,
       "acEcEntry": acEcEntry,
       "acEcIndex": acEcIndex,
       "acEcDescr": acEcDescr,
       "acEcRevision": acEcRevision,
       "acStatus": acStatus,
       "acInterfaceStatus": acInterfaceStatus,
       "acInterfaceStatusNumber": acInterfaceStatusNumber,
       "acInterfaceStatusTable": acInterfaceStatusTable,
       "acInterfaceStatusEntry": acInterfaceStatusEntry,
       "acInterfaceStatusIndex": acInterfaceStatusIndex,
       "acInterfaceStatusState": acInterfaceStatusState,
       "acInterfaceStatusLastChange": acInterfaceStatusLastChange,
       "acInterfaceStatusDescr": acInterfaceStatusDescr,
       "acInterfaceStatusRxCells": acInterfaceStatusRxCells,
       "acInterfaceStatusTxCells": acInterfaceStatusTxCells,
       "acInterfaceStatusRxBytes": acInterfaceStatusRxBytes,
       "acInterfaceStatusTxBytes": acInterfaceStatusTxBytes,
       "acInterfaceStatusRxRate": acInterfaceStatusRxRate,
       "acInterfaceStatusTxRate": acInterfaceStatusTxRate,
       "acEncryptorStatus": acEncryptorStatus,
       "acEncryptorStatusNumber": acEncryptorStatusNumber,
       "acEncryptorStatusTable": acEncryptorStatusTable,
       "acEncryptorStatusEntry": acEncryptorStatusEntry,
       "acEncryptorStatusIndex": acEncryptorStatusIndex,
       "acEncryptorStatusState": acEncryptorStatusState,
       "acEncryptorStatusLastChange": acEncryptorStatusLastChange,
       "acEncryptorStatusDescr": acEncryptorStatusDescr,
       "acMaintenance": acMaintenance,
       "acMaUptime": acMaUptime,
       "acMaLastBoot": acMaLastBoot,
       "acMaSystime": acMaSystime,
       "acMaTemperature": acMaTemperature,
       "acMaCpuTemperature1": acMaCpuTemperature1,
       "acMaCpuTemperature2": acMaCpuTemperature2,
       "acMaFanSpeed1": acMaFanSpeed1,
       "acMaFanSpeed2": acMaFanSpeed2,
       "acMaFanSpeed3": acMaFanSpeed3,
       "acMaFanSpeed4": acMaFanSpeed4,
       "acMaPowerState": acMaPowerState,
       "acMaPowerLastChange": acMaPowerLastChange,
       "acTransmission": acTransmission,
       "acSonet": acSonet,
       "acSonetStatus": acSonetStatus,
       "acSonetStatusNumber": acSonetStatusNumber,
       "acSonetStatusTable": acSonetStatusTable,
       "acSonetStatusEntry": acSonetStatusEntry,
       "acSonetStatusIndex": acSonetStatusIndex,
       "acSonetStatusState": acSonetStatusState,
       "acSonetStatusLOS": acSonetStatusLOS,
       "acSonetStatusOOF": acSonetStatusOOF,
       "acSonetStatusLOC": acSonetStatusLOC,
       "acSonetStatusLineAIS": acSonetStatusLineAIS,
       "acSonetStatusLineRDI": acSonetStatusLineRDI,
       "acSonetStatusPathAIS": acSonetStatusPathAIS,
       "acSonetStatusPathYellow": acSonetStatusPathYellow,
       "acSonetStatusCustom": acSonetStatusCustom,
       "acSonetStatusDescr": acSonetStatusDescr,
       "acSonetAlarms": acSonetAlarms,
       "acSonetAlarmsNumber": acSonetAlarmsNumber,
       "acSonetAlarmsTable": acSonetAlarmsTable,
       "acSonetAlarmsEntry": acSonetAlarmsEntry,
       "acSonetAlarmsIndex": acSonetAlarmsIndex,
       "acSonetAlarmsLOS": acSonetAlarmsLOS,
       "acSonetAlarmsLineAIS": acSonetAlarmsLineAIS,
       "acSonetAlarmsLineRDI": acSonetAlarmsLineRDI,
       "acSonetAlarmsPathAIS": acSonetAlarmsPathAIS,
       "acSonetAlarmsPathYellow": acSonetAlarmsPathYellow,
       "acSonetErrCounter": acSonetErrCounter,
       "acSonetErrCounterNumber": acSonetErrCounterNumber,
       "acSonetErrCounterTable": acSonetErrCounterTable,
       "acSonetErrCounterEntry": acSonetErrCounterEntry,
       "acSonetErrCounterIndex": acSonetErrCounterIndex,
       "acSonetErrCounterOOF": acSonetErrCounterOOF,
       "acSonetErrCounterLOC": acSonetErrCounterLOC,
       "acSonetErrCounterB1BIP": acSonetErrCounterB1BIP,
       "acSonetErrCounterB2BIP": acSonetErrCounterB2BIP,
       "acSonetErrCounterB3BIP": acSonetErrCounterB3BIP,
       "acSonetErrCounterLineFEBE": acSonetErrCounterLineFEBE,
       "acSonetErrCounterPathFEBE": acSonetErrCounterPathFEBE,
       "acSonetErrCounterHEC": acSonetErrCounterHEC,
       "acSonetEtsCounter": acSonetEtsCounter,
       "acSonetEtsCounterNumber": acSonetEtsCounterNumber,
       "acSonetEtsCounterTable": acSonetEtsCounterTable,
       "acSonetEtsCounterEntry": acSonetEtsCounterEntry,
       "acSonetEtsCounterIndex": acSonetEtsCounterIndex,
       "acSonetEtsCounterOOF": acSonetEtsCounterOOF,
       "acSonetEtsCounterLOC": acSonetEtsCounterLOC,
       "acSonetEtsCounterB1BIP": acSonetEtsCounterB1BIP,
       "acSonetEtsCounterB2BIP": acSonetEtsCounterB2BIP,
       "acSonetEtsCounterB3BIP": acSonetEtsCounterB3BIP,
       "acSonetEtsCounterLineFEBE": acSonetEtsCounterLineFEBE,
       "acSonetEtsCounterPathFEBE": acSonetEtsCounterPathFEBE,
       "acSonetEtsCounterHEC": acSonetEtsCounterHEC,
       "acE3": acE3,
       "acE3Status": acE3Status,
       "acE3StatusNumber": acE3StatusNumber,
       "acE3StatusTable": acE3StatusTable,
       "acE3StatusEntry": acE3StatusEntry,
       "acE3StatusIndex": acE3StatusIndex,
       "acE3StatusState": acE3StatusState,
       "acE3StatusLOS": acE3StatusLOS,
       "acE3StatusOOF": acE3StatusOOF,
       "acE3StatusLOC": acE3StatusLOC,
       "acE3StatusAIS": acE3StatusAIS,
       "acE3StatusMAFERF": acE3StatusMAFERF,
       "acE3StatusCustom": acE3StatusCustom,
       "acE3StatusDescr": acE3StatusDescr,
       "acE3Alarms": acE3Alarms,
       "acE3AlarmsNumber": acE3AlarmsNumber,
       "acE3AlarmsTable": acE3AlarmsTable,
       "acE3AlarmsEntry": acE3AlarmsEntry,
       "acE3AlarmsIndex": acE3AlarmsIndex,
       "acE3AlarmsLOS": acE3AlarmsLOS,
       "acE3AlarmsAIS": acE3AlarmsAIS,
       "acE3AlarmsMAFERF": acE3AlarmsMAFERF,
       "acE3ErrCounter": acE3ErrCounter,
       "acE3ErrCounterNumber": acE3ErrCounterNumber,
       "acE3ErrCounterTable": acE3ErrCounterTable,
       "acE3ErrCounterEntry": acE3ErrCounterEntry,
       "acE3ErrCounterIndex": acE3ErrCounterIndex,
       "acE3ErrCounterLCV": acE3ErrCounterLCV,
       "acE3ErrCounterOOF": acE3ErrCounterOOF,
       "acE3ErrCounterLOC": acE3ErrCounterLOC,
       "acE3ErrCounterBIP": acE3ErrCounterBIP,
       "acE3ErrCounterMAFEBE": acE3ErrCounterMAFEBE,
       "acE3ErrCounterHEC": acE3ErrCounterHEC,
       "acE3EtsCounter": acE3EtsCounter,
       "acE3EtsCounterNumber": acE3EtsCounterNumber,
       "acE3EtsCounterTable": acE3EtsCounterTable,
       "acE3EtsCounterEntry": acE3EtsCounterEntry,
       "acE3EtsCounterIndex": acE3EtsCounterIndex,
       "acE3EtsCounterLCV": acE3EtsCounterLCV,
       "acE3EtsCounterOOF": acE3EtsCounterOOF,
       "acE3EtsCounterLOC": acE3EtsCounterLOC,
       "acE3EtsCounterBIP": acE3EtsCounterBIP,
       "acE3EtsCounterMAFEBE": acE3EtsCounterMAFEBE,
       "acE3EtsCounterHEC": acE3EtsCounterHEC,
       "acE1": acE1,
       "acE1Status": acE1Status,
       "acE1Alarms": acE1Alarms,
       "acE1ErrCounter": acE1ErrCounter,
       "acE1EtsCounter": acE1EtsCounter,
       "acGigabit": acGigabit,
       "acGigabitStatus": acGigabitStatus,
       "acGigabitStatusNumber": acGigabitStatusNumber,
       "acGigabitStatusTable": acGigabitStatusTable,
       "acGigabitStatusEntry": acGigabitStatusEntry,
       "acGigabitStatusIndex": acGigabitStatusIndex,
       "acGigabitStatusState": acGigabitStatusState,
       "acGigabitStatusLOS": acGigabitStatusLOS,
       "acGigabitStatusLossofSync": acGigabitStatusLossofSync,
       "acGigabitStatusLinkDown": acGigabitStatusLinkDown,
       "acGigabitStatusCustom": acGigabitStatusCustom,
       "acGigabitStatusDescr": acGigabitStatusDescr,
       "acGigabitAlarms": acGigabitAlarms,
       "acGigabitAlarmsNumber": acGigabitAlarmsNumber,
       "acGigabitAlarmsTable": acGigabitAlarmsTable,
       "acGigabitAlarmsEntry": acGigabitAlarmsEntry,
       "acGigabitAlarmsIndex": acGigabitAlarmsIndex,
       "acGigabitAlarmsLOS": acGigabitAlarmsLOS,
       "acGigabitAlarmsLinkDown": acGigabitAlarmsLinkDown,
       "acGigabitErrCounter": acGigabitErrCounter,
       "acGigabitErrCounterNumber": acGigabitErrCounterNumber,
       "acGigabitErrCounterTable": acGigabitErrCounterTable,
       "acGigabitErrCounterEntry": acGigabitErrCounterEntry,
       "acGigabitErrCounterIndex": acGigabitErrCounterIndex,
       "acGigabitErrCounterTotalFrame": acGigabitErrCounterTotalFrame,
       "acGigabitErrCounterErroredFrame": acGigabitErrCounterErroredFrame,
       "acGigabitErrCounterFalseCarrier": acGigabitErrCounterFalseCarrier,
       "acGigabitErrCounterLossofSync": acGigabitErrCounterLossofSync,
       "acGigabitErrCounterLineError": acGigabitErrCounterLineError,
       "acGigabitEtsCounter": acGigabitEtsCounter,
       "acGigabitEtsCounterNumber": acGigabitEtsCounterNumber,
       "acGigabitEtsCounterTable": acGigabitEtsCounterTable,
       "acGigabitEtsCounterEntry": acGigabitEtsCounterEntry,
       "acGigabitEtsCounterIndex": acGigabitEtsCounterIndex,
       "acGigabitEtsCounterTotalFrame": acGigabitEtsCounterTotalFrame,
       "acGigabitEtsCounterErroredFrame": acGigabitEtsCounterErroredFrame,
       "acGigabitEtsCounterFalseCarrier": acGigabitEtsCounterFalseCarrier,
       "acGigabitEtsCounterLossofSync": acGigabitEtsCounterLossofSync,
       "acGigabitEtsCounterLineError": acGigabitEtsCounterLineError,
       "acFibrechannel": acFibrechannel,
       "acFibrechannelStatus": acFibrechannelStatus,
       "acFibrechannelStatusNumber": acFibrechannelStatusNumber,
       "acFibrechannelStatusTable": acFibrechannelStatusTable,
       "acFibrechannelStatusEntry": acFibrechannelStatusEntry,
       "acFibrechannelStatusIndex": acFibrechannelStatusIndex,
       "acFibrechannelStatusState": acFibrechannelStatusState,
       "acFibrechannelStatusLOS": acFibrechannelStatusLOS,
       "acFibrechannelStatusLossofSync": acFibrechannelStatusLossofSync,
       "acFibrechannelStatusLinkDown": acFibrechannelStatusLinkDown,
       "acFibrechannelStatusCustom": acFibrechannelStatusCustom,
       "acFibrechannelStatusDescr": acFibrechannelStatusDescr,
       "acFibrechannelAlarms": acFibrechannelAlarms,
       "acFibrechannelAlarmsNumber": acFibrechannelAlarmsNumber,
       "acFibrechannelAlarmsTable": acFibrechannelAlarmsTable,
       "acFibrechannelAlarmsEntry": acFibrechannelAlarmsEntry,
       "acFibrechannelAlarmsIndex": acFibrechannelAlarmsIndex,
       "acFibrechannelAlarmsLOS": acFibrechannelAlarmsLOS,
       "acFibrechannelAlarmsLinkDown": acFibrechannelAlarmsLinkDown,
       "acFibrechannelErrCounter": acFibrechannelErrCounter,
       "acFibrechannelErrCounterNumber": acFibrechannelErrCounterNumber,
       "acFibrechannelErrCounterTable": acFibrechannelErrCounterTable,
       "acFibrechannelErrCounterEntry": acFibrechannelErrCounterEntry,
       "acFibrechannelErrCounterIndex": acFibrechannelErrCounterIndex,
       "acFibrechannelErrCounterTotalFrame": acFibrechannelErrCounterTotalFrame,
       "acFibrechannelErrCounterErroredFrame": acFibrechannelErrCounterErroredFrame,
       "acFibrechannelErrCounterDiscardFrame": acFibrechannelErrCounterDiscardFrame,
       "acFibrechannelErrCounterLossofSync": acFibrechannelErrCounterLossofSync,
       "acFibrechannelErrCounterLineError": acFibrechannelErrCounterLineError,
       "acFibrechannelErrCounterFCSError": acFibrechannelErrCounterFCSError,
       "acFibrechannelErrCounterCheckError": acFibrechannelErrCounterCheckError,
       "acFibrechannelEtsCounter": acFibrechannelEtsCounter,
       "acFibrechannelEtsCounterNumber": acFibrechannelEtsCounterNumber,
       "acFibrechannelEtsCounterTable": acFibrechannelEtsCounterTable,
       "acFibrechannelEtsCounterEntry": acFibrechannelEtsCounterEntry,
       "acFibrechannelEtsCounterIndex": acFibrechannelEtsCounterIndex,
       "acFibrechannelEtsCounterTotalFrame": acFibrechannelEtsCounterTotalFrame,
       "acFibrechannelEtsCounterErroredFrame": acFibrechannelEtsCounterErroredFrame,
       "acFibrechannelEtsCounterDiscardFrame": acFibrechannelEtsCounterDiscardFrame,
       "acFibrechannelEtsCounterLossofSync": acFibrechannelEtsCounterLossofSync,
       "acFibrechannelEtsCounterLineError": acFibrechannelEtsCounterLineError,
       "acFibrechannelEtsCounterFCSError": acFibrechannelEtsCounterFCSError,
       "acFibrechannelEtsCounterCheckError": acFibrechannelEtsCounterCheckError}
)
