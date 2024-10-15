# SNMP MIB module (CTRON-ELAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-ELAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:46 2024
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

(ctAtmfLanEmulation,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctAtmfLanEmulation")

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



class CtLaneDebugLevel(Integer32):
    """Custom type CtLaneDebugLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("detailed", 6),
          ("error", 3),
          ("informational", 5),
          ("trace", 7),
          ("user", 1),
          ("warning", 4))
    )





class ElanLocalIndex(Integer32):
    """Custom type ElanLocalIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtLeClient_ObjectIdentity = ObjectIdentity
ctLeClient = _CtLeClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 1)
)
_CtElan_ObjectIdentity = ObjectIdentity
ctElan = _CtElan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2)
)
_CtElanConfGroup_ObjectIdentity = ObjectIdentity
ctElanConfGroup = _CtElanConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1)
)
_CtElanConfTable_Object = MibTable
ctElanConfTable = _CtElanConfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ctElanConfTable.setStatus("mandatory")
_CtElanConfEntry_Object = MibTableRow
ctElanConfEntry = _CtElanConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 1, 1)
)
ctElanConfEntry.setIndexNames(
    (0, "CTRON-ELAN-MIB", "ctElanConfIndex"),
)
if mibBuilder.loadTexts:
    ctElanConfEntry.setStatus("mandatory")
_CtElanConfIndex_Type = ElanLocalIndex
_CtElanConfIndex_Object = MibTableColumn
ctElanConfIndex = _CtElanConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 1, 1, 1),
    _CtElanConfIndex_Type()
)
ctElanConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctElanConfIndex.setStatus("mandatory")


class _CtElanConfUnitNumber_Type(Integer32):
    """Custom type ctElanConfUnitNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_CtElanConfUnitNumber_Type.__name__ = "Integer32"
_CtElanConfUnitNumber_Object = MibTableColumn
ctElanConfUnitNumber = _CtElanConfUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 1, 1, 2),
    _CtElanConfUnitNumber_Type()
)
ctElanConfUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctElanConfUnitNumber.setStatus("mandatory")


class _CtElanConfPolicy_Type(Integer32):
    """Custom type ctElanConfPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonsecure", 2),
          ("secure", 1))
    )


_CtElanConfPolicy_Type.__name__ = "Integer32"
_CtElanConfPolicy_Object = MibTableColumn
ctElanConfPolicy = _CtElanConfPolicy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 1, 1, 3),
    _CtElanConfPolicy_Type()
)
ctElanConfPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctElanConfPolicy.setStatus("mandatory")


class _CtElanConfDelPolicyWithElan_Type(Integer32):
    """Custom type ctElanConfDelPolicyWithElan based on Integer32"""
    defaultValue = 1

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


_CtElanConfDelPolicyWithElan_Type.__name__ = "Integer32"
_CtElanConfDelPolicyWithElan_Object = MibTableColumn
ctElanConfDelPolicyWithElan = _CtElanConfDelPolicyWithElan_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 1, 1, 4),
    _CtElanConfDelPolicyWithElan_Type()
)
ctElanConfDelPolicyWithElan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctElanConfDelPolicyWithElan.setStatus("mandatory")


class _CtElanConfRowStatus_Type(Integer32):
    """Custom type ctElanConfRowStatus based on Integer32"""
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


_CtElanConfRowStatus_Type.__name__ = "Integer32"
_CtElanConfRowStatus_Object = MibTableColumn
ctElanConfRowStatus = _CtElanConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 1, 1, 5),
    _CtElanConfRowStatus_Type()
)
ctElanConfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctElanConfRowStatus.setStatus("mandatory")
_CtElanSFDSPeerTable_Object = MibTable
ctElanSFDSPeerTable = _CtElanSFDSPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ctElanSFDSPeerTable.setStatus("mandatory")
_CtElanSFDSPeerEntry_Object = MibTableRow
ctElanSFDSPeerEntry = _CtElanSFDSPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 2, 1)
)
ctElanSFDSPeerEntry.setIndexNames(
    (0, "CTRON-ELAN-MIB", "ctElanSFDSPeerIP"),
)
if mibBuilder.loadTexts:
    ctElanSFDSPeerEntry.setStatus("mandatory")
