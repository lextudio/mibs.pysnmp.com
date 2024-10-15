# SNMP MIB module (AcAtm) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AcAtm
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:00 2024
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

(AtmAddr,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmAddr")

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
 RowStatus,
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

acAtm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6)
)
acAtm.setRevisions(
        ("2003-10-16 00:00",
         "2006-03-21 10:48")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AudioCodes_ObjectIdentity = ObjectIdentity
audioCodes = _AudioCodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003)
)
_AcRegistrations_ObjectIdentity = ObjectIdentity
acRegistrations = _AcRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 7)
)
_AcGeneric_ObjectIdentity = ObjectIdentity
acGeneric = _AcGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8)
)
_AcProducts_ObjectIdentity = ObjectIdentity
acProducts = _AcProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9)
)
_AcBoardMibs_ObjectIdentity = ObjectIdentity
acBoardMibs = _AcBoardMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10)
)
_AcAtmConfiguration_ObjectIdentity = ObjectIdentity
acAtmConfiguration = _AcAtmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1)
)
_AtmGeneralParams_ObjectIdentity = ObjectIdentity
atmGeneralParams = _AtmGeneralParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 1)
)


class _AtmGeneralParamsAtmDefaultApplicationType_Type(Integer32):
    """Custom type atmGeneralParamsAtmDefaultApplicationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 1),
          ("aal2-i-366-2", 2),
          ("aal2-umts", 3))
    )


_AtmGeneralParamsAtmDefaultApplicationType_Type.__name__ = "Integer32"
_AtmGeneralParamsAtmDefaultApplicationType_Object = MibScalar
atmGeneralParamsAtmDefaultApplicationType = _AtmGeneralParamsAtmDefaultApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 1, 1),
    _AtmGeneralParamsAtmDefaultApplicationType_Type()
)
atmGeneralParamsAtmDefaultApplicationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGeneralParamsAtmDefaultApplicationType.setStatus("current")


class _AtmGeneralParamsAtmTransmissionMode_Type(Integer32):
    """Custom type atmGeneralParamsAtmTransmissionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("sdh", 0),
          ("sonet", 1))
    )


_AtmGeneralParamsAtmTransmissionMode_Type.__name__ = "Integer32"
_AtmGeneralParamsAtmTransmissionMode_Object = MibScalar
atmGeneralParamsAtmTransmissionMode = _AtmGeneralParamsAtmTransmissionMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 1, 2),
    _AtmGeneralParamsAtmTransmissionMode_Type()
)
atmGeneralParamsAtmTransmissionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGeneralParamsAtmTransmissionMode.setStatus("current")
_AtmPort_ObjectIdentity = ObjectIdentity
atmPort = _AtmPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2)
)
_AtmPortTable_Object = MibTable
atmPortTable = _AtmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    atmPortTable.setStatus("current")
_AtmPortEntry_Object = MibTableRow
atmPortEntry = _AtmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1, 1)
)
atmPortEntry.setIndexNames(
    (0, "AcAtm", "atmPortNumber"),
)
if mibBuilder.loadTexts:
    atmPortEntry.setStatus("current")


class _AtmPortAdministrativeState_Type(Integer32):
    """Custom type atmPortAdministrativeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 1),
          ("unlocked", 2))
    )


_AtmPortAdministrativeState_Type.__name__ = "Integer32"
_AtmPortAdministrativeState_Object = MibTableColumn
atmPortAdministrativeState = _AtmPortAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1, 1, 1),
    _AtmPortAdministrativeState_Type()
)
atmPortAdministrativeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortAdministrativeState.setStatus("current")


class _AtmPortOperationalState_Type(Integer32):
    """Custom type atmPortOperationalState based on Integer32"""
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


_AtmPortOperationalState_Type.__name__ = "Integer32"
_AtmPortOperationalState_Object = MibTableColumn
atmPortOperationalState = _AtmPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1, 1, 2),
    _AtmPortOperationalState_Type()
)
atmPortOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortOperationalState.setStatus("current")


class _AtmPortNumber_Type(Integer32):
    """Custom type atmPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port0", 0),
          ("port1", 1),
          ("port2", 2))
    )


_AtmPortNumber_Type.__name__ = "Integer32"
_AtmPortNumber_Object = MibTableColumn
atmPortNumber = _AtmPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1, 1, 3),
    _AtmPortNumber_Type()
)
atmPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortNumber.setStatus("current")


class _AtmPortAdminAddress_Type(AtmAddr):
    """Custom type atmPortAdminAddress based on AtmAddr"""
    subtypeSpec = AtmAddr.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AtmPortAdminAddress_Type.__name__ = "AtmAddr"
_AtmPortAdminAddress_Object = MibTableColumn
atmPortAdminAddress = _AtmPortAdminAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1, 1, 4),
    _AtmPortAdminAddress_Type()
)
atmPortAdminAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortAdminAddress.setStatus("current")


class _AtmPortOperationalAddress_Type(AtmAddr):
    """Custom type atmPortOperationalAddress based on AtmAddr"""
    subtypeSpec = AtmAddr.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AtmPortOperationalAddress_Type.__name__ = "AtmAddr"
_AtmPortOperationalAddress_Object = MibTableColumn
atmPortOperationalAddress = _AtmPortOperationalAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1, 1, 5),
    _AtmPortOperationalAddress_Type()
)
atmPortOperationalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortOperationalAddress.setStatus("current")


