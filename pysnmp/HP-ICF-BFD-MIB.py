# SNMP MIB module (HP-ICF-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-BFD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:07 2024
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

(bfdObjects,
 bfdSessEntry) = mibBuilder.importSymbols(
    "BFD-STD-MIB",
    "bfdObjects",
    "bfdSessEntry")

(BfdIntervalTC,
 BfdMultiplierTC) = mibBuilder.importSymbols(
    "BFD-TC-STD-MIB",
    "BfdIntervalTC",
    "BfdMultiplierTC")

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(IANAbfdSessAuthenticationKeyTC,
 IANAbfdSessAuthenticationTypeTC) = mibBuilder.importSymbols(
    "IANA-BFD-TC-STD-MIB",
    "IANAbfdSessAuthenticationKeyTC",
    "IANAbfdSessAuthenticationTypeTC")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

hpicfBfd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120)
)
hpicfBfd.setRevisions(
        ("2016-11-28 10:00",
         "2010-10-28 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfBfdSessTable_Object = MibTable
hpicfBfdSessTable = _HpicfBfdSessTable_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfBfdSessTable.setStatus("current")
_HpicfBfdSessEntry_Object = MibTableRow
hpicfBfdSessEntry = _HpicfBfdSessEntry_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hpicfBfdSessEntry.setStatus("current")


class _HpicfBfdSessApplicationID_Type(Integer32):
    """Custom type hpicfBfdSessApplicationID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 3),
          ("multiple", 4),
          ("none", 0),
          ("ospf", 1),
          ("static", 5),
          ("vrrp", 2))
    )


_HpicfBfdSessApplicationID_Type.__name__ = "Integer32"
_HpicfBfdSessApplicationID_Object = MibTableColumn
hpicfBfdSessApplicationID = _HpicfBfdSessApplicationID_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 6, 1, 1),
    _HpicfBfdSessApplicationID_Type()
)
hpicfBfdSessApplicationID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBfdSessApplicationID.setStatus("current")


class _HpicfBfdSessStaus_Type(Integer32):
    """Custom type hpicfBfdSessStaus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_HpicfBfdSessStaus_Type.__name__ = "Integer32"
_HpicfBfdSessStaus_Object = MibTableColumn
hpicfBfdSessStaus = _HpicfBfdSessStaus_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 6, 1, 2),
    _HpicfBfdSessStaus_Type()
)
hpicfBfdSessStaus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBfdSessStaus.setStatus("current")


class _HpicfBfdSessClearStats_Type(TruthValue):
    """Custom type hpicfBfdSessClearStats based on TruthValue"""


_HpicfBfdSessClearStats_Object = MibTableColumn
hpicfBfdSessClearStats = _HpicfBfdSessClearStats_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 6, 1, 3),
    _HpicfBfdSessClearStats_Type()
)
hpicfBfdSessClearStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBfdSessClearStats.setStatus("current")
_HpicfBfdObjects_ObjectIdentity = ObjectIdentity
hpicfBfdObjects = _HpicfBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 1)
)
_HpicfBfdSessConfigTable_Object = MibTable
hpicfBfdSessConfigTable = _HpicfBfdSessConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfBfdSessConfigTable.setStatus("current")
_HpicfBfdSessConfigEntry_Object = MibTableRow
hpicfBfdSessConfigEntry = _HpicfBfdSessConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 1, 1, 1)
)
hpicfBfdSessConfigEntry.setIndexNames(
    (0, "HP-ICF-BFD-MIB", "hpicfBfdSessConfigIfIndex"),
)
if mibBuilder.loadTexts:
    hpicfBfdSessConfigEntry.setStatus("current")
