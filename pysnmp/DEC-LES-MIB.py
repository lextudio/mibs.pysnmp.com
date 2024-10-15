# SNMP MIB module (DEC-LES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEC-LES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:36 2024
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

(decMIBextension,) = mibBuilder.importSymbols(
    "DECATM-MIB",
    "decMIBextension")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DecLesMIB_ObjectIdentity = ObjectIdentity
decLesMIB = _DecLesMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28)
)
_DecLesMIBObjects_ObjectIdentity = ObjectIdentity
decLesMIBObjects = _DecLesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1)
)
_DecLesConfigTable_Object = MibTable
decLesConfigTable = _DecLesConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1)
)
if mibBuilder.loadTexts:
    decLesConfigTable.setStatus("mandatory")
_DecLesConfigEntry_Object = MibTableRow
decLesConfigEntry = _DecLesConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1)
)
decLesConfigEntry.setIndexNames(
    (0, "DEC-LES-MIB", "decLesIndex"),
)
if mibBuilder.loadTexts:
    decLesConfigEntry.setStatus("mandatory")
_DecLesIndex_Type = Integer32
_DecLesIndex_Object = MibTableColumn
decLesIndex = _DecLesIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1, 1),
    _DecLesIndex_Type()
)
decLesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesIndex.setStatus("mandatory")


class _DecLesRowStatus_Type(Integer32):
    """Custom type decLesRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecLesRowStatus_Type.__name__ = "Integer32"
_DecLesRowStatus_Object = MibTableColumn
decLesRowStatus = _DecLesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1, 2),
    _DecLesRowStatus_Type()
)
decLesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesRowStatus.setStatus("mandatory")


class _DecLesAdminStatus_Type(Integer32):
    """Custom type decLesAdminStatus based on Integer32"""
    defaultValue = 2

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


_DecLesAdminStatus_Type.__name__ = "Integer32"
_DecLesAdminStatus_Object = MibTableColumn
decLesAdminStatus = _DecLesAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1, 3),
    _DecLesAdminStatus_Type()
)
decLesAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesAdminStatus.setStatus("mandatory")


class _DecLesOperStatus_Type(Integer32):
    """Custom type decLesOperStatus based on Integer32"""
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
        *(("deleting", 4),
          ("disabling", 3),
          ("down", 2),
          ("up", 1))
    )


_DecLesOperStatus_Type.__name__ = "Integer32"
_DecLesOperStatus_Object = MibTableColumn
decLesOperStatus = _DecLesOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1, 4),
    _DecLesOperStatus_Type()
)
decLesOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesOperStatus.setStatus("mandatory")
_DecLesLastChange_Type = TimeTicks
_DecLesLastChange_Object = MibTableColumn
decLesLastChange = _DecLesLastChange_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1, 5),
    _DecLesLastChange_Type()
)
decLesLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesLastChange.setStatus("mandatory")


class _DecLesAtmAddress_Type(OctetString):
    """Custom type decLesAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecLesAtmAddress_Type.__name__ = "OctetString"
_DecLesAtmAddress_Object = MibTableColumn
decLesAtmAddress = _DecLesAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1, 6),
    _DecLesAtmAddress_Type()
)
decLesAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesAtmAddress.setStatus("mandatory")


class _DecLesDescription_Type(OctetString):
    """Custom type decLesDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DecLesDescription_Type.__name__ = "OctetString"
_DecLesDescription_Object = MibTableColumn
decLesDescription = _DecLesDescription_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1, 7),
    _DecLesDescription_Type()
)
decLesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesDescription.setStatus("mandatory")


class _DecLesLanName_Type(OctetString):
    """Custom type decLesLanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DecLesLanName_Type.__name__ = "OctetString"
_DecLesLanName_Object = MibTableColumn
decLesLanName = _DecLesLanName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1, 8),
    _DecLesLanName_Type()
)
decLesLanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesLanName.setStatus("mandatory")


class _DecLesLanType_Type(Integer32):
    """Custom type decLesLanType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aflane8023", 2),
          ("aflane8025", 3))
    )


_DecLesLanType_Type.__name__ = "Integer32"
_DecLesLanType_Object = MibTableColumn
decLesLanType = _DecLesLanType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1, 9),
    _DecLesLanType_Type()
)
decLesLanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesLanType.setStatus("mandatory")


class _DecLesMaxDataFrameSize_Type(Integer32):
    """Custom type decLesMaxDataFrameSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("max1516", 2),
          ("max18190", 5),
          ("max4544", 3),
          ("max9234", 4))
    )


_DecLesMaxDataFrameSize_Type.__name__ = "Integer32"
_DecLesMaxDataFrameSize_Object = MibTableColumn
decLesMaxDataFrameSize = _DecLesMaxDataFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1, 10),
    _DecLesMaxDataFrameSize_Type()
)
decLesMaxDataFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesMaxDataFrameSize.setStatus("mandatory")


class _DecLesAtmAddressOfBUS_Type(OctetString):
    """Custom type decLesAtmAddressOfBUS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecLesAtmAddressOfBUS_Type.__name__ = "OctetString"
_DecLesAtmAddressOfBUS_Object = MibTableColumn
decLesAtmAddressOfBUS = _DecLesAtmAddressOfBUS_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1, 11),
    _DecLesAtmAddressOfBUS_Type()
)
decLesAtmAddressOfBUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesAtmAddressOfBUS.setStatus("mandatory")


class _DecLesControlTimeout_Type(Integer32):
    """Custom type decLesControlTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_DecLesControlTimeout_Type.__name__ = "Integer32"
_DecLesControlTimeout_Object = MibTableColumn
decLesControlTimeout = _DecLesControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1, 12),
    _DecLesControlTimeout_Type()
)
decLesControlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesControlTimeout.setStatus("mandatory")


class _DecLesArpResponsePolicy_Type(Integer32):
    """Custom type decLesArpResponsePolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 3),
          ("direct", 2),
          ("unspecified", 1))
    )


_DecLesArpResponsePolicy_Type.__name__ = "Integer32"
_DecLesArpResponsePolicy_Object = MibTableColumn
decLesArpResponsePolicy = _DecLesArpResponsePolicy_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1, 13),
    _DecLesArpResponsePolicy_Type()
)
decLesArpResponsePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesArpResponsePolicy.setStatus("mandatory")


class _DecLesNarpRequestPolicy_Type(Integer32):
    """Custom type decLesNarpRequestPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 2),
          ("forward", 1))
    )


_DecLesNarpRequestPolicy_Type.__name__ = "Integer32"
_DecLesNarpRequestPolicy_Object = MibTableColumn
decLesNarpRequestPolicy = _DecLesNarpRequestPolicy_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1, 14),
    _DecLesNarpRequestPolicy_Type()
)
decLesNarpRequestPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesNarpRequestPolicy.setStatus("mandatory")


class _DecLesTopologyChangeMode_Type(Integer32):
    """Custom type decLesTopologyChangeMode based on Integer32"""
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


_DecLesTopologyChangeMode_Type.__name__ = "Integer32"
_DecLesTopologyChangeMode_Object = MibTableColumn
decLesTopologyChangeMode = _DecLesTopologyChangeMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1, 15),
    _DecLesTopologyChangeMode_Type()
)
decLesTopologyChangeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesTopologyChangeMode.setStatus("mandatory")
_DecLesLastTcModeChange_Type = TimeTicks
_DecLesLastTcModeChange_Object = MibTableColumn
decLesLastTcModeChange = _DecLesLastTcModeChange_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1, 16),
    _DecLesLastTcModeChange_Type()
)
decLesLastTcModeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesLastTcModeChange.setStatus("mandatory")


class _DecLesTopologyChangeTimeout_Type(Integer32):
    """Custom type decLesTopologyChangeTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_DecLesTopologyChangeTimeout_Type.__name__ = "Integer32"
_DecLesTopologyChangeTimeout_Object = MibTableColumn
decLesTopologyChangeTimeout = _DecLesTopologyChangeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 1, 1, 17),
    _DecLesTopologyChangeTimeout_Type()
)
decLesTopologyChangeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesTopologyChangeTimeout.setStatus("mandatory")
_DecLesClientStatesTable_Object = MibTable
decLesClientStatesTable = _DecLesClientStatesTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 2)
)
if mibBuilder.loadTexts:
    decLesClientStatesTable.setStatus("mandatory")
_DecLesClientStatesEntry_Object = MibTableRow
decLesClientStatesEntry = _DecLesClientStatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 2, 1)
)
decLesClientStatesEntry.setIndexNames(
    (0, "DEC-LES-MIB", "decLesIndex"),
)
if mibBuilder.loadTexts:
    decLesClientStatesEntry.setStatus("mandatory")
_DecLesActiveClients_Type = Integer32
_DecLesActiveClients_Object = MibTableColumn
decLesActiveClients = _DecLesActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 2, 1, 1),
    _DecLesActiveClients_Type()
)
decLesActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesActiveClients.setStatus("mandatory")
_DecLesActiveProxyClients_Type = Integer32
_DecLesActiveProxyClients_Object = MibTableColumn
decLesActiveProxyClients = _DecLesActiveProxyClients_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 2, 1, 2),
    _DecLesActiveProxyClients_Type()
)
decLesActiveProxyClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesActiveProxyClients.setStatus("mandatory")
_DecLesAwaitingJoinRequest_Type = Integer32
_DecLesAwaitingJoinRequest_Object = MibTableColumn
decLesAwaitingJoinRequest = _DecLesAwaitingJoinRequest_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 2, 1, 3),
    _DecLesAwaitingJoinRequest_Type()
)
decLesAwaitingJoinRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesAwaitingJoinRequest.setStatus("mandatory")
_DecLesCtlDistributeInProgress_Type = Integer32
_DecLesCtlDistributeInProgress_Object = MibTableColumn
decLesCtlDistributeInProgress = _DecLesCtlDistributeInProgress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 2, 1, 4),
    _DecLesCtlDistributeInProgress_Type()
)
decLesCtlDistributeInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesCtlDistributeInProgress.setStatus("mandatory")
_DecLesTerminating_Type = Integer32
_DecLesTerminating_Object = MibTableColumn
decLesTerminating = _DecLesTerminating_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 2, 1, 5),
    _DecLesTerminating_Type()
)
decLesTerminating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesTerminating.setStatus("mandatory")
_DecLesClientTable_Object = MibTable
decLesClientTable = _DecLesClientTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 3)
)
if mibBuilder.loadTexts:
    decLesClientTable.setStatus("mandatory")
_DecLesClientEntry_Object = MibTableRow
decLesClientEntry = _DecLesClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 3, 1)
)
decLesClientEntry.setIndexNames(
    (0, "DEC-LES-MIB", "decLesIndex"),
    (0, "DEC-LES-MIB", "decLesClientID"),
)
if mibBuilder.loadTexts:
    decLesClientEntry.setStatus("mandatory")


class _DecLesClientID_Type(Integer32):
    """Custom type decLesClientID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65279),
    )