class _AtmPortAlarmStatus_Type(Integer32):
    """Custom type atmPortAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ais", 2),
          ("cleared", 0),
          ("los", 1),
          ("rdi", 4))
    )


_AtmPortAlarmStatus_Type.__name__ = "Integer32"
_AtmPortAlarmStatus_Object = MibTableColumn
atmPortAlarmStatus = _AtmPortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1, 1, 6),
    _AtmPortAlarmStatus_Type()
)
atmPortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortAlarmStatus.setStatus("current")


class _AtmPortAddressMode_Type(Integer32):
    """Custom type atmPortAddressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addrModeILMI", 2),
          ("addrModeManual", 1),
          ("addrModeNone", 0))
    )


_AtmPortAddressMode_Type.__name__ = "Integer32"
_AtmPortAddressMode_Object = MibTableColumn
atmPortAddressMode = _AtmPortAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1, 1, 7),
    _AtmPortAddressMode_Type()
)
atmPortAddressMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortAddressMode.setStatus("current")
_AtmRemoteGateway_ObjectIdentity = ObjectIdentity
atmRemoteGateway = _AtmRemoteGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3)
)
_AtmRemoteGatewayTable_Object = MibTable
atmRemoteGatewayTable = _AtmRemoteGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    atmRemoteGatewayTable.setStatus("current")
_AtmRemoteGatewayEntry_Object = MibTableRow
atmRemoteGatewayEntry = _AtmRemoteGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1, 1)
)
atmRemoteGatewayEntry.setIndexNames(
    (0, "AcAtm", "atmRemoteGatewayIndex"),
)
if mibBuilder.loadTexts:
    atmRemoteGatewayEntry.setStatus("current")
_AtmRemoteGatewayRowStatus_Type = RowStatus
_AtmRemoteGatewayRowStatus_Object = MibTableColumn
atmRemoteGatewayRowStatus = _AtmRemoteGatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1, 1, 1),
    _AtmRemoteGatewayRowStatus_Type()
)
atmRemoteGatewayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmRemoteGatewayRowStatus.setStatus("current")


class _AtmRemoteGatewayAction_Type(Integer32):
    """Custom type atmRemoteGatewayAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AtmRemoteGatewayAction_Type.__name__ = "Integer32"
_AtmRemoteGatewayAction_Object = MibTableColumn
atmRemoteGatewayAction = _AtmRemoteGatewayAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1, 1, 2),
    _AtmRemoteGatewayAction_Type()
)
atmRemoteGatewayAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmRemoteGatewayAction.setStatus("current")


class _AtmRemoteGatewayActionResult_Type(Integer32):
    """Custom type atmRemoteGatewayActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AtmRemoteGatewayActionResult_Type.__name__ = "Integer32"
_AtmRemoteGatewayActionResult_Object = MibTableColumn
atmRemoteGatewayActionResult = _AtmRemoteGatewayActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1, 1, 3),
    _AtmRemoteGatewayActionResult_Type()
)
atmRemoteGatewayActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmRemoteGatewayActionResult.setStatus("current")


class _AtmRemoteGatewayIndex_Type(Integer32):
    """Custom type atmRemoteGatewayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AtmRemoteGatewayIndex_Type.__name__ = "Integer32"
_AtmRemoteGatewayIndex_Object = MibTableColumn
atmRemoteGatewayIndex = _AtmRemoteGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1, 1, 4),
    _AtmRemoteGatewayIndex_Type()
)
atmRemoteGatewayIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmRemoteGatewayIndex.setStatus("current")


class _AtmRemoteGatewayName_Type(OctetString):
    """Custom type atmRemoteGatewayName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtmRemoteGatewayName_Type.__name__ = "OctetString"
_AtmRemoteGatewayName_Object = MibTableColumn
atmRemoteGatewayName = _AtmRemoteGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1, 1, 5),
    _AtmRemoteGatewayName_Type()
)
atmRemoteGatewayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmRemoteGatewayName.setStatus("current")


class _AtmRemoteGatewayNSAPAddress_Type(AtmAddr):
    """Custom type atmRemoteGatewayNSAPAddress based on AtmAddr"""
    subtypeSpec = AtmAddr.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AtmRemoteGatewayNSAPAddress_Type.__name__ = "AtmAddr"
_AtmRemoteGatewayNSAPAddress_Object = MibTableColumn
atmRemoteGatewayNSAPAddress = _AtmRemoteGatewayNSAPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1, 1, 6),
    _AtmRemoteGatewayNSAPAddress_Type()
)
atmRemoteGatewayNSAPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmRemoteGatewayNSAPAddress.setStatus("current")


