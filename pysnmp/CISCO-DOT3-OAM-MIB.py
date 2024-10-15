# SNMP MIB module (CISCO-DOT3-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DOT3-OAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:00 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cdot3OamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 136)
)
cdot3OamMIB.setRevisions(
        ("2006-05-31 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Cdot3Oui(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



# MIB Managed Objects in the order of their OIDs

_Cdot3OamNotifications_ObjectIdentity = ObjectIdentity
cdot3OamNotifications = _Cdot3OamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 0)
)
_Cdot3OamObjects_ObjectIdentity = ObjectIdentity
cdot3OamObjects = _Cdot3OamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1)
)
_Cdot3OamTable_Object = MibTable
cdot3OamTable = _Cdot3OamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 1)
)
if mibBuilder.loadTexts:
    cdot3OamTable.setStatus("current")
_Cdot3OamEntry_Object = MibTableRow
cdot3OamEntry = _Cdot3OamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 1, 1)
)
cdot3OamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdot3OamEntry.setStatus("current")


class _Cdot3OamAdminState_Type(Integer32):
    """Custom type cdot3OamAdminState based on Integer32"""
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


_Cdot3OamAdminState_Type.__name__ = "Integer32"
_Cdot3OamAdminState_Object = MibTableColumn
cdot3OamAdminState = _Cdot3OamAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 1, 1, 1),
    _Cdot3OamAdminState_Type()
)
cdot3OamAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamAdminState.setStatus("current")


class _Cdot3OamOperStatus_Type(Integer32):
    """Custom type cdot3OamOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("activeSendLocal", 4),
          ("disabled", 1),
          ("linkFault", 2),
          ("nonOperHalfDuplex", 10),
          ("oamPeeringLocallyRejected", 7),
          ("oamPeeringRemotelyRejected", 8),
          ("operational", 9),
          ("passiveWait", 3),
          ("sendLocalAndRemote", 5),
          ("sendLocalAndRemoteOk", 6))
    )


_Cdot3OamOperStatus_Type.__name__ = "Integer32"
_Cdot3OamOperStatus_Object = MibTableColumn
cdot3OamOperStatus = _Cdot3OamOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 1, 1, 2),
    _Cdot3OamOperStatus_Type()
)
cdot3OamOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamOperStatus.setStatus("current")


class _Cdot3OamMode_Type(Integer32):
    """Custom type cdot3OamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_Cdot3OamMode_Type.__name__ = "Integer32"
_Cdot3OamMode_Object = MibTableColumn
cdot3OamMode = _Cdot3OamMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 1, 1, 3),
    _Cdot3OamMode_Type()
)
cdot3OamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamMode.setStatus("current")


class _Cdot3OamMaxOamPduSize_Type(Unsigned32):
    """Custom type cdot3OamMaxOamPduSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_Cdot3OamMaxOamPduSize_Type.__name__ = "Unsigned32"
_Cdot3OamMaxOamPduSize_Object = MibTableColumn
cdot3OamMaxOamPduSize = _Cdot3OamMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 1, 1, 4),
    _Cdot3OamMaxOamPduSize_Type()
)
cdot3OamMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamMaxOamPduSize.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamMaxOamPduSize.setUnits("octets")


class _Cdot3OamConfigRevision_Type(Unsigned32):
    """Custom type cdot3OamConfigRevision based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdot3OamConfigRevision_Type.__name__ = "Unsigned32"
_Cdot3OamConfigRevision_Object = MibTableColumn
cdot3OamConfigRevision = _Cdot3OamConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 1, 1, 5),
    _Cdot3OamConfigRevision_Type()
)
cdot3OamConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamConfigRevision.setStatus("current")


class _Cdot3OamFunctionsSupported_Type(Bits):
    """Custom type cdot3OamFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("eventSupport", 2),
          ("loopbackSupport", 1),
          ("unidirectionalSupport", 0),
          ("variableSupport", 3))
    )

_Cdot3OamFunctionsSupported_Type.__name__ = "Bits"
_Cdot3OamFunctionsSupported_Object = MibTableColumn
cdot3OamFunctionsSupported = _Cdot3OamFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 1, 1, 6),
    _Cdot3OamFunctionsSupported_Type()
)
cdot3OamFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamFunctionsSupported.setStatus("current")
_Cdot3OamPeerTable_Object = MibTable
cdot3OamPeerTable = _Cdot3OamPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 2)
)
if mibBuilder.loadTexts:
    cdot3OamPeerTable.setStatus("current")
_Cdot3OamPeerEntry_Object = MibTableRow
cdot3OamPeerEntry = _Cdot3OamPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 2, 1)
)
cdot3OamPeerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdot3OamPeerEntry.setStatus("current")
_Cdot3OamPeerMacAddress_Type = MacAddress
_Cdot3OamPeerMacAddress_Object = MibTableColumn
cdot3OamPeerMacAddress = _Cdot3OamPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 2, 1, 1),
    _Cdot3OamPeerMacAddress_Type()
)
cdot3OamPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamPeerMacAddress.setStatus("current")
_Cdot3OamPeerVendorOui_Type = Cdot3Oui
_Cdot3OamPeerVendorOui_Object = MibTableColumn
cdot3OamPeerVendorOui = _Cdot3OamPeerVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 2, 1, 2),
    _Cdot3OamPeerVendorOui_Type()
)
cdot3OamPeerVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamPeerVendorOui.setStatus("current")
_Cdot3OamPeerVendorInfo_Type = Unsigned32
_Cdot3OamPeerVendorInfo_Object = MibTableColumn
cdot3OamPeerVendorInfo = _Cdot3OamPeerVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 2, 1, 3),
    _Cdot3OamPeerVendorInfo_Type()
)
cdot3OamPeerVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamPeerVendorInfo.setStatus("current")


class _Cdot3OamPeerMode_Type(Integer32):
    """Custom type cdot3OamPeerMode based on Integer32"""
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
          ("passive", 2),
          ("unknown", 3))
    )


_Cdot3OamPeerMode_Type.__name__ = "Integer32"
_Cdot3OamPeerMode_Object = MibTableColumn
cdot3OamPeerMode = _Cdot3OamPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 2, 1, 4),
    _Cdot3OamPeerMode_Type()
)
cdot3OamPeerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamPeerMode.setStatus("current")


class _Cdot3OamPeerMaxOamPduSize_Type(Unsigned32):
    """Custom type cdot3OamPeerMaxOamPduSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1518),
    )