_CtElanSFDSPeerIP_Type = IpAddress
_CtElanSFDSPeerIP_Object = MibTableColumn
ctElanSFDSPeerIP = _CtElanSFDSPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 2, 1, 1),
    _CtElanSFDSPeerIP_Type()
)
ctElanSFDSPeerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctElanSFDSPeerIP.setStatus("mandatory")


class _CtElanSFDSPeerRowStatus_Type(Integer32):
    """Custom type ctElanSFDSPeerRowStatus based on Integer32"""
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


_CtElanSFDSPeerRowStatus_Type.__name__ = "Integer32"
_CtElanSFDSPeerRowStatus_Object = MibTableColumn
ctElanSFDSPeerRowStatus = _CtElanSFDSPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 2, 1, 2),
    _CtElanSFDSPeerRowStatus_Type()
)
ctElanSFDSPeerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctElanSFDSPeerRowStatus.setStatus("mandatory")
_CtElanConfDirectoryServicesIP_Type = IpAddress
_CtElanConfDirectoryServicesIP_Object = MibScalar
ctElanConfDirectoryServicesIP = _CtElanConfDirectoryServicesIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 3),
    _CtElanConfDirectoryServicesIP_Type()
)
ctElanConfDirectoryServicesIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctElanConfDirectoryServicesIP.setStatus("mandatory")


class _CtElanDSStatus_Type(Integer32):
    """Custom type ctElanDSStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("connectionLost", 2),
          ("unknown", 3))
    )


_CtElanDSStatus_Type.__name__ = "Integer32"
_CtElanDSStatus_Object = MibScalar
ctElanDSStatus = _CtElanDSStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 4),
    _CtElanDSStatus_Type()
)
ctElanDSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctElanDSStatus.setStatus("mandatory")


class _CtElanUNIVersion_Type(Integer32):
    """Custom type ctElanUNIVersion based on Integer32"""
    defaultValue = 1

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
        *(("uni30", 2),
          ("uni31", 3),
          ("uni40", 4),
          ("unknown", 1))
    )


_CtElanUNIVersion_Type.__name__ = "Integer32"
_CtElanUNIVersion_Object = MibScalar
ctElanUNIVersion = _CtElanUNIVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 5),
    _CtElanUNIVersion_Type()
)
ctElanUNIVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctElanUNIVersion.setStatus("mandatory")


class _CtElanLaneDbgOutputFile_Type(DisplayString):
    """Custom type ctElanLaneDbgOutputFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CtElanLaneDbgOutputFile_Type.__name__ = "DisplayString"
_CtElanLaneDbgOutputFile_Object = MibScalar
ctElanLaneDbgOutputFile = _CtElanLaneDbgOutputFile_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 6),
    _CtElanLaneDbgOutputFile_Type()
)
ctElanLaneDbgOutputFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctElanLaneDbgOutputFile.setStatus("mandatory")


class _CtElanLaneDbgConnectionServices_Type(CtLaneDebugLevel):
    """Custom type ctElanLaneDbgConnectionServices based on CtLaneDebugLevel"""


_CtElanLaneDbgConnectionServices_Object = MibScalar
ctElanLaneDbgConnectionServices = _CtElanLaneDbgConnectionServices_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 7),
    _CtElanLaneDbgConnectionServices_Type()
)
ctElanLaneDbgConnectionServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctElanLaneDbgConnectionServices.setStatus("mandatory")


class _CtElanLaneDbgDatabaseManagement_Type(CtLaneDebugLevel):
    """Custom type ctElanLaneDbgDatabaseManagement based on CtLaneDebugLevel"""


_CtElanLaneDbgDatabaseManagement_Object = MibScalar
ctElanLaneDbgDatabaseManagement = _CtElanLaneDbgDatabaseManagement_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 8),
    _CtElanLaneDbgDatabaseManagement_Type()
)
ctElanLaneDbgDatabaseManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctElanLaneDbgDatabaseManagement.setStatus("mandatory")


class _CtElanCtLaneDbgSNMP_Type(CtLaneDebugLevel):
    """Custom type ctElanCtLaneDbgSNMP based on CtLaneDebugLevel"""


_CtElanCtLaneDbgSNMP_Object = MibScalar
ctElanCtLaneDbgSNMP = _CtElanCtLaneDbgSNMP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 9),
    _CtElanCtLaneDbgSNMP_Type()
)
ctElanCtLaneDbgSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctElanCtLaneDbgSNMP.setStatus("mandatory")