class _AtmRemoteGatewayALCAPInstanceNum_Type(Integer32):
    """Custom type atmRemoteGatewayALCAPInstanceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AtmRemoteGatewayALCAPInstanceNum_Type.__name__ = "Integer32"
_AtmRemoteGatewayALCAPInstanceNum_Object = MibTableColumn
atmRemoteGatewayALCAPInstanceNum = _AtmRemoteGatewayALCAPInstanceNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1, 1, 7),
    _AtmRemoteGatewayALCAPInstanceNum_Type()
)
atmRemoteGatewayALCAPInstanceNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmRemoteGatewayALCAPInstanceNum.setStatus("current")
_Aal2PVC_ObjectIdentity = ObjectIdentity
aal2PVC = _Aal2PVC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4)
)
_Aal2PVCTable_Object = MibTable
aal2PVCTable = _Aal2PVCTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    aal2PVCTable.setStatus("current")
_Aal2PVCEntry_Object = MibTableRow
aal2PVCEntry = _Aal2PVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1)
)
aal2PVCEntry.setIndexNames(
    (0, "AcAtm", "aal2PVCRemoteGatewayIndex"),
    (0, "AcAtm", "aal2PVCVCCIPATHID"),
)
if mibBuilder.loadTexts:
    aal2PVCEntry.setStatus("current")
_Aal2PVCRowStatus_Type = RowStatus
_Aal2PVCRowStatus_Object = MibTableColumn
aal2PVCRowStatus = _Aal2PVCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 1),
    _Aal2PVCRowStatus_Type()
)
aal2PVCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aal2PVCRowStatus.setStatus("current")


class _Aal2PVCAction_Type(Integer32):
    """Custom type aal2PVCAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_Aal2PVCAction_Type.__name__ = "Integer32"
_Aal2PVCAction_Object = MibTableColumn
aal2PVCAction = _Aal2PVCAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 2),
    _Aal2PVCAction_Type()
)
aal2PVCAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2PVCAction.setStatus("current")


class _Aal2PVCActionResult_Type(Integer32):
    """Custom type aal2PVCActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_Aal2PVCActionResult_Type.__name__ = "Integer32"
_Aal2PVCActionResult_Object = MibTableColumn
aal2PVCActionResult = _Aal2PVCActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 3),
    _Aal2PVCActionResult_Type()
)
aal2PVCActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2PVCActionResult.setStatus("current")


class _Aal2PVCRemoteGatewayIndex_Type(Integer32):
    """Custom type aal2PVCRemoteGatewayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Aal2PVCRemoteGatewayIndex_Type.__name__ = "Integer32"
_Aal2PVCRemoteGatewayIndex_Object = MibTableColumn
aal2PVCRemoteGatewayIndex = _Aal2PVCRemoteGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 4),
    _Aal2PVCRemoteGatewayIndex_Type()
)
aal2PVCRemoteGatewayIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2PVCRemoteGatewayIndex.setStatus("current")


class _Aal2PVCVCCIPATHID_Type(Integer32):
    """Custom type aal2PVCVCCIPATHID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_Aal2PVCVCCIPATHID_Type.__name__ = "Integer32"
_Aal2PVCVCCIPATHID_Object = MibTableColumn
aal2PVCVCCIPATHID = _Aal2PVCVCCIPATHID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 5),
    _Aal2PVCVCCIPATHID_Type()
)
aal2PVCVCCIPATHID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2PVCVCCIPATHID.setStatus("current")


class _Aal2PVCPortNumber_Type(Integer32):
    """Custom type aal2PVCPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port0", 0),
          ("port1", 1),
          ("port2", 2))
    )


_Aal2PVCPortNumber_Type.__name__ = "Integer32"
_Aal2PVCPortNumber_Object = MibTableColumn
aal2PVCPortNumber = _Aal2PVCPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 6),
    _Aal2PVCPortNumber_Type()
)
aal2PVCPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2PVCPortNumber.setStatus("current")


class _Aal2PVCVpi_Type(Integer32):
    """Custom type aal2PVCVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Aal2PVCVpi_Type.__name__ = "Integer32"
_Aal2PVCVpi_Object = MibTableColumn
aal2PVCVpi = _Aal2PVCVpi_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 7),
    _Aal2PVCVpi_Type()
)
aal2PVCVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2PVCVpi.setStatus("current")


class _Aal2PVCVci_Type(Integer32):
    """Custom type aal2PVCVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Aal2PVCVci_Type.__name__ = "Integer32"
_Aal2PVCVci_Object = MibTableColumn
aal2PVCVci = _Aal2PVCVci_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 8),
    _Aal2PVCVci_Type()
)
aal2PVCVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2PVCVci.setStatus("current")


class _Aal2PVCMaxNumOfCid_Type(Integer32):
    """Custom type aal2PVCMaxNumOfCid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_Aal2PVCMaxNumOfCid_Type.__name__ = "Integer32"
_Aal2PVCMaxNumOfCid_Object = MibTableColumn
aal2PVCMaxNumOfCid = _Aal2PVCMaxNumOfCid_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 9),
    _Aal2PVCMaxNumOfCid_Type()
)
aal2PVCMaxNumOfCid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2PVCMaxNumOfCid.setStatus("current")


class _Aal2PVCNumOfCidInUse_Type(Integer32):
    """Custom type aal2PVCNumOfCidInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_Aal2PVCNumOfCidInUse_Type.__name__ = "Integer32"
_Aal2PVCNumOfCidInUse_Object = MibTableColumn
aal2PVCNumOfCidInUse = _Aal2PVCNumOfCidInUse_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 10),
    _Aal2PVCNumOfCidInUse_Type()
)
aal2PVCNumOfCidInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2PVCNumOfCidInUse.setStatus("current")


class _Aal2PVCServiceCategory_Type(Integer32):
    """Custom type aal2PVCServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("rtVbr", 2))
    )


_Aal2PVCServiceCategory_Type.__name__ = "Integer32"
_Aal2PVCServiceCategory_Object = MibTableColumn
aal2PVCServiceCategory = _Aal2PVCServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 11),
    _Aal2PVCServiceCategory_Type()
)
aal2PVCServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2PVCServiceCategory.setStatus("current")


class _Aal2PVCPCR_Type(Integer32):
    """Custom type aal2PVCPCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49600),
    )