_Cdot3OamPeerMaxOamPduSize_Type.__name__ = "Unsigned32"
_Cdot3OamPeerMaxOamPduSize_Object = MibTableColumn
cdot3OamPeerMaxOamPduSize = _Cdot3OamPeerMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 2, 1, 5),
    _Cdot3OamPeerMaxOamPduSize_Type()
)
cdot3OamPeerMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamPeerMaxOamPduSize.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamPeerMaxOamPduSize.setUnits("octets")


class _Cdot3OamPeerConfigRevision_Type(Unsigned32):
    """Custom type cdot3OamPeerConfigRevision based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdot3OamPeerConfigRevision_Type.__name__ = "Unsigned32"
_Cdot3OamPeerConfigRevision_Object = MibTableColumn
cdot3OamPeerConfigRevision = _Cdot3OamPeerConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 2, 1, 6),
    _Cdot3OamPeerConfigRevision_Type()
)
cdot3OamPeerConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamPeerConfigRevision.setStatus("current")


class _Cdot3OamPeerFunctionsSupported_Type(Bits):
    """Custom type cdot3OamPeerFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("eventSupport", 2),
          ("loopbackSupport", 1),
          ("unidirectionalSupport", 0),
          ("variableSupport", 3))
    )

_Cdot3OamPeerFunctionsSupported_Type.__name__ = "Bits"
_Cdot3OamPeerFunctionsSupported_Object = MibTableColumn
cdot3OamPeerFunctionsSupported = _Cdot3OamPeerFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 2, 1, 7),
    _Cdot3OamPeerFunctionsSupported_Type()
)
cdot3OamPeerFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamPeerFunctionsSupported.setStatus("current")
_Cdot3OamLoopbackTable_Object = MibTable
cdot3OamLoopbackTable = _Cdot3OamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 3)
)
if mibBuilder.loadTexts:
    cdot3OamLoopbackTable.setStatus("current")
_Cdot3OamLoopbackEntry_Object = MibTableRow
cdot3OamLoopbackEntry = _Cdot3OamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 3, 1)
)
cdot3OamLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdot3OamLoopbackEntry.setStatus("current")


class _Cdot3OamLoopbackStatus_Type(Integer32):
    """Custom type cdot3OamLoopbackStatus based on Integer32"""
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
        *(("initiatingLoopback", 2),
          ("localLoopback", 5),
          ("noLoopback", 1),
          ("remoteLoopback", 3),
          ("terminatingLoopback", 4),
          ("unknown", 6))
    )


_Cdot3OamLoopbackStatus_Type.__name__ = "Integer32"
_Cdot3OamLoopbackStatus_Object = MibTableColumn
cdot3OamLoopbackStatus = _Cdot3OamLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 3, 1, 1),
    _Cdot3OamLoopbackStatus_Type()
)
cdot3OamLoopbackStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamLoopbackStatus.setStatus("current")


