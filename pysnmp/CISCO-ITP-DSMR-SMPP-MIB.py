# SNMP MIB module (CISCO-ITP-DSMR-SMPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-DSMR-SMPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:17 2024
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

(cgspCLLICode,
 cgspEventSequenceNumber,
 cgspInstNetwork) = mibBuilder.importSymbols(
    "CISCO-ITP-GSP-MIB",
    "cgspCLLICode",
    "cgspEventSequenceNumber",
    "cgspInstNetwork")

(CmlrName,) = mibBuilder.importSymbols(
    "CISCO-ITP-MLR-MIB",
    "CmlrName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoItpDsmrSmppMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301)
)
ciscoItpDsmrSmppMIB.setRevisions(
        ("2005-05-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CdsmrSmppInactivityTimer(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 9000000),
    )



class CdsmrSmppResponseTimer(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 10000),
    )



class CdsmrSmppSendWindow(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )



class CdsmrSmppSessionInitTimer(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(500, 120000),
    )



class CdsmrSmppBindType(Integer32, TextualConvention):
    status = "current"
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
        *(("any", 2),
          ("none", 1),
          ("receiver", 3),
          ("transceiver", 4),
          ("transmitter", 5))
    )



class CdsmrSmppKeepaliveTimer(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(500, 120000),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoItpDsmrSmppMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoItpDsmrSmppMIBNotifs = _CiscoItpDsmrSmppMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 0)
)
_CiscoItpDsmrSmppMIBObjects_ObjectIdentity = ObjectIdentity
ciscoItpDsmrSmppMIBObjects = _CiscoItpDsmrSmppMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1)
)
_CdsmrSmppScalars_ObjectIdentity = ObjectIdentity
cdsmrSmppScalars = _CdsmrSmppScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 0)
)


class _CdsmrSmppSessionStateNotifEnable_Type(TruthValue):
    """Custom type cdsmrSmppSessionStateNotifEnable based on TruthValue"""


_CdsmrSmppSessionStateNotifEnable_Object = MibScalar
cdsmrSmppSessionStateNotifEnable = _CdsmrSmppSessionStateNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 0, 1),
    _CdsmrSmppSessionStateNotifEnable_Type()
)
cdsmrSmppSessionStateNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsmrSmppSessionStateNotifEnable.setStatus("current")
_CdsmrSmppProfileTable_Object = MibTable
cdsmrSmppProfileTable = _CdsmrSmppProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 2)
)
if mibBuilder.loadTexts:
    cdsmrSmppProfileTable.setStatus("current")
_CdsmrSmppProfileTableEntry_Object = MibTableRow
cdsmrSmppProfileTableEntry = _CdsmrSmppProfileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 2, 1)
)
cdsmrSmppProfileTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppProfileName"),
)
if mibBuilder.loadTexts:
    cdsmrSmppProfileTableEntry.setStatus("current")