_Aal2PVCPCR_Type.__name__ = "Integer32"
_Aal2PVCPCR_Object = MibTableColumn
aal2PVCPCR = _Aal2PVCPCR_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 12),
    _Aal2PVCPCR_Type()
)
aal2PVCPCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2PVCPCR.setStatus("current")


class _Aal2PVCSCR_Type(Integer32):
    """Custom type aal2PVCSCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49600),
    )


_Aal2PVCSCR_Type.__name__ = "Integer32"
_Aal2PVCSCR_Object = MibTableColumn
aal2PVCSCR = _Aal2PVCSCR_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 13),
    _Aal2PVCSCR_Type()
)
aal2PVCSCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2PVCSCR.setStatus("current")


class _Aal2PVCMBS_Type(Integer32):
    """Custom type aal2PVCMBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Aal2PVCMBS_Type.__name__ = "Integer32"
_Aal2PVCMBS_Object = MibTableColumn
aal2PVCMBS = _Aal2PVCMBS_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 14),
    _Aal2PVCMBS_Type()
)
aal2PVCMBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2PVCMBS.setStatus("current")
_AtmPortLoopbackConfig_ObjectIdentity = ObjectIdentity
atmPortLoopbackConfig = _AtmPortLoopbackConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5)
)
_AtmPortLoopbackConfigTable_Object = MibTable
atmPortLoopbackConfigTable = _AtmPortLoopbackConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1)
)
if mibBuilder.loadTexts:
    atmPortLoopbackConfigTable.setStatus("current")
_AtmPortLoopbackConfigEntry_Object = MibTableRow
atmPortLoopbackConfigEntry = _AtmPortLoopbackConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1)
)
atmPortLoopbackConfigEntry.setIndexNames(
    (0, "AcAtm", "atmPortLoopbackConfigPortNumber"),
)
if mibBuilder.loadTexts:
    atmPortLoopbackConfigEntry.setStatus("current")


class _AtmPortLoopbackConfigIsUsed_Type(Integer32):
    """Custom type atmPortLoopbackConfigIsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AtmPortLoopbackConfigIsUsed_Type.__name__ = "Integer32"
_AtmPortLoopbackConfigIsUsed_Object = MibTableColumn
atmPortLoopbackConfigIsUsed = _AtmPortLoopbackConfigIsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 1),
    _AtmPortLoopbackConfigIsUsed_Type()
)
atmPortLoopbackConfigIsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLoopbackConfigIsUsed.setStatus("current")


class _AtmPortLoopbackConfigAction_Type(Integer32):
    """Custom type atmPortLoopbackConfigAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AtmPortLoopbackConfigAction_Type.__name__ = "Integer32"
_AtmPortLoopbackConfigAction_Object = MibTableColumn
atmPortLoopbackConfigAction = _AtmPortLoopbackConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 2),
    _AtmPortLoopbackConfigAction_Type()
)
atmPortLoopbackConfigAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortLoopbackConfigAction.setStatus("current")


class _AtmPortLoopbackConfigActionResult_Type(Integer32):
    """Custom type atmPortLoopbackConfigActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AtmPortLoopbackConfigActionResult_Type.__name__ = "Integer32"
_AtmPortLoopbackConfigActionResult_Object = MibTableColumn
atmPortLoopbackConfigActionResult = _AtmPortLoopbackConfigActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 3),
    _AtmPortLoopbackConfigActionResult_Type()
)
atmPortLoopbackConfigActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortLoopbackConfigActionResult.setStatus("current")


class _AtmPortLoopbackConfigPortNumber_Type(Integer32):
    """Custom type atmPortLoopbackConfigPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port0", 0),
          ("port1", 1),
          ("port2", 2))
    )


_AtmPortLoopbackConfigPortNumber_Type.__name__ = "Integer32"
_AtmPortLoopbackConfigPortNumber_Object = MibTableColumn
atmPortLoopbackConfigPortNumber = _AtmPortLoopbackConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 4),
    _AtmPortLoopbackConfigPortNumber_Type()
)
atmPortLoopbackConfigPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLoopbackConfigPortNumber.setStatus("current")


class _AtmPortLoopbackConfigMode_Type(Integer32):
    """Custom type atmPortLoopbackConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("uni", 1),
          ("vp", 2))
    )


_AtmPortLoopbackConfigMode_Type.__name__ = "Integer32"
_AtmPortLoopbackConfigMode_Object = MibTableColumn
atmPortLoopbackConfigMode = _AtmPortLoopbackConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 5),
    _AtmPortLoopbackConfigMode_Type()
)
atmPortLoopbackConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLoopbackConfigMode.setStatus("current")


class _AtmPortLoopbackConfigOutBoundVirtualPath_Type(Integer32):
    """Custom type atmPortLoopbackConfigOutBoundVirtualPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmPortLoopbackConfigOutBoundVirtualPath_Type.__name__ = "Integer32"
_AtmPortLoopbackConfigOutBoundVirtualPath_Object = MibTableColumn
atmPortLoopbackConfigOutBoundVirtualPath = _AtmPortLoopbackConfigOutBoundVirtualPath_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 6),
    _AtmPortLoopbackConfigOutBoundVirtualPath_Type()
)
atmPortLoopbackConfigOutBoundVirtualPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLoopbackConfigOutBoundVirtualPath.setStatus("current")