_HpicfBfdSessConfigIfIndex_Type = InterfaceIndex
_HpicfBfdSessConfigIfIndex_Object = MibTableColumn
hpicfBfdSessConfigIfIndex = _HpicfBfdSessConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 1, 1, 1, 1),
    _HpicfBfdSessConfigIfIndex_Type()
)
hpicfBfdSessConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfBfdSessConfigIfIndex.setStatus("current")
_HpicfBfdSessConfigDesiredMinTxInterval_Type = BfdIntervalTC
_HpicfBfdSessConfigDesiredMinTxInterval_Object = MibTableColumn
hpicfBfdSessConfigDesiredMinTxInterval = _HpicfBfdSessConfigDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 1, 1, 1, 2),
    _HpicfBfdSessConfigDesiredMinTxInterval_Type()
)
hpicfBfdSessConfigDesiredMinTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBfdSessConfigDesiredMinTxInterval.setStatus("current")
_HpicfBfdSessConfigReqMinRxInterval_Type = BfdIntervalTC
_HpicfBfdSessConfigReqMinRxInterval_Object = MibTableColumn
hpicfBfdSessConfigReqMinRxInterval = _HpicfBfdSessConfigReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 1, 1, 1, 3),
    _HpicfBfdSessConfigReqMinRxInterval_Type()
)
hpicfBfdSessConfigReqMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBfdSessConfigReqMinRxInterval.setStatus("current")
_HpicfBfdSessConfigReqMinEchoRxInterval_Type = BfdIntervalTC
_HpicfBfdSessConfigReqMinEchoRxInterval_Object = MibTableColumn
hpicfBfdSessConfigReqMinEchoRxInterval = _HpicfBfdSessConfigReqMinEchoRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 1, 1, 1, 4),
    _HpicfBfdSessConfigReqMinEchoRxInterval_Type()
)
hpicfBfdSessConfigReqMinEchoRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBfdSessConfigReqMinEchoRxInterval.setStatus("current")
_HpicfBfdSessConfigDetectMult_Type = BfdMultiplierTC
_HpicfBfdSessConfigDetectMult_Object = MibTableColumn
hpicfBfdSessConfigDetectMult = _HpicfBfdSessConfigDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 1, 1, 1, 5),
    _HpicfBfdSessConfigDetectMult_Type()
)
hpicfBfdSessConfigDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBfdSessConfigDetectMult.setStatus("current")


class _HpicfBfdSessConfigAuthPresFlag_Type(TruthValue):
    """Custom type hpicfBfdSessConfigAuthPresFlag based on TruthValue"""


_HpicfBfdSessConfigAuthPresFlag_Object = MibTableColumn
hpicfBfdSessConfigAuthPresFlag = _HpicfBfdSessConfigAuthPresFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 1, 1, 1, 6),
    _HpicfBfdSessConfigAuthPresFlag_Type()
)
hpicfBfdSessConfigAuthPresFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBfdSessConfigAuthPresFlag.setStatus("current")


class _HpicfBfdSessConfigAuthenticationType_Type(IANAbfdSessAuthenticationTypeTC):
    """Custom type hpicfBfdSessConfigAuthenticationType based on IANAbfdSessAuthenticationTypeTC"""


_HpicfBfdSessConfigAuthenticationType_Object = MibTableColumn
hpicfBfdSessConfigAuthenticationType = _HpicfBfdSessConfigAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 1, 1, 1, 7),
    _HpicfBfdSessConfigAuthenticationType_Type()
)
hpicfBfdSessConfigAuthenticationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBfdSessConfigAuthenticationType.setStatus("current")