_CdsmrSmppProfileName_Type = CmlrName
_CdsmrSmppProfileName_Object = MibTableColumn
cdsmrSmppProfileName = _CdsmrSmppProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 2, 1, 1),
    _CdsmrSmppProfileName_Type()
)
cdsmrSmppProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmrSmppProfileName.setStatus("current")
_CdsmrSmppProfileBindType_Type = CdsmrSmppBindType
_CdsmrSmppProfileBindType_Object = MibTableColumn
cdsmrSmppProfileBindType = _CdsmrSmppProfileBindType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 2, 1, 2),
    _CdsmrSmppProfileBindType_Type()
)
cdsmrSmppProfileBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppProfileBindType.setStatus("current")
_CdsmrSmppProfileInactivityTimer_Type = CdsmrSmppInactivityTimer
_CdsmrSmppProfileInactivityTimer_Object = MibTableColumn
cdsmrSmppProfileInactivityTimer = _CdsmrSmppProfileInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 2, 1, 3),
    _CdsmrSmppProfileInactivityTimer_Type()
)
cdsmrSmppProfileInactivityTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppProfileInactivityTimer.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrSmppProfileInactivityTimer.setUnits("milliseconds")
_CdsmrSmppProfileKeepaliveTimer_Type = CdsmrSmppKeepaliveTimer
_CdsmrSmppProfileKeepaliveTimer_Object = MibTableColumn
cdsmrSmppProfileKeepaliveTimer = _CdsmrSmppProfileKeepaliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 2, 1, 4),
    _CdsmrSmppProfileKeepaliveTimer_Type()
)
cdsmrSmppProfileKeepaliveTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppProfileKeepaliveTimer.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrSmppProfileKeepaliveTimer.setUnits("milliseconds")
_CdsmrSmppProfileCallingParty_Type = TruthValue
_CdsmrSmppProfileCallingParty_Object = MibTableColumn
cdsmrSmppProfileCallingParty = _CdsmrSmppProfileCallingParty_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 2, 1, 5),
    _CdsmrSmppProfileCallingParty_Type()
)
cdsmrSmppProfileCallingParty.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppProfileCallingParty.setStatus("current")
_CdsmrSmppProfileResponseTimer_Type = CdsmrSmppResponseTimer
_CdsmrSmppProfileResponseTimer_Object = MibTableColumn
cdsmrSmppProfileResponseTimer = _CdsmrSmppProfileResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 2, 1, 6),
    _CdsmrSmppProfileResponseTimer_Type()
)
cdsmrSmppProfileResponseTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppProfileResponseTimer.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrSmppProfileResponseTimer.setUnits("milliseconds")
_CdsmrSmppProfileSendWindow_Type = CdsmrSmppSendWindow
_CdsmrSmppProfileSendWindow_Object = MibTableColumn
cdsmrSmppProfileSendWindow = _CdsmrSmppProfileSendWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 2, 1, 7),
    _CdsmrSmppProfileSendWindow_Type()
)
cdsmrSmppProfileSendWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppProfileSendWindow.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrSmppProfileSendWindow.setUnits("bytes")
_CdsmrSmppProfileSessionInitTimer_Type = CdsmrSmppSessionInitTimer
_CdsmrSmppProfileSessionInitTimer_Object = MibTableColumn
cdsmrSmppProfileSessionInitTimer = _CdsmrSmppProfileSessionInitTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 2, 1, 8),
    _CdsmrSmppProfileSessionInitTimer_Type()
)
cdsmrSmppProfileSessionInitTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppProfileSessionInitTimer.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrSmppProfileSessionInitTimer.setUnits("milliseconds")
_CdsmrSmppProfileRowStatus_Type = RowStatus
_CdsmrSmppProfileRowStatus_Object = MibTableColumn
cdsmrSmppProfileRowStatus = _CdsmrSmppProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 2, 1, 9),
    _CdsmrSmppProfileRowStatus_Type()
)
cdsmrSmppProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppProfileRowStatus.setStatus("current")
_CdsmrSmppSessionTable_Object = MibTable
cdsmrSmppSessionTable = _CdsmrSmppSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 3)
)
if mibBuilder.loadTexts:
    cdsmrSmppSessionTable.setStatus("current")
_CdsmrSmppSessionTableEntry_Object = MibTableRow
cdsmrSmppSessionTableEntry = _CdsmrSmppSessionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 3, 1)
)
cdsmrSmppSessionTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppSessionLocalPortNumber"),
)
if mibBuilder.loadTexts:
    cdsmrSmppSessionTableEntry.setStatus("current")