class _AtmPortLoopbackConfigInBoundVirtualPath_Type(Integer32):
    """Custom type atmPortLoopbackConfigInBoundVirtualPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmPortLoopbackConfigInBoundVirtualPath_Type.__name__ = "Integer32"
_AtmPortLoopbackConfigInBoundVirtualPath_Object = MibTableColumn
atmPortLoopbackConfigInBoundVirtualPath = _AtmPortLoopbackConfigInBoundVirtualPath_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 7),
    _AtmPortLoopbackConfigInBoundVirtualPath_Type()
)
atmPortLoopbackConfigInBoundVirtualPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLoopbackConfigInBoundVirtualPath.setStatus("current")


class _AtmPortLoopbackConfigVciRangeFirst_Type(Integer32):
    """Custom type atmPortLoopbackConfigVciRangeFirst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33, 2047),
    )


_AtmPortLoopbackConfigVciRangeFirst_Type.__name__ = "Integer32"
_AtmPortLoopbackConfigVciRangeFirst_Object = MibTableColumn
atmPortLoopbackConfigVciRangeFirst = _AtmPortLoopbackConfigVciRangeFirst_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 8),
    _AtmPortLoopbackConfigVciRangeFirst_Type()
)
atmPortLoopbackConfigVciRangeFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLoopbackConfigVciRangeFirst.setStatus("current")


class _AtmPortLoopbackConfigVciRangeLast_Type(Integer32):
    """Custom type atmPortLoopbackConfigVciRangeLast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33, 2047),
    )


_AtmPortLoopbackConfigVciRangeLast_Type.__name__ = "Integer32"
_AtmPortLoopbackConfigVciRangeLast_Object = MibTableColumn
atmPortLoopbackConfigVciRangeLast = _AtmPortLoopbackConfigVciRangeLast_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 9),
    _AtmPortLoopbackConfigVciRangeLast_Type()
)
atmPortLoopbackConfigVciRangeLast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLoopbackConfigVciRangeLast.setStatus("current")


class _AtmPortLoopbackConfigServiceCategory_Type(Integer32):
    """Custom type atmPortLoopbackConfigServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("rtVbr", 2))
    )


_AtmPortLoopbackConfigServiceCategory_Type.__name__ = "Integer32"
_AtmPortLoopbackConfigServiceCategory_Object = MibTableColumn
atmPortLoopbackConfigServiceCategory = _AtmPortLoopbackConfigServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 10),
    _AtmPortLoopbackConfigServiceCategory_Type()
)
atmPortLoopbackConfigServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLoopbackConfigServiceCategory.setStatus("current")


class _AtmPortLoopbackConfigPCR_Type(Integer32):
    """Custom type atmPortLoopbackConfigPCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(171, 59600),
    )


_AtmPortLoopbackConfigPCR_Type.__name__ = "Integer32"
_AtmPortLoopbackConfigPCR_Object = MibTableColumn
atmPortLoopbackConfigPCR = _AtmPortLoopbackConfigPCR_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 11),
    _AtmPortLoopbackConfigPCR_Type()
)
atmPortLoopbackConfigPCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLoopbackConfigPCR.setStatus("current")


class _AtmPortLoopbackConfigSCR_Type(Integer32):
    """Custom type atmPortLoopbackConfigSCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(171, 59600),
    )


_AtmPortLoopbackConfigSCR_Type.__name__ = "Integer32"
_AtmPortLoopbackConfigSCR_Object = MibTableColumn
atmPortLoopbackConfigSCR = _AtmPortLoopbackConfigSCR_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 12),
    _AtmPortLoopbackConfigSCR_Type()
)
atmPortLoopbackConfigSCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLoopbackConfigSCR.setStatus("current")


class _AtmPortLoopbackConfigMBS_Type(Integer32):
    """Custom type atmPortLoopbackConfigMBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmPortLoopbackConfigMBS_Type.__name__ = "Integer32"
_AtmPortLoopbackConfigMBS_Object = MibTableColumn
atmPortLoopbackConfigMBS = _AtmPortLoopbackConfigMBS_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 13),
    _AtmPortLoopbackConfigMBS_Type()
)
atmPortLoopbackConfigMBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLoopbackConfigMBS.setStatus("current")
_AtmSvcProfile_ObjectIdentity = ObjectIdentity
atmSvcProfile = _AtmSvcProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6)
)
_AtmSvcProfileTable_Object = MibTable
atmSvcProfileTable = _AtmSvcProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1)
)
if mibBuilder.loadTexts:
    atmSvcProfileTable.setStatus("current")
_AtmSvcProfileEntry_Object = MibTableRow
atmSvcProfileEntry = _AtmSvcProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1)
)
atmSvcProfileEntry.setIndexNames(
    (0, "AcAtm", "atmSvcProfileIndex"),
)
if mibBuilder.loadTexts:
    atmSvcProfileEntry.setStatus("current")


class _AtmSvcProfileIsUsed_Type(Integer32):
    """Custom type atmSvcProfileIsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AtmSvcProfileIsUsed_Type.__name__ = "Integer32"
_AtmSvcProfileIsUsed_Object = MibTableColumn
atmSvcProfileIsUsed = _AtmSvcProfileIsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1, 1),
    _AtmSvcProfileIsUsed_Type()
)
atmSvcProfileIsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSvcProfileIsUsed.setStatus("current")