class _HpicfBfdSessConfigAuthenticationKeyID_Type(Integer32):
    """Custom type hpicfBfdSessConfigAuthenticationKeyID based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_HpicfBfdSessConfigAuthenticationKeyID_Type.__name__ = "Integer32"
_HpicfBfdSessConfigAuthenticationKeyID_Object = MibTableColumn
hpicfBfdSessConfigAuthenticationKeyID = _HpicfBfdSessConfigAuthenticationKeyID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 1, 1, 1, 8),
    _HpicfBfdSessConfigAuthenticationKeyID_Type()
)
hpicfBfdSessConfigAuthenticationKeyID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBfdSessConfigAuthenticationKeyID.setStatus("current")
_HpicfBfdSessConfigAuthenticationKey_Type = IANAbfdSessAuthenticationKeyTC
_HpicfBfdSessConfigAuthenticationKey_Object = MibTableColumn
hpicfBfdSessConfigAuthenticationKey = _HpicfBfdSessConfigAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 1, 1, 1, 9),
    _HpicfBfdSessConfigAuthenticationKey_Type()
)
hpicfBfdSessConfigAuthenticationKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBfdSessConfigAuthenticationKey.setStatus("current")
_HpicfBfdSessConfigAuthEncPwd_Type = IANAbfdSessAuthenticationKeyTC
_HpicfBfdSessConfigAuthEncPwd_Object = MibTableColumn
hpicfBfdSessConfigAuthEncPwd = _HpicfBfdSessConfigAuthEncPwd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 1, 1, 1, 10),
    _HpicfBfdSessConfigAuthEncPwd_Type()
)
hpicfBfdSessConfigAuthEncPwd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBfdSessConfigAuthEncPwd.setStatus("current")
_HpicfBfdSessConfigRowStatus_Type = RowStatus
_HpicfBfdSessConfigRowStatus_Object = MibTableColumn
hpicfBfdSessConfigRowStatus = _HpicfBfdSessConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 1, 1, 1, 11),
    _HpicfBfdSessConfigRowStatus_Type()
)
hpicfBfdSessConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBfdSessConfigRowStatus.setStatus("current")
_HpicfBfdScalarObjects_ObjectIdentity = ObjectIdentity
hpicfBfdScalarObjects = _HpicfBfdScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 1, 2)
)
_HpicfBfdEchoSrcIpAddType_Type = InetAddressType
_HpicfBfdEchoSrcIpAddType_Object = MibScalar
hpicfBfdEchoSrcIpAddType = _HpicfBfdEchoSrcIpAddType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 1, 2, 1),
    _HpicfBfdEchoSrcIpAddType_Type()
)
hpicfBfdEchoSrcIpAddType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBfdEchoSrcIpAddType.setStatus("current")
_HpicfBfdEchoSrcIpAdd_Type = InetAddress
_HpicfBfdEchoSrcIpAdd_Object = MibScalar
hpicfBfdEchoSrcIpAdd = _HpicfBfdEchoSrcIpAdd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 1, 2, 2),
    _HpicfBfdEchoSrcIpAdd_Type()
)
hpicfBfdEchoSrcIpAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBfdEchoSrcIpAdd.setStatus("current")
_HpicfBfdConformance_ObjectIdentity = ObjectIdentity
hpicfBfdConformance = _HpicfBfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 2)
)
_HpicfBfdGroups_ObjectIdentity = ObjectIdentity
hpicfBfdGroups = _HpicfBfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 2, 1)
)
_HpicfBfdCompliances_ObjectIdentity = ObjectIdentity
hpicfBfdCompliances = _HpicfBfdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 2, 2)
)
bfdSessEntry.registerAugmentions(
    ("HP-ICF-BFD-MIB",
     "hpicfBfdSessEntry")
)
hpicfBfdSessEntry.setIndexNames(*bfdSessEntry.getIndexNames())

# Managed Objects groups

hpicfBfdSessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 2, 1, 1)
)
hpicfBfdSessGroup.setObjects(
      *(("HP-ICF-BFD-MIB", "hpicfBfdSessConfigDesiredMinTxInterval"),
        ("HP-ICF-BFD-MIB", "hpicfBfdSessConfigReqMinRxInterval"),
        ("HP-ICF-BFD-MIB", "hpicfBfdSessConfigReqMinEchoRxInterval"),
        ("HP-ICF-BFD-MIB", "hpicfBfdSessConfigDetectMult"),
        ("HP-ICF-BFD-MIB", "hpicfBfdSessConfigAuthPresFlag"),
        ("HP-ICF-BFD-MIB", "hpicfBfdSessConfigAuthenticationType"),
        ("HP-ICF-BFD-MIB", "hpicfBfdSessConfigAuthenticationKeyID"),
        ("HP-ICF-BFD-MIB", "hpicfBfdSessConfigAuthenticationKey"),
        ("HP-ICF-BFD-MIB", "hpicfBfdSessConfigAuthEncPwd"),
        ("HP-ICF-BFD-MIB", "hpicfBfdSessConfigRowStatus"),
        ("HP-ICF-BFD-MIB", "hpicfBfdSessApplicationID"),
        ("HP-ICF-BFD-MIB", "hpicfBfdSessStaus"),
        ("HP-ICF-BFD-MIB", "hpicfBfdSessClearStats"))
)
if mibBuilder.loadTexts:
    hpicfBfdSessGroup.setStatus("current")

hpicfBfdScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 2, 1, 2)
)
hpicfBfdScalarGroup.setObjects(
      *(("HP-ICF-BFD-MIB", "hpicfBfdEchoSrcIpAddType"),
        ("HP-ICF-BFD-MIB", "hpicfBfdEchoSrcIpAdd"))
)
if mibBuilder.loadTexts:
    hpicfBfdScalarGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfBfdCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfBfdCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-BFD-MIB",
    **{"hpicfBfdSessTable": hpicfBfdSessTable,
       "hpicfBfdSessEntry": hpicfBfdSessEntry,
       "hpicfBfdSessApplicationID": hpicfBfdSessApplicationID,
       "hpicfBfdSessStaus": hpicfBfdSessStaus,
       "hpicfBfdSessClearStats": hpicfBfdSessClearStats,
       "hpicfBfd": hpicfBfd,
       "hpicfBfdObjects": hpicfBfdObjects,
       "hpicfBfdSessConfigTable": hpicfBfdSessConfigTable,
       "hpicfBfdSessConfigEntry": hpicfBfdSessConfigEntry,
       "hpicfBfdSessConfigIfIndex": hpicfBfdSessConfigIfIndex,
       "hpicfBfdSessConfigDesiredMinTxInterval": hpicfBfdSessConfigDesiredMinTxInterval,
       "hpicfBfdSessConfigReqMinRxInterval": hpicfBfdSessConfigReqMinRxInterval,
       "hpicfBfdSessConfigReqMinEchoRxInterval": hpicfBfdSessConfigReqMinEchoRxInterval,
       "hpicfBfdSessConfigDetectMult": hpicfBfdSessConfigDetectMult,
       "hpicfBfdSessConfigAuthPresFlag": hpicfBfdSessConfigAuthPresFlag,
       "hpicfBfdSessConfigAuthenticationType": hpicfBfdSessConfigAuthenticationType,
       "hpicfBfdSessConfigAuthenticationKeyID": hpicfBfdSessConfigAuthenticationKeyID,
       "hpicfBfdSessConfigAuthenticationKey": hpicfBfdSessConfigAuthenticationKey,
       "hpicfBfdSessConfigAuthEncPwd": hpicfBfdSessConfigAuthEncPwd,
       "hpicfBfdSessConfigRowStatus": hpicfBfdSessConfigRowStatus,
       "hpicfBfdScalarObjects": hpicfBfdScalarObjects,
       "hpicfBfdEchoSrcIpAddType": hpicfBfdEchoSrcIpAddType,
       "hpicfBfdEchoSrcIpAdd": hpicfBfdEchoSrcIpAdd,
       "hpicfBfdConformance": hpicfBfdConformance,
       "hpicfBfdGroups": hpicfBfdGroups,
       "hpicfBfdSessGroup": hpicfBfdSessGroup,
       "hpicfBfdScalarGroup": hpicfBfdScalarGroup,
       "hpicfBfdCompliances": hpicfBfdCompliances,
       "hpicfBfdCompliance": hpicfBfdCompliance}
)