_CdsmrSmppSessionLocalPortNumber_Type = InetPortNumber
_CdsmrSmppSessionLocalPortNumber_Object = MibTableColumn
cdsmrSmppSessionLocalPortNumber = _CdsmrSmppSessionLocalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 3, 1, 1),
    _CdsmrSmppSessionLocalPortNumber_Type()
)
cdsmrSmppSessionLocalPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmrSmppSessionLocalPortNumber.setStatus("current")
_CdsmrSmppSessionLocalIpAddrType_Type = InetAddressType
_CdsmrSmppSessionLocalIpAddrType_Object = MibTableColumn
cdsmrSmppSessionLocalIpAddrType = _CdsmrSmppSessionLocalIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 3, 1, 2),
    _CdsmrSmppSessionLocalIpAddrType_Type()
)
cdsmrSmppSessionLocalIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppSessionLocalIpAddrType.setStatus("current")
_CdsmrSmppSessionLocalIpAddress_Type = InetAddress
_CdsmrSmppSessionLocalIpAddress_Object = MibTableColumn
cdsmrSmppSessionLocalIpAddress = _CdsmrSmppSessionLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 3, 1, 3),
    _CdsmrSmppSessionLocalIpAddress_Type()
)
cdsmrSmppSessionLocalIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppSessionLocalIpAddress.setStatus("current")
_CdsmrSmppSessionDynamicDest_Type = TruthValue
_CdsmrSmppSessionDynamicDest_Object = MibTableColumn
cdsmrSmppSessionDynamicDest = _CdsmrSmppSessionDynamicDest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 3, 1, 4),
    _CdsmrSmppSessionDynamicDest_Type()
)
cdsmrSmppSessionDynamicDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppSessionDynamicDest.setStatus("current")
_CdsmrSmppSessionRowStatus_Type = RowStatus
_CdsmrSmppSessionRowStatus_Object = MibTableColumn
cdsmrSmppSessionRowStatus = _CdsmrSmppSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 3, 1, 5),
    _CdsmrSmppSessionRowStatus_Type()
)
cdsmrSmppSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppSessionRowStatus.setStatus("current")
_CdsmrSmppDestTable_Object = MibTable
cdsmrSmppDestTable = _CdsmrSmppDestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4)
)
if mibBuilder.loadTexts:
    cdsmrSmppDestTable.setStatus("current")
_CdsmrSmppDestTableEntry_Object = MibTableRow
cdsmrSmppDestTableEntry = _CdsmrSmppDestTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1)
)
cdsmrSmppDestTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppSessionLocalPortNumber"),
    (0, "CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestName"),
)
if mibBuilder.loadTexts:
    cdsmrSmppDestTableEntry.setStatus("current")
_CdsmrSmppDestName_Type = CmlrName
_CdsmrSmppDestName_Object = MibTableColumn
cdsmrSmppDestName = _CdsmrSmppDestName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 1),
    _CdsmrSmppDestName_Type()
)
cdsmrSmppDestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmrSmppDestName.setStatus("current")
_CdsmrSmppDestBindType_Type = CdsmrSmppBindType
_CdsmrSmppDestBindType_Object = MibTableColumn
cdsmrSmppDestBindType = _CdsmrSmppDestBindType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 2),
    _CdsmrSmppDestBindType_Type()
)
cdsmrSmppDestBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppDestBindType.setStatus("current")
_CdsmrSmppDestInactivityTimer_Type = CdsmrSmppInactivityTimer
_CdsmrSmppDestInactivityTimer_Object = MibTableColumn
cdsmrSmppDestInactivityTimer = _CdsmrSmppDestInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 3),
    _CdsmrSmppDestInactivityTimer_Type()
)
cdsmrSmppDestInactivityTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppDestInactivityTimer.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrSmppDestInactivityTimer.setUnits("milliseconds")
_CdsmrSmppDestKeepaliveTimer_Type = CdsmrSmppKeepaliveTimer
_CdsmrSmppDestKeepaliveTimer_Object = MibTableColumn
cdsmrSmppDestKeepaliveTimer = _CdsmrSmppDestKeepaliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 4),
    _CdsmrSmppDestKeepaliveTimer_Type()
)
cdsmrSmppDestKeepaliveTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppDestKeepaliveTimer.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrSmppDestKeepaliveTimer.setUnits("milliseconds")
_CdsmrSmppDestCallingParty_Type = TruthValue
_CdsmrSmppDestCallingParty_Object = MibTableColumn
cdsmrSmppDestCallingParty = _CdsmrSmppDestCallingParty_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 5),
    _CdsmrSmppDestCallingParty_Type()
)
cdsmrSmppDestCallingParty.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppDestCallingParty.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrSmppDestCallingParty.setUnits("milliseconds")
_CdsmrSmppDestResponseTimer_Type = CdsmrSmppResponseTimer
_CdsmrSmppDestResponseTimer_Object = MibTableColumn
cdsmrSmppDestResponseTimer = _CdsmrSmppDestResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 6),
    _CdsmrSmppDestResponseTimer_Type()
)
cdsmrSmppDestResponseTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppDestResponseTimer.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrSmppDestResponseTimer.setUnits("milliseconds")
_CdsmrSmppDestSendWindow_Type = CdsmrSmppSendWindow
_CdsmrSmppDestSendWindow_Object = MibTableColumn
cdsmrSmppDestSendWindow = _CdsmrSmppDestSendWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 7),
    _CdsmrSmppDestSendWindow_Type()
)
cdsmrSmppDestSendWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppDestSendWindow.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrSmppDestSendWindow.setUnits("bytes")
_CdsmrSmppDestSessionInitTimer_Type = CdsmrSmppSessionInitTimer
_CdsmrSmppDestSessionInitTimer_Object = MibTableColumn
cdsmrSmppDestSessionInitTimer = _CdsmrSmppDestSessionInitTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 8),
    _CdsmrSmppDestSessionInitTimer_Type()
)
cdsmrSmppDestSessionInitTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppDestSessionInitTimer.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrSmppDestSessionInitTimer.setUnits("milliseconds")
_CdsmrSmppDestRemotePortNumber_Type = InetPortNumber
_CdsmrSmppDestRemotePortNumber_Object = MibTableColumn
cdsmrSmppDestRemotePortNumber = _CdsmrSmppDestRemotePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 9),
    _CdsmrSmppDestRemotePortNumber_Type()
)
cdsmrSmppDestRemotePortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppDestRemotePortNumber.setStatus("current")
_CdsmrSmppDestRemoteIpAddrType_Type = InetAddressType
_CdsmrSmppDestRemoteIpAddrType_Object = MibTableColumn
cdsmrSmppDestRemoteIpAddrType = _CdsmrSmppDestRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 10),
    _CdsmrSmppDestRemoteIpAddrType_Type()
)
cdsmrSmppDestRemoteIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppDestRemoteIpAddrType.setStatus("current")
_CdsmrSmppDestRemoteIpAddress_Type = InetAddress
_CdsmrSmppDestRemoteIpAddress_Object = MibTableColumn
cdsmrSmppDestRemoteIpAddress = _CdsmrSmppDestRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 11),
    _CdsmrSmppDestRemoteIpAddress_Type()
)
cdsmrSmppDestRemoteIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppDestRemoteIpAddress.setStatus("current")
_CdsmrSmppDestProfileName_Type = CmlrName
_CdsmrSmppDestProfileName_Object = MibTableColumn
cdsmrSmppDestProfileName = _CdsmrSmppDestProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 12),
    _CdsmrSmppDestProfileName_Type()
)
cdsmrSmppDestProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppDestProfileName.setStatus("current")