class _AtmSvcProfileIndex_Type(Integer32):
    """Custom type atmSvcProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 550),
    )


_AtmSvcProfileIndex_Type.__name__ = "Integer32"
_AtmSvcProfileIndex_Object = MibTableColumn
atmSvcProfileIndex = _AtmSvcProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1, 2),
    _AtmSvcProfileIndex_Type()
)
atmSvcProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSvcProfileIndex.setStatus("current")


class _AtmSvcProfileMaxNumOfCids_Type(Integer32):
    """Custom type atmSvcProfileMaxNumOfCids based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_AtmSvcProfileMaxNumOfCids_Type.__name__ = "Integer32"
_AtmSvcProfileMaxNumOfCids_Object = MibTableColumn
atmSvcProfileMaxNumOfCids = _AtmSvcProfileMaxNumOfCids_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1, 3),
    _AtmSvcProfileMaxNumOfCids_Type()
)
atmSvcProfileMaxNumOfCids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSvcProfileMaxNumOfCids.setStatus("current")


class _AtmSvcProfilePCR_Type(Integer32):
    """Custom type atmSvcProfilePCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(171, 59600),
    )


_AtmSvcProfilePCR_Type.__name__ = "Integer32"
_AtmSvcProfilePCR_Object = MibTableColumn
atmSvcProfilePCR = _AtmSvcProfilePCR_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1, 4),
    _AtmSvcProfilePCR_Type()
)
atmSvcProfilePCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSvcProfilePCR.setStatus("current")


class _AtmSvcProfileSCR_Type(Integer32):
    """Custom type atmSvcProfileSCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(171, 59600),
    )


_AtmSvcProfileSCR_Type.__name__ = "Integer32"
_AtmSvcProfileSCR_Object = MibTableColumn
atmSvcProfileSCR = _AtmSvcProfileSCR_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1, 5),
    _AtmSvcProfileSCR_Type()
)
atmSvcProfileSCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSvcProfileSCR.setStatus("current")


class _AtmSvcProfileMBS_Type(Integer32):
    """Custom type atmSvcProfileMBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmSvcProfileMBS_Type.__name__ = "Integer32"
_AtmSvcProfileMBS_Object = MibTableColumn
atmSvcProfileMBS = _AtmSvcProfileMBS_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1, 6),
    _AtmSvcProfileMBS_Type()
)
atmSvcProfileMBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSvcProfileMBS.setStatus("current")


class _AtmSvcProfilePersistence_Type(Integer32):
    """Custom type atmSvcProfilePersistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AtmSvcProfilePersistence_Type.__name__ = "Integer32"
_AtmSvcProfilePersistence_Object = MibTableColumn
atmSvcProfilePersistence = _AtmSvcProfilePersistence_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1, 7),
    _AtmSvcProfilePersistence_Type()
)
atmSvcProfilePersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSvcProfilePersistence.setStatus("current")


class _AtmSvcProfileServiceCategory_Type(Integer32):
    """Custom type atmSvcProfileServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("rtVbr", 2))
    )


_AtmSvcProfileServiceCategory_Type.__name__ = "Integer32"
_AtmSvcProfileServiceCategory_Object = MibTableColumn
atmSvcProfileServiceCategory = _AtmSvcProfileServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1, 8),
    _AtmSvcProfileServiceCategory_Type()
)
atmSvcProfileServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSvcProfileServiceCategory.setStatus("current")
_AcAtmStatus_ObjectIdentity = ObjectIdentity
acAtmStatus = _AcAtmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2)
)
_AtmSvcConnection_ObjectIdentity = ObjectIdentity
atmSvcConnection = _AtmSvcConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1)
)
_AtmSvcConnectionTable_Object = MibTable
atmSvcConnectionTable = _AtmSvcConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    atmSvcConnectionTable.setStatus("current")
_AtmSvcConnectionEntry_Object = MibTableRow
atmSvcConnectionEntry = _AtmSvcConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1)
)
atmSvcConnectionEntry.setIndexNames(
    (0, "AcAtm", "atmSvcConnectionIndex"),
)
if mibBuilder.loadTexts:
    atmSvcConnectionEntry.setStatus("current")


class _AtmSvcConnectionIndex_Type(Integer32):
    """Custom type atmSvcConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_AtmSvcConnectionIndex_Type.__name__ = "Integer32"
_AtmSvcConnectionIndex_Object = MibTableColumn
atmSvcConnectionIndex = _AtmSvcConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 1),
    _AtmSvcConnectionIndex_Type()
)
atmSvcConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSvcConnectionIndex.setStatus("current")


class _AtmSvcConnectionRemoteGatewayAddress_Type(AtmAddr):
    """Custom type atmSvcConnectionRemoteGatewayAddress based on AtmAddr"""
    subtypeSpec = AtmAddr.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AtmSvcConnectionRemoteGatewayAddress_Type.__name__ = "AtmAddr"
_AtmSvcConnectionRemoteGatewayAddress_Object = MibTableColumn
atmSvcConnectionRemoteGatewayAddress = _AtmSvcConnectionRemoteGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 2),
    _AtmSvcConnectionRemoteGatewayAddress_Type()
)
atmSvcConnectionRemoteGatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSvcConnectionRemoteGatewayAddress.setStatus("current")