class _Cdot3OamLoopbackIgnoreRx_Type(Integer32):
    """Custom type cdot3OamLoopbackIgnoreRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("process", 2))
    )


_Cdot3OamLoopbackIgnoreRx_Type.__name__ = "Integer32"
_Cdot3OamLoopbackIgnoreRx_Object = MibTableColumn
cdot3OamLoopbackIgnoreRx = _Cdot3OamLoopbackIgnoreRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 3, 1, 2),
    _Cdot3OamLoopbackIgnoreRx_Type()
)
cdot3OamLoopbackIgnoreRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamLoopbackIgnoreRx.setStatus("current")
_Cdot3OamStatsTable_Object = MibTable
cdot3OamStatsTable = _Cdot3OamStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4)
)
if mibBuilder.loadTexts:
    cdot3OamStatsTable.setStatus("current")
_Cdot3OamStatsEntry_Object = MibTableRow
cdot3OamStatsEntry = _Cdot3OamStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1)
)
cdot3OamStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdot3OamStatsEntry.setStatus("current")
_Cdot3OamInformationTx_Type = Counter32
_Cdot3OamInformationTx_Object = MibTableColumn
cdot3OamInformationTx = _Cdot3OamInformationTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1, 1),
    _Cdot3OamInformationTx_Type()
)
cdot3OamInformationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamInformationTx.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamInformationTx.setUnits("frames")
_Cdot3OamInformationRx_Type = Counter32
_Cdot3OamInformationRx_Object = MibTableColumn
cdot3OamInformationRx = _Cdot3OamInformationRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1, 2),
    _Cdot3OamInformationRx_Type()
)
cdot3OamInformationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamInformationRx.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamInformationRx.setUnits("frames")
_Cdot3OamUniqueEventNotificationTx_Type = Counter32
_Cdot3OamUniqueEventNotificationTx_Object = MibTableColumn
cdot3OamUniqueEventNotificationTx = _Cdot3OamUniqueEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1, 3),
    _Cdot3OamUniqueEventNotificationTx_Type()
)
cdot3OamUniqueEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamUniqueEventNotificationTx.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamUniqueEventNotificationTx.setUnits("frames")
_Cdot3OamUniqueEventNotificationRx_Type = Counter32
_Cdot3OamUniqueEventNotificationRx_Object = MibTableColumn
cdot3OamUniqueEventNotificationRx = _Cdot3OamUniqueEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1, 4),
    _Cdot3OamUniqueEventNotificationRx_Type()
)
cdot3OamUniqueEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamUniqueEventNotificationRx.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamUniqueEventNotificationRx.setUnits("frames")
_Cdot3OamDuplicateEventNotificationTx_Type = Counter32
_Cdot3OamDuplicateEventNotificationTx_Object = MibTableColumn
cdot3OamDuplicateEventNotificationTx = _Cdot3OamDuplicateEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1, 5),
    _Cdot3OamDuplicateEventNotificationTx_Type()
)
cdot3OamDuplicateEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamDuplicateEventNotificationTx.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamDuplicateEventNotificationTx.setUnits("frames")
_Cdot3OamDuplicateEventNotificationRx_Type = Counter32
_Cdot3OamDuplicateEventNotificationRx_Object = MibTableColumn
cdot3OamDuplicateEventNotificationRx = _Cdot3OamDuplicateEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1, 6),
    _Cdot3OamDuplicateEventNotificationRx_Type()
)
cdot3OamDuplicateEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamDuplicateEventNotificationRx.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamDuplicateEventNotificationRx.setUnits("frames")
_Cdot3OamLoopbackControlTx_Type = Counter32
_Cdot3OamLoopbackControlTx_Object = MibTableColumn
cdot3OamLoopbackControlTx = _Cdot3OamLoopbackControlTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1, 7),
    _Cdot3OamLoopbackControlTx_Type()
)
cdot3OamLoopbackControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamLoopbackControlTx.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamLoopbackControlTx.setUnits("frames")
_Cdot3OamLoopbackControlRx_Type = Counter32
_Cdot3OamLoopbackControlRx_Object = MibTableColumn
cdot3OamLoopbackControlRx = _Cdot3OamLoopbackControlRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1, 8),
    _Cdot3OamLoopbackControlRx_Type()
)
cdot3OamLoopbackControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamLoopbackControlRx.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamLoopbackControlRx.setUnits("frames")
_Cdot3OamVariableRequestTx_Type = Counter32
_Cdot3OamVariableRequestTx_Object = MibTableColumn
cdot3OamVariableRequestTx = _Cdot3OamVariableRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1, 9),
    _Cdot3OamVariableRequestTx_Type()
)
cdot3OamVariableRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamVariableRequestTx.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamVariableRequestTx.setUnits("frames")
_Cdot3OamVariableRequestRx_Type = Counter32
_Cdot3OamVariableRequestRx_Object = MibTableColumn
cdot3OamVariableRequestRx = _Cdot3OamVariableRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1, 10),
    _Cdot3OamVariableRequestRx_Type()
)
cdot3OamVariableRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamVariableRequestRx.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamVariableRequestRx.setUnits("frames")
_Cdot3OamVariableResponseTx_Type = Counter32
_Cdot3OamVariableResponseTx_Object = MibTableColumn
cdot3OamVariableResponseTx = _Cdot3OamVariableResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1, 11),
    _Cdot3OamVariableResponseTx_Type()
)
cdot3OamVariableResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamVariableResponseTx.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamVariableResponseTx.setUnits("frames")
_Cdot3OamVariableResponseRx_Type = Counter32
_Cdot3OamVariableResponseRx_Object = MibTableColumn
cdot3OamVariableResponseRx = _Cdot3OamVariableResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1, 12),
    _Cdot3OamVariableResponseRx_Type()
)
cdot3OamVariableResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamVariableResponseRx.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamVariableResponseRx.setUnits("frames")
_Cdot3OamOrgSpecificTx_Type = Counter32
_Cdot3OamOrgSpecificTx_Object = MibTableColumn
cdot3OamOrgSpecificTx = _Cdot3OamOrgSpecificTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1, 13),
    _Cdot3OamOrgSpecificTx_Type()
)
cdot3OamOrgSpecificTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamOrgSpecificTx.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamOrgSpecificTx.setUnits("frames")
_Cdot3OamOrgSpecificRx_Type = Counter32
_Cdot3OamOrgSpecificRx_Object = MibTableColumn
cdot3OamOrgSpecificRx = _Cdot3OamOrgSpecificRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1, 14),
    _Cdot3OamOrgSpecificRx_Type()
)
cdot3OamOrgSpecificRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamOrgSpecificRx.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamOrgSpecificRx.setUnits("frames")
_Cdot3OamUnsupportedCodesTx_Type = Counter32
_Cdot3OamUnsupportedCodesTx_Object = MibTableColumn
cdot3OamUnsupportedCodesTx = _Cdot3OamUnsupportedCodesTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1, 15),
    _Cdot3OamUnsupportedCodesTx_Type()
)
cdot3OamUnsupportedCodesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamUnsupportedCodesTx.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamUnsupportedCodesTx.setUnits("frames")
_Cdot3OamUnsupportedCodesRx_Type = Counter32
_Cdot3OamUnsupportedCodesRx_Object = MibTableColumn
cdot3OamUnsupportedCodesRx = _Cdot3OamUnsupportedCodesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1, 16),
    _Cdot3OamUnsupportedCodesRx_Type()
)
cdot3OamUnsupportedCodesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamUnsupportedCodesRx.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamUnsupportedCodesRx.setUnits("frames")
_Cdot3OamFramesLostDueToOam_Type = Counter32
_Cdot3OamFramesLostDueToOam_Object = MibTableColumn
cdot3OamFramesLostDueToOam = _Cdot3OamFramesLostDueToOam_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 4, 1, 17),
    _Cdot3OamFramesLostDueToOam_Type()
)
cdot3OamFramesLostDueToOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamFramesLostDueToOam.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamFramesLostDueToOam.setUnits("frames")
_Cdot3OamEventConfigTable_Object = MibTable
cdot3OamEventConfigTable = _Cdot3OamEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5)
)
if mibBuilder.loadTexts:
    cdot3OamEventConfigTable.setStatus("current")
_Cdot3OamEventConfigEntry_Object = MibTableRow
cdot3OamEventConfigEntry = _Cdot3OamEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5, 1)
)
cdot3OamEventConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdot3OamEventConfigEntry.setStatus("current")
_Cdot3OamErrSymPeriodWindowHi_Type = Unsigned32
_Cdot3OamErrSymPeriodWindowHi_Object = MibTableColumn
cdot3OamErrSymPeriodWindowHi = _Cdot3OamErrSymPeriodWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5, 1, 1),
    _Cdot3OamErrSymPeriodWindowHi_Type()
)
cdot3OamErrSymPeriodWindowHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamErrSymPeriodWindowHi.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamErrSymPeriodWindowHi.setUnits("2^32 symbols")
_Cdot3OamErrSymPeriodWindowLo_Type = Unsigned32
_Cdot3OamErrSymPeriodWindowLo_Object = MibTableColumn
cdot3OamErrSymPeriodWindowLo = _Cdot3OamErrSymPeriodWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5, 1, 2),
    _Cdot3OamErrSymPeriodWindowLo_Type()
)
cdot3OamErrSymPeriodWindowLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamErrSymPeriodWindowLo.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamErrSymPeriodWindowLo.setUnits("symbols")
_Cdot3OamErrSymPeriodThresholdHi_Type = Unsigned32
_Cdot3OamErrSymPeriodThresholdHi_Object = MibTableColumn
cdot3OamErrSymPeriodThresholdHi = _Cdot3OamErrSymPeriodThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5, 1, 3),
    _Cdot3OamErrSymPeriodThresholdHi_Type()
)
cdot3OamErrSymPeriodThresholdHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamErrSymPeriodThresholdHi.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamErrSymPeriodThresholdHi.setUnits("2^32 symbols")
_Cdot3OamErrSymPeriodThresholdLo_Type = Unsigned32
_Cdot3OamErrSymPeriodThresholdLo_Object = MibTableColumn
cdot3OamErrSymPeriodThresholdLo = _Cdot3OamErrSymPeriodThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5, 1, 4),
    _Cdot3OamErrSymPeriodThresholdLo_Type()
)
cdot3OamErrSymPeriodThresholdLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamErrSymPeriodThresholdLo.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamErrSymPeriodThresholdLo.setUnits("symbols")
_Cdot3OamErrSymPeriodEvNotifEnable_Type = TruthValue
_Cdot3OamErrSymPeriodEvNotifEnable_Object = MibTableColumn
cdot3OamErrSymPeriodEvNotifEnable = _Cdot3OamErrSymPeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5, 1, 5),
    _Cdot3OamErrSymPeriodEvNotifEnable_Type()
)
cdot3OamErrSymPeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamErrSymPeriodEvNotifEnable.setStatus("current")
_Cdot3OamErrFramePeriodWindow_Type = Unsigned32
_Cdot3OamErrFramePeriodWindow_Object = MibTableColumn
cdot3OamErrFramePeriodWindow = _Cdot3OamErrFramePeriodWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5, 1, 6),
    _Cdot3OamErrFramePeriodWindow_Type()
)
cdot3OamErrFramePeriodWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamErrFramePeriodWindow.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamErrFramePeriodWindow.setUnits("frames")
_Cdot3OamErrFramePeriodThreshold_Type = Unsigned32
_Cdot3OamErrFramePeriodThreshold_Object = MibTableColumn
cdot3OamErrFramePeriodThreshold = _Cdot3OamErrFramePeriodThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5, 1, 7),
    _Cdot3OamErrFramePeriodThreshold_Type()
)
cdot3OamErrFramePeriodThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamErrFramePeriodThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamErrFramePeriodThreshold.setUnits("frames")
_Cdot3OamErrFramePeriodEvNotifEnable_Type = TruthValue
_Cdot3OamErrFramePeriodEvNotifEnable_Object = MibTableColumn
cdot3OamErrFramePeriodEvNotifEnable = _Cdot3OamErrFramePeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5, 1, 8),
    _Cdot3OamErrFramePeriodEvNotifEnable_Type()
)
cdot3OamErrFramePeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamErrFramePeriodEvNotifEnable.setStatus("current")
_Cdot3OamErrFrameWindow_Type = Unsigned32
_Cdot3OamErrFrameWindow_Object = MibTableColumn
cdot3OamErrFrameWindow = _Cdot3OamErrFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5, 1, 9),
    _Cdot3OamErrFrameWindow_Type()
)
cdot3OamErrFrameWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamErrFrameWindow.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamErrFrameWindow.setUnits("tenths of a second")
_Cdot3OamErrFrameThreshold_Type = Unsigned32
_Cdot3OamErrFrameThreshold_Object = MibTableColumn
cdot3OamErrFrameThreshold = _Cdot3OamErrFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5, 1, 10),
    _Cdot3OamErrFrameThreshold_Type()
)
cdot3OamErrFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamErrFrameThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamErrFrameThreshold.setUnits("frames")
_Cdot3OamErrFrameEvNotifEnable_Type = TruthValue
_Cdot3OamErrFrameEvNotifEnable_Object = MibTableColumn
cdot3OamErrFrameEvNotifEnable = _Cdot3OamErrFrameEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5, 1, 11),
    _Cdot3OamErrFrameEvNotifEnable_Type()
)
cdot3OamErrFrameEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamErrFrameEvNotifEnable.setStatus("current")


class _Cdot3OamErrFrameSecsSummaryWindow_Type(Integer32):
    """Custom type cdot3OamErrFrameSecsSummaryWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 9000),
    )