_DecLesClientID_Type.__name__ = "Integer32"
_DecLesClientID_Object = MibTableColumn
decLesClientID = _DecLesClientID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 3, 1, 1),
    _DecLesClientID_Type()
)
decLesClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesClientID.setStatus("mandatory")


class _DecLesClientAtmAddress_Type(OctetString):
    """Custom type decLesClientAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecLesClientAtmAddress_Type.__name__ = "OctetString"
_DecLesClientAtmAddress_Object = MibTableColumn
decLesClientAtmAddress = _DecLesClientAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 3, 1, 2),
    _DecLesClientAtmAddress_Type()
)
decLesClientAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesClientAtmAddress.setStatus("mandatory")


class _DecLesClientIsProxy_Type(Integer32):
    """Custom type decLesClientIsProxy based on Integer32"""
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


_DecLesClientIsProxy_Type.__name__ = "Integer32"
_DecLesClientIsProxy_Object = MibTableColumn
decLesClientIsProxy = _DecLesClientIsProxy_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 3, 1, 3),
    _DecLesClientIsProxy_Type()
)
decLesClientIsProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesClientIsProxy.setStatus("mandatory")


class _DecLesClientState_Type(Integer32):
    """Custom type decLesClientState based on Integer32"""
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
        *(("deleting", 6),
          ("joining", 4),
          ("lesConnect", 3),
          ("noLesConnect", 2),
          ("operational", 5),
          ("other", 1))
    )


_DecLesClientState_Type.__name__ = "Integer32"
_DecLesClientState_Object = MibTableColumn
decLesClientState = _DecLesClientState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 3, 1, 4),
    _DecLesClientState_Type()
)
decLesClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesClientState.setStatus("mandatory")


class _DecLesClientRowStatus_Type(Integer32):
    """Custom type decLesClientRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecLesClientRowStatus_Type.__name__ = "Integer32"
_DecLesClientRowStatus_Object = MibTableColumn
decLesClientRowStatus = _DecLesClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 3, 1, 5),
    _DecLesClientRowStatus_Type()
)
decLesClientRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesClientRowStatus.setStatus("mandatory")
_DecLesLecTable_Object = MibTable
decLesLecTable = _DecLesLecTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 4)
)
if mibBuilder.loadTexts:
    decLesLecTable.setStatus("mandatory")
_DecLesLecEntry_Object = MibTableRow
decLesLecEntry = _DecLesLecEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 4, 1)
)
decLesLecEntry.setIndexNames(
    (0, "DEC-LES-MIB", "decLesIndex"),
    (0, "DEC-LES-MIB", "decLesLecAtmAddress"),
)
if mibBuilder.loadTexts:
    decLesLecEntry.setStatus("mandatory")


class _DecLesLecAtmAddress_Type(OctetString):
    """Custom type decLesLecAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecLesLecAtmAddress_Type.__name__ = "OctetString"
_DecLesLecAtmAddress_Object = MibTableColumn
decLesLecAtmAddress = _DecLesLecAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 4, 1, 1),
    _DecLesLecAtmAddress_Type()
)
decLesLecAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesLecAtmAddress.setStatus("mandatory")


class _DecLesLecID_Type(Integer32):
    """Custom type decLesLecID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65279),
    )


_DecLesLecID_Type.__name__ = "Integer32"
_DecLesLecID_Object = MibTableColumn
decLesLecID = _DecLesLecID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 4, 1, 2),
    _DecLesLecID_Type()
)
decLesLecID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesLecID.setStatus("mandatory")


class _DecLesLecIsProxy_Type(Integer32):
    """Custom type decLesLecIsProxy based on Integer32"""
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


_DecLesLecIsProxy_Type.__name__ = "Integer32"
_DecLesLecIsProxy_Object = MibTableColumn
decLesLecIsProxy = _DecLesLecIsProxy_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 4, 1, 3),
    _DecLesLecIsProxy_Type()
)
decLesLecIsProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesLecIsProxy.setStatus("mandatory")


class _DecLesLecState_Type(Integer32):
    """Custom type decLesLecState based on Integer32"""
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
        *(("deleting", 6),
          ("joining", 4),
          ("lesConnect", 3),
          ("noLesConnect", 2),
          ("operational", 5),
          ("other", 1))
    )


_DecLesLecState_Type.__name__ = "Integer32"
_DecLesLecState_Object = MibTableColumn
decLesLecState = _DecLesLecState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 4, 1, 4),
    _DecLesLecState_Type()
)
decLesLecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesLecState.setStatus("mandatory")


class _DecLesLecRowStatus_Type(Integer32):
    """Custom type decLesLecRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecLesLecRowStatus_Type.__name__ = "Integer32"
_DecLesLecRowStatus_Object = MibTableColumn
decLesLecRowStatus = _DecLesLecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 4, 1, 5),
    _DecLesLecRowStatus_Type()
)
decLesLecRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesLecRowStatus.setStatus("mandatory")
_DecLesCtlDirectTable_Object = MibTable
decLesCtlDirectTable = _DecLesCtlDirectTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 5)
)
if mibBuilder.loadTexts:
    decLesCtlDirectTable.setStatus("mandatory")
_DecLesCtlDirectEntry_Object = MibTableRow
decLesCtlDirectEntry = _DecLesCtlDirectEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 5, 1)
)
decLesCtlDirectEntry.setIndexNames(
    (0, "DEC-LES-MIB", "decLesIndex"),
    (0, "DEC-LES-MIB", "decLesLecAtmAddress"),
)
if mibBuilder.loadTexts:
    decLesCtlDirectEntry.setStatus("mandatory")


class _DecLesControlDirectInterface_Type(Integer32):
    """Custom type decLesControlDirectInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DecLesControlDirectInterface_Type.__name__ = "Integer32"
_DecLesControlDirectInterface_Object = MibTableColumn
decLesControlDirectInterface = _DecLesControlDirectInterface_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 5, 1, 1),
    _DecLesControlDirectInterface_Type()
)
decLesControlDirectInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesControlDirectInterface.setStatus("mandatory")


class _DecLesControlDirectVpi_Type(Integer32):
    """Custom type decLesControlDirectVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DecLesControlDirectVpi_Type.__name__ = "Integer32"
_DecLesControlDirectVpi_Object = MibTableColumn
decLesControlDirectVpi = _DecLesControlDirectVpi_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 5, 1, 2),
    _DecLesControlDirectVpi_Type()
)
decLesControlDirectVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesControlDirectVpi.setStatus("mandatory")


class _DecLesControlDirectVci_Type(Integer32):
    """Custom type decLesControlDirectVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DecLesControlDirectVci_Type.__name__ = "Integer32"
_DecLesControlDirectVci_Object = MibTableColumn
decLesControlDirectVci = _DecLesControlDirectVci_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 5, 1, 3),
    _DecLesControlDirectVci_Type()
)
decLesControlDirectVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesControlDirectVci.setStatus("mandatory")


class _DecLesControlDirectRowStatus_Type(Integer32):
    """Custom type decLesControlDirectRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecLesControlDirectRowStatus_Type.__name__ = "Integer32"
_DecLesControlDirectRowStatus_Object = MibTableColumn
decLesControlDirectRowStatus = _DecLesControlDirectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 5, 1, 4),
    _DecLesControlDirectRowStatus_Type()
)
decLesControlDirectRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesControlDirectRowStatus.setStatus("mandatory")
_DecLesCtlDistTable_Object = MibTable
decLesCtlDistTable = _DecLesCtlDistTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 6)
)
if mibBuilder.loadTexts:
    decLesCtlDistTable.setStatus("mandatory")
_DecLesCtlDistEntry_Object = MibTableRow
decLesCtlDistEntry = _DecLesCtlDistEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 6, 1)
)
decLesCtlDistEntry.setIndexNames(
    (0, "DEC-LES-MIB", "decLesIndex"),
    (0, "DEC-LES-MIB", "decLesControlDistInterface"),
    (0, "DEC-LES-MIB", "decLesControlDistVpi"),
    (0, "DEC-LES-MIB", "decLesControlDistVci"),
)
if mibBuilder.loadTexts:
    decLesCtlDistEntry.setStatus("mandatory")


class _DecLesControlDistInterface_Type(Integer32):
    """Custom type decLesControlDistInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DecLesControlDistInterface_Type.__name__ = "Integer32"
_DecLesControlDistInterface_Object = MibTableColumn
decLesControlDistInterface = _DecLesControlDistInterface_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 6, 1, 1),
    _DecLesControlDistInterface_Type()
)
decLesControlDistInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesControlDistInterface.setStatus("mandatory")


class _DecLesControlDistVpi_Type(Integer32):
    """Custom type decLesControlDistVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DecLesControlDistVpi_Type.__name__ = "Integer32"
_DecLesControlDistVpi_Object = MibTableColumn
decLesControlDistVpi = _DecLesControlDistVpi_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 6, 1, 2),
    _DecLesControlDistVpi_Type()
)
decLesControlDistVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesControlDistVpi.setStatus("mandatory")


class _DecLesControlDistVci_Type(Integer32):
    """Custom type decLesControlDistVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DecLesControlDistVci_Type.__name__ = "Integer32"
_DecLesControlDistVci_Object = MibTableColumn
decLesControlDistVci = _DecLesControlDistVci_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 6, 1, 3),
    _DecLesControlDistVci_Type()
)
decLesControlDistVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesControlDistVci.setStatus("mandatory")


class _DecLesControlDistRowStatus_Type(Integer32):
    """Custom type decLesControlDistRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecLesControlDistRowStatus_Type.__name__ = "Integer32"
_DecLesControlDistRowStatus_Object = MibTableColumn
decLesControlDistRowStatus = _DecLesControlDistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 6, 1, 4),
    _DecLesControlDistRowStatus_Type()
)
decLesControlDistRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesControlDistRowStatus.setStatus("mandatory")
_DecLesMacAddressTable_Object = MibTable
decLesMacAddressTable = _DecLesMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 7)
)
if mibBuilder.loadTexts:
    decLesMacAddressTable.setStatus("mandatory")
_DecLesMacAddressEntry_Object = MibTableRow
decLesMacAddressEntry = _DecLesMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 7, 1)
)
decLesMacAddressEntry.setIndexNames(
    (0, "DEC-LES-MIB", "decLesIndex"),
    (0, "DEC-LES-MIB", "decLesMacAddress"),
)
if mibBuilder.loadTexts:
    decLesMacAddressEntry.setStatus("mandatory")


class _DecLesMacAddress_Type(OctetString):
    """Custom type decLesMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_DecLesMacAddress_Type.__name__ = "OctetString"