class _AtmSvcConnectionPort_Type(Integer32):
    """Custom type atmSvcConnectionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port0", 0),
          ("port1", 1),
          ("port2", 2))
    )


_AtmSvcConnectionPort_Type.__name__ = "Integer32"
_AtmSvcConnectionPort_Object = MibTableColumn
atmSvcConnectionPort = _AtmSvcConnectionPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 3),
    _AtmSvcConnectionPort_Type()
)
atmSvcConnectionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSvcConnectionPort.setStatus("current")


class _AtmSvcConnectionVpi_Type(Integer32):
    """Custom type atmSvcConnectionVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmSvcConnectionVpi_Type.__name__ = "Integer32"
_AtmSvcConnectionVpi_Object = MibTableColumn
atmSvcConnectionVpi = _AtmSvcConnectionVpi_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 4),
    _AtmSvcConnectionVpi_Type()
)
atmSvcConnectionVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSvcConnectionVpi.setStatus("current")


class _AtmSvcConnectionVci_Type(Integer32):
    """Custom type atmSvcConnectionVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSvcConnectionVci_Type.__name__ = "Integer32"
_AtmSvcConnectionVci_Object = MibTableColumn
atmSvcConnectionVci = _AtmSvcConnectionVci_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 5),
    _AtmSvcConnectionVci_Type()
)
atmSvcConnectionVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSvcConnectionVci.setStatus("current")


class _AtmSvcConnectionAALType_Type(Integer32):
    """Custom type atmSvcConnectionAALType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 1),
          ("aal2", 2))
    )


_AtmSvcConnectionAALType_Type.__name__ = "Integer32"
_AtmSvcConnectionAALType_Object = MibTableColumn
atmSvcConnectionAALType = _AtmSvcConnectionAALType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 6),
    _AtmSvcConnectionAALType_Type()
)
atmSvcConnectionAALType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSvcConnectionAALType.setStatus("current")


class _AtmSvcConnectionDirection_Type(Integer32):
    """Custom type atmSvcConnectionDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 0),
          ("outgoing", 1))
    )


_AtmSvcConnectionDirection_Type.__name__ = "Integer32"
_AtmSvcConnectionDirection_Object = MibTableColumn
atmSvcConnectionDirection = _AtmSvcConnectionDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 7),
    _AtmSvcConnectionDirection_Type()
)
atmSvcConnectionDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSvcConnectionDirection.setStatus("current")
_AtmSvcConnectionEecid_Type = Unsigned32
_AtmSvcConnectionEecid_Object = MibTableColumn
atmSvcConnectionEecid = _AtmSvcConnectionEecid_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 8),
    _AtmSvcConnectionEecid_Type()
)
atmSvcConnectionEecid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSvcConnectionEecid.setStatus("current")


class _AtmSvcConnectionVcci_Type(Integer32):
    """Custom type atmSvcConnectionVcci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSvcConnectionVcci_Type.__name__ = "Integer32"
_AtmSvcConnectionVcci_Object = MibTableColumn
atmSvcConnectionVcci = _AtmSvcConnectionVcci_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 9),
    _AtmSvcConnectionVcci_Type()
)
atmSvcConnectionVcci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSvcConnectionVcci.setStatus("current")


class _AtmSvcConnectionMaxNumOfCid_Type(Integer32):
    """Custom type atmSvcConnectionMaxNumOfCid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_AtmSvcConnectionMaxNumOfCid_Type.__name__ = "Integer32"
_AtmSvcConnectionMaxNumOfCid_Object = MibTableColumn
atmSvcConnectionMaxNumOfCid = _AtmSvcConnectionMaxNumOfCid_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 10),
    _AtmSvcConnectionMaxNumOfCid_Type()
)
atmSvcConnectionMaxNumOfCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSvcConnectionMaxNumOfCid.setStatus("current")


class _AtmSvcConnectionNumOfCidInUse_Type(Integer32):
    """Custom type atmSvcConnectionNumOfCidInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_AtmSvcConnectionNumOfCidInUse_Type.__name__ = "Integer32"
