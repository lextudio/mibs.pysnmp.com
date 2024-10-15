# SNMP MIB module (OASUBSCR-CFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OASUBSCR-CFG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:35 2024
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



class SubscriberName(DisplayString):
    """Custom type SubscriberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 35),
    )





class DirectionType(Integer32):
    """Custom type DirectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egress", 3),
          ("ingress", 2),
          ("other", 1))
    )





class AccountCouter(Counter32):
    """Custom type AccountCouter based on Counter32"""




class AccountCounter64(Counter64):
    """Custom type AccountCounter64 based on Counter64"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_NbSwitchG1_ObjectIdentity = ObjectIdentity
nbSwitchG1 = _NbSwitchG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1)
)
_NbSwitchG1Il_ObjectIdentity = ObjectIdentity
nbSwitchG1Il = _NbSwitchG1Il_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50)
)
_OaSubscriberConfig_ObjectIdentity = ObjectIdentity
oaSubscriberConfig = _OaSubscriberConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15)
)
_OaSubscrConfigGen_ObjectIdentity = ObjectIdentity
oaSubscrConfigGen = _OaSubscrConfigGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 1)
)
_OaSubscrAccounting_ObjectIdentity = ObjectIdentity
oaSubscrAccounting = _OaSubscrAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6)
)
_OaSubscrAccNameTable_Object = MibTable
oaSubscrAccNameTable = _OaSubscrAccNameTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10)
)
if mibBuilder.loadTexts:
    oaSubscrAccNameTable.setStatus("mandatory")
_OaSubscrAccNameEntry_Object = MibTableRow
oaSubscrAccNameEntry = _OaSubscrAccNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1)
)
oaSubscrAccNameEntry.setIndexNames(
    (0, "OASUBSCR-CFG-MIB", "oaSubscrName"),
    (0, "OASUBSCR-CFG-MIB", "oaSubscrDirection"),
)
if mibBuilder.loadTexts:
    oaSubscrAccNameEntry.setStatus("mandatory")
_OaSubscrName_Type = SubscriberName
_OaSubscrName_Object = MibTableColumn
oaSubscrName = _OaSubscrName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 1),
    _OaSubscrName_Type()
)
oaSubscrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSubscrName.setStatus("mandatory")
_OaSubscrDirection_Type = DirectionType
_OaSubscrDirection_Object = MibTableColumn
oaSubscrDirection = _OaSubscrDirection_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 2),
    _OaSubscrDirection_Type()
)
oaSubscrDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSubscrDirection.setStatus("mandatory")


class _OaSubscrAccNmAdminStatus_Type(Integer32):
    """Custom type oaSubscrAccNmAdminStatus based on Integer32"""
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
        *(("clear", 6),
          ("disable", 3),
          ("enable", 2),
          ("other", 1),
          ("pause", 4),
          ("resume", 5))
    )


_OaSubscrAccNmAdminStatus_Type.__name__ = "Integer32"
_OaSubscrAccNmAdminStatus_Object = MibTableColumn
oaSubscrAccNmAdminStatus = _OaSubscrAccNmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 3),
    _OaSubscrAccNmAdminStatus_Type()
)
oaSubscrAccNmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSubscrAccNmAdminStatus.setStatus("mandatory")


class _OaSubscrAccNmOperStatus_Type(Integer32):
    """Custom type oaSubscrAccNmOperStatus based on Integer32"""
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
        *(("active", 2),
          ("disabled", 4),
          ("other", 1),
          ("paused", 3))
    )


_OaSubscrAccNmOperStatus_Type.__name__ = "Integer32"
_OaSubscrAccNmOperStatus_Object = MibTableColumn
oaSubscrAccNmOperStatus = _OaSubscrAccNmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 4),
    _OaSubscrAccNmOperStatus_Type()
)
oaSubscrAccNmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSubscrAccNmOperStatus.setStatus("mandatory")
_OaSubscrAccNmConformingBytes_Type = AccountCouter
_OaSubscrAccNmConformingBytes_Object = MibTableColumn
oaSubscrAccNmConformingBytes = _OaSubscrAccNmConformingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 6),
    _OaSubscrAccNmConformingBytes_Type()
)
oaSubscrAccNmConformingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSubscrAccNmConformingBytes.setStatus("mandatory")
_OaSubscrAccNmHighConformingBytes_Type = Counter32
_OaSubscrAccNmHighConformingBytes_Object = MibTableColumn
oaSubscrAccNmHighConformingBytes = _OaSubscrAccNmHighConformingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 7),
    _OaSubscrAccNmHighConformingBytes_Type()
)
oaSubscrAccNmHighConformingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSubscrAccNmHighConformingBytes.setStatus("mandatory")
_OaSubscrAccNmLowConformingBytes_Type = Counter32
_OaSubscrAccNmLowConformingBytes_Object = MibTableColumn
oaSubscrAccNmLowConformingBytes = _OaSubscrAccNmLowConformingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 8),
    _OaSubscrAccNmLowConformingBytes_Type()
)
oaSubscrAccNmLowConformingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSubscrAccNmLowConformingBytes.setStatus("mandatory")
_OaSubscrAccNmExceedingBytes_Type = AccountCouter
_OaSubscrAccNmExceedingBytes_Object = MibTableColumn
oaSubscrAccNmExceedingBytes = _OaSubscrAccNmExceedingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 9),
    _OaSubscrAccNmExceedingBytes_Type()
)
oaSubscrAccNmExceedingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSubscrAccNmExceedingBytes.setStatus("mandatory")
_OaSubscrAccNmHighExceedingBytes_Type = Counter32
_OaSubscrAccNmHighExceedingBytes_Object = MibTableColumn
oaSubscrAccNmHighExceedingBytes = _OaSubscrAccNmHighExceedingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 10),
    _OaSubscrAccNmHighExceedingBytes_Type()
)
oaSubscrAccNmHighExceedingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSubscrAccNmHighExceedingBytes.setStatus("mandatory")
_OaSubscrAccNmLowExceedingBytes_Type = Counter32
_OaSubscrAccNmLowExceedingBytes_Object = MibTableColumn
oaSubscrAccNmLowExceedingBytes = _OaSubscrAccNmLowExceedingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 11),
    _OaSubscrAccNmLowExceedingBytes_Type()
)
oaSubscrAccNmLowExceedingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSubscrAccNmLowExceedingBytes.setStatus("mandatory")
_OaSubscrAccNmConformingPackets_Type = AccountCouter
_OaSubscrAccNmConformingPackets_Object = MibTableColumn
oaSubscrAccNmConformingPackets = _OaSubscrAccNmConformingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 12),
    _OaSubscrAccNmConformingPackets_Type()
)
oaSubscrAccNmConformingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSubscrAccNmConformingPackets.setStatus("mandatory")
_OaSubscrAccNmHighConformingPackets_Type = Counter32
_OaSubscrAccNmHighConformingPackets_Object = MibTableColumn
oaSubscrAccNmHighConformingPackets = _OaSubscrAccNmHighConformingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 13),
    _OaSubscrAccNmHighConformingPackets_Type()
)
oaSubscrAccNmHighConformingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSubscrAccNmHighConformingPackets.setStatus("mandatory")
_OaSubscrAccNmLowConformingPackets_Type = Counter32
_OaSubscrAccNmLowConformingPackets_Object = MibTableColumn
oaSubscrAccNmLowConformingPackets = _OaSubscrAccNmLowConformingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 14),
    _OaSubscrAccNmLowConformingPackets_Type()
)
oaSubscrAccNmLowConformingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSubscrAccNmLowConformingPackets.setStatus("mandatory")
_OaSubscrAccNmExceedingPackets_Type = AccountCouter
_OaSubscrAccNmExceedingPackets_Object = MibTableColumn
oaSubscrAccNmExceedingPackets = _OaSubscrAccNmExceedingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 15),
    _OaSubscrAccNmExceedingPackets_Type()
)
oaSubscrAccNmExceedingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSubscrAccNmExceedingPackets.setStatus("mandatory")
_OaSubscrAccNmHighExceedingPackets_Type = Counter32
_OaSubscrAccNmHighExceedingPackets_Object = MibTableColumn
oaSubscrAccNmHighExceedingPackets = _OaSubscrAccNmHighExceedingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 16),
    _OaSubscrAccNmHighExceedingPackets_Type()
)
oaSubscrAccNmHighExceedingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSubscrAccNmHighExceedingPackets.setStatus("mandatory")
_OaSubscrAccNmLowExceedingPackets_Type = Counter32
_OaSubscrAccNmLowExceedingPackets_Object = MibTableColumn
oaSubscrAccNmLowExceedingPackets = _OaSubscrAccNmLowExceedingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 17),
    _OaSubscrAccNmLowExceedingPackets_Type()
)
oaSubscrAccNmLowExceedingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSubscrAccNmLowExceedingPackets.setStatus("mandatory")
_OaSubscrAccNm64ConformingBytes_Type = AccountCounter64
_OaSubscrAccNm64ConformingBytes_Object = MibTableColumn
oaSubscrAccNm64ConformingBytes = _OaSubscrAccNm64ConformingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 18),
    _OaSubscrAccNm64ConformingBytes_Type()
)
oaSubscrAccNm64ConformingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSubscrAccNm64ConformingBytes.setStatus("mandatory")
_OaSubscrAccNm64ExceedingBytes_Type = AccountCounter64
_OaSubscrAccNm64ExceedingBytes_Object = MibTableColumn
oaSubscrAccNm64ExceedingBytes = _OaSubscrAccNm64ExceedingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 19),
    _OaSubscrAccNm64ExceedingBytes_Type()
)
oaSubscrAccNm64ExceedingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSubscrAccNm64ExceedingBytes.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OASUBSCR-CFG-MIB",
    **{"SubscriberName": SubscriberName,
       "DirectionType": DirectionType,
       "AccountCouter": AccountCouter,
       "AccountCounter64": AccountCounter64,
       "nbase": nbase,
       "nbSwitchG1": nbSwitchG1,
       "nbSwitchG1Il": nbSwitchG1Il,
       "oaSubscriberConfig": oaSubscriberConfig,
       "oaSubscrConfigGen": oaSubscrConfigGen,
       "oaSubscrAccounting": oaSubscrAccounting,
       "oaSubscrAccNameTable": oaSubscrAccNameTable,
       "oaSubscrAccNameEntry": oaSubscrAccNameEntry,
       "oaSubscrName": oaSubscrName,
       "oaSubscrDirection": oaSubscrDirection,
       "oaSubscrAccNmAdminStatus": oaSubscrAccNmAdminStatus,
       "oaSubscrAccNmOperStatus": oaSubscrAccNmOperStatus,
       "oaSubscrAccNmConformingBytes": oaSubscrAccNmConformingBytes,
       "oaSubscrAccNmHighConformingBytes": oaSubscrAccNmHighConformingBytes,
       "oaSubscrAccNmLowConformingBytes": oaSubscrAccNmLowConformingBytes,
       "oaSubscrAccNmExceedingBytes": oaSubscrAccNmExceedingBytes,
       "oaSubscrAccNmHighExceedingBytes": oaSubscrAccNmHighExceedingBytes,
       "oaSubscrAccNmLowExceedingBytes": oaSubscrAccNmLowExceedingBytes,
       "oaSubscrAccNmConformingPackets": oaSubscrAccNmConformingPackets,
       "oaSubscrAccNmHighConformingPackets": oaSubscrAccNmHighConformingPackets,
       "oaSubscrAccNmLowConformingPackets": oaSubscrAccNmLowConformingPackets,
       "oaSubscrAccNmExceedingPackets": oaSubscrAccNmExceedingPackets,
       "oaSubscrAccNmHighExceedingPackets": oaSubscrAccNmHighExceedingPackets,
       "oaSubscrAccNmLowExceedingPackets": oaSubscrAccNmLowExceedingPackets,
       "oaSubscrAccNm64ConformingBytes": oaSubscrAccNm64ConformingBytes,
       "oaSubscrAccNm64ExceedingBytes": oaSubscrAccNm64ExceedingBytes}
)