_DecLesMacAddress_Object = MibTableColumn
decLesMacAddress = _DecLesMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 7, 1, 1),
    _DecLesMacAddress_Type()
)
decLesMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesMacAddress.setStatus("mandatory")
_DecLesMacAddressOwner_Type = Integer32
_DecLesMacAddressOwner_Object = MibTableColumn
decLesMacAddressOwner = _DecLesMacAddressOwner_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 7, 1, 2),
    _DecLesMacAddressOwner_Type()
)
decLesMacAddressOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesMacAddressOwner.setStatus("mandatory")


class _DecLesMacAddressAtmBinding_Type(OctetString):
    """Custom type decLesMacAddressAtmBinding based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecLesMacAddressAtmBinding_Type.__name__ = "OctetString"
_DecLesMacAddressAtmBinding_Object = MibTableColumn
decLesMacAddressAtmBinding = _DecLesMacAddressAtmBinding_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 7, 1, 3),
    _DecLesMacAddressAtmBinding_Type()
)
decLesMacAddressAtmBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesMacAddressAtmBinding.setStatus("mandatory")
_DecLesRouteDescrTable_Object = MibTable
decLesRouteDescrTable = _DecLesRouteDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 8)
)
if mibBuilder.loadTexts:
    decLesRouteDescrTable.setStatus("mandatory")
_DecLesRouteDescrEntry_Object = MibTableRow
decLesRouteDescrEntry = _DecLesRouteDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 8, 1)
)
decLesRouteDescrEntry.setIndexNames(
    (0, "DEC-LES-MIB", "decLesIndex"),
    (0, "DEC-LES-MIB", "decLesRouteDescrSegmentID"),
    (0, "DEC-LES-MIB", "decLesRouteDescrBridgeNumber"),
)
if mibBuilder.loadTexts:
    decLesRouteDescrEntry.setStatus("mandatory")


class _DecLesRouteDescrSegmentID_Type(Integer32):
    """Custom type decLesRouteDescrSegmentID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_DecLesRouteDescrSegmentID_Type.__name__ = "Integer32"
_DecLesRouteDescrSegmentID_Object = MibTableColumn
decLesRouteDescrSegmentID = _DecLesRouteDescrSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 8, 1, 1),
    _DecLesRouteDescrSegmentID_Type()
)
decLesRouteDescrSegmentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRouteDescrSegmentID.setStatus("mandatory")


class _DecLesRouteDescrBridgeNumber_Type(Integer32):
    """Custom type decLesRouteDescrBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DecLesRouteDescrBridgeNumber_Type.__name__ = "Integer32"
_DecLesRouteDescrBridgeNumber_Object = MibTableColumn
decLesRouteDescrBridgeNumber = _DecLesRouteDescrBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 8, 1, 2),
    _DecLesRouteDescrBridgeNumber_Type()
)
decLesRouteDescrBridgeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRouteDescrBridgeNumber.setStatus("mandatory")
_DecLesRouteDescrOwner_Type = Integer32
_DecLesRouteDescrOwner_Object = MibTableColumn
decLesRouteDescrOwner = _DecLesRouteDescrOwner_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 8, 1, 3),
    _DecLesRouteDescrOwner_Type()
)
decLesRouteDescrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRouteDescrOwner.setStatus("mandatory")


class _DecLesRouteDescrAtmBinding_Type(OctetString):
    """Custom type decLesRouteDescrAtmBinding based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecLesRouteDescrAtmBinding_Type.__name__ = "OctetString"
_DecLesRouteDescrAtmBinding_Object = MibTableColumn
decLesRouteDescrAtmBinding = _DecLesRouteDescrAtmBinding_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 8, 1, 4),
    _DecLesRouteDescrAtmBinding_Type()
)
decLesRouteDescrAtmBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRouteDescrAtmBinding.setStatus("mandatory")
_DecLesTrafficTable_Object = MibTable
decLesTrafficTable = _DecLesTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 9)
)
if mibBuilder.loadTexts:
    decLesTrafficTable.setStatus("mandatory")
_DecLesTrafficEntry_Object = MibTableRow
decLesTrafficEntry = _DecLesTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 9, 1)
)
decLesTrafficEntry.setIndexNames(
    (0, "DEC-LES-MIB", "decLesIndex"),
)
if mibBuilder.loadTexts:
    decLesTrafficEntry.setStatus("mandatory")
_DecLesControlFramesIn_Type = Counter32
_DecLesControlFramesIn_Object = MibTableColumn
decLesControlFramesIn = _DecLesControlFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 9, 1, 1),
    _DecLesControlFramesIn_Type()
)
decLesControlFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesControlFramesIn.setStatus("mandatory")
_DecLesShortFrames_Type = Counter32
_DecLesShortFrames_Object = MibTableColumn
decLesShortFrames = _DecLesShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 9, 1, 2),
    _DecLesShortFrames_Type()
)
decLesShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesShortFrames.setStatus("mandatory")
_DecLesUnjoinedClientFrames_Type = Counter32
_DecLesUnjoinedClientFrames_Object = MibTableColumn
decLesUnjoinedClientFrames = _DecLesUnjoinedClientFrames_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 9, 1, 3),
    _DecLesUnjoinedClientFrames_Type()
)
decLesUnjoinedClientFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesUnjoinedClientFrames.setStatus("mandatory")
_DecLesVersionsNotSupported_Type = Counter32
_DecLesVersionsNotSupported_Object = MibTableColumn
decLesVersionsNotSupported = _DecLesVersionsNotSupported_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 9, 1, 4),
    _DecLesVersionsNotSupported_Type()
)
decLesVersionsNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesVersionsNotSupported.setStatus("mandatory")
_DecLesInvalidFrames_Type = Counter32
_DecLesInvalidFrames_Object = MibTableColumn
decLesInvalidFrames = _DecLesInvalidFrames_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 9, 1, 5),
    _DecLesInvalidFrames_Type()
)
decLesInvalidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesInvalidFrames.setStatus("mandatory")
_DecLesReceiveQueueDiscards_Type = Counter32
_DecLesReceiveQueueDiscards_Object = MibTableColumn
decLesReceiveQueueDiscards = _DecLesReceiveQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 9, 1, 6),
    _DecLesReceiveQueueDiscards_Type()
)
decLesReceiveQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesReceiveQueueDiscards.setStatus("mandatory")
_DecLesMiscDiscards_Type = Counter32
_DecLesMiscDiscards_Object = MibTableColumn
decLesMiscDiscards = _DecLesMiscDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 9, 1, 7),
    _DecLesMiscDiscards_Type()
)
decLesMiscDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesMiscDiscards.setStatus("mandatory")
_DecLesCallStatsTable_Object = MibTable
decLesCallStatsTable = _DecLesCallStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 10)
)
if mibBuilder.loadTexts:
    decLesCallStatsTable.setStatus("mandatory")
_DecLesCallStatsEntry_Object = MibTableRow
decLesCallStatsEntry = _DecLesCallStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 10, 1)
)
decLesCallStatsEntry.setIndexNames(
    (0, "DEC-LES-MIB", "decLesIndex"),
)
if mibBuilder.loadTexts:
    decLesCallStatsEntry.setStatus("mandatory")
_DecLesCtlDirectCalls_Type = Counter32
_DecLesCtlDirectCalls_Object = MibTableColumn
decLesCtlDirectCalls = _DecLesCtlDirectCalls_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 10, 1, 1),
    _DecLesCtlDirectCalls_Type()
)
decLesCtlDirectCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesCtlDirectCalls.setStatus("mandatory")
_DecLesCtlDirectFailures_Type = Counter32
_DecLesCtlDirectFailures_Object = MibTableColumn
decLesCtlDirectFailures = _DecLesCtlDirectFailures_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 10, 1, 2),
    _DecLesCtlDirectFailures_Type()
)
decLesCtlDirectFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesCtlDirectFailures.setStatus("mandatory")
_DecLesCtlDirectOutOfResources_Type = Counter32
_DecLesCtlDirectOutOfResources_Object = MibTableColumn
decLesCtlDirectOutOfResources = _DecLesCtlDirectOutOfResources_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 10, 1, 3),
    _DecLesCtlDirectOutOfResources_Type()
)
decLesCtlDirectOutOfResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesCtlDirectOutOfResources.setStatus("mandatory")
_DecLesCtlDirectInvalidInfoElements_Type = Counter32
_DecLesCtlDirectInvalidInfoElements_Object = MibTableColumn
decLesCtlDirectInvalidInfoElements = _DecLesCtlDirectInvalidInfoElements_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 10, 1, 4),
    _DecLesCtlDirectInvalidInfoElements_Type()
)
decLesCtlDirectInvalidInfoElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesCtlDirectInvalidInfoElements.setStatus("mandatory")
_DecLesCtlDistributeCalls_Type = Counter32
_DecLesCtlDistributeCalls_Object = MibTableColumn
decLesCtlDistributeCalls = _DecLesCtlDistributeCalls_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 10, 1, 5),
    _DecLesCtlDistributeCalls_Type()
)
decLesCtlDistributeCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesCtlDistributeCalls.setStatus("mandatory")
_DecLesCtlDistributeFailures_Type = Counter32
_DecLesCtlDistributeFailures_Object = MibTableColumn
decLesCtlDistributeFailures = _DecLesCtlDistributeFailures_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 10, 1, 6),
    _DecLesCtlDistributeFailures_Type()
)
decLesCtlDistributeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesCtlDistributeFailures.setStatus("mandatory")
_DecLesCtlDistribOutOfResources_Type = Counter32
_DecLesCtlDistribOutOfResources_Object = MibTableColumn
decLesCtlDistribOutOfResources = _DecLesCtlDistribOutOfResources_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 10, 1, 7),
    _DecLesCtlDistribOutOfResources_Type()
)
decLesCtlDistribOutOfResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesCtlDistribOutOfResources.setStatus("mandatory")
_DecLesJoinTable_Object = MibTable
decLesJoinTable = _DecLesJoinTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11)
)
if mibBuilder.loadTexts:
    decLesJoinTable.setStatus("mandatory")
_DecLesJoinEntry_Object = MibTableRow
decLesJoinEntry = _DecLesJoinEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1)
)
decLesJoinEntry.setIndexNames(
    (0, "DEC-LES-MIB", "decLesIndex"),
)
if mibBuilder.loadTexts:
    decLesJoinEntry.setStatus("mandatory")