class _CdsmrSmppDestState_Type(Integer32):
    """Custom type cdsmrSmppDestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("open", 3))
    )


_CdsmrSmppDestState_Type.__name__ = "Integer32"
_CdsmrSmppDestState_Object = MibTableColumn
cdsmrSmppDestState = _CdsmrSmppDestState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 13),
    _CdsmrSmppDestState_Type()
)
cdsmrSmppDestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrSmppDestState.setStatus("current")
_CdsmrSmppDestSentRequests_Type = Counter32
_CdsmrSmppDestSentRequests_Object = MibTableColumn
cdsmrSmppDestSentRequests = _CdsmrSmppDestSentRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 14),
    _CdsmrSmppDestSentRequests_Type()
)
cdsmrSmppDestSentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrSmppDestSentRequests.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrSmppDestSentRequests.setUnits("requests")
_CdsmrSmppDestRcvdRequests_Type = Counter32
_CdsmrSmppDestRcvdRequests_Object = MibTableColumn
cdsmrSmppDestRcvdRequests = _CdsmrSmppDestRcvdRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 15),
    _CdsmrSmppDestRcvdRequests_Type()
)
cdsmrSmppDestRcvdRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrSmppDestRcvdRequests.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrSmppDestRcvdRequests.setUnits("requests")
_CdsmrSmppDestSentResponses_Type = Counter32
_CdsmrSmppDestSentResponses_Object = MibTableColumn
cdsmrSmppDestSentResponses = _CdsmrSmppDestSentResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 16),
    _CdsmrSmppDestSentResponses_Type()
)
cdsmrSmppDestSentResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrSmppDestSentResponses.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrSmppDestSentResponses.setUnits("responses")
_CdsmrSmppDestRcvdResponses_Type = Counter32
_CdsmrSmppDestRcvdResponses_Object = MibTableColumn
cdsmrSmppDestRcvdResponses = _CdsmrSmppDestRcvdResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 17),
    _CdsmrSmppDestRcvdResponses_Type()
)
cdsmrSmppDestRcvdResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrSmppDestRcvdResponses.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrSmppDestRcvdResponses.setUnits("responses")
_CdsmrSmppDestRowStatus_Type = RowStatus
_CdsmrSmppDestRowStatus_Object = MibTableColumn
cdsmrSmppDestRowStatus = _CdsmrSmppDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 1, 4, 1, 18),
    _CdsmrSmppDestRowStatus_Type()
)
cdsmrSmppDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrSmppDestRowStatus.setStatus("current")
_CiscoItpDsmrSmppMIBConform_ObjectIdentity = ObjectIdentity
ciscoItpDsmrSmppMIBConform = _CiscoItpDsmrSmppMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 2)
)
_CiscoItpDsmrSmppMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoItpDsmrSmppMIBCompliances = _CiscoItpDsmrSmppMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 2, 1)
)
_CiscoItpDsmrSmppMIBGroups_ObjectIdentity = ObjectIdentity
ciscoItpDsmrSmppMIBGroups = _CiscoItpDsmrSmppMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 2, 2)
)

# Managed Objects groups

ciscoItpDsmrSmppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 2, 2, 1)
)
ciscoItpDsmrSmppGroup.setObjects(
      *(("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppSessionStateNotifEnable"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppProfileBindType"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppProfileInactivityTimer"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppProfileKeepaliveTimer"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppProfileCallingParty"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppProfileResponseTimer"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppProfileSendWindow"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppProfileSessionInitTimer"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppProfileRowStatus"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppSessionLocalIpAddrType"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppSessionLocalIpAddress"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppSessionDynamicDest"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppSessionRowStatus"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestBindType"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestInactivityTimer"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestKeepaliveTimer"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestCallingParty"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestResponseTimer"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestSendWindow"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestRemotePortNumber"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestSessionInitTimer"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestRemoteIpAddrType"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestRemoteIpAddress"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestProfileName"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestState"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestSentRequests"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestRcvdRequests"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestSentResponses"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestRcvdResponses"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoItpDsmrSmppGroup.setStatus("current")


# Notification objects

ciscoItpDsmrSmppSessionState = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 0, 1)
)
ciscoItpDsmrSmppSessionState.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-DSMR-SMPP-MIB", "cdsmrSmppDestState"))
)
if mibBuilder.loadTexts:
    ciscoItpDsmrSmppSessionState.setStatus(
        "current"
    )


# Notifications groups

ciscoItpDsmrSmppNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 2, 2, 2)
)
ciscoItpDsmrSmppNotificationsGroup.setObjects(
    ("CISCO-ITP-DSMR-SMPP-MIB", "ciscoItpDsmrSmppSessionState")
)
if mibBuilder.loadTexts:
    ciscoItpDsmrSmppNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoItpDsmrSmppMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 1301, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoItpDsmrSmppMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-DSMR-SMPP-MIB",
    **{"CdsmrSmppInactivityTimer": CdsmrSmppInactivityTimer,
       "CdsmrSmppResponseTimer": CdsmrSmppResponseTimer,
       "CdsmrSmppSendWindow": CdsmrSmppSendWindow,
       "CdsmrSmppSessionInitTimer": CdsmrSmppSessionInitTimer,
       "CdsmrSmppBindType": CdsmrSmppBindType,
       "CdsmrSmppKeepaliveTimer": CdsmrSmppKeepaliveTimer,
       "ciscoItpDsmrSmppMIB": ciscoItpDsmrSmppMIB,
       "ciscoItpDsmrSmppMIBNotifs": ciscoItpDsmrSmppMIBNotifs,
       "ciscoItpDsmrSmppSessionState": ciscoItpDsmrSmppSessionState,
       "ciscoItpDsmrSmppMIBObjects": ciscoItpDsmrSmppMIBObjects,
       "cdsmrSmppScalars": cdsmrSmppScalars,
       "cdsmrSmppSessionStateNotifEnable": cdsmrSmppSessionStateNotifEnable,
       "cdsmrSmppProfileTable": cdsmrSmppProfileTable,
       "cdsmrSmppProfileTableEntry": cdsmrSmppProfileTableEntry,
       "cdsmrSmppProfileName": cdsmrSmppProfileName,
       "cdsmrSmppProfileBindType": cdsmrSmppProfileBindType,
       "cdsmrSmppProfileInactivityTimer": cdsmrSmppProfileInactivityTimer,
       "cdsmrSmppProfileKeepaliveTimer": cdsmrSmppProfileKeepaliveTimer,
       "cdsmrSmppProfileCallingParty": cdsmrSmppProfileCallingParty,
       "cdsmrSmppProfileResponseTimer": cdsmrSmppProfileResponseTimer,
       "cdsmrSmppProfileSendWindow": cdsmrSmppProfileSendWindow,
       "cdsmrSmppProfileSessionInitTimer": cdsmrSmppProfileSessionInitTimer,
       "cdsmrSmppProfileRowStatus": cdsmrSmppProfileRowStatus,
       "cdsmrSmppSessionTable": cdsmrSmppSessionTable,
       "cdsmrSmppSessionTableEntry": cdsmrSmppSessionTableEntry,
       "cdsmrSmppSessionLocalPortNumber": cdsmrSmppSessionLocalPortNumber,
       "cdsmrSmppSessionLocalIpAddrType": cdsmrSmppSessionLocalIpAddrType,
       "cdsmrSmppSessionLocalIpAddress": cdsmrSmppSessionLocalIpAddress,
       "cdsmrSmppSessionDynamicDest": cdsmrSmppSessionDynamicDest,
       "cdsmrSmppSessionRowStatus": cdsmrSmppSessionRowStatus,
       "cdsmrSmppDestTable": cdsmrSmppDestTable,
       "cdsmrSmppDestTableEntry": cdsmrSmppDestTableEntry,
       "cdsmrSmppDestName": cdsmrSmppDestName,
       "cdsmrSmppDestBindType": cdsmrSmppDestBindType,
       "cdsmrSmppDestInactivityTimer": cdsmrSmppDestInactivityTimer,
       "cdsmrSmppDestKeepaliveTimer": cdsmrSmppDestKeepaliveTimer,
       "cdsmrSmppDestCallingParty": cdsmrSmppDestCallingParty,
       "cdsmrSmppDestResponseTimer": cdsmrSmppDestResponseTimer,
       "cdsmrSmppDestSendWindow": cdsmrSmppDestSendWindow,
       "cdsmrSmppDestSessionInitTimer": cdsmrSmppDestSessionInitTimer,
       "cdsmrSmppDestRemotePortNumber": cdsmrSmppDestRemotePortNumber,
       "cdsmrSmppDestRemoteIpAddrType": cdsmrSmppDestRemoteIpAddrType,
       "cdsmrSmppDestRemoteIpAddress": cdsmrSmppDestRemoteIpAddress,
       "cdsmrSmppDestProfileName": cdsmrSmppDestProfileName,
       "cdsmrSmppDestState": cdsmrSmppDestState,
       "cdsmrSmppDestSentRequests": cdsmrSmppDestSentRequests,
       "cdsmrSmppDestRcvdRequests": cdsmrSmppDestRcvdRequests,
       "cdsmrSmppDestSentResponses": cdsmrSmppDestSentResponses,
       "cdsmrSmppDestRcvdResponses": cdsmrSmppDestRcvdResponses,
       "cdsmrSmppDestRowStatus": cdsmrSmppDestRowStatus,
       "ciscoItpDsmrSmppMIBConform": ciscoItpDsmrSmppMIBConform,
       "ciscoItpDsmrSmppMIBCompliances": ciscoItpDsmrSmppMIBCompliances,
       "ciscoItpDsmrSmppMIBCompliance": ciscoItpDsmrSmppMIBCompliance,
       "ciscoItpDsmrSmppMIBGroups": ciscoItpDsmrSmppMIBGroups,
       "ciscoItpDsmrSmppGroup": ciscoItpDsmrSmppGroup,
       "ciscoItpDsmrSmppNotificationsGroup": ciscoItpDsmrSmppNotificationsGroup}
)