_Cdot3OamErrFrameSecsSummaryWindow_Type.__name__ = "Integer32"
_Cdot3OamErrFrameSecsSummaryWindow_Object = MibTableColumn
cdot3OamErrFrameSecsSummaryWindow = _Cdot3OamErrFrameSecsSummaryWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5, 1, 12),
    _Cdot3OamErrFrameSecsSummaryWindow_Type()
)
cdot3OamErrFrameSecsSummaryWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamErrFrameSecsSummaryWindow.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamErrFrameSecsSummaryWindow.setUnits("tenths of a second")


class _Cdot3OamErrFrameSecsSummaryThreshold_Type(Integer32):
    """Custom type cdot3OamErrFrameSecsSummaryThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_Cdot3OamErrFrameSecsSummaryThreshold_Type.__name__ = "Integer32"
_Cdot3OamErrFrameSecsSummaryThreshold_Object = MibTableColumn
cdot3OamErrFrameSecsSummaryThreshold = _Cdot3OamErrFrameSecsSummaryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5, 1, 13),
    _Cdot3OamErrFrameSecsSummaryThreshold_Type()
)
cdot3OamErrFrameSecsSummaryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamErrFrameSecsSummaryThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cdot3OamErrFrameSecsSummaryThreshold.setUnits("errored frame seconds")
_Cdot3OamErrFrameSecsEvNotifEnable_Type = TruthValue
_Cdot3OamErrFrameSecsEvNotifEnable_Object = MibTableColumn
cdot3OamErrFrameSecsEvNotifEnable = _Cdot3OamErrFrameSecsEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5, 1, 14),
    _Cdot3OamErrFrameSecsEvNotifEnable_Type()
)
cdot3OamErrFrameSecsEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamErrFrameSecsEvNotifEnable.setStatus("current")
_Cdot3OamDyingGaspEnable_Type = TruthValue
_Cdot3OamDyingGaspEnable_Object = MibTableColumn
cdot3OamDyingGaspEnable = _Cdot3OamDyingGaspEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5, 1, 15),
    _Cdot3OamDyingGaspEnable_Type()
)
cdot3OamDyingGaspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamDyingGaspEnable.setStatus("current")
_Cdot3OamCriticalEventEnable_Type = TruthValue
_Cdot3OamCriticalEventEnable_Object = MibTableColumn
cdot3OamCriticalEventEnable = _Cdot3OamCriticalEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 5, 1, 16),
    _Cdot3OamCriticalEventEnable_Type()
)
cdot3OamCriticalEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot3OamCriticalEventEnable.setStatus("current")
_Cdot3OamEventLogTable_Object = MibTable
cdot3OamEventLogTable = _Cdot3OamEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 6)
)
if mibBuilder.loadTexts:
    cdot3OamEventLogTable.setStatus("current")
_Cdot3OamEventLogEntry_Object = MibTableRow
cdot3OamEventLogEntry = _Cdot3OamEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 6, 1)
)
cdot3OamEventLogEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT3-OAM-MIB", "cdot3OamEventLogIndex"),
)
if mibBuilder.loadTexts:
    cdot3OamEventLogEntry.setStatus("current")
_Cdot3OamEventLogIndex_Type = Unsigned32
_Cdot3OamEventLogIndex_Object = MibTableColumn
cdot3OamEventLogIndex = _Cdot3OamEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 6, 1, 1),
    _Cdot3OamEventLogIndex_Type()
)
cdot3OamEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdot3OamEventLogIndex.setStatus("current")
_Cdot3OamEventLogTimestamp_Type = TimeStamp
_Cdot3OamEventLogTimestamp_Object = MibTableColumn
cdot3OamEventLogTimestamp = _Cdot3OamEventLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 6, 1, 2),
    _Cdot3OamEventLogTimestamp_Type()
)
cdot3OamEventLogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamEventLogTimestamp.setStatus("current")
_Cdot3OamEventLogOui_Type = Cdot3Oui
_Cdot3OamEventLogOui_Object = MibTableColumn
cdot3OamEventLogOui = _Cdot3OamEventLogOui_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 6, 1, 3),
    _Cdot3OamEventLogOui_Type()
)
cdot3OamEventLogOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamEventLogOui.setStatus("current")
_Cdot3OamEventLogType_Type = Unsigned32
_Cdot3OamEventLogType_Object = MibTableColumn
cdot3OamEventLogType = _Cdot3OamEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 6, 1, 4),
    _Cdot3OamEventLogType_Type()
)
cdot3OamEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamEventLogType.setStatus("current")


class _Cdot3OamEventLogLocation_Type(Integer32):
    """Custom type cdot3OamEventLogLocation based on Integer32"""
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


_Cdot3OamEventLogLocation_Type.__name__ = "Integer32"
_Cdot3OamEventLogLocation_Object = MibTableColumn
cdot3OamEventLogLocation = _Cdot3OamEventLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 6, 1, 5),
    _Cdot3OamEventLogLocation_Type()
)
cdot3OamEventLogLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamEventLogLocation.setStatus("current")
_Cdot3OamEventLogWindowHi_Type = Unsigned32
_Cdot3OamEventLogWindowHi_Object = MibTableColumn
cdot3OamEventLogWindowHi = _Cdot3OamEventLogWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 6, 1, 6),
    _Cdot3OamEventLogWindowHi_Type()
)
cdot3OamEventLogWindowHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamEventLogWindowHi.setStatus("current")
_Cdot3OamEventLogWindowLo_Type = Unsigned32
_Cdot3OamEventLogWindowLo_Object = MibTableColumn
cdot3OamEventLogWindowLo = _Cdot3OamEventLogWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 6, 1, 7),
    _Cdot3OamEventLogWindowLo_Type()
)
cdot3OamEventLogWindowLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamEventLogWindowLo.setStatus("current")
_Cdot3OamEventLogThresholdHi_Type = Unsigned32
_Cdot3OamEventLogThresholdHi_Object = MibTableColumn
cdot3OamEventLogThresholdHi = _Cdot3OamEventLogThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 6, 1, 8),
    _Cdot3OamEventLogThresholdHi_Type()
)
cdot3OamEventLogThresholdHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamEventLogThresholdHi.setStatus("current")
_Cdot3OamEventLogThresholdLo_Type = Unsigned32
_Cdot3OamEventLogThresholdLo_Object = MibTableColumn
cdot3OamEventLogThresholdLo = _Cdot3OamEventLogThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 6, 1, 9),
    _Cdot3OamEventLogThresholdLo_Type()
)
cdot3OamEventLogThresholdLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamEventLogThresholdLo.setStatus("current")
_Cdot3OamEventLogValue_Type = CounterBasedGauge64
_Cdot3OamEventLogValue_Object = MibTableColumn
cdot3OamEventLogValue = _Cdot3OamEventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 6, 1, 10),
    _Cdot3OamEventLogValue_Type()
)
cdot3OamEventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamEventLogValue.setStatus("current")
_Cdot3OamEventLogRunningTotal_Type = CounterBasedGauge64
_Cdot3OamEventLogRunningTotal_Object = MibTableColumn
cdot3OamEventLogRunningTotal = _Cdot3OamEventLogRunningTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 6, 1, 11),
    _Cdot3OamEventLogRunningTotal_Type()
)
cdot3OamEventLogRunningTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamEventLogRunningTotal.setStatus("current")
_Cdot3OamEventLogEventTotal_Type = Unsigned32
_Cdot3OamEventLogEventTotal_Object = MibTableColumn
cdot3OamEventLogEventTotal = _Cdot3OamEventLogEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 1, 6, 1, 12),
    _Cdot3OamEventLogEventTotal_Type()
)
cdot3OamEventLogEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot3OamEventLogEventTotal.setStatus("current")
_Cdot3OamConformance_ObjectIdentity = ObjectIdentity
cdot3OamConformance = _Cdot3OamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 2)
)
_Cdot3OamGroups_ObjectIdentity = ObjectIdentity
cdot3OamGroups = _Cdot3OamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 2, 1)
)
_Cdot3OamCompliances_ObjectIdentity = ObjectIdentity
cdot3OamCompliances = _Cdot3OamCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 2, 2)
)

# Managed Objects groups

cdot3OamControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 2, 1, 1)
)
cdot3OamControlGroup.setObjects(
      *(("CISCO-DOT3-OAM-MIB", "cdot3OamAdminState"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamOperStatus"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamMode"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamMaxOamPduSize"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamConfigRevision"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamFunctionsSupported"))
)
if mibBuilder.loadTexts:
    cdot3OamControlGroup.setStatus("current")

cdot3OamPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 2, 1, 2)
)
cdot3OamPeerGroup.setObjects(
      *(("CISCO-DOT3-OAM-MIB", "cdot3OamPeerMacAddress"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamPeerVendorOui"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamPeerVendorInfo"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamPeerMode"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamPeerFunctionsSupported"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamPeerMaxOamPduSize"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamPeerConfigRevision"))
)
if mibBuilder.loadTexts:
    cdot3OamPeerGroup.setStatus("current")

cdot3OamStatsBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 2, 1, 3)
)
cdot3OamStatsBaseGroup.setObjects(
      *(("CISCO-DOT3-OAM-MIB", "cdot3OamInformationTx"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamInformationRx"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamUniqueEventNotificationTx"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamUniqueEventNotificationRx"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamDuplicateEventNotificationTx"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamDuplicateEventNotificationRx"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamLoopbackControlTx"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamLoopbackControlRx"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamVariableRequestTx"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamVariableRequestRx"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamVariableResponseTx"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamVariableResponseRx"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamOrgSpecificTx"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamOrgSpecificRx"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamUnsupportedCodesTx"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamUnsupportedCodesRx"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamFramesLostDueToOam"))
)
if mibBuilder.loadTexts:
    cdot3OamStatsBaseGroup.setStatus("current")

cdot3OamLoopbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 2, 1, 4)
)
cdot3OamLoopbackGroup.setObjects(
      *(("CISCO-DOT3-OAM-MIB", "cdot3OamLoopbackStatus"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamLoopbackIgnoreRx"))
)
if mibBuilder.loadTexts:
    cdot3OamLoopbackGroup.setStatus("current")

cdot3OamErrSymbolPeriodEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 2, 1, 5)
)
cdot3OamErrSymbolPeriodEventGroup.setObjects(
      *(("CISCO-DOT3-OAM-MIB", "cdot3OamErrSymPeriodWindowHi"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamErrSymPeriodWindowLo"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamErrSymPeriodThresholdHi"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamErrSymPeriodThresholdLo"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamErrSymPeriodEvNotifEnable"))
)
if mibBuilder.loadTexts:
    cdot3OamErrSymbolPeriodEventGroup.setStatus("current")

cdot3OamErrFramePeriodEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 2, 1, 6)
)
cdot3OamErrFramePeriodEventGroup.setObjects(
      *(("CISCO-DOT3-OAM-MIB", "cdot3OamErrFramePeriodWindow"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamErrFramePeriodThreshold"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamErrFramePeriodEvNotifEnable"))
)
if mibBuilder.loadTexts:
    cdot3OamErrFramePeriodEventGroup.setStatus("current")

cdot3OamErrFrameEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 2, 1, 7)
)
cdot3OamErrFrameEventGroup.setObjects(
      *(("CISCO-DOT3-OAM-MIB", "cdot3OamErrFrameWindow"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamErrFrameThreshold"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamErrFrameEvNotifEnable"))
)
if mibBuilder.loadTexts:
    cdot3OamErrFrameEventGroup.setStatus("current")

cdot3OamErrFrameSecsSummaryEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 2, 1, 8)
)
cdot3OamErrFrameSecsSummaryEventGroup.setObjects(
      *(("CISCO-DOT3-OAM-MIB", "cdot3OamErrFrameSecsSummaryWindow"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamErrFrameSecsSummaryThreshold"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamErrFrameSecsEvNotifEnable"))
)
if mibBuilder.loadTexts:
    cdot3OamErrFrameSecsSummaryEventGroup.setStatus("current")

cdot3OamFlagEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 2, 1, 9)
)
cdot3OamFlagEventGroup.setObjects(
      *(("CISCO-DOT3-OAM-MIB", "cdot3OamDyingGaspEnable"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamCriticalEventEnable"))
)
if mibBuilder.loadTexts:
    cdot3OamFlagEventGroup.setStatus("current")

cdot3OamEventLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 2, 1, 10)
)
cdot3OamEventLogGroup.setObjects(
      *(("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogTimestamp"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogOui"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogType"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogLocation"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogWindowHi"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogWindowLo"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogThresholdHi"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogThresholdLo"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogValue"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogRunningTotal"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    cdot3OamEventLogGroup.setStatus("current")


# Notification objects

cdot3OamThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 0, 1)
)
cdot3OamThresholdEvent.setObjects(
      *(("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogTimestamp"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogOui"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogType"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogLocation"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogWindowHi"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogWindowLo"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogThresholdHi"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogThresholdLo"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogValue"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogRunningTotal"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    cdot3OamThresholdEvent.setStatus(
        "current"
    )

cdot3OamNonThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 0, 2)
)
cdot3OamNonThresholdEvent.setObjects(
      *(("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogTimestamp"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogOui"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogType"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogLocation"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    cdot3OamNonThresholdEvent.setStatus(
        "current"
    )


# Notifications groups

cdot3OamNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 2, 1, 11)
)
cdot3OamNotificationGroup.setObjects(
      *(("CISCO-DOT3-OAM-MIB", "cdot3OamThresholdEvent"),
        ("CISCO-DOT3-OAM-MIB", "cdot3OamNonThresholdEvent"))
)
if mibBuilder.loadTexts:
    cdot3OamNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cdot3OamCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 136, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cdot3OamCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOT3-OAM-MIB",
    **{"Cdot3Oui": Cdot3Oui,
       "cdot3OamMIB": cdot3OamMIB,
       "cdot3OamNotifications": cdot3OamNotifications,
       "cdot3OamThresholdEvent": cdot3OamThresholdEvent,
       "cdot3OamNonThresholdEvent": cdot3OamNonThresholdEvent,
       "cdot3OamObjects": cdot3OamObjects,
       "cdot3OamTable": cdot3OamTable,
       "cdot3OamEntry": cdot3OamEntry,
       "cdot3OamAdminState": cdot3OamAdminState,
       "cdot3OamOperStatus": cdot3OamOperStatus,
       "cdot3OamMode": cdot3OamMode,
       "cdot3OamMaxOamPduSize": cdot3OamMaxOamPduSize,
       "cdot3OamConfigRevision": cdot3OamConfigRevision,
       "cdot3OamFunctionsSupported": cdot3OamFunctionsSupported,
       "cdot3OamPeerTable": cdot3OamPeerTable,
       "cdot3OamPeerEntry": cdot3OamPeerEntry,
       "cdot3OamPeerMacAddress": cdot3OamPeerMacAddress,
       "cdot3OamPeerVendorOui": cdot3OamPeerVendorOui,
       "cdot3OamPeerVendorInfo": cdot3OamPeerVendorInfo,
       "cdot3OamPeerMode": cdot3OamPeerMode,
       "cdot3OamPeerMaxOamPduSize": cdot3OamPeerMaxOamPduSize,
       "cdot3OamPeerConfigRevision": cdot3OamPeerConfigRevision,
       "cdot3OamPeerFunctionsSupported": cdot3OamPeerFunctionsSupported,
       "cdot3OamLoopbackTable": cdot3OamLoopbackTable,
       "cdot3OamLoopbackEntry": cdot3OamLoopbackEntry,
       "cdot3OamLoopbackStatus": cdot3OamLoopbackStatus,
       "cdot3OamLoopbackIgnoreRx": cdot3OamLoopbackIgnoreRx,
       "cdot3OamStatsTable": cdot3OamStatsTable,
       "cdot3OamStatsEntry": cdot3OamStatsEntry,
       "cdot3OamInformationTx": cdot3OamInformationTx,
       "cdot3OamInformationRx": cdot3OamInformationRx,
       "cdot3OamUniqueEventNotificationTx": cdot3OamUniqueEventNotificationTx,
       "cdot3OamUniqueEventNotificationRx": cdot3OamUniqueEventNotificationRx,
       "cdot3OamDuplicateEventNotificationTx": cdot3OamDuplicateEventNotificationTx,
       "cdot3OamDuplicateEventNotificationRx": cdot3OamDuplicateEventNotificationRx,
       "cdot3OamLoopbackControlTx": cdot3OamLoopbackControlTx,
       "cdot3OamLoopbackControlRx": cdot3OamLoopbackControlRx,
       "cdot3OamVariableRequestTx": cdot3OamVariableRequestTx,
       "cdot3OamVariableRequestRx": cdot3OamVariableRequestRx,
       "cdot3OamVariableResponseTx": cdot3OamVariableResponseTx,
       "cdot3OamVariableResponseRx": cdot3OamVariableResponseRx,
       "cdot3OamOrgSpecificTx": cdot3OamOrgSpecificTx,
       "cdot3OamOrgSpecificRx": cdot3OamOrgSpecificRx,
       "cdot3OamUnsupportedCodesTx": cdot3OamUnsupportedCodesTx,
       "cdot3OamUnsupportedCodesRx": cdot3OamUnsupportedCodesRx,
       "cdot3OamFramesLostDueToOam": cdot3OamFramesLostDueToOam,
       "cdot3OamEventConfigTable": cdot3OamEventConfigTable,
       "cdot3OamEventConfigEntry": cdot3OamEventConfigEntry,
       "cdot3OamErrSymPeriodWindowHi": cdot3OamErrSymPeriodWindowHi,
       "cdot3OamErrSymPeriodWindowLo": cdot3OamErrSymPeriodWindowLo,
       "cdot3OamErrSymPeriodThresholdHi": cdot3OamErrSymPeriodThresholdHi,
       "cdot3OamErrSymPeriodThresholdLo": cdot3OamErrSymPeriodThresholdLo,
       "cdot3OamErrSymPeriodEvNotifEnable": cdot3OamErrSymPeriodEvNotifEnable,
       "cdot3OamErrFramePeriodWindow": cdot3OamErrFramePeriodWindow,
       "cdot3OamErrFramePeriodThreshold": cdot3OamErrFramePeriodThreshold,
       "cdot3OamErrFramePeriodEvNotifEnable": cdot3OamErrFramePeriodEvNotifEnable,
       "cdot3OamErrFrameWindow": cdot3OamErrFrameWindow,
       "cdot3OamErrFrameThreshold": cdot3OamErrFrameThreshold,
       "cdot3OamErrFrameEvNotifEnable": cdot3OamErrFrameEvNotifEnable,
       "cdot3OamErrFrameSecsSummaryWindow": cdot3OamErrFrameSecsSummaryWindow,
       "cdot3OamErrFrameSecsSummaryThreshold": cdot3OamErrFrameSecsSummaryThreshold,
       "cdot3OamErrFrameSecsEvNotifEnable": cdot3OamErrFrameSecsEvNotifEnable,
       "cdot3OamDyingGaspEnable": cdot3OamDyingGaspEnable,
       "cdot3OamCriticalEventEnable": cdot3OamCriticalEventEnable,
       "cdot3OamEventLogTable": cdot3OamEventLogTable,
       "cdot3OamEventLogEntry": cdot3OamEventLogEntry,
       "cdot3OamEventLogIndex": cdot3OamEventLogIndex,
       "cdot3OamEventLogTimestamp": cdot3OamEventLogTimestamp,
       "cdot3OamEventLogOui": cdot3OamEventLogOui,
       "cdot3OamEventLogType": cdot3OamEventLogType,
       "cdot3OamEventLogLocation": cdot3OamEventLogLocation,
       "cdot3OamEventLogWindowHi": cdot3OamEventLogWindowHi,
       "cdot3OamEventLogWindowLo": cdot3OamEventLogWindowLo,
       "cdot3OamEventLogThresholdHi": cdot3OamEventLogThresholdHi,
       "cdot3OamEventLogThresholdLo": cdot3OamEventLogThresholdLo,
       "cdot3OamEventLogValue": cdot3OamEventLogValue,
       "cdot3OamEventLogRunningTotal": cdot3OamEventLogRunningTotal,
       "cdot3OamEventLogEventTotal": cdot3OamEventLogEventTotal,
       "cdot3OamConformance": cdot3OamConformance,
       "cdot3OamGroups": cdot3OamGroups,
       "cdot3OamControlGroup": cdot3OamControlGroup,
       "cdot3OamPeerGroup": cdot3OamPeerGroup,
       "cdot3OamStatsBaseGroup": cdot3OamStatsBaseGroup,
       "cdot3OamLoopbackGroup": cdot3OamLoopbackGroup,
       "cdot3OamErrSymbolPeriodEventGroup": cdot3OamErrSymbolPeriodEventGroup,
       "cdot3OamErrFramePeriodEventGroup": cdot3OamErrFramePeriodEventGroup,
       "cdot3OamErrFrameEventGroup": cdot3OamErrFrameEventGroup,
       "cdot3OamErrFrameSecsSummaryEventGroup": cdot3OamErrFrameSecsSummaryEventGroup,
       "cdot3OamFlagEventGroup": cdot3OamFlagEventGroup,
       "cdot3OamEventLogGroup": cdot3OamEventLogGroup,
       "cdot3OamNotificationGroup": cdot3OamNotificationGroup,
       "cdot3OamCompliances": cdot3OamCompliances,
       "cdot3OamCompliance": cdot3OamCompliance}
)