_DecLesJoinRequests_Type = Counter32
_DecLesJoinRequests_Object = MibTableColumn
decLesJoinRequests = _DecLesJoinRequests_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 1),
    _DecLesJoinRequests_Type()
)
decLesJoinRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinRequests.setStatus("mandatory")
_DecLesJoinSuccesses_Type = Counter32
_DecLesJoinSuccesses_Object = MibTableColumn
decLesJoinSuccesses = _DecLesJoinSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 2),
    _DecLesJoinSuccesses_Type()
)
decLesJoinSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinSuccesses.setStatus("mandatory")
_DecLesJoinFailures_Type = Counter32
_DecLesJoinFailures_Object = MibTableColumn
decLesJoinFailures = _DecLesJoinFailures_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 3),
    _DecLesJoinFailures_Type()
)
decLesJoinFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinFailures.setStatus("mandatory")
_DecLesJoinDuplicates_Type = Counter32
_DecLesJoinDuplicates_Object = MibTableColumn
decLesJoinDuplicates = _DecLesJoinDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 4),
    _DecLesJoinDuplicates_Type()
)
decLesJoinDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinDuplicates.setStatus("mandatory")
_DecLesJoinNonDuplicates_Type = Counter32
_DecLesJoinNonDuplicates_Object = MibTableColumn
decLesJoinNonDuplicates = _DecLesJoinNonDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 5),
    _DecLesJoinNonDuplicates_Type()
)
decLesJoinNonDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinNonDuplicates.setStatus("mandatory")
_DecLesJoinDiscards_Type = Counter32
_DecLesJoinDiscards_Object = MibTableColumn
decLesJoinDiscards = _DecLesJoinDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 6),
    _DecLesJoinDiscards_Type()
)
decLesJoinDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinDiscards.setStatus("mandatory")
_DecLesJoinTimeouts_Type = Counter32
_DecLesJoinTimeouts_Object = MibTableColumn
decLesJoinTimeouts = _DecLesJoinTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 7),
    _DecLesJoinTimeouts_Type()
)
decLesJoinTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinTimeouts.setStatus("mandatory")
_DecLesJoinVersionsNotSupported_Type = Counter32
_DecLesJoinVersionsNotSupported_Object = MibTableColumn
decLesJoinVersionsNotSupported = _DecLesJoinVersionsNotSupported_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 8),
    _DecLesJoinVersionsNotSupported_Type()
)
decLesJoinVersionsNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinVersionsNotSupported.setStatus("mandatory")
_DecLesJoinInvalidParameters_Type = Counter32
_DecLesJoinInvalidParameters_Object = MibTableColumn
decLesJoinInvalidParameters = _DecLesJoinInvalidParameters_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 9),
    _DecLesJoinInvalidParameters_Type()
)
decLesJoinInvalidParameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinInvalidParameters.setStatus("mandatory")
_DecLesJoinDuplicateAtmAddresses_Type = Counter32
_DecLesJoinDuplicateAtmAddresses_Object = MibTableColumn
decLesJoinDuplicateAtmAddresses = _DecLesJoinDuplicateAtmAddresses_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 10),
    _DecLesJoinDuplicateAtmAddresses_Type()
)
decLesJoinDuplicateAtmAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinDuplicateAtmAddresses.setStatus("mandatory")
_DecLesJoinDuplicateLanDestinations_Type = Counter32
_DecLesJoinDuplicateLanDestinations_Object = MibTableColumn
decLesJoinDuplicateLanDestinations = _DecLesJoinDuplicateLanDestinations_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 11),
    _DecLesJoinDuplicateLanDestinations_Type()
)
decLesJoinDuplicateLanDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinDuplicateLanDestinations.setStatus("mandatory")
_DecLesJoinInvalidAtmAddresses_Type = Counter32
_DecLesJoinInvalidAtmAddresses_Object = MibTableColumn
decLesJoinInvalidAtmAddresses = _DecLesJoinInvalidAtmAddresses_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 12),
    _DecLesJoinInvalidAtmAddresses_Type()
)
decLesJoinInvalidAtmAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinInvalidAtmAddresses.setStatus("mandatory")
_DecLesJoinInvalidLanDestinations_Type = Counter32
_DecLesJoinInvalidLanDestinations_Object = MibTableColumn
decLesJoinInvalidLanDestinations = _DecLesJoinInvalidLanDestinations_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 13),
    _DecLesJoinInvalidLanDestinations_Type()
)
decLesJoinInvalidLanDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinInvalidLanDestinations.setStatus("mandatory")
_DecLesJoinWrongLanTypes_Type = Counter32
_DecLesJoinWrongLanTypes_Object = MibTableColumn
decLesJoinWrongLanTypes = _DecLesJoinWrongLanTypes_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 14),
    _DecLesJoinWrongLanTypes_Type()
)
decLesJoinWrongLanTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinWrongLanTypes.setStatus("mandatory")
_DecLesJoinMaxFrameSizesTooSmall_Type = Counter32
_DecLesJoinMaxFrameSizesTooSmall_Object = MibTableColumn
decLesJoinMaxFrameSizesTooSmall = _DecLesJoinMaxFrameSizesTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 15),
    _DecLesJoinMaxFrameSizesTooSmall_Type()
)
decLesJoinMaxFrameSizesTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinMaxFrameSizesTooSmall.setStatus("mandatory")
_DecLesJoinInvalidLECIDs_Type = Counter32
_DecLesJoinInvalidLECIDs_Object = MibTableColumn
decLesJoinInvalidLECIDs = _DecLesJoinInvalidLECIDs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 16),
    _DecLesJoinInvalidLECIDs_Type()
)
decLesJoinInvalidLECIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinInvalidLECIDs.setStatus("mandatory")
_DecLesJoinCtlDistributeRejects_Type = Counter32
_DecLesJoinCtlDistributeRejects_Object = MibTableColumn
decLesJoinCtlDistributeRejects = _DecLesJoinCtlDistributeRejects_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 17),
    _DecLesJoinCtlDistributeRejects_Type()
)
decLesJoinCtlDistributeRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinCtlDistributeRejects.setStatus("mandatory")
_DecLesJoinOutOfResources_Type = Counter32
_DecLesJoinOutOfResources_Object = MibTableColumn
decLesJoinOutOfResources = _DecLesJoinOutOfResources_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 18),
    _DecLesJoinOutOfResources_Type()
)
decLesJoinOutOfResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinOutOfResources.setStatus("mandatory")
_DecLesJoinRcvQueueDiscards_Type = Counter32
_DecLesJoinRcvQueueDiscards_Object = MibTableColumn
decLesJoinRcvQueueDiscards = _DecLesJoinRcvQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 19),
    _DecLesJoinRcvQueueDiscards_Type()
)
decLesJoinRcvQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinRcvQueueDiscards.setStatus("mandatory")
_DecLesJoinLecRcvQueueDiscards_Type = Counter32
_DecLesJoinLecRcvQueueDiscards_Object = MibTableColumn
decLesJoinLecRcvQueueDiscards = _DecLesJoinLecRcvQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 20),
    _DecLesJoinLecRcvQueueDiscards_Type()
)
decLesJoinLecRcvQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinLecRcvQueueDiscards.setStatus("mandatory")
_DecLesJoinResourceDiscards_Type = Counter32
_DecLesJoinResourceDiscards_Object = MibTableColumn
decLesJoinResourceDiscards = _DecLesJoinResourceDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 11, 1, 21),
    _DecLesJoinResourceDiscards_Type()
)
decLesJoinResourceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesJoinResourceDiscards.setStatus("mandatory")
_DecLesRegisterTable_Object = MibTable
decLesRegisterTable = _DecLesRegisterTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12)
)
if mibBuilder.loadTexts:
    decLesRegisterTable.setStatus("mandatory")
_DecLesRegisterEntry_Object = MibTableRow
decLesRegisterEntry = _DecLesRegisterEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1)
)
decLesRegisterEntry.setIndexNames(
    (0, "DEC-LES-MIB", "decLesIndex"),
)
if mibBuilder.loadTexts:
    decLesRegisterEntry.setStatus("mandatory")