class _CtElanLaneDbgLECS_Type(CtLaneDebugLevel):
    """Custom type ctElanLaneDbgLECS based on CtLaneDebugLevel"""


_CtElanLaneDbgLECS_Object = MibScalar
ctElanLaneDbgLECS = _CtElanLaneDbgLECS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 10),
    _CtElanLaneDbgLECS_Type()
)
ctElanLaneDbgLECS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctElanLaneDbgLECS.setStatus("mandatory")


class _CtElanCtLaneDbgLES_Type(CtLaneDebugLevel):
    """Custom type ctElanCtLaneDbgLES based on CtLaneDebugLevel"""


_CtElanCtLaneDbgLES_Object = MibScalar
ctElanCtLaneDbgLES = _CtElanCtLaneDbgLES_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 11),
    _CtElanCtLaneDbgLES_Type()
)
ctElanCtLaneDbgLES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctElanCtLaneDbgLES.setStatus("mandatory")


class _CtElanHotStandbyStatus_Type(Integer32):
    """Custom type ctElanHotStandbyStatus based on Integer32"""
    defaultValue = 4

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
          ("initial", 1),
          ("standby", 3),
          ("unknown", 4))
    )


_CtElanHotStandbyStatus_Type.__name__ = "Integer32"
_CtElanHotStandbyStatus_Object = MibScalar
ctElanHotStandbyStatus = _CtElanHotStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 12),
    _CtElanHotStandbyStatus_Type()
)
ctElanHotStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctElanHotStandbyStatus.setStatus("mandatory")
_CtElanConfHotStandbyIP_Type = IpAddress
_CtElanConfHotStandbyIP_Object = MibScalar
ctElanConfHotStandbyIP = _CtElanConfHotStandbyIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2, 1, 13),
    _CtElanConfHotStandbyIP_Type()
)
ctElanConfHotStandbyIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctElanConfHotStandbyIP.setStatus("mandatory")
_CtLes_ObjectIdentity = ObjectIdentity
ctLes = _CtLes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 3)
)
_CtBus_ObjectIdentity = ObjectIdentity
ctBus = _CtBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-ELAN-MIB",
    **{"CtLaneDebugLevel": CtLaneDebugLevel,
       "ElanLocalIndex": ElanLocalIndex,
       "ctLeClient": ctLeClient,
       "ctElan": ctElan,
       "ctElanConfGroup": ctElanConfGroup,
       "ctElanConfTable": ctElanConfTable,
       "ctElanConfEntry": ctElanConfEntry,
       "ctElanConfIndex": ctElanConfIndex,
       "ctElanConfUnitNumber": ctElanConfUnitNumber,
       "ctElanConfPolicy": ctElanConfPolicy,
       "ctElanConfDelPolicyWithElan": ctElanConfDelPolicyWithElan,
       "ctElanConfRowStatus": ctElanConfRowStatus,
       "ctElanSFDSPeerTable": ctElanSFDSPeerTable,
       "ctElanSFDSPeerEntry": ctElanSFDSPeerEntry,
       "ctElanSFDSPeerIP": ctElanSFDSPeerIP,
       "ctElanSFDSPeerRowStatus": ctElanSFDSPeerRowStatus,
       "ctElanConfDirectoryServicesIP": ctElanConfDirectoryServicesIP,
       "ctElanDSStatus": ctElanDSStatus,
       "ctElanUNIVersion": ctElanUNIVersion,
       "ctElanLaneDbgOutputFile": ctElanLaneDbgOutputFile,
       "ctElanLaneDbgConnectionServices": ctElanLaneDbgConnectionServices,
       "ctElanLaneDbgDatabaseManagement": ctElanLaneDbgDatabaseManagement,
       "ctElanCtLaneDbgSNMP": ctElanCtLaneDbgSNMP,
       "ctElanLaneDbgLECS": ctElanLaneDbgLECS,
       "ctElanCtLaneDbgLES": ctElanCtLaneDbgLES,
       "ctElanHotStandbyStatus": ctElanHotStandbyStatus,
       "ctElanConfHotStandbyIP": ctElanConfHotStandbyIP,
       "ctLes": ctLes,
       "ctBus": ctBus}
)