_AtmSvcConnectionNumOfCidInUse_Object = MibTableColumn
atmSvcConnectionNumOfCidInUse = _AtmSvcConnectionNumOfCidInUse_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 11),
    _AtmSvcConnectionNumOfCidInUse_Type()
)
atmSvcConnectionNumOfCidInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSvcConnectionNumOfCidInUse.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AcAtm",
    **{"audioCodes": audioCodes,
       "acRegistrations": acRegistrations,
       "acGeneric": acGeneric,
       "acProducts": acProducts,
       "acBoardMibs": acBoardMibs,
       "acAtm": acAtm,
       "acAtmConfiguration": acAtmConfiguration,
       "atmGeneralParams": atmGeneralParams,
       "atmGeneralParamsAtmDefaultApplicationType": atmGeneralParamsAtmDefaultApplicationType,
       "atmGeneralParamsAtmTransmissionMode": atmGeneralParamsAtmTransmissionMode,
       "atmPort": atmPort,
       "atmPortTable": atmPortTable,
       "atmPortEntry": atmPortEntry,
       "atmPortAdministrativeState": atmPortAdministrativeState,
       "atmPortOperationalState": atmPortOperationalState,
       "atmPortNumber": atmPortNumber,
       "atmPortAdminAddress": atmPortAdminAddress,
       "atmPortOperationalAddress": atmPortOperationalAddress,
       "atmPortAlarmStatus": atmPortAlarmStatus,
       "atmPortAddressMode": atmPortAddressMode,
       "atmRemoteGateway": atmRemoteGateway,
       "atmRemoteGatewayTable": atmRemoteGatewayTable,
       "atmRemoteGatewayEntry": atmRemoteGatewayEntry,
       "atmRemoteGatewayRowStatus": atmRemoteGatewayRowStatus,
       "atmRemoteGatewayAction": atmRemoteGatewayAction,
       "atmRemoteGatewayActionResult": atmRemoteGatewayActionResult,
       "atmRemoteGatewayIndex": atmRemoteGatewayIndex,
       "atmRemoteGatewayName": atmRemoteGatewayName,
       "atmRemoteGatewayNSAPAddress": atmRemoteGatewayNSAPAddress,
       "atmRemoteGatewayALCAPInstanceNum": atmRemoteGatewayALCAPInstanceNum,
       "aal2PVC": aal2PVC,
       "aal2PVCTable": aal2PVCTable,
       "aal2PVCEntry": aal2PVCEntry,
       "aal2PVCRowStatus": aal2PVCRowStatus,
       "aal2PVCAction": aal2PVCAction,
       "aal2PVCActionResult": aal2PVCActionResult,
       "aal2PVCRemoteGatewayIndex": aal2PVCRemoteGatewayIndex,
       "aal2PVCVCCIPATHID": aal2PVCVCCIPATHID,
       "aal2PVCPortNumber": aal2PVCPortNumber,
       "aal2PVCVpi": aal2PVCVpi,
       "aal2PVCVci": aal2PVCVci,
       "aal2PVCMaxNumOfCid": aal2PVCMaxNumOfCid,
       "aal2PVCNumOfCidInUse": aal2PVCNumOfCidInUse,
       "aal2PVCServiceCategory": aal2PVCServiceCategory,
       "aal2PVCPCR": aal2PVCPCR,
       "aal2PVCSCR": aal2PVCSCR,
       "aal2PVCMBS": aal2PVCMBS,
       "atmPortLoopbackConfig": atmPortLoopbackConfig,
       "atmPortLoopbackConfigTable": atmPortLoopbackConfigTable,
       "atmPortLoopbackConfigEntry": atmPortLoopbackConfigEntry,
       "atmPortLoopbackConfigIsUsed": atmPortLoopbackConfigIsUsed,
       "atmPortLoopbackConfigAction": atmPortLoopbackConfigAction,
       "atmPortLoopbackConfigActionResult": atmPortLoopbackConfigActionResult,
       "atmPortLoopbackConfigPortNumber": atmPortLoopbackConfigPortNumber,
       "atmPortLoopbackConfigMode": atmPortLoopbackConfigMode,
       "atmPortLoopbackConfigOutBoundVirtualPath": atmPortLoopbackConfigOutBoundVirtualPath,
       "atmPortLoopbackConfigInBoundVirtualPath": atmPortLoopbackConfigInBoundVirtualPath,
       "atmPortLoopbackConfigVciRangeFirst": atmPortLoopbackConfigVciRangeFirst,
       "atmPortLoopbackConfigVciRangeLast": atmPortLoopbackConfigVciRangeLast,
       "atmPortLoopbackConfigServiceCategory": atmPortLoopbackConfigServiceCategory,
       "atmPortLoopbackConfigPCR": atmPortLoopbackConfigPCR,
       "atmPortLoopbackConfigSCR": atmPortLoopbackConfigSCR,
       "atmPortLoopbackConfigMBS": atmPortLoopbackConfigMBS,
       "atmSvcProfile": atmSvcProfile,
       "atmSvcProfileTable": atmSvcProfileTable,
       "atmSvcProfileEntry": atmSvcProfileEntry,
       "atmSvcProfileIsUsed": atmSvcProfileIsUsed,
       "atmSvcProfileIndex": atmSvcProfileIndex,
       "atmSvcProfileMaxNumOfCids": atmSvcProfileMaxNumOfCids,
       "atmSvcProfilePCR": atmSvcProfilePCR,
       "atmSvcProfileSCR": atmSvcProfileSCR,
       "atmSvcProfileMBS": atmSvcProfileMBS,
       "atmSvcProfilePersistence": atmSvcProfilePersistence,
       "atmSvcProfileServiceCategory": atmSvcProfileServiceCategory,
       "acAtmStatus": acAtmStatus,
       "atmSvcConnection": atmSvcConnection,
       "atmSvcConnectionTable": atmSvcConnectionTable,
       "atmSvcConnectionEntry": atmSvcConnectionEntry,
       "atmSvcConnectionIndex": atmSvcConnectionIndex,
       "atmSvcConnectionRemoteGatewayAddress": atmSvcConnectionRemoteGatewayAddress,
       "atmSvcConnectionPort": atmSvcConnectionPort,
       "atmSvcConnectionVpi": atmSvcConnectionVpi,
       "atmSvcConnectionVci": atmSvcConnectionVci,
       "atmSvcConnectionAALType": atmSvcConnectionAALType,
       "atmSvcConnectionDirection": atmSvcConnectionDirection,
       "atmSvcConnectionEecid": atmSvcConnectionEecid,
       "atmSvcConnectionVcci": atmSvcConnectionVcci,
       "atmSvcConnectionMaxNumOfCid": atmSvcConnectionMaxNumOfCid,
       "atmSvcConnectionNumOfCidInUse": atmSvcConnectionNumOfCidInUse}
)