_DecLesRegisterRequests_Type = Counter32
_DecLesRegisterRequests_Object = MibTableColumn
decLesRegisterRequests = _DecLesRegisterRequests_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 1),
    _DecLesRegisterRequests_Type()
)
decLesRegisterRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRegisterRequests.setStatus("mandatory")
_DecLesRegisterSuccesses_Type = Counter32
_DecLesRegisterSuccesses_Object = MibTableColumn
decLesRegisterSuccesses = _DecLesRegisterSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 2),
    _DecLesRegisterSuccesses_Type()
)
decLesRegisterSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRegisterSuccesses.setStatus("mandatory")
_DecLesRegisterFailures_Type = Counter32
_DecLesRegisterFailures_Object = MibTableColumn
decLesRegisterFailures = _DecLesRegisterFailures_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 3),
    _DecLesRegisterFailures_Type()
)
decLesRegisterFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRegisterFailures.setStatus("mandatory")
_DecLesRegisterDiscards_Type = Counter32
_DecLesRegisterDiscards_Object = MibTableColumn
decLesRegisterDiscards = _DecLesRegisterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 4),
    _DecLesRegisterDiscards_Type()
)
decLesRegisterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRegisterDiscards.setStatus("mandatory")
_DecLesUnregisterRequests_Type = Counter32
_DecLesUnregisterRequests_Object = MibTableColumn
decLesUnregisterRequests = _DecLesUnregisterRequests_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 5),
    _DecLesUnregisterRequests_Type()
)
decLesUnregisterRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesUnregisterRequests.setStatus("mandatory")
_DecLesUnregisterSuccesses_Type = Counter32
_DecLesUnregisterSuccesses_Object = MibTableColumn
decLesUnregisterSuccesses = _DecLesUnregisterSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 6),
    _DecLesUnregisterSuccesses_Type()
)
decLesUnregisterSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesUnregisterSuccesses.setStatus("mandatory")
_DecLesUnregisterFailures_Type = Counter32
_DecLesUnregisterFailures_Object = MibTableColumn
decLesUnregisterFailures = _DecLesUnregisterFailures_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 7),
    _DecLesUnregisterFailures_Type()
)
decLesUnregisterFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesUnregisterFailures.setStatus("mandatory")
_DecLesUnregisterDiscards_Type = Counter32
_DecLesUnregisterDiscards_Object = MibTableColumn
decLesUnregisterDiscards = _DecLesUnregisterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 8),
    _DecLesUnregisterDiscards_Type()
)
decLesUnregisterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesUnregisterDiscards.setStatus("mandatory")
_DecLesRegDuplicateAtmAddresses_Type = Counter32
_DecLesRegDuplicateAtmAddresses_Object = MibTableColumn
decLesRegDuplicateAtmAddresses = _DecLesRegDuplicateAtmAddresses_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 9),
    _DecLesRegDuplicateAtmAddresses_Type()
)
decLesRegDuplicateAtmAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRegDuplicateAtmAddresses.setStatus("mandatory")
_DecLesRegDuplicateLanDestinations_Type = Counter32
_DecLesRegDuplicateLanDestinations_Object = MibTableColumn
decLesRegDuplicateLanDestinations = _DecLesRegDuplicateLanDestinations_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 10),
    _DecLesRegDuplicateLanDestinations_Type()
)
decLesRegDuplicateLanDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRegDuplicateLanDestinations.setStatus("mandatory")
_DecLesRegInvalidAtmAddresses_Type = Counter32
_DecLesRegInvalidAtmAddresses_Object = MibTableColumn
decLesRegInvalidAtmAddresses = _DecLesRegInvalidAtmAddresses_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 11),
    _DecLesRegInvalidAtmAddresses_Type()
)
decLesRegInvalidAtmAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRegInvalidAtmAddresses.setStatus("mandatory")
_DecLesRegInvalidLanDestinations_Type = Counter32
_DecLesRegInvalidLanDestinations_Object = MibTableColumn
decLesRegInvalidLanDestinations = _DecLesRegInvalidLanDestinations_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 12),
    _DecLesRegInvalidLanDestinations_Type()
)
decLesRegInvalidLanDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRegInvalidLanDestinations.setStatus("mandatory")
_DecLesRegInvalidLECIDs_Type = Counter32
_DecLesRegInvalidLECIDs_Object = MibTableColumn
decLesRegInvalidLECIDs = _DecLesRegInvalidLECIDs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 13),
    _DecLesRegInvalidLECIDs_Type()
)
decLesRegInvalidLECIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRegInvalidLECIDs.setStatus("mandatory")
_DecLesRegOutOfResources_Type = Counter32
_DecLesRegOutOfResources_Object = MibTableColumn
decLesRegOutOfResources = _DecLesRegOutOfResources_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 14),
    _DecLesRegOutOfResources_Type()
)
decLesRegOutOfResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRegOutOfResources.setStatus("mandatory")
_DecLesRegRcvQueueDiscards_Type = Counter32
_DecLesRegRcvQueueDiscards_Object = MibTableColumn
decLesRegRcvQueueDiscards = _DecLesRegRcvQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 15),
    _DecLesRegRcvQueueDiscards_Type()
)
decLesRegRcvQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRegRcvQueueDiscards.setStatus("mandatory")
_DecLesRegLecRcvQueueDiscards_Type = Counter32
_DecLesRegLecRcvQueueDiscards_Object = MibTableColumn
decLesRegLecRcvQueueDiscards = _DecLesRegLecRcvQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 16),
    _DecLesRegLecRcvQueueDiscards_Type()
)
decLesRegLecRcvQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRegLecRcvQueueDiscards.setStatus("mandatory")
_DecLesRegResourceDiscards_Type = Counter32
_DecLesRegResourceDiscards_Object = MibTableColumn
decLesRegResourceDiscards = _DecLesRegResourceDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 17),
    _DecLesRegResourceDiscards_Type()
)
decLesRegResourceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRegResourceDiscards.setStatus("mandatory")
_DecLesUnRegInvalidLanDestinations_Type = Counter32
_DecLesUnRegInvalidLanDestinations_Object = MibTableColumn
decLesUnRegInvalidLanDestinations = _DecLesUnRegInvalidLanDestinations_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 18),
    _DecLesUnRegInvalidLanDestinations_Type()
)
decLesUnRegInvalidLanDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesUnRegInvalidLanDestinations.setStatus("mandatory")
_DecLesUnRegInvalidLECIDs_Type = Counter32
_DecLesUnRegInvalidLECIDs_Object = MibTableColumn
decLesUnRegInvalidLECIDs = _DecLesUnRegInvalidLECIDs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 19),
    _DecLesUnRegInvalidLECIDs_Type()
)
decLesUnRegInvalidLECIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesUnRegInvalidLECIDs.setStatus("mandatory")
_DecLesUnRegRcvQueueDiscards_Type = Counter32
_DecLesUnRegRcvQueueDiscards_Object = MibTableColumn
decLesUnRegRcvQueueDiscards = _DecLesUnRegRcvQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 20),
    _DecLesUnRegRcvQueueDiscards_Type()
)
decLesUnRegRcvQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesUnRegRcvQueueDiscards.setStatus("mandatory")
_DecLesUnRegLecRcvQueueDiscards_Type = Counter32
_DecLesUnRegLecRcvQueueDiscards_Object = MibTableColumn
decLesUnRegLecRcvQueueDiscards = _DecLesUnRegLecRcvQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 21),
    _DecLesUnRegLecRcvQueueDiscards_Type()
)
decLesUnRegLecRcvQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesUnRegLecRcvQueueDiscards.setStatus("mandatory")
_DecLesUnRegResourceDiscards_Type = Counter32
_DecLesUnRegResourceDiscards_Object = MibTableColumn
decLesUnRegResourceDiscards = _DecLesUnRegResourceDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 22),
    _DecLesUnRegResourceDiscards_Type()
)
decLesUnRegResourceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesUnRegResourceDiscards.setStatus("mandatory")
_DecLesRegAlreadyRegistered_Type = Counter32
_DecLesRegAlreadyRegistered_Object = MibTableColumn
decLesRegAlreadyRegistered = _DecLesRegAlreadyRegistered_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 23),
    _DecLesRegAlreadyRegistered_Type()
)
decLesRegAlreadyRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesRegAlreadyRegistered.setStatus("mandatory")
_DecLesUnRegNoSuchLanDestinations_Type = Counter32
_DecLesUnRegNoSuchLanDestinations_Object = MibTableColumn
decLesUnRegNoSuchLanDestinations = _DecLesUnRegNoSuchLanDestinations_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 24),
    _DecLesUnRegNoSuchLanDestinations_Type()
)
decLesUnRegNoSuchLanDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesUnRegNoSuchLanDestinations.setStatus("mandatory")
_DecLesUnRegNoSuchAddressPairs_Type = Counter32
_DecLesUnRegNoSuchAddressPairs_Object = MibTableColumn
decLesUnRegNoSuchAddressPairs = _DecLesUnRegNoSuchAddressPairs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 25),
    _DecLesUnRegNoSuchAddressPairs_Type()
)
decLesUnRegNoSuchAddressPairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesUnRegNoSuchAddressPairs.setStatus("mandatory")
_DecLesUnRegOwnedByOthers_Type = Counter32
_DecLesUnRegOwnedByOthers_Object = MibTableColumn
decLesUnRegOwnedByOthers = _DecLesUnRegOwnedByOthers_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 12, 1, 26),
    _DecLesUnRegOwnedByOthers_Type()
)
decLesUnRegOwnedByOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesUnRegOwnedByOthers.setStatus("mandatory")
_DecLesArpTable_Object = MibTable
decLesArpTable = _DecLesArpTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13)
)
if mibBuilder.loadTexts:
    decLesArpTable.setStatus("mandatory")
_DecLesArpEntry_Object = MibTableRow
decLesArpEntry = _DecLesArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1)
)
decLesArpEntry.setIndexNames(
    (0, "DEC-LES-MIB", "decLesIndex"),
)
if mibBuilder.loadTexts:
    decLesArpEntry.setStatus("mandatory")
_DecLesArpRequestsAnswered_Type = Counter32
_DecLesArpRequestsAnswered_Object = MibTableColumn
decLesArpRequestsAnswered = _DecLesArpRequestsAnswered_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 1),
    _DecLesArpRequestsAnswered_Type()
)
decLesArpRequestsAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesArpRequestsAnswered.setStatus("mandatory")
_DecLesArpRequestsForwarded_Type = Counter32
_DecLesArpRequestsForwarded_Object = MibTableColumn
decLesArpRequestsForwarded = _DecLesArpRequestsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 2),
    _DecLesArpRequestsForwarded_Type()
)
decLesArpRequestsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesArpRequestsForwarded.setStatus("mandatory")
_DecLesArpRequestsRejected_Type = Counter32
_DecLesArpRequestsRejected_Object = MibTableColumn
decLesArpRequestsRejected = _DecLesArpRequestsRejected_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 3),
    _DecLesArpRequestsRejected_Type()
)
decLesArpRequestsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesArpRequestsRejected.setStatus("mandatory")
_DecLesArpRequestsDiscarded_Type = Counter32
_DecLesArpRequestsDiscarded_Object = MibTableColumn
decLesArpRequestsDiscarded = _DecLesArpRequestsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 4),
    _DecLesArpRequestsDiscarded_Type()
)
decLesArpRequestsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesArpRequestsDiscarded.setStatus("mandatory")
_DecLesArpResponsesForwarded_Type = Counter32
_DecLesArpResponsesForwarded_Object = MibTableColumn
decLesArpResponsesForwarded = _DecLesArpResponsesForwarded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 5),
    _DecLesArpResponsesForwarded_Type()
)
decLesArpResponsesForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesArpResponsesForwarded.setStatus("mandatory")
_DecLesArpResponsesRejected_Type = Counter32
_DecLesArpResponsesRejected_Object = MibTableColumn
decLesArpResponsesRejected = _DecLesArpResponsesRejected_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 6),
    _DecLesArpResponsesRejected_Type()
)
decLesArpResponsesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesArpResponsesRejected.setStatus("mandatory")
_DecLesArpResponsesDiscarded_Type = Counter32
_DecLesArpResponsesDiscarded_Object = MibTableColumn
decLesArpResponsesDiscarded = _DecLesArpResponsesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 7),
    _DecLesArpResponsesDiscarded_Type()
)
decLesArpResponsesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesArpResponsesDiscarded.setStatus("mandatory")
_DecLesNarpRequestsForwarded_Type = Counter32
_DecLesNarpRequestsForwarded_Object = MibTableColumn
decLesNarpRequestsForwarded = _DecLesNarpRequestsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 8),
    _DecLesNarpRequestsForwarded_Type()
)
decLesNarpRequestsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesNarpRequestsForwarded.setStatus("mandatory")
_DecLesNarpRequestsFiltered_Type = Counter32
_DecLesNarpRequestsFiltered_Object = MibTableColumn
decLesNarpRequestsFiltered = _DecLesNarpRequestsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 9),
    _DecLesNarpRequestsFiltered_Type()
)
decLesNarpRequestsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesNarpRequestsFiltered.setStatus("mandatory")
_DecLesNarpRequestsRejected_Type = Counter32
_DecLesNarpRequestsRejected_Object = MibTableColumn
decLesNarpRequestsRejected = _DecLesNarpRequestsRejected_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 10),
    _DecLesNarpRequestsRejected_Type()
)
decLesNarpRequestsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesNarpRequestsRejected.setStatus("mandatory")
_DecLesNarpRequestsDiscarded_Type = Counter32
_DecLesNarpRequestsDiscarded_Object = MibTableColumn
decLesNarpRequestsDiscarded = _DecLesNarpRequestsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 11),
    _DecLesNarpRequestsDiscarded_Type()
)
decLesNarpRequestsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesNarpRequestsDiscarded.setStatus("mandatory")
_DecLesTopologyRequestsForwarded_Type = Counter32
_DecLesTopologyRequestsForwarded_Object = MibTableColumn
decLesTopologyRequestsForwarded = _DecLesTopologyRequestsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 12),
    _DecLesTopologyRequestsForwarded_Type()
)
decLesTopologyRequestsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesTopologyRequestsForwarded.setStatus("mandatory")
_DecLesTopologyRequestsGenerated_Type = Counter32
_DecLesTopologyRequestsGenerated_Object = MibTableColumn
decLesTopologyRequestsGenerated = _DecLesTopologyRequestsGenerated_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 13),
    _DecLesTopologyRequestsGenerated_Type()
)
decLesTopologyRequestsGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesTopologyRequestsGenerated.setStatus("mandatory")
_DecLesTopologyRequestsRejected_Type = Counter32
_DecLesTopologyRequestsRejected_Object = MibTableColumn
decLesTopologyRequestsRejected = _DecLesTopologyRequestsRejected_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 14),
    _DecLesTopologyRequestsRejected_Type()
)
decLesTopologyRequestsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesTopologyRequestsRejected.setStatus("mandatory")
_DecLesTopologyRequestsDiscarded_Type = Counter32
_DecLesTopologyRequestsDiscarded_Object = MibTableColumn
decLesTopologyRequestsDiscarded = _DecLesTopologyRequestsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 15),
    _DecLesTopologyRequestsDiscarded_Type()
)
decLesTopologyRequestsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesTopologyRequestsDiscarded.setStatus("mandatory")
_DecLesTopologyRequestGenFailures_Type = Counter32
_DecLesTopologyRequestGenFailures_Object = MibTableColumn
decLesTopologyRequestGenFailures = _DecLesTopologyRequestGenFailures_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 16),
    _DecLesTopologyRequestGenFailures_Type()
)
decLesTopologyRequestGenFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesTopologyRequestGenFailures.setStatus("mandatory")
_DecLesArpReqInvalidAtmAddresses_Type = Counter32
_DecLesArpReqInvalidAtmAddresses_Object = MibTableColumn
decLesArpReqInvalidAtmAddresses = _DecLesArpReqInvalidAtmAddresses_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 17),
    _DecLesArpReqInvalidAtmAddresses_Type()
)
decLesArpReqInvalidAtmAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesArpReqInvalidAtmAddresses.setStatus("mandatory")
_DecLesArpReqInvalidLanDestinations_Type = Counter32
_DecLesArpReqInvalidLanDestinations_Object = MibTableColumn
decLesArpReqInvalidLanDestinations = _DecLesArpReqInvalidLanDestinations_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 18),
    _DecLesArpReqInvalidLanDestinations_Type()
)
decLesArpReqInvalidLanDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesArpReqInvalidLanDestinations.setStatus("mandatory")
_DecLesArpReqInvalidLECIDs_Type = Counter32
_DecLesArpReqInvalidLECIDs_Object = MibTableColumn
decLesArpReqInvalidLECIDs = _DecLesArpReqInvalidLECIDs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 19),
    _DecLesArpReqInvalidLECIDs_Type()
)
decLesArpReqInvalidLECIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesArpReqInvalidLECIDs.setStatus("mandatory")
_DecLesArpReqReceiveQueueDiscards_Type = Counter32
_DecLesArpReqReceiveQueueDiscards_Object = MibTableColumn
decLesArpReqReceiveQueueDiscards = _DecLesArpReqReceiveQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 20),
    _DecLesArpReqReceiveQueueDiscards_Type()
)
decLesArpReqReceiveQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesArpReqReceiveQueueDiscards.setStatus("mandatory")
_DecLesArpReqResourceDiscards_Type = Counter32
_DecLesArpReqResourceDiscards_Object = MibTableColumn
decLesArpReqResourceDiscards = _DecLesArpReqResourceDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 21),
    _DecLesArpReqResourceDiscards_Type()
)
decLesArpReqResourceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesArpReqResourceDiscards.setStatus("mandatory")
_DecLesArpRespInvalidLECIDs_Type = Counter32
_DecLesArpRespInvalidLECIDs_Object = MibTableColumn
decLesArpRespInvalidLECIDs = _DecLesArpRespInvalidLECIDs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 22),
    _DecLesArpRespInvalidLECIDs_Type()
)
decLesArpRespInvalidLECIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesArpRespInvalidLECIDs.setStatus("mandatory")
_DecLesArpRespReceiveQueueDiscards_Type = Counter32
_DecLesArpRespReceiveQueueDiscards_Object = MibTableColumn
decLesArpRespReceiveQueueDiscards = _DecLesArpRespReceiveQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 23),
    _DecLesArpRespReceiveQueueDiscards_Type()
)
decLesArpRespReceiveQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesArpRespReceiveQueueDiscards.setStatus("mandatory")
_DecLesArpRespResourceDiscards_Type = Counter32
_DecLesArpRespResourceDiscards_Object = MibTableColumn
decLesArpRespResourceDiscards = _DecLesArpRespResourceDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 24),
    _DecLesArpRespResourceDiscards_Type()
)
decLesArpRespResourceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesArpRespResourceDiscards.setStatus("mandatory")
_DecLesNarpReqInvalidAtmAddresses_Type = Counter32
_DecLesNarpReqInvalidAtmAddresses_Object = MibTableColumn
decLesNarpReqInvalidAtmAddresses = _DecLesNarpReqInvalidAtmAddresses_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 25),
    _DecLesNarpReqInvalidAtmAddresses_Type()
)
decLesNarpReqInvalidAtmAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesNarpReqInvalidAtmAddresses.setStatus("mandatory")
_DecLesNarpReqInvalidLanDestinations_Type = Counter32
_DecLesNarpReqInvalidLanDestinations_Object = MibTableColumn
decLesNarpReqInvalidLanDestinations = _DecLesNarpReqInvalidLanDestinations_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 26),
    _DecLesNarpReqInvalidLanDestinations_Type()
)
decLesNarpReqInvalidLanDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesNarpReqInvalidLanDestinations.setStatus("mandatory")
_DecLesNarpReqInvalidLECIDs_Type = Counter32
_DecLesNarpReqInvalidLECIDs_Object = MibTableColumn
decLesNarpReqInvalidLECIDs = _DecLesNarpReqInvalidLECIDs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 27),
    _DecLesNarpReqInvalidLECIDs_Type()
)
decLesNarpReqInvalidLECIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesNarpReqInvalidLECIDs.setStatus("mandatory")
_DecLesNarpReqReceiveQueueDiscards_Type = Counter32
_DecLesNarpReqReceiveQueueDiscards_Object = MibTableColumn
decLesNarpReqReceiveQueueDiscards = _DecLesNarpReqReceiveQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 28),
    _DecLesNarpReqReceiveQueueDiscards_Type()
)
decLesNarpReqReceiveQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesNarpReqReceiveQueueDiscards.setStatus("mandatory")
_DecLesNarpReqResourceDiscards_Type = Counter32
_DecLesNarpReqResourceDiscards_Object = MibTableColumn
decLesNarpReqResourceDiscards = _DecLesNarpReqResourceDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 29),
    _DecLesNarpReqResourceDiscards_Type()
)
decLesNarpReqResourceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesNarpReqResourceDiscards.setStatus("mandatory")
_DecLesTopoReqReceiveQueueDiscards_Type = Counter32
_DecLesTopoReqReceiveQueueDiscards_Object = MibTableColumn
decLesTopoReqReceiveQueueDiscards = _DecLesTopoReqReceiveQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 30),
    _DecLesTopoReqReceiveQueueDiscards_Type()
)
decLesTopoReqReceiveQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesTopoReqReceiveQueueDiscards.setStatus("mandatory")
_DecLesTopoReqResourceDiscards_Type = Counter32
_DecLesTopoReqResourceDiscards_Object = MibTableColumn
decLesTopoReqResourceDiscards = _DecLesTopoReqResourceDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 13, 1, 31),
    _DecLesTopoReqResourceDiscards_Type()
)
decLesTopoReqResourceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesTopoReqResourceDiscards.setStatus("mandatory")
_DecLesFlushTable_Object = MibTable
decLesFlushTable = _DecLesFlushTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 14)
)
if mibBuilder.loadTexts:
    decLesFlushTable.setStatus("mandatory")
_DecLesFlushEntry_Object = MibTableRow
decLesFlushEntry = _DecLesFlushEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 14, 1)
)
decLesFlushEntry.setIndexNames(
    (0, "DEC-LES-MIB", "decLesIndex"),
)
if mibBuilder.loadTexts:
    decLesFlushEntry.setStatus("mandatory")
_DecLesFlushResponsesForwarded_Type = Counter32
_DecLesFlushResponsesForwarded_Object = MibTableColumn
decLesFlushResponsesForwarded = _DecLesFlushResponsesForwarded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 14, 1, 1),
    _DecLesFlushResponsesForwarded_Type()
)
decLesFlushResponsesForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesFlushResponsesForwarded.setStatus("mandatory")
_DecLesFlushResponsesRejected_Type = Counter32
_DecLesFlushResponsesRejected_Object = MibTableColumn
decLesFlushResponsesRejected = _DecLesFlushResponsesRejected_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 14, 1, 2),
    _DecLesFlushResponsesRejected_Type()
)
decLesFlushResponsesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesFlushResponsesRejected.setStatus("mandatory")
_DecLesFlushResponsesDiscarded_Type = Counter32
_DecLesFlushResponsesDiscarded_Object = MibTableColumn
decLesFlushResponsesDiscarded = _DecLesFlushResponsesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 14, 1, 3),
    _DecLesFlushResponsesDiscarded_Type()
)
decLesFlushResponsesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesFlushResponsesDiscarded.setStatus("mandatory")
_DecLesEventLogMaximumSize_Type = Integer32
_DecLesEventLogMaximumSize_Object = MibScalar
decLesEventLogMaximumSize = _DecLesEventLogMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 15),
    _DecLesEventLogMaximumSize_Type()
)
decLesEventLogMaximumSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decLesEventLogMaximumSize.setStatus("mandatory")
_DecLesEventLogTable_Object = MibTable
decLesEventLogTable = _DecLesEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 16)
)
if mibBuilder.loadTexts:
    decLesEventLogTable.setStatus("mandatory")
_DecLesEventLogEntry_Object = MibTableRow
decLesEventLogEntry = _DecLesEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 16, 1)
)
decLesEventLogEntry.setIndexNames(
    (0, "DEC-LES-MIB", "decLesEventIndex"),
)
if mibBuilder.loadTexts:
    decLesEventLogEntry.setStatus("mandatory")
_DecLesEventIndex_Type = Integer32
_DecLesEventIndex_Object = MibTableColumn
decLesEventIndex = _DecLesEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 16, 1, 1),
    _DecLesEventIndex_Type()
)
decLesEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesEventIndex.setStatus("mandatory")


class _DecLesEventType_Type(Integer32):
    """Custom type decLesEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("joinFailed", 1),
          ("registrationFailed", 2))
    )


_DecLesEventType_Type.__name__ = "Integer32"
_DecLesEventType_Object = MibTableColumn
decLesEventType = _DecLesEventType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 16, 1, 2),
    _DecLesEventType_Type()
)
decLesEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesEventType.setStatus("mandatory")


class _DecLesEventReason_Type(Integer32):
    """Custom type decLesEventReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              90,
              91,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("accessDenied", 7),
          ("busConnectTimeout", 58),
          ("clientNotConnectedToLes", 59),
          ("controlDistributeFailure", 54),
          ("duplicateAtmAddress", 5),
          ("duplicateLanDestination", 4),
          ("insecureAtmAddress", 100),
          ("insufficientResources", 6),
          ("invalidAalMode", 90),
          ("invalidAalParameters", 81),
          ("invalidAalSccs", 91),
          ("invalidAtmAddress", 10),
          ("invalidAtmTrafficDescriptor", 82),
          ("invalidBlli", 84),
          ("invalidBroadbandBearerCapability", 83),
          ("invalidCalledPartyNumber", 86),
          ("invalidCallingPartyNumber", 85),
          ("invalidConnectionIdentifier", 87),
          ("invalidInformationElement", 80),
          ("invalidLanDestination", 9),
          ("invalidQosParameter", 88),
          ("invalidRequestParameters", 2),
          ("invalidRequestorId", 8),
          ("joinNotCompleted", 56),
          ("joinTimeout", 57),
          ("missingInformationElement", 70),
          ("multicastForwardFailure", 55),
          ("noAalParameters", 71),
          ("noAtmTrafficDescriptor", 72),
          ("noBlli", 74),
          ("noBroadbandBearerCapability", 73),
          ("noCalledPartyNumber", 76),
          ("noCallingPartyNumber", 75),
          ("noConnectionIdentifier", 77),
          ("noQosParameter", 78),
          ("nonDuplicateRequest", 53),
          ("unverifiedAtmAddress", 101),
          ("versionNotSupported", 1),
          ("wrongJoinMaxFrameSize", 52),
          ("wrongLanType", 50),
          ("wrongMaxFrameSize", 51))
    )


_DecLesEventReason_Type.__name__ = "Integer32"
_DecLesEventReason_Object = MibTableColumn
decLesEventReason = _DecLesEventReason_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 16, 1, 3),
    _DecLesEventReason_Type()
)
decLesEventReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesEventReason.setStatus("mandatory")
_DecLesEventServer_Type = Integer32
_DecLesEventServer_Object = MibTableColumn
decLesEventServer = _DecLesEventServer_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 16, 1, 4),
    _DecLesEventServer_Type()
)
decLesEventServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesEventServer.setStatus("mandatory")


class _DecLesEventServerAtmAddress_Type(OctetString):
    """Custom type decLesEventServerAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecLesEventServerAtmAddress_Type.__name__ = "OctetString"
_DecLesEventServerAtmAddress_Object = MibTableColumn
decLesEventServerAtmAddress = _DecLesEventServerAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 16, 1, 5),
    _DecLesEventServerAtmAddress_Type()
)
decLesEventServerAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesEventServerAtmAddress.setStatus("mandatory")


class _DecLesEventClientAtmAddress_Type(OctetString):
    """Custom type decLesEventClientAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecLesEventClientAtmAddress_Type.__name__ = "OctetString"
_DecLesEventClientAtmAddress_Object = MibTableColumn
decLesEventClientAtmAddress = _DecLesEventClientAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 16, 1, 6),
    _DecLesEventClientAtmAddress_Type()
)
decLesEventClientAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesEventClientAtmAddress.setStatus("mandatory")


class _DecLesEventClientMacAddress_Type(OctetString):
    """Custom type decLesEventClientMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_DecLesEventClientMacAddress_Type.__name__ = "OctetString"
_DecLesEventClientMacAddress_Object = MibTableColumn
decLesEventClientMacAddress = _DecLesEventClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 16, 1, 7),
    _DecLesEventClientMacAddress_Type()
)
decLesEventClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesEventClientMacAddress.setStatus("mandatory")
_DecLesEventTimestamp_Type = TimeTicks
_DecLesEventTimestamp_Object = MibTableColumn
decLesEventTimestamp = _DecLesEventTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 1, 16, 1, 8),
    _DecLesEventTimestamp_Type()
)
decLesEventTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decLesEventTimestamp.setStatus("mandatory")
_DecLesMIBConformance_ObjectIdentity = ObjectIdentity
decLesMIBConformance = _DecLesMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2)
)
_DecLesMIBGroups_ObjectIdentity = ObjectIdentity
decLesMIBGroups = _DecLesMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2, 1)
)
_DecLesConfigGroup_ObjectIdentity = ObjectIdentity
decLesConfigGroup = _DecLesConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2, 1, 1)
)
_DecLesClientStatesGroup_ObjectIdentity = ObjectIdentity
decLesClientStatesGroup = _DecLesClientStatesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2, 1, 2)
)
_DecLesClientGroup_ObjectIdentity = ObjectIdentity
decLesClientGroup = _DecLesClientGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2, 1, 3)
)
_DecLesLecGroup_ObjectIdentity = ObjectIdentity
decLesLecGroup = _DecLesLecGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2, 1, 4)
)
_DecLesCircuitGroup_ObjectIdentity = ObjectIdentity
decLesCircuitGroup = _DecLesCircuitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2, 1, 5)
)
_DecLesMacAddressGroup_ObjectIdentity = ObjectIdentity
decLesMacAddressGroup = _DecLesMacAddressGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2, 1, 6)
)
_DecLesRouteDescrGroup_ObjectIdentity = ObjectIdentity
decLesRouteDescrGroup = _DecLesRouteDescrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2, 1, 7)
)
_DecLesTrafficGroup_ObjectIdentity = ObjectIdentity
decLesTrafficGroup = _DecLesTrafficGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2, 1, 8)
)
_DecLesCallStatsGroup_ObjectIdentity = ObjectIdentity
decLesCallStatsGroup = _DecLesCallStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2, 1, 9)
)
_DecLesJoinStatsGroup_ObjectIdentity = ObjectIdentity
decLesJoinStatsGroup = _DecLesJoinStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2, 1, 10)
)
_DecLesRegisterStatsGroup_ObjectIdentity = ObjectIdentity
decLesRegisterStatsGroup = _DecLesRegisterStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2, 1, 11)
)
_DecLesArpStatsGroup_ObjectIdentity = ObjectIdentity
decLesArpStatsGroup = _DecLesArpStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2, 1, 12)
)
_DecLesFlushStatsGroup_ObjectIdentity = ObjectIdentity
decLesFlushStatsGroup = _DecLesFlushStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2, 1, 13)
)
_DecLesEventLogGroup_ObjectIdentity = ObjectIdentity
decLesEventLogGroup = _DecLesEventLogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2, 1, 14)
)
_DecLesMIBCompliances_ObjectIdentity = ObjectIdentity
decLesMIBCompliances = _DecLesMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2, 2)
)
_DecLesMIBCompliance_ObjectIdentity = ObjectIdentity
decLesMIBCompliance = _DecLesMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 28, 2, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEC-LES-MIB",
    **{"decLesMIB": decLesMIB,
       "decLesMIBObjects": decLesMIBObjects,
       "decLesConfigTable": decLesConfigTable,
       "decLesConfigEntry": decLesConfigEntry,
       "decLesIndex": decLesIndex,
       "decLesRowStatus": decLesRowStatus,
       "decLesAdminStatus": decLesAdminStatus,
       "decLesOperStatus": decLesOperStatus,
       "decLesLastChange": decLesLastChange,
       "decLesAtmAddress": decLesAtmAddress,
       "decLesDescription": decLesDescription,
       "decLesLanName": decLesLanName,
       "decLesLanType": decLesLanType,
       "decLesMaxDataFrameSize": decLesMaxDataFrameSize,
       "decLesAtmAddressOfBUS": decLesAtmAddressOfBUS,
       "decLesControlTimeout": decLesControlTimeout,
       "decLesArpResponsePolicy": decLesArpResponsePolicy,
       "decLesNarpRequestPolicy": decLesNarpRequestPolicy,
       "decLesTopologyChangeMode": decLesTopologyChangeMode,
       "decLesLastTcModeChange": decLesLastTcModeChange,
       "decLesTopologyChangeTimeout": decLesTopologyChangeTimeout,
       "decLesClientStatesTable": decLesClientStatesTable,
       "decLesClientStatesEntry": decLesClientStatesEntry,
       "decLesActiveClients": decLesActiveClients,
       "decLesActiveProxyClients": decLesActiveProxyClients,
       "decLesAwaitingJoinRequest": decLesAwaitingJoinRequest,
       "decLesCtlDistributeInProgress": decLesCtlDistributeInProgress,
       "decLesTerminating": decLesTerminating,
       "decLesClientTable": decLesClientTable,
       "decLesClientEntry": decLesClientEntry,
       "decLesClientID": decLesClientID,
       "decLesClientAtmAddress": decLesClientAtmAddress,
       "decLesClientIsProxy": decLesClientIsProxy,
       "decLesClientState": decLesClientState,
       "decLesClientRowStatus": decLesClientRowStatus,
       "decLesLecTable": decLesLecTable,
       "decLesLecEntry": decLesLecEntry,
       "decLesLecAtmAddress": decLesLecAtmAddress,
       "decLesLecID": decLesLecID,
       "decLesLecIsProxy": decLesLecIsProxy,
       "decLesLecState": decLesLecState,
       "decLesLecRowStatus": decLesLecRowStatus,
       "decLesCtlDirectTable": decLesCtlDirectTable,
       "decLesCtlDirectEntry": decLesCtlDirectEntry,
       "decLesControlDirectInterface": decLesControlDirectInterface,
       "decLesControlDirectVpi": decLesControlDirectVpi,
       "decLesControlDirectVci": decLesControlDirectVci,
       "decLesControlDirectRowStatus": decLesControlDirectRowStatus,
       "decLesCtlDistTable": decLesCtlDistTable,
       "decLesCtlDistEntry": decLesCtlDistEntry,
       "decLesControlDistInterface": decLesControlDistInterface,
       "decLesControlDistVpi": decLesControlDistVpi,
       "decLesControlDistVci": decLesControlDistVci,
       "decLesControlDistRowStatus": decLesControlDistRowStatus,
       "decLesMacAddressTable": decLesMacAddressTable,
       "decLesMacAddressEntry": decLesMacAddressEntry,
       "decLesMacAddress": decLesMacAddress,
       "decLesMacAddressOwner": decLesMacAddressOwner,
       "decLesMacAddressAtmBinding": decLesMacAddressAtmBinding,
       "decLesRouteDescrTable": decLesRouteDescrTable,
       "decLesRouteDescrEntry": decLesRouteDescrEntry,
       "decLesRouteDescrSegmentID": decLesRouteDescrSegmentID,
       "decLesRouteDescrBridgeNumber": decLesRouteDescrBridgeNumber,
       "decLesRouteDescrOwner": decLesRouteDescrOwner,
       "decLesRouteDescrAtmBinding": decLesRouteDescrAtmBinding,
       "decLesTrafficTable": decLesTrafficTable,
       "decLesTrafficEntry": decLesTrafficEntry,
       "decLesControlFramesIn": decLesControlFramesIn,
       "decLesShortFrames": decLesShortFrames,
       "decLesUnjoinedClientFrames": decLesUnjoinedClientFrames,
       "decLesVersionsNotSupported": decLesVersionsNotSupported,
       "decLesInvalidFrames": decLesInvalidFrames,
       "decLesReceiveQueueDiscards": decLesReceiveQueueDiscards,
       "decLesMiscDiscards": decLesMiscDiscards,
       "decLesCallStatsTable": decLesCallStatsTable,
       "decLesCallStatsEntry": decLesCallStatsEntry,
       "decLesCtlDirectCalls": decLesCtlDirectCalls,
       "decLesCtlDirectFailures": decLesCtlDirectFailures,
       "decLesCtlDirectOutOfResources": decLesCtlDirectOutOfResources,
       "decLesCtlDirectInvalidInfoElements": decLesCtlDirectInvalidInfoElements,
       "decLesCtlDistributeCalls": decLesCtlDistributeCalls,
       "decLesCtlDistributeFailures": decLesCtlDistributeFailures,
       "decLesCtlDistribOutOfResources": decLesCtlDistribOutOfResources,
       "decLesJoinTable": decLesJoinTable,
       "decLesJoinEntry": decLesJoinEntry,
       "decLesJoinRequests": decLesJoinRequests,
       "decLesJoinSuccesses": decLesJoinSuccesses,
       "decLesJoinFailures": decLesJoinFailures,
       "decLesJoinDuplicates": decLesJoinDuplicates,
       "decLesJoinNonDuplicates": decLesJoinNonDuplicates,
       "decLesJoinDiscards": decLesJoinDiscards,
       "decLesJoinTimeouts": decLesJoinTimeouts,
       "decLesJoinVersionsNotSupported": decLesJoinVersionsNotSupported,
       "decLesJoinInvalidParameters": decLesJoinInvalidParameters,
       "decLesJoinDuplicateAtmAddresses": decLesJoinDuplicateAtmAddresses,
       "decLesJoinDuplicateLanDestinations": decLesJoinDuplicateLanDestinations,
       "decLesJoinInvalidAtmAddresses": decLesJoinInvalidAtmAddresses,
       "decLesJoinInvalidLanDestinations": decLesJoinInvalidLanDestinations,
       "decLesJoinWrongLanTypes": decLesJoinWrongLanTypes,
       "decLesJoinMaxFrameSizesTooSmall": decLesJoinMaxFrameSizesTooSmall,
       "decLesJoinInvalidLECIDs": decLesJoinInvalidLECIDs,
       "decLesJoinCtlDistributeRejects": decLesJoinCtlDistributeRejects,
       "decLesJoinOutOfResources": decLesJoinOutOfResources,
       "decLesJoinRcvQueueDiscards": decLesJoinRcvQueueDiscards,
       "decLesJoinLecRcvQueueDiscards": decLesJoinLecRcvQueueDiscards,
       "decLesJoinResourceDiscards": decLesJoinResourceDiscards,
       "decLesRegisterTable": decLesRegisterTable,
       "decLesRegisterEntry": decLesRegisterEntry,
       "decLesRegisterRequests": decLesRegisterRequests,
       "decLesRegisterSuccesses": decLesRegisterSuccesses,
       "decLesRegisterFailures": decLesRegisterFailures,
       "decLesRegisterDiscards": decLesRegisterDiscards,
       "decLesUnregisterRequests": decLesUnregisterRequests,
       "decLesUnregisterSuccesses": decLesUnregisterSuccesses,
       "decLesUnregisterFailures": decLesUnregisterFailures,
       "decLesUnregisterDiscards": decLesUnregisterDiscards,
       "decLesRegDuplicateAtmAddresses": decLesRegDuplicateAtmAddresses,
       "decLesRegDuplicateLanDestinations": decLesRegDuplicateLanDestinations,
       "decLesRegInvalidAtmAddresses": decLesRegInvalidAtmAddresses,
       "decLesRegInvalidLanDestinations": decLesRegInvalidLanDestinations,
       "decLesRegInvalidLECIDs": decLesRegInvalidLECIDs,
       "decLesRegOutOfResources": decLesRegOutOfResources,
       "decLesRegRcvQueueDiscards": decLesRegRcvQueueDiscards,
       "decLesRegLecRcvQueueDiscards": decLesRegLecRcvQueueDiscards,
       "decLesRegResourceDiscards": decLesRegResourceDiscards,
       "decLesUnRegInvalidLanDestinations": decLesUnRegInvalidLanDestinations,
       "decLesUnRegInvalidLECIDs": decLesUnRegInvalidLECIDs,
       "decLesUnRegRcvQueueDiscards": decLesUnRegRcvQueueDiscards,
       "decLesUnRegLecRcvQueueDiscards": decLesUnRegLecRcvQueueDiscards,
       "decLesUnRegResourceDiscards": decLesUnRegResourceDiscards,
       "decLesRegAlreadyRegistered": decLesRegAlreadyRegistered,
       "decLesUnRegNoSuchLanDestinations": decLesUnRegNoSuchLanDestinations,
       "decLesUnRegNoSuchAddressPairs": decLesUnRegNoSuchAddressPairs,
       "decLesUnRegOwnedByOthers": decLesUnRegOwnedByOthers,
       "decLesArpTable": decLesArpTable,
       "decLesArpEntry": decLesArpEntry,
       "decLesArpRequestsAnswered": decLesArpRequestsAnswered,
       "decLesArpRequestsForwarded": decLesArpRequestsForwarded,
       "decLesArpRequestsRejected": decLesArpRequestsRejected,
       "decLesArpRequestsDiscarded": decLesArpRequestsDiscarded,
       "decLesArpResponsesForwarded": decLesArpResponsesForwarded,
       "decLesArpResponsesRejected": decLesArpResponsesRejected,
       "decLesArpResponsesDiscarded": decLesArpResponsesDiscarded,
       "decLesNarpRequestsForwarded": decLesNarpRequestsForwarded,
       "decLesNarpRequestsFiltered": decLesNarpRequestsFiltered,
       "decLesNarpRequestsRejected": decLesNarpRequestsRejected,
       "decLesNarpRequestsDiscarded": decLesNarpRequestsDiscarded,
       "decLesTopologyRequestsForwarded": decLesTopologyRequestsForwarded,
       "decLesTopologyRequestsGenerated": decLesTopologyRequestsGenerated,
       "decLesTopologyRequestsRejected": decLesTopologyRequestsRejected,
       "decLesTopologyRequestsDiscarded": decLesTopologyRequestsDiscarded,
       "decLesTopologyRequestGenFailures": decLesTopologyRequestGenFailures,
       "decLesArpReqInvalidAtmAddresses": decLesArpReqInvalidAtmAddresses,
       "decLesArpReqInvalidLanDestinations": decLesArpReqInvalidLanDestinations,
       "decLesArpReqInvalidLECIDs": decLesArpReqInvalidLECIDs,
       "decLesArpReqReceiveQueueDiscards": decLesArpReqReceiveQueueDiscards,
       "decLesArpReqResourceDiscards": decLesArpReqResourceDiscards,
       "decLesArpRespInvalidLECIDs": decLesArpRespInvalidLECIDs,
       "decLesArpRespReceiveQueueDiscards": decLesArpRespReceiveQueueDiscards,
       "decLesArpRespResourceDiscards": decLesArpRespResourceDiscards,
       "decLesNarpReqInvalidAtmAddresses": decLesNarpReqInvalidAtmAddresses,
       "decLesNarpReqInvalidLanDestinations": decLesNarpReqInvalidLanDestinations,
       "decLesNarpReqInvalidLECIDs": decLesNarpReqInvalidLECIDs,
       "decLesNarpReqReceiveQueueDiscards": decLesNarpReqReceiveQueueDiscards,
       "decLesNarpReqResourceDiscards": decLesNarpReqResourceDiscards,
       "decLesTopoReqReceiveQueueDiscards": decLesTopoReqReceiveQueueDiscards,
       "decLesTopoReqResourceDiscards": decLesTopoReqResourceDiscards,
       "decLesFlushTable": decLesFlushTable,
       "decLesFlushEntry": decLesFlushEntry,
       "decLesFlushResponsesForwarded": decLesFlushResponsesForwarded,
       "decLesFlushResponsesRejected": decLesFlushResponsesRejected,
       "decLesFlushResponsesDiscarded": decLesFlushResponsesDiscarded,
       "decLesEventLogMaximumSize": decLesEventLogMaximumSize,
       "decLesEventLogTable": decLesEventLogTable,
       "decLesEventLogEntry": decLesEventLogEntry,
       "decLesEventIndex": decLesEventIndex,
       "decLesEventType": decLesEventType,
       "decLesEventReason": decLesEventReason,
       "decLesEventServer": decLesEventServer,
       "decLesEventServerAtmAddress": decLesEventServerAtmAddress,
       "decLesEventClientAtmAddress": decLesEventClientAtmAddress,
       "decLesEventClientMacAddress": decLesEventClientMacAddress,
       "decLesEventTimestamp": decLesEventTimestamp,
       "decLesMIBConformance": decLesMIBConformance,
       "decLesMIBGroups": decLesMIBGroups,
       "decLesConfigGroup": decLesConfigGroup,
       "decLesClientStatesGroup": decLesClientStatesGroup,
       "decLesClientGroup": decLesClientGroup,
       "decLesLecGroup": decLesLecGroup,
       "decLesCircuitGroup": decLesCircuitGroup,
       "decLesMacAddressGroup": decLesMacAddressGroup,
       "decLesRouteDescrGroup": decLesRouteDescrGroup,
       "decLesTrafficGroup": decLesTrafficGroup,
       "decLesCallStatsGroup": decLesCallStatsGroup,
       "decLesJoinStatsGroup": decLesJoinStatsGroup,
       "decLesRegisterStatsGroup": decLesRegisterStatsGroup,
       "decLesArpStatsGroup": decLesArpStatsGroup,
       "decLesFlushStatsGroup": decLesFlushStatsGroup,
       "decLesEventLogGroup": decLesEventLogGroup,
       "decLesMIBCompliances": decLesMIBCompliances,
       "decLesMIBCompliance": decLesMIBCompliance}
)
